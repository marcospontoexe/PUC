# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository overview

This is a coursework repository for the **Computação Natural** (Natural Computing) course at PUC. It contains the module PDFs (`1-...pdf` through `8-...pdf`, plus a supplementary paper `a17v38n34p31.pdf`) and Jupyter notebooks implementing the bio-inspired algorithms covered in the course. There is no application code, build system, package manifest, or test suite — this is a set of standalone notebooks.

All notebooks were originally authored for **Google Colab**: some cells call `drive.mount('/content/drive')` or read files from `/content/...`, and each notebook opens with an "Open in Colab" badge. When adapting a notebook to run locally, replace Drive-mount/`/content` paths with local file paths (e.g. `atividade_formativa_2/mapa.PNG` next to `Atividade_somativa_2.ipynb`).

## Notebooks

- **[Algorítimo genético-oneMax.ipynb](Algorítimo genético-oneMax.ipynb)** — Genetic algorithm solving the OneMax problem using the `deap` library (`eaSimple`, tournament selection, one-point crossover, bit-flip mutation).
- **[colônia de abelhas.ipynb](colônia de abelhas.ipynb)** — Artificial Bee Colony algorithm (via the `ecabc` library) solving the 0-1 Knapsack problem, using a `Knapsack01Problem` class adapted from Wirsansky (2020).
- **[colônia de formigas.ipynb](colônia de formigas.ipynb)** — Ant Colony Optimization solving a TSP instance over US state capitals, with a hand-rolled, vectorized `AntColonySolver` class (adapted from the Kaggle notebook by James McGuigan).
- **[atividade_formativa_2/Atividade_somativa_2.ipynb](atividade_formativa_2/Atividade_somativa_2.ipynb)** — The graded formative activity: the same `AntColonySolver`/ACO approach applied to a custom set of locations plotted over [atividade_formativa_2/mapa.PNG](atividade_formativa_2/mapa.PNG). The write-up is in [atividade_formativa_2/marcos daniel santana.docx](atividade_formativa_2/marcos daniel santana.docx).

## Running notebooks locally

There is no `requirements.txt`/environment file in the repo. Dependencies are installed inline via `!pip install <package>` cells (`deap`, `ecabc`) plus `numpy`, `matplotlib`, and `seaborn` from a standard scientific Python environment. To work with a notebook locally:

```powershell
pip install deap ecabc numpy matplotlib seaborn jupyter
jupyter notebook "colônia de formigas.ipynb"
```

Remove or adapt any `google.colab` import / `drive.mount(...)` cell before running outside Colab.
