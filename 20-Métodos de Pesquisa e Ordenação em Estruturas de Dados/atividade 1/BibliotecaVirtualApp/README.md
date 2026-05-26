# Documentação do Sistema Biblioteca Virtual em Java

## Visão Geral

O sistema **Biblioteca Virtual** foi desenvolvido em Java utilizando diversas estruturas de dados clássicas para simular o funcionamento de uma biblioteca digital.

O projeto implementa:

* **LinkedList** → gerenciamento da coleção de livros
* **Queue (Fila)** → lista de espera de empréstimos
* **Stack (Pilha)** → histórico de navegação
* **HashMap + Set (Grafo)** → sistema de recomendação e relações entre livros
* **Serialização JSON** → persistência dos dados em arquivo

---

# Estruturas de Dados Utilizadas

## 1. LinkedList

### Objetivo

Armazenar os livros cadastrados na biblioteca.

### Implementação

```java
private LinkedList<Livro> livros = new LinkedList<>();
```

### Funcionamento

Cada elemento da lista representa um livro contendo:

* título
* autor
* gênero
* ano de publicação
* status de empréstimo

### Vantagens

* Inserção rápida
* Remoção eficiente
* Fácil navegação pelos elementos

---

# 2. Queue (Fila)

## Objetivo

Gerenciar listas de espera para livros emprestados.

### Implementação

```java
private Map<String, Queue<String>> filasEspera = new HashMap<>();
```

### Funcionamento

Quando um livro está emprestado:

1. Usuários entram na fila
2. O primeiro da fila recebe prioridade
3. A estrutura segue o padrão FIFO:

> First In, First Out

### Exemplo

```text
Fila:
João
Maria
Carlos
```

Ao devolver o livro:

* João recebe primeiro
* Depois Maria
* Depois Carlos

---

# 3. Stack (Pilha)

## Objetivo

Registrar o histórico de navegação do usuário.

### Implementação

```java
private Stack<Livro> historicoNavegacao = new Stack<>();
```

### Funcionamento

Sempre que um livro é pesquisado:

```java
historicoNavegacao.push(livro);
```

O livro fica no topo da pilha.

### Característica

A pilha segue o padrão:

> LIFO — Last In, First Out

O último livro visualizado é o primeiro a ser acessado.

---

# 4. Grafo com HashMap

## Objetivo

Criar relações entre livros.

### Estrutura

```java
private HashMap<Livro, HashMap<TipoRelacao, Set<Livro>>> grafoRelacoes;
```

---

# Representação do Grafo

Cada:

* Livro = nó
* Relação = aresta

Exemplo:

```text
Duna
 ├── SEMELHANCA → Fundação
 ├── MESMO_GENERO → Neuromancer
 └── RECOMENDADO → 1984
```

---

# Tipos de Relação

## Enum TipoRelacao

```java
enum TipoRelacao {
    SEMELHANCA,
    MESMO_GENERO,
    MESMO_AUTOR,
    RECOMENDADO
}
```

---

# Relações do Grafo

## 1. MESMO_GENERO

Livros do mesmo gênero.

Exemplo:

```text
Harry Potter → O Hobbit
```

---

## 2. MESMO_AUTOR

Livros do mesmo autor.

Exemplo:

```text
1984 → A Revolução dos Bichos
```

---

## 3. SEMELHANCA

Livros parecidos considerando:

* gênero
* autor
* proximidade de ano

### Cálculo de similaridade

```java
private int calcularSimilaridade(Livro a, Livro b)
```

Pontuação:

| Critério                 | Pontos |
| ------------------------ | ------ |
| Mesmo gênero             | +3     |
| Mesmo autor              | +2     |
| Até 5 anos de diferença  | +2     |
| Até 15 anos de diferença | +1     |

---

## 4. RECOMENDADO

Livros recomendados automaticamente com base na maior similaridade.

---

# Classe Livro

## Objetivo

