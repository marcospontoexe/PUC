# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão Geral

Materiais da disciplina **"IA aplicada à Saúde"** (PUCPR). É uma subpasta do monorepo [PUC](../), que agrupa uma pasta por disciplina do curso. Não há build, testes nem pacote Python — o conteúdo é:

- **PDFs numerados (1–8)**: slides das unidades, do panorama de IA em saúde até ética/privacidade e futuro da informática em saúde.
- **Notebooks-tutorial do professor**: [Explainable-AI.ipynb](Explainable-AI.ipynb) e [Clinical_POS_Tagging_and_NER.ipynb](Clinical_POS_Tagging_and_NER.ipynb).
- **Atividades somativas do aluno**: [atividade somativa 1](atividade%20somativa%201/) e [atividade somativa 2](atividade%20somativa%202/), cada uma com dataset CSV, notebook, `orientação.pdf` e os HTMLs de entrega.

Todo o conteúdo (markdown dos notebooks, comentários de código, títulos de gráficos) é escrito em **português** — mantenha esse padrão ao editar ou gerar código aqui.

## Início rápido

`conda`, `jupyter` e `git` **não estão no PATH**. Use os binários pelo caminho completo:

```powershell
& "C:\Users\marcos\anaconda3\Scripts\jupyter-lab.exe"
```

Vários pacotes importados pelos notebooks (`ydata-profiling`, `shap`, `lime`, `flair`, …) **não estão instalados** — confira antes de afirmar que uma célula roda. Detalhes em [DOCS/ambiente.md](DOCS/ambiente.md).

## Índice de contexto detalhado

Consulte o ficheiro específico quando precisar de mais informação sobre o tópico:

| Tópico | Ficheiro |
|---|---|
| Interpretador, comandos do Jupyter, pacotes instalados e ausentes | [DOCS/ambiente.md](DOCS/ambiente.md) |
| Método compartilhado pelos notebooks, seeds, anti-data-leakage, APIs quebradas | [DOCS/notebooks.md](DOCS/notebooks.md) |
| Datasets, alvos, dicionário de variáveis e armadilhas dos dados | [DOCS/datasets.md](DOCS/datasets.md) |

Estado da sessão e próximos passos: [CONTEXTO.md](CONTEXTO.md).
