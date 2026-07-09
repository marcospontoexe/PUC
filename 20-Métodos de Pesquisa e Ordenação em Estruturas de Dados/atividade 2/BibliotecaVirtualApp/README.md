# Documentação do Projeto — Biblioteca Virtual com Dijkstra

## 1. Visão Geral

O projeto **Biblioteca Virtual** é uma aplicação desenvolvida em Java com o objetivo de demonstrar, na prática, o uso de estruturas de dados e algoritmos clássicos estudados na disciplina de Métodos de Pesquisa e Ordenação.

O sistema permite:

- cadastrar livros;
- buscar livros;
- emprestar e devolver livros;
- controlar fila de espera;
- armazenar histórico de navegação;
- criar relações entre livros;
- gerar recomendações;
- calcular os livros mais próximos usando o algoritmo de Dijkstra.

O projeto utiliza diversas estruturas de dados importantes, como:

- LinkedList;
- Queue;
- Stack;
- HashMap;
- Set;
- Grafos.

Além disso, foi implementado o algoritmo de Dijkstra para encontrar os caminhos mais curtos entre livros relacionados.

---

# 2. Objetivo do Sistema

O objetivo principal do sistema é simular uma biblioteca digital inteligente capaz de recomendar livros relacionados com base em similaridade.

A ideia central é tratar cada livro como um vértice de um grafo.
As conexões entre livros representam relações como:

- mesmo autor;
- mesmo gênero;
- ano de publicação próximo;
- similaridade calculada.

Quanto menor a distância entre dois livros, maior a chance de serem boas recomendações.

---

# 3. Estrutura Geral do Projeto

O sistema é composto pelas seguintes classes principais:

| Classe | Responsabilidade |
|---|---|
| Livro | Representa um livro da biblioteca |
| Biblioteca | Contém toda a lógica do sistema |
| BibliotecaVirtualApp | Classe principal com menu interativo |
| TipoRelacao | Enumeração dos tipos de relação entre livros |

---

# 4. Classe Livro

A classe `Livro` representa a entidade principal do sistema.

## Principais atributos

```java
private String titulo;
private String autor;
private String genero;
private int ano;
private boolean emprestado;
```

## Responsabilidades

A classe é responsável por:

- armazenar informações do livro;
- controlar estado de empréstimo;
- fornecer métodos getters e setters;
- sobrescrever métodos como `equals()` e `hashCode()`.

## Importância do equals() e hashCode()

Esses métodos são fundamentais porque os livros são usados como chaves em estruturas HashMap.

Sem eles, o sistema não conseguiria:

- comparar livros corretamente;
- localizar livros no grafo;
- evitar duplicações;
- utilizar algoritmos de busca corretamente.

---

# 5. Enum TipoRelacao

A enumeração `TipoRelacao` define os tipos de conexões existentes entre livros.

## Exemplos

```java
MESMO_AUTOR
MESMO_GENERO
SIMILARIDADE
RECOMENDACAO
```

Essas relações ajudam na construção do grafo de recomendações.

---

# 6. Classe Biblioteca

A classe `Biblioteca` concentra toda a lógica do sistema.

Ela funciona como o núcleo da aplicação.

## Estruturas de dados utilizadas

### 6.1 LinkedList

```java
private LinkedList<Livro> livros;
```

Responsável por armazenar os livros cadastrados.

### Vantagens

- inserção simples;
- remoção eficiente;
- boa estrutura para listas dinâmicas.

---

### 6.2 Queue

```java
private Map<String, Queue<String>> filaEspera;
```

Usada para controlar fila de espera de empréstimos.

Segue a lógica FIFO:

- primeiro que entra;
- primeiro que sai.

### Exemplo prático

Se um livro já estiver emprestado:

1. o usuário entra na fila;
2. quando o livro é devolvido;
3. o próximo usuário recebe prioridade.

---

### 6.3 Stack

```java
private Stack<Livro> historico;
```

Armazena o histórico de livros pesquisados.

Segue a lógica LIFO:

- último pesquisado;
- primeiro recuperado.

---

### 6.4 Grafo

O sistema utiliza um grafo para representar relações entre livros.

```java
private HashMap<Livro,
    HashMap<TipoRelacao, Set<Livro>>> grafo;
```

## Estrutura do grafo

- cada livro é um vértice;
- cada relação é uma aresta;
- os conjuntos evitam duplicidade.

---

# 7. Construção das Relações Entre Livros

As relações são construídas automaticamente.

