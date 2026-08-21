# Otimização de Rotas com Colônia de Formigas (ACO) aplicada a Curitiba

Implementação de um algoritmo bioinspirado de **Otimização por Colônia de Formigas (Ant Colony Optimization)** para resolver uma instância do clássico **Problema do Caixeiro-Viajante (TSP)**, aplicada a 10 pontos de interesse reais da cidade de Curitiba.

Projeto desenvolvido como atividade avaliativa da disciplina de Computação Natural, do curso de Inteligência Artificial Aplicada da PUC-PR, a partir de uma base teórica sobre algoritmos evolutivos e algoritmos de enxame.

## O problema

Dado um conjunto de locais, qual é a rota de menor distância total que passa por todos eles uma única vez e retorna ao ponto de partida? Esse é o Problema do Caixeiro-Viajante, um problema de otimização combinatória **NP-difícil**: o número de rotas possíveis cresce fatorialmente com o número de locais, tornando a busca exaustiva inviável a partir de poucas dezenas de pontos.

## A solução: inteligência de enxame

Em vez de força bruta, o projeto usa uma meta-heurística inspirada no comportamento de formigas reais: cada "formiga" (agente) constrói uma rota probabilisticamente, depositando feromônio nos caminhos percorridos. Rotas mais curtas acumulam feromônio mais rápido e passam a atrair mais formigas nas iterações seguintes, enquanto a evaporação gradual evita que o algoritmo fique preso em ótimos locais. O resultado é uma convergência coletiva para rotas cada vez mais eficientes, sem que nenhum agente individual "veja" o problema como um todo.

**Principais características da implementação:**
- Classe `AntColonySolver` totalmente vetorizada com NumPy, simulando múltiplas formigas em paralelo por iteração.
- Locais reais de Curitiba (Parque Barigui, Passeio Público, Jockey Plaza, Teatro Paiol, entre outros) plotados sobre um mapa customizado da cidade.
- Experimentação controlada de hiperparâmetros do algoritmo (`distance_power`, `decay_power`, `ant_count`), com análise comparativa dos resultados.

## Resultados

| Execução | Parâmetros ajustados | Distância inicial | Melhor rota encontrada |
|---|---|---|---|
| Baseline | `ant_count=16`, `decay_power=1` | 5309 | 2760 |
| Ajuste 1 | `decay_power=0` | 5309 | 2760 |
| Ajuste 2 | `ant_count=8` | 5309 | 2841 |

O algoritmo reduziu a distância total da rota em **~48%** em relação a uma ordenação arbitrária dos pontos, evidenciando o impacto direto dos parâmetros de feromônio e do tamanho da população de formigas na qualidade e na velocidade de convergência da solução.

## Tecnologias e conceitos aplicados

`Python` · `NumPy` · `Matplotlib` · Algoritmos bioinspirados · Meta-heurísticas de otimização · Computação evolutiva e de enxame · Análise experimental de hiperparâmetros

## Estrutura do projeto

- [Atividade_somativa_2.ipynb](Atividade_somativa_2.ipynb) — notebook com a implementação completa do algoritmo e os experimentos.
- [mapa.PNG](mapa.PNG) — mapa customizado usado como referência espacial dos locais.
- [marcos daniel santana.docx](marcos%20daniel%20santana.docx) — relatório com a análise detalhada dos parâmetros e resultados.

## Créditos

Implementação do `AntColonySolver` adaptada do notebook original de [James McGuigan](https://www.kaggle.com/jamesmcguigan/ant-colony-optimization-algorithm/data) (Kaggle), com adaptações para uso local e aplicação a um novo cenário geográfico.
