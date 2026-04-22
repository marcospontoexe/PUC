# bot_whatsapp_purificador_menu_5.py
# -*- coding: utf-8 -*-

import time
import logging
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================
# CONFIG
# =========================

URL = "https://web.whatsapp.com/"
LOG = "bot.log"

# CONTATOS = ["5541999496865"]  # pode colocar nome OU número aqui
CONTATOS = ["Lovezona"]  # pode colocar nome OU número aqui
# CONTATOS = ["5541997069783"]  # pode colocar nome OU número aqui


# =========================
# LOG
# =========================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(LOG), logging.StreamHandler()]
)


# =========================
# BOT
# =========================

class Bot:

    def __init__(self):
        self.driver = None
        self.wait = None

    def start(self):
        profile = Path.home() / "selenium_whatsapp"
        profile.mkdir(exist_ok=True)

        options = Options()
        options.add_argument(f"--user-data-dir={profile}")
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 60)

        self.driver.get(URL)

        print("Faça login no WhatsApp...")
        self.wait_ready()

    def wait_ready(self):
        """
        Espera o WhatsApp carregar
        """
        while True:
            try:
                self.driver.find_element(By.ID, "app")
                print("WhatsApp pronto")
                return
            except:
                time.sleep(1)

    def debug(self):
        """
        Salva debug (muito útil)
        """
        self.driver.save_screenshot("erro.png")
        with open("erro.html", "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

    def get_search_box(self):
        """
        🔥 Função robusta para encontrar a busca
        """

        seletores = [
            "//div[@contenteditable='true'][@role='textbox']",
            "//div[@contenteditable='true']",
            "//div[contains(@aria-label,'Pesquisar')]",
            "//div[contains(@aria-label,'Search')]",
            "//div[@data-tab='3']",
            "//div[@data-tab='10']",
        ]

        for sel in seletores:
            try:
                elems = self.driver.find_elements(By.XPATH, sel)
                for e in elems:
                    if e.is_displayed():
                        return e
            except:
                continue

        self.debug()
        raise Exception("Caixa de busca não encontrada")

    def abrir_chat(self, nome):
        try:
            box = self.get_search_box()

            box.click()
            time.sleep(0.5)

            box.send_keys(Keys.CONTROL, "a")
            box.send_keys(Keys.BACKSPACE)

            box.send_keys(nome)
            time.sleep(1.5)

            box.send_keys(Keys.ENTER)
            time.sleep(1.5)

            return True

        except Exception as e:
            logging.info(f"Falha ao abrir chat por busca ({nome}): {e}")
            return False

    def ultima_msg(self):
        try:
            msgs = self.driver.find_elements(
                By.CSS_SELECTOR,
                "div.message-in span.selectable-text"
            )
            if msgs:
                return msgs[-1].text
        except:
            pass
        return ""

    def enviar(self, msg):
        box = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//footer//div[@contenteditable='true']")
            )
        )
        box.click()
        box.send_keys(msg)
        box.send_keys(Keys.ENTER)

    def run(self):
        self.start()

        ultima = ""

        while True:
            for contato in CONTATOS:

                if not self.abrir_chat(contato):
                    continue

                try:
                    msg = self.ultima_msg()

                    if not msg:
                        continue

                    if msg == ultima:
                        continue

                    ultima = msg

                    logging.info(f"Mensagem recebida: {msg}")

                    # resposta simples teste
                    resposta = "Recebi sua mensagem!"

                    self.enviar(resposta)

                except StaleElementReferenceException:
                    logging.info("Elemento stale, ignorando...")
                    continue
                except Exception as e:
                    logging.exception(f"Erro: {e}")

            time.sleep(3)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    Bot().run()