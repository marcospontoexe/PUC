# 5. Plano de Avaliação

## a) Tipos e Metodologias de Avaliação

O plano de avaliação do AtendeBot contempla três dimensões complementares:

### 1. Avaliação Técnica (Automática)

**Metodologia**: avaliação quantitativa baseada em métricas de PLN e ML.

**Procedimento**:
- Dividir os dados de treinamento em 80% treino / 20% teste usando *stratified split*
- Executar *cross-validation* com k=5 folds no conjunto de treino
- Avaliar no conjunto de teste reservado
- Testar com frases completamente novas (fora do corpus) para avaliar generalização

**Métricas**:

| Métrica | O que avalia | Meta |
|---------|-------------|------|
| **Acurácia** | Taxa geral de acerto na classificação de intenções | ≥ 85% |
| **Precisão** (por classe) | Proporção de classificações corretas para cada intenção | ≥ 80% |
| **Recall** (por classe) | Proporção de exemplos corretamente identificados por intenção | ≥ 80% |
| **F1-Score** (macro) | Média harmônica entre precisão e recall, balanceada entre classes | ≥ 80% |
| **Matriz de confusão** | Identificação de pares de intenções frequentemente confundidas | Análise qualitativa |
| **Taxa de fallback** | Percentual de mensagens não compreendidas (abaixo do limiar) | ≤ 15% |
| **Tempo de resposta** | Latência média para processar e responder uma mensagem | ≤ 500ms |

### 2. Avaliação Funcional (Testes de Cenário)

**Metodologia**: testes de cenários conversacionais end-to-end, verificando se os fluxos completos funcionam conforme o fluxograma.

**Procedimento**:
- Definir 10-15 cenários de teste cobrindo todos os fluxos do fluxograma
- Cada cenário inclui uma sequência de mensagens do usuário e as respostas esperadas do agente
- Executar cada cenário manualmente e verificar aderência ao comportamento esperado
- Documentar desvios e classificar por severidade (crítico, moderado, leve)

**Cenários de Teste Prioritários**:

| # | Cenário | Fluxo Testado |
|---|---------|---------------|
| 1 | Cliente consulta plano com CPF válido | Identificação → Consulta plano |
| 2 | Cliente consulta fatura do mês atual | Identificação → Consulta fatura |
| 3 | Cliente solicita segunda via de boleto | Identificação → Segunda via |
| 4 | Cliente reporta internet sem funcionar | Identificação → Problema técnico → Chamado |
| 5 | Cliente pede upgrade de plano e aceita | Identificação → Upgrade → Confirmação |
| 6 | Cliente pede upgrade e recusa | Identificação → Upgrade → Recusa → Retorno |
| 7 | CPF inválido 3 vezes consecutivas | Validação → Fallback → Atendente |
| 8 | Mensagem não compreendida 2 vezes | Classificação → Fallback → Atendente |
| 9 | Cliente pede para falar com atendente | Transferência direta |
| 10 | Conversa completa com múltiplas intenções | Fluxo multi-turno |
| 11 | Cliente usa gírias e abreviações | Robustez do PLN |
| 12 | Cliente envia mensagem com erros de digitação | Tolerância a erros |

### 3. Avaliação de Usabilidade (com Usuários)

**Metodologia**: avaliação qualitativa com usuários reais seguindo o modelo **SUS (System Usability Scale)** adaptado para agentes conversacionais, combinado com **entrevistas semiestruturadas**.

**Participantes**: 10-15 usuários com perfis variados:
- 5 usuários com alta familiaridade com chatbots
- 5 usuários com baixa familiaridade com chatbots
- 3-5 usuários da faixa etária 50+

**Procedimento**:
1. Briefing: explicar o contexto e as tarefas a realizar (sem revelar detalhes técnicos)
2. Execução: cada usuário realiza 3-5 tarefas predefinidas com o agente
3. Questionário SUS adaptado (10 questões, escala Likert 1-5)
4. Entrevista semiestruturada (5-10 minutos)

**Tarefas para os Usuários**:
1. Identificar-se e consultar seu plano atual
2. Verificar o valor da última fatura
3. Reportar um problema de internet lenta
4. Perguntar sobre opções de upgrade
5. Solicitar transferência para atendente humano

## b) Características a Ser Avaliadas

### Dimensão Técnica
- **Acurácia de classificação**: o agente identifica corretamente a intenção?
- **Extração de entidades**: o agente extrai corretamente CPF, tipo de serviço, etc.?
- **Coerência contextual**: as respostas fazem sentido no contexto da conversa?
- **Robustez**: o agente lida bem com erros de digitação, gírias e abreviações?

### Dimensão Conversacional
- **Naturalidade**: as respostas parecem naturais e humanas?
- **Completude**: o agente fornece todas as informações necessárias?
- **Concisão**: as respostas são objetivas sem ser lacônicas?
- **Proatividade**: o agente oferece informações relevantes além do solicitado?
- **Tratamento de erros**: o agente lida graciosamente com situações inesperadas?
- **Personalização**: o agente usa o nome do cliente e contextualiza respostas?

### Dimensão de Experiência do Usuário
- **Facilidade de uso**: quão fácil é interagir com o agente?
- **Satisfação**: o usuário ficou satisfeito com o atendimento?
- **Eficiência**: quantas mensagens foram necessárias para resolver a demanda?
- **Confiança**: o usuário confia nas informações fornecidas?
- **Preferência**: o usuário prefere o agente ao atendimento por telefone para essas demandas?

## c) Instrumentos de Coleta

### Questionário SUS Adaptado

1. Eu gostaria de usar este agente frequentemente
2. Achei o agente desnecessariamente complexo
3. Achei o agente fácil de usar
4. Precisaria de apoio técnico para usar o agente
5. As diferentes funções do agente estavam bem integradas
6. Havia muita inconsistência no agente
7. A maioria das pessoas aprenderia a usar este agente rapidamente
8. Achei o agente muito desconfortável de usar
9. Me senti confiante usando o agente
10. Precisei aprender muitas coisas antes de usar o agente

### Roteiro de Entrevista

1. O que achou da experiência geral com o agente?
2. O agente entendeu bem o que você quis dizer? Houve algum momento de confusão?
3. As respostas do agente foram úteis e completas?
4. Você usaria este agente no lugar de ligar para o SAC? Por quê?
5. O que poderia ser melhorado?

## Cronograma de Avaliação Proposto

| Fase | Atividade | Duração |
|------|-----------|---------|
| 1 | Preparação (definição de cenários, recrutamento) | 1 semana |
| 2 | Avaliação técnica (automática) | 2 dias |
| 3 | Avaliação funcional (cenários) | 3 dias |
| 4 | Avaliação com usuários (10-15 sessões) | 1 semana |
| 5 | Análise dos resultados e relatório | 1 semana |
| **Total** | | **~3 semanas** |
