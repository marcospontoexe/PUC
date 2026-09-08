# Resumos — Técnica em Graph Mining (PUCPR)

> Documento único consolidando o resumo detalhado de cada unidade da disciplina, para fins de estudo.
> Fontes: PDFs na raiz do projeto ([1-Introdução à Teoria dos Grafos.pdf](../1-Introdução%20à%20Teoria%20dos%20Grafos.pdf), [2-Explorando grafos com programação.pdf](../2-Explorando%20grafos%20com%20programação.pdf), [3-Conhecendo os diferentes modelos de redes complexa.pdf](../3-Conhecendo%20os%20diferentes%20modelos%20de%20redes%20complexa.pdf), [4-Extraindo informações de redes complexas – Parte I.pdf](../4-Extraindo%20informações%20de%20redes%20complexas%20–%20Parte%20I.pdf), [5-Extraindo informações de redes complexas - Parte II.pdf](../5-Extraindo%20informações%20de%20redes%20complexas%20-%20Parte%20II.pdf), [6-Detectando grupos e comunidades em redes complexas.pdf](../6-Detectando%20grupos%20e%20comunidades%20em%20redes%20complexas.pdf), [7-Prevendo novas conexões na rede.pdf](../7-Prevendo%20novas%20conexões%20na%20rede.pdf), [8-Melhorando os aspectos visuais das redes complexas.pdf](../8-Melhorando%20os%20aspectos%20visuais%20das%20redes%20complexas.pdf)).

## Sumário

