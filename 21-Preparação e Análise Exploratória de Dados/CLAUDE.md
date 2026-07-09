# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão Geral

Repositório de materiais da disciplina **"Preparação e Análise Exploratória de Dados"** da PUCPR. Contém apenas PDFs das unidades do curso — não há código-fonte, build ou testes.

Quando solicitado a produzir exemplos de código relacionados ao conteúdo, usar **Python** com `pandas`, `numpy`, `matplotlib` e `seaborn`, que são as bibliotecas utilizadas nas videoaulas da disciplina.

---

## Conteúdo das Unidades

### Unidade 01 — Análise Exploratória de Dados
Diferenciação entre três conceitos relacionados:
- **Estatística descritiva**: caixa de ferramentas (média, mediana, moda, desvio-padrão, histogramas, gráficos de barras/setores).
- **Análise descritiva de dados**: aplicação das ferramentas para *comunicar* o que os dados mostram.
- **AED (Análise Exploratória de Dados)**: etapa investigativa que vai além — busca padrões, relações entre variáveis e levanta hipóteses. Não comprova causas; aponta possibilidades a serem testadas por métodos inferenciais.

### Unidade 02 — Análise Descritiva de Dados Univariados
- **Dados univariados**: análise de uma única variável (distribuição, tendência central, dispersão, outliers).
- **Dados multivariados**: análise de múltiplas variáveis e suas interações (correlação, regressão, PCA).
- Ferramentas para univariados: **histogramas** (distribuição), **boxplots** (dispersão e outliers), **tabelas estatísticas** (média, mediana, moda).
- Atenção ao tamanho das classes no histograma: classes muito largas escondem detalhes; muito estreitas fragmentam o gráfico.

### Unidade 03 — Análise Multivariada: Correlação e Visualização
- **Correlação**: mede o quanto duas variáveis "caminham juntas". Correlação ≠ causalidade.
  - Positiva: as duas sobem juntas.
  - Negativa: uma sobe enquanto a outra cai.
  - Nula: sem relação aparente.
- Visualizações multivariadas: **gráficos de dispersão**, **mapas de calor** (heatmaps), **pairplots** (gráfico de dispersão matricial).
- Bibliotecas da disciplina: **Pandas** (cálculo de correlação) e **Seaborn** (visualização — construído sobre Matplotlib, integra diretamente com DataFrames).

### Unidade 04 — Gráficos, Grids e Códigos Visuais
Tipos de gráficos de barras e quando usar cada um:
- **Simples**: uma variável categórica, comparação de frequência ou valor agregado.
- **Agrupadas** (múltiplas): subcategorias lado a lado, para comparar grupos relacionados.
- **Empilhadas**: mostra o total por categoria e a composição das subcategorias.

Boas práticas ensinadas: cores contrastantes, eixo Y iniciando em zero, legendas claras, evitar excesso de categorias.

Também abordados: gráficos de densidade e grids de visualização para análise multivariada avançada.

### Unidade 05 — Detecção de Valores Faltantes e Outliers
- **Valores faltantes** (`NaN`): surgem por falhas na coleta, erros de registro. Dificultam cálculos e distorcem análises.
- **Outliers**: valores muito diferentes do padrão. Podem ser erros *ou* descobertas importantes (fraudes, falhas industriais, eventos extremos).
- Detecção de outliers:
  - **IQR (Intervalo Interquartílico)**: mais comum — define faixa fora da qual os valores são outliers.
  - **Desvios-padrão**: valores muito afastados da média.
  - **Visual**: boxplot (pontos fora da caixa) e gráficos de dispersão.
- Biblioteca utilizada: **Pandas**.

### Unidade 06 — Tratamento de Valores Faltantes (Imputação)
Técnicas de imputação ensinadas, em ordem de complexidade:

| Técnica | Quando usar |
|---|---|
| Substituição pela **média** | Variáveis numéricas com distribuição simétrica |
| Substituição pela **mediana** | Dados assimétricos ou com outliers (mais robusta) |
| Substituição pela **moda** | Variáveis categóricas |
| Valor **constante** (ex.: "desconhecido") | Quando ausência é informação em si |
| **Remoção** da linha/coluna | Quando a quantidade de faltantes é pequena |
| **Avançadas** (KNN, regressão, ML) | Quando as técnicas simples introduzem viés |

A escolha depende do contexto: técnicas simples são rápidas mas podem reduzir variabilidade ou introduzir viés. Imputação inadequada compromete modelos preditivos.

### Unidade 07 — Discretização de Dados
Transforma variáveis **contínuas** em **discretas** (categorias/intervalos). Útil para algoritmos que exigem dados categóricos (árvores de decisão, regras de associação) e para facilitar interpretação.

**Não supervisionada** (sem considerar variável-alvo):
- **Por intervalos iguais** (*equal width*): divide o range em faixas de mesmo tamanho.
- **Por frequência** (*equal frequency*): cada faixa contém aproximadamente o mesmo número de registros.

**Supervisionada** (orientada pela variável-alvo):
- **Por entropia / ganho de informação**: maximiza a "pureza" das categorias em relação à variável-alvo.
- **Por similaridade / clustering**: agrupa valores similares minimizando variabilidade interna.

Bibliotecas utilizadas: **Pandas** e **Numpy**.
