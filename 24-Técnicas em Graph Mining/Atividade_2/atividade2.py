"""
Atividade Somativa 2 — Mineração de grafos com dados da série Game of Thrones
Disciplina: Técnicas em Graph Mining (PUCPR)

Compara a rede de interações entre personagens da 1ª temporada (S1)
com a da 8ª temporada (S8).

Tarefa 1 — distribuição de graus, grau médio, densidade e transitividade
Tarefa 2 — 3 personagens mais centrais (grau, intermediação, proximidade, autovetor)
Tarefa 3 — detecção de comunidades (algoritmo de Louvain) e visualização

Execução:
    python atividade2.py
"""

from pathlib import Path

import networkx as nx                 # criação e análise de grafos
import pandas as pd                   # leitura dos arquivos CSV
import numpy as np                    # operações numéricas
import matplotlib.pyplot as plt       # geração das figuras

PASTA = Path(__file__).resolve().parent
SEED = 42                             # semente fixa => resultados reproduzíveis

# ==========================================================================
# CARREGAMENTO DOS DADOS (conforme o código sugerido na orientação)
# ==========================================================================
S1 = pd.read_csv(PASTA / "got-s1-edges_semanas7_8.csv", delimiter=",")
Grafo_Temporada1 = nx.from_pandas_edgelist(S1, source="Source", target="Target",
                                           edge_attr="Weight")

S8 = pd.read_csv(PASTA / "got-s8-edges_semanas7_8 .csv", delimiter=",")
Grafo_Temporada8 = nx.from_pandas_edgelist(S8, source="Source", target="Target",
                                           edge_attr="Weight")

redes = {"Temporada 1": Grafo_Temporada1, "Temporada 8": Grafo_Temporada8}


# ==========================================================================
# TAREFA 1 — Distribuição de graus, grau médio, densidade e transitividade
# ==========================================================================
print("=" * 78)
print("TAREFA 1 — Comparação estrutural das redes")
print("=" * 78)

metricas = {}
for nome, G in redes.items():
    graus = [g for _, g in G.degree()]                       # grau de cada vértice
    metricas[nome] = {
        "vertices": G.number_of_nodes(),
        "arestas": G.number_of_edges(),
        "grau_medio": sum(graus) / G.number_of_nodes(),       # grau médio da rede
        "densidade": nx.density(G),                           # arestas existentes / máximas
        "transitividade": nx.transitivity(G),                 # coef. de agrupamento global
        "coef_medio": nx.average_clustering(G),               # coef. de agrupamento médio
        "grau_min": min(graus),
        "grau_max": max(graus),
        "componentes": nx.number_connected_components(G),     # nº de componentes conexas
        "graus": graus,
    }

print(f"{'Métrica':<34}{'Temporada 1':>16}{'Temporada 8':>16}")
print("-" * 78)
for chave, rotulo in [("vertices", "Vértices (personagens)"),
                      ("arestas", "Arestas (interações)"),
                      ("grau_medio", "Grau médio"),
                      ("densidade", "Densidade"),
                      ("transitividade", "Transitividade (coef. global)"),
                      ("coef_medio", "Coef. de agrupamento médio"),
                      ("grau_min", "Grau mínimo"),
                      ("grau_max", "Grau máximo"),
                      ("componentes", "Componentes conexas")]:
    v1, v8 = metricas["Temporada 1"][chave], metricas["Temporada 8"][chave]
    if isinstance(v1, float):
        print(f"{rotulo:<34}{v1:>16.4f}{v8:>16.4f}")
    else:
        print(f"{rotulo:<34}{v1:>16}{v8:>16}")

# vértice de maior grau e estrutura de componentes em cada rede
for nome, G in redes.items():
    topo = max(G.degree(), key=lambda x: x[1])
    print(f"Personagem de maior grau na {nome}: {topo[0]} (grau {topo[1]})")
    comps = sorted(nx.connected_components(G), key=len, reverse=True)
    if len(comps) > 1:
        print(f"  {nome} é DESCONEXA — tamanhos das componentes: {[len(c) for c in comps]}")
        for c in comps[1:]:
            print(f"  Fora da componente principal: {sorted(c)}")

