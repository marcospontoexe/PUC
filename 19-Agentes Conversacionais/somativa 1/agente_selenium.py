# ---------------------------------------------------------------------------
# AGENTE WHATSAPP COM SELENIUM (MONITORAMENTO REAL)
# ---------------------------------------------------------------------------
# Versão completa que monitora e responde mensagens em tempo real.
#
# INSTALAÇÃO: pip install selenium webdriver-manager
# ---------------------------------------------------------------------------

import re
import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# --- 1. LÓGICA DO CHATBOT E CONFIGURAÇÕES ---

CONTATOS_AUTORIZADOS = {
    "Lovezona",
    "5541999496865",
}

regras = [
    # ... (cole aqui TODAS as regras do script simulador) ...
    { "padrao": r'oi|olá|bom\s+dia', "respostas": ["Olá! Sou o assistente virtual da Água Pura. Como posso te ajudar?"] },
    { "padrao": r'horário|atendimento', "respostas": ["Nosso horário de atendimento é de segunda a sexta, das 8h30 às 18h, e aos sábados das 9h às 12h."] },
    { "padrao": r'endereço|onde\s+fica', "respostas": ["Nossa loja física fica na Rua das Águas Claras, 123 - Centro."] },
    { "padrao": r'atendente|falar\s+com', "respostas": ["Entendido. Para falar com um de nossos vendedores, por favor, ligue para (41) 3333-4444."] },
    # (etc...)
]

def encontrar_resposta(mensagem_usuario):
    for regra in regras:
        if re.search(regra["padrao"], mensagem_usuario, re.IGNORECASE):
            return random.choice(regra["respostas"])
    return "Desculpe, não entendi sua pergunta. Você pode me perguntar sobre: preço, modelos, instalação, etc."

# --- 2. FUNÇÕES DO AGENTE SELENIUM ---

def iniciar_driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://web.whatsapp.com" )
    print("Navegador iniciado. Por favor, escaneie o QR Code.")
    return driver

def responder(driver, resposta):
    try:
        caixa_de_texto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))
        )
        caixa_de_texto.click()
        caixa_de_texto.send_keys(resposta)
        botao_enviar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
        )
        botao_enviar.click()
        print(f"Resposta enviada: {resposta}")
    except Exception as e:
        print(f"Erro ao tentar responder: {e}")

# --- 3. LOOP DE MONITORAMENTO ---

def monitorar_mensagens(driver):
    print("\nLogin detectado. Iniciando monitoramento...")
    while True:
        try:
            # Seletor para a notificação de mensagem não lida
            xpath_seletor = '//span[@data-testid="icon-unread-count"]/ancestor::div[@role="listitem"]'
            conversa_nao_lida = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath_seletor))
            )
            
            # Extrai o nome/número do contato
            nome_contato_elemento = conversa_nao_lida.find_element(By.XPATH, './/span[@dir="auto" and @aria-label]')
            contato_bruto = nome_contato_elemento.get_attribute("aria-label")
            
            # Lógica de autorização
            contato_id_numerico = re.sub(r'[^\d]', '', contato_bruto)
            if contato_bruto in CONTATOS_AUTORIZADOS or contato_id_numerico in CONTATOS_AUTORIZADOS:
                print(f"Nova mensagem do contato autorizado: {contato_bruto}")
                conversa_nao_lida.click()
                time.sleep(2)
                
                # Pega a última mensagem
                mensagens = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
                if mensagens:
                    ultima_mensagem_texto = mensagens[-1].find_element(By.CSS_SELECTOR, "span.selectable-text").text
                    resposta = encontrar_resposta(ultima_mensagem_texto)
                    responder(driver, resposta)
            else:
                # Se não for autorizado, apenas clica para marcar como lida e ignora
                print(f"Contato '{contato_bruto}' não autorizado. Ignorando.")
                conversa_nao_lida.click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/button').click()

        except TimeoutException:
            print("Nenhuma mensagem nova. Verificando novamente...")
            time.sleep(5)
        except Exception as e:
            print(f"Erro no loop principal: {e}")
            time.sleep(10)

# --- 4. EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    driver = None
    try:
        driver = iniciar_driver()
        WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.ID, "side")))
        monitorar_mensagens(driver)
    except (KeyboardInterrupt, SystemExit):
        print("\nScript interrompido pelo usuário.")
    except Exception as e:
        print(f"Um erro fatal ocorreu: {e}")
    finally:
        if driver:
            print("Encerrando o navegador.")
            driver.quit()
