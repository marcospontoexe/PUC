# Atividade formativa da unidade 07 — duplo treinamento (RNC + RNT)

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md).
Pasta: [../atividade formativa-s7/](../atividade%20formativa-s7/).
Relatório: [`relatorio-atividade-formativa-s7.md`](../atividade%20formativa-s7/relatorio-atividade-formativa-s7.md).

## O que a atividade pede

Duas partes independentes. Na **RNC**, ajustar duas redes competitivas (cilindrada × eficiência e
cilindrada × CO₂) e as duas regressões, entregando tabelas de parâmetros, gráficos, tabelas de
agrupamento, funções polinomiais e duas previsões. Na **RNT**, ajustar o modelo sobre a série do
dólar e entregar parâmetros, gráficos e métricas.

## Parte RNC

### Diagnóstico
- Com os valores originais, **o nº de grupos não bate com o nº de neurônios**: 3 grupos para 4
  neurônios na rede 1, e **4 grupos para 8 neurônios** na rede 2, com 96% dos veículos num só.
- Causa: `np.random.rand` inicializa os pesos em [0,1)², mas os dados estão fora dessa região
  (eficiência começa em 2,98; CO₂ em 18). Os neurônios nascem abaixo da nuvem e a maioria nunca vence.
- `taxa_aprend_rnc2 = 2.00` é destrutiva: `w + η(x − w)` com η = 2 devolve `2x − w`, à mesma
  distância do dado, do lado oposto.
- **A base `base_veiculos_1.csv` é idêntica à `base_veiculos.csv`** da unidade 05 (mesmos 37.967
  registros). A novidade é só a coluna CO₂ entrar na análise.

### Parâmetros escolhidos

| Parâmetro | Era | Ficou |
|---|---|---|
| `num_neur_rnc1` | 4 | **3** |
| `num_neur_rnc2` | 8 | **10** |
| `epocas_rnc1` | 10 | 10 |
| `epocas_rnc2` | 1 | **10** |
| `taxa_aprend_rnc1` | 0,01 | **0,3** |
| `taxa_aprend_rnc2` | 2,00 | **0,5** |
| `ordem_pol1` | 1 | **7** |
| `ordem_pol2` | 10 | **5** |

Varredura de 30 configurações por rede, 3 sementes (`busca_rnc_s7.py`, scratchpad). Resultado
contraintuitivo: **só 5 de 30 configurações da rede 1 evitam grupo vazio, contra 25 de 30 da rede 2**
— a faixa ampla do CO₂ dá mais espaço para os neurônios se distribuírem.

### Achado central: os grupos da rede 2 são faixas puras de CO₂

A amplitude do CO₂ é **98,8× maior** que a da cilindrada, então ele domina a distância euclidiana por
completo. As faixas de CO₂ dos 10 grupos são limpas e não se sobrepõem; as de cilindrada se sobrepõem
inteiramente (um grupo vai de 1,9 a 8,4 L). **A rede ignorou a cilindrada.** É o mesmo fenômeno da
unidade 05, ampliado de 2,8× para 98,8×.

### Ordem dos polinômios, validada contra a realidade
Comparadas com a média real por faixa de cilindrada, não pelo R².
- Eficiência, **ordem 7**: prevê 10,79 km/L em 1,8 L contra **10,88 reais** (2.087 veículos).
- CO₂, **ordem 5**: prevê 444,98 g/km em 8,2 L contra **440,37 reais** (43 veículos).
- A ordem 9 tinha erro menor nas faixas, mas **prevê CO₂ negativo (−35,26)** em 0,6 L. Desqualificada.
- Ressalva registrada no relatório: a ordem 7 oscila levemente acima de 7,5 L, onde há poucos dados.

## Parte RNT

### Diagnóstico
- **Mesmo defeito estrutural da unidade 06:** `Dense(5)` é a última camada, então o modelo devolve 5
  números para um alvo escalar e o código nem roda. `neuronios_densa = 1` é exigência estrutural.
- `binary_crossentropy` numa série que vale de 2,50 a 6,00.
- Treino e teste são séries **distintas** desta vez (não é prefixo, ao contrário da unidade 06).

### Parâmetros escolhidos

| Parâmetro | Era | Ficou |
|---|---|---|
| `janela_prev` | 50 | 50 |
| `funcao_perda` | `binary_crossentropy` | **`mean_squared_error`** |
| `otimizador` | `sgd` | **`RMSprop`** |
| `neuronios_LSTM` | 2 | **4** |
| `neuronios_densa` | 5 | **1** |
| `epocas` | 5 | **50** |
| `lote` | 20 | **32** |

Modelo com **101 parâmetros**. Métricas: R² 0,9854 no treino e **0,9294 no teste**, partindo de
0,9384 / 0,7903.

### Dois pontos de método

1. **Mais neurônios pioraram.** LSTM 50 deu R² de teste 0,9102 contra 0,9248 do LSTM 4. A série tem
   só 1.095 pontos.
2. **A busca sequencial tem ponto cego.** Na etapa 1 a perda MAE parecia melhor que a MSE (0,8824
   contra 0,8367), mas a busca seguiu com MSE fixo. Reconferido no ponto de chegada com 3 sementes:
   0,9265 contra 0,9267 — a diferença sumiu depois que os outros parâmetros mudaram. **Sempre
   reconferir a primeira decisão de uma busca sequencial.**

### Achados sobre os dados

- **A RNT empata com a previsão ingênua.** Repetir o último valor dá R² 0,9890 no treino e 0,9251 no
  teste, com MAE 0,0753 e 0,0772. A rede ganha no erro quadrático e perde no absoluto. Mesma lição
  da unidade 06, aqui em versão mais equilibrada.
- **A série de teste é 51% mais volátil** que a de treinamento (desvio das variações 0,1557 contra
  0,1031). É isso que explica R² 0,985 no treino e 0,929 no teste — não é sobreajuste.
- Hipótese que **não se confirmou**: o gráfico sugeria uma série de teste sintética, com platôs. A
  medição mostrou 1.082 valores distintos em 1.095 pontos. O que parecia platô é oscilação densa na
  escala do gráfico. Só o valor exato 5,00, que aparece 13 vezes, sugere algum teto.

## Observações sobre o código

- O enunciado pede "S7_RNC.py"; o arquivo entregue chama-se **`S7_RCN.py`** (letras trocadas).
- Linha 112 do RNT: `np.reshape(X_test, (X_test.shape[0], X_train.shape[1], 1))` usa `X_train` no
  lugar de `X_test`. Funciona por coincidência.
- Nenhum dos dois fixa semente.
- Ambos só chamam `plt.show()`, que não grava arquivo. As figuras foram geradas à parte por
  `graficos_rnc_s7.py` e `graficos_rnt_s7.py` (scratchpad).

## Preparação do ambiente

Os três CSVs foram copiados para `C:\RN\`, caminho fixo esperado pelos códigos.