# --- histogramas da distribuição de graus (lado a lado) ---
fig, eixos = plt.subplots(1, 2, figsize=(14, 5))
for eixo, (nome, G) in zip(eixos, redes.items()):
    graus = metricas[nome]["graus"]
    valores, frequencias = np.unique(graus, return_counts=True)
    eixo.bar(valores, frequencias, color="blue")
    eixo.set_title(f"Distribuição de graus — {nome}")
    eixo.set_xlabel("Grau")
    eixo.set_ylabel("Frequência (nº de personagens)")
plt.tight_layout()
plt.savefig(PASTA / "fig1_distribuicao_graus.png", dpi=150, bbox_inches="tight")
plt.show()

print("\nDistribuição de graus (grau: nº de personagens):")
for nome in redes:
    valores, frequencias = np.unique(metricas[nome]["graus"], return_counts=True)
    print(f"  {nome}:", dict(zip(valores.tolist(), frequencias.tolist())))


# ==========================================================================
# TAREFA 2 — Os 3 personagens mais centrais segundo 4 medidas de centralidade
# ==========================================================================
print("\n" + "=" * 78)
print("TAREFA 2 — Personagens mais centrais (top 3 por medida)")
print("=" * 78)

def top3(dicionario):
    """Retorna os 3 vértices com maior valor em um dicionário de centralidades."""
    return sorted(dicionario.items(), key=lambda x: x[1], reverse=True)[:3]

# NOTA METODOLÓGICA: a centralidade de autovetor e a de proximidade não são
# bem definidas em grafos desconexos (limitação discutida na Unidade 5). Como a
# rede da Temporada 8 possui 2 componentes, as centralidades são calculadas
# sobre a MAIOR COMPONENTE CONEXA de cada rede, garantindo comparabilidade.
centralidades = {}
for nome, G in redes.items():
    maior_componente = max(nx.connected_components(G), key=len)
    Gc = G.subgraph(maior_componente).copy()
    if Gc.number_of_nodes() < G.number_of_nodes():
        print(f"\n[{nome}] centralidades calculadas na maior componente: "
              f"{Gc.number_of_nodes()} de {G.number_of_nodes()} personagens "
              f"(excluídos: {sorted(set(G) - maior_componente)})")
    centralidades[nome] = {
        "Grau": nx.degree_centrality(Gc),
        "Intermediação": nx.betweenness_centrality(Gc),
        "Proximidade": nx.closeness_centrality(Gc),
        "Autovetor": nx.eigenvector_centrality_numpy(Gc),
    }

for nome in redes:
    print(f"\n--- {nome} ---")
    for medida, valores in centralidades[nome].items():
        formatado = ", ".join(f"{p} ({v:.4f})" for p, v in top3(valores))
        print(f"  {medida:<16}: {formatado}")

# personagens que aparecem no top 3 de alguma medida, em cada temporada
top_s1 = {p for medida in centralidades["Temporada 1"].values()
          for p, _ in top3(medida)}
top_s8 = {p for medida in centralidades["Temporada 8"].values()
          for p, _ in top3(medida)}

print("\nPersonagens no top 3 de alguma medida:")
print("  Temporada 1:", sorted(top_s1))
print("  Temporada 8:", sorted(top_s8))
print("  >>> Centrais em AMBAS as temporadas:", sorted(top_s1 & top_s8))


# ==========================================================================
# TAREFA 3 — Detecção de comunidades (algoritmo de Louvain) e visualização
# ==========================================================================
print("\n" + "=" * 78)
print("TAREFA 3 — Detecção de comunidades com o algoritmo de Louvain")
print("=" * 78)

comunidades = {}
for nome, G in redes.items():
    # Louvain: método aglomerativo baseado na maximização da modularidade
    coms = nx.community.louvain_communities(G, seed=SEED)
    comunidades[nome] = coms
    modularidade = nx.community.modularity(G, coms)
    print(f"\n--- {nome} ---")
    print(f"  Comunidades encontradas: {len(coms)}")
    print(f"  Modularidade: {modularidade:.4f}")
    for i, c in enumerate(sorted(coms, key=len, reverse=True), start=1):
        membros = sorted(c)
        print(f"  Comunidade {i} ({len(membros)} personagens): {', '.join(membros)}")

