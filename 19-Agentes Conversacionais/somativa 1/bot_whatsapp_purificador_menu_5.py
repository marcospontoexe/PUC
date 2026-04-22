# bot_whatsapp_all_contacts.py

import time
import logging

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =========================
# CONFIG
# =========================

URL = "https://web.whatsapp.com/"
RESPOSTA = "Olá! Recebi sua mensagem 👍"

logging.basicConfig(level=logging.INFO)


# =========================
# BOT
# =========================

class Bot:

    def __init__(self):
        self.driver = None
        self.wait = None
        self.respondidas = {}

    def start(self):
        options = Options()
        options.add_argument("--start-maximized")

        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 60)

        self.driver.get(URL)

        print("Escaneie o QR Code...")
        self.wait.until(EC.presence_of_element_located((By.ID, "app")))

        print("WhatsApp pronto!")

    def get_unread_chats(self):
        """
        🔥 pega conversas com mensagem NÃO LIDA (bolinha verde)
        """
        return self.driver.find_elements(
            By.XPATH,
            "//div[@role='row']//span[@aria-label]"
        )

    def open_chat(self, element):
        self.driver.execute_script("arguments[0].click();", element)
        time.sleep(1)

    def get_contact_name(self):
        try:
            return self.driver.find_element(
                By.XPATH, "//header//span[@title]"
            ).text
        except:
            return "Desconhecido"

    def get_last_message(self):
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

    def send(self, msg):
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

        print("Bot rodando...")

        while True:
            try:
                chats = self.get_unread_chats()

                for chat in chats:
                    try:
                        self.open_chat(chat)

                        nome = self.get_contact_name()
                        msg = self.get_last_message()

                        if not msg:
                            continue

                        # evita responder repetido
                        if self.respondidas.get(nome) == msg:
                            continue

                        logging.info(f"{nome}: {msg}")

                        self.send(RESPOSTA)

                        self.respondidas[nome] = msg

                        logging.info("Resposta enviada")

                    except Exception as e:
                        logging.info(f"Erro no chat: {e}")
                        continue

                time.sleep(3)

            except Exception as e:
                logging.error(f"Erro geral: {e}")
                time.sleep(5)


# =========================
# MAIN
# =========================

if __name__ == "__main__":
    Bot().run()