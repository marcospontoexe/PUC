# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-08-17 22:02
- **Sessão nº:** 1
- **Status geral:** pronto para revisão

## 1. Objetivo da tarefa

Documentar a pasta da disciplina [16-IA aplicada à Saúde](.) para sessões futuras e, em seguida, revisar e corrigir a [atividade somativa 1](atividade%20somativa%201/) contra os requisitos do respectivo [orientação.pdf](atividade%20somativa%201/orientação.pdf).

## 2. Já feito ✅

**Documentação:**

- Exploração completa da pasta e leitura do código-fonte dos 4 notebooks.
- Auditoria do ambiente: Anaconda, versão do Python, pacotes instalados e ausentes.
- Criados [CLAUDE.md](CLAUDE.md) (enxuto, com índice), [DOCS/ambiente.md](DOCS/ambiente.md), [DOCS/notebooks.md](DOCS/notebooks.md) e [DOCS/datasets.md](DOCS/datasets.md).

**Revisão e correção da atividade somativa 1:**

- Confronto do notebook com os 4 requisitos do enunciado. Diagnóstico: requisitos 2, 3 e 4 cumpridos; requisito 1 (estatísticas básicas) não estava visível no `.ipynb` — só existia dentro do [relatorio_df_uci.html](atividade%20somativa%201/relatorio_df_uci.html), que não é o formato de entrega.
- Aplicadas **todas** as correções da lista em [Diagnóstico_de_Doenças_Cardiovasculares_usando_Machine_Learning.ipynb](atividade%20somativa%201/Diagnóstico_de_Doenças_Cardiovasculares_usando_Machine_Learning.ipynb) (89 → 102 células), detalhadas na seção 5.
- Notebook reexecutado do início ao fim: **0 erros, 0 células não executadas**. HTML de entrega regerado.

## 3. Em andamento 🔧

Nenhum. A revisão foi concluída e o notebook está executado e consistente.

## 4. Próximos passos (planejado) 📋

1. **O utilizador revisar o notebook corrigido** — especialmente as conclusões da seção 4 e a análise de correlação, que foram reescritas com base nos resultados medidos. A somativa 1 está **concluída**: 19 correções aplicadas, notebook executado (45 células, 0 erros, 9 gráficos) e HTML atualizado.
2. ~~Auditar a somativa 2~~ — **concluída**. Ver seção 5b.
3. Modernizar [Explainable-AI.ipynb](Explainable-AI.ipynb) para o stack atual (ver [DOCS/notebooks.md](DOCS/notebooks.md)) — hoje não executa.
4. Commitar o trabalho no repositório [PUC](../) — bloqueado, ver seção 7.

## 5. Decisões e raciocínio 🧠

**Sobre a documentação:**

- Um CLAUDE.md por disciplina, seguindo a convenção já existente em [21-Preparação e Análise Exploratória de Dados](../21-Preparação%20e%20Análise%20Exploratória%20de%20Dados/CLAUDE.md).
- Documentar o método (seeds, split, anti-leakage) e não o código, já que os notebooks não compartilham módulos.

**Correções aplicadas ao notebook da somativa 1:**

| # | Correção | Motivo |
|---|---|---|
| 1 | Nova célula com `describe()` de `trestbps`, `thalach` e `oldpeak` | Requisito 1 do enunciado não estava visível no `.ipynb` |
| 2 | Conclusões: 54%/46% invertidos, corrigido para 45,9% positivos | Contradizia o próprio notebook (139 de 303) |
| 3 | `stratify=df_uci['num']` no split | Sem ele, teste ficava com 50,8% de positivos contra 44,6% no treino |
| 4 | Ranking por Recall + Precisão, F1 e AUC | Acurácia ignora o falso negativo, o erro grave em diagnóstico |
| 5 | Validação cruzada estratificada (5 folds) | Teste de 61 amostras: 1,6 ponto de acurácia = 1 paciente |
| 6 | `VarianceThreshold` removido dos 3 pipelines | Aplicado antes do scaler, selecionava por unidade de medida |
| 7 | `StandardScaler()` novo em cada pipeline | A instância compartilhada quebrava a reexecução fora de ordem |
| 8 | `plt.xlim(0.7, 1.0)` → `plt.xlim(0, 1)` | Eixo truncado exagera diferenças; contraria o fluxograma do enunciado |
| 9 | Curva ROC adicionada | Reforça o requisito 2 e permite escolher o limiar de decisão |
| 10 | Random Forest incluído como baseline em `Pipeline` | Comparação justa entre os 4 modelos |
| 11 | `n_estimators` de 10 → 100 no Random Forest | 10 árvores geram variância alta |
| 12 | One-hot de `cp`, `restecg` e `thal` antes da correlação | Pearson sobre código nominal não tem interpretação direta |
| 13 | Markdown justificando a manutenção dos outliers | Detectados no box plot e antes ignorados sem justificativa |
| 14 | Números fixos da matriz de confusão passam a ser impressos | Ficavam desatualizados a cada mudança de seed |
| 15 | `ProfileReport` comentado, com instrução de reativação | `ydata-profiling` não está instalado e impedia a reexecução |
| 16 | Frase quebrada, "features do sexo feminino", "4 modelos" | Erros de redação |
| 17 | "acurácia de 84%" → ~85% | Defasado após a correção nº 11 (`n_estimators`) e nº 3 (`stratify`) |
| 18 | Correlações da análise do `ProfileReport` recalculadas | Valores lidos a olho no mapa de calor não batiam com nenhum método; `trestbps` constava como 0,000 quando é 0,151, e sobre esse erro havia sido construída a hipótese de "artefato nos dados" |
| 19 | "menor correlação existente, -0,42" → "correlação negativa mais forte" | O texto sugeria que `thalach` era irrelevante, quando é o principal indicador de ausência de doença |

**Descartado:** instalar `ydata-profiling` no env `base`. A biblioteca tem pinos rígidos de versão e poderia forçar downgrade de `numpy`/`pandas`, quebrando o ambiente inteiro por um relatório que já estava gerado.

**⚠️ O risco acima se concretizou (22:42).** O utilizador descomentou as chamadas do `ProfileReport`, adicionou uma célula `pip install ydata-profiling` e executou. O pip desinstalou o `matplotlib` 3.10.6 e falhou no meio: o ambiente ficou sem matplotlib, o notebook parou no primeiro `import` e as saídas foram perdidas. **Já reparado** — restos `~` removidos de `site-packages`, `matplotlib==3.10.6` reinstalado, célula do `pip install` neutralizada com aviso, `ProfileReport` recomentado, notebook reexecutado (45 células, 0 erros, 9 gráficos) e HTML regerado. Procedimento completo de diagnóstico e reparo em [DOCS/ambiente.md](DOCS/ambiente.md).

### 5b. Auditoria e correção da atividade somativa 2

O enunciado da somativa 2 é bem mais extenso que o da 1 (4 grupos de artefatos, 7 requisitos mínimos no programa). **Dois requisitos obrigatórios não estavam entregues** e havia um erro metodológico que comprometia todos os números.

| # | Correção | Motivo |
|---|---|---|
| 1 | **Seção de interpretabilidade criada** — coeficientes/*odds ratio* da Regressão Logística, *permutation importance* de dois modelos e predição individual com contribuição por variável | Requisito 4.5 **ausente**. Usa apenas `sklearn.inspection`, sem dependências novas |
| 2 | **Outliers deixam de ser removidos do conjunto de TESTE** | O filtro descartava 18 e 16 pacientes do teste, das quais **61% e 75% eram diabéticas**; os limites de `Age` no `df_short` excluíam toda paciente acima de 55 anos. Inflava as métricas e é impossível em produção |
| 3 | **Quatro tipos de gráfico novos**: mapa de calor de correlação, histogramas por classe, matriz de confusão e curva ROC | Requisito 4.3 pedia ≥3 tipos; só havia box plots |
| 4 | **Removido o `df_short.drop(['BMI','Insulin'])`** | O texto justificava com "menor correlação com a outcome", mas `Insulin` era o 3º e `BMI` o 4º melhor preditor de 8 — acima de `SkinThickness`, que foi mantida. Sem o drop, o `df_short` passa a ser de fato "com Insulin e SkinThickness", como as tabelas afirmam |
| 5 | `stratify=y` nos dois splits | No `df_short` o teste tinha 40,5% de positivas contra 31,3% no treino |
| 6 | Validação cruzada estratificada (5 folds) nos dois datasets | O teste do `df_short` tinha 79 pacientes; uma paciente valia ~4 pontos de recall |
| 7 | Correlações **calculadas no notebook** em vez de transcritas do `ProfileReport` | Valores lidos a olho no mapa de calor divergiam do real (`Glucose`×`Insulin`: texto 0,659, real 0,581) |
| 8 | `import ydata_profiling` removido da célula de imports | Estava **ativo** e impedia qualquer reexecução no ambiente atual |
| 9 | `SVC(probability=True)`, `max_iter=2000` na LR, AUC em todas as tabelas | Sem `probability` não há como calcular AUC nem plotar ROC |
| 10 | Justificativa das bibliotecas (req. 2.4) e "em quais tarefas o dataset poderia ser útil" (req. 3.4) | Requisitos do enunciado não atendidos |
| 11 | Conclusões reescritas; typos, célula vazia e cabeçalho `print` errado corrigidos | — |

**Segunda rodada (estrutura e coerência do documento), 11 pontos:** numeração das seções refeita para mapear 1:1 nos artefatos do enunciado (com tabela "onde encontrar cada requisito" no topo); resposta explícita sobre PLN não se aplicar a dados tabulares (req. 2.2); seção 1.4 de motivação (req. 1.3); retomada da hipótese inicial sobre ensembles, que os resultados não confirmaram; texto de segunda pessoa uniformizado; leitura escrita dos box plots (req. 4.3 pede descritivo dos insights); subtítulo `df_limpo` que faltava; seção de normalização religada ao que o código faz; rótulos das visualizações corrigidos (são 6 tipos, não 4); `classification_report` importado e não usado removido; bullet vazio; escolha do XGBoost sobre LightGBM/CatBoost justificada.

**A conclusão original se inverteu.** O trabalho afirmava que "as features `Insulin` e `SkinThickness` são extremamente valiosas" — sendo que `Insulin` sequer estava no modelo. Com o drop removido e a interpretabilidade implementada, os *odds ratio* dessas duas variáveis são **1,13 e 1,10**, entre os três menores do modelo; `Glucose` domina com **3,09**. O `df_short` sacrificou 49% do dataset por duas variáveis que quase não agregam.

A validação cruzada mostra **empate técnico** entre os cinco modelos e entre os dois datasets (recall de 0,53 a 0,64, desvios ~0,08). A recomendação passou a ser `df_limpo` + Regressão Logística: usa 724 pacientes em vez de 392, dispensa dois exames caros e é o modelo mais interpretável.

**Resultado analítico relevante:** a validação cruzada mostrou **empate técnico** entre os quatro modelos (recall de 0,756 a 0,784, desvios ~0,04) e o XGBoost ficou em último, contrariando a expectativa registrada na versão anterior das conclusões. O one-hot revelou que o poder preditivo de `thal` está concentrado nas categorias 3 e 7 — a categoria 6 (defeito fixo) é quase irrelevante (+0,105), o que a correlação sobre o código bruto escondia.

## 6. Estado do projeto / ambiente

| Ficheiro | Situação |
|---|---|
| [CLAUDE.md](CLAUDE.md) | Criado — guia enxuto + índice |
| [DOCS/ambiente.md](DOCS/ambiente.md), [DOCS/notebooks.md](DOCS/notebooks.md), [DOCS/datasets.md](DOCS/datasets.md) | Criados |
| [CONTEXTO.md](CONTEXTO.md) | Este handoff |
| [.../Diagnóstico_...ipynb](atividade%20somativa%201/Diagnóstico_de_Doenças_Cardiovasculares_usando_Machine_Learning.ipynb) | **Modificado e reexecutado** (102 células, 0 erros) |
| [.../Diagnóstico_...html](atividade%20somativa%201/Diagnóstico_de_Doenças_Cardiovasculares_usando_Machine_Learning.html) | Regerado a partir do notebook corrigido |
| [.../somativa_2.ipynb](atividade%20somativa%202/somativa_2.ipynb) | **Modificado e reexecutado** (39 → 53 células, 22 de código, 0 erros, 7 gráficos) |
| [.../somativa_2.html](atividade%20somativa%202/somativa_2.html) | Regerado |

**Backups dos notebooks originais** (antes das correções), caso seja preciso comparar ou reverter — ambos em
`C:\Users\marcos\AppData\Local\Temp\claude\c--Users-marcos-Documents-GitHub-PUC-16-IA-aplicada---Sa-de\2fd91f20-5313-4be4-906f-b5ecfb39bedc\scratchpad\`:
`BACKUP_somativa1.ipynb` e `BACKUP_somativa2.ipynb`.
⚠️ Ficam no diretório temporário — copie para um local permanente se quiser preservá-los.

Ambiente: Anaconda em [C:\Users\marcos\anaconda3](file:///C:/Users/marcos/anaconda3), Python 3.13.9 no `base`. `conda`, `jupyter` e `git` não estão no PATH. Notebook em `nbformat` 4.4 — **não aceita o campo `id` nas células**; adicioná-lo gera erro de validação no nbconvert. Branch git: `main`; todos os ficheiros acima estão **não commitados**.

## 7. Bloqueios e pendências ⚠️

- **`git` não é invocável** a partir do shell desta sessão. O commit precisa ser feito manualmente pelo utilizador, ou ele deve informar o caminho do executável.
- Nenhum erro técnico por resolver.

## 8. Comandos úteis

```powershell
# JupyterLab
& "C:\Users\marcos\anaconda3\Scripts\jupyter-lab.exe"

# Reexecutar o notebook inteiro (usado após cada correção)
& "C:\Users\marcos\anaconda3\python.exe" -m jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 "atividade somativa 1\Diagnóstico_de_Doenças_Cardiovasculares_usando_Machine_Learning.ipynb"

# Regerar o HTML de entrega
& "C:\Users\marcos\anaconda3\python.exe" -m jupyter nbconvert --to html "atividade somativa 1\Diagnóstico_de_Doenças_Cardiovasculares_usando_Machine_Learning.ipynb"
```

Não há comandos de build, lint ou teste nesta disciplina.

## 9. Como retomar

Leia este ficheiro e o [CLAUDE.md](CLAUDE.md). A somativa 1 está corrigida, executada e exportada — nada ficou a meio. Continue a partir da seção 4, passo 1 (revisão pelo utilizador) ou passo 2 (auditar a somativa 2), conforme o que ele pedir.
