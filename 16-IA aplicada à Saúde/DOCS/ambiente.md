# Ambiente e Comandos

## Interpretador

Os notebooks foram salvos com o kernel `Python [conda env:base]` (Python 3.13.5). O `base` instalado atualmente na máquina é **Python 3.13.9**, em [C:\Users\marcos\anaconda3](file:///C:/Users/marcos/anaconda3).

`conda`, `jupyter` e `git` **não estão no PATH** do PowerShell. Use sempre o caminho completo dos binários.

## Comandos

```powershell
# Abrir o JupyterLab na pasta da disciplina
& "C:\Users\marcos\anaconda3\Scripts\jupyter-lab.exe"

# Executar um notebook inteiro no lugar (sem abrir a UI)
& "C:\Users\marcos\anaconda3\python.exe" -m jupyter nbconvert --to notebook --execute --inplace "atividade somativa 2\somativa_2.ipynb"

# Regerar o HTML de entrega a partir do notebook
& "C:\Users\marcos\anaconda3\python.exe" -m jupyter nbconvert --to html "atividade somativa 2\somativa_2.ipynb"

# Conferir o que está instalado antes de afirmar que uma célula roda
& "C:\Users\marcos\anaconda3\python.exe" -m pip list
```

Caminhos com espaços e acentos são a norma nesta disciplina — sempre entre aspas.

## Pacotes

### Instalados no `base`

| Pacote | Versão |
|---|---|
| pandas | 2.3.3 |
| numpy | 2.3.5 |
| scikit-learn | 1.7.2 |
| xgboost | 3.4.0 |
| matplotlib | 3.10.6 |
| seaborn | 0.13.2 |
| tensorflow | 2.21.0 |
| nltk | 3.9.2 |
| jupyterlab | 4.4.7 |
| notebook | 7.4.5 |

### Importados pelos notebooks mas **ausentes** do ambiente

Precisam de `pip install` antes de executar as células correspondentes:

- `ydata-profiling` — usado nas duas atividades somativas (`ProfileReport`). **Ver o aviso abaixo antes de instalar.**
- `shap`, `lime`, `eli5`, `alibi`, `pdpbox` — usados em [Explainable-AI.ipynb](../Explainable-AI.ipynb).
- `flair`, `transformers` — usados em [Clinical_POS_Tagging_and_NER.ipynb](../Clinical_POS_Tagging_and_NER.ipynb).

### ⚠️ Não instale `ydata-profiling` no ambiente `base`

Já aconteceu uma vez (2026-08-17) e quebrou o ambiente inteiro.

O `ydata-profiling` exige uma versão de `matplotlib` mais antiga que a instalada (3.10.6). O pip desinstala a versão atual antes de colocar a antiga; a operação falhou no meio e o ambiente ficou **sem matplotlib**, com nenhuma célula de nenhum notebook executando. O sintoma é enganoso:

```
ModuleNotFoundError: No module named 'matplotlib.colorbar'
```

`matplotlib.colorbar` é módulo interno do próprio matplotlib — se ele "não existe", a instalação está corrompida, não falta uma dependência.

**Como diagnosticar:** procure diretórios com prefixo `~` em `site-packages` (por exemplo `~atplotlib-3.10.6.dist-info`). Esse prefixo é a marca que o pip deixa em desinstalação interrompida.

**Como reparar:**

```powershell
Remove-Item "C:\Users\marcos\anaconda3\Lib\site-packages\~atplotlib-3.10.6.dist-info" -Recurse -Force
Remove-Item "C:\Users\marcos\anaconda3\Lib\site-packages\matplotlib\~pl-data" -Recurse -Force
& "C:\Users\marcos\anaconda3\python.exe" -m pip install --force-reinstall --no-deps "matplotlib==3.10.6"
```

**Como evitar:** os relatórios `relatorio_*.html` já estão gerados e versionados — não é preciso instalar nada para trabalhar nas atividades. Se for mesmo necessário regenerá-los, use um ambiente separado:

```powershell
conda create -n perfil python=3.11 -y
conda activate perfil
pip install ydata-profiling
```

Não existe [requirements.txt](../requirements.txt) nem `environment.yml` na disciplina; as dependências estão apenas implícitas nos imports dos notebooks.
