# Atividade formativa da unidade 06 — RNT

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md).
Pasta: [../atividade formativa-s6/](../atividade%20formativa-s6/).

## O que a atividade pede

Ajustar os parâmetros de `S6_RNT.py` até as previsões ficarem boas, e entregar um relatório com:
tabela de parâmetros, os dois gráficos, e a tabela de métricas (MSE, MAE e R², treino e teste).

Entregue em
[`relatorio-atividade-formativa-s6.md`](../atividade%20formativa-s6/relatorio-atividade-formativa-s6.md).

## Os dois impedimentos do código original

1. **Não executa.** `model.fit` quebra com
   `ValueError: target.shape=(None,), output.shape=(None, 20)`. A arquitetura é
   `LSTM → Dense(neuronios_densa)` **sem camada de saída depois**, então a densa É a saída. Com
   `neuronios_densa = 20` o modelo devolve 20 números para um alvo escalar. Em Keras antigo isso
   passava por difusão silenciosa (daí as "linhas laranjas inadequadas" do enunciado); no Keras 3 é
   fatal. **`neuronios_densa = 1` não é escolha de desempenho, é exigência estrutural.**
2. **A perda é de classificação.** `binary_crossentropy` numa série que vale de 491 a 1217.

## Parâmetros escolhidos

| Parâmetro | Era | Ficou |
|---|---|---|
| `janela_prev` | 200 | **5** |
| `funcao_perda` | `binary_crossentropy` | **`mean_squared_error`** |
| `otimizador` | `RMSprop` | **`adam`** |
| `neuronios_LSTM` | 4 | **50** |
| `neuronios_densa` | 20 | **1** |
| `epocas` | 10 | **50** |
| `lote` | 200 | **16** |

Já aplicados em [`S6_RNT.py`](../atividade%20formativa-s6/S6_RNT.py). Modelo com 10.451 parâmetros.

Busca feita por varredura, uma dimensão por vez, com semente 42
(`busca_rnt_s6.py`, no scratchpad). Achado contraintuitivo: **janelas maiores pioraram tudo** —
janela 5 deu R² de teste 0,9914 contra 0,9747 da janela 60.

## Resultados

| Métrica | Treinamento | Teste |
|---|---|---|
| MSE | 404,93 | 146,24 |
| MAE | 8,58 | 8,53 |
| R² | 0,9851 | 0,9957 |

Partindo de R² **−2,34 / −3,76** com a perda original. O MAE caiu de 243 para 8,6 (redução de 96%).

## Os três achados críticos, que estão no relatório

### 1. A previsão ingênua bate o modelo

Repetir o último valor observado, sem aprendizado nenhum, dá **R² 0,9865 no treino e 0,9962 no
teste**, com MAE 7,36 e 7,43 — melhor que a rede treinada nas três métricas e nos dois conjuntos.

O R² de 0,99 vem da autocorrelação da série, não da capacidade preditiva do modelo. **Lição
metodológica a carregar: em série temporal, R² alto isolado não demonstra aprendizado.** A
comparação com um preditor trivial é obrigatória.

### 2. O conjunto de teste está contido no de treinamento

Os 560 valores de `serie_teste.csv` são **idênticos aos 560 primeiros** de
`serie_treinamento.csv` (verificado). As métricas de teste não medem generalização, e é por isso
que o "teste" sai melhor que o treino.

### 3. Há uma emenda artificial na série de treinamento

No índice 559 → 560, exatamente onde a série de teste termina, o valor cai de **1128,87 para
556,93**, uma variação de −571,94 num único período. Todas as demais variações da série ficam abaixo
de 123. O desvio-padrão das variações é 19,19 com o salto e **10,38 sem ele**. É visível a olho nu no
gráfico de treinamento do relatório.

## Observações menores sobre o código

- Linha 112: `np.reshape(X_test, (X_test.shape[0], X_train.shape[1], 1))` usa `X_train` no lugar de
  `X_test`. Funciona por coincidência, porque ambas têm a mesma janela.
- Não fixa semente: cada execução dá números levemente diferentes. A execução final do arquivo deu
  0,9851/0,9957; a versão com semente 42 deu 0,9853/0,9958.
- Só chama `plt.show()`, que não grava arquivo. A figura do relatório foi gerada à parte por
  `graficos_s6.py` (scratchpad), a partir das mesmas previsões.

## Preparação do ambiente

Os CSVs foram copiados para `C:\RN\`, que é o caminho fixo esperado pelo código, seguindo a mesma
convenção das atividades anteriores.