## Critérios usados

### Mesmo autor

Livros do mesmo autor recebem ligação.

### Mesmo gênero

Livros do mesmo gênero recebem ligação.

### Similaridade

A similaridade considera:

- gênero;
- autor;
- proximidade de ano.

Quanto maior a similaridade:

- menor será a distância entre os livros.

---

# 8. Algoritmo de Dijkstra

## Objetivo

O algoritmo de Dijkstra foi implementado para encontrar os livros mais próximos de um livro escolhido.

No contexto do projeto:

- cada livro representa um nó;
- cada relação representa uma conexão;
- cada conexão possui um peso;
- o algoritmo encontra os menores caminhos.

---

# 9. Funcionamento do Dijkstra no Projeto

## Ideia geral

O algoritmo começa em um livro de origem.

Depois:

1. visita os vizinhos;
2. calcula as menores distâncias;
3. atualiza os caminhos;
4. continua até visitar todos os livros possíveis.

---

# 10. Estruturas usadas no Dijkstra

## Mapa de distâncias

```java
Map<Livro, Integer> distancias
```

Armazena a menor distância conhecida até cada livro.

---

## Fila de prioridade

```java
PriorityQueue<Livro>
```

Seleciona sempre o livro com menor distância atual.

Isso melhora a eficiência do algoritmo.

---

## Mapa de predecessores

```java
Map<Livro, Livro> anteriores
```

Permite reconstruir o caminho encontrado.

---

# 11. Lógica Simplificada do Algoritmo

```java
1. Definir distância inicial como 0
2. Inserir livro inicial na fila
3. Enquanto existir item na fila:
    - remover menor distância
    - visitar vizinhos
    - calcular nova distância
    - atualizar menor caminho
4. Retornar distâncias
```

---

# 12. Exemplo Prático

Suponha os seguintes livros:

- Livro A
- Livro B
- Livro C

Relações:

- A → B = 1
- B → C = 2
- A → C = 5

O algoritmo escolherá:

```text
A → B → C
```

Pois:

```text
1 + 2 = 3
```

que é menor que:

```text
5
```

---

# 13. Funcionalidade de Recomendação

Após calcular as distâncias:

- os livros mais próximos são exibidos;
- livros com menor distância são considerados mais relevantes.

Isso transforma o sistema em uma biblioteca com recomendação inteligente.

---

# 14. Persistência em JSON

O sistema salva os dados em arquivos JSON.

## Objetivo

Permitir que os dados permaneçam salvos após encerrar o programa.

## Técnicas utilizadas

- Files.writeString()
- leitura de arquivos;
- regex simples para reconstrução.

---

# 15. Menu Interativo

A classe `BibliotecaVirtualApp` possui um menu textual.

## Funções disponíveis

- cadastrar livro;
- listar livros;
- buscar livro;
- emprestar livro;
- devolver livro;
- mostrar histórico;
- gerar recomendações;
- executar Dijkstra.

---

# 16. Complexidade do Algoritmo

## Dijkstra

### Complexidade média

```text
O((V + E) log V)
```

Onde:

- V = quantidade de livros;
- E = quantidade de relações.

---

# 17. Relação com os Conteúdos da Disciplina

O projeto aplica diretamente os conceitos estudados nas unidades.

| Conteúdo | Aplicação no projeto |
|---|---|
| Listas encadeadas | armazenamento de livros |
| Filas | fila de espera |
| Pilhas | histórico |
| Grafos | recomendações |
| HashMap | indexação |
| Busca | pesquisa de livros |
| Dijkstra | menor caminho |
| Ordenação | ranking de recomendações |

---

# 18. Pontos Fortes do Projeto

## Aplicação prática real

O sistema mostra como estruturas de dados são usadas em aplicações reais.

## Organização modular

Cada classe possui responsabilidade bem definida.

## Uso de múltiplas estruturas

O projeto demonstra integração entre várias estruturas diferentes.

## Recomendação inteligente

A implementação do grafo com Dijkstra torna o sistema mais sofisticado.

---

# 19. Conclusão

O projeto Biblioteca Virtual demonstra, de forma prática, como estruturas de dados e algoritmos podem ser integrados em uma aplicação funcional.

A utilização de listas, pilhas, filas, HashMaps, grafos e do algoritmo de Dijkstra transforma o sistema em uma aplicação inteligente capaz de:

- armazenar informações;
- organizar relacionamentos;
- realizar buscas eficientes;
- gerar recomendações relevantes.



