# Datasets

| Arquivo | Origem | Alvo | Observação |
|---|---|---|---|
| [heart-disease-uci.csv](../atividade%20somativa%201/heart-disease-uci.csv) | Cleveland Clinic / UCI — 303 linhas × 14 colunas | `num` | Sem valores ausentes; outliers reais em `chol`, `trestbps` e `oldpeak` |
| [diabetes.csv](../atividade%20somativa%202/diabetes.csv) | Pima Indians Diabetes — 768 linhas × 9 colunas | `Outcome` | **Zeros são faltantes disfarçados** — ver abaixo |
| `processed.cleveland.data` | Baixado por URL direto da UCI em [Explainable-AI.ipynb](../Explainable-AI.ipynb) | `target` | Requer rede; lido com `na_values='?'` |

## Armadilha do dataset Pima ([diabetes.csv](../atividade%20somativa%202/diabetes.csv))

Zeros em `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin` e `BMI` são clinicamente impossíveis — são valores ausentes codificados como zero. O notebook os converte para `NaN` **antes de qualquer análise**. `Pregnancies` e `Outcome` aceitam zero legitimamente e ficam de fora dessa conversão.

Percentual de ausentes após a conversão: `Insulin` 48,7%, `SkinThickness` 29,6%, `BloodPressure` 4,6%, `BMI` 1,4%, `Glucose` 0,7%.

A estratégia adotada foi comparar dois DataFrames:

- `df_limpo` — remove as linhas com ausentes em `Glucose`/`BloodPressure`/`BMI` e **descarta** as colunas `Insulin` e `SkinThickness`.
- `df_short` — mantém todas as colunas e remove todas as linhas com qualquer `NaN`.

Conclusão registrada no notebook: `df_short` vence, porque `Insulin` e `SkinThickness` elevam o Recall da Regressão Logística de 0,524 para 0,700.

## Alvo multiclasse → binário (datasets Cleveland/UCI)

`num` (ou `target`) tem valores 0–4. Todos os valores 1–4 são convertidos para `1` (presença de doença); `0` permanece ausência. Isso segue a convenção da literatura que usa esse dataset e vale tanto para a [atividade somativa 1](../atividade%20somativa%201/) quanto para [Explainable-AI.ipynb](../Explainable-AI.ipynb).

## Dicionário de variáveis — Cleveland/UCI

`age` idade · `sex` (0 mulher, 1 homem) · `cp` tipo de dor torácica (1 angina típica … 4 assintomática) · `trestbps` pressão arterial em repouso · `chol` colesterol sérico · `fbs` glicemia de jejum > 120 mg/dl · `restecg` eletrocardiograma de repouso · `thalach` frequência cardíaca máxima atingida · `exang` angina induzida por exercício · `oldpeak` depressão do segmento ST · `slope` inclinação do segmento ST · `ca` nº de vasos principais por fluoroscopia · `thal` teste de tálio (3 normal, 6 defeito fixo, 7 defeito reversível).

Preditores mais fortes encontrados na análise: `thal`, `cp`, `ca`, `oldpeak` e `exang`. `thalach` alto é o principal indicador de **ausência** de doença.
