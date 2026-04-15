# bot_whatsapp_purificador_menu.py
# -*- coding: utf-8 -*-

import re
import time
import logging
import unicodedata
from dataclasses import dataclass
from typing import Dict, List, Tuple, Optional

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================================================
# CONFIGURAÇÃO
# =========================================================

WHATSAPP_WEB_URL = "https://web.whatsapp.com/"
POLL_INTERVAL_SECONDS = 3

# Números autorizados com DDI + DDD + número, apenas dígitos
# Exemplo: 5541999999999
CONTATOS_AUTORIZADOS = {
    "5541997069783",
    "5541999496865",
}

LOG_ARQUIVO = "bot_whatsapp.log"

MENU_INICIAL = (
    "Olá! Sou o assistente da loja de purificadores.\n"
    "Digite uma opção:\n"
    "1 - Horário de atendimento\n"
    "2 - Endereço\n"
    "3 - Modelos\n"
    "4 - Preço\n"
    "5 - Instalação\n"
    "6 - Manutenção\n"
    "7 - Refil\n"
    "8 - Garantia\n"
    "9 - Pagamento\n"
    "10 - Entrega\n"
    "11 - Falar com atendente\n"
)

RESPOSTA_PADRAO = "Não entendi. Digite uma opção do menu ou escreva sua dúvida."
ENCERRAMENTO = "Obrigado pelo contato."

RESPOSTAS = {
    "1": "Atendemos de segunda a sexta, das 8h30 às 18h, e sábado das 9h00 às 12h.",
    "2": "Nossa loja fica na Rua X, número Y.",
    "3": "Temos modelos de parede, bancada e com refrigeração.",
    "4": "Os valores variam conforme o modelo.",
    "5": "Sim, realizamos instalação.",
    "6": "Fazemos manutenção preventiva e corretiva.",
    "7": "A troca do refil depende do uso, em média a cada 6 meses.",
    "8": "Nossos produtos possuem garantia de fábrica.",
    "9": "Aceitamos PIX, cartão e parcelamento.",
    "10": "Realizamos entrega em várias regiões.",
    "11": "Vou encaminhar para um atendente humano.",
}

INTENTS: List[Tuple[str, List[str]]] = [
    ("1", ["horário", "horas", "fecha", "abre", "funciona", "atendimento"]),
    ("2", ["endereço", "endereco", "onde fica", "localização", "localizacao"]),
    ("3", ["marca", "tipos", "modelos", "quais purificadores", "catálogo", "catalogo", "produtos"]),
    ("4", ["preço", "preco", "valor", "custa", "quanto", "caro", "barato"]),
    ("5", ["instalação", "instalacao", "instalar", "instalam",  "montagem"]),
    ("6", ["manutenção", "manutencao", "assistência", "assistencia", "conserto", "reparo", "estrago"]),
    ("7", ["refil", "filtro", "troca do filtro", "troca de filtro"]),
    ("8", ["garantia", "defeito", "troca", "quebrou", "estragou"]),
    ("9", ["pagamento", "cartão", "cartao", "pix", "parcelamento"]),
    ("10", ["entrega", "frete", "prazo"]),
    ("11", ["atendente", "humano", "vendedor", "pessoa"]),
]

AFIRMATIVAS = {"sim", "s", "claro", "quero", "pode", "ok", "continuar"}
NEGATIVAS = {"nao", "não", "n", "obrigado", "obrigada", "sair", "encerrar", "parar"}


# =========================================================
# LOGGING
# =========================================================

def configurar_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(LOG_ARQUIVO, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )


# =========================================================
# UTILITÁRIOS
# =========================================================

def normalize_text(text: str) -> str:
    if not text:
        return ""
    text = text.lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = " ".join(text.split())
    return text


def normalize_phone(phone: str) -> str:
    return re.sub(r"\D", "", phone or "")


def extract_phone_from_text(text: str) -> Optional[str]:
    """
    Tenta extrair telefone do texto.
    Retorna apenas dígitos, se houver algo com cara de número válido.
    """
    if not text:
        return None

    patterns = [
        r"(\+?55\s*\(?\d{2}\)?\s*9?\d{4}-?\d{4})",
        r"(\(?\d{2}\)?\s*9?\d{4}-?\d{4})",
        r"(\+?\d{10,13})",
    ]

    for pattern in patterns:
        m = re.search(pattern, text)
        if m:
            digits = normalize_phone(m.group(1))
            if 10 <= len(digits) <= 13:
                return digits

    digits = normalize_phone(text)
    if 10 <= len(digits) <= 13:
        return digits

    return None


def contains_any(text: str, phrases: List[str]) -> bool:
    t = normalize_text(text)
    return any(normalize_text(p) in t for p in phrases)


def detectar_opcao_mensagem(message: str) -> Optional[str]:
    """
    Se o usuário digitar diretamente '1', '2', etc., retorna a opção.
    Caso contrário, tenta inferir pela palavra-chave.
    """
    msg = normalize_text(message)

    if msg in RESPOSTAS:
        return msg

    for opcao, keywords in INTENTS:
        if contains_any(msg, keywords):
            return opcao

    return None


# =========================================================
# ESTADO
# =========================================================

@dataclass
class ContactState:
    last_processed_message: str = ""
    awaiting_menu: bool = True
    awaiting_more_help: bool = False


# =========================================================
# BOT
# =========================================================

