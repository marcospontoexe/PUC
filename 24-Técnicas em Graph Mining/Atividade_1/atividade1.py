"""
Atividade Somativa 1 — Extração de Características em Grafos
Disciplina: Técnicas em Graph Mining (PUCPR)

Base de dados: Grafo3_semana4.csv (matriz de adjacências 512 x 512)

Execução:
    python atividade1.py
As figuras são exibidas na tela (plt.show) e também salvas em PNG na pasta do script.
"""

from pathlib import Path

import networkx as nx                 # criação e análise de grafos
import pandas as pd                   # leitura do arquivo CSV
import numpy as np                    # operações com a matriz de adjacências
import matplotlib.pyplot as plt       # geração das figuras

# diretório do próprio script: permite executar de qualquer pasta
PASTA = Path(__file__).resolve().parent
ARQUIVO_CSV = PASTA / "Grafo3_semana4.csv"


# ==========================================================================
# TAREFA 1 — Criar o grafo G e verificar se é direcionado
# ==========================================================================
print("=" * 70)
print("TAREFA 1 — Criação do grafo e verificação de direcionamento")
print("=" * 70)

# lê a matriz de adjacências; header=None pois o arquivo não possui cabeçalho
matriz = pd.read_csv(ARQUIVO_CSV, header=None)

# --- verificações de sanidade da matriz (justificam as escolhas metodológicas) ---
A = matriz.values
print("Dimensão da matriz:", A.shape)                       # deve ser quadrada (N x N)
print("Valores presentes na matriz:", np.unique(A))         # 0/1 => grafo não valorado
print("Soma da diagonal principal:", A.trace(), "(0 = sem laços)")

# matriz simétrica (A = A^T) indica que cada conexão está nas duas direções,
# ou seja, a matriz representa um grafo NÃO direcionado
simetrica = np.array_equal(A, A.T)
print("A matriz de adjacências é simétrica?", simetrica)

# cria o grafo a partir da matriz de adjacências, usando a classe adequada:
# matriz simétrica -> nx.Graph (não direcionado) | assimétrica -> nx.DiGraph (direcionado)
G = nx.from_pandas_adjacency(matriz, create_using=nx.Graph if simetrica else nx.DiGraph)

# resposta da tarefa: True ou False
print("\n>>> O grafo G é direcionado?", G.is_directed())


# ==========================================================================
# TAREFA 2 — Desenhar o grafo G com dimensões 12 x 7
# ==========================================================================
print("\n" + "=" * 70)
print("TAREFA 2 — Desenho do grafo G (12 x 7)")
print("=" * 70)

plt.figure(figsize=(12, 7))                       # define o tamanho da figura como 12 x 7
posicoes = nx.spring_layout(G, seed=42)           # seed fixa => desenho reproduzível
nx.draw(G, pos=posicoes, node_size=50, node_color="orange",
        edge_color="gray", width=0.5)
plt.title("Grafo G (512 vértices, 512 arestas)")
plt.savefig(PASTA / "figura_grafo_12x7.png", dpi=150, bbox_inches="tight")
plt.show()
print("Figura exibida na tela e salva em: figura_grafo_12x7.png")


# ==========================================================================
# TAREFA 3 — Quantidade de vértices e de arestas
# ==========================================================================
print("\n" + "=" * 70)
print("TAREFA 3 — Quantidade de vértices e arestas")
print("=" * 70)

print(">>> Quantidade de vértices (ordem):", G.number_of_nodes())
print(">>> Quantidade de arestas (tamanho):", G.number_of_edges())


# ==========================================================================
# TAREFA 4 — Grau do vértice 33 e diferença em relação ao grau médio
# ==========================================================================
print("\n" + "=" * 70)
print("TAREFA 4 — Grau do vértice 33 vs. grau médio da rede")
print("=" * 70)

VERTICE = 33                                              # vértice de interesse

grau_vertice = G.degree(VERTICE)                          # grau do vértice 33
graus = [grau for _, grau in G.degree()]                  # grau de todos os vértices
grau_medio = sum(graus) / G.number_of_nodes()             # grau médio da rede
diferenca = grau_vertice - grau_medio                     # diferença em relação à média

print(f">>> Grau do vértice {VERTICE}:", grau_vertice)
print(">>> Grau médio da rede:", round(grau_medio, 4))
print(f">>> Diferença (grau do vértice {VERTICE} - grau médio):", round(diferenca, 4))

# conferência pela fórmula do grau médio: 2*|E| / |V| (grafo não direcionado)
print("Conferência do grau médio por 2*|E|/|V|:",
      round(2 * G.number_of_edges() / G.number_of_nodes(), 4))


# ==========================================================================
# TAREFA 5 — Arestas conectadas ao vértice 33 (apresentadas em uma lista)
# ==========================================================================
print("\n" + "=" * 70)
print("TAREFA 5 — Arestas conectadas ao vértice 33")
print("=" * 70)

arestas_vertice = list(G.edges(VERTICE))                  # arestas incidentes ao vértice 33
vizinhos = sorted(G.neighbors(VERTICE))                   # vértices vizinhos

print(f">>> Arestas conectadas ao vértice {VERTICE}:", arestas_vertice)
print(">>> Vértices vizinhos:", vizinhos)
print(">>> Total de arestas incidentes:", len(arestas_vertice),
      "(confere com o grau obtido na Tarefa 4)")

# figura complementar: destaca o vértice 33 e seus vizinhos dentro da rede
cores = ["red" if n == VERTICE else "gold" if n in vizinhos else "lightgray"
         for n in G.nodes()]
tamanhos = [220 if n == VERTICE else 120 if n in vizinhos else 30 for n in G.nodes()]
plt.figure(figsize=(12, 7))
nx.draw(G, pos=posicoes, node_size=tamanhos, node_color=cores,
        edge_color="lightgray", width=0.5)
nx.draw_networkx_labels(G, pos=posicoes,
                        labels={n: str(n) for n in [VERTICE] + vizinhos},
                        font_size=9, font_weight="bold")
plt.title(f"Vértice {VERTICE} (vermelho) e seus vizinhos {vizinhos} (amarelo)")
plt.savefig(PASTA / "figura_vertice33_destaque.png", dpi=150, bbox_inches="tight")
plt.show()


# ==========================================================================
# TAREFA 6 — Distribuição de graus em uma figura com dimensões 10 x 5
# ==========================================================================
print("\n" + "=" * 70)
print("TAREFA 6 — Distribuição de graus (10 x 5)")
print("=" * 70)

# conta quantos vértices existem para cada valor de grau
valores, frequencias = np.unique(graus, return_counts=True)

plt.figure(figsize=(10, 5))                               # tamanho da figura: 10 x 5
plt.bar(valores, frequencias, color="blue")
plt.title("Distribuição de graus do grafo G")
plt.xlabel("Grau")
plt.ylabel("Frequência")
plt.xticks(valores)
# rotula cada barra com a quantidade exata de vértices
for v, f in zip(valores, frequencias):
    plt.text(v, f + 3, str(f), ha="center", fontsize=9)
plt.savefig(PASTA / "figura_distribuicao_graus_10x5.png", dpi=150, bbox_inches="tight")
plt.show()

print("Distribuição de graus (grau: quantidade de vértices):")
for v, f in zip(valores, frequencias):
    print(f"  grau {v}: {f} vértice(s)  ({100 * f / G.number_of_nodes():.1f}%)")


# ==========================================================================
# CARACTERIZAÇÃO ESTRUTURAL COMPLEMENTAR (embasa a análise da distribuição)
# ==========================================================================
print("\n" + "=" * 70)
print("CARACTERIZAÇÃO ESTRUTURAL COMPLEMENTAR")
print("=" * 70)

componentes = list(nx.connected_components(G))
# número ciclomático = |E| - |V| + nº de componentes => quantidade de ciclos independentes
ciclos_independentes = G.number_of_edges() - G.number_of_nodes() + len(componentes)

print("Grau mínimo / máximo:", min(graus), "/", max(graus))
print("Vértices isolados (grau 0):", sum(1 for g in graus if g == 0))
print("Vértice de maior grau:", max(G.degree(), key=lambda x: x[1]))
print("Densidade da rede:", round(nx.density(G), 6))
print("Coeficiente de agrupamento médio:", round(nx.average_clustering(G), 6))
print("Componentes conexas:", len(componentes), "| O grafo é conexo?", nx.is_connected(G))
print("É árvore?", nx.is_tree(G))
print("Ciclos independentes (número ciclomático):", ciclos_independentes)
