"""
Atividade Somativa 1 — Extração de Características em Grafos
Disciplina: Técnicas em Graph Mining (PUCPR)

Base de dados: Grafo3_semana4.csv (matriz de adjacências)
"""

import networkx as nx                 # biblioteca para criação e análise de grafos
import pandas as pd                   # leitura do arquivo CSV
import numpy as np                    # operações com a matriz de adjacências
import matplotlib
matplotlib.use("Agg")                 # backend para salvar as figuras em arquivo
import matplotlib.pyplot as plt       # geração das figuras

# ==========================================================================
# TAREFA 1 — Criar o grafo G e verificar se é direcionado
# ==========================================================================

# lê a matriz de adjacências; header=None pois o arquivo não possui cabeçalho
matriz = pd.read_csv("Grafo3_semana4.csv", header=None)

# verifica se a matriz é simétrica (matriz simétrica => grafo NÃO direcionado)
simetrica = np.array_equal(matriz.values, matriz.values.T)
print("A matriz de adjacências é simétrica?", simetrica)

# cria o grafo a partir da matriz de adjacências
# matriz simétrica -> nx.Graph (não direcionado) | assimétrica -> nx.DiGraph (direcionado)
G = nx.from_pandas_adjacency(matriz, create_using=nx.Graph if simetrica else nx.DiGraph)

# verifica se o grafo criado é direcionado (resposta em True ou False)
print("O grafo G é direcionado?", G.is_directed())

# ==========================================================================
# TAREFA 2 — Desenhar o grafo G com dimensões 12 x 7
# ==========================================================================

plt.figure(figsize=(12, 7))                  # define o tamanho da figura como 12 x 7
nx.draw(G, node_size=50, node_color="orange", edge_color="gray", width=0.5)
plt.savefig("figura_grafo_12x7.png", dpi=150, bbox_inches="tight")
plt.close()

# ==========================================================================
# TAREFA 3 — Quantidade de vértices e de arestas
# ==========================================================================

print("Quantidade de vértices (ordem):", G.number_of_nodes())
print("Quantidade de arestas (tamanho):", G.number_of_edges())

# ==========================================================================
# TAREFA 4 — Grau do vértice 33 e diferença em relação ao grau médio
# ==========================================================================

grau_33 = G.degree(33)                                   # grau do vértice 33
graus = [grau for _, grau in G.degree()]                 # lista com o grau de todos os vértices
grau_medio = sum(graus) / G.number_of_nodes()            # grau médio da rede
diferenca = grau_33 - grau_medio                         # diferença entre o grau do vértice e a média

print("Grau do vértice 33:", grau_33)
print("Grau médio da rede:", round(grau_medio, 4))
print("Diferença (grau do vértice 33 - grau médio):", round(diferenca, 4))

# ==========================================================================
# TAREFA 5 — Arestas conectadas ao vértice 33 (apresentadas em uma lista)
# ==========================================================================

arestas_33 = list(G.edges(33))     # conjunto de arestas incidentes ao vértice 33
print("Arestas conectadas ao vértice 33:", arestas_33)
print("Total de arestas conectadas ao vértice 33:", len(arestas_33))

# ==========================================================================
# TAREFA 6 — Distribuição de graus em uma figura com dimensões 10 x 5
# ==========================================================================

plt.figure(figsize=(10, 5))                              # define o tamanho da figura como 10 x 5
valores, frequencias = np.unique(graus, return_counts=True)   # conta quantos vértices há em cada grau
plt.bar(valores, frequencias, color="blue")
plt.title("Distribuição de graus do grafo G")
plt.xlabel("Grau")
plt.ylabel("Frequência")
plt.xticks(valores)
plt.savefig("figura_distribuicao_graus_10x5.png", dpi=150, bbox_inches="tight")
plt.close()

# tabela auxiliar da distribuição de graus (grau -> quantidade de vértices)
print("\nDistribuição de graus (grau: quantidade de vértices):")
for v, f in zip(valores, frequencias):
    print(f"  grau {v}: {f} vértice(s)")
