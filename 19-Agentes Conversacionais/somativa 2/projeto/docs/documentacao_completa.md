# Documentação Completa do Projeto AtendeBot

**Agente Conversacional de SAC — TeleConecta Brasil**

---

## Sumário

1. [Visão Geral do Projeto](#1-visão-geral-do-projeto)
2. [Arquitetura do Sistema](#2-arquitetura-do-sistema)
3. [Estrutura de Arquivos](#3-estrutura-de-arquivos)
4. [Módulo de Pré-processamento de Texto](#4-módulo-de-pré-processamento-de-texto-preprocessorpy)
5. [Módulo de Classificação de Intenções](#5-módulo-de-classificação-de-intenções-intent_classifierpy)
6. [Módulo de Extração de Entidades](#6-módulo-de-extração-de-entidades-entity_extractorpy)
7. [Módulo de Gerenciamento de Diálogo](#7-módulo-de-gerenciamento-de-diálogo-managerpy)
8. [Módulo de Respostas Dinâmicas](#8-módulo-de-respostas-dinâmicas-responsespy)
9. [Módulo de Banco de Dados](#9-módulo-de-banco-de-dados-dbpy)
10. [Dados de Treinamento](#10-dados-de-treinamento-training_datajson)
11. [Servidor Web e API](#11-servidor-web-e-api-mainpy)
12. [Interface Web (Frontend)](#12-interface-web-frontend)
13. [Testes Automatizados](#13-testes-automatizados)
14. [Fluxo Completo de uma Conversa](#14-fluxo-completo-de-uma-conversa)
15. [Instruções de Execução](#15-instruções-de-execução)

---

## 1. Visão Geral do Projeto

### O que é o AtendeBot

O AtendeBot é um **agente conversacional de Serviço de Atendimento ao Cliente (SAC)** desenvolvido para a empresa fictícia **TeleConecta Brasil**, uma operadora de telecomunicações que oferece telefonia móvel, internet banda larga e TV por assinatura.

### Problema que resolve

A TeleConecta Brasil recebe aproximadamente 15.000 chamados de clientes por dia. Desses, 60% são consultas simples e repetitivas — como verificação de plano, consulta de fatura e solicitação de segunda via de boleto. O tempo médio de espera para atendimento humano é de 12 minutos, causando insatisfação e uma taxa de abandono de 25%.

O AtendeBot automatiza esse atendimento de primeiro nível, oferecendo:

- Consulta de planos contratados
- Verificação de faturas e status de pagamento
- Geração de segunda via de boleto
- Registro de chamados técnicos
- Oferta de upgrade de planos
- Respostas a perguntas frequentes (FAQ)
- Transferência para atendente humano quando necessário

### Abordagem técnica

O projeto adota uma **abordagem híbrida** que combina três técnicas:

1. **Regras determinísticas** — para saudações, despedidas e extração de entidades estruturadas (CPF, tipo de serviço)
2. **Aprendizado de máquina supervisionado** — para classificação de intenções usando TF-IDF e similaridade de cosseno
3. **Recuperação por similaridade** — para responder perguntas frequentes não cobertas pelas intenções fixas

Essa combinação oferece **previsibilidade** (essencial em SAC, onde respostas imprecisas são inaceitáveis) com **flexibilidade** para compreender variações na linguagem natural dos usuários.

---

## 2. Arquitetura do Sistema

O sistema é organizado em camadas independentes que se comunicam de forma sequencial:

```
┌─────────────────────────────────────────────────────┐
│                   INTERFACE WEB                      │
│              (HTML + CSS + JavaScript)                │
│         Envio de mensagens via fetch API              │
└──────────────────────┬──────────────────────────────┘
                       │ POST /api/chat
                       ▼
┌─────────────────────────────────────────────────────┐
│                 SERVIDOR FLASK                        │
│                   (main.py)                           │
│     Gerencia sessões e roteia para DialogueManager    │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│            GERENCIADOR DE DIÁLOGO                    │
│                (manager.py)                           │
│     Máquina de estados finita (FSM)                  │
│     Controla o fluxo e contexto da conversa          │
│                                                      │
│  ┌──────────────┐  ┌───────────────┐                │
│  │ Classificador │  │   Extrator    │                │
│  │ de Intenções  │  │ de Entidades  │                │
│  │  (TF-IDF)    │  │   (regex)     │                │
│  └──────┬───────┘  └──────┬────────┘                │
│         │                 │                          │
│         ▼                 ▼                          │
│  ┌────────────────────────────────┐                  │
│  │   Pré-processador de Texto    │                  │
│  │  (tokenização, stemming RSLP, │                  │
│  │   stopwords, normalização)    │                  │
│  └────────────────────────────────┘                  │
└──────────────────────┬──────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────┐
│              BANCO DE DADOS SQLite                   │
│                   (db.py)                            │
│   Tabelas: clientes, planos, contratos,             │
│            faturas, chamados                         │
└─────────────────────────────────────────────────────┘
```

### Fluxo de processamento de uma mensagem

1. O **frontend** envia a mensagem do usuário via `POST /api/chat` como JSON
2. O **servidor Flask** identifica a sessão e delega ao `DialogueManager` correspondente
3. O `DialogueManager` executa simultaneamente:
   - **Classificação de intenção**: pré-processa o texto e calcula a similaridade com os padrões de treinamento
   - **Extração de entidades**: aplica expressões regulares e dicionários de sinônimos
4. Com base no **estado atual** da conversa, na intenção e nas entidades, o gerenciador decide a ação
5. Se necessário, consulta o **banco de dados** (planos, faturas, etc.)
6. O módulo de **respostas** formata a resposta com os dados obtidos
7. A resposta é retornada como JSON ao frontend, que a exibe na interface de chat

---

## 3. Estrutura de Arquivos

```
projeto/
├── README.md                         # Guia rápido do projeto
├── requirements.txt                  # Dependências Python
│
├── app/                              # Código-fonte principal
│   ├── __init__.py
│   ├── main.py                       # Servidor Flask (ponto de entrada)
│   │
│   ├── nlp/                          # Módulos de PLN
│   │   ├── __init__.py
│   │   ├── preprocessor.py           # Pré-processamento de texto (Tokenização, stemming, normalização)
│   │   ├── intent_classifier.py      # Classificação de intenções (TF-IDF)
│   │   └── entity_extractor.py       # Extração de entidades (regex)
│   │
│   ├── dialogue/                     # Módulos de diálogo
│   │   ├── __init__.py
│   │   ├── manager.py                # Gerenciador de diálogo (FSM)
│   │   └── responses.py              # Templates de respostas dinâmicas
│   │
│   ├── database/                     # Camada de dados
│   │   ├── __init__.py
│   │   └── db.py                     # Banco SQLite simulado
│   │
│   ├── templates/
│   │   └── index.html                # Página HTML do chat
│   │
│   └── static/
│       ├── css/style.css             # Estilos visuais
│       └── js/chat.js                # Lógica do frontend
│
├── data/
│   └── training_data.json            # Dados de treinamento (intents + FAQ)
│
├── docs/                             # Documentação completa
│   ├── cenario.md                    # Descrição do cenário
│   ├── fluxo_conversacional.md       # Fluxograma (Mermaid)
│   ├── tecnologias.md                # Tecnologias utilizadas
│   ├── plano_avaliacao.md            # Plano de avaliação
│   └── documentacao_completa.md      # Este arquivo
│
└── tests/
    ├── __init__.py
    └── test_agent.py                 # Testes automatizados (24 testes)
```

---

## 4. Módulo de Pré-processamento de Texto (`preprocessor.py`)

**Localização:** `app/nlp/preprocessor.py`

Este módulo é responsável por transformar o texto bruto do usuário em uma representação normalizada adequada para as etapas de classificação e busca. O pré-processamento é fundamental em PLN porque reduz a variabilidade do texto, permitindo que frases como "Qual é o meu PLANO?" e "qual meu plano" sejam tratadas como equivalentes.

### Pipeline de pré-processamento

A função `preprocess(text)` executa as seguintes etapas em sequência:

**Etapa 1 — Conversão para minúsculas e remoção de espaços extras**

```python
text = text.lower().strip()
```

Exemplo: `"  Qual é o Meu PLANO?  "` → `"qual é o meu plano?"`

**Etapa 2 — Remoção de acentos**

```python
text = remove_accents(text)
```

Utiliza a biblioteca padrão `unicodedata` para decompor caracteres acentuados (normalização NFKD) e remover os diacríticos. Isso torna o sistema robusto a variações como "não"/"nao" ou "você"/"voce", comuns em digitação informal.

Exemplo: `"qual é o meu plano?"` → `"qual e o meu plano?"`

**Etapa 3 — Remoção de pontuação e números**

```python
text = re.sub(r"[{}]".format(re.escape(string.punctuation)), " ", text)
text = re.sub(r"\d+", " ", text)
```

Pontuação e números são substituídos por espaços. Os números são removidos porque a classificação de intenções não depende deles (entidades numéricas como CPF são extraídas separadamente pelo `entity_extractor`).

Exemplo: `"qual e o meu plano?"` → `"qual e o meu plano"`

**Etapa 4 — Tokenização**

```python
tokens = word_tokenize(text, language="portuguese")
```

Usa o tokenizador do NLTK configurado para português, que segmenta o texto em unidades léxicas (tokens). O parâmetro `language="portuguese"` garante que contrações e expressões do português sejam tratadas corretamente.

Exemplo: `"qual e o meu plano"` → `["qual", "e", "o", "meu", "plano"]`

**Etapa 5 — Remoção de stopwords**

```python
tokens = [t for t in tokens if t not in _effective_stopwords and len(t) > 1]
```

Stopwords são palavras muito frequentes que não contribuem para distinguir intenções — como artigos ("o", "a", "os"), preposições ("de", "para", "em") e conjunções ("e", "ou"). O NLTK fornece uma lista de 207 stopwords em português.

**Decisão de projeto importante:** nem todas as stopwords padrão são removidas. Palavras como "não", "sem", "qual", "quero", "meu" e "minha" são **mantidas** porque carregam semântica fundamental para o contexto de SAC:

```python
_keep_words = {
    "não", "nao", "sem", "mais", "menos", "quando", "como",
    "qual", "quero", "preciso", "meu", "minha",
}
_effective_stopwords = _stopwords_pt - _keep_words
```

Sem essa customização, frases como "não funciona" perderiam o "não" e se tornariam simplesmente "funciona", invertendo completamente o significado.

Exemplo: `["qual", "e", "o", "meu", "plano"]` → `["qual", "meu", "plano"]`

**Etapa 6 — Stemming RSLP**

```python
tokens = [_stemmer.stem(t) for t in tokens]
```

O **stemming** reduz cada palavra ao seu radical (stem), removendo sufixos flexionais e derivacionais. O algoritmo **RSLP (Removedor de Sufixos da Língua Portuguesa)**, de Viviane Moreira Orengo, é específico para português e aplica regras morfológicas da língua, diferentemente de stemmers genéricos como o Porter (projetado para inglês).

Exemplos de stems RSLP:
- "planos" → "plan"
- "faturas" → "fatur"
- "minha" → "minh"
- "internet" → "internet"
- "cancelar" → "cancel"

Com o stemming, "quero ver meus planos" e "quero ver meu plano" produzem o mesmo resultado após pré-processamento, aumentando a capacidade de generalização do classificador.

Exemplo final: `["qual", "meu", "plano"]` → `["qual", "meu", "plan"]`

### Funções auxiliares

- `remove_accents(text)` — Remove acentos usando decomposição Unicode NFKD
- `tokenize_simple(text)` — Tokenização básica sem stemming, utilizada na extração de entidades onde o texto original importa

---

## 5. Módulo de Classificação de Intenções (`intent_classifier.py`)

**Localização:** `app/nlp/intent_classifier.py`

Este módulo é o núcleo de compreensão de linguagem natural do AtendeBot. Ele recebe a mensagem do usuário e determina qual **intenção** (intent) ela expressa — por exemplo, se o cliente quer consultar um plano, verificar uma fatura ou relatar um problema técnico.

### Algoritmo: TF-IDF + Similaridade de Cosseno

A classificação utiliza uma abordagem baseada em **recuperação por similaridade**, onde a mensagem do usuário é comparada a um corpus de frases de treinamento e recebe a mesma intenção da frase mais similar.

#### TF-IDF (Term Frequency-Inverse Document Frequency)

O TF-IDF é uma técnica de vetorização de texto que transforma frases em vetores numéricos, onde cada dimensão corresponde a um termo do vocabulário e o valor reflete a importância relativa desse termo.

A fórmula combina dois fatores:

- **TF (Term Frequency)**: frequência do termo no documento. Termos que aparecem mais vezes em uma frase têm maior peso.
- **IDF (Inverse Document Frequency)**: inverso da frequência do termo no corpus inteiro. Termos que aparecem em muitos documentos (menos discriminativos) recebem menor peso.

```
TF-IDF(t, d) = TF(t, d) × log(N / DF(t))
```

Na prática, a palavra "plano" terá peso alto em frases sobre planos porque é frequente nelas (TF alto) mas não aparece em frases de saudação (IDF moderado). Já a palavra "meu" aparece em muitas intenções diferentes e recebe peso menor (IDF baixo).

#### Similaridade de Cosseno

Após vetorizar a mensagem do usuário e todas as frases de treinamento, calculamos a **similaridade de cosseno** entre o vetor da mensagem e cada vetor do corpus:

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

O resultado varia de 0 (nenhuma semelhança) a 1 (idênticos). A intenção atribuída é a da frase de treinamento com a **maior similaridade de cosseno**.

### Inicialização da classe `IntentClassifier`

Ao ser instanciado, o classificador executa:

1. **Carrega** o arquivo `training_data.json` com todas as intenções e padrões
2. **Pré-processa** cada frase de treinamento usando o pipeline do `preprocessor.py`
3. **Treina** o `TfidfVectorizer` do scikit-learn, construindo a matriz TF-IDF do corpus
4. **Repete** o processo para a base de FAQ (separada), usada como fallback

```python
self._vectorizer = TfidfVectorizer()
self._tfidf_matrix = self._vectorizer.fit_transform(self._corpus)
```

O `fit_transform` ajusta o vocabulário (quais palavras existem e seus IDFs) e transforma o corpus em uma matriz esparsa onde cada linha é uma frase e cada coluna é um termo.

### Método `classify(text)`

```python
def classify(self, text: str) -> tuple[str, float]:
```

1. Pré-processa a mensagem do usuário
2. Transforma em vetor TF-IDF usando o mesmo vocabulário do treinamento
3. Calcula a similaridade de cosseno com todas as frases do corpus
4. Retorna a tag da intenção mais similar e o score de confiança

**Limiar de confiança:** se o maior score for inferior a `0.35` (definido em `CONFIDENCE_THRESHOLD`), a mensagem é classificada como `"nao_compreendido"`, evitando respostas incorretas quando o classificador não tem segurança.

### Método `search_faq(text)`

Quando a intenção classificada não corresponde a nenhuma das principais, o sistema tenta buscar uma resposta na **base de FAQ** usando o mesmo mecanismo de TF-IDF + cosseno, mas com um corpus e vocabulário separados. O limiar para FAQ é mais permissivo (`0.25`) porque as perguntas da FAQ tendem a ser mais longas e descritivas.

### Exemplo prático

Mensagem do usuário: **"Qual é o valor da minha conta?"**

1. Pré-processamento: `"qual valor minh cont"` (minúsculas, sem acentos, stemming)
2. Vetorização TF-IDF: vetor numérico com pesos para cada termo
3. Comparação com corpus:
   - `"qual valor minh fatur"` (consultar_fatura) → score 0.82
   - `"quant minh cont"` (consultar_fatura) → score 0.71
   - `"segund vi"` (segunda_via) → score 0.12
4. Resultado: `("consultar_fatura", 0.82)`

---

## 6. Módulo de Extração de Entidades (`entity_extractor.py`)

**Localização:** `app/nlp/entity_extractor.py`

Enquanto o classificador de intenções determina **o que** o usuário quer fazer, o extrator de entidades identifica **os dados específicos** mencionados na mensagem. Por exemplo, na frase "Minha internet está lenta", a intenção é `problema_tecnico`, e as entidades extraídas são `tipo_servico=internet` e `tipo_problema=lentidao`.

### Entidades extraídas

#### 1. CPF (`extract_cpf`)

Utiliza a expressão regular:

```python
CPF_PATTERN = re.compile(r"(\d{3}[\.\s]?\d{3}[\.\s]?\d{3}[\-\s]?\d{2})")
```

Esta regex aceita CPFs em diversos formatos:
- Com pontos e traço: `123.456.789-01`
- Apenas números: `12345678901`
- Com espaços: `123 456 789 01`

Após a captura, todos os caracteres não-numéricos são removidos, e verifica-se que restam exatamente 11 dígitos.

A função `validate_cpf(cpf)` realiza uma validação simplificada: verifica que o CPF tem 11 dígitos e que não são todos iguais (como `111.111.111-11`, que é inválido).

#### 2. Tipo de Serviço (`extract_tipo_servico`)

Utiliza um **dicionário de sinônimos** que mapeia variações coloquiais e abreviações para três categorias canônicas:

| Palavras-chave reconhecidas | Entidade canônica |
|---|---|
| internet, net, wifi, wi-fi, fibra, banda larga, roteador, modem | `internet` |
| celular, cel, telefone, móvel, linha, chip | `celular` |
| tv, televisão, canais, canal | `tv` |

O mapeamento funciona por busca de substring no texto em minúsculas. Isso permite que frases como "meu cel tá sem sinal" ou "a net caiu" sejam corretamente interpretadas.

#### 3. Tipo de Problema (`extract_tipo_problema`)

Similar ao tipo de serviço, mapeia descrições coloquiais de problemas para três categorias:

| Palavras-chave | Entidade canônica | Significado |
|---|---|---|
| lenta, lento, devagar, velocidade baixa | `lentidao` | Problema de performance |
| caiu, caindo, cai, queda, instável, oscilando | `queda` | Interrupções intermitentes |
| sem sinal, não funciona, parou, não liga, fora do ar | `sem_sinal` | Serviço completamente parado |

#### 4. Mês de Referência (`extract_mes`)

Reconhece nomes de meses em português (completos e abreviados) e a expressão relativa "mês passado". Isso permite que o cliente pergunte, por exemplo, "Qual a fatura de março?" e o sistema filtre corretamente as faturas daquele mês.

### Função `extract_all(text)`

Executa todos os extratores em paralelo e retorna um dicionário com todas as entidades encontradas:

```python
{
    "cpf": "12345678901",       # ou None
    "tipo_servico": "internet", # ou None
    "tipo_problema": "lentidao",# ou None
    "mes_referencia": 3,        # ou None
}
```

---

## 7. Módulo de Gerenciamento de Diálogo (`manager.py`)

**Localização:** `app/dialogue/manager.py`

Este é o módulo central que orquestra toda a conversa. Ele implementa uma **Máquina de Estados Finita (FSM — Finite State Machine)** que controla o fluxo conversacional, garantindo que o agente saiba em que ponto da conversa está e qual é a ação esperada.

### Estados da FSM

O agente possui **6 estados**, definidos como um `Enum`:

```python
class State(Enum):
    INICIO = auto()
    AGUARDANDO_CPF = auto()
    IDENTIFICADO = auto()
    COLETANDO_PROBLEMA_SERVICO = auto()
    COLETANDO_PROBLEMA_DETALHE = auto()
    AGUARDANDO_UPGRADE_ESCOLHA = auto()
```

| Estado | Descrição | Próximo estado possível |
|--------|-----------|------------------------|
| `INICIO` | Estado inicial; nenhum cliente identificado | → `AGUARDANDO_CPF` |
| `AGUARDANDO_CPF` | Agente solicitou o CPF e aguarda resposta | → `IDENTIFICADO` ou → `INICIO` (falha) |
| `IDENTIFICADO` | Cliente autenticado; agente processa intenções | → vários, dependendo da intenção |
| `COLETANDO_PROBLEMA_SERVICO` | Agente precisa saber qual serviço tem problema | → `COLETANDO_PROBLEMA_DETALHE` ou → `IDENTIFICADO` |
| `COLETANDO_PROBLEMA_DETALHE` | Agente precisa saber que tipo de problema é | → `IDENTIFICADO` |
| `AGUARDANDO_UPGRADE_ESCOLHA` | Agente mostrou planos e aguarda escolha | → `IDENTIFICADO` |

### Contexto da conversa

Além do estado, o gerenciador mantém um dicionário de **contexto** com informações acumuladas ao longo da conversa:

```python
self.context = {
    "cliente": None,              # Dados do cliente autenticado (dict com id, nome, cpf, etc.)
    "tentativas_cpf": 0,          # Contador de tentativas de CPF inválido
    "tentativas_fallback": 0,     # Contador de mensagens não compreendidas
    "tipo_servico_problema": None, # Serviço com problema (preenchido progressivamente)
    "tipo_problema": None,         # Tipo de problema (preenchido progressivamente)
    "ultimo_intent": None,         # Última intenção identificada
}
```

### Método principal: `process_message(user_message)`

Este é o ponto de entrada para cada mensagem do usuário. O fluxo é:

1. **Extrai entidades** da mensagem (CPF, serviço, problema, mês)
2. **Classifica a intenção** (tag + score de confiança)
3. **Delega para o handler** do estado atual

Cada estado tem seu próprio handler:

#### `_handle_inicio` — Estado INICIO

Trata a primeira mensagem do usuário. Se o texto já contém um CPF, tenta identificar imediatamente. Caso contrário, exibe mensagem de boas-vindas e transiciona para `AGUARDANDO_CPF`.

#### `_handle_aguardando_cpf` — Estado AGUARDANDO_CPF

Tenta extrair o CPF da mensagem. Se não consegue, incrementa o contador de tentativas. Após **3 tentativas**, transfere automaticamente para atendente humano — evitando frustração do cliente.

Estratégia de extração progressiva:
1. Tenta `extract_cpf()` (regex formal)
2. Se falhar, extrai apenas dígitos e verifica se há 11
3. Valida o CPF encontrado
4. Busca no banco de dados

#### `_try_identify` — Identificação do cliente

Busca o CPF no banco de dados. Se encontra, armazena os dados do cliente no contexto, zera contadores e transiciona para `IDENTIFICADO`. A mensagem de boas-vindas inclui o **primeiro nome** do cliente e um menu de opções.

#### `_handle_identificado` — Estado IDENTIFICADO (estado principal)

Este é o handler mais complexo, pois trata todas as intenções do cliente autenticado. A lógica segue uma cadeia de `if/elif`:

| Intenção | Ação |
|----------|------|
| `consultar_plano` | Consulta `buscar_planos_cliente()` no banco e formata resposta |
| `consultar_fatura` | Consulta `buscar_faturas_cliente()` com filtro opcional de mês |
| `segunda_via` | Busca contrato ativo e gera link simulado com `gerar_segunda_via()` |
| `problema_tecnico` | Se tem serviço **e** problema: cria chamado. Senão: pede detalhes |
| `upgrade_plano` | Lista planos disponíveis e transiciona para `AGUARDANDO_UPGRADE_ESCOLHA` |
| `falar_atendente` | Transfere para humano e reseta sessão |
| `faq_*` | Retorna resposta pré-definida para cobertura, cancelamento ou horário |
| `agradecimento` | Responde educadamente e pergunta se precisa de mais algo |
| `despedida` | Encerra conversa e reseta sessão |
| `saudacao` | Cumprimenta pelo nome (já identificado) |
| Não compreendido | Tenta FAQ por similaridade; se falhar, pede reformulação ou transfere |

**Mecanismo de fallback:** se o classificador não identifica a intenção, o sistema tenta a busca de FAQ. Se também falhar, o contador `tentativas_fallback` é incrementado. Na **segunda falha consecutiva**, o agente transfere para atendente humano.

#### `_handle_coletando_servico` — Coleta progressiva de informações técnicas

Quando o cliente reporta um problema mas não especifica qual serviço, o agente entra neste estado para perguntar. Assim que o serviço é identificado, verifica se o problema também foi mencionado; se sim, cria o chamado; se não, transiciona para `COLETANDO_PROBLEMA_DETALHE`.

#### `_handle_coletando_detalhe` — Coleta do tipo de problema

Similar ao anterior, mas para o detalhe do problema. Se o cliente não especificar claramente, o sistema assume `"sem_sinal"` como padrão — pois "não funciona" é a queixa mais genérica e comum.

#### `_handle_upgrade_escolha` — Seleção de plano

Após listar os planos, o agente aguarda que o cliente escolha um. O handler reconhece:
- **Negativa** ("não", "cancelar", "voltar") → volta ao estado `IDENTIFICADO`
- **Nome de plano** → confirma a alteração (simulada)
- **Confirmação genérica** ("sim", "quero") → pede para especificar qual plano
- **Qualquer outra coisa** → informa que não entendeu e volta ao `IDENTIFICADO`

---

## 8. Módulo de Respostas Dinâmicas (`responses.py`)

**Localização:** `app/dialogue/responses.py`

Este módulo centraliza a **geração de respostas** do agente. Diferentemente das respostas fixas (como saudações), as respostas dinâmicas são montadas com dados reais do banco de dados e contextualizadas para cada cliente.

### Dicionários de tradução

O módulo define constantes para traduzir códigos internos em textos legíveis:

- `MESES_PT` — mapeia números de meses para nomes em português
- `STATUS_PT` — mapeia status de fatura para texto com emojis visuais (✅ Pago, ⏳ Pendente, 🔴 Atrasado)
- `TIPO_SERVICO_PT` — mapeia códigos de serviço para nomes completos
- `TIPO_PROBLEMA_PT` — mapeia códigos de problema para descrições

### Funções de resposta

Cada função recebe dados do banco e retorna uma string formatada:

- `resposta_planos(nome, planos)` — Lista os planos do cliente com nome, tipo, velocidade, franquia, descrição, preço e data de contratação
- `resposta_faturas(nome, faturas)` — Lista faturas com plano, mês/ano, valor, vencimento e status
- `resposta_segunda_via(dados)` — Exibe link de pagamento simulado e código de barras
- `resposta_chamado_criado(dados, servico, problema)` — Confirma abertura de chamado com protocolo, serviço, problema, data e previsão
- `resposta_upgrade(planos, filtro)` — Lista planos disponíveis agrupados por categoria
- `resposta_upgrade_confirmado(plano)` — Confirma alteração de plano
- `resposta_problema_pedir_detalhes(tipo)` — Solicita informações faltantes sobre o problema

As respostas usam formatação Markdown (bold com `**`) e emojis para melhorar a legibilidade na interface web.

---

## 9. Módulo de Banco de Dados (`db.py`)

**Localização:** `app/database/db.py`

Este módulo simula o sistema de informação da TeleConecta Brasil usando **SQLite**, um banco de dados relacional embutido no Python que não requer instalação de servidor.

### Modelo de dados (5 tabelas)

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   clientes   │     │    planos    │     │   chamados   │
├──────────────┤     ├──────────────┤     ├──────────────┤
│ id (PK)      │     │ id (PK)      │     │ id (PK)      │
│ cpf (UNIQUE) │     │ nome         │     │ cliente_id   │→ clientes
│ nome         │     │ tipo         │     │ tipo_servico │
│ email        │     │ velocidade   │     │ tipo_problema│
│ telefone     │     │ franquia     │     │ descricao    │
└──────┬───────┘     │ preco        │     │ protocolo    │
       │             │ descricao    │     │ status       │
       │             └──────┬───────┘     │ data_abertura│
       │                    │             │ previsao     │
       ▼                    ▼             └──────────────┘
┌──────────────────────────────┐
│          contratos           │
├──────────────────────────────┤
│ id (PK)                      │
│ cliente_id (FK) → clientes   │
│ plano_id (FK) → planos       │
│ data_inicio                  │
│ status                       │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│           faturas            │
├──────────────────────────────┤
│ id (PK)                      │
│ contrato_id (FK) → contratos │
│ mes_referencia               │
│ ano_referencia               │
│ valor                        │
│ vencimento                   │
│ status                       │
│ codigo_barras                │
└──────────────────────────────┘
```

### Dados de demonstração (seed)

O banco é populado automaticamente na primeira execução com:

**9 planos** distribuídos em 4 categorias:

| Plano | Tipo | Preço |
|-------|------|-------|
| Básico Móvel | celular | R$ 39,90 |
| Essencial Móvel | celular | R$ 59,90 |
| Premium Móvel | celular | R$ 99,90 |
| Fibra 100 | internet | R$ 89,90 |
| Fibra 300 | internet | R$ 119,90 |
| Fibra 500 | internet | R$ 149,90 |
| TV Essencial | tv | R$ 69,90 |
| TV Premium | tv | R$ 119,90 |
| Combo Família | combo | R$ 199,90 |

**5 clientes:**

| CPF | Nome | Plano(s) |
|-----|------|----------|
| 12345678901 | Maria Silva | Essencial Móvel + Fibra 300 |
| 98765432100 | João Santos | Premium Móvel |
| 11122233344 | Ana Oliveira | Combo Família |
| 55566677788 | Carlos Pereira | Fibra 100 |
| 99988877766 | Patrícia Costa | Básico Móvel |

**Faturas:** 3 meses de faturas para cada contrato, com status aleatório (pago/pendente) para o mês atual e "pago" para meses anteriores.

### Funções de consulta

- `buscar_cliente_por_cpf(cpf)` — Retorna dados do cliente ou `None`
- `buscar_planos_cliente(cliente_id)` — Retorna planos ativos via JOIN com contratos
- `buscar_faturas_cliente(cliente_id, mes=None)` — Retorna até 6 faturas recentes, com filtro opcional por mês
- `buscar_planos_upgrade(tipo=None)` — Lista todos os planos ou filtra por tipo de serviço
- `criar_chamado(cliente_id, servico, problema, descricao)` — Insere chamado técnico com protocolo único gerado automaticamente (formato: `TC` + data + 4 dígitos) e previsão de resolução aleatória (24h, 48h ou 72h)
- `gerar_segunda_via(contrato_id)` — Simula geração de boleto com link e código de barras fictícios

---

## 10. Dados de Treinamento (`training_data.json`)

**Localização:** `data/training_data.json`

O arquivo JSON contém dois blocos:

### Bloco `intents` — Intenções

Cada intenção é composta por:
- `tag` — identificador único (ex: `"consultar_plano"`)
- `patterns` — lista de frases de exemplo que expressam essa intenção (usadas para treinar o TF-IDF)
- `responses` — lista de respostas possíveis (quando aplicável; intenções dinâmicas como `consultar_plano` têm respostas vazias porque são montadas pelo `responses.py`)

**Total: 12 intenções com 198 frases de treinamento:**

| Intenção | Nº de padrões | Tipo de resposta |
|----------|---------------|------------------|
| `saudacao` | 21 | Fixa (3 variações) |
| `consultar_plano` | 19 | Dinâmica (banco de dados) |
| `consultar_fatura` | 24 | Dinâmica (banco de dados) |
| `segunda_via` | 18 | Dinâmica (banco de dados) |
| `problema_tecnico` | 35 | Dinâmica (banco de dados) |
| `upgrade_plano` | 21 | Dinâmica (banco de dados) |
| `falar_atendente` | 17 | Fixa (3 variações) |
| `faq_cobertura` | 11 | Fixa (1 resposta) |
| `faq_cancelamento` | 10 | Fixa (1 resposta) |
| `faq_horario` | 10 | Fixa (1 resposta) |
| `agradecimento` | 12 | Fixa (3 variações) |
| `despedida` | 17 | Fixa (3 variações) |

Os padrões incluem variações com e sem acento ("não"/"nao"), gírias ("tá", "eae"), abreviações ("vlw", "flw") e diferentes formas de expressar a mesma ideia, garantindo robustez.

### Bloco `faq` — Perguntas Frequentes

5 pares pergunta/resposta para questões que não se encaixam nas intenções principais:

1. Como funciona o plano família?
2. Posso usar meu celular no exterior?
3. Como funciona a portabilidade?
4. Qual a velocidade mínima garantida?
5. Como instalar o roteador Wi-Fi?

Essas perguntas são buscadas por similaridade TF-IDF quando nenhuma intenção principal é identificada, funcionando como um **fallback inteligente** antes de transferir para atendente humano.

---

## 11. Servidor Web e API (`main.py`)

**Localização:** `app/main.py`

O servidor Flask expõe três endpoints:

### `GET /` — Página principal

Retorna o HTML da interface de chat. Gera um `session_id` aleatório para rastreamento da sessão.

### `POST /api/chat` — Envio de mensagem

**Request:**
```json
{
    "message": "qual meu plano?",
    "session_id": "abc123"
}
```

**Response:**
```json
{
    "response": "📋 Maria, aqui estão seus planos ativos:\n...",
    "state": "IDENTIFICADO",
    "identified": true
}
```

O campo `state` indica o estado atual da FSM e `identified` indica se há um cliente autenticado. O frontend usa essas informações para mostrar/ocultar os botões de ação rápida.

### `POST /api/reset` — Reiniciar conversa

Remove o `DialogueManager` da sessão, forçando a criação de uma nova instância na próxima mensagem.

### Gerenciamento de sessões

Cada sessão (identificada por `session_id` do frontend) tem seu próprio `DialogueManager`, permitindo múltiplas conversas simultâneas com estados independentes:

```python
_managers: dict[str, DialogueManager] = {}

def _get_manager(session_id: str) -> DialogueManager:
    if session_id not in _managers:
        _managers[session_id] = DialogueManager()
    return _managers[session_id]
```

---

## 12. Interface Web (Frontend)

### HTML (`index.html`)

A página é composta por:

- **Header** — Logo SVG do robô, nome "AtendeBot", indicador "Online" e botão de reiniciar
- **Área de mensagens** — Container com scroll onde as mensagens são exibidas
- **Ações rápidas** — Barra de botões (Meu Plano, Faturas, 2ª Via, Problema, Upgrade) que aparece após a identificação do cliente
- **Campo de entrada** — Input de texto com botão de enviar

### CSS (`style.css`)

Design moderno inspirado em aplicativos de mensagem como WhatsApp Web:

- **Layout responsivo** — adapta-se a telas de celular (100% width) e desktop (max-width 520px)
- **Bolhas de mensagem** — diferenciadas por cor: azul claro para o bot, azul escuro para o usuário
- **Animação de digitação** — três pontos pulsando enquanto o agente "processa" a resposta
- **Animação de entrada** — mensagens surgem com fade-in suave
- **Ações rápidas** — botões com estilo de "chip" que se transformam ao hover

### JavaScript (`chat.js`)

Lógica do frontend que gerencia a comunicação com o servidor:

- **`sendMessage(text)`** — Função principal: exibe a mensagem do usuário, mostra o indicador de digitação, envia `POST /api/chat` via fetch API, espera um delay proporcional ao tamanho da resposta (simulando "digitação" do bot), e exibe a resposta
- **`formatMessage(text)`** — Converte Markdown simplificado (`**bold**` e `` `code` ``) em HTML
- **`addMessage(content, isUser)`** — Cria o elemento DOM da mensagem com timestamp
- **Botões de ação rápida** — Cada botão envia uma mensagem pré-definida via `data-message`
- **Botão de reset** — Chama `/api/reset` e limpa a interface
- **Gerenciamento de estado** — Mostra/oculta os botões de ação rápida com base no campo `identified` da resposta da API

---

## 13. Testes Automatizados

**Localização:** `tests/test_agent.py`

O projeto inclui **24 testes automatizados** organizados em 5 classes que cobrem todas as camadas do sistema:

### `TestPreprocessor` (3 testes)

Valida o pré-processamento de texto:
- Remoção de acentos (`"ação"` → `"acao"`)
- Conversão para minúsculas
- Remoção de pontuação

### `TestEntityExtractor` (7 testes)

Valida a extração de entidades:
- CPF formatado (`"123.456.789-01"` → `"12345678901"`)
- CPF sem formatação
- Ausência de CPF em texto genérico
- Validação de CPF válido e inválido (todos dígitos iguais)
- Tipo de serviço (internet, celular, tv, wifi→internet)
- Tipo de problema (lenta→lentidão, caindo→queda, sem sinal→sem_sinal)

### `TestIntentClassifier` (6 testes)

Valida a classificação de intenções:
- Saudação com score > 0.3
- Consulta de plano
- Consulta de fatura
- Problema técnico
- Despedida (aceita "despedida" ou "agradecimento" para "tchau obrigado")
- Mensagem aleatória classificada como não compreendida

### `TestDatabase` (2 testes)

Valida o banco de dados:
- Busca de cliente existente (Maria Silva)
- Busca de cliente inexistente retorna None

### `TestDialogueManager` (6 testes)

Valida fluxos conversacionais completos:
- Saudação inicial transiciona para `AGUARDANDO_CPF`
- CPF válido transiciona para `IDENTIFICADO` e retorna nome
- 3 CPFs inválidos transferem para atendente
- Consulta de plano após identificação
- Consulta de fatura após identificação
- Problema técnico completo (internet + lenta) gera protocolo

### Execução

```bash
cd projeto
python -m unittest tests.test_agent -v
```

---

## 14. Fluxo Completo de uma Conversa

Para ilustrar como todos os módulos trabalham juntos, vamos acompanhar uma conversa real passo a passo:

### Turno 1: Usuário envia "Olá"

```
Frontend → POST /api/chat {"message": "Olá", "session_id": "abc"}
```

1. `DialogueManager.process_message("Olá")` é chamado
2. Estado atual: `INICIO`
3. `extract_all("Olá")` → nenhuma entidade encontrada
4. `classifier.classify("Olá")` → `("saudacao", 0.89)`
5. `_handle_inicio()`: não há CPF → escolhe resposta aleatória de saudação → transiciona para `AGUARDANDO_CPF`

```
Resposta: "Olá! Bem-vindo à TeleConecta Brasil! Sou o AtendeBot.
           Para começar, por favor me informe seu CPF."
```

### Turno 2: Usuário envia "123.456.789-01"

1. Estado atual: `AGUARDANDO_CPF`
2. `extract_all("123.456.789-01")` → `{cpf: "12345678901", ...}`
3. `_handle_aguardando_cpf()`: CPF extraído!
4. `validate_cpf("12345678901")` → `True`
5. `_try_identify("12345678901")`:
   - `db.buscar_cliente_por_cpf("12345678901")` → `{id: 1, nome: "Maria Silva", ...}`
   - Armazena cliente no contexto
   - Transiciona para `IDENTIFICADO`

```
Resposta: "Olá, Maria! Encontrei seu cadastro. Como posso te ajudar hoje?
           • 📋 Consultar seu plano  • 💳 Ver suas faturas ..."
```

### Turno 3: Usuário envia "Minha internet está lenta"

1. Estado atual: `IDENTIFICADO`
2. `extract_all("Minha internet está lenta")`:
   - `tipo_servico`: "internet" (via "internet" no dicionário)
   - `tipo_problema`: "lentidao" (via "lenta" no dicionário)
3. `classifier.classify(...)` → `("problema_tecnico", 0.76)`
4. `_handle_identificado()`:
   - Intent = `problema_tecnico`
   - Tem tipo_servico **E** tipo_problema → cria chamado diretamente!
   - `db.criar_chamado(1, "internet", "lentidao", "Minha internet está lenta")`
   - Retorna protocolo `TC202604263847`, previsão 48h

```
Resposta: "🔧 Chamado técnico registrado com sucesso!
           Protocolo: TC202604263847
           Serviço: Internet
           Problema: Lentidão na conexão
           Previsão de resolução: 2026-04-28 00:20"
```

### Turno 4: Usuário envia "Obrigado, tchau"

1. `classifier.classify("Obrigado, tchau")` → `("despedida", 0.72)`
2. Reseta sessão (cliente = None, estado = INICIO)

```
Resposta: "Tchau! Obrigado pela preferência TeleConecta Brasil.
           Volte sempre que precisar!"
```

---

## 15. Instruções de Execução

### Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

```bash
# 1. Entrar no diretório do projeto
cd projeto

# 2. (Opcional) Criar ambiente virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# 3. Instalar dependências
pip install -r requirements.txt

# 4. Baixar dados do NLTK (executado automaticamente na primeira execução)
python -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('rslp')"
```

### Execução

```bash
python -m app.main
```

O servidor inicia em `http://localhost:5000`. O banco de dados é criado e populado automaticamente.

### Testes

```bash
python -m unittest tests.test_agent -v
```

### CPFs para teste

| CPF | Cliente |
|-----|---------|
| 12345678901 | Maria Silva (2 planos) |
| 98765432100 | João Santos |
| 11122233344 | Ana Oliveira |
| 55566677788 | Carlos Pereira |
| 99988877766 | Patrícia Costa |
