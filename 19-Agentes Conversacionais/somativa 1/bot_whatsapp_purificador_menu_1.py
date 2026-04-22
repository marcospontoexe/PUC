# bot_whatsapp_purificador.py
# -*- coding: utf-8 -*-

import time
import logging
import unicodedata
from dataclasses import dataclass
from typing import Dict, Optional, List, Tuple

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

# Use exatamente o nome do contato como aparece no WhatsApp Web
CONTATOS_AUTORIZADOS = {
    "+5541997069783",
    "+5541999496865",
}

# Se quiser usar o número salvo no contato, coloque o nome/número visível no WhatsApp
# Ex.: "Marcos (WhatsApp)" ou "+55 41 99999-9999"

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
    """Normaliza texto: minúsculas, sem acentos e com espaços compactados."""
    if not text:
        return ""
    text = text.lower().strip()
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = " ".join(text.split())
    return text


def contains_any(text: str, phrases: List[str]) -> bool:
    """Verifica se alguma expressão da lista está contida no texto normalizado."""
    t = normalize_text(text)
    for phrase in phrases:
        if normalize_text(phrase) in t:
            return True
    return False


def detect_intent(message: str) -> str:
    """Classifica a mensagem em uma intenção simples baseada em regras."""
    text = normalize_text(message)

    for intent, keywords in INTENTS:
        if contains_any(text, keywords):
            return intent

    return "desconhecido"


# =========================================================
# BOT
# =========================================================

@dataclass
class ContactState:
    last_processed_message: str = ""
    awaiting_more_help: bool = False


class WhatsAppFAQBot:
    def __init__(self):
        self.driver = None
        self.wait = None
        self.states: Dict[str, ContactState] = {
            contato: ContactState() for contato in CONTATOS_AUTORIZADOS
        }

    def start_browser(self):
        options = Options()
        # Mantém a sessão logada usando o perfil padrão do Chrome
        options.add_argument("--user-data-dir=./chrome_profile")
        options.add_argument("--profile-directory=Default")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 25)
        self.driver.get(WHATSAPP_WEB_URL)

        print("Abra o WhatsApp Web e leia o QR Code, se necessário.")
        print("Aguardando carregar a interface...")

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Lista de conversas' or @role='grid']"))
        )
        print("WhatsApp Web carregado com sucesso.")

    def search_and_open_chat(self, contact_name: str) -> bool:
        """Pesquisa e abre uma conversa pelo nome do contato."""
        try:
            # Caixa de pesquisa do WhatsApp Web
            search_box = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        "//div[@contenteditable='true' and (@aria-label='Pesquisar ou começar uma nova conversa' "
                        "or @aria-label='Search or start new chat' or @data-tab='3')]"
                    )
                )
            )

            search_box.click()
            time.sleep(0.3)
            search_box.send_keys(Keys.CONTROL, "a")
            search_box.send_keys(Keys.BACKSPACE)
            search_box.send_keys(contact_name)
            time.sleep(1)

            # Clica no contato encontrado
            contact = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        f"//span[@title='{contact_name}']"
                    )
                )
            )
            contact.click()
            time.sleep(0.8)
            return True

        except Exception as e:
            logging.exception("Erro ao abrir conversa com %s: %s", contact_name, e)
            return False

    def get_last_incoming_message(self) -> str:
        """Retorna a última mensagem recebida na conversa aberta."""
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

    def get_last_message_from_chat(self) -> str:
        """Retorna a última mensagem visível na conversa (entrada ou saída)."""
        try:
            messages = self.driver.find_elements(
                By.CSS_SELECTOR,
                "span.selectable-text"
            )
            if not messages:
                return ""
            return messages[-1].text.strip()
        except Exception:
            return ""

    def send_message(self, message: str):
        """Envia mensagem para o chat aberto."""
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

    def reply_to_message(self, incoming_text: str) -> str:
        """Gera a resposta para a mensagem do usuário seguindo o fluxo do trabalho."""
        normalized = normalize_text(incoming_text)

        if normalized in AFIRMATIVAS:
            return MENSAGEM_BOAS_VINDAS + "\n\n" + MENSAGEM_CONTINUAR

        if normalized in NEGATIVAS:
            return MENSAGEM_ENCERRAMENTO

        intent = detect_intent(incoming_text)

        if intent == "desconhecido":
            return MENSAGEM_NAO_ENTENDI

        return f"{RESPOSTAS[intent]}\n\n{MENSAGEM_CONTINUAR}"

    def process_contact(self, contact_name: str):
        """Processa uma conversa específica, respeitando o estado do fluxo."""
        if contact_name not in CONTATOS_AUTORIZADOS:
            return

        if not self.search_and_open_chat(contact_name):
            return

        incoming_text = self.get_last_incoming_message()
        if not incoming_text:
            return

        state = self.states.setdefault(contact_name, ContactState())

        # Evita responder a mesma mensagem repetidamente
        if incoming_text == state.last_processed_message:
            return

        state.last_processed_message = incoming_text

        # Gera resposta conforme o fluxo
        outgoing = self.reply_to_message(incoming_text)
        self.send_message(outgoing)

        # Atualiza estado simples da conversa
        normalized = normalize_text(incoming_text)

        if normalized in NEGATIVAS:
            state.awaiting_more_help = False
        else:
            state.awaiting_more_help = True

    def run(self):
        self.start_browser()

        print("Bot em execução. Pressione CTRL+C para parar.")
        try:
            while True:
                for contact in CONTATOS_AUTORIZADOS:
                    self.process_contact(contact)
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