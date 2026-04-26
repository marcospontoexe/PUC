# 3. Descrição das Tecnologias Adotadas

## a) Abordagem de Desenvolvimento

O AtendeBot adota uma **abordagem híbrida** que combina:

1. **Regras determinísticas** para saudações, despedidas e detecção de entidades estruturadas (CPF, tipo de serviço)
2. **Aprendizado de máquina supervisionado** para classificação de intenções (intents)
3. **Recuperação por similaridade** (TF-IDF + cosseno) para perguntas frequentes (FAQ)

Essa abordagem é a mais adequada para o cenário de SAC por oferecer **controle e previsibilidade** nas respostas (essencial em atendimento ao cliente) enquanto mantém **flexibilidade** para compreender variações na linguagem natural dos usuários.

## b) Técnicas de PLN e ML Utilizadas

### Pré-processamento de Texto
- **Tokenização**: segmentação do texto em tokens (palavras)
- **Normalização**: conversão para minúsculas, remoção de acentos e caracteres especiais
- **Remoção de stopwords**: eliminação de palavras sem carga semântica (artigos, preposições)
- **Stemming (RSLP)**: redução de palavras ao radical usando o algoritmo RSLP, específico para português

### Classificação de Intenções
- **TF-IDF (Term Frequency-Inverse Document Frequency)**: vetorização do texto que pondera a importância relativa de cada termo no corpus de treinamento
- **Similaridade de cosseno**: métrica para comparar a semelhança entre o vetor da mensagem do usuário e os vetores das frases de treinamento
- **Classificação por vizinho mais próximo**: a intenção atribuída é a da frase de treinamento com maior similaridade de cosseno acima do limiar de confiança

### Extração de Entidades
- **Expressões regulares (regex)**: padrões para extração de CPF, meses, tipos de serviço
- **Dicionários de sinônimos**: mapeamento de variações linguísticas para entidades canônicas (ex.: "net" → "internet", "cel" → "celular")

### Gerenciamento de Diálogo
- **Máquina de estados finita (FSM)**: controle do fluxo conversacional com estados e transições determinísticas
- **Context tracking**: manutenção de contexto da conversa (cliente identificado, último serviço consultado, etc.)

## c) Bibliotecas/Pacotes/Frameworks Utilizados

| Biblioteca | Versão | Função | Justificativa |
|-----------|--------|--------|---------------|
| **Flask** | 3.0+ | Framework web para interface e API | Leve, simples e amplamente utilizado para prototipagem de APIs em Python |
| **scikit-learn** | 1.4+ | TF-IDF e similaridade de cosseno | Referência em ML para Python; implementação eficiente e bem documentada |
| **NLTK** | 3.8+ | Tokenização, stopwords, stemming RSLP | Biblioteca clássica de PLN com suporte robusto ao português (stemmer RSLP, stopwords pt) |
| **unidecode** | 1.3+ | Remoção de acentos | Normalização eficiente de texto em português |
| **SQLite3** | (stdlib) | Banco de dados simulado | Embutido no Python, não requer instalação; ideal para simular o banco de dados da operadora |

## d) Plataforma Conversacional

O agente é disponibilizado através de uma **interface web própria** desenvolvida com:

- **Backend**: Flask (Python) servindo uma API REST
- **Frontend**: HTML5 + CSS3 + JavaScript vanilla
- **Comunicação**: requisições AJAX (fetch API) para troca de mensagens em tempo real

### Justificativa da Plataforma

A escolha de uma interface web própria (ao invés de plataformas como Dialogflow, Watson ou Telegram) se justifica por:

1. **Independência de plataforma**: não depende de serviços de terceiros nem de chaves de API externas
2. **Controle total**: permite personalizar completamente a experiência do usuário
3. **Foco educacional**: demonstra a construção completa do pipeline de PLN, desde o pré-processamento até a geração de resposta
4. **Portabilidade**: funciona em qualquer navegador moderno sem instalação adicional
5. **Facilidade de execução**: `python main.py` é suficiente para iniciar o agente

## e) Justificativa Geral das Tecnologias

A escolha tecnológica prioriza:

- **Transparência**: cada componente (classificação, extração, diálogo) é implementado de forma explícita, permitindo entender e auditar o comportamento do agente
- **Reprodutibilidade**: não depende de APIs pagas, chaves de acesso ou serviços cloud
- **Adequação ao cenário**: para SAC, onde as respostas devem ser precisas e controladas, uma abordagem baseada em ML supervisionado com regras é mais confiável do que modelos generativos (LLMs), que podem gerar respostas imprecisas ou inventadas (hallucination)
- **Desempenho**: o agente responde em menos de 100ms, atendendo ao requisito de resposta rápida para SAC
- **Escalabilidade do corpus**: novas intenções e respostas podem ser adicionadas simplesmente editando o arquivo de dados de treinamento JSON, sem necessidade de retreinar modelos complexos
