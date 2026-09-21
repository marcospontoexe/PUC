# Atividade da unidade 05 — RNC

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md). Pasta: [../RNC/](../RNC/).

## Conteúdo da pasta

| Arquivo | O que é |
|---|---|
| `RNC/S5_RNC.py` | o código da disciplina (9,6 KB) |
| `RNC/base_veiculos.csv` | a base (1,7 MB) |
| `RNC/template da atividade.docx` | o enunciado |
| `RNC/resultado_rnc.png` | a figura gerada para o relatório |

A pasta apareceu na raiz em 15/09/2026. Antes disso, o código não existia nesta máquina, e as
figuras da unidade 05 do Resumo foram feitas a partir do PDF.

## O que o código faz

Classe `RNC` de ~30 linhas em numpy puro, sem Keras:

- `weights = np.random.rand(num_neurons, input_shape)` — **sem bias**, sem soma ponderada, sem
  ativação. Isso confirmou a decisão tomada na figura `arquitetura_rnc.png`.
- `np.linalg.norm(input_sample - weights, axis=1)` seguido de `argmin` — distância euclidiana.
- `update_weights` atualiza **apenas o vencedor**.

**Descoberta mais importante:** não há grade, não há vizinhança, não há h nem σ. O código implementa
**aprendizado competitivo puro** (quantização vetorial on-line), não um mapa de Kohonen, embora o
PDF descreva vizinhança topológica e traga o passo 5 "atualização dos pesos dos neurônios vizinhos".

> Uma nota sobre essa diferença chegou a ser escrita na seção 5.4 do Resumo, e **o utilizador a
> removeu**. Ver as regras editoriais em [resumo-estudo.md](resumo-estudo.md).

## A base

37.967 linhas; colunas `Make`, `Model`, `Cilindrada`, `Eficiencia`, `CO2`; 125 montadoras e 3.681
modelos. **Nenhum valor ausente e nenhum zero**, então o `dropna()` e o filtro de zeros do código
não removem nada. **23.179 linhas (61%) são duplicadas**, e só existem **768 posições distintas** no
plano cilindrada × eficiência — por isso o gráfico parece uma grade de pontos alinhados.

Cilindrada de 0,6 a 8,4 L; eficiência de 2,98 a 24,66 km/L. Amplitudes **2,78× diferentes**, e o
código **não normaliza**, ao contrário do que o próprio PDF exige.

## Os problemas do código, medidos

### η = 2,0 (o valor de fábrica) é destrutivo
`w + η(x − w)` com η = 2 devolve `2x − w`, que fica **à mesma distância do dado, do lado oposto**
(medido: 2,24 antes, 2,24 depois). Na prática: 78,4% das atualizações jogam o peso para fora da
faixa dos dados, os pesos finais param em (30,97; 37,00) e (−1,51; 48,59), 2 dos 4 neurônios ficam
vazios e 37.962 dos 37.967 veículos caem num único grupo.

### Os neurônios nascem mortos
`np.random.rand` sorteia os pesos em [0,1) nos dois eixos, mas a eficiência começa em 2,98 km/L.
**Todo neurônio nasce abaixo da nuvem de dados**, e só os poucos mais próximos conseguem vencer. Com
k = 6, **quatro dos seis terminaram nas coordenadas exatas em que nasceram**. É por isso que k de 3
a 10 dava erro idêntico.

### Épocas são inertes
1, 5, 20 e 50 épocas dão resultado igual até a quarta casa, inclusive com os dados embaralhados. Com
taxa constante e sem decaimento, a memória do modelo é de ~1/η amostras, então o que define os pesos
finais é o fim da base, não quantas vezes ela foi percorrida. O que falta para épocas importarem é o
**decaimento de η**, não mais iterações.

### Normalizar resolveria
Com min-max, os neurônios mortos somem e o erro passa a cair com k (1,229 em k=3 até 0,888 em k=10).
Mas normalizar é mudar o código, e a atividade pede ajuste dos quatro parâmetros numéricos — ficou
como observação para o relatório.

## A busca de parâmetros

56 configurações (k de 3 a 10 × 7 taxas), 3 sementes cada. **Só 6 não deixam nenhum grupo vazio.**

Critério **declarado antes de ver os números**: descartar quem deixa grupo vazio → menor erro de
quantização → desempate pelo menor k.

| Parâmetro | Era | Ficou |
|---|---|---|
| `num_neur_rnc` | 4 | **3** |
| `taxa_aprend_rnc` | 2.0 | **0.3** |
| `epocas_rnc` | 1 | **5** |
| `ordem_pol` | 1 | **5** |
| `cilindrada_info` | 1.0 | 1.0 |

Já aplicados em [../RNC/S5_RNC.py](../RNC/S5_RNC.py).

A vice-campeã (k = 4, taxa 1,0) tem erro 1,2% pior e é degenerada de outro jeito: com taxa 1,0 o
peso pula em cima de cada amostra, então os pesos finais são literalmente as últimas amostras vistas.

**A ordem do polinômio foi validada contra a realidade**, não só por R²: comparada com a média real
de eficiência por faixa de cilindrada. A ordem 5 prevê 15,44 km/L para 1,0 L contra **15,38 km/L
reais** (186 veículos entre 0,9 e 1,1 L), e 5,84 em 8,0 L contra 5,49 reais. A ordem 7 ajusta as
faixas um pouco melhor mas erra mais na ponta, onde há poucos dados.

## Resultado final

| Grupo | Veículos | Cilindrada | Eficiência | Peso do neurônio |
|---|---|---|---|---|
| Pequenos e eficientes | 467 | 0,6 a 2,5 L | 14,88 a 24,66 km/L | (1,92 ; 19,33) |
| Intermediários | 14.659 | 0,9 a 4,3 L | 7,23 a 14,45 km/L | (2,00 ; 10,20) |
| Motores grandes | 22.841 | 1,3 a 8,4 L | 2,98 a 10,20 km/L | (4,25 ; 7,93) |

`f(x) = -0.01x⁵ + 0.23x⁴ - 2.18x³ + 9.92x² - 23.03x + 30.51`, previsão de **15,44 km/L** para 1,0 L.

**Achado para a análise do relatório:** os grupos se separam quase só por **eficiência** (faixas
limpas, que não se tocam) enquanto a cilindrada se sobrepõe muito. É a falta de normalização: a
eficiência tem amplitude 2,78× maior e domina a distância euclidiana.

**Reprodutibilidade:** o código não fixa semente, mas duas execuções seguidas deram particionamento
idêntico. O que muda entre execuções é só a **numeração** dos grupos. **Ao escrever o relatório,
referir-se aos grupos pelo perfil, nunca pelo número.**

## Pendência

**Montar o relatório** em DOCX ou PDF para o AVA. O template pede: tabela de parâmetros, gráfico,
tabela de agrupamentos, função polinomial, previsão de eficiência e um texto de análise. Todos os
dados estão acima e a figura já existe em `RNC/resultado_rnc.png`.

Detalhe do enunciado: ele manda baixar "S5_RNC.spy", mas o arquivo entregue é `.py`.

## Scripts de apoio (no scratchpad, voláteis)

`busca_parametros_rnc.py`, `diagnostico_rnc.py`, `escolhe_parametros_rnc.py`,
`analisa_rnc_curso.py`, `grafico_rnc.py`.