Representar um livro da biblioteca.

### Atributos

```java
String titulo;
String autor;
String genero;
int anoPublicacao;
boolean emprestado;
```

---

# equals() e hashCode()

Esses métodos foram sobrescritos para permitir uso correto em:

* HashMap
* Set
* Grafo

### equals()

```java
@Override
public boolean equals(Object obj)
```

Compara livros pelo título.

---

### hashCode()

```java
@Override
public int hashCode()
```

Gera hash baseado no título.

---

# Persistência em JSON

## Objetivo

Salvar os livros em arquivo.

### Arquivo utilizado

```text
livros_biblioteca.json
```

---

# Salvamento

Método:

```java
salvarEmJson()
```

Converte os livros para JSON.

Exemplo:

```json
[
  {
    "titulo": "1984",
    "autor": "George Orwell",
    "genero": "Ficção Científica",
    "anoPublicacao": 1949,
    "emprestado": false
  }
]
```

---

# Carregamento

Método:

```java
carregarDeJson()
```

Executado na inicialização do sistema.

---

# Funcionalidades do Sistema

# 1. Cadastro de Livros

Permite inserir livros na LinkedList.

Validação:

* não permite títulos duplicados

---

# 2. Listagem de Livros

Mostra:

* título
* autor
* gênero
* ano
* status

---

# 3. Busca de Livros

Procura pelo título.

Além disso:

* registra no histórico da pilha

---

# 4. Remoção de Livros

Remove:

* da LinkedList
* do grafo
* das filas relacionadas

---

# 5. Listagem por Gênero

Filtra livros por gênero.

---

# 6. Empréstimo

Marca:

```java
livro.emprestado = true;
```

---

# 7. Devolução

Se houver fila:

* próximo usuário recebe automaticamente

Senão:

* livro volta a ficar disponível

---

# 8. Fila de Espera

Usuários entram na fila de um livro emprestado.

---

# 9. Histórico de Navegação

Mostra livros visualizados recentemente.

---

# 10. Relações do Grafo

Exibe:

* similaridades
* mesmo autor
* mesmo gênero
* recomendações

---

# 11. Recomendações

O sistema sugere livros automaticamente usando o grafo.

---

# Fluxo Geral do Sistema

```text
Usuário inicia sistema
        ↓
JSON é carregado
        ↓
Livros entram na LinkedList
        ↓
Grafo é reconstruído
        ↓
Usuário interage pelo menu
        ↓
Sistema atualiza:
- pilha
- fila
- grafo
- JSON
```

---

# Complexidade das Estruturas

| Estrutura  | Uso                        |
| ---------- | -------------------------- |
| LinkedList | coleção principal          |
| Queue      | fila de espera             |
| Stack      | histórico                  |
| HashMap    | grafo                      |
| Set        | evitar relações duplicadas |

---

# Conceitos de Estruturas de Dados Aplicados

O projeto demonstra na prática:

* listas encadeadas
* pilhas
* filas
* grafos
* hashing
* serialização
* persistência de dados
* recomendação por similaridade

---

# Possíveis Melhorias Futuras

## Banco de Dados

Substituir JSON por:

* MySQL
* PostgreSQL
* SQLite

---

## Interface Gráfica

Criar interface usando:

* JavaFX
* Swing

---

## Login de Usuários

Adicionar:

* autenticação
* permissões
* perfis

---

## API REST

Transformar o sistema em backend web.

---

# Conclusão

O projeto Biblioteca Virtual integra múltiplas estruturas de dados em um único sistema funcional.

O sistema demonstra:

* manipulação eficiente de dados
* persistência em JSON
* algoritmos de recomendação
* modelagem de relações usando grafos
* uso prático de estruturas fundamentais da computação

Além disso, o projeto serve como base para sistemas maiores e mais complexos, como plataformas reais de gerenciamento de bibliotecas digitais e recomendação de conteúdo.
