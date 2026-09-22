# Atividade Somativa 2 — unidade 08 (RNC + RNT)

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md).
Pasta: [../atividade_2/](../atividade_2/).
Relatório: [`relatorio-atividade-somativa-2.md`](../atividade_2/relatorio-atividade-somativa-2.md).
Entrega: [`Atividade_Somativa_2_Respondida.docx`](../atividade_2/Atividade_Somativa_2_Respondida.docx).

## O que a atividade pede

Duas partes. Na **RNC**, ajustar **três** redes competitivas (cilindrada × eficiência,
cilindrada × CO₂ e — a novidade — eficiência × CO₂) e as três regressões, entregando tabela de
parâmetros, gráficos, tabelas de agrupamento, funções polinomiais, as previsões e um texto de
análise. Na **RNT**, o código foi dividido em `S8_RNT_train.py` (treina e **salva** o modelo em
`C:\RN\S8_RNT_treinada.h5`) e `S8_RNT_test.py` (carrega e avalia).

## Dado de partida importante

**As três bases são idênticas às da atividade formativa da unidade 07**: `base_veiculos_2.csv` ==
`base_veiculos_1.csv`, `dolar_treinamento_2.csv` == `dolar_treinamento.csv`, `dolar_teste_2.csv` ==
`dolar_teste.csv`. Só o código mudou. Isso permitiu reaproveitar as respostas já validadas para
`rnc1`, `rnc2` e os dois primeiros polinômios, concentrando a busca na terceira rede.

## Parâmetros escolhidos

| Parâmetro | Era | Ficou | | Parâmetro | Era | Ficou |
|---|---|---|---|---|---|---|
| `num_neur_rnc1` | 4 | **3** | | `janela_prev` | 10 | **50** |
| `num_neur_rnc2` | 8 | **10** | | `funcao_perda` | `binary_crossentropy` | **`mean_squared_error`** |
| `num_neur_rnc3` | 4 | **10** | | `otimizador` | `RMSprop` | `RMSprop` |
| `epocas_rnc2/3` | 1 | **10** | | `neuronios_LSTM` | 5 | **4** |
| `taxa_aprend_rnc1` | 0,01 | **0,30** | | `neuronios_densa` | 50 | **1** |
| `taxa_aprend_rnc2` | 2,00 | **0,50** | | `epocas` | 3 | **50** |
| `taxa_aprend_rnc3` | 1,00 | **0,50** | | `lote` | 100 | **32** |
| `ordem_pol1` | 1 | **7** | | | | |
| `ordem_pol2` | 10 | **5** | | | | |
| `ordem_pol3` | 6 | **4** | | | | |

## Os dois achados centrais

### 1. As redes 2 e 3 produzem a mesma partição

**37.964 dos 37.967 veículos (99,99%) caem no mesmo grupo nas duas redes.** As dez faixas de CO₂
são idênticas; só três veículos mudam de lado. Trocar cilindrada por eficiência no eixo X não mudou
nada porque **a rede nunca usou o eixo X** — o CO₂ (amplitude 770,86) domina a distância euclidiana
sobre a cilindrada (7,80) e a eficiência (21,68). Um único grupo cobre 83% da amplitude da
cilindrada e 75% da eficiência.

É o fenômeno já visto nas unidades 05 e 07, aqui na sua forma mais nítida: duas redes com entradas
diferentes chegando ao mesmo resultado.

### 2. A relação eficiência × CO₂ é física, não estatística

O produto `eficiência (km/L) × CO₂ (g/km)` tem unidade de **g de CO₂ por litro de combustível** e
vale **2.353,8 ± 77,0** — variação de 3,3%. O valor de referência da EPA para gasolina é 2.348 g/L.
A base **calcula** o CO₂ a partir do consumo; não o mede.

Consequência: a hipérbole de **um parâmetro** `CO₂ = 2.354/eficiência` atinge R² 0,9884, contra
0,9886 do polinômio de ordem 10, que tem onze coeficientes. E como polinômio não tem assíntota, a
ordem 3 prevê **CO₂ negativo (−98,66)** no extremo superior — por isso a escolha caiu na ordem 4.

## Parte RNT

### Resultados

| | MSE | MAE | R² |
|---|---|---|---|
| Treinamento | 0,0171 | 0,1008 | **0,9820** |
| Teste | 0,0239 | 0,0930 | **0,9213** |

Ponto de partida (com `neuronios_densa` corrigido para 1, senão nem roda): R² **−0,6555** no treino
e **−3,0004** no teste — exatamente os "valores negativos" que o enunciado menciona.

