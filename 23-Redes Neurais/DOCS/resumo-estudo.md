# Resumo de estudo (`Resumo.md`)

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md).

## O que é

[../Resumo.md](../Resumo.md) é o material de estudo da disciplina: leitura integral dos 8 PDFs
(unidades 01 a 08), com mapa da disciplina, resumo por unidade, tabelas de síntese, glossário, 20
perguntas de autoavaliação e referências. Foi sendo aprofundado ao longo de várias rodadas de
perguntas do utilizador.

## Regras editoriais a respeitar

1. **É material teórico.** Não menciona a pasta [../RNC/](../RNC/), o `S5_RNC.py`, a base
   `base_veiculos.csv` nem resultados de atividade. Uma nota sobre o código da disciplina chegou a
   ser escrita na seção 5.4 e **o utilizador a removeu**, junto com o restante do material de
   atividade. Não reintroduzir sem pedido explícito. Referências ao código das unidades 07/08 que
   já estavam no texto (como `inshape = combinacao.shape[1]`) são aceitáveis.
2. **Sem ⭐ nos títulos novos.** O utilizador vem removendo as estrelas que existiam.
3. **Todo número é conferido por script antes de entrar.** Sem exceção. Vários achados da sessão
   vieram de medir em vez de supor.
4. **A numeração das seções muda a cada inserção.** Sempre reconferir com `grep "^## "` antes de
   citar um número de seção.

## Estado por unidade

| Unidade | Estado |
|---|---|
| 01 Introdução | resumo original |
| 02 MLP | **aprofundada** |
| 03 CNN | **aprofundada** (reescrita quase completa) |
| 04 Comparativo | resumo original + a atividade prática |
| 05 RNC | **aprofundada** (4 seções novas + 4 figuras) |
| 06 RNT | **aprofundada** (10 seções novas + 3 figuras) |
| 07 Duplo treinamento | resumo original — **próximo alvo** |
| 08 Continuação | resumo original — **próximo alvo** |

## Unidade 02 — o que foi acrescentado

- Seção sobre dropout, L1/L2, early stopping, validação cruzada e walk-forward.
- Seção detalhada sobre a atualização de pesos por lote: forward pass, backpropagation e otimizador,
  com exemplo numérico de uma amostra individual atravessando a rede.

## Unidade 03 — o que foi acrescentado e depois reorganizado

**Primeira rodada (aprofundamento):** motivação MLP × CNN, mecânica da convolução passo a passo com
exemplo numérico, padding/stride e a fórmula de dimensão, canais e profundidade, pooling, flatten,
arquitetura MNIST completa comentada com contagem de parâmetros, como o mapa de características é
gerado (deslizamento 2D + múltiplos canais + múltiplos filtros), weight sharing e backprop dentro da
convolução, e uma seção mostrando como a 2ª convolução (64 filtros) processa os 32 mapas da 1ª.

**Segunda rodada (reorganização da unidade inteira).** O utilizador relatou que a unidade estava
confusa para entender canal, filtro e kernel. O diagnóstico confirmou:

- **"Canal" era explicado duas vezes:** na 3.1.1 (completa) e de novo na 3.4.
- **A distinção kernel × filtro estava na 3.4**, oitava posição — mas a 3.2 já usava "um filtro (ou
  *kernel*)" como sinônimos, contradizendo o que a 3.4 diria depois.
- **A ordem estava invertida:** a 3.2.1 trazia o exemplo numérico de múltiplos canais dizendo "a
  seção 3.4 descreve isso conceitualmente" — o conceito vinha **depois** da conta.
- A fórmula de parâmetros estava na 3.4, mas era usada na 3.9 e na 3.9.1.

**A solução:** uma **nova seção 3.2 dedicada ao vocabulário** (canal → kernel → filtro → mapa,
encaixados nessa ordem), que absorveu a 3.1.1 e a 3.4 inteiras, e todo o resto desceu uma posição.
A unidade passou a ir de 3.1 a 3.18, sem subseções `x.y.z`.

