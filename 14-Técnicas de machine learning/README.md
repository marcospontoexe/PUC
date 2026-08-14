# Prevendo a demanda de bicicletas compartilhadas em Seul

**Um estudo completo de regressão com XGBoost — da análise exploratória ao pipeline otimizado.**

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square&logo=python&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.7-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-3.4-337AB7?style=flat-square)
![pandas](https://img.shields.io/badge/pandas-2.3-150458?style=flat-square&logo=pandas&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)

---

## Bem-vindo

Todo dia, uma operadora de bicicletas compartilhadas enfrenta a mesma pergunta: **quantas bicicletas
colocar na rua na próxima hora?** Errar para baixo significa clientes sem bicicleta. Errar para cima
significa capital parado nas estações. É um problema de negócio real — e é exatamente o tipo de
problema que Machine Learning resolve bem.

Este repositório documenta minha resposta a esse desafio, desenvolvido durante a disciplina
**Técnicas de Machine Learning** do curso de Inteligência Artificial da **PUC-PR**. O trabalho é
dividido em duas atividades somativas que, juntas, formam um único projeto contínuo: a primeira
constrói um modelo preditivo funcional, e a segunda o transforma em um pipeline profissional,
metricamente avaliado e com hiperparâmetros otimizados.

O enunciado propõe um cenário de simulação: você é candidato ao programa de estágio de uma grande
consultoria de dados e recebeu um dataset para demonstrar seu domínio de Python aplicado a ML. E o
critério de avaliação é explícito — **avalia-se o caminho, não apenas o resultado**. Foi com essa
régua que escrevi cada célula: código legível, cada decisão técnica justificada em markdown e cada
conclusão sustentada por números.

> **Uma nota sobre o estilo dos notebooks:** eles são deliberadamente didáticos. Cada técnica é
> explicada antes de ser aplicada, em português, de forma que alguém sem conhecimento de Python
> consiga acompanhar o raciocínio. Isso foi um requisito da atividade — e, na prática, é a mesma
> habilidade exigida ao apresentar um modelo para stakeholders de negócio.

---

## O problema

**Dataset:** `seoul_bike_data.xlsx` — 8.760 registros horários (24h × 365 dias) de aluguel de
bicicletas públicas em Seul, na Coreia do Sul, entre dezembro de 2017 e novembro de 2018.

**Variável alvo:** `Rented Bike Count` — número de bicicletas alugadas em cada hora.

**Tipo de problema:** regressão. O alvo é uma contagem contínua, não uma categoria.

**Features disponíveis:** hora do dia, dia da semana, temperatura, umidade, velocidade do vento,
visibilidade, ponto de orvalho, radiação solar, precipitação de chuva e de neve.

---

## As duas atividades

| | Atividade | Foco | Notebook |
|---|---|---|---|
| **I** | Criando a sua própria IA — Parte 1 | Do dado bruto ao primeiro modelo treinado | [`regrssion_XGBoost.ipynb`](Atividade_somativa_1/regrssion_XGBoost.ipynb) |
| **II** | Criando a sua própria IA — Parte 2 | Do modelo ao pipeline avaliado e otimizado | [`regression.ipynb`](Atividade_somativa_2/regression.ipynb) |

### Atividade Somativa 1 — construindo o modelo

**Objetivo:** escolher um dataset, preparar os dados aplicando obrigatoriamente uma técnica de
seleção ou extração de atributos, dividir a base entre treino e teste, definir e justificar o tipo
de problema, treinar um algoritmo supervisionado e apresentar as predições.

**[Abrir o notebook →](Atividade_somativa_1/regrssion_XGBoost.ipynb)**

O que foi feito:

- **Análise exploratória** com `ydata-profiling`, gerando um relatório completo de distribuições e
  correlações.
- **Diagnóstico de multicolinearidade:** `Temperature(°C)` e `Dew point temperature(°C)`
  apresentaram correlação de **0.912** — redundância clara. A decisão de qual manter não foi
  arbitrária: comparei a correlação de cada uma com o alvo (0.565 contra 0.374) e descartei a mais
  fraca.
- **Leitura crítica das correlações fracas:** `Weekday` e `Day` têm correlação linear quase nula com
  o alvo, mas foram **mantidas propositalmente** — o padrão de uso em dia útil (picos de
  deslocamento casa-trabalho) contra fim de semana (lazer) é cíclico, não linear, e modelos baseados
  em árvores capturam exatamente esse tipo de relação. Correlação baixa não é sinônimo de
  irrelevância.
- **Justificativa para não normalizar:** o XGBoost pertence à família dos algoritmos simbólicos, que
  particionam o espaço por regras de decisão (`Temperature > 15°C?`) e são, por construção, imunes à
  escala das features.
- **Divisão em três conjuntos** — treino, validação e teste — em vez dos dois habituais, para
  viabilizar *early stopping* honesto.
- **Treino do `XGBRegressor`** com `n_estimators=2000` e parada antecipada monitorando o conjunto de
  validação, que interrompeu o treino na iteração ideal e preveniu overfitting.

### Atividade Somativa 2 — industrializando o modelo

**Objetivo:** dar continuidade ao mesmo dataset, **reordenar as etapas** para eliminar vazamento de
dados, encapsular todo o processo em um `Pipeline` do scikit-learn, avaliar com múltiplas métricas
e concluir criticamente sobre os resultados.

**[Abrir o notebook →](Atividade_somativa_2/regression.ipynb)**

Esta é a parte tecnicamente mais densa do projeto — 52 células organizadas em 10 seções:

- **A inversão que muda tudo.** Na parte 1, os dados eram preparados antes da divisão. Na parte 2,
  **a divisão vem primeiro**. Essa mudança de ordem é o coração da atividade: cada transformador
  aprende (`fit`) exclusivamente no conjunto de treino e apenas aplica (`transform`) em validação e
  teste. Isso vale inclusive para os **limites de outliers pelo método IQR** — calcular os quartis
  no conjunto de teste seria usar informação do futuro para tratar o presente, uma forma sutil de
  *data leakage* que inflaria artificialmente as métricas.
- **Seleção de atributos comparada, não presumida.** `VarianceThreshold` e `SelectKBest` (com
  `f_regression` e `mutual_info_regression`) foram aplicados e **medidos um contra o outro** — e não
  simplesmente escolhidos por preferência.
- **Oito variantes de pipeline** construídas de forma incremental — sem tratamento algum, só com
  remoção de outliers, com seleção de atributos, com padronização, com e sem *early stopping* — e
  avaliadas lado a lado sobre o mesmo conjunto de teste.
- **Otimização de hiperparâmetros** com `GridSearchCV`, cruzando thresholds de variância,
  `n_estimators`, `max_depth` e `learning_rate` com validação cruzada.
- **Predição em cenário extremo:** o modelo foi confrontado com uma tempestade de inverno
  (−10.5 °C, 95% de umidade, 10 mm de chuva, 5 cm de neve, 4h da manhã) e retornou demanda negativa
  — sinal de que, nessas condições, o aluguel é um evento praticamente inexistente na base.

---

## Resultados

Modelo final — `XGBRegressor` com tratamento completo de dados, sobre o conjunto de teste:

| Métrica | Valor | Leitura prática |
|---|---|---|
| **R²** | `0.83` | O modelo explica 83% da variância da demanda horária |
| **MAE** | `163` bicicletas | Erro médio absoluto por hora |
| **RMSE** | `279` bicicletas | Penaliza mais os erros grandes, revelando os picos ainda difíceis |

A distância entre MAE e RMSE é informativa por si só: o modelo acerta bem o comportamento típico,
mas ainda erra mais nos horários de pico extremo — justamente onde o custo de negócio é maior.

### O que os experimentos mostraram

O achado mais interessante deste projeto foi **negativo** — e está registrado no notebook com a
mesma honestidade dos resultados positivos:

- `SelectKBest` com `k=7` retornou **o mesmo conjunto de colunas** usando `f_regression` (relações
  lineares) e `mutual_info_regression` (relações não-lineares).
- `VarianceThreshold` superou consistentemente o `SelectKBest` neste dataset.
- **Reduzir features piorou o modelo.** Com apenas 10 colunas de entrada, o XGBoost já lida bem com
  redundância internamente, e descartar atributos custou informação útil sem ganho compensatório em
  variância.
- **Os hiperparâmetros do `GridSearchCV` não superaram os ajustados manualmente.** A busca em grade
  é limitada pelo espaço que você define — e um espaço mal escolhido devolve um ótimo local pior que
  a intuição informada pelos experimentos anteriores.

Vale mais registrar um experimento que refutou a hipótese do que esconder o resultado que não
confirmou a expectativa.

---

## Competências demonstradas

`Análise exploratória de dados` · `Diagnóstico de multicolinearidade` · `Tratamento de outliers
(IQR)` · `Seleção de atributos` · `Padronização de escala` · `Prevenção de data leakage` ·
`Gradient Boosting` · `Early stopping` · `Pipelines do scikit-learn` · `Validação cruzada` ·
`Otimização de hiperparâmetros` · `Métricas de regressão` · `Comunicação técnica`

**Stack:** Python 3.13 · pandas · NumPy · scikit-learn · XGBoost · ydata-profiling · Matplotlib ·
Seaborn · JupyterLab

---

## Estrutura

```
.
├── Atividade_somativa_1/
│   ├── regrssion_XGBoost.ipynb   # notebook da parte 1
│   ├── regrssion_XGBoost.html    # versão exportada, para leitura sem Jupyter
│   ├── relatorio.html            # relatório de profiling do dataset
│   └── seoul_bike_data.xlsx      # dataset
├── Atividade_somativa_2/
│   ├── regression.ipynb          # notebook da parte 2
│   ├── regression.html           # versão exportada, para leitura sem Jupyter
│   ├── relatorio.html            # relatório de profiling do dataset
│   └── seoul_bike_data.xlsx      # dataset
└── ConteudoSemanas/              # material de estudo da disciplina, por semana
```

> **Quer só ler o resultado?** Os arquivos `.html` abrem direto no navegador, com todas as saídas
> e gráficos já renderizados — não é preciso instalar nada.

---

## Como executar

```bash
# 1. Instale as dependências
pip install pandas numpy scikit-learn xgboost ydata-profiling openpyxl matplotlib seaborn jupyterlab

# 2. Entre na pasta da atividade desejada (os notebooks leem o dataset por caminho relativo)
cd Atividade_somativa_2

# 3. Abra o notebook
jupyter lab regression.ipynb
```

---

## Sobre este repositório

Projeto acadêmico desenvolvido individualmente na **PUC-PR**, no curso de Inteligência Artificial,
disciplina de Técnicas de Machine Learning. O código está disponível como portfólio técnico — se
você é estudante da mesma disciplina, use-o como referência de método, não como resposta pronta.

Feedback, críticas e conversas sobre ML são muito bem-vindos.
