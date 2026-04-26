# AtendeBot — Agente Conversacional de SAC

**Agente conversacional para Serviço de Atendimento ao Cliente da TeleConecta Brasil**

Projeto acadêmico de desenvolvimento de agente conversacional aplicado a um cenário empresarial de telecomunicações.

## Visão Geral

O AtendeBot é um chatbot de SAC que atende clientes da operadora fictícia TeleConecta Brasil. Ele utiliza técnicas de Processamento de Linguagem Natural (PLN) e Aprendizado de Máquina (ML) para:

- Classificar intenções do usuário (TF-IDF + Similaridade de Cosseno)
- Extrair entidades (CPF, tipo de serviço, tipo de problema)
- Gerenciar diálogo com máquina de estados finita
- Acessar banco de dados simulado (SQLite) para consultas de planos, faturas e chamados

## Estrutura do Projeto

```
projeto/
├── README.md                  # Este arquivo
├── requirements.txt           # Dependências Python
├── app/
│   ├── main.py               # Servidor Flask (ponto de entrada)
│   ├── nlp/
│   │   ├── preprocessor.py   # Tokenização, stemming, normalização
│   │   ├── intent_classifier.py  # Classificação de intenções (TF-IDF)
│   │   └── entity_extractor.py   # Extração de entidades (regex)
│   ├── dialogue/
│   │   ├── manager.py        # Gerenciador de diálogo (FSM)
│   │   └── responses.py      # Templates de respostas dinâmicas
│   ├── database/
│   │   └── db.py             # Banco de dados simulado (SQLite)
│   ├── templates/
│   │   └── index.html        # Interface web do chat
│   └── static/
│       ├── css/style.css     # Estilos da interface
│       └── js/chat.js        # Lógica do frontend
├── data/
│   └── training_data.json    # Dados de treinamento (intents + FAQ)
├── docs/
│   ├── cenario.md            # Descrição do cenário
│   ├── fluxo_conversacional.md  # Fluxograma do agente
│   ├── tecnologias.md        # Tecnologias adotadas
│   └── plano_avaliacao.md    # Plano de avaliação
└── tests/
    └── test_agent.py         # Testes automatizados
```

## Como Executar

### 1. Instalar dependências

```bash
pip install -r requirements.txt
```

### 2. Iniciar o agente

```bash
cd projeto
python -m app.main
```

### 3. Acessar a interface

Abra o navegador em: **http://localhost:5000**

### 4. CPFs de teste

O banco de dados vem populado com os seguintes clientes fictícios:

| CPF | Nome | Plano(s) |
|-----|------|----------|
| 123.456.789-01 | Maria Silva | Essencial Móvel + Fibra 300 |
| 987.654.321-00 | João Santos | Premium Móvel |
| 111.222.333-44 | Ana Oliveira | Combo Família |
| 555.666.777-88 | Carlos Pereira | Fibra 100 |
| 999.888.777-66 | Patrícia Costa | Básico Móvel |

## Executar Testes

```bash
cd projeto
python -m pytest tests/ -v
```

Ou com unittest:

```bash
cd projeto
python -m unittest tests.test_agent -v
```

## Tecnologias

| Tecnologia | Uso |
|-----------|-----|
| Python 3.10+ | Linguagem principal |
| Flask | Servidor web e API REST |
| scikit-learn | TF-IDF e similaridade de cosseno |
| NLTK | Tokenização, stopwords, stemming RSLP |
| SQLite | Banco de dados simulado |
| HTML/CSS/JS | Interface web do chat |

## Funcionalidades

- **Identificação por CPF** com validação e até 3 tentativas
- **Consulta de planos** contratados
- **Consulta de faturas** com status de pagamento
- **Geração de segunda via** de boleto (simulada)
- **Abertura de chamado técnico** com protocolo e previsão
- **Upgrade de plano** com listagem de opções
- **FAQ** com busca por similaridade
- **Transferência para atendente humano**
- **Fallback inteligente** com limite de tentativas
- **Interface web responsiva** com botões de ação rápida

## Documentação

Consulte a pasta `docs/` para os artefatos do projeto:

1. [Documentação completa e detalhada do projeto](docs/documentacao_completa.md)
2. [Descrição do Cenário](docs/cenario.md)
3. [Fluxo Conversacional](docs/fluxo_conversacional.md)
4. [Tecnologias Adotadas](docs/tecnologias.md)
5. [Plano de Avaliação](docs/plano_avaliacao.md)