1. [Unidade 1 — Introdução à Teoria dos Grafos](#unidade-1--introdução-à-teoria-dos-grafos)
2. [Unidade 2 — Explorando Grafos com Programação](#unidade-2--explorando-grafos-com-programação)
3. [Unidade 3 — Modelos de Redes Complexas](#unidade-3--modelos-de-redes-complexas)
4. [Unidade 4 — Extraindo Informações de Redes Complexas (Parte I)](#unidade-4--extraindo-informações-de-redes-complexas-parte-i)
5. [Unidade 5 — Extraindo Informações de Redes Complexas (Parte II)](#unidade-5--extraindo-informações-de-redes-complexas-parte-ii)
6. [Unidade 6 — Detectando Grupos e Comunidades em Redes Complexas](#unidade-6--detectando-grupos-e-comunidades-em-redes-complexas)
7. [Unidade 7 — Prevendo Novas Conexões na Rede](#unidade-7--prevendo-novas-conexões-na-rede)
8. [Unidade 8 — Melhorando os Aspectos Visuais das Redes Complexas](#unidade-8--melhorando-os-aspectos-visuais-das-redes-complexas)

---

## Unidade 1 — Introdução à Teoria dos Grafos

### 1.1 Contextualização

Primeira unidade da disciplina **Graph Mining**. Constrói a base conceitual para representar problemas do cotidiano (redes sociais, transporte, internet, redes de computadores) usando grafos, e introduz a visão geral das tarefas de mineração exploradas ao longo da disciplina.

### 1.2 Conceitos básicos e terminologia

**Definição formal:** um grafo é uma estrutura matemática **G = (V, E)**, onde:
- **V** = conjunto de **vértices** (ou nós) — representam os objetos do problema;
- **E** = conjunto de **arestas** (*edges*) — representam as relações entre pares de objetos.

Pontos importantes:
- Uma aresta conecta no máximo dois vértices; se houver mais de uma aresta ligando o mesmo par, são chamadas de **arestas paralelas**.
- Quando uma aresta liga um vértice a ele mesmo, chama-se **laço** (*loop*).
- Vértices são representados por círculos/quadrados e arestas por linhas ou setas nos diagramas.

### 1.3 Tipos de grafos (classificação pela direção das arestas)

| Tipo | Arestas | Laços? | Arestas paralelas? |
|---|---|---|---|
| Grafo simples | Não dirigidas | Não | Não |
| Grafo completo | Não dirigidas | Não | Não |
| Digrafo (dirigido) | Dirigidas | Não | Não |
| Grafo não dirigido | Não dirigidas | Não | Não |
| Grafo misto | Dirigidas e não dirigidas | Não | Não |
| Multigrafo | Não dirigidas | Não | Sim |
| Multigrafo dirigido | Dirigidas | Não | Sim |
| Pseudografo | Não dirigidas | Sim | Sim |

Outras classificações importantes:
- **Grafo orientado/dirigido (digrafo):** usa setas — a direção importa.
- **Grafo completo:** existe aresta entre **todos** os pares possíveis de vértices.
- **Grafo conexo:** existe pelo menos um caminho entre cada par de vértices. Caso contrário, é **desconexo**.
- **Árvore:** grafo conexo **sem ciclos**.
- **Ciclo:** caminho que visita ao menos três vértices e pode retornar ao vértice inicial.

### 1.4 Ordem e Tamanho

- **Ordem** de um grafo = cardinalidade de V (quantidade de vértices), |V|.
- **Tamanho** de um grafo = cardinalidade de E (quantidade de arestas), |E|.

### 1.5 Grafos vs. Redes Complexas

Redes complexas são um tipo específico de grafo que apresenta propriedades particulares (não encontradas em grafos simples), como:
- Vértices fortemente conectados formando **comunidades**;
- Distribuição de graus seguindo uma **lei de potência**.

Ou seja: toda rede complexa é um grafo, mas nem todo grafo é uma rede complexa.

### 1.6 Grau de um vértice

O **grau** (*degree*) representa quantas conexões um vértice possui.

- Em **grafos dirigidos**, distingue-se:
  - **Grau de entrada** (*indegree*): número de arestas que chegam ao vértice;
  - **Grau de saída** (*outdegree*): número de arestas que partem do vértice.

### 1.7 Distribuição de graus

Representa quantos vértices possuem cada grau específico — geralmente visualizada por **histogramas**.

- Em dados/fenômenos aleatórios "comuns" (altura, notas), a distribuição costuma seguir uma **curva Gaussiana (normal)**, com formato de sino simétrico em torno de uma média.
- Em **redes complexas reais**, a distribuição de graus segue tipicamente uma **lei de potência** (cauda longa): a maioria dos vértices tem poucas conexões, e uma minoria concentra um número enorme de conexões (ex.: a maioria dos usuários do Twitter tem poucos seguidores, enquanto celebridades têm milhões).

### 1.8 Pesos das arestas

Quando as arestas possuem um custo ou importância associada, o grafo é chamado **valorado** ou **ponderado**, representado como **G = (V, E, W)**. Exemplo clássico: distâncias entre cidades.

### 1.9 Grafos estáticos vs. dinâmicos

- **Estáticos:** agregam todos os eventos ocorridos em um período em um único grafo (mais simples, mais usado).
- **Dinâmicos:** representam o estado atual e evoluem em tempo real (mais preciso, mas computacionalmente mais custoso).

### 1.10 Origens da Teoria dos Grafos

A Teoria dos Grafos nasceu em **1736**, quando o matemático **Leonhard Euler** resolveu o problema das **Sete Pontes de Königsberg**: seria possível atravessar as sete pontes da cidade sem repetir nenhuma e retornar ao ponto de partida?

- Euler representou o problema como um **multigrafo** (4 regiões = vértices, 7 pontes = arestas) e provou matematicamente que era **impossível**.
- Surgiu daí o conceito de **grafo euleriano**: um grafo que possui um **ciclo euleriano** (caminho que percorre cada aresta exatamente uma vez, retornando ao vértice inicial).
  - Grafo **não dirigido** é euleriano ⟺ todos os vértices têm **grau par**.
  - Grafo **dirigido** é euleriano ⟺ grau de entrada = grau de saída em todos os vértices.

### 1.11 Aplicações de grafos e redes complexas (4 categorias)

1. **Redes tecnológicas:** redes de computadores, telefonia, distribuição de energia, transporte (rotas aéreas, rodovias).
2. **Redes de informação:** páginas web (vértices = *webpages*, arestas = *links*) e redes de citações acadêmicas.
3. **Redes biológicas:** conexões cerebrais, interações entre proteínas, redes de expressão gênica.
4. **Redes sociais:** relações entre pessoas (amizade, parentesco, colaboração profissional) — estudadas desde 1930 na Sociologia, muito antes das redes sociais digitais.

### 1.12 Visão geral das tarefas de Graph Mining

*Graph mining* é o uso de técnicas de IA para extrair conhecimento de dados representados em grafos, dividido em duas categorias:
- **Tarefas preditivas:** predizer valores desconhecidos ou futuros.
- **Tarefas descritivas:** explicar o comportamento dos dados.

As três tarefas centrais da disciplina:
1. **Análise de centralidade:** identificar os vértices mais importantes da rede (grau, proximidade, intermediação).
2. **Detecção de comunidades:** encontrar grupos de vértices mais conectados entre si do que com o resto da rede.
3. **Predição de conexões:** estimar a probabilidade de existir uma aresta futura entre dois vértices ainda não conectados.

**Dica de estudo:** essa unidade é a base de toda a disciplina — os conceitos de grau, ordem/tamanho e tipos de grafo reaparecem constantemente nas unidades seguintes.

---

## Unidade 2 — Explorando Grafos com Programação

### 2.1 Contextualização

Esta unidade tem dois grandes blocos: **(1)** as estruturas de dados usadas para representar grafos computacionalmente e **(2)** a introdução prática à biblioteca **NetworkX** para manipular grafos em Python. É a ponte entre a teoria (unidade 1) e a implementação prática usada no resto da disciplina.

### 2.2 Grafos densos vs. esparsos

Antes de escolher uma estrutura de dados, é preciso saber a densidade do grafo:
- **Grafo denso:** número de arestas próximo do máximo possível.
  - Máximo em grafo dirigido: **N·(N−1)**
  - Máximo em grafo não dirigido: **N·(N−1)/2**
- **Grafo esparso:** poucas arestas em relação ao número de vértices.

Os critérios para escolher a estrutura ideal são: **custo de memória (espaço)** e **custo de tempo** para operações básicas (verificar se uma aresta existe, encontrar vizinhos de um vértice).

### 2.3 As quatro estruturas de dados para representar grafos

#### 2.3.1 Lista de vértices e lista de arestas
A forma mais simples: duas listas Python, uma com os vértices (`V`) e outra com as arestas como tuplas (`E`). Para grafos ponderados, adiciona-se um terceiro elemento na tupla (o peso).
```python
V = [1, 2, 3, 4, 5]
E = [(1,2,0.3), (2,4,0.8), (3,1,1), ...]  # terceiro valor = peso
```
- **Complexidade de espaço:** O(|V| + |E|)
- **Desvantagem:** para achar vizinhos ou verificar conexão entre vértices, precisa de **busca sequencial** por toda a lista de arestas → custo **O(|E|)**, caro em grafos grandes.

#### 2.3.2 Lista de adjacência
Para cada vértice, mantém-se uma lista dos vértices vizinhos (em Python, um **dicionário de listas**).
```python
listaAdjacenciaGrafo = {1: [2], 2: [1,3,5], 3: [2,4,5], 4: [3,5], 5: [2,3,4]}
```
- **Complexidade de espaço:** O(|V| + |E|) — mas em grafos não dirigidos cada aresta é armazenada duas vezes (uma para cada direção).
- **Vantagem:** encontrar vizinhos de um vértice é **O(1)** (acesso direto ao índice).
- Verificar se dois vértices estão conectados: **O(|V|)** (precisa percorrer a lista encadeada do vértice).

#### 2.3.3 Matriz de adjacência
Matriz quadrada |V|×|V|, onde a posição (i,j) recebe 1 se existe aresta entre i e j (ou o peso, se ponderado), e 0 caso contrário.
- Grafo **não dirigido** → matriz **simétrica**.
- **Complexidade de espaço:** O(|V|²) — quadrática, independente de o grafo ser denso ou esparso (desperdiça memória em grafos esparsos).
- Encontrar vizinhos de um vértice: O(|V|) (percorrer a linha).
- Verificar conexão entre dois vértices: **O(1)** (acesso direto à posição).

#### 2.3.4 Matriz de incidência
Matriz de dimensão |V|×|E|, relacionando vértices com arestas (não vértices com vértices).
- Em **grafos dirigidos**: 1 = aresta parte do vértice; -1 = aresta chega ao vértice; 0 = não incide.
- Em **grafos não dirigidos**: 1 = a aresta incide no vértice; 0 = caso contrário.
- **Complexidade de espaço:** O(|V|·|E|) — a mais custosa em espaço.
- Encontrar vizinhos: O(|V|·|E|). Verificar conexão: O(|E|).

#### 2.3.5 Tabela-resumo de complexidades

| Estrutura | Espaço | Vizinhos de um vértice | Verificar conexão |
|---|---|---|---|
| Lista de vértices/arestas | O(\|V\|+\|E\|) | O(\|E\|) | O(\|E\|) |
| Lista de adjacência | O(\|V\|+\|E\|) | O(1) | O(\|V\|) |
| Matriz de adjacência | O(\|V\|²) | O(\|V\|) | O(1) |
| Matriz de incidência | O(\|V\|·\|E\|) | O(\|V\|·\|E\|) | O(\|E\|) |

**Conclusão prática:** matriz de adjacência é ótima para grafos densos e quando se precisa verificar conexões com frequência; lista de adjacência é melhor para grafos esparsos e busca de vizinhos.

### 2.4 A biblioteca NetworkX

**NetworkX** é uma biblioteca Python para criação, manipulação e estudo de grafos/redes complexas, capaz de processar redes com mais de 10 milhões de vértices e 100 milhões de arestas.

#### 2.4.1 Instalação
```bash
$ conda install networkx
$ conda install pip
$ pip install numpy scipy pandas matplotlib
```

#### 2.4.2 Criando um grafo básico
```python
import networkx as nx
G = nx.Graph()                        # cria um grafo vazio não dirigido

# adicionando vértices (nodes)
G.add_node(1)                         # adiciona um único vértice
G.add_nodes_from([3, 4, 5])           # adiciona uma lista de vértices

# adicionando arestas (edges)
G.add_edge(1, 2)                              # adiciona uma única aresta
G.add_edges_from([(2,3), (2,5), (4,2)])       # adiciona várias arestas de uma vez

# desenhando o grafo
nx.draw(G)                                                        # desenho simples, sem rótulos
nx.draw_networkx(G, with_labels=True, node_color='orange', node_size=2000)  # com personalização
```

#### 2.4.3 Classes de grafos disponíveis
| Classe | Uso |
|---|---|
| `Graph()` | Grafo não dirigido (ignora arestas duplicadas/paralelas) |
| `DiGraph()` | Grafo dirigido |
| `MultiGraph()` | Grafo não dirigido permitindo arestas múltiplas |
| `MultiDiGraph()` | Grafo dirigido permitindo arestas múltiplas |

Importante: vértices podem ser de qualquer tipo — inteiros, strings, caracteres.

#### 2.4.4 Removendo vértices e arestas
```python
G2.remove_nodes_from(['Antonio', 'Matheus'])  # remove uma lista de vértices (e arestas associadas)
G2.remove_node(1)                             # remove um único vértice
G2.remove_edge('A', 'C')                      # remove a aresta entre A e C
G2.remove_edges_from([('A','C'), ('B','D')])  # remove uma lista de arestas
```
⚠️ Ao remover um vértice, todas as arestas ligadas a ele também são removidas automaticamente.

#### 2.4.5 Consultando informações do grafo
```python
G2.order()                    # quantidade de vértices
G2.size()                     # quantidade de arestas
G2.degree()                   # grau de todos os vértices
G2.degree('D')                # grau de um vértice específico
G2.adj                        # retorna a lista de adjacência
nx.to_numpy_matrix(G2)        # converte o grafo para matriz de adjacência

list(G2.nodes)                # lista de vértices
list(G2.edges)                # lista de arestas

G2.has_node('A')              # verifica se o vértice existe
G2.has_edge('B', 'C')         # verifica se a aresta existe
G2.is_directed()              # verifica se o grafo é dirigido
G2.is_multigraph()            # verifica se é multigrafo
list(G2.neighbors('A'))       # lista os vizinhos de um vértice
```

#### 2.4.6 Salvando e lendo grafos em disco
```python
nx.write_edgelist(G2, 'G2_lista_arestas.txt')      # salva usando lista de arestas
nx.write_adjlist(G2, 'G2_lista_adjacencia.txt')    # salva usando lista de adjacência

G2B_arestas = nx.read_edgelist('G2_lista_arestas.txt')       # lê a partir da lista de arestas
G2B_adjacencia = nx.read_adjlist('G2_lista_adjacencia.txt')  # lê a partir da lista de adjacência
```

#### 2.4.7 Grafos ponderados
Para grafos com pesos nas arestas, usa-se `add_weighted_edges_from()`:
```python
G3 = nx.DiGraph()
vertices = ['A','B','C','D','E']
arestas = [('A','C',0.2), ('A','B',0.1), ('B','D',0.9),
           ('B','E',0.6), ('D','C',1), ('E','A',0.4)]   # cada tupla: (origem, destino, peso)

G3.add_nodes_from(vertices)
G3.add_weighted_edges_from(arestas)
```
Para **visualizar os pesos** no desenho, é necessário um passo extra:
```python
labels = nx.get_edge_attributes(G3, 'weight')      # dicionário {aresta: peso}
pos = nx.spring_layout(G3)                          # calcula posição dos vértices automaticamente
nx.draw_networkx(G3, pos, with_labels=True, node_color='orange', node_size=2000)
nx.draw_networkx_edge_labels(G3, pos, edge_labels=labels)  # desenha os rótulos de peso nas arestas
```

**Dica de estudo:** a tabela de complexidades (seção 2.3.5) é o ponto-chave desta unidade — ela justifica *por que* bibliotecas como o NetworkX usam internamente listas de adjacência (bom equilíbrio entre espaço e tempo) para a maioria das operações do dia a dia.

---

## Unidade 3 — Modelos de Redes Complexas

### 3.1 Contextualização

Existem duas formas de estudar redes complexas: **(1)** por **modelos de formação** (regras matemáticas que simulam como a rede surge e cresce) — úteis quando não se tem acesso a todos os dados, ou quando se quer simular cenários futuros/passados (ex.: propagação de epidemia, construção histórica da Web); e **(2)** por **extração de métricas** de uma rede já existente (tema da Unidade 4). Esta unidade aborda **4 modelos de formação** clássicos.

### 3.2 Modelo de redes regulares

O modelo mais simples: todos os vértices possuem exatamente o mesmo grau **k**. Constrói-se **N** vértices dispostos em anel, e cada vértice se conecta a exatamente **k** vizinhos mais próximos.

- **Limitação:** não reflete a maioria dos problemas reais — dificilmente todo mundo numa rede social ou todas as empresas numa rede de negócios têm exatamente o mesmo número de conexões.

### 3.3 Modelo de redes aleatórias de Erdös-Rényi (1959)

Proposto pelos matemáticos húngaros **Paul Erdös** e **Alfred Rényi**. Constrói-se a rede assim:
1. Inicia-se com N vértices totalmente desconectados.
2. Em cada passo, escolhem-se dois vértices aleatoriamente e conecta-se com uma probabilidade fixa **p** (cada par é considerado uma única vez, sem laços nem arestas múltiplas).
3. Repete-se para todos os pares possíveis — o máximo de arestas é **N·(N−1)/2** (grafo não dirigido).

Duas variantes matemáticas equivalentes:
- **Modelo G(N,p):** N fixo, cada par tem probabilidade p de se conectar.
- **Modelo G(N,M):** N e a quantidade de arestas M são fixos; escolhem-se M pares aleatoriamente.

**Propriedade chave:** como todas as conexões têm a mesma probabilidade, a rede é homogênea e sua **distribuição de graus segue uma curva Gaussiana (normal)** em torno de uma média — não reflete redes sociais reais, onde a maioria tem poucas conexões e poucos possuem milhões (ex.: rede social com 3 bilhões de usuários).

```python
import networkx as nx
rede_aleatoria = nx.erdos_renyi_graph(n=100, p=0.1)   # n=vértices, p=probabilidade de conexão
```

### 3.4 Modelo de redes de mundo pequeno de Watts-Strogatz (1998)

Desenvolvido por **Duncan Watts** e **Steven Strogatz**, baseado no fenômeno dos **"seis graus de separação"** (experimento de **Stanley Milgram**, 1967): em média, qualquer pessoa no mundo está a apenas ~6 conexões de distância de qualquer outra.

Redes de mundo pequeno combinam:
- **Caminhos curtos** entre pares de vértices (como nas redes aleatórias);
- **Alto coeficiente de agrupamento** (efeito de vizinhança — amigos dos meus amigos tendem a se conhecer).

**Construção (3 parâmetros: N, k, p):**
1. Cria-se uma rede **regular** com N vértices em anel, cada um conectado aos k vizinhos mais próximos (alto agrupamento inicial).
2. Percorre-se a rede (sentido horário ou anti-horário) e, para cada aresta, reconecta-se uma das extremidades a um vértice aleatório com probabilidade **p** (sem gerar laços ou arestas múltiplas).
3. Quando **p=0** → rede permanece regular. Quando **p=1** → rede totalmente aleatória. Valores intermediários geram o efeito de "mundo pequeno".

- **Limitação:** ainda gera distribuição de graus Gaussiana (não realista) e **N é fixo** — não é possível simular o crescimento da rede ao longo do tempo.

```python
rede_mundo_pequeno = nx.watts_strogatz_graph(n=100, k=5, p=0.3)  # n=vértices, k=grau inicial, p=prob. reconexão
```

### 3.5 Modelo de redes livres de escala de Barabási-Albert (1999)

Em 1999, **Albert-László Barabási** e **Réka Albert** mapearam a estrutura da **World Wide Web** usando um *crawler* (rastreador de páginas/*links*) e descobriram que, embora a Web apresentasse mundo pequeno, sua distribuição de graus **não** era Gaussiana — seguia uma **lei de potência**: a maioria das páginas tem poucos links, e uma pequena minoria (**hubs**) concentra um número enorme de conexões.

- Esse mesmo padrão aparece em redes de citações científicas, colaboração acadêmica, e redes sociais (perfis de celebridades no Instagram/Twitter = hubs).

**Mecanismo de formação — conexão preferencial ("rich-get-richer"):** vértices com mais conexões têm maior probabilidade de receber novas conexões. À medida que a rede cresce, os hubs tendem a ficar cada vez mais conectados.

**Construção:**
1. Inicia-se com um pequeno número de vértices **n₀** já conectados.
2. A cada passo, adiciona-se um novo vértice com **k** arestas (k ≤ n₀), conectando-se a vértices já existentes.
3. A probabilidade de conexão a um vértice **j** é **proporcional ao grau de j** (ligação preferencial).
4. Repete-se até atingir o tamanho/tempo desejado.

- **Chamado "livre de escala"** porque suas propriedades estruturais (lei de potência) se mantêm independentemente do tamanho (N) e ordem da rede — mesmo à medida que a rede cresce.
- **Resiliente a falhas aleatórias** (remoção aleatória raramente atinge um hub, já que hubs são poucos), mas **vulnerável a ataques direcionados** (remover um hub pode desconectar grande parte da rede).
- É o **único dos 4 modelos** que permite simular o **crescimento** da rede ao longo do tempo (N não é fixo).

```python
rede_livre_escala = nx.barabasi_albert_graph(n=100, m=1)   # n=vértices finais, m=arestas por novo vértice
```

### 3.6 Comparação visual dos 3 modelos (Erdös-Rényi vs. Watts-Strogatz vs. Barabási-Albert)

```python
import matplotlib as plt
plt.figure(figsize=(20,5))            # define o tamanho da figura como 20 x 5
plt.subplot(131); nx.draw(rede_aleatoria)      # subplot 1 de 3
plt.subplot(132); nx.draw(rede_mundo_pequeno)  # subplot 2 de 3
plt.subplot(133); nx.draw(rede_livre_escala)   # subplot 3 de 3
```

### 3.7 Propriedades compartilhadas por redes reais (resumo)

1. **Fenômeno de mundo pequeno:** existência de atalhos entre a maioria dos vértices.
2. **Transitividade/agrupamento:** alta probabilidade de "amigo do meu amigo também ser meu amigo" (triângulos na rede).
3. **Distribuição de graus em lei de potência:** poucos hubs, muitos vértices com grau baixo.
4. **Resiliência da rede:** robusta a remoções aleatórias, mas sensível à remoção de hubs.
5. **Estrutura de comunidade:** grupos densamente conectados internamente e esparsamente conectados entre si.

### 3.8 Tabela-resumo dos 4 modelos

| Modelo | Grau dos vértices | Distribuição de graus | N fixo? | Reflete redes reais? |
|---|---|---|---|---|
| Redes regulares | Todos iguais (k) | — | Sim | Não |
| Erdös-Rényi (aleatório) | Similar, em torno de uma média | Gaussiana | Sim | Não |
| Watts-Strogatz (mundo pequeno) | Similar, em torno de uma média | Gaussiana | Sim | Parcialmente (caminhos curtos + agrupamento) |
| Barabási-Albert (livre de escala) | Muito variável (hubs) | Lei de potência | **Não** (cresce com o tempo) | Sim |

**Dica de estudo:** a evolução histórica dos modelos (regular → aleatório → mundo pequeno → livre de escala) é também uma evolução na fidelidade à realidade — cada modelo corrige uma limitação do anterior.

---

## Unidade 4 — Extraindo Informações de Redes Complexas (Parte I)

### 4.1 Contextualização

Complementando os modelos de formação (Unidade 3), esta unidade aborda a **segunda abordagem** de análise de redes: extrair **métricas** de uma rede já construída, para caracterizar sua estrutura (topologia) tanto no nível local (vértices e conexões) quanto global (a rede como um todo). Os cálculos são apresentados a partir da **matriz de adjacências**.

### 4.2 Ordem e Tamanho (revisão formal)

- **Ordem:** quantidade de vértices — corresponde à dimensão N×N da matriz de adjacências.
- **Tamanho:** quantidade de arestas — em grafos **não dirigidos**, soma-se apenas os valores **1** da parte superior (ou inferior) da matriz, **ignorando a diagonal principal**, pois cada aresta é representada duas vezes (simetria da matriz).

### 4.3 Grau de um vértice (fórmula formal)

O grau **kᵢ** de um vértice *i* é a soma de todos os elementos da linha (ou coluna) *i* da matriz de adjacência **A**:

```
kᵢ = Σ(j=1 até N) A[i][j]
```

### 4.4 Grau médio da rede

Média do grau de todos os vértices:

```
Grau médio = (1/N) · Σ(i=1 até N) kᵢ
```

Exemplo: rede com 10 vértices e graus [5,6,5,4,4,3,4,4,3,6] → grau médio = 4,4.

### 4.5 Distribuição de graus

Contagem de quantos vértices possuem cada valor de grau, geralmente visualizada como histograma (barras). Procedimento: ordenar os graus de forma crescente, contar as ocorrências de cada valor, e plotar.

### 4.6 Distância geodésica e distância geodésica média

- **Distância geodésica (d(i,j)):** comprimento do **caminho mínimo** (menor número de arestas) entre dois vértices *i* e *j*.
- **Distância geodésica média** da rede: soma das distâncias mínimas entre **todos** os pares de vértices, dividida pela quantidade máxima de arestas possíveis N·(N−1):

```
Distância geodésica média = Σ(i,j ∈ V) d(i,j) / [N·(N−1)]
```

- Interpretação prática: quão longe, em média, dois vértices quaisquer estão um do outro. Uma distância média baixa é evidência da propriedade de **mundo pequeno**.

### 4.7 Excentricidade de vértice

A **excentricidade** de um vértice *i* é a **maior** distância geodésica observada entre *i* e qualquer outro vértice *j* da rede — ou seja, o quão distante o vértice está do vértice mais "longe" dele.

### 4.8 Raio e diâmetro do grafo

- **Raio:** a **menor** excentricidade entre todos os vértices da rede.
- **Diâmetro:** a **maior** excentricidade entre todos os vértices da rede (ou seja, a maior distância observada entre qualquer par de vértices).

### 4.9 Densidade

Mede a fração de arestas existentes em relação ao número **máximo** possível de arestas:
- Grafos **dirigidos**: densidade = m / [N·(N−1)]
- Grafos **não dirigidos**: densidade = m / [N·(N−1)/2]

Onde *n* = número de vértices e *m* = número de arestas. Valor sempre entre **0** (nenhuma aresta) e **1** (grafo completo).
- **Rede densa** (ou "densamente conectada"): densidade próxima de 1.
- **Rede esparsa:** densidade baixa. **A maioria das redes complexas reais é esparsa** — por exemplo, a densidade da rede da Wikipédia é de apenas 0,1 (Zinoviev, 2018).
- Segundo Wasserman e Faust (1994): quanto mais densa a rede, melhor o fluxo de informação entre seus vértices.

### 4.10 Coeficiente de agrupamento (3 variantes)

Mede a propensão da rede de formar grupos (*clusters*) — conjuntos de vértices densamente conectados entre si, correspondentes a **comunidades** em redes sociais.

**Conceitos-base:**
- **Trio:** sequência de 3 vértices conectados por **2** arestas (ex.: A–B, A–C, sem B–C).
- **Triângulo:** 3 vértices conectados por **3** arestas (todos ligados entre si) — forma um **clique**.

#### 4.10.1 Coeficiente de agrupamento local
Mede a propensão de um vértice específico, junto de seus vizinhos, formar um clique.

```
Cᵢ = 2·Tᵢ / [kᵢ·(kᵢ−1)]
```
Onde **kᵢ** = grau do vértice *i* e **Tᵢ** = número de arestas que interconectam os vizinhos de *i*.

- Varia entre **0** (nenhum vizinho de *i* se conecta entre si) e **1** (todos os vizinhos de *i* formam um clique com *i*).
- Exemplo: vértice com grau k=3, conectado a vizinhos com 2 arestas entre eles → C = (2·2)/(3·2) = 0,66.

#### 4.10.2 Coeficiente de agrupamento global (transitividade)
Mede a propensão de toda a rede formar grupos, usando a proporção entre triângulos e trios:

```
Coef. global = 3 · (quantidade de triângulos) / (quantidade de trios)
```
- Quanto mais próximo de 1, mais a rede se aproxima de um grafo completo.
- Exemplo: rede com 2 triângulos e 3 trios → coeficiente = (3·2)/3 = **0,75** — ou seja, transitividade alta = "amigo do meu amigo também é meu amigo".

#### 4.10.3 Coeficiente de agrupamento médio
Média do coeficiente de agrupamento **local** de todos os vértices da rede:

```
Coef. médio = (1/N) · Σ(i=1 até N) Cᵢ
```

- **Importante para diferenciar tipos de rede:** redes de **mundo pequeno** apresentam coeficiente de agrupamento médio significativamente **maior** que redes **aleatórias** com o mesmo número de vértices (ex.: 0,71 vs. 0,26 em uma rede de 20 vértices) — reforçando a ligação entre este coeficiente e a Unidade 3.

### 4.11 Tabela-resumo das métricas da Unidade 4

| Métrica | O que mede | Fórmula/observação |
|---|---|---|
| Ordem / Tamanho | Nº de vértices / arestas | Dimensão da matriz / soma da parte superior |
| Grau de um vértice | Nº de conexões | Soma da linha/coluna da matriz |
| Grau médio | Conectividade média | Média dos graus |
| Distância geodésica média | Distância típica entre vértices | Soma dos caminhos mínimos / máx. de arestas |
| Excentricidade | Distância ao vértice mais longe | Maior d(i,j) de um vértice |
| Raio / Diâmetro | Excentricidade mín./máx. da rede | — |
| Densidade | Nível de conectividade geral | Arestas existentes / arestas máximas |
| Coef. de agrupamento (local/global/médio) | Propensão a formar grupos | Baseado em trios e triângulos |

**Dica de estudo:** esta unidade prepara o terreno para a Unidade 5 (medidas de centralidade), que aprofunda a ideia de "importância" de um vértice além do grau simples (ex.: centralidade de proximidade, intermediação, autovetor).

---

## Unidade 5 — Extraindo Informações de Redes Complexas (Parte II)

### 5.1 Contextualização

Segunda parte da extração de métricas de redes complexas. Enquanto a Unidade 4 tratou de medidas **locais** (grau, excentricidade, coeficiente de agrupamento) e **globais** (densidade, distância geodésica média) que assumem que já sabemos qual vértice nos interessa, esta unidade aborda uma tarefa anterior e essencial: **identificar quais são os vértices mais importantes da rede** — as **medidas de centralidade**.

### 5.2 Centralidade — conceito geral

A **centralidade** (ou **prestígio**) de um vértice mede sua importância na rede, geralmente relacionada ao número de vértices que ele consegue alcançar. Vértices centrais têm "poder" na rede — por exemplo, acesso mais rápido a informações. As medidas de centralidade têm origem no estudo de redes sociais (Freeman, 1978) e hoje são usadas em redes de comunicação, biológicas, metabólicas, e em mecanismos de busca como o Google (algoritmo PageRank, baseado em centralidade de autovetor).

Para facilitar a comparação entre redes de tamanhos diferentes, os valores de centralidade costumam ser **normalizados** entre 0 e 1 (0 = baixa importância, 1 = alta importância).

### 5.3 Centralidade de grau (*degree centrality*)

A medida mais simples e intuitiva: quanto mais conexões um vértice tem, mais importante ele é. É o grau do vértice, **normalizado** pelo grau máximo possível (n−1, em um grafo não dirigido com n vértices):

```
Centralidade de grau(i) = kᵢ / (n − 1)
```

Exemplo: em um grafo com 6 vértices, o vértice D com grau 4 tem centralidade de grau = 4/(6−1) = 0,8; um vértice com grau 1 tem centralidade = 1/(6-1) = 0,2.

### 5.4 Centralidade de intermediação (*betweenness centrality*)

Mede a importância de um vértice pela **quantidade de vezes que ele aparece nos caminhos mínimos** entre todos os pares de vértices da rede. Um vértice com alta intermediação é essencial para o fluxo de informação na rede — sua remoção obriga a busca de novos caminhos.

```
Centralidade de intermediação(i) = Σ (s≠t≠i ∈ V) [ nᵢₛₜ / gₛₜ ]
```
Onde **nᵢₛₜ** = quantidade de caminhos mínimos entre os vértices *s* e *t* que passam por *i*, e **gₛₜ** = quantidade total de caminhos mínimos entre *s* e *t*. Versão normalizada (dividindo pelo total de pares (n−1)(n−2)/2):

```
Centralidade de intermediação(i) = Σ (nᵢₛₜ/gₛₜ) / [(n−1)(n−2)/2]
```

- Valor **0**: vértice não participa de nenhum caminho mínimo (removê-lo não afeta o fluxo de informação).
- Valor **1**: vértice está presente em **todos** os caminhos mínimos da rede (removê-lo compromete seriamente a comunicação).
- **Custo computacional elevado** — depende do cálculo de caminhos mínimos entre todos os pares. O **algoritmo de Brandes (2001)** (usado pelo NetworkX) otimiza esse cálculo; em redes muito grandes, usam-se algoritmos aproximados (Borassi e Natale, 2016).

### 5.5 Centralidade de proximidade (*closeness centrality*)

Mede a importância de um vértice pela sua **proximidade média** a todos os demais vértices da rede — quanto mais próximo (menor distância geodésica média), mais central.

```
Centralidade de proximidade(i) = (n − 1) / Σ(j=1 até n, j≠i) d(i,j)
```

- Valor próximo de **1**: vértice tem baixa distância média — informação a partir dele chega rápido a toda a rede.
- Valor próximo de **0**: vértice está distante da maioria dos demais.
- **Limitações:** exige adaptação para grafos com múltiplas componentes desconexas; e como as distâncias crescem logaritmicamente com o tamanho da rede, a diferença de *ranking* entre vértices tende a ser pequena (só nos últimos dígitos) em redes grandes.

### 5.6 Centralidade de autovetor (*eigenvector centrality*)

Estende a centralidade de grau: um vértice é importante não só pela quantidade de conexões que possui, mas também pela **importância de seus vizinhos**. Ou seja, um vértice é central se está conectado a muitos vértices, **ou** se está conectado a poucos vértices que, por sua vez, são muito conectados.

```
xᵢ = (1/λ) · Σ(j=1 até n) aᵢⱼ · xⱼ
```
Onde **λ** é o maior autovalor da matriz de adjacência **A** (usado para normalizar o resultado entre 0 e 1), e **aᵢⱼ** é a entrada da matriz de adjacência.

- **Base do algoritmo PageRank** (Google, Larry Page e Sergey Brin, 1998): a ideia é que a "importância" de uma página web deve considerar não apenas quantos links ela recebe, mas a **qualidade/relevância** de quem faz esses links.
- Exemplo prático: em uma rede de citações acadêmicas, a centralidade de autovetor pode identificar autores pouco citados no total, mas frequentemente citados por autores muito importantes.

### 5.7 Comparação entre as 4 medidas de centralidade

| Medida | Um vértice é importante quando... |
|---|---|
| Centralidade de grau | está conectado a muitos outros vértices |
| Centralidade de proximidade | sua distância média a todos os outros vértices é pequena |
| Centralidade de intermediação | faz parte de muitos caminhos mínimos da rede |
| Centralidade de autovetor | está conectado a outros vértices que também são considerados importantes |

Exemplos de aplicação por medida:
- **Grau:** rede de colaborações → artista com mais colaborações.
- **Intermediação:** rede de telecomunicações → nó por onde passa mais tráfego (exige atenção especial na manutenção).
- **Proximidade:** rede de propagação de doenças → indivíduo com maior potencial de transmissão rápida.
- **Autovetor:** rede de citações → autor pouco citado, mas citado por autores muito relevantes.

**Dica de estudo:** as quatro medidas respondem perguntas diferentes sobre "importância" — não existe uma única métrica "correta"; a escolha depende do que se quer entender sobre o problema representado pela rede.

---

## Unidade 6 — Detectando Grupos e Comunidades em Redes Complexas

### 6.1 O que são comunidades e por que detectá-las

Uma **comunidade** (ou grupo, ou *cluster*) em um grafo G é um subconjunto de vértices **densamente conectados entre si**, mas **esparsamente conectados** com o restante da rede. Vértices de uma mesma comunidade tendem a compartilhar propriedades ou desempenhar papéis semelhantes na rede.

O estudo de comunidades tem raízes em duas áreas distintas desde a década de 70: o **particionamento de grafos** (Ciência da Computação, para alocar tarefas a processadores minimizando comunicação) e o **agrupamento hierárquico** (Sociologia, para simplificar a análise de fenômenos sociais).

### 6.2 Aplicações

- **Redes sociais:** recomendação de amizades, vagas de emprego, músicas.
- **Comércio eletrônico:** recomendação de produtos, *marketing* direcionado.
- **Segurança:** identificação de grupos terroristas/criminosos ou *bots* maliciosos.
- **Redes de computadores:** agrupar servidores por fluxo de informação (tabelas de roteamento mais compactas).
- **Colaboração científica:** identificar grupos de pesquisadores com temas em comum.
- **Biologia:** grupos de proteínas com funções similares; dinâmica de epidemias por grupos sociais/comorbidades.

### 6.3 Abordagens algorítmicas: aglomerativa vs. divisiva

As comunidades podem ser organizadas **hierarquicamente** (ex.: pessoas → país → cidade → empresa → departamento). Essa hierarquia é representada por um **dendrograma**. Duas abordagens principais:
- **Métodos aglomerativos:** começam com cada vértice sendo sua própria comunidade e vão **unindo** vértices/comunidades semelhantes a cada iteração (constrói o dendrograma de baixo para cima).
- **Métodos divisivos:** começam com **toda a rede como uma única comunidade** e vão **removendo arestas** para dividi-la progressivamente (constrói o dendrograma de cima para baixo).

O corte do dendrograma em diferentes níveis produz diferentes quantidades de comunidades (cortes mais próximos da base = mais comunidades, com menos vértices cada).

### 6.4 Métodos divisivos — Algoritmo *Edge Betweenness* (Girvan-Newman, 2002)

Um dos algoritmos mais populares. Remove arestas progressivamente até que não seja possível remover mais nenhuma (cada vértice se torna sua própria comunidade).

**Critério de remoção:** a **centralidade de intermediação de aresta** (*edge betweenness*) — análoga à centralidade de intermediação de vértice (Unidade 5), mas medindo quantos caminhos mínimos passam por cada **aresta**. Arestas que conectam comunidades diferentes ("pontes") tendem a ter alta intermediação — removê-las isola os grupos.

**Algoritmo (4 passos, repetidos até remover todas as arestas):**
1. Calcular a centralidade de intermediação de todas as arestas da rede;
2. Remover a aresta com maior valor de intermediação;
3. Recalcular os valores de intermediação para as arestas restantes;
4. Voltar ao passo 2.

- **Saída:** um dendrograma completo; o corte em diferentes níveis revela diferentes partições da rede.
- **Custo computacional elevado:** só o cálculo da intermediação de todas as arestas já é O(M·N²) (M arestas, N vértices) — e deve ser refeito a cada remoção. Inviável em redes muito grandes.

### 6.5 Métodos aglomerativos — Algoritmo CNM (Clauset-Newman-Moore, 2004)

Baseado na medida de **modularidade (Q)**, que avalia a qualidade das comunidades encontradas (varia entre -1 e 1; valores próximos de 1 indicam melhor estrutura de comunidades):

```
Q = Σ(i=1 até K) (eᵢᵢ − aᵢ²)
```
Onde *i* representa uma comunidade, **eᵢᵢ** = fração de arestas inteiramente dentro da comunidade *i*, e **aᵢ** = fração de arestas com pelo menos um extremo na comunidade *i*.

**Funcionamento:** inicia com N comunidades (uma por vértice). A cada iteração, une o par de comunidades que resulta no **maior ganho** (ou menor perda) de modularidade Q. Repete até restar uma única comunidade, gerando um dendrograma; corta-se no nível de **maior valor de Q**. Também chamado de algoritmo ***greedy*** (guloso) em algumas bibliotecas.

- **Complexidade:** O(M·d·log N), onde *d* = profundidade do dendrograma — menor que Girvan-Newman em média, mas ainda custoso em redes densas.

### 6.6 Métodos aglomerativos — Algoritmo de Louvain (Blondel et al., 2008)

Também baseado em modularidade, mas em **duas fases**, repetidas em **passos**:
1. **Fase 1:** cada vértice começa como sua própria comunidade. Para cada vértice *i*, verifica-se o ganho de modularidade ao mover *i* para a comunidade de cada vizinho *j*; *i* é movido para a comunidade que gera o **maior ganho positivo** (ou permanece, se nenhum ganho é positivo). Repete até não haver mais ganho possível.
2. **Fase 2:** constrói-se uma **nova rede** em que cada comunidade da Fase 1 se torna um único vértice (ponderado). Pesos das arestas = soma das conexões entre as comunidades; cada vértice recebe um laço com peso igual a 2× o número de conexões internas da comunidade.
3. As duas fases se repetem sobre a rede reduzida até não haver mais ganho de modularidade.

- **Complexidade:** O(N log N) — muito mais eficiente, capaz de processar redes com **até 100 milhões de vértices**.
- Tende a obter **melhores valores de modularidade** que Girvan-Newman e CNM.

### 6.7 Algoritmo de Propagação de Rótulos (*Label Propagation*, Raghavan, Albert e Kumara, 2007)

Detecta comunidades usando **apenas a estrutura da rede**, sem otimizar uma função objetivo (como modularidade).

**Funcionamento:** cada vértice recebe um rótulo aleatório (indicando sua comunidade). Em cada iteração, cada vértice **atualiza seu rótulo** para o rótulo mais comum (consenso) entre seus vizinhos (ordem de visita e empates decididos aleatoriamente). O algoritmo termina quando cada vértice já possui o rótulo da maioria de seus vizinhos.

- **Vantagem:** muito rápido, indicado para redes de larga escala.
- **Desvantagem:** é **não determinístico** — cada execução pode gerar um resultado diferente (mitigado fixando a mesma *seed* aleatória entre execuções); em redes aleatórias homogêneas, tende a identificar toda a rede como uma única comunidade.

### 6.8 Desafios da detecção de comunidades

- **Alto custo computacional**, especialmente em redes densamente conectadas (muitos algoritmos escalam com o número de arestas, que pode superar em muito o número de vértices).
- **Não se sabe a priori** o número ou tamanho ideal das comunidades.
- A **modularidade** é a medida de qualidade mais usada, mas um valor maior de modularidade **não garante** que o resultado seja mais útil para o especialista do domínio — cabe a ele avaliar e escolher o algoritmo mais adequado ao problema.
- Todos os algoritmos discutidos assumem que cada vértice pertence a **uma única comunidade**; existem algoritmos (não cobertos aqui) que permitem **sobreposição** de comunidades — relevante, por exemplo, em redes sociais, onde pessoas pertencem a várias comunidades simultaneamente.

### 6.9 Tabela-resumo dos algoritmos de detecção de comunidades

| Algoritmo | Abordagem | Critério | Complexidade |
|---|---|---|---|
| Edge Betweenness (Girvan-Newman) | Divisiva | Centralidade de intermediação de aresta | O(M·N²) |
| CNM (Clauset-Newman-Moore) | Aglomerativa | Modularidade (Q) | O(M·d·log N) |
| Louvain | Aglomerativa (2 fases) | Modularidade (Q) | O(N log N) |
| Propagação de Rótulos | Nenhuma (baseado em consenso) | Rótulo majoritário dos vizinhos | Muito baixa (redes de larga escala) |

**Dica de estudo:** note o paralelo direto entre esta unidade e a Unidade 5 — a centralidade de intermediação (de vértice) vira "centralidade de intermediação de aresta" no algoritmo de Girvan-Newman; entender bem a Unidade 5 facilita entender esta.

---

## Unidade 7 — Prevendo Novas Conexões na Rede

### 7.1 Contextualização e definição da tarefa

A **predição de conexões** (ou *link prediction*) é uma das tarefas mais populares de mineração de grafos — está por trás de sugestões de amizade em redes sociais, recomendações de filmes/produtos, etc. O objetivo é **estimar a probabilidade de existir uma conexão futura** entre dois vértices que atualmente não estão conectados, com base nos atributos dos vértices e nas conexões já existentes na rede.

A tarefa considera o **aspecto temporal**: dado o estado da rede no tempo *t*, busca-se prever quais conexões surgirão no tempo futuro *t+1*. Uma tarefa relacionada é a **predição de links faltantes** — identificar conexões que podem ter sido perdidas durante a construção da rede (útil, por exemplo, em manutenção preditiva de redes de equipamentos).

### 7.2 Avaliação da qualidade da predição

Como não é possível "esperar o futuro" para validar, avalia-se removendo arestas conhecidas da rede e verificando se o algoritmo consegue identificá-las de volta. Quatro categorias de resultado:
- **Verdadeiro positivo:** aresta removida foi corretamente identificada.
- **Verdadeiro negativo:** aresta que de fato não existe foi corretamente não predita.
- **Falso positivo:** algoritmo previu uma conexão que não existe/não ocorrerá.
- **Falso negativo:** algoritmo deixou de prever uma conexão que de fato existe/ocorrerá.

Medidas de avaliação derivadas dessas taxas:
```
Precisão  = Verdadeiros positivos / (Verdadeiros positivos + Falsos positivos)
Revocação = Verdadeiros positivos / (Verdadeiros positivos + Falsos negativos)
```
- **Precisão:** das arestas indicadas pelo algoritmo, quantas realmente existiam?
- **Revocação:** das arestas que foram removidas, quantas foram identificadas corretamente?
- **AUC (*Area Under Curve*):** medida baseada na curva **ROC** (*Receiver Operating Characteristic*), que relaciona a taxa de verdadeiros positivos com a taxa de falsos positivos.

### 7.3 Aplicações

- **Redes sociais:** sugestão de amizades; redes de coautoria científica (sugerir colaborações).
- **Sistemas de recomendação:** produtos, serviços, notícias, músicas, filmes.
- **Propagação de doenças:** prever caminhos futuros de contágio (AIDS, dengue, Coronavírus) para planejar isolamento/vacinação.
- **Estruturação de redes criminosas:** inferir conexões ocultas (ex.: redes terroristas) a partir de informação parcial.
- Também presente em redes biológicas (interação entre proteínas) e aplicações médicas (predição de sintomas/novos usos de medicamentos).
- Pode envolver **redes heterogêneas** (componentes de natureza diferente — pessoas, eventos, músicas, produtos) ou **redes homogêneas** (todos os vértices com a mesma função).

### 7.4 Abordagens: métodos baseados em similaridade

Segundo Lü e Zhou (2011), os métodos de predição de links dividem-se em: **(i)** baseados em similaridade, **(ii)** baseados em máxima verossimilhança, e **(iii)** modelos probabilísticos (+ métodos híbridos). Esta unidade foca nos **métodos baseados em similaridade** — os mais populares, por serem simples, eficazes e aplicáveis a qualquer tipo de rede (usam apenas informação topológica).

Para cada par de vértices, calcula-se uma **pontuação de similaridade**: pares com maior pontuação são considerados mais propensos a se conectarem no futuro. Os índices se dividem em:
- **Índices locais:** usam apenas informações do par de vértices e sua vizinhança — computacionalmente baratos.
- **Índices globais:** usam informações de toda (ou da maior parte) da rede — mais custosos, porém com maior poder preditivo.

*(Notação usada abaixo: Γ(x) = conjunto de vizinhos do vértice x; kₓ = grau do vértice x.)*

### 7.5 Índice de Vizinhos Comuns (*Common Neighbors*) — local

```
S(x,y) = |Γ(x) ∩ Γ(y)|
```
Conta quantos vizinhos os vértices *x* e *y* têm em comum. Quanto maior a contagem, maior a probabilidade de conexão futura (efeito de **fechamento de triângulos** — "o amigo do meu amigo tende a ser meu amigo"). Simples, computacionalmente barato e base de muitos outros índices.

### 7.6 Índice de Jaccard — local

Corrige uma limitação do índice anterior: vértices com muitos vizinhos (ex.: celebridades) podem ter alto valor de vizinhos comuns mesmo sem grande similaridade real. O Índice de Jaccard **normaliza pela união** dos vizinhos:

```
S(x,y) = |Γ(x) ∩ Γ(y)| / |Γ(x) ∪ Γ(y)|
```

### 7.7 Índice de Salton — local

Também baseado em vizinhos comuns, mas normaliza **pelo grau dos vértices** (a raiz do produto dos graus), de modo que pares com maior grau tendem a valores mais baixos de similaridade:

```
S(x,y) = |Γ(x) ∩ Γ(y)| / √(kₓ · k_y)
```

### 7.8 Índice de Conexão Preferencial (*Preferential Attachment*) — local

Baseado no fenômeno "*rich get richer*" (Unidade 3 — modelo Barabási-Albert): vértices com mais conexões têm maior probabilidade de ganhar novas conexões.

```
S(x,y) = kₓ · k_y
```
- **Vantagem importante:** não exige conhecer a vizinhança dos vértices (apenas o grau), tornando-o o índice de **menor custo computacional** entre os apresentados.

### 7.9 Índice de Alocação de Recursos (*Resource Allocation*) — local

Inspirado no processo físico de **alocação de recursos**: cada vizinho comum *w* de *x* e *y* distribui uma unidade de recurso igualmente entre todos os seus próprios vizinhos; a quantidade de recurso recebida por *y* a partir de *x* é a medida de similaridade:

```
S(x,y) = Σ (w ∈ Γ(x)∩Γ(y)) 1/|Γ(w)|
```
Ou seja, vizinhos comuns com **poucas conexões próprias** contribuem mais para a pontuação do que vizinhos comuns muito conectados (hubs).

### 7.10 Índice de Adamic-Adar — local

Muito similar ao de Alocação de Recursos, mas **suaviza o peso** de cada vizinho comum aplicando o **logaritmo** do seu grau:

```
S(x,y) = Σ (w ∈ Γ(x)∩Γ(y)) 1/log|Γ(w)|
```

### 7.11 Índice de Katz — global

Considera a soma de **todos os caminhos possíveis** (não apenas o mínimo) entre dois vértices, ponderando caminhos mais curtos com maior peso:

```
S(x,y) = Σ(l=1 até ∞) βˡ · |caminhos_{x,y}^{(l)}|
```
Onde **caminhos_{x,y}^{(l)}** é o conjunto de caminhos de tamanho *l* entre *x* e *y*, e **β ∈ (0,1)** controla o peso dado a caminhos mais longos (valores de β mais próximos de 1 aumentam a influência de caminhos longos).

### 7.12 Índice SimRank — global

Considera que dois vértices são similares se **seus vizinhos também são similares** entre si (definição recursiva):

```
S(x,y) = γ · [ Σ(a∈Γ(x)) Σ(b∈Γ(y)) S(a,b) ] / [|Γ(x)| · |Γ(y)|]
```
Onde **γ** é uma constante e **S(x,x) = 1** (similaridade máxima de um vértice com ele mesmo). Os autores originais sugerem γ = 0,8 e 5 iterações.

### 7.13 Tabela-resumo dos índices de similaridade

| Índice | Tipo | Ideia central |
|---|---|---|
| Vizinhos Comuns | Local | Contagem de vizinhos compartilhados |
| Jaccard | Local | Vizinhos comuns normalizados pela união |
| Salton | Local | Vizinhos comuns normalizados pelo grau |
| Conexão Preferencial | Local | Produto dos graus (rich-get-richer); não precisa da vizinhança |
| Alocação de Recursos | Local | "Recurso" distribuído pelos vizinhos comuns, ponderado pelo grau deles |
| Adamic-Adar | Local | Como Alocação de Recursos, mas com peso logarítmico |
| Katz | Global | Soma de todos os caminhos, ponderados pelo tamanho |
| SimRank | Global | Similaridade recursiva entre vizinhos |

### 7.14 Desafios da predição de links

- **Custo computacional:** verificar a maioria das arestas possíveis da rede é caro; índices locais são preferíveis em redes de larga escala.
- **Uso de pesos das arestas:** ainda é um desafio de pesquisa — alguns estudos indicam que conexões com pesos maiores são mais relevantes para predição, outros sugerem o contrário (Rebaza, 2013).
- **Temporalidade:** conexões não surgem todas ao mesmo tempo; a informação de *quando* cada link surgiu também pode ser relevante para o modelo preditivo.

**Dica de estudo:** os índices locais formam uma progressão natural — Vizinhos Comuns é a base; Jaccard e Salton são normalizações dele; Conexão Preferencial usa só o grau (mais barato); Alocação de Recursos e Adamic-Adar refinam o peso dado a cada vizinho comum.

---

## Unidade 8 — Melhorando os Aspectos Visuais das Redes Complexas

### 8.1 Contextualização

O sucesso da análise de dados usando grafos não depende só dos algoritmos de extração de métricas e das tarefas de mineração (centralidade, comunidades, predição de links) — depende também de **apresentar os resultados de forma clara e eficaz**, tanto para especialistas quanto para leigos no domínio do problema. Esta unidade discute **algoritmos de leiaute** (distribuição espacial dos vértices) e **técnicas visuais** (cor, tamanho) para tornar redes mais legíveis.

### 8.2 Por que a distribuição dos vértices importa

A forma mais simples de posicionar vértices é **aleatoriamente** — baixo custo computacional, mas com duas limitações importantes:
1. **Não é reprodutível:** cada vez que a rede é desenhada, os vértices aparecem em posições diferentes, dificultando a comparação visual entre execuções ou o compartilhamento de uma mesma "leitura" da rede entre usuários diferentes.
2. **Não destaca vértices importantes:** a posição aleatória não considera se um vértice é central ou faz parte de algum grupo.

Um bom posicionamento deve seguir critérios como: **minimizar cruzamentos de arestas**, manter **simetria**, agrupar vértices semelhantes em regiões próximas e manter **tamanhos uniformes** de arestas.

Os algoritmos de leiaute mais conhecidos se dividem em duas categorias: **distribuição circular** e **dirigidos por força** (*force-directed*).

### 8.3 Algoritmos de distribuição circular

Posicionam os vértices na borda de uma circunferência. **Baixo custo computacional** — O(n), linear no número de vértices — mas tendem a apresentar **muitos cruzamentos de arestas** em redes densamente conectadas.

#### 8.3.1 Leiaute circular básico
Vértices dispostos em círculo, igualmente espaçados. A ordem pode ser aleatória, pelo rótulo do vértice, ou por alguma medida extraída da rede (ex.: grau) — ordenar por uma medida ajuda a identificar grupos de vértices similares e reduz cruzamentos. Indicado para redes **pequenas**.

#### 8.3.2 Leiaute circular duplo
Variação que distribui os vértices em **duas circunferências** concêntricas, permitindo destacar um subconjunto de vértices (ex.: os 5 vértices de maior grau) em uma circunferência separada (interna ou externa à principal).

#### 8.3.3 Leiaute estrela
Variação do circular duplo em que **apenas um** vértice principal (ex.: o de maior grau) é destacado, isolado no centro/interior da rede.

#### 8.3.4 Leiaute de eixo radial
Posiciona os vértices principais de acordo com uma medida/critério em uma **circunferência central**, e agrupa os demais vértices em **eixos** que irradiam dessa circunferência — permite escolher diferentes critérios tanto para a formação do círculo central quanto para o agrupamento nos eixos (ex.: grau para o círculo, coeficiente de agrupamento para os eixos).

### 8.4 Algoritmos dirigidos por força (*force-directed*)

Modelam o grafo como um **sistema físico de corpos** com forças de atração (vértices conectados) e repulsão (vértices não conectados) atuando entre si, buscando **minimizar a energia do sistema**. Resultam em redes com maior **uniformidade de tamanho das arestas** e **simetria** na distribuição dos vértices (Kobourov, 2004). Em geral, **mais custosos computacionalmente** — complexidade O(n²) para os algoritmos clássicos.

#### 8.4.1 Kamada-Kawai
Baseado na **lei de Hooke** (física de corpos elásticos/molas). Modela cada vértice como conectado por "molas" cujo tamanho é proporcional à distância entre os vértices. Passos: (1) posições iniciais aleatórias; (2) cálculo da distância geodésica entre todos os pares; (3) definição de uma distância "ideal" considerando a área disponível, o diâmetro da rede e a distância entre os vértices; (4) reposicionamento dos vértices para minimizar a energia (aproximando-se da distância ideal).

#### 8.4.2 Fruchterman-Reingold
Também simula um sistema de partículas com molas, combinando **forças de atração** entre vértices vizinhos e **forças de repulsão** entre vértices não conectados. Tende a produzir redes com boa simetria em formato aproximadamente esférico, com cruzamentos de arestas ainda mais reduzidos que o Kamada-Kawai.

#### 8.4.3 Force Atlas 2
Também simula um sistema físico (vértices como partículas carregadas que se repelem; arestas como molas que atraem), mas com formulação matemática diferente para as forças — segundo os autores, mais fiel ao comportamento real de sistemas de molas (Jacomy et al., 2014). **Vantagem:** menor custo computacional, **O(n log n)**. Permite configurar uma relação **linear, exponencial ou logarítmica** entre distância e força (os demais algoritmos assumem relação linear).

#### 8.4.4 Tabela-resumo dos algoritmos dirigidos por força

| Algoritmo | Base física | Complexidade | Observação |
|---|---|---|---|
| Kamada-Kawai | Lei de Hooke (molas) | O(n²) | Usa distância geodésica ideal |
| Fruchterman-Reingold | Atração/repulsão de partículas | O(n²) | Boa simetria esférica |
| Force Atlas 2 | Partículas carregadas + molas | O(n log n) | Mais eficiente; relação distância-força configurável |

*(Outros algoritmos citados mas não detalhados na unidade: Force Atlas, OpenOrd, Yafan Hu.)*

### 8.5 Melhorando a legibilidade com cor e tamanho

Além do leiaute, é possível evidenciar características da rede alterando as **propriedades visuais** dos elementos:

#### 8.5.1 Uso de cores para os vértices
Atribui-se um **mapa de cores** (ex.: do branco/claro ao vermelho/escuro) de acordo com o *ranking* dos vértices em alguma medida (grau, intermediação, proximidade, autovetor, etc.) — vértices/arestas mais "importantes" recebem cores mais intensas. Também é usado para destacar **comunidades** detectadas (uma cor distinta por comunidade).

#### 8.5.2 Combinando cor e tamanho dos vértices
Quando se quer destacar **mais de uma característica simultaneamente**, pode-se combinar: cor para uma medida (ex.: comunidade, ou centralidade de intermediação) e **tamanho do vértice** para outra medida (ex.: grau, proximidade, coeficiente de agrupamento). Isso permite visualizar duas propriedades da rede ao mesmo tempo em uma única imagem.

#### 8.5.3 Arestas curvas
Por razões estéticas, também é possível usar **arestas curvas** em vez de retas, o que pode reduzir a sobreposição visual em certos leiautes.

### 8.6 Conclusão da unidade

Em redes pequenas, a disposição manual ou aleatória dos vértices não é um grande problema. Em redes com muitos elementos, porém, a distribuição aleatória torna a rede difícil ou impossível de compreender — daí a necessidade de algoritmos de leiaute (circulares ou dirigidos por força) combinados com o uso estratégico de **cor** e **tamanho** para evidenciar vértices centrais, comunidades e outras propriedades extraídas da rede nas unidades anteriores.

**Dica de estudo:** esta unidade é o "acabamento" de todo o curso — ela não ensina novas métricas, mas ensina a **comunicar visualmente** os resultados das Unidades 4, 5 e 6 (centralidade, comunidades) de forma acessível a não especialistas.

---

## Referências bibliográficas citadas nas unidades

- FACELI, K., LORENA, A. C., GAMA, J., ALMEIDA, T. A., CARVALHO, A. C. P. L. F. *Inteligência Artificial - Uma Abordagem de Aprendizado de Máquina.* 2ª ed. Rio de Janeiro: Editora LTC - Grupo GEN, 2021.
- GOLDBARG, M.; GOLDBARG, E. *Grafos: conceitos, algoritmos e aplicações.* Rio de Janeiro: Editora LTC - Grupo GEN, 2012.
- NETTO, P. O. B.; JURKIEWICZ, S. *Grafos: Introdução e prática.* São Paulo: Blucher, 2017.
- SIMÕES-PEREIRA, J. M. S. *Grafos e redes: teoria e algoritmos básicos.* Rio de Janeiro: Editora Interciência, 2013.
- HAGBERG, A. A.; SCHULT, D. A.; SWART, P. J. "Exploring network structure, dynamics, and function using NetworkX", Proceedings of the 7th Python in Science Conference (SciPy2008), 2008.
- BARABÁSI, A.; ALBERT, R. "Emergence of scaling in random networks." *Science*, v. 286, pp. 509-512, 1999.
- ERDÖS, P.; RÉNYI, A. "On random graphs." *Publicationes Mathematicae*, v. 6, pp. 290-297, 1959.
- WATTS, D. J.; STROGATZ, S. H. "Collective dynamics of small-world networks." *Nature*, 393, pp. 440–442, 1998.
- MILGRAM, S. "The small-world problem." *Psychology Today*, 1(1):61-67, 1967.
- FIGUEIREDO, D. R. "Introdução a Redes Complexas." Em: Atualizações em Informática 2011, PUC-Rio, Cap. 7, pp. 303-358, 2011.
- NEWMAN, M. E. J. "The structure and function of complex networks." *SIAM Review*, 45(23):167-228, 2003.
- WASSERMAN, S.; FAUST, K. *Social Network Analysis: Methods and Applications.* Cambridge University Press, 1994.
- ZINOVIEV, D. *Complex Network Analysis in Python.* Raleigh: The Pragmatic Bookshelf, 2018.
- FREEMAN, L. C. "Centrality in Social Networks Conceptual Clarification." *Social Networks*, v. 1, n. 1968, pp. 215-239, 1978.
- BRANDES, U. "A faster algorithm for betweenness centrality." *Journal of Mathematical Sociology*, 25(163): 163-177, 2001.
- BORASSI, M.; NATALE, E. "KADABRA is an adaptive algorithm for Betweenness via Random Approximation." *ACM Journal of Experimental Algorithms*, 24:2-18, 2016.
- GABARDO, A. C. *Análise de redes sociais: uma visão computacional.* São Paulo: Novatec, 2015.
- GOLDSCHMIDT, R.; PASSOS, E.; BEZERRA, E. *Data Mining: Conceitos, técnicas, algoritmos, orientações e aplicações.* 2ª ed. Rio de Janeiro: Editora LTC - Grupo GEN, 2015.
- GIRVAN, M.; NEWMAN, M. E. J. "Community structure in social and biological networks." *Proceedings of the National Academy of Sciences*, v. 99, n. 12, pp. 7821-7826, 2002.
- NEWMAN, M. E. J.; GIRVAN, M. "Finding and evaluating community structure in networks." *Physical Review E*, v. 69, n. 2, p. 026113, 2004.
- CLAUSET, A.; NEWMAN, M. E. J.; MOORE, C. "Finding community structure in very large networks." *Physical Review E*, v. 70, n. 6, p. 066111, 2004.
- BLONDEL, V. D.; GUILLAUME, J. L.; LAMBIOTTE, R.; LEFEBVRE, E. "Fast unfolding of communities in large networks." *Journal of Statistical Mechanics: Theory and Experiment*, v. 2008, n. 10, p. P10008, 2008.
- RAGHAVAN, U. N.; ALBERT, R.; KUMARA, S. "Near linear time algorithm to detect community structures in large-scale networks." *Physical Review E*, v. 76, n. 3, p. 036106, 2007.
- LÜ, L.; ZHOU, T. "Link prediction in complex networks: a survey." *Physica A: Statistical Mechanics and its Applications*, v. 390, n. 6, pp. 1150-1170, 2011.
- REBAZA, J. C. V. *Predição de links em redes complexas utilizando informações de estruturas de comunidades.* 2013. Dissertação (Mestrado em Ciências de Computação e Matemática Computacional) - ICMC, USP, São Carlos, 2013.
- COSTA, C. C. S. *Modelagem de algoritmos de distribuição espacial de grafos: uma extensão da UML para aplicações de visualização de redes sociais e complexas.* Dissertação (Mestrado) - SENAI CIMATEC, Salvador, 2017.
- JACOMY, M.; VENTURINI, T.; HEYMANN, S.; BASTIAN, M. "ForceAtlas2, a continuous graph layout algorithm for handy network visualization designed for the Gephi software." *PLoS one*, v. 9, n. 6, p. e98679, 2014.
- KOBOUROV, S. G. "Force-directed drawing algorithms." 2004.
- MARQUEZ, A. C.; GONÇALVES, B. B.; MEDEIROS, J. M. R.; REIS, N. A. *Gephi: um software open source de manipulação e visualização de grafos.* Oficina Gephi: Mapeando e analisando a vida das redes sociais, 2013.
- MAZZA, R. *Introduction to information visualization.* Springer Science & Business Media, 2009.
