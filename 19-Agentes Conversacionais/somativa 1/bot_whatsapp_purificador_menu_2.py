# bot_whatsapp_purificador_por_telefone.py
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

# Números autorizados somente com dígitos.
# Exemplo: "5541999999999" = +55 (41) 99999-9999
CONTATOS_AUTORIZADOS = {
    "5541997069783",
    "5541999496865",
}

MENSAGEM_BOAS_VINDAS = (
    "Olá! Sou o assistente virtual da loja de purificadores de água. "
    "Como posso ajudar você hoje?\n\n"
    "Você pode perguntar sobre:\n"
    "• horário de atendimento\n"
    "• endereço\n"
    "• modelos\n"
    "• preço\n"
    "• instalação\n"
    "• manutenção\n"
    "• refil\n"
    "• garantia\n"
    "• pagamento\n"
    "• entrega\n"
    "• falar com atendente"
)

MENSAGEM_NAO_ENTENDI = (
    "Desculpe, não entendi sua solicitação.\n"
    "Você pode perguntar sobre: preço, modelos, instalação, refil, "
    "garantia, entrega, pagamento, horário ou atendente."
)

MENSAGEM_CONTINUAR = "Posso ajudar em mais alguma coisa? (sim/não)"
MENSAGEM_ENCERRAMENTO = "Obrigado pelo contato. Estamos à disposição!"

RESPOSTAS = {
    "saudacao": "Olá! Como posso ajudar você hoje?",
    "horario": "Nosso atendimento é de segunda a sexta, das 8h às 18h, e aos sábados das 8h às 12h.",
    "endereco": "Nossa loja fica na Rua X, número Y. Se quiser, posso te passar referências de localização.",
    "modelos": "Trabalhamos com purificadores de parede, bancada e modelos com refrigeração.",
    "preco": "Os valores variam conforme o modelo. Me diga qual tipo de purificador você procura que eu posso orientar melhor.",
    "instalacao": "Sim, realizamos instalação. Posso verificar a disponibilidade para sua região.",
    "manutencao": "Fazemos manutenção preventiva e corretiva.",
    "refil": "A troca do refil depende do uso, em média a cada 6 meses.",
    "garantia": "Nossos produtos possuem garantia de fábrica. Posso te passar os detalhes por modelo.",
    "pagamento": "Aceitamos PIX, cartão e parcelamento, conforme o produto.",
    "entrega": "Realizamos entrega em várias regiões. Posso verificar o prazo para o seu endereço.",
    "atendente": "Vou encaminhar sua solicitação para um atendente humano."
}

# Palavras-chave por intenção
INTENTS: List[Tuple[str, List[str]]] = [
    ("saudacao", ["oi", "olá", "ola", "bom dia", "boa tarde", "boa noite"]),
    ("horario", ["horário", "horario", "abre", "funciona", "atendimento"]),
    ("endereco", ["endereço", "endereco", "onde fica", "localização", "localizacao"]),
    ("modelos", ["modelos", "quais purificadores", "catálogo", "catalogo", "produtos"]),
    ("preco", ["preço", "preco", "valor", "custa", "quanto"]),
    ("instalacao", ["instalação", "instalacao", "instalar", "instalam"]),
    ("manutencao", ["manutenção", "manutencao", "assistência", "assistencia", "conserto"]),
    ("refil", ["refil", "filtro", "troca do filtro", "troca de filtro"]),
    ("garantia", ["garantia", "defeito", "troca", "assistência técnica", "assistencia tecnica"]),
    ("pagamento", ["pagamento", "cartão", "cartao", "pix", "parcelamento"]),
    ("entrega", ["entrega", "frete", "prazo"]),
    ("atendente", ["atendente", "humano", "vendedor", "pessoa"]),
]

AFIRMATIVAS = {
    "sim", "s", "claro", "quero", "pode", "pode sim", "quero sim", "continuar", "vamos", "ok"
}

NEGATIVAS = {
    "nao", "não", "n", "nao obrigado", "não obrigado", "obrigado", "obrigada", "sair", "encerrar", "parar"
}


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
    """Remove tudo que não for dígito."""
    return re.sub(r"\D", "", phone or "")


def extract_phone_from_text(text: str) -> Optional[str]:
    """
    Extrai um possível telefone do texto.
    Primeiro tenta padrões comuns de BR; se não encontrar, usa apenas dígitos.
    """
    if not text:
        return None

    # Tenta encontrar um telefone brasileiro comum, com ou sem +55.
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
    return any(normalize_text(phrase) in t for phrase in phrases)


def detect_intent(message: str) -> str:
    for intent, keywords in INTENTS:
        if contains_any(message, keywords):
            return intent
    return "desconhecido"


# =========================================================
# ESTADO
# =========================================================