# --- figuras: grafos coloridos por comunidade, com nomes dos vértices ---
for nome, G in redes.items():
    coms = sorted(comunidades[nome], key=len, reverse=True)
    # mapeia cada vértice ao índice da sua comunidade (define a cor)
    cor_do_vertice = {v: i for i, c in enumerate(coms) for v in c}
    cores = [cor_do_vertice[v] for v in G.nodes()]
    # tamanho do vértice proporcional ao grau (destaca personagens centrais)
    tamanhos = [80 + 40 * G.degree(v) for v in G.nodes()]

    plt.figure(figsize=(20, 14))
    # k maior e mais iterações => vértices mais espalhados e rótulos legíveis
    pos = nx.spring_layout(G, seed=SEED, k=0.9, iterations=200)
    nx.draw_networkx_edges(G, pos, edge_color="lightgray", width=0.5)
    nx.draw_networkx_nodes(G, pos, node_color=cores, cmap=plt.cm.tab10,
                           node_size=tamanhos, alpha=0.9)
    nx.draw_networkx_labels(G, pos, font_size=7)
    plt.title(f"{nome} — {len(coms)} comunidades detectadas pelo algoritmo de Louvain",
              fontsize=15)
    plt.axis("off")
    arquivo = f"fig{2 if nome == 'Temporada 1' else 3}_comunidades_{nome.replace(' ', '').lower()}.png"
    plt.savefig(PASTA / arquivo, dpi=150, bbox_inches="tight")
    plt.show()
    print(f"Figura salva: {arquivo}")

# --- comparação objetiva entre as comunidades das duas temporadas ---
# índice de Jaccard entre cada par de comunidades (S1 x S8) para embasar a análise visual
print("\n" + "-" * 78)
print("Similaridade entre comunidades das duas temporadas (índice de Jaccard)")
print("-" * 78)
coms1 = sorted(comunidades["Temporada 1"], key=len, reverse=True)
coms8 = sorted(comunidades["Temporada 8"], key=len, reverse=True)

pares = []
for i, c1 in enumerate(coms1, start=1):
    for j, c8 in enumerate(coms8, start=1):
        inter = c1 & c8
        uniao = c1 | c8
        jaccard = len(inter) / len(uniao) if uniao else 0
        if inter:
            pares.append((jaccard, i, j, len(inter), sorted(inter)))

pares.sort(reverse=True)
print(f"{'Jaccard':>9}  {'S1':>3} {'S8':>3}  {'|∩|':>4}  personagens em comum")
for jac, i, j, n, membros in pares[:6]:
    nomes = ", ".join(membros[:12]) + ("..." if len(membros) > 12 else "")
    print(f"{jac:>9.3f}  C{i:<2} C{j:<2}  {n:>4}  {nomes}")

# O Jaccard acima é penalizado pela renovação do elenco (personagens que morreram
# ou surgiram). Por isso, a comparação é refeita considerando SOMENTE os
# personagens presentes nas duas temporadas.
comuns = set(Grafo_Temporada1) & set(Grafo_Temporada8)
print("\n" + "-" * 78)
print(f"Comparação restrita aos {len(comuns)} personagens presentes nas DUAS temporadas")
print("-" * 78)
print("Personagens em comum:", ", ".join(sorted(comuns)))

pares_restritos = []
for i, c1 in enumerate(coms1, start=1):
    for j, c8 in enumerate(coms8, start=1):
        a, b = c1 & comuns, c8 & comuns          # restringe ao elenco comum
        inter, uniao = a & b, a | b
        if len(inter) >= 2:                      # ignora coincidências triviais
            pares_restritos.append((len(inter) / len(uniao), i, j, sorted(inter)))

pares_restritos.sort(reverse=True)
print(f"\n{'Jaccard':>9}  {'S1':>3} {'S8':>3}  personagens que permaneceram juntos")
for jac, i, j, membros in pares_restritos[:8]:
    print(f"{jac:>9.3f}  C{i:<2} C{j:<2}  {', '.join(membros)}")
