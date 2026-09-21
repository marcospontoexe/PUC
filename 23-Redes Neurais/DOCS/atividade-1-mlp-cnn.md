# Atividade Somativa 1 — MLP × CNN (unidade 04)

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md). Pasta:
[../atividade_1/](../atividade_1/).

## Setup

- Orientação em `atividade_1/Orientação.pdf`; template Word extraído via `python-docx`.
- **Dados:** as 20 imagens de `atividade_1/RN/RN/*.png` foram copiadas para `C:\RN\*.png`, na raiz
  do disco C:, exatamente como a orientação instrui. Os scripts do professor usam caminho fixo
  (`HD='C'`, `pasta='RN'`).
- **Por que copiar em vez de mudar o código:** manter os scripts idênticos ao que o aluno usaria no
  Spyder.

## Configurações escolhidas

Testadas ~8 configurações de MLP e ~7 de CNN (scripts de busca ficaram no scratchpad), variando
ativações, função de perda, otimizador, número de camadas/neurônios/filtros, tamanho do kernel,
percentual de treino, épocas e batch size.

| | MLP (`S4_MLP.py`) | CNN (`S4_CNN.py`) |
|---|---|---|
| Arquitetura | 2 ocultas: 256 e 128, tanh | kernels 3×3, 32 e 64 filtros, densa de 128 |
| Saída | softmax | softmax |
| Perda | `categorical_crossentropy` | `categorical_crossentropy` |
| Otimizador | `adam` | `adam` |
| Split | 20% teste | 40% treino |
| Épocas / lote | 15 / 128 | 5 / 128 |
| Resultado MNIST | loss 0,1059 · acc **97,16%** | loss 0,0578 · acc **98,19%** |
| Conjunto 1 | **10/10** | **10/10** |

## Bugs do template corrigidos

- MLP: saída `relu` + `mean_absolute_error` (inadequados para classificação).
- CNN: saída `sigmoid` + `categorical_hinge`, e kernel 9×9 com apenas 2 filtros (o 9×9 encolhia
  demais a imagem).
- Acrescentado `set_random_seed(42)` e `print()` das previsões no console.

**Por que fixar a semente:** sem ela, os resultados da Parte 1 e da Parte 2 variariam por acaso, e
seria impossível separar "variação por aleatoriedade" de "variação por mudança de distribuição das
imagens" — que é justamente o ponto pedagógico da Parte 3.

## Parte 2 (conjunto do professor)

Criados `S4_MLP_partB.py` e `S4_CNN_partB.py` como **arquivos separados**, não editando os
originais, para manter os dois estados reproduzíveis (a orientação pede resultados de ambas as
partes no relatório).

- MLP Parte 2: **3/10** (acertou 0, 2, 5).
- CNN Parte 2: **6/10** (acertou 1, 2, 3, 4, 5, 8).
- Loss e accuracy **idênticos** à Parte 1, porque são calculados sobre o split do MNIST; as imagens
  da pasta RN só entram no `model.predict()` qualitativo, nunca no `model.evaluate()`.

## Por que a queda no 2º conjunto

Comparação estatística das 20 imagens contra o MNIST: os desenhos do professor têm **metade da
tinta** (0,083 contra 0,158), **quase nenhum anti-aliasing** (0,05 contra 0,39), caixa do dígito
variando de 15 a 22 px (o MNIST normaliza sempre para 20) e centro de massa deslocado até 3 px.

## Experimento de data augmentation

Duas estratégias foram testadas: pré-processamento estilo MNIST na entrada e augmentation no treino.
**Decisão do utilizador: usar apenas augmentation**, mencionando no relatório que ele resolve parte
do problema de padronização.

`S4_MLP_aug.py` e `S4_CNN_aug.py`: mesmos parâmetros mais `RandomRotation(0.08)`,
`RandomTranslation(0.10, 0.10)` e `RandomZoom(0.10)`, com épocas triplicadas (MLP 15→45, CNN 5→15)
porque o augmentation torna a convergência mais lenta. Ambos testam os dois conjuntos na mesma
execução.

| | Sem augmentation | Com augmentation |
|---|---|---|
| MLP, conjunto 2 | 3/10 | **9/10** |
| CNN, conjunto 2 | 6/10 | **9/10** |
| MLP, MNIST | 97,16% | 98,27% |
| CNN, MNIST | 98,19% | 98,54% |

Ambos mantiveram 10/10 no conjunto 1.

## Relatório entregue

`atividade_1/Atividade_Somativa_1_Respondida.docx`, montado a partir do template via `python-docx`,
com tabelas de parâmetros, previsões e loss/métrica para MLP e CNN nas Partes 1 e 2, a análise da
Parte 3 (as duas perguntas da orientação) e a seção "Experimento complementar — Data Augmentation"
com 3 tabelas e 5 parágrafos.

## Pendências

- **"Nome Completo:" na capa não foi preenchido.** Não há nome real disponível, e o e-mail do
  utilizador não é um nome verificável. Nunca inferir.
- Os gráficos de treino (`plt.show()` dos 4 scripts) não foram salvos em arquivo, porque a execução
  automatizada usou backend `Agg`. Para tê-los: rodar no Spyder ou pedir para gerá-los.
