# ---------------------------------------------------------------------------
# AGENTE DE ATENDIMENTO (V6 - SELETOR CONFIRMADO E REFINADO)
# ---------------------------------------------------------------------------
# Usando o seletor exato confirmado pelo usuário e refinando a lógica
# de extração para máxima robustez.
# ---------------------------------------------------------------------------

import time
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

# --- 1. CONFIGURAÇÕES DO AGENTE ---
print("[LOG] Carregando configurações...")
CONTATOS_AUTORIZADOS = {
    "Lovezona",
    "5541997069783",
}
print(f"[LOG] Contatos autorizados: {CONTATOS_AUTORIZADOS}")

# ... (O resto das configurações INTENTS e RESPOSTAS permanece o mesmo) ...
INTENTS = {
    "saudacao": [r'oi', r'olá', r'bom\s+dia', r'boa\s+tarde', r'boa\s+noite', r'tudo\s+bem'],
    "horario": [r'horário', r'horas', r'fecha', r'abre', r'funciona', r'atendimento'],
    "endereco": [r'endereço', r'onde\s+fica', r'localização', r'local'],
    "modelos": [r'marca', r'tipos', r'modelos', r'quais\s+purificadores', r'catálogo'],
    "preco": [r'preço', r'valor', r'custa', r'quanto', r'caro', r'barato'],
    "instalacao": [r'instalação', r'instalar', r'instalam', r'montagem'],
    "manutencao": [r'manutenção', r'assistência', r'conserto', r'reparo', r'estrago'],
    "refil": [r'refil', r'troca\s+do\s+filtro', r'filtro'],
    "garantia": [r'garantia', r'troca', r'defeito'],
    "pagamento": [r'pagamento', r'cartão', r'pix', r'parcelamento', r'aceita'],
    "entrega": [r'entrega', r'frete', r'prazo', r'entregam'],
    "atendente": [r'atendente', r'humano', r'vendedor', r'falar\s+com']
}

RESPOSTAS = {
    "saudacao": "Olá! Sou o assistente virtual da Água Pura. Como posso te ajudar hoje com seu purificador?",
    "horario": "Nosso horário de atendimento é de segunda a sexta, das 8h30 às 18h, e aos sábados das 9h às 12h.",
    "endereco": "Nossa loja física fica na Rua das Águas Claras, 123 - Centro. Venha nos visitar!",
    "modelos": "Trabalhamos com excelentes modelos de parede, bancada e com refrigeração. Você tem alguma preferência para eu poder te ajudar melhor?",
    "preco": "Os valores variam bastante conforme o modelo e suas funcionalidades. Para qual tipo de uso você precisa? (Ex: residencial, comercial)",
    "instalacao": "Sim, oferecemos serviço de instalação! A taxa pode variar conforme sua região. Para qual CEP seria?",
    "manutencao": "Com certeza! Realizamos tanto a manutenção preventiva quanto consertos. O que aconteceu com o seu aparelho?",
    "refil": "A troca do refil é essencial e recomendamos, em média, a cada 6 meses. Temos o refil para todos os modelos que vendemos!",
    "garantia": "Todos os nossos purificadores possuem garantia de fábrica de 12 meses contra defeitos de fabricação.",
    "pagamento": "Aceitamos PIX, dinheiro e cartões de débito e crédito. Parcelamos em até 10x sem juros, dependendo do modelo!",
    "entrega": "Entregamos em toda a cidade! O prazo médio é de 2 dias úteis. Se preferir, pode retirar na loja.",
    "atendente": "Entendido. Para falar com um de nossos vendedores, por favor, ligue para (41) 3333-4444 ou aguarde um momento que alguém já irá responder por aqui.",
    "fallback": "Desculpe, não entendi sua pergunta. Você pode me perguntar sobre: preço, modelos, instalação, refil, garantia, entrega, pagamento, horário ou como falar com um atendente."
}


# --- 2. FUNÇÕES DE LÓGICA ---

def classificar_intencao(mensagem):
    print(f"[LOG] Classificando intenção da mensagem: '{mensagem}'")
    mensagem_lower = mensagem.lower()
    for intencao, palavras_chave in INTENTS.items():
        for palavra in palavras_chave:
            if re.search(palavra, mensagem_lower):
                print(f"[LOG] Intenção encontrada: '{intencao}'")
                return intencao
    print("[LOG] Nenhuma intenção específica encontrada. Usando 'fallback'.")
    return "fallback"

# --- 3. FUNÇÕES DO AGENTE SELENIUM ---

def iniciar_driver():
    print("[LOG] Iniciando o driver do Selenium...")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://web.whatsapp.com" )
    print("[LOG] Navegador iniciado. Por favor, escaneie o QR Code.")
    return driver

def responder(driver, resposta):
    print(f"[LOG] Entrando na função 'responder' para enviar: '{resposta}'")
    try:
        caixa_de_texto = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'))
        )
        print("[LOG] Caixa de texto encontrada. Clicando e digitando...")
        caixa_de_texto.click()
        caixa_de_texto.send_keys(resposta)
        
        botao_enviar = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button'))
        )
        print("[LOG] Botão de enviar encontrado. Clicando...")
        botao_enviar.click()
        print(f"[LOG] SUCESSO: Resposta enviada.")
        time.sleep(2)
    except Exception as e:
        print(f"[ERRO] Falha na função 'responder': {e}")

def monitorar_mensagens(driver):
    print("\n[LOG] Login detectado. Iniciando o loop de monitoramento de mensagens...")
    while True:
        print("\n[LOG] Procurando por conversas não lidas usando o seletor confirmado...")
        try:
            # --- SELETOR REFINADO ---
            # Este XPath é o mais importante. Ele encontra o elemento que contém a notificação
            # e sobe para o "pai" que é a linha inteira da conversa (um item de lista clicável).
            xpath_seletor = '//span[@data-testid="icon-unread-count"]/ancestor::div[@role="listitem"]'
            
            conversa_nao_lida = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath_seletor))
            )
            
            print("[LOG] SUCESSO: Elemento de conversa não lida foi encontrado!")
            
            # Extrai o nome do contato a partir do 'aria-label' do elemento filho
            nome_contato_elemento = conversa_nao_lida.find_element(By.XPATH, './/span[@dir="auto" and @aria-label]')
            contato_bruto = nome_contato_elemento.get_attribute("aria-label")
            print(f"[LOG] Contato bruto extraído da tela: '{contato_bruto}'")

            contato_id_numerico = re.sub(r'[^\d]', '', contato_bruto)
            print(f"[LOG] Contato normalizado para ID numérico: '{contato_id_numerico}'")

            print(f"[LOG] Verificando autorização: '{contato_bruto}' está em {CONTATOS_AUTORIZADOS}? Ou '{contato_id_numerico}' está em {CONTATOS_AUTORIZADOS}?")
            autorizado = contato_bruto in CONTATOS_AUTORIZADOS or contato_id_numerico in CONTATOS_AUTORIZADOS
            
            if not autorizado:
                print(f"[LOG] RESULTADO: Contato '{contato_bruto}' NÃO autorizado. Ignorando.")
                conversa_nao_lida.click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/button').click()
                time.sleep(1)
                continue

            print(f"[LOG] RESULTADO: Contato '{contato_bruto}' AUTORIZADO. Processando...")
            conversa_nao_lida.click()
            time.sleep(2)

            mensagens = driver.find_elements(By.CSS_SELECTOR, "div.message-in")
            if not mensagens:
                print("[LOG] AVISO: Nenhuma mensagem de entrada ('div.message-in') encontrada na conversa.")
                continue
            
            ultima_mensagem_texto = mensagens[-1].find_element(By.CSS_SELECTOR, "span.selectable-text").text
            print(f"[LOG] Última mensagem extraída: '{ultima_mensagem_texto}'")

            intencao = classificar_intencao(ultima_mensagem_texto)
            resposta = RESPOSTAS.get(intencao, RESPOSTAS["fallback"])
            
            responder(driver, resposta)

        except TimeoutException:
            print("[LOG] Nenhuma conversa não lida encontrada após 20 segundos. O loop continua...")
            time.sleep(5)
        except Exception as e:
            print(f"[ERRO] Erro inesperado no loop principal: {e}")
            print("[LOG] Tentando recarregar a página para se recuperar...")
            try:
                driver.refresh()
                WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "side")))
                print("[LOG] Página recarregada com sucesso.")
            except Exception as refresh_error:
                print(f"[ERRO FATAL] Falha ao recarregar a página: {refresh_error}. Encerrando script.")
                break

# --- 4. EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    driver = None
    try:
        driver = iniciar_driver()
        WebDriverWait(driver, 120).until(
            EC.presence_of_element_located((By.ID, "side"))
        )
        monitorar_mensagens(driver)
    except TimeoutException:
        print("[ERRO FATAL] Tempo de login esgotado (2 minutos).")
    except KeyboardInterrupt:
        print("\n[LOG] Script interrompido pelo usuário.")
    except Exception as e:
        print(f"[ERRO FATAL] Um erro crítico ocorreu na execução principal: {e}")
    finally:
        if driver:
            print("[LOG] Encerrando o navegador.")
            driver.quit()
