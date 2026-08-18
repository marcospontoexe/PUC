# Notebooks: método compartilhado e pontos de atenção

Cada notebook é autocontido — não há módulos compartilhados, e o mesmo pipeline é reescrito do zero em cada um. O que se repete entre eles, e deve ser preservado ao editar, é o **método**, não o código.

## O pipeline padrão da disciplina

1. Carga do CSV → EDA → tratamento de faltantes e outliers → split → padronização → treino de vários modelos → comparação por métricas → conclusões em markdown.
2. **Alvo multiclasse vira binário** nos datasets Cleveland/UCI — ver [datasets.md](datasets.md).
3. **Split 80/20 com seed fixa**: `random_state=35` nas atividades somativas, `seed = 42` em [Explainable-AI.ipynb](../Explainable-AI.ipynb). Não troque as seeds — os números citados no markdown e nos HTMLs de entrega dependem delas.
4. **Anti-data-leakage explícito**: os limites de outlier (IQR sobre Q1/Q3) e o `StandardScaler` são aprendidos **apenas em `X_train`** e depois aplicados a treino e teste. O markdown chama isso de "Regra de Ouro"; qualquer alteração precisa manter esse comportamento.
5. **Comparação de modelos via `Pipeline`**: `StandardScaler` + estimador, para os cinco modelos padrão — Regressão Logística, KNN, Random Forest, XGBoost e SVM — avaliados por Acurácia, Precisão, Recall e F1. Em diagnóstico médico o notebook privilegia **Recall** sobre Precisão; conclusões devem refletir isso.
6. **`ProfileReport` (ydata_profiling)** gera os `relatorio_*.html` versionados ao lado do notebook. As chamadas ficam **comentadas** depois de o HTML ter sido gerado — é intencional, para o notebook reexecutar rápido. Não descomente sem motivo.
7. Cada atividade tem um `.html` irmão do `.ipynb` — é o artefato de entrega. Se o notebook mudar, o HTML precisa ser regerado (comando em [ambiente.md](ambiente.md)).

## Atividades somativas

- [atividade somativa 1](../atividade%20somativa%201/) — diagnóstico de doenças cardiovasculares com o dataset Cleveland/UCI. Parte de um artigo-tutorial (EDA + Random Forest, acurácia 84%) e segue para a atividade em si: EDA com `ProfileReport`, box plots, scatter com matiz, e três pipelines `VarianceThreshold` + `StandardScaler` + modelo (Regressão Logística, SVM-rbf, XGBoost).
- [atividade somativa 2](../atividade%20somativa%202/) — predição de risco de diabetes na população Pima, enquadrada como prova de conceito para uma clínica fictícia de atenção primária. Compara os cinco modelos padrão sobre os dois DataFrames descritos em [datasets.md](datasets.md).

Cada pasta tem seu `orientação.pdf` com o enunciado da atividade.

## [Explainable-AI.ipynb](../Explainable-AI.ipynb) — não roda como está

Tutorial que demonstra sete técnicas de XAI sobre um Random Forest (sklearn) e uma rede neural (Keras) treinados no dataset Cleveland: **Feature/Permutation Importance (ELI5)**, **LIME**, **Anchor**, **SHAP**, **PDP**, **ALE** e **Counterfactual**.

Foi escrito para versões antigas do stack e quebra no ambiente atual. Ao mexer nele, **migre a API em vez de contornar o erro**:

- `plot_confusion_matrix` — removido do scikit-learn; usar `ConfusionMatrixDisplay` (já importado no notebook).
- `tf.compat.v1.disable_v2_behavior()` — exigido pelo alibi, que ainda dependia de construções do TF1.
- `pdp.pdp_isolate`, `pdp.pdp_plot`, `info_plots` — API antiga do pdpbox.
- `alibi.utils.mapping` (`ohe_to_ord`, `ord_to_ohe`) — caminho de import mudou.
- `shap_values[1]` — indexação do SHAP legado.

Além disso, `shap`, `lime`, `eli5`, `alibi` e `pdpbox` não estão instalados.

## [Clinical_POS_Tagging_and_NER.ipynb](../Clinical_POS_Tagging_and_NER.ipynb) — feito para o Colab

Tutorial do Prof. Lucas Oliveira (HAILab-PUCPR). Cobre:

1. Pré-processamento com NLTK — tokenização, segmentação de sentenças, stemming RSLP e stop-words em português. O markdown alerta que remover a negação ("não") pode inverter o sentido de um texto clínico.
2. POS-tagging clínico com Flair, modelo `pt-pos-clinical` do HAILab.
3. NER com Flair sobre o corpus `PortugueseClinicalNER` (formato IOB), mais modelos `pucpr/*` do HuggingFace — no exemplo, `pucpr/clinicalnerpt-pharmacologic`.

Cuidados ao executar: usa `!pip install`, **clona um repositório do GitHub** e escreve `train.txt` / `test.txt` / `dev.txt` no diretório corrente — rodar localmente polui a pasta da disciplina. A célula de treino do Flair é intencionalmente não executada (custo de GPU). Prefira executá-lo no Google Colab.
