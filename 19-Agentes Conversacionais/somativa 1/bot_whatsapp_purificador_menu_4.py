# bot_whatsapp_purificador_menu.py
# -*- coding: utf-8 -*-

import re
import time
import logging
import unicodedata
from pathlib import Path
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

CONTATOS_AUTORIZADOS_NUMEROS = {
    "5541997069783",
    "5541999496865",
}

CONTATOS_AUTORIZADOS_NOMES = {
    "Lovezona",
    "Cliente Teste",
}

LOG_ARQUIVO = "bot_whatsapp.log"

MENU_INICIAL = (
    "Olá! Sou o assistente da loja de purificadores.\n"
    "Digite uma opção:\n"
    "1 - Horário\n2 - Endereço\n3 - Modelos\n4 - Preço\n"
    "5 - Instalação\n6 - Manutenção\n7 - Refil\n"
    "8 - Garantia\n9 - Pagamento\n10 - Entrega\n11 - Atendente"
)

RESPOSTA_PADRAO = "Não entendi. Digite uma opção do menu."
ENCERRAMENTO = "Obrigado pelo contato."

RESPOSTAS = {
    "1": "Atendemos de seg a sex, 8h30–18h, sábado até 12h.",
    "2": "Rua X, número Y.",
    "3": "Temos modelos de parede e bancada.",
    "4": "Valores variam conforme modelo.",
    "5": "Sim, fazemos instalação.",
    "6": "Fazemos manutenção completa.",
    "7": "Troca do refil a cada 6 meses.",
    "8": "Produtos com garantia.",
    "9": "Aceitamos PIX e cartão.",
    "10": "Realizamos entrega.",
    "11": "Encaminhando para atendente.",
}


# =========================================================
# LOG
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
# UTIL
# =========================================================

def normalize_text(text):
    text = text.lower().strip()
    text = unicodedata.normalize("NFKD", text)
    return "".join(c for c in text if not unicodedata.combining(c))


def normalize_phone(phone):
    return re.sub(r"\D", "", phone or "")


def extract_phone_from_text(text):
    if not text:
        return None

    digits = normalize_phone(text)
    if 10 <= len(digits) <= 13:
        return digits

    return None


def find_authorized_name(text):
    text_norm = normalize_text(text)
    for nome in CONTATOS_AUTORIZADOS_NOMES:
        if normalize_text(nome) in text_norm:
            return nome
    return None


def contato_autorizado(phone, name):
    if phone and normalize_phone(phone) in CONTATOS_AUTORIZADOS_NUMEROS:
        return True
    if name and name in CONTATOS_AUTORIZADOS_NOMES:
        return True
    return False


# =========================================================
# ESTADO
# =========================================================

@dataclass
class ContactState:
    last_message: str = ""
    first: bool = True


# =========================================================
# BOT
# =========================================================

class Bot:

    def __init__(self):
        self.driver = None
        self.wait = None
        self.states = {}

    def start_browser(self):
        profile = Path.home() / "selenium_whatsapp"
        profile.mkdir(exist_ok=True)

        options = Options()
        options.add_argument(f"--user-data-dir={profile}")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 120)

        self.driver.get(WHATSAPP_WEB_URL)

        print("Faça login no WhatsApp...")
        self.wait_for_ready()

    def wait_for_ready(self):
        for _ in range(120):
            if self.driver.find_elements(By.XPATH, "//div[@role='grid']"):
                print("WhatsApp pronto")
                return
            time.sleep(1)

        raise Exception("WhatsApp não carregou")

    def get_rows(self):
        grids = self.driver.find_elements(By.XPATH, "//div[@role='grid']")
        if not grids:
            self.debug()
            raise Exception("Lista não encontrada")

        return grids[0].find_elements(By.XPATH, ".//div[@role='row']")

    def debug(self):
        Path("debug.html").write_text(self.driver.page_source)
        self.driver.save_screenshot("debug.png")

    def open_chat(self, row):
        row.click()
        time.sleep(1)

    def get_title(self):
        try:
            el = self.driver.find_element(By.XPATH, "//header//span[@title]")
            return el.get_attribute("title")
        except:
            return ""

    def get_last_message(self):
        msgs = self.driver.find_elements(By.CSS_SELECTOR, "div.message-in span.selectable-text")
        if msgs:
            return msgs[-1].text
        return ""

    def send(self, msg):
        box = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//footer//div[@contenteditable='true']")
        ))
        box.click()
        box.send_keys(msg)
        box.send_keys(Keys.ENTER)

    def process(self):
        rows = self.get_rows()

        for row in rows:
            txt = row.text

            phone = extract_phone_from_text(txt)
            name = find_authorized_name(txt)

            logging.info(f"Row: {txt}")

            if not contato_autorizado(phone, name):
                continue

            self.open_chat(row)

            title = self.get_title()
            phone = extract_phone_from_text(title)
            name = find_authorized_name(title)

            key = phone or name or title

            msg = self.get_last_message()

            if not msg:
                continue

            state = self.states.setdefault(key, ContactState())

            if msg == state.last_message:
                continue

            state.last_message = msg

            if state.first:
                state.first = False
                self.send(MENU_INICIAL)
                continue

            if msg.strip() in RESPOSTAS:
                self.send(RESPOSTAS[msg.strip()])
            else:
                self.send(RESPOSTA_PADRAO)

    def run(self):
        try:
            self.start_browser()
            while True:
                self.process()
                time.sleep(POLL_INTERVAL_SECONDS)

        except Exception as e:
            print("Erro:", e)
            input("ENTER para fechar...")

        finally:
            if self.driver:
                self.driver.quit()


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":
    configurar_logging()
    Bot().run()