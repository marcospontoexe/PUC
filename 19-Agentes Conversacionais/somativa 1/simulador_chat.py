# ---------------------------------------------------------------------------
# AGENTE DE ATENDIMENTO (SIMULADOR DE TERMINAL)
# ---------------------------------------------------------------------------
# Baseado na estrutura do "Exemplo_1_Chatbot_baseado_em_regras.ipynb".
# Este script simula o atendimento a um cliente de uma loja de
# purificadores de água diretamente no terminal.
# ---------------------------------------------------------------------------

import re
import random

# --- 1. DEFINIÇÃO DAS REGRAS (PADRÕES E RESPOSTAS) ---
# Cada regra é um dicionário contendo um padrão (regex) e uma lista de respostas.

regras = [
    {
        "padrao": r'oi|olá|bom\s+dia|boa\s+tarde|boa\s+noite',
        "respostas": ["Olá! Sou o assistente virtual da Água Pura. Como posso te ajudar hoje?"]
    },
    {
        "padrao": r'horário|horas|fecha|abre|funciona|atendimento',
        "respostas": ["Nosso horário de atendimento é de segunda a sexta, das 8h30 às 18h, e aos sábados das 9h às 12h."]
    },
    {
        "padrao": r'endereço|onde\s+fica|localização|local',
        "respostas": ["Nossa loja física fica na Rua das Águas Claras, 123 - Centro. Venha nos visitar!"]
    },
    {
        "padrao": r'marca|tipos|modelos|quais\s+purificadores|catálogo',
        "respostas": ["Trabalhamos com excelentes modelos de parede, bancada e com refrigeração. Você tem alguma preferência para eu poder te ajudar melhor?"]
    },
    {
        "padrao": r'preço|valor|custa|quanto|caro|barato',
        "respostas": ["Os valores variam bastante conforme o modelo e suas funcionalidades. Para qual tipo de uso você precisa? (Ex: residencial, comercial)"]
    },
    {
        "padrao": r'instalação|instalar|instalam|montagem',
        "respostas": ["Sim, oferecemos serviço de instalação! A taxa pode variar conforme sua região. Para qual CEP seria?"]
    },
    {
        "padrao": r'manutenção|assistência|conserto|reparo|estrago',
        "respostas": ["Com certeza! Realizamos tanto a manutenção preventiva quanto consertos. O que aconteceu com o seu aparelho?"]
    },
    {
        "padrao": r'refil|troca\s+do\s+filtro|filtro',
        "respostas": ["A troca do refil é essencial e recomendamos, em média, a cada 6 meses. Temos o refil para todos os modelos que vendemos!"]
    },
    {
        "padrao": r'garantia|troca|defeito',
        "respostas": ["Todos os nossos purificadores possuem garantia de fábrica de 12 meses contra defeitos de fabricação."]
    },
    {
        "padrao": r'pagamento|cartão|pix|parcelamento|aceita',
        "respostas": ["Aceitamos PIX, dinheiro e cartões de débito e crédito. Parcelamos em até 10x sem juros, dependendo do modelo!"]
    },
    {
        "padrao": r'entrega|frete|prazo|entregam',
        "respostas": ["Entregamos em toda a cidade! O prazo médio é de 2 dias úteis. Se preferir, pode retirar na loja."]
    },
    {
        "padrao": r'atendente|humano|vendedor|falar\s+com',
        "respostas": ["Entendido. Para falar com um de nossos vendedores, por favor, ligue para (41) 3333-4444 ou aguarde um momento que alguém já irá responder por aqui."]
    },
    {
        "padrao": r'obrigado|agradecido|valeu',
        "respostas": ["De nada! Se precisar de mais alguma coisa, é só chamar."]
    },
    {
        "padrao": r'adeus|tchau|sair',
        "respostas": ["Obrigado pelo seu contato! Tenha um ótimo dia."]
    }
]

# --- 2. FUNÇÃO DE CORRESPONDÊNCIA ---

def encontrar_resposta(mensagem_usuario):
    """
    Percorre as regras para encontrar uma correspondência e retorna uma resposta aleatória.
    """
    for regra in regras:
        # re.search verifica se o padrão existe em qualquer parte da mensagem
        if re.search(regra["padrao"], mensagem_usuario, re.IGNORECASE):
            # random.choice escolhe uma das respostas possíveis
            return random.choice(regra["respostas"])
    
    # Se nenhuma regra corresponder, retorna uma resposta padrão (fallback)
    return "Desculpe, não entendi sua pergunta. Você pode me perguntar sobre: preço, modelos, instalação, refil, garantia, entrega, pagamento, ou horário."

# --- 3. LOOP DE CONVERSAÇÃO ---

def iniciar_chat():
    """
    Inicia o loop principal do chatbot no terminal.
    """
    print("--- Simulador de Atendimento da Loja Água Pura ---")
    print("Assistente: Olá! Sou o assistente virtual. Digite sua dúvida ou 'sair' para encerrar.")
    
    while True:
        # Pede a entrada do usuário
        mensagem = input("Você: ")
        
        # Encerra o chat se o usuário digitar 'sair'
        if mensagem.lower() == 'sair':
            print("Assistente: Obrigado pelo contato. Até logo!")
            break
        
        # Encontra e imprime a resposta do bot
        resposta = encontrar_resposta(mensagem)
        print(f"Assistente: {resposta}")

# --- 4. EXECUÇÃO PRINCIPAL ---

if __name__ == "__main__":
    iniciar_chat()