| Antes | Depois |
|---|---|
| 3.1.1 "O que é um canal?" | absorvida pela nova **3.2** |
| 3.4 "Canais e profundidade" (com kernel × filtro) | absorvida pela nova **3.2** |
| 3.2 convolução passo a passo | 3.3 |
| 3.2.1 como o mapa é gerado | 3.4 |
| 3.3 padding/stride | 3.5 |
| 3.5 … 3.9.1 | 3.6 … 3.11 |
| 3.10 … 3.16 | 3.12 … 3.18 |

A reorganização foi feita por script (`reorganiza_unidade3.py`, no scratchpad), que preserva os
corpos palavra por palavra, renumera os títulos e corrige as ~20 referências cruzadas. Ele deixa um
backup em `Resumo.md.bak`.

> **Armadilha encontrada na execução, que vale lembrar se algo parecido for refeito:** os textos de
> ajuste escritos já na numeração nova passaram pelo mapa de renumeração e foram remapeados **de
> novo**, gerando duas referências erradas (uma delas auto-referente). Textos autorais novos não
> podem passar pela função de correção de referências.

Também foi corrigido o diagrama da seção 3.9 (*weight sharing*), que mostrava a entrada e a saída mas
**não mostrava a matriz de pesos**. Agora traz o kernel 3×3 com `w11…w33`, o viés, e as quatro
janelas que o mesmo kernel percorre.

## Unidade 05 — seções novas

### 5.2.1 Mapeamento de entradas para neurônios
Parte da frase do PDF. Sete tópicos: o vetor de pesos como ponto no espaço dos dados; sensibilidade
como região de Voronoi (4 veículos mapeados para A, B e C); euclidiana × cosseno; escala dos
atributos; especialização (com η = 0,1, após 30 passadas o peso vai de (0,6;0,5) a (0,811;0,285),
perto da média (0,810;0,287)); preservação da topologia; e armadilhas (neurônio morto, poucos ou
muitos neurônios, escala).

### 5.2.2 O espaço de dados
Um eixo por atributo, cada registro é um ponto, e os pesos moram no mesmo espaço. Divisão por
Voronoi com as três mediatrizes calculadas para A = (0,2;0,9), B = (0,6;0,5), C = (0,5;0,1). Áreas
das regiões conferidas em malha fina de 6001×6001: **A 24,12%, B 45,00%, C 30,87%**. O efeito da
unidade de medida: multiplicar um eixo por 3 faz **30,5% do espaço trocar de dono**, enquanto
multiplicar **todos** os eixos pelo mesmo fator não muda nada (prova: ‖s·x − s·w‖ = s·‖x − w‖).
Maldição da dimensionalidade medida: o contraste das distâncias cai de 82,7× em 2D para 0,16× em
784D, com a ressalva de que dados reais vivem numa superfície de dimensão menor.

Fecha respondendo "normalização é obrigatória?": **o algoritmo não exige, a metodologia sim**, porque
sem normalizar quem escolhe a geometria é a unidade de registro. Cosmético quando todos os atributos
estão na mesma unidade; inevitável quando diferem. E min-max e z-score produzem **geometrias
diferentes** entre si.

### 5.4.1 Como os pesos sinápticos são alterados
A regra `w_j(t+1) = w_j(t) + η(t) · h_jv(t) · [x(t) − w_j(t)]` com o papel de cada termo; o efeito da
taxa de aprendizado; a função de vizinhança gaussiana com o alerta de que `dist_grade` é medida **na
grade**, não no espaço dos dados; o passo completo com 3 neurônios; as duas fases do treino
(ordenação e convergência); por que o peso acaba na média do grupo; esboço de código comentado; e
tabela de variações (on-line, batch, vizinhança retangular, cosseno, consciência).

Três observações a preservar: nenhum neurônio é empurrado para longe do dado (não há ajuste
negativo); todos são atualizados a cada dado, mas com forças tão diferentes que só o vencedor e a
vizinhança se movem; encolher σ rápido demais congela o mapa torcido, sem conserto.