class WhatsAppFAQBot:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.states: Dict[str, ContactState] = {}

    def start_browser(self):
        options = Options()
        options.add_argument("--user-data-dir=./chrome_profile")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 25)
        self.driver.get(WHATSAPP_WEB_URL)

        print("Abra o WhatsApp Web e faça login, se necessário.")
        print("Aguardando carregar...")

        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='grid' or @aria-label='Lista de conversas']")
            )
        )

        print("WhatsApp Web pronto.")
        logging.info("WhatsApp Web carregado com sucesso.")

    def get_conversation_rows(self):
        grid = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='grid' or @aria-label='Lista de conversas']")
            )
        )
        return grid.find_elements(By.XPATH, ".//div[@role='row']")

    def open_conversation_by_row(self, row) -> bool:
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", row)
            time.sleep(0.2)
            row.click()
            time.sleep(0.8)
            return True
        except Exception as e:
            logging.exception("Erro ao abrir conversa: %s", e)
            return False

    def get_chat_title_text(self) -> str:
        selectors = [
            (By.XPATH, "//header//span[@title]"),
            (By.XPATH, "//header//span[@dir='auto']"),
        ]

        for by, sel in selectors:
            try:
                els = self.driver.find_elements(by, sel)
                for el in els:
                    txt = (el.get_attribute("title") or el.text or "").strip()
                    if txt:
                        return txt
            except Exception:
                pass

        return ""

    def get_current_phone(self) -> Optional[str]:
        title = self.get_chat_title_text()
        return extract_phone_from_text(title)

    def get_last_incoming_message(self) -> str:
        try:
            incoming_messages = self.driver.find_elements(
                By.CSS_SELECTOR,
                "div.message-in span.selectable-text"
            )
            if not incoming_messages:
                return ""
            return incoming_messages[-1].text.strip()
        except Exception:
            return ""

    def send_message(self, message: str):
        try:
            box = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//footer//div[@contenteditable='true' and (@role='textbox' or @data-tab='10' or @data-tab='9')]"
                    )
                )
            )
            box.click()
            box.send_keys(message)
            box.send_keys(Keys.ENTER)
            time.sleep(0.7)
        except Exception as e:
            logging.exception("Erro ao enviar mensagem: %s", e)

    def is_authorized_phone(self, phone: Optional[str]) -> bool:
        if not phone:
            return False
        return normalize_phone(phone) in CONTATOS_AUTORIZADOS

    def responder(self, phone: str, incoming_text: str) -> str:
        state = self.states.setdefault(phone, ContactState())
        msg = normalize_text(incoming_text)

        logging.info("Mensagem recebida de %s: %s", phone, incoming_text)

        # Primeira interação: envia menu
        if state.awaiting_menu:
            state.awaiting_menu = False
            state.awaiting_more_help = True
            return MENU_INICIAL

        # Respostas de continuidade
        if state.awaiting_more_help and msg in AFIRMATIVAS:
            return MENU_INICIAL

        if state.awaiting_more_help and msg in NEGATIVAS:
            state.awaiting_more_help = False
            return ENCERRAMENTO

        # Opção numérica
        opcao = detectar_opcao_mensagem(incoming_text)

        if opcao and opcao in RESPOSTAS:
            state.awaiting_more_help = True
            return f"{RESPOSTAS[opcao]}\n\n{MENSAGEM_CONTINUAR}"

        # Fallback
        state.awaiting_more_help = True
        return f"{RESPOSTA_PADRAO}\n\n{MENSAGEM_CONTINUAR}"

    def process_visible_conversations(self):
        rows = self.get_conversation_rows()

        for row in rows:
            try:
                row_text = (row.text or "").strip()
                phone_from_row = extract_phone_from_text(row_text)

                logging.info("Linha encontrada: %s", row_text)
                logging.info("Telefone extraído da linha: %s", phone_from_row)

                if not phone_from_row:
                    logging.info("Nenhum telefone visível nesta linha. Pulando conversa.")
                    continue

                if not self.is_authorized_phone(phone_from_row):
                    logging.info("Nenhum telefone não autorizado. Pulando conversa.")
                    continue

                if not self.open_conversation_by_row(row):
                    continue

                phone_from_header = self.get_current_phone()
                phone = phone_from_header if phone_from_header else phone_from_row

                if not self.is_authorized_phone(phone):
                    continue

                incoming_text = self.get_last_incoming_message()
                if not incoming_text:
                    continue

                state = self.states.setdefault(phone, ContactState())

                if incoming_text == state.last_processed_message:
                    continue

                state.last_processed_message = incoming_text

                reply = self.responder(phone, incoming_text)
                self.send_message(reply)

                logging.info("Resposta enviada para %s: %s", phone, reply)

            except Exception as e:
                logging.exception("Erro ao processar conversa: %s", e)

    def run(self):
        self.start_browser()

        print("Bot em execução. Pressione CTRL+C para parar.")
        logging.info("Bot iniciado.")

        try:
            while True:
                self.process_visible_conversations()
                time.sleep(POLL_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("\nEncerrando bot...")
            logging.info("Bot encerrado pelo usuário.")
        finally:
            if self.driver:
                self.driver.quit()


# =========================================================
# EXECUÇÃO
# =========================================================

if __name__ == "__main__":
    configurar_logging()
    bot = WhatsAppFAQBot()
    bot.run()