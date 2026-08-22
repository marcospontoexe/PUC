# Técnicas de machine learning

1. Aprendizagem supervisionada
* Regressão
* Classificação 
* Série temporal

2. Aprendizagem não supervisionada
* Redução de dimensionalidade
* Agrupamento

3. Aprendizagem semi-supervisionada
* rotulagem (labeling)

4. Aprendizagem por reforço
* escalas de trabalho ótimas
* agentes de jogo

# O processo de ML, do início ao fim

1. Coleta de dados
2. Preparação dos dados
3. Seleção do modelo
4. Treinamento do modelo
5. Avaliação do modelo
6. Ajuste de parâmetros
7. Aplicação

# Aprendizagem não supervisionada

## a maldição da dimensionalidade
quanto mais colunas em relação ao número de linhas, mais difícil (e mais lento) fica o aprendizado — fenômeno chamado maldição da dimensionalidade (a complexidade cresce quase exponencialmente com o número de atributos).

### Seleção de atributos (feature selection): 
* Redução de dimensionalidade
* Remove atributos irrelevantes ou redundantes, mantendo os originais.
* Precisa reduzir atributos e conseguir explicar quais fatores levaram ao resultado, sem poder modificá-los?
* Precisa apenas filtrar quais atributos mais contribuem para uma classe

1. VarianceThreshold:	Remove colunas com variância baixa (que “não variam”, logo carregam pouca informação).
2. SelectKBest:	Seleciona as k melhores colunas por teste estatístico (ex.: qui-quadrado).
3. SelectPercentile: Como o SelectKBest, mas seleciona por percentil em vez de quantidade fixa.

### Extração de atributos (feature extraction): 
* Redução de dimensionalidade
* Cria novos atributos combinando/ transformando os existentes.
* Está combinando atributos ligados entre si num valor único (ex.: idade + escolaridade + renda + CEP → “qualidade de vida”)

1. PCA (principal component analysis): busca manter o máximo de poder explicativo do dataset com o mínimo de variáveis, combinando as colunas originais em componentes principais novos.

### Agrupamento (clustering):
* Agrupamento de dados
* Descobre perfis/grupos entre as instâncias.
* Precisa agrupar instâncias em perfis

1. KMeans / MiniBatchKMeans:	O mais conhecido: divide as instâncias em k grupos (definidos por você) tão homogêneos quanto possível, a partir de centroides. 
2. DBSCAN:	Baseado em densidade: encontra exemplos bem próximos entre si e expande a partir dos “vizinhos”. Ao contrário do KMeans, não exige que você defina o número de grupos.
3. OPTICS:	Parecido com o DBSCAN, mas pode gerar agrupamentos diferentes por penalizar elementos com poucos exemplos similares.

# Aprendizagem supervisionada

## as cinco tribos

### 1. Symbolists (simbolistas)

* Foco: lógica matemática, regras
* Exemplos: árvore de decisão, random forest
* Pontos fortes: fácil interpretação; funciona bem com bases pequenas
* Pontos fracos: sensível a ruído; pode não escalar para bases grandes

### 2. Analogizers (analogizadores)

* Foco: generalização por similaridade
* Exemplos: KNN, SVM, regressão linear
* Pontos fortes: reconhece similaridade entre casos com facilidade
* Pontos fracos: sofre com a maldição da dimensionalidade

### 3. Bayesians (bayesianos)

* Foco: incerteza e estatística
* Exemplos: Naïve Bayes
* Pontos fortes: robusto a ruído e ambiguidade nos dados
* Pontos fracos: custo computacional mais alto

## 4. Connectionists (conexionistas)

Foco :neurociência aplicada a algoritmos
Exemplos: redes neurais, deep learning
Pontos fortes: aprende problemas muito complexos
Pontos fracos: caro, complexo, pouco explicável (“caixa-preta”)

### 5. Evolutionaries (evolucionários)

Foco: genes, gerações, mutação
Exemplos: algoritmos genéticos
Pontos fortes: explora múltiplas soluções em paralelo
Pontos fracos: pode não explorar todas as alternativas; custo alto

## Ensembles: comitês de algoritmos
Ensembles combinam vários modelos para obter um resultado mais robusto do que qualquer um sozinho 

* Bagging — calcula uma média/votação de vários modelos que servem de base. O random forest é o exemplo clássico: um comitê de árvores de decisão.

* Boosting — o resultado de um modelo serve de entrada para o próximo, numa cadeia em que cada nova árvore tenta corrigir o erro das anteriores. É o princípio do gradient boosting, implementado pelo XGBoost e pelo LightGBM — diferente do random forest, as árvores aqui não são geradas aleatoriamente, mas de forma progressivamente “mais inteligente”.

# Padronização (standardization)
Transforma os dados para terem média 0 e desvio-padrão 1, mantendo a forma da distribuição original.

z = (x - média) / desvio_padrão

* Não tem limite fixo — os valores podem continuar sendo, por exemplo, -3 ou +5.
* Classe no scikit-learn: StandardScaler.
* Existe uma variante robusta a outliers: RobustScaler, que usa a mediana e o intervalo interquartil (IQR) em vez de média e desvio-padrão — por isso um valor muito extremo distorce menos o resultado.

# Normalização (normalization, no sentido estrito)
Reescala os dados para caberem dentro de um intervalo fixo, normalmente [0, 1].

x' = (x - mínimo) / (máximo - mínimo)

* Classe no scikit-learn: MinMaxScaler.
* É muito mais sensível a outliers: um único valor extremo vira o novo "máximo" e comprime todos os outros pontos para perto de 0. 

# Métricas de regressão
Todas partem do conceito de erro: a diferença entre o valor real e o previsto. Se o modelo previu 20 graus e o real foi 25, o erro foi 5; se previu 15 e o real foi 13, o erro foi −2.

## R² (R-squared)
Mede quão bem os atributos explicam a variável dependente. Scikit-learn: r2_score

* Quando usar — em conjunto com outras métricas, nunca sozinho; pode analisar associações entre atributos.
* Quando não usar — para comparar modelos treinados em datasets diferentes (só serve dentro do mesmo dataset); em bases com muitos atributos, o R² tende a subir artificialmente a cada coluna nova adicionada (existe uma correção chamada R² ajustado, fora do scikit-learn).
* Como interpretar — vai de 0,0 a 1,0; quanto mais perto de 1,0, melhor. Em problemas reais é raro (e suspeito) ter R² acima de 0,9. Um R² baixo não significa necessariamente um modelo ruim — em áreas como vendas e logística existem fatores externos que o modelo desconhece.

## MAE — Erro médio absoluto
Média de todos os erros, ignorando o sinal (um erro para mais e um erro para menos pesam igual). Scikit-learn: mean_absolute_error

* Quando usar — quando o impacto do erro é proporcional ao seu tamanho (dobrar o erro dobra o impacto). Comum no mundo financeiro: perder 10% é duas vezes pior que perder 5%.
* Quando não usar — quando você quer penalizar mais os outliers, ou quando erro e impacto não são proporcionais (errar a nota final de 6 para 7 pode ser a diferença entre reprovar e passar — um salto de impacto que o MAE não capta).
* Como interpretar — quanto mais perto de 0, melhor.

## MSE — Erro médio quadrático
Média de todos os erros elevados ao quadrado. Scikit-learn: mean_squared_error

* Quando usar — quando você quer garantir que erros grandes sejam capturados: um erro isolado muito maior que os demais "pesa" desproporcionalmente no resultado final, evidenciando que houve um erro grotesco em algum ponto.
* Quando não usar — quando não quiser penalizar erros grandes.
* Como interpretar — quanto mais perto de 0, melhor. Como o valor fica elevado ao quadrado, sai da unidade original do problema (reais, graus, etc.) — por isso existe a variante **RMSE** (raiz quadrada do MSE), que devolve o erro para a unidade original e é mais compreensível para humanos. Existe também o **NRMSE**, que normaliza o erro em algo parecido com uma porcentagem (mas não com a mesma lógica do MAPE, abaixo).

## MSLE — Erro logarítmico médio quadrático
Como o MSE, mas usa logaritmos para calcular o erro. Scikit-learn: mean_squared_log_error

* O que faz de diferente — pune mais os erros para baixo do que os erros para cima (prever 18°C quando o real é 20°C gera um MSLE maior do que prever 22°C quando o real é 20°C). Busca o erro proporcional ao valor: um erro de R$ 1 para quem tem R$ 1.000 pesa diferente de um erro de R$ 1 para quem tem R$ 10.
* Quando usar — quando você se importa com a proporção do erro.
* Quando não usar — fora de dados contínuos; quando não quiser pesar diferente erros para cima e para baixo.
* Como interpretar — quanto mais perto de 0, melhor. Existe a variante RMSLE (raiz quadrada do MSLE).

## MAPE — Erro médio absoluto percentual
Média das porcentagens de erro (real 100, previsto 90 → erro de 0,10; real 100, previsto 110 → erro também de 0,10). Scikit-learn: mean_absolute_percentage_error

* Quando usar — quando você quer que erros percentuais destoantes (muito altos) afetem fortemente a métrica.
* Quando não usar — com muitos outliers; com muitos valores reais iguais a zero (o cálculo divide pelo valor real — um valor real zero gera erro percentual infinito/travado, distorcendo tudo).
* Como interpretar — quanto mais perto de 0, melhor.

# Métricas de classificação

## Accuracy (acurácia)
Accuracy = (TP + TN) / (TP + TN + FP + FN)

## Precision e Recall

1. Precision = TP / (TP + FP) — das vezes que o algoritmo disse "positivo", quantas realmente eram positivas?

2. Recall = TP / (TP + FN) — de todos os positivos reais, quantos o algoritmo conseguiu pegar?

## F1-score
F1 = 2 × (Precision × Recall) / (Precision + Recall)

Agrega precision e recall numa única métrica (0 a 1, quanto mais perto de 1, melhor)

## Matriz de confusão

## Curva ROC e AUC
A curva ROC (Receiver Operating Characteristic) mostra visualmente a performance de um classificador que também informa a probabilidade da previsão (via predict_proba). Quanto mais a curva se aproxima do canto superior esquerdo do gráfico, melhor — uma linha diagonal representaria um classificador aleatório (cara ou coroa). 
A AUC (área sob a curva) resume essa performance num único número entre 0 e 1: quanto mais perto de 1, melhor.

# Pipeline
O Pipeline do scikit-learn agrupa todas essas etapas numa única variável: você chama fit uma vez (ele executa, internamente, o fit de cada etapa em sequência — criação de coluna, encoders, scaler, modelo) e predict uma vez para novos dados (o pipeline aplica, na mesma ordem, o transform de cada etapa e finaliza com o predict do modelo).

# Hiperparâmetros

## Busca automática: grid search vs. randomized search
Ambos testam sistematicamente combinações de hiperparâmetros e escolhem a melhor

1. GridSearchCV
* Estratégia:	Busca exaustiva — testa todas as combinações possíveis.
* Vantagem:	Garante encontrar a melhor combinação dentro do espaço definido.
* Desvantagem:	Pode demorar muito tempo em espaços grandes.

2. RandomizedSearchCV
* Estratégia:	Testa apenas uma amostra aleatória das combinações.
* Vantagem:	Mais rápido, especialmente com muitos hiperparâmetros/valores.
* Desvantagem: Não garante encontrar a melhor combinação (por não testar tudo).

# Validação cruzada (cross-validation)
O CV no nome de ambas as funções vem de cross-validation: em vez de um único train_test_split, o algoritmo divide a base de treino em várias partes menores (folds — tipicamente 5) e roda o treinamento em rotação:

* Split 1: treina com os folds 2, 3, 4 e 5; valida no fold 1.
* Split 2: treina com os folds 1, 3, 4 e 5; valida no fold 2.
* ...e assim sucessivamente, até que cada fold já tenha servido de validação uma vez.

O objetivo é reduzir as chances de overfitting ao garantir que todas as partes da base de treino sejam usadas tanto para treinar quanto para validar, em rodadas diferentes.

# Séries temporais: quando o tempo importa

## Decomposição de séries temporais
1. Nível — a ordem de grandeza dos dados: centenas? milhares? milhões?
2. Tendência — os números estão, de forma geral, crescendo ou caindo no longo prazo?
3. Sazonalidade — os números sobem/caem de forma cíclica? Toda sexta? Toda madrugada? Todo início de mês?
4. Ruído — o que sobra depois de explicar nível, tendência e sazonalidade: interferências sem causa clara, como o chiado de um rádio.

## Cuidados específicos de dados temporais

1. Outliers:	Um pico isolado (ex.: dólar “disparando” para R$ 52,76 por um dia) costuma ser erro de digitação (5,276 lido como 52,76) — analisar pelo bom senso antes de tratar como evento real.

2. Dados faltantes:	Preencher com zero pode ser pior do que deixar vazio (o algoritmo pode aprender uma queda brusca que nunca existiu). Sem uma fonte alternativa, técnicas como média móvel ajudam a preencher a lacuna de forma mais coerente com a tendência.

## Sliding window e backtest
Dois conceitos centrais para transformar uma série temporal em algo que um algoritmo consiga treinar:

1. Sliding window (janela deslizante): Técnica que reorganiza o dataset para um problema de regressão, criando colunas adicionais com as observações t-1, t-2, t-3… O tamanho da janela depende do caso

2. Backtest: Uma forma específica de dividir treino/teste pelo tempo, e não aleatoriamente como no train_test_split

## Três formas de modelar séries temporais
1. Regressão com sliding window:
Depois de transformada a base (seção anterior), o problema vira uma regressão comum, resolvida com qualquer algoritmo já visto — RandomForestRegressor, XGBoost, LightGBM.

2. Prophet:
Biblioteca criada pelo Facebook, boa para dados com sazonalidade clara. Em sua forma mais básica, exige apenas duas colunas com nomes fixos: ds (a data) e y (o valor a prever).

3. ARIMA:
Autoregressive Integrated Moving Average — um modelo estatístico (não de ML no sentido restrito) com três parâmetros:

* p (AR — autoregressive) — quantos termos autorregressivos considerar (quantas observações anteriores, t-1, t-2, t-3…, entram no cálculo).
* d (I — integrated) — quantas vezes a série precisa ser diferenciada (subtraída de si mesma) para se tornar estacionária — uma série sem tendência e sem sazonalidade.
* q (MA — moving average) — o tamanho da janela usada para calcular a média móvel entre a observação e o ruído das últimas observações.

Em Python, o ARIMA (do statsmodels) exige que você defina p, d e q manualmente, a partir de critérios estatísticos sobre o comportamento da série; já o **AutoARIMA** (biblioteca pmdarima) calcula esses três parâmetros automaticamente.