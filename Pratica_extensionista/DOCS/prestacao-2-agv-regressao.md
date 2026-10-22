# Prestação de serviços 2: estimativa do peso da carga de um AGV por regressão (100 h)

Segunda prática do tipo **Prestação de serviços**. Ela ainda precisa ser cadastrada na Calculadora. Com a Formação (30 h) e a prestação do harness (100 h), totaliza **230 h**, acima das **224 h** exigidas.

## Descrição para a Calculadora (490 caracteres)

> Desenvolvimento de um modelo de machine learning (regressão) que estima o peso da carga transportada por um AGV (veículo autoguiado) a partir da corrente e da velocidade do motor. Após levantamento presencial na empresa, serão coletados dados com cargas de peso conhecido, o modelo será treinado e validado, e a equipe receberá uma ferramenta de estimativa sem balança, que ajuda a detectar sobrecarga, reduzir o desgaste do equipamento e aumentar a segurança da operação (ODS 9, meta 9.4).

## Pendências de elegibilidade (confirmar antes de cadastrar)

- **Onde fica o AGV?** Se for o local de trabalho do usuário, é permitido. Nesse caso, o Termo de aceite deve ser assinado por um responsável, não pelo usuário.
- **Atividade remunerada:** a prática não pode ser uma tarefa paga do próprio emprego, pois a extensão não pode gerar remuneração.
- **Empresa própria:** o usuário não pode ser sócio da empresa.
- **Conflito de propriedade intelectual:** pelo Anexo 2 do [Manual](../Manual_de_Resposabilidades.pdf), o modelo pertenceria à APC/PUCPR. Se a empresa tiver política própria de PI, as duas regras entram em conflito.

## ODS

- **ODS 9, meta 9.4:** modernizar a indústria com uso eficiente de recursos e tecnologias mais limpas. Justificativa: evitar sobrecarga e desgaste do equipamento.
- **Alternativa ODS 8, meta 8.8:** ambientes de trabalho seguros. Use esta se o foco principal for a segurança da operação. Nesse caso, ajustar o final da descrição.

## Etapas e horas (somam 100 h)

| # | Etapa | Horas | Presencial |
|---|---|---|---|
| 1 | Reunião inicial e Termo de aceite | 2 | sim |
| 2 | Diagnóstico: operação, faixa de cargas, como o peso é controlado hoje, sinais que o AGV já registra (corrente, velocidade, taxa de amostragem, tensão da bateria) e meta de erro aceitável | 6 | sim |
| 3 | Redação e postagem do planejamento | 6 | |
| 4 | Coleta de dados: pesar as cargas numa balança e rodar trajetos padronizados com ≥ 5 níveis de peso e várias repetições | 16 | sim |
| 5 | Preparação e análise exploratória: sincronizar os sinais, filtrar, separar as fases (aceleração × velocidade constante), criar atributos (aceleração, corrente média por fase, tensão da bateria) | 14 | |
| 6 | Modelagem: modelo linear de referência, depois modelos não lineares (random forest, gradient boosting); validação cruzada agrupada por corrida; métricas MAE (kg) e R² | 20 | |
| 7 | Ferramenta de estimativa: script ou serviço que lê os sinais e devolve o peso e um alerta de sobrecarga | 12 | |
| 8 | Validação em campo com cargas que não entraram no treino | 6 | sim |
| 9 | Entrega: apresentação dos resultados, documentação e orientação da equipe | 6 | sim |
| 10 | Coleta de feedback (Feedback da comunidade) | 2 | sim |
| 11 | Redação e postagem da execução | 10 | |

## Pontos técnicos

- **Viabilidade:** em velocidade constante e piso plano, a corrente depende pouco da massa. O sinal mais forte aparece na aceleração (F = m·a). Antes de prometer uma precisão, confirmar no diagnóstico que os registros têm trechos de aceleração e taxa de amostragem suficiente.
- **Vazamento de dados:** janelas de uma mesma corrida não podem ficar umas no treino e outras no teste. A validação precisa agrupar por corrida.
- **Variáveis de confusão:** carga da bateria, temperatura do motor, inclinação e tipo de piso.
- **Dados da empresa:** os dados operacionais pertencem à empresa e não devem ir para o repositório.

## Relação com a teoria (1.11)

- Técnicas de Machine Learning (14): regressão e validação.
- Preparação e Análise Exploratória de Dados (21).
- IoT (7) e IoT em um Mundo Conectado (11): sinais do motor como dados de sensores.
- Redes Neurais (23): só se for usada uma rede neural.

## Diferença em relação à prestação 1

As duas são do mesmo tipo, mas acontecem em locais diferentes e têm objetivos e entregas distintos: um LLM local numa startup e um modelo de regressão para um AGV. Isso atende à regra para mais de uma prática do mesmo tipo.