@dataclass
class ContactState:
    last_processed_message: str = ""
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
        print("Aguardando a interface carregar...")

        self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='grid' or @aria-label='Lista de conversas']")
            )
        )

        print("WhatsApp Web pronto.")

    def get_conversation_rows(self):
        """
        Retorna as linhas visíveis da lista de conversas.
        A estrutura do WhatsApp Web pode mudar, então pode ser necessário ajustar o seletor.
        """
        grid = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[@role='grid' or @aria-label='Lista de conversas']")
            )
        )
        rows = grid.find_elements(By.XPATH, ".//div[@role='row']")
        return rows

    def open_conversation_by_row(self, row) -> bool:
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", row)
            time.sleep(0.2)
            row.click()
            time.sleep(0.9)
            return True
        except Exception as e:
            logging.exception("Erro ao abrir conversa: %s", e)
            return False

    def get_chat_title_text(self) -> str:
        """
        Tenta ler o título do chat aberto.
        Em conversas sem contato salvo, esse título pode ser o número.
        """
        selectors = [
            (By.XPATH, "//header//span[@title]"),
            (By.XPATH, "//header//span[@dir='auto']"),
            (By.XPATH, "//header//*[self::span or self::div][@title]"),
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
        """
        Extrai o telefone do chat aberto.
        Se o título não contiver número, retorna None.
        """
        title = self.get_chat_title_text()
        phone = extract_phone_from_text(title)
        return phone

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
            time.sleep(0.8)
        except Exception as e:
            logging.exception("Erro ao enviar mensagem: %s", e)

    def is_authorized_phone(self, phone: Optional[str]) -> bool:
        if not phone:
            return False
        return normalize_phone(phone) in CONTATOS_AUTORIZADOS

    def build_reply(self, phone: str, incoming_text: str) -> str:
        """
        Regras de resposta:
        - se o contato respondeu 'sim' após uma interação, orienta para próxima dúvida;
        - se respondeu 'não', encerra;
        - senão, detecta intenção e responde o FAQ.
        """
        state = self.states.setdefault(phone, ContactState())
        normalized = normalize_text(incoming_text)

        # Respostas curtas de continuidade
        if state.awaiting_more_help and normalized in AFIRMATIVAS:
            state.awaiting_more_help = False
            return (
                "Perfeito. Pode me enviar sua próxima dúvida sobre preço, modelos, instalação, "
                "refil, garantia, entrega, pagamento ou atendente."
            )

        if state.awaiting_more_help and normalized in NEGATIVAS:
            state.awaiting_more_help = False
            return MENSAGEM_ENCERRAMENTO

        # Resposta FAQ por regras
        intent = detect_intent(incoming_text)

        if intent == "desconhecido":
            state.awaiting_more_help = True
            return f"{MENSAGEM_NAO_ENTENDI}\n\n{MENSAGEM_CONTINUAR}"

        # Se reconheceu intenção
        state.awaiting_more_help = True
        return f"{RESPOSTAS[intent]}\n\n{MENSAGEM_CONTINUAR}"

    def process_visible_conversations(self):
        """
        Percorre as conversas visíveis na lista lateral.
        Para cada conversa, tenta extrair o telefone:
        - primeiro do título/linha da conversa;
        - depois do cabeçalho do chat aberto;
        e só responde se o número estiver na lista autorizada.
        """
        rows = self.get_conversation_rows()

        for row in rows:
            try:
                row_text = (row.text or "").strip()
                phone_from_row = extract_phone_from_text(row_text)

                # Se não houver telefone visível na linha, pula.
                if not phone_from_row:
                    continue

                # Só conversa com números autorizados
                if not self.is_authorized_phone(phone_from_row):
                    continue

                if not self.open_conversation_by_row(row):
                    continue

                # Tenta extrair novamente pelo cabeçalho do chat
                phone_from_header = self.get_current_phone()
                phone = phone_from_header if phone_from_header else phone_from_row

                if not self.is_authorized_phone(phone):
                    continue

                incoming_text = self.get_last_incoming_message()
                if not incoming_text:
                    continue

                state = self.states.setdefault(phone, ContactState())

                # Evita responder a mesma mensagem repetidamente
                if incoming_text == state.last_processed_message:
                    continue

                state.last_processed_message = incoming_text

                reply = self.build_reply(phone, incoming_text)
                self.send_message(reply)

            except Exception as e:
                logging.exception("Erro ao processar conversa: %s", e)

    def run(self):
        self.start_browser()

        print("Bot em execução. Pressione CTRL+C para parar.")
        try:
            while True:
                self.process_visible_conversations()
                time.sleep(POLL_INTERVAL_SECONDS)
        except KeyboardInterrupt:
            print("\nEncerrando bot...")
        finally:
            if self.driver:
                self.driver.quit()


# =========================================================
# EXECUÇÃO
# =========================================================

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    bot = WhatsAppFAQBot()
    bot.run()