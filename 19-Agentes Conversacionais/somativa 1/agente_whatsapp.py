# ---------------------------------------------------------------------------
# AGENTE DE ATENDIMENTO (FAQ BOT) PARA LOJA DE PURIFICADORES DE ÁGUA (V2 - CORRIGIDO)
# ---------------------------------------------------------------------------
# CORREÇÃO: Garante que o número de telefone inclua o código do país com '+'
# ---------------------------------------------------------------------------

import pywhatkit
import time
import re

# --- 1. CONFIGURAÇÕES DO AGENTE ---

# Lista de contatos autorizados.
# NÚMEROS DEVEM ESTAR COMO STRINGS, MAS A LÓGICA IRÁ ADICIONAR O '+'
CONTATOS_AUTORIZADOS = {
    "Lovezona",
    "5541997069783",
}

# Dicionário de intenções (sem alterações)
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

# Dicionário de respostas (sem alterações)
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

# --- 2. FUNÇÕES DO AGENTE ---

def classificar_intencao(mensagem):
    mensagem_lower = mensagem.lower()
    for intencao, palavras_chave in INTENTS.items():
        for palavra in palavras_chave:
            if re.search(palavra, mensagem_lower):
                return intencao
    return "fallback"

def processar_mensagem(contato, mensagem):
    print(f"--- Nova Mensagem ---")
    print(f"De: {contato}")
    print(f"Mensagem: {mensagem}")

    if contato not in CONTATOS_AUTORIZADOS:
        print(f"Status: Contato '{contato}' não autorizado. Ignorando.")
        return

    print(f"Status: Contato '{contato}' autorizado. Processando...")

    intencao = classificar_intencao(mensagem)
    print(f"Intenção identificada: {intencao}")

    resposta = RESPOSTAS.get(intencao, RESPOSTAS["fallback"])

    # --- INÍCIO DA CORREÇÃO ---
    # Prepara o destinatário para a função de envio
    destinatario = contato
    # Se o contato for um número (composto apenas por dígitos), adiciona o '+'
    if destinatario.isdigit():
        destinatario = f"+{contato}"
    # --- FIM DA CORREÇÃO ---

    try:
        # Usa a variável 'destinatario' já formatada
        pywhatkit.sendwhatmsg_instantly(destinatario, resposta, wait_time=15, tab_close=True)
        print(f"Resposta enviada para {destinatario}: {resposta}")
        time.sleep(5)
    except Exception as e:
        # A mensagem de erro agora será mais específica se o problema persistir
        print(f"Erro ao enviar mensagem para {destinatario}: {e}")

# --- 3. SIMULAÇÃO DE EXECUÇÃO (COM NÚMEROS CORRIGIDOS) ---

if __name__ == "__main__":
    print(">>> Agente de Atendimento iniciado. Simulando recebimento de mensagens...")

    # Simulação 1: Contato autorizado, pergunta sobre horário
    processar_mensagem("5541997069783", "Olá, qual o horário de funcionamento?")

    # Simulação 2: Contato autorizado (nome), pergunta desconhecida
    # Nota: O envio para "Lovezona" depende de como o pywhatkit encontra o contato.
    # Se ele não abrir a conversa correta, usar o número de telefone é mais garantido.
    processar_mensagem("Lovezona", "Vocês vendem café?")

    # Simulação 3: Contato não autorizado
    processar_mensagem("5511988887777", "Oi, tudo bem?")
    
    # Simulação 4: Contato autorizado, pede para falar com atendente
    processar_mensagem("5541997069783", "Quero falar com um vendedor por favor")

    print("\n>>> Simulação concluída.")
