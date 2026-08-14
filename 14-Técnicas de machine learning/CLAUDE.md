# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este repositório

Pasta da disciplina **14 - Técnicas de Machine Learning** do curso de IA da PUC-PR, dentro do
monorepo acadêmico `PUC` (a raiz do git é um nível acima). Não há código de aplicação, build,
lint ou testes — o conteúdo é **100% Jupyter Notebooks + datasets + PDFs de aula**.

Dois tipos de conteúdo, com propósitos distintos:

- [ConteudoSemanas/](ConteudoSemanas/) — material fornecido pelo professor (aulas, videoaulas e
  gabaritos), organizado por semana. **Referência, não trabalho autoral.** Semanas 2 a 8 cobrem,
  nesta ordem: pré-processamento/seleção de atributos/clustering → algoritmos supervisionados →
  scaling e PCA → métricas → pipelines e otimização de hiperparâmetros → séries temporais.
- [Atividade_somativa_1/](Atividade_somativa_1/) e [Atividade_somativa_2/](Atividade_somativa_2/) —
  os trabalhos avaliativos do usuário. **É aqui que o trabalho real acontece.**

## Ambiente

O `python` do PATH é o stub da Microsoft Store e **não serve**. Os notebooks rodam no ambiente
`base` do Anaconda (kernel declarado: `Python [conda env:base] *`, Python 3.13.5):

```powershell
& "C:\Users\marcos\anaconda3\python.exe" ...
& "C:\Users\marcos\anaconda3\Scripts\conda.exe" ...
& "C:\Users\marcos\anaconda3\Scripts\jupyter.exe" lab
```

`git` também não está no PATH — usar o embutido no GitHub Desktop:
`C:\Users\marcos\AppData\Local\GitHubDesktop\app-3.6.3\resources\app\git\cmd\git.exe`

**Pacotes ausentes no `base`:** `lightgbm`, `prophet`, `ydata-profiling`, `pmdarima`. Os notebooks
das semanas 3, 4, 6 e 8 importam esses pacotes e falharão logo na primeira célula. Instalar antes
de executá-los. Já instalados: pandas 2.3.3, numpy 2.3.5, scikit-learn 1.7.2, xgboost 3.4.0,
statsmodels, matplotlib, seaborn, openpyxl, jupyterlab.

## Convenções que quebram as coisas se ignoradas

**Caminhos relativos à pasta do notebook.** Todo `pd.read_csv`/`read_excel` usa nome de arquivo nu
(`'seoul_bike_data.xlsx'`, `'dolar.tsv'`). Sempre execute com o CWD na pasta do próprio notebook.
Exceção única: [Semana3_TecnicasMachineLearning_ML.ipynb](ConteudoSemanas/Semana3/Semana3_TecnicasMachineLearning_ML.ipynb)
lê `../Semana8/dolar.tsv`.

**Arquivos `.tsv` exigem `sep='\t'`** (`brasileirao.tsv`, `saldoconta.tsv`, `dolar.tsv`); vários
`.csv` das aulas vêm da UCI com `sep=';'`.

**Ignore `.ipynb_checkpoints/`** em buscas — são cópias automáticas do Jupyter e poluem qualquer
grep/glob com duplicatas desatualizadas.

**Notebooks são commitados com os outputs**, por isso alguns passam de 8 MB. Ao editar, prefira
alterações cirúrgicas de célula a reescrever o arquivo inteiro.

**Arquivos `.html` são artefatos gerados, não fontes.** `relatorio.html` e
`relatorio_salvo_nesta_mesma_pasta.html` vêm de `ProfileReport(df).to_file(...)` do `ydata_profiling`;
os demais (`regression.html`, `regrssion_XGBoost.html`) são exports do notebook via `nbconvert`.
Nos notebooks essas chamadas ficam **comentadas** depois que o relatório é gerado — mantenha assim.

## O pipeline de referência (Atividade Somativa)

[Atividade_somativa_2/regression.ipynb](Atividade_somativa_2/regression.ipynb) é a evolução da
somativa 1 e o artefato mais completo do repositório — use-o como modelo estrutural. A somativa 1
é entrega fechada; não a altere para "melhorar".

Dataset `seoul_bike_data.xlsx` (8.760 linhas horárias), alvo **`Rented Bike Count`** (regressão).
A espinha dorsal, em 10 seções numeradas:

1. Carga + profiling → 2. limpeza (drop de `DateTime` e `Dew point temperature(°C)` por
multicolinearidade) → 3. split em **três** conjuntos (treino/validação/teste, `random_state=35`),
onde a validação existe só para o **early stopping** do XGBoost → 4. preparação (outliers por IQR,
`VarianceThreshold`, `SelectKBest`, `StandardScaler`) → 5. treino do `XGBRegressor` →
6. métricas → 7. os mesmos passos reescritos como `Pipeline` do sklearn, em variantes acumulativas →
8. comparação das variantes → 9. `GridSearchCV` → 10. conclusões.

**Regra metodológica central, repetida em todo o notebook:** todo transformador aprende
(`fit`/`fit_transform`) **exclusivamente no conjunto de treino** e apenas transforma (`transform`)
validação e teste — inclusive os limites de outliers do IQR. Qualquer sugestão que recalcule
estatísticas no teste é vazamento de dados e contraria o texto do próprio notebook.

**Nomenclatura por sufixo encadeado**, que sinaliza o estágio do dado: `_limpo` (sem outliers) →
`_vt` / `_kbest` (pós-seleção de atributos) → `_normalizado` (pós-scaler); `_early_stp` marca o
subconjunto de treino reduzido, e cada pipeline gera `previsoes_<nome_do_pipeline>`. Ao adicionar
uma variante, siga a cadeia em vez de inventar nomes novos.

## Estilo esperado nos notebooks

O padrão dos arquivos (e a preferência explícita do usuário) é **didático e em português**:

- Célula markdown explicando o **conceito** antes de cada bloco de código — o que é a técnica, por
  que se aplica ali, e a interpretação do resultado obtido.
- Comentário inline em **cada** import e em **cada** hiperparâmetro relevante, explicando o papel
  daquele valor.
- Alternativas descartadas ficam como linhas comentadas logo abaixo da ativa (ex.: os três
  `fit_transform` concorrentes na célula do `StandardScaler`) — é um registro de experimento
  deliberado, não código morto a ser limpo.

## Ponto de atenção conhecido

Na seção 8 de [regression.ipynb](Atividade_somativa_2/regression.ipynb), as variáveis `rmse_*` são
calculadas como `np.sqrt(mean_absolute_error(...))` — a raiz do MAE, não o RMSE. A comparação entre
pipelines continua monotônica, mas os números não são RMSE. Só corrija se o usuário pedir; se ele
citar esses valores, vale sinalizar.

## Documentação de apoio

Contexto detalhado por tópico deve ir em `DOCS/` (criar sob demanda) e ser referenciado aqui como
índice, mantendo este arquivo enxuto. Handoffs entre sessões vão em `CONTEXTO.md` na raiz.
