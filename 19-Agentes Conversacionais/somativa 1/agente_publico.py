# ---------------------------------------------------------------------------
# AGENTE WHATSAPP COM SELENIUM (V. PÚBLICO - RESPONDE A TODOS)
# ---------------------------------------------------------------------------
# Esta versão foi modificada para responder a QUALQUER nova mensagem de
# QUALQUER contato, removendo o filtro de autorização.
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

# --- 1. LÓGICA DO CHATBOT ---
# A lista de contatos autorizados foi removida.

regras = [
    { "padrao": r'oi|olá|bom\s+dia|boa\s+tarde|boa\s+noite', "respostas": ["Olá! Sou o assistente virtual da Água Pura. Como posso te ajudar hoje?"] },
    { "padrao": r'horário|horas|fecha|abre|funciona|atendimento', "respostas": ["Nosso horário de atendimento é de segunda a sexta, das 8h30 às 18h, e aos sábados das 9h às 12h."] },
    { "padrao": r'endereço|onde\s+fica|localização|local', "respostas": ["Nossa loja física fica na Rua das Águas Claras, 123 - Centro. Venha nos visitar!"] },
    { "padrao": r'marca|tipos|modelos|quais\s+purificadores|catálogo', "respostas": ["Trabalhamos com excelentes modelos de parede, bancada e com refrigeração. Você tem alguma preferência para eu poder te ajudar melhor?"] },
    { "padrao": r'preço|valor|custa|quanto|caro|barato', "respostas": ["Os valores variam bastante conforme o modelo e suas funcionalidades. Para qual tipo de uso você precisa? (Ex: residencial, comercial)"] },
    { "padrao": r'instalação|instalar|instalam|montagem', "respostas": ["Sim, oferecemos serviço de instalação! A taxa pode variar conforme sua região. Para qual CEP seria?"] },
    { "padrao": r'manutenção|assistência|conserto|reparo|estrago', "respostas": ["Com certeza! Realizamos tanto a manutenção preventiva quanto consertos. O que aconteceu com o seu aparelho?"] },
    { "padrao": r'refil|troca\s+do\s+filtro|filtro', "respostas": ["A troca do refil é essencial e recomendamos, em média, a cada 6 meses. Temos o refil para todos os modelos que vendemos!"] },
    { "padrao": r'garantia|troca|defeito', "respostas": ["Todos os nossos purificadores possuem garantia de fábrica de 12 meses contra defeitos de fabricação."] },
    { "padrao": r'pagamento|cartão|pix|parcelamento|aceita', "respostas": ["Aceitamos PIX, dinheiro e cartões de débito e crédito. Parcelamos em até 10x sem juros, dependendo do modelo!"] },
    { "padrao": r'entrega|frete|prazo|entregam', "respostas": ["Entregamos em toda a cidade! O prazo médio é de 2 dias úteis. Se preferir, pode retirar na loja."] },
    { "padrao": r'atendente|humano|vendedor|falar\s+com', "respostas": ["Entendido. Para falar com um de nossos vendedores, por favor, ligue para (41) 3333-4444 ou aguarde um momento que alguém já irá responder por aqui."] },
    { "padrao": r'obrigado|agradecido|valeu', "respostas": ["De nada! Se precisar de mais alguma coisa, é só chamar."] },
    { "padrao": r'adeus|tchau|sair', "respostas": ["Obrigado pelo seu contato! Tenha um ótimo dia."] }
]

def encontrar_resposta(mensagem_usuario):
    for regra in regras:
        if re.search(regra["padrao"], mensagem_usuario, re.IGNORECASE):
            return random.choice(regra["respostas"])
    return "Desculpe, não entendi sua pergunta. Você pode me perguntar sobre: preço, modelos, instalação, refil, garantia, entrega, pagamento, ou horário."

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

# --- 3. LOOP DE MONITORAMENTO (MODIFICADO) ---

def monitorar_mensagens(driver):
    print("\nLogin detectado. Iniciando monitoramento PÚBLICO (responderá a todos)...")
    while True:
        try:
            # Seletor para a notificação de mensagem não lida
            xpath_seletor = '//span[@data-testid="icon-unread-count"]/ancestor::div[@role="listitem"]'
            conversa_nao_lida = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath_seletor))
            )
            
            # Extrai o nome/número do contato apenas para log
            nome_contato_elemento = conversa_nao_lida.find_element(By.XPATH, './/span[@dir="auto" and @aria-label]')
            contato_bruto = nome_contato_elemento.get_attribute("aria-label")
            
            print(f"Nova mensagem detectada do contato: {contato_bruto}. Processando...")
            
            # Clica na conversa para abri-la
            conversa_nao_lida.click()
            time.sleep(2)
            
            # Pega a última mensagem recebida
            mensagens = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
            if mensagens:
                ultima_mensagem_texto = mensagens[-1].find_element(By.CSS_SELECTOR, "span.selectable-text").text
                print(f"Mensagem recebida: '{ultima_mensagem_texto}'")
                
                # Encontra a resposta e a envia
                resposta = encontrar_resposta(ultima_mensagem_texto)
                responder(driver, resposta)
            else:
                print("AVISO: Nenhuma mensagem de entrada encontrada na conversa. Ignorando.")

        except TimeoutException:
            # Isso é normal, apenas significa que não há novas mensagens
            print("Nenhuma mensagem nova. Verificando novamente...")
            time.sleep(5)
        except Exception as e:
            print(f"Erro no loop principal: {e}")
            print("Tentando se recuperar...")
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