### 5.4.2 A vizinhança: h e σ
h como "volume" e σ como "alcance" (analogia da lanterna). Perfil de h para σ = 3,0 / 2,0 / 1,0 /
0,85 / 0,5 nas distâncias 0 a 5. σ₀ perto de metade do lado da grade, caindo para abaixo de 1. Duas
confusões comuns: h não é η; a gaussiana não é obrigatória (existe a retangular).

**Coerência a manter:** a figura `arquitetura_rnc.png` mostra o vizinho imediato andando com metade
da força e "A não é vizinho: fica parado". No texto isso é h = 0,5 para o vizinho imediato
(gaussiana com σ ≈ 0,849) e A a 4 casas, com h = 0,000015. Se a figura for refeita, esses valores
precisam continuar batendo.

## Unidade 06 — seções novas

| Seção | Conteúdo central |
|---|---|
| **6.1 (nota)** | o conceito de RNT é geral, mas tudo o que é concreto na unidade aponta para regressão sobre série histórica |
| **6.1.1** | a conexão recorrente; `h(t)` tem **papel duplo** (é a saída e a memória); o eco de um pulso único (0,4621 → 0,1367 em 6 instantes); desenrolar no tempo |
| **6.3.1** | neurônios temporais e potencial de memória; não é histórico, é resumo comprimido; os dois estados da LSTM |
| **6.3.2** | sinapses temporais: `W` (entrada) × `U` (recorrente), provado com os formatos de peso do Keras — **96% dos parâmetros da LSTM são sinapses temporais** |
| **6.3.3** | camada de saída: regressão, classificação e geração de texto; laço autorregressivo; com vocabulário de 5.000 palavras a saída tem 255.000 parâmetros, 24× a LSTM inteira |
| **6.4.1** | retroalimentação temporal: separa **três** coisas que o PDF mistura (estado para frente, erro para trás, saída autorregressiva) |
| **6.5 (nota)** | BPTT, TBPTT e RTRL são **algoritmos**; LSTM é **arquitetura de célula**. O PDF lista os quatro juntos |
| **6.5.1** | como os pesos são atualizados: **o gradiente de um peso compartilhado é a SOMA das contribuições de cada instante**, conferido contra a derivada automática do TensorFlow com diferença 0,00e+00 |
| **6.6.1** | vanishing/exploding: só o fator 1,00 é estável; derivada da tanh; o exploding avisa, o vanishing é silencioso |
| **6.6.2** | hidden state × cell state, os quatro portões, um passo numérico (c = 1,02 e h = 0,5389) e a **meia-vida da memória** (6,6 instantes com f = 0,9; 69 com f = 0,99) |
| **6.6.3** | arquiteturas sem recorrência: atenção/Transformers e TCN; numa sequência de 1.000, a RNT precisa de 999 passos e a atenção de **1**, ao custo de 1.000.000 de comparações |
| **6.7.1** | `neuronios_LSTM` × `neuronios_dense`: "a LSTM enxerga o tempo, a densa não"; LSTM(50)=10.400, Dense(25)=1.275, Dense(1)=26, total 11.701 |

Números da unidade 06 conferidos em `numeros_rnt.py` e `numeros_rnt2.py`, que montam o modelo no
Keras de verdade em vez de confiar nas fórmulas.

## Imprecisões dos materiais sinalizadas no Resumo

| Unidade | O que o PDF traz | O correto |
|---|---|---|
| 08 | `inshape3 = combinacao2.shape[1]` | `combinacao3.shape[1]` (funciona por coincidência, as três têm 2 colunas) |
| 06 | "RMSdrop" | `RMSprop` |
| 06 | BPTT, TBPTT, RTRL e LSTM como "algoritmos de aprendizado" | os três primeiros são algoritmos; LSTM é arquitetura de célula |

## Figuras e onde estão

Ver [figuras.md](figuras.md). Mapa rápido: `similaridade_cosseno_euclidiana.png` (5.2.1),
`voronoi_rnc.png` (5.2.2), `arquitetura_rnc.png` (5.3), `vizinhanca_h_sigma.png` (5.4.2),
`arquitetura_rnt.png` (6.3), `treinamento_rnt.png` (6.5), `celula_lstm.png` (6.6.1).