### O bug do normalizador melhora a nota

`S8_RNT_test.py` linha 46 faz `scaler.fit_transform(test_data)`, criando um normalizador novo sobre
o teste. Medido com o mesmo modelo: protocolo da atividade R² **0,9285**; protocolo correto
**0,9248**. O bug **favorece** o número, porque estica o teste (R$ 3,00–5,00) para [0,1] inteiro em
vez de comprimi-lo em [0,143 · 0,714]. É vazamento de dados: usa o mínimo e o máximo de toda a
série futura.

### Contra o preditor trivial, com 5 sementes

Como o código não fixa semente, a comparação só faz sentido repetida. R² de teste variou de 0,9197
a 0,9322 (a execução entregue, 0,9213, ficou na parte baixa).

| Métrica (teste) | Rede (média de 5) | Repetir o último valor |
|---|---|---|
| MSE | **0,0219** | 0,0228 |
| MAE | 0,0859 | **0,0772** |
| R² | **0,9280** | 0,9251 |

A rede ganha no MSE e no R², perde no MAE (11% pior). 4 das 5 inicializações superaram o trivial no
R². A leitura: a rede **suaviza** — acerta melhor nos movimentos bruscos, erra mais nos dias calmos.

## Defeitos encontrados no código

`S8_RCN.py`: linha 83 `inshape3 = combinacao2.shape[1]` (deveria ser `combinacao3`); linha 238 a
tabela 3 rotula a segunda coluna como `'Cil. (max)'` mas o valor é o máximo da **eficiência**;
linha 226 comentário errado; linha 349 usa `+10` onde os outros usam `+2`; linha 275 formata com
`{:.2f}` e imprime `0.00x^7` para um coeficiente de 0,0021.

`S8_RNT_test.py`: linha 46 o normalizador; linhas 39 e 42 atribuição duplicada.

## Armadilha do `.docx`, que custou tempo

O Word recusava o documento gerado com **"arquivo aparentemente corrompido"**, enquanto o
`python-docx` o abria sem reclamar. Depois de isolar por bisecção:

- não era XML malformado, nem relação quebrada, nem tamanho, nem a imagem em si;
- documento em branco + 8 imagens: **abre**. Template intacto + 4 imagens: **abre**.
  Template com o **corpo esvaziado** + 4 imagens: **recusa**.

**Causa:** o `python-docx` numera o `<wp:docPr>` de cada imagem a partir do maior `id` que encontra
no corpo. Com o corpo esvaziado ele recomeça em 1, e o cabeçalho deste template já usa os ids 2 e
16, e o rodapé 5 e 8. A partir da quarta imagem o Word rejeita o arquivo.

**Correção**, aplicada no gerador antes de salvar:

```python
NS_WP = "{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}"
for i, dp in enumerate(corpo.iter(f"{NS_WP}docPr"), start=1000):
    dp.set("id", str(i))
    dp.set("name", f"Imagem {i - 999}")
```

Vale para **qualquer** docx construído a partir de um template cujo corpo seja esvaziado. Junto com
isso, soltar as relações de imagem e as de `customXml` do template (o `python-docx` não regrava as
partes `customXml/itemN.xml` mas mantém as relações, deixando 4 referências órfãs) derrubou o
arquivo de 1.631 KB para 983 KB.

## Outras decisões

- **Figuras separadas no `.docx`.** As figuras combinadas (3 painéis numa linha) ficam legíveis na
  tela, mas comprimidas nos 6,69 pol úteis do A4 os rótulos somem. O `.docx` usa cinco figuras
  individuais, em [../atividade_2/figuras/](../atividade_2/figuras/), numeradas como no enunciado.
  O markdown continua com as combinadas.
- **O `.docx` parte do próprio template**, o que preserva estilos, margens, cabeçalho com o brasão,
  rodapé e numeração de página da PUCPR.
- **"Nome completo:" ficou em branco** na capa, para o utilizador preencher.
- O enunciado lista como entregáveis só as previsões a partir da cilindrada, sem mencionar a
  terceira que o código acrescentou. As três estão no relatório.

## Verificação

Os três scripts foram executados de verdade, na ordem que o enunciado manda. A execução real do
`S8_RCN.py` — sem semente fixa — reproduziu **exatamente** as faixas encontradas na varredura com
semente fixa, o que mostra que a configuração escolhida converge independentemente da
inicialização. As métricas nas figuras da RNT vêm do modelo salvo pela execução do
`S8_RNT_train.py`, e batem com o que os scripts imprimiram no console.
