# Natural Language Toolkit - NLTK
Como o nome já diz, o NLTK é um toolkit para processamento de linguagem natural. Ele fornece várioas funcionalidades para criação de programas de PLN. O NLTK foi desenvolvido com 4 objetivos principais:

1. Simplicidade: Fornecer um framework intuitivo junto a substanciais blocos de construção, dotando os usuários de um conhecimento prático de PLN sem prender-se nas tediosas tarefas de "arrumação da casa" geralmente associadas com o processamento de dados linguísticos anotados.
2. Consistência: Fornecer um framework unificado com interfaces e estruturas de dados consistentes, e nomes de método facilmente conjecturáveis
3. Extensibilidade: Fornecer uma estrutura na qual novos módulos de software possam ser acomodados facilmente, incluindo implementações alternativas a abordagens diversas para uma mesma tarefa
4. Modularidade: Fornecer componentes que possam ser utilizados independentemente sem a necessidade de compreender o restante do toolkit

# Operações Básicas ou Pré-processamento
As operações a seguir geralmente fazem parte de uma etapa do PLN chamada de **Pré-processamento**, e já se tornaram triviais a todos programas de PLN, pois preparam o texto bruto para ser realmente processado e "entendido" pela máquina.

* Tokenização
* Segmentação de sentenças
* Normalização
* Stemming
* Lematização

## Tokenização
Serve para separar o texto em tokens - que são uma sequência de caracteres com algum significado semântico.

Principais dificuldades:

* "São Paulo" - uma ou duas palavras?
* "A seleção dos E.U.A. venceu." - Pontuação pode ser considerada quebra de sentença
* "Tromba d'água"
* "São João da Boa Vista"
* "Interação humano-computador"

```python
# Você deve importar o tokenizador da biblioteca NLTK
import nltk
from nltk import tokenize

# Caso não tenha feito o download de todos recursos do NLTK, você pode fazê-lo de maneira individual
#nltk.download('punkt')
#nltk.download('punkt_tab') # Download the specific resource for Portuguese
texto = "Um exemplo de texto para visualizarmos a técnica de tokenização."
# Tokeniza o texto
tokens = tokenize.word_tokenize(texto, language='portuguese')
'''
['Um',
 'exemplo',
 'de',
 'texto',
 'para',
 'visualizarmos',
 'a',
 'técnica',
 'de',
 'tokenização',
 '.']
'''
```

```python
# Usando funcionalidades básicas do Python
len(set(tokens))    # 10
```

```python
# Usando a biblioteca collections
from collections import Counter

contador = Counter(tokens)

for cont in contador.items():
  print(cont)
'''
('Um', 1)
('exemplo', 1)
('de', 2)
('texto', 1)
('para', 1)
('visualizarmos', 1)
('a', 1)
('técnica', 1)
('tokenização', 1)
('.', 1)
'''
```

```python
# Mostra os termos mais frequentes
contador.most_common(3) # [('de', 2), ('Um', 1), ('exemplo', 1)]
```

## Segmentação de sentenças
As regras principais de segmentação de sentenças contam com a divisão a partir de pontuações encontradas no texto ou quebras de linha.

![nltk-segmentacao-sentencas](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/nltk-segmentacao-sentencas.png)

```python
from nltk import sent_tokenize

texto = "Definição da sentença 1. Mais uma sentença. Última sentença."

sents = sent_tokenize(texto)    # ['Definição da sentença 1.', 'Mais uma sentença.', 'Última sentença.']
```

## Stemming
Reduz as palavras ao seu stem, retirando o sufixo. Faz com que palavras de mesmo significado semântico (ou similar) sejam escritas da mesma maneira (e.g., correr, correndo, correu). Geralmente o stem não é uma palavra válida.

```python
# Caso não tenha feito o download de todos recursos do NLTK, você pode fazê-lo de maneira individual
nltk.download('rslp')

# Inicia o Stemmer
stemmer = nltk.stem.RSLPStemmer()

print(stemmer.stem("ferro"))        # ferr
print(stemmer.stem("ferreiro"))      # ferr

print(stemmer.stem("correr"))       #corr
print(stemmer.stem("correu"))        #corr
```

```python
# Define uma função que faz Stemming em todo um texto
def Stemming(texto):
  stemmer = nltk.stem.RSLPStemmer()
  novotexto = []
  for token in texto:
    novotexto.append(stemmer.stem(token.lower()))
  return novotexto

texto1 = "Eu gostei de correr"
texto2 = "Eu gosto de corrida"

# Tokeniza o texto
tokens1 = tokenize.word_tokenize(texto1, language='portuguese')
tokens2 = tokenize.word_tokenize(texto2, language='portuguese')

novotexto1 = Stemming(tokens1)
novotexto2 = Stemming(tokens2)

print(novotexto1)   # ['eu', 'gost', 'de', 'corr']
print(novotexto2)   # ['eu', 'gost', 'de', 'corr']
```

## Lematização
Similar ao processo de Stemming, porém, faz uma análise morfológica completa para identificar e remover os sufixos. Geralmente leva os verbos ao infinitivo e substantivos/adjetivos ao masculino singular. Se diferencia do Stemming pois sempre gera uma palavra válida.

Infelizmente, esta funcionalidade não é suportada pelo NLTK.

Para nossa disciplina iremos utilizar o stemmer, caso queira saber um pouco mais sobre o impacto dessa decisão, você pode ler [este capítulo](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) do livro de Information Retrieval da Universidade de Stanford.

## Retirada de Stop-words
As vezes é necessário remover as palavras de maior ocorrência no conjunto de textos, pois geralmente elas não agregam grande valor semântico aos textos e não ajudam no processo de selecionar as informações relevantes ao sistema de PLN.

Este processo pode ser diferente, de acordo com a tarefa de PLN que você está executando, mas no geral temos duas abordagens: retirar as palavras de maior ocorrência levando em conta a [lei de Zipg](https://terrierteam.dcs.gla.ac.uk/publications/rtlo_DIRpaper.pdf), ou utilizar uma lista de stop-words pronta para seu idioma. Iremos realizar a segunda opção.

```python
# Caso não tenha feito o download de todos recursos do NLTK, você pode fazê-lo de maneira individual
nltk.download('stopwords')

# O NLTK fornece uma lista de stop-words para o idioma português
stopwords = nltk.corpus.stopwords.words('portuguese')   # recebe todas as stop words para o padrão protugues-br
```

```python
# Define uma função que remove as stop words de um texto
def removeStopWords(texto):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    novotexto = []
    for token in texto:
        if token.lower() not in stopwords:
            novotexto.append(token)
    return novotexto

texto = "Quais palavras serão retiradas deste texto? Eu não sei, mas este processo é necessário em alguns momentos."

# Tokeniza o texto
tokens = tokenize.word_tokenize(texto, language='portuguese')

novotexto = removeStopWords(tokens)

print(novotexto)    # ['Quais', 'palavras', 'retiradas', 'deste', 'texto', '?', 'sei', ',', 'processo', 'necessário', 'alguns', 'momentos', '.']
```

**IMPORTANTE**: Em alguns casos retirar as palavras referentes a negação (i.e., não) pode retirar um significado semântico muito importante do texto. Por exemplo, no texto: "O paciente não apresenta sintomas da doença". Neste caso a negação muda completamente o sentido da frase. Existem alguns outros casos (principalmente quando utilizamos Deep Learning) em que a retirada das stop-words pode ser prejudicial ao algoritmo, portanto, sempre teste seus algoritmos com e sem esta opção!

## Normalização
Além do Stemming, é possível realizar processos mais específicos de normalização do texto, de acordo com a tarefa.

* Exemplo 1: Para um algoritmo de Geração de fala, o texto bruto pode estar escrito como "Com os preços de R$ 100,00 para a primeira versão, e R$ 10,00 para a segunda". Para o meu algoritmo é mais interessante que o texto seja normalizado para: "Com os preços de cem reais para a primeira versão e dez reais para a segunda"

* Exemplo 2: Todas as datas serem normalizadas para um padrão único. As formas "18/mai", "dezoito de maio", "18-05" serem normalizadas para "18/05".

Pergunta rápida: Nos casos acima qual recurso nos ajudaria a fazer a normalização?

Uma maneira simples de normalizar o texto é transformar todas as letras em minúsculas, assim ocorrências escritas de maneira diferente são normalizadas para uma única. "Brasil", "BraSil" e "BRAsil" seriam normalizadas para "brasil".

```python
texto = "Se escreve LOL, LoL ou Lol?"

# Efetua lowercase
texto = texto.lower()

# Tokeniza o texto
tokenize.word_tokenize(texto, language='portuguese')        # ['se', 'escreve', 'lol', ',', 'lol', 'ou', 'lol', '?']
```

## Part-of-speech Tagging (POS-Tagging)
Esta também pode ser considerada uma das operações básicas de PLN, e tem por objetivo definir o valor morfológico de cada palavra no texto (e.g., substantivo, adjetivo, verbo, artigo, advérbio).

O objetivo da morfologia é estudar a estrutura interna e a variabilidade das palavras em uma língua, como conjugações verbais, plurais, nominalização, etc.

Ao contrário dos processos mostrados até agora, este depende do treinamento de um algoritmo supervisionado de *Machine Learning*, treinado a partir de **corpus anotado com as informações morfológicas de cada palavra**.
> **DEFINIÇÃO**: Um corpus anotado, é uma coleção de documentos etiquetada por humanos para identificar determinado valor morfológico, sintático ou semântico do texto.

No caso a seguir, estaremos trabalhando com um corpus anotado com informações morfológicas de palavras.

### Principais dificuldades
As principais dificuldades na realização deste processo são:

* Ambiguidade: uma mesma palavra pode ter papéis diferentes de acordo com o contexto (e.g., "Ele deu um parecer" - "O verbo parecer")
* Palavras fora do vocabulário: quando nosso corpus não contém alguma palavra, fica difícil para o POS-Tagger "adivinhar" o valor morfológico da palavra. Isso é especialmente comum quando utilizar um POS-Tagger treinado em um domínio em textos de algum domínio específico, por exemplo, utilizar um POS-Tagger treinado em textos jornalísticos para marcação de um texto de prontuários de pacientes.


# Similaridade Léxica
O conceito de similaridade textual é muito importante para diversas tarefas de PLN e existem diversos métodos de cálculo de similaridade. 

Existe uma série de diferentes cálculos/medidas que indicam a similaridade léxica entre palavras, as chamamos de string-based.

![similarity-measures](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/similarity-measures.png)

## Como a similaridade semântica difere da léxica?
Além dos diversos métodos de cálculo de similaridade léxica, devemos estar atentos ao conceito de similaridade semântica, que está mais associado ao significado das palavras do que à sua forma. 

## Levenshtein (edit) distance
A distância de Levenshtein entre duas palavras é o número mínimo de edições de um caractere (inserções, exclusões ou substituições) necessárias para alterar uma palavra pela outra. Usaremos para comparar PALAVRAS/TOKENS.

```python
import nltk

# Define 4 palavras diferentes
p1 = "padeiro"
p2 = "pandeiro"
p3 = "bombeiro"
p4 = "padaria"

nltk.edit_distance(p1, p2)  # 1
nltk.edit_distance(p1, p3)  # 4
nltk.edit_distance(p1, p4)  # 4
nltk.edit_distance(p3, p4)  # 7
```

## N-grams
O N-grams são basicamente um conjunto de caracteres/palavras co-ocorrentes em uma determinada janela de abertura. Usaremos tanto para comparar CARACTERES quanto PALAVRAS.

```python
import nltk
from nltk.util import ngrams

# Necessário pois utilizaremos o tokenizador
nltk.download('punkt_tab')

# Função para gerar n-grams de palavras a partir de uma sentença.
def extrair_ngrams_palavras(sent, n):
    n_grams = ngrams(nltk.word_tokenize(sent, language='portuguese'), n)
    return [ ' '.join(grams) for grams in n_grams]

texto = 'Esta é uma sentença para testarmos n-grams de palavras.'

print("1-gram: ", extrair_ngrams_palavras(texto, 1))  # 1-gram:  ['Esta', 'é', 'uma', 'sentença', 'para', 'testarmos', 'n-grams', 'de', 'palavras', '.']
print("2-gram: ", extrair_ngrams_palavras(texto, 2))   # 2-gram:  ['Esta é', 'é uma', 'uma sentença', 'sentença para', 'para testarmos', 'testarmos n-grams', 'n-grams de', 'de palavras', 'palavras .']
print("3-gram: ", extrair_ngrams_palavras(texto, 3))  # 3-gram:  ['Esta é uma', 'é uma sentença', 'uma sentença para', 'sentença para testarmos', 'para testarmos n-grams', 'testarmos n-grams de', 'n-grams de palavras', 'de palavras .']
print("4-gram: ", extrair_ngrams_palavras(texto, 4))  # 4-gram:  ['Esta é uma sentença', 'é uma sentença para', 'uma sentença para testarmos', 'sentença para testarmos n-grams', 'para testarmos n-grams de', 'testarmos n-grams de palavras', 'n-grams de palavras .']
```

**IMPORTANTE**: Mas quais seriam algumas das aplicações dos n-grams?

### 1) Reconhecimento de entidades / Chunking
Imagine que você tenha um corpus (conjunto de documentos) e visualize os seguintes n-grams:

1.   São Paulo (2-gram)
2.   processamento de linguagem natural (4-gram)
3.   o presidente alega que é inocente (6-gram)

Ao fazermos um levantamento de frequência, possivelmente os exemplos 1 e 2 ocorram com mais frequência no corpus. Agora se aplicarmos um modelo de probabilidade podemos **encontrar entidades** compostas por múltiplas palavras no texto.

### 2) Predição de palavras
Seguindo a mesma linha anterior, é possível também utilizar os n-grams para fazer **predições de palavras**. Por exemplo, se houver a sentença parcial "*Meu beatle favorito é*", a probabilidade da próxima palavra ser "*John*", "*Paul*", "*George*" ou "*Ringo*" é bem maior que o restante das palavras do vocabulário.

### 3) Correção ortográfica
A sentença "*beba vino*" poderia ser corrigida para "*beba vinho*" se você soubesse que a palavra "*vinho*" tem uma alta probabilidade de ocorrência após a palavra "*beba*". Além disso, a sobreposição de letras entre "*vino*" e "*vinho*" é alta (i.e., baixa distância de edição).

### 4) Similaridade léxica
Vamos extrair 2-grams de caracteres das duas palavras a seguir.

```python
p1 = "parar"
p2 = "parado"

# 4 bi-grams - 2 únicos
print("2-grams: ", extrair_ngrams_char(p1,2)) # 2-grams:  ['p a', 'a r', 'r a', 'a r']
# 5 bi-grams - 5 únicos
print("2-grams: ", extrair_ngrams_char(p2,2)) # 2-grams:  ['p a', 'a r', 'r a', 'a d', 'd o']
```

Para cálculo de similaridade utilizando n-grams usamos a fórmula: `S = 2C / A + B`

Onde:
* A é o número de n-grams únicos na primeira palavra
* B é o número de n-grams únicos na segunda palavra
* C é o número de n-grams únicos compartilhados
Portanto, neste exemplo o cálculo ficaria: S = 2 * 2 / 2 + 5 = 0.57

## Jaccard distance
A distância de Jaccard é definida como o tamanho da interseção dividida pelo tamanho da união de dois conjuntos. Usaremos tanto para comparar CARACTERES quanto PALAVRAS.

* Sentença 1: Eu gosto de fazer programas usando processamento de linguagem natural
* Sentença 2: Eu sei programar técnicas de processamento de linguagem natural

![jaccard-similarity](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/jaccard-similarity.png)

```python
w1 = set('tráfico')
w2 = set('tráfego')

nltk.jaccard_distance(w1, w2) # 0.4444444444444444
```

**IMPORTANTE**: Esta medida calcula a distância entre os dois termos, portanto quanto maior o valor, mais distantes (diferentes) são os termos!

**ATENÇÃO**: a função jaccard_distance() não aceita strings, você deve transformar sua entrada em set

```python
#Jaccard em PALAVRAS
s1 = 'Eu gosto de fazer programas usando processamento de linguagem natural'
s2 = 'Eu sei programar técnicas de processamento de linguagem natural'

# Tokeniza e transforma lista de tokens em set
s1_set = set(nltk.word_tokenize(s1, language='portuguese'))
s2_set = set(nltk.word_tokenize(s2, language='portuguese'))

nltk.jaccard_distance(s1_set, s2_set)   # 0.5833333333333334
```

# Similaridade semântica
A Similaridade semântica é medida através da semelhança de significado ou conteúdo semântico entre palavras/sentenças/documentos.

**WordNet** é a rede semântica mais popular na área de medir a similaridade knowledge-based; O WordNet é um grande banco de dados léxico, disponível em diversos idiomas. Substantivos, verbos, adjetivos e advérbios são agrupados em conjuntos de sinônimos cognitivos (synsets), cada um expressando um conceito distinto. 

O que é um **synset**? É um conjunto de sinônimos que compartilham um mesmo significado.
Os synsets são interligados por meio de relações conceitual-semânticas e léxicas.

Cada synset possui um ou mais **lemmas**, que representam um significado particular de uma palavra específica.

## Acessando o WordNet utilizando o NLTK
Infelizmente o NLTK ainda não dá suporte ao acesso direto a busca em algum grande WordNet em português (e.g., openWordnet-PT, WordNet.PT). Trabalharemos nossos exemplos em inglês e utilizando a versão em português contida no Open Multilingual Wordnet que o NLTK dá suporte.

```python
import nltk
from nltk.corpus import wordnet

# Obtém o(s) synset(s) para a palavra "pain" (dor)
syn = wordnet.synsets("pain")
# Imprime a definição
print(syn[0].definition())  # a symptom of some physical hurt or disorder
# Imprime exemplos de aplicação em uma frase
print(syn[0].examples())  # ['the patient developed severe pain and distension']
```

## Utilizando synsets e lemmas em português através do Open Multilingual Wordnet
```python
# Busca synsets em português
wordnet.synsets("cão", lang="por")

# Busca lemmas em português
wordnet.lemmas("cão", lang="por")
```

## Polissemias
A polissemia é a quantidade de sentidos/significados de uma palavra.

## Path Similarity (path)
Retorna uma pontuação indicando o quão semelhantes os sentidos de duas palavras são, com base no caminho mais curto que conecta os sentidos na taxonomia is-a (é-um) (Hiperonímia / Hiponímia). A pontuação está no intervalo de 0 a 1.

## Leacock-Chodorow Similarity (lch)
Similar ao anterior, porém utiliza também a profundidade máxima da taxonomia em que os sentidos ocorrem no cálculo.

## Leacock-Chodorow Similarity (lch)
Similar ao anterior, porém utiliza também a profundidade máxima da taxonomia em que os sentidos ocorrem no cálculo.

# Representação vetorial de textos
Hoje trabalharemos com um assunto essencial ao PLN moderno, a representação vetorial de textos. Nesta aula você realizará atividades práticas relacionadas a técnica chamada Bag of words (BoW)

## Bag of words (BoW)
É uma técnica de PLN na qual transformamos textos em **vetores numéricos** para **extrair características do texto**. Tais características podem ser interpretadas por diversos algoritmos, incluindo (principalmente) os de *Machine Learning*.

Apenas dois passos são necessários no algoritmo de BoW:
1.   Determinar o vocabulário do(s) texto(s)
2.   Realizar contagem do termos (frequência das palavras)

Imagine um corpus com os seguintes documentos:
*   *O menino correu*
*   *O menino correu do cão*
*   *O menino com o cão*

### 1) Determinar vocabulário
Para determinar o vocabulário, basta definirmos uma lista com todas palavras contidas em nosso corpus.
As palavras encontradas nos documentos acima são: `o`, `menino`, `correu`, `do`, `cão` e `com`

### 2) Contagem das palavras
Nesta etapa devemos contar quantas vezes cada palavra do vocabulário aparece em cada documento/texto, e criamos um vetor com as quantidades computadas.

![Tabela Bag of Words](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/table-bag-of-words.png)

Assim são gerados vetores individuais de cada documento:

*   *O menino correu*: `[1, 1, 1, 0, 0, 0]`
*   *O menino correu do cão*: `[1, 1, 1, 1, 1, 0]`
*   *O menino com o cão*: `[2, 1, 0, 0, 1, 0]`

**SACO DE PALAVRAS?** A técnica tem esse nome pois perde-se toda informação contextual do texto, ou seja, onde cada palavra apareceu em cada documento, como se pegássemos todas palavras e colocássemos dentro de um saco!

A matriz com as frequências das palavras também é chamada de **MATRIZ TERMO-DOCUMENTO**

**Mas, qual a ideia por trás do BoW?**

O BoW segue a ideia de que **documentos semelhantes terão contagens de palavras semelhantes** entre si. Em outras palavras, quanto mais semelhantes forem as palavras em dois documentos, mais semelhantes poderão ser os documentos.
Além disso, ao definir a matriz termo-documento, intui-se que **palavras com alta ocorrência em um documento, sejam importantes a ele**, ou seja, devem estar entre os temas centrais do texto.

**EXEMPLO**: Imagine os vetores a seguir:

![Tabela Bag of Words](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/table-bag-of-words-2.png)

O vetor do documento 1 e 2 são similares (assim como seus textos). Já o vetor do documento 3 se difere completamente.

### Utilizando o scikit-learn para calcular o BoW ou matriz termo-documento
Apesar de ser uma técnica simples de se implementar, não há necessidade, pois ela já é implementada dentro da biblioteca **scikit-learn** sob o nome de **CountVectorizer**

```python
from sklearn.feature_extraction.text import CountVectorizer

# Exemplo de corpus
corpus = ["o menino correu.", "o menino correu do cão.", "O Menino com o Cão."]

# Cria instância de CountVectorizer
vect = CountVectorizer()

# Transforma o corpus em vetores numéricos (BoW)
X = vect.fit_transform(corpus)    # <Compressed Sparse Row sparse matrix of dtype 'int64'	with 9 stored elements and shape (3, 5)>

# Imprime a ordem de cada coluna
print(vect.get_feature_names_out()) # ['com' 'correu' 'cão' 'do' 'menino']

# Imprime vetores (BoW)
print(X.toarray())
"""
[[0 1 0 0 1]
[0 1 1 1 1]
[1 0 1 0 1]]
"""
```

**ATENÇÃO**: O **CountVectorizer** já transforma as palavras em **lowercase** por padrão, ignora pontuação e coloca as palavras em **ordem alfabética** nos vetores. Além disso ignora palavras que tenham frequência abaixo ou acima dos parâmetros **min_df** e **max_df**.

É possível também vetorizar **N-Grams** do corpus usando o **CountVectorizer**, sem necessidade de usar alguma função extra. Geralmente o fazemos para obter mais contexto do texto.

```python
# Cria instância de CountVectorizer
# Apenas 2-grams serão gerados
vect = CountVectorizer( ngram_range=(2,2) )

# Transforma o corpus em vetores numéricos (BoW)
X = vect.fit_transform(corpus)  # <Compressed Sparse Row sparse matrix of dtype 'int64'	with 6 stored elements and shape (3, 5)>

# Imprime a ordem de cada coluna
print(vect.get_feature_names_out()) # ['com cão' 'correu do' 'do cão' 'menino com' 'menino correu']

# Imprime vetores (BoW)
print(X.toarray())
'''
[[0 0 0 0 1]
 [0 1 1 0 1]
 [1 0 0 1 0]]
'''
```

**DICA**: Vale a pena olhar a [**documentação**](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) do CountVectorizer, pois existem diversos parâmetros úteis que podemos utilizar.

### Limitações do BoW
Apesar das ideias de que documentos semelhantes terão contagens de palavras semelhantes entre si (ao aprender Classificação de Textos você poderá ver isso mais detalhadamente) e que uma palavra com alta frequência em um documento é considerada importante funcionarem em vários casos, o modelo BoW tem algumas limitações, entre elas:

* **Peso igual a todas palavras**: o BoW dá um peso igual a todas palavras. Em nosso exemplo palavras como "com" e "do", tem o mesmo peso de "cão" e "menino". Isso não é bom pois palavras mais comuns (artigos, preposições, etc) deveriam ter peso menor, pois são menos discriminantes.
* **Significado semântico**: a abordagem básica do BOW não considera o significado da palavra no documento. Ignora completamente o contexto em que é usado. A mesma palavra pode ser usada em vários locais com base no contexto ou nas palavras próximas (embora o uso de n-grams possa amenizar um pouco o problema do contexto).
* Tamanho do vetor - **maldição da dimensionalidade**: para um documento grande, o tamanho do vetor pode ser enorme, resultando em muito tempo de processamento e alto consumo de memória. Pode ser necessário ignorar as palavras com base na relevância do seu caso de uso.

### Aplicações do BoW
Ele é útil em qualquer tarefa em que a posição ou informação contextual do texto não é tão importante. Alguns exemplos são:

* Identificar o autor de um documento (classificação de textos)
* Agrupar documentos por tópicos (clusterização)
* Análise de sentimentos - identificar "positividade"/"negatividade" de um documento (regressão)

## TF-IDF
É uma medida estatística utilizada para avaliar a importância de uma palavra em um documento dentro de um corpus. A importância aumenta proporcionalmente ao número de vezes que uma palavra aparece no documento, mas é compensada pela frequência da palavra no corpus.

Mas o que quer dizer a sigla TF-IDF? TF-IDF é uma abreviação do inglês para **term frequency**–**inverse document frequency**, que significa frequência do termo–inverso da frequência nos documentos.

## Como Calcular?
O TF-IDF é composto por duas métricas. A primeira é calculada pela **frequência normalizada do termo** (TF), ou seja,o número de vezes que uma palavra aparece em um documento, dividido pelo número total de palavras nesse documento. A segunda é a **Frequência inversa de documentos** (IDF), calculada como o logaritmo do número de documentos no corpus dividido pelo número de documentos em que o termo específico aparece.

## TF (Term Frequency)
Mede a frequência com que um termo ocorre em um documento. Como todo documento tem tamanho diferente, é possível que um termo apareça muito mais vezes em documentos longos do que em documentos mais curtos. Assim, o termo frequência é geralmente dividido pelo tamanho do documento (também conhecido como número total de termos no documento) como forma de normalização.

`TF(t) = (número de ocorrências do termo t no documento) / (número total de termos no documento)`.

## IDF (Inverse Document Frequency)
Mede a importância de um termo no corpus. Ao calcular o TF, todos os termos são considerados igualmente importantes. No entanto, sabe-se que certos termos, como "é", "de" e "isso", podem aparecer muitas vezes, mas têm pouca importância. Portanto, precisamos diminuir o peso dos termos frequentes e aumentar dos raros.

`IDF(t) = log_e(número total de documentos / número de documentos com o termo t).`

## TF-IDF
Define a importância de uma palavra para um documento considerando todo corpus.

`TF-IDF(t) = TF(t) * IDF(t)`.

## Exemplo
Queremos calcular a importância da palavra "**carro**" em um documento contido em um corpus de 1 milhão de documentos.

A palavra aparece 5 vezes em um documento com 100 palavras, portanto seu TF pode ser calculado como:

`TF(carro) = 5 / 100 = 0.05`

Verificou-se que a palavra "carro" aparece em 500 documentos do corpus, portanto, para calcular seu IDF fazemos:

`IDF(carro) log_e(1000000 / 500) = 3.3`

E enfim, o TF-IDF desta palavra é o produto deste valores:

`TF-IDF(carro) = 0.05 * 3.3 = 0.16`

### **RESUMINDO**
O peso de um termo:

* aumenta quando t aparece muitas vezes em poucos documentos
* diminui quando t aparece em muitos documentos
* diminui quando t aparece poucas vezes no documento

### Intuição por trás do TF-IDF ( vs. Bag of words )
Uma das limitações do BoW é justamente o peso igual para todas palavras. Ao normalizar a frequência de um termo no documento e calcular a importância do termo para todo o corpus, resolvemos este grande problema da abordagem BoW.

## Utilizando o scikit-learn para calcular o TF-IDF

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# A seguir um corpus composto por resumos dos primeiros 12 capítulos do livro "Senhor dos Anéis"
# Traduzidos por Luciano Soares e Reinaldo Imrahil - disponível em: https://www.valinor.com.br/82
corpus = [
          "Capítulo 1: Uma festa muito esperada\nSessenta anos passaram desde que Bilbo Bolseiro, o herói de O Hobbit, tinha voltado de sua jornada. Ele é conhecido por muitos, tanto pela sua riqueza legendária como pelo fato de que a idade não parece afetá-lo. Ele anuncia uma grande celebração em honra do 111o aniversário dele e o 33o aniversário do seu sobrinho Frodo, que ele tinha adotado como herdeiro alguns anos atrás e trouxera para viver no Bolsão. A festa estava esplêndida, e um grande número de hobbits foi convidado. Mas Bilbo sentia-se estranho ultimamente, e decidiu que precisava de umas férias e deixaria o Condado; assim, depois de fazer um discurso depois do jantar, na frente dos 144 amigos mais íntimos dele e de Frodo, e também de seus parentes, ele coloca o anel mágico e desaparece, causando grande surpresa. Ele fala mais uma vez com Gandalf antes de partir, e quase muda a sua intenção original de deixar o anel com Frodo; mas o mago o convence a manter a idéia, e Bilbo parte, muito aliviado e mais feliz do que nunca. Gandalf adverte Frodo para não usar o anel. No dia seguinte Frodo está ocupado, pois Bilbo tinha deixado presentes de despedida para muitos hobbits, e agora uma multidão de pessoas se encontra no Bolsão, muitos deles cavando ao redor e procurando os tesouros imaginários de Bilbo. Gandalf parte, e não volta por muito tempo.",
          "Capítulo 2: A Sombra do Passado\nGandalf visita Frodo só algumas vezes pelos anos que seguem. Frodo se acostuma a ser o mestre do Bolsão, e faz amizade com alguns dos hobbits mais jovem [por exemplo com Peregrin Tûk e Merry Brandebuque] enquanto a maioria o considera esquisito, como Bilbo. Rumores de eventos estranhos fora do Condado surgem, como o da ascensão do Poder Escuro na Terra de Mordor, embora a maioria dos hobbits não acreditasse nisso. No qüinquagésimo ano da vida de Frodo, Gandalf o visita novamente e eles têm uma conversa longa sobre o anel que Frodo tinha herdado de Bilbo. Gandalf explica a Frodo a natureza e a história do anel, que é de fato o maior dos Anéis de Poder e foi feito há muito tempo por Sauron, o Senhor do Escuro de Mordor. Sauron o está procurando agora avidamente. Achando o anel o seu poder cresceria imensamente. O anel deveria ser destruído para que Sauron perdesse seu poder, mas só poderia ser destruído em Orodruin, a Montanha da Perdição em Mordor. Parece que Sauron já tinha ouvido falar de Bilbo e do Condado através de Gollum; assim, o Condado provavelmente não é mais um lugar seguro para Frodo. Ele decide partir, acompanhado por Sam Gamgi, o seu jovem jardineiro, que [ao contrário da maioria dos hobbits] acredita nas antigas histórias e adoraria ver os Elfos",
          "Capítulo 3: Três não é demais\nFrodo vende o Bolsão aos Sacola-Bolseiros e compra uma casa na Terra dos Buques, a leste do Condado, onde ele tinha passado sua infância. No seu qüinquagésimo aniversário, ele deixa o Bolsão e parte com seu amigo Pippin [Peregrin Tûk] e Sam Gamgi; Gandalf o deixou por algum tempo para procurar notícias do que acontecia na Terra-média, e ainda não voltou, o que preocupa muito Frodo. No dia seguinte, os três hobbits notam que estão sendo seguidos pelos misteriosos Cavaleiros Negros. Não sabem exatamente quem eles são, e Frodo, cuidadoso, decide não deixar que os Cavaleiros os vejam. Eles conhecem, durante a noite, um grupo vagante de Altos-elfos conduzido por Gildor Inglorion; Frodo fala por muito tempo com Gildor, e o elfo o aconselha a tentar alcançar Valfenda apesar da ausência de Gandalf, e conta-lhe que os Cavaleiros Negros são os perigosos Servos do Inimigo.",
          "Capítulo 4: Um atalho para cogumelos\nNo dia seguinte, Frodo decide pegar um atalho para o rio Brandevin, onde Merry deveria encontrá-los naquele dia; queriam chegar lá mais cedo, e evitar serem vistos novamente pelos Cavaleiros Negros. De fato, eles percebem que um dos Cavaleiros está na estrada e decidem sair dela. Depois de uma passagem longa e desagradável pelos bosques, eles alcançam a propriedade de Fazendeiro Magote, que é conhecido por soltar seus cachorros em qualquer invasor que venha a colher os seus cogumelos [como o próprio Frodo tinha experimentado na sua mocidade]. Contudo, ele é bastante amigável, especialmente por conhecer bastante Pippin; ele conta a Frodo e seus amigos que pouco tempo antes um cavaleiro negro estranho e amedrontador perguntara-lhe por um Bolseiro . Para ajudar Frodo a alcançar a balsa do Brandevin da maneira mais segura e rápida possível, Magote leva os três hobbits com sua carroça , e eles acham Merry esperando-os ansiosamente.",
          "Capítulo 5: Conspiração Desmascarada\nConforme eles cruzam o Rio, notam uma figura negra parada, e cada vez mais próxima. Eles vão para a casa nova de Frodo em Cricôncavo, e falam sobre as suas aventuras na viagem. Frodo pretende falar finalmente para os amigos que vai partir o mais cedo possível quando, para o seu assombro, eles dizem que já sabem sobre o Anel, e sobre o propósito de sua viagem, e que pretendem acompanhá-lo e ajudá-lo. Depois do choque inicial, Frodo aceita a ajuda deles alegremente, e eles decidem partir no dia seguinte, bem cedo, pela Floresta Velha, um lugar conhecido como esquisito e perigoso, para evitar as estradas que provavelmente serão vigiadas pelos Cavaleiros.",
          "Capítulo 6: A Floresta Velha\nOs hobbits entram na Floresta Velha e logo começam a sentir sua estranheza, como se as árvores estivessem vigiando-os e os odiassem. Eles chegam à Clareira onde os hobbits queimaram uma grande quantidade de árvores há muito tempo atrás. De lá, eles seguem um caminho que os conduz a uma colina que sobe fora da Floresta, e de lá, como eles eventualmente notam, para o Rio Withywindle, a parte central e mais estranha da floresta. Eles querem evitar isso e deixar o caminho, mas acham o terreno sempre mais difícil na direção em que gostariam de ir. Eles caem em um barranco que é muito íngreme para ser escalado novamente e, seguindo-o, chegam ao Withywindle e acham um caminho que corre ao longo dele. Este caminho os traz a um velho salgueiro, perto do qual começam a sentir-se sonolentos de repente. Frodo, Merry e Pippin dormem, e a árvore lança Frodo na água e captura Merry e Pippin debaixo de suas raízes. Sam e Frodo não podem salvá-los, e correm ao longo do caminho, enquanto pedem por ajuda, desesperados. Eles encontram Tom Bombadil, um homem estranho que canta canções absurdas. Tom canta a melodia certa, e o salgueiro liberta Merry e Pippin; então Tom convida os hobbits para irem à casa dele, onde vive com Fruta DOuro.",
          "Capítulo 7: Na Casa de Tom Bombadil\nEles comem um jantar magnífico e então vão dormir, e cada um deles tem sonhos diferentes e estranhos. No dia os hobbits falam com Tom Bombadil durante o dia inteiro. Tom lhes fala muito sobre a Floresta, os tipos de árvores e animais, o Velho Homem-Salgueiro, e a história antiga da Terra-média, embora de maneira enigmática. Para a surpresa deles, descobrem que o Anel não tem nenhum poder sobre Bombadil. Ele lhes dá conselhos no dia seguinte, e lhes ensina uma rima parra chamá-lo se eles precisarem da ajuda dele.",
          "Capítulo 8: Névoa nas Colinas dos Túmulos\nNo dia seguinte, os hobbits deixam a casa de Tom, pretendendo cruzar os Túmulos. Eles fazem um progresso bom pela manhã, e ao redor de meio-dia param para descansar. Estranhamente há um grande pedra fria que se levanta no topo plano de uma colina. Eles adormecem e são despertados por um pôr-do-sol cercado pela névoa. Eles imediatamente se encaminham na direção que eles acreditam ser a mais direta para a Estrada; algum tempo depois Frodo, que estava na frente, passa entre duas pedras paradas e nota que os outros se foram. Ele começa a gritar por ajuda, e é capturado por uma Criatura Tumular. Ele desperta novamente dentro de um túmulo, nota que os outros estão inconscientes perto dele e que uma mão está rastejando na direção deles. Frodo canta a rima que Tom Bombadil tinha lhes ensinado um dia antes, e realmente Tom vem muito rápido, e a luz do dia destrói a Criatura Tumular. Tom desperta os outros três hobbits, e dá a cada um deles uma espada, tirada dos tesouros que estavam dentro do túmulo. Ele também traz os pôneis deles que fugiram à noite, e os acompanha durante algum tempo, até as fronteiras das terras dele. Os hobbits partem, e chegam à aldeia de Bri pela noite.",
          "Capítulo 9: No Pônei Saltitante\nO hobbits entram no Pônei Saltitante, uma hospedaria grande em Bri. Um grupo diversificado de hóspedes já esta reunido lá: hobbits locais e homens, anões em viagem, homens estranhos do Sul, e um Guardião misterioso conhecido como Passolargo. Depois da ceia, Frodo, Sam e Pippin decidem unir-se aos hóspedes; Pippin chama a atenção contando uma história sobre o Prefeito do Condado e, empolgado, começa a contar sobre a festa de despedida de Bilbo. Frodo não quer mencionar o desaparecimento de Bilbo, e para interromper Pippin salta sobre uma mesa e começa a cantar e dançar. Ele salta e cai da mesa, e enquanto cai o Anel desliza para o dedo dele, e ele desaparece. Isto causa muita ansiedade, e apesar das explicações posteriores a maioria dos hóspedes deixa o aposento. Passolargo parece saber o real nome de Frodo, e a verdadeira causa do seu desaparecimento, e lhe pede que tenham uma conversa depois. Carrapicho, o estalajadeiro, também se lembra de algo e pede para ter uma conversa particular com Frodo.",
          "Capítulo 10: Passolargo\nPassolargo vai falar com Frodo, Sam e Pippin. Ele se oferece para ser o guia deles, e parece já saber muito de Frodo; porém, por causa da sua aparência, os hobbits não confiam nele. Então Carrapicho chega e explica que Gandalf tinha deixado uma carta para um certo Frodo Bolseiro, que Carrapicho esquecera de enviar ao Condado há vários meses atrás. Frodo e seus companheiros batem com a descrição que Gandalf dera a Carrapicho, e este dá a carta a Frodo. Entre outras coisas, essa carta contém um conselho de Gandalf para aceitar a ajuda de um amigo seu, um homem chamado Passolargo [com o verdadeiro nome Aragorn], se eles chegassem a conhecê-lo. Assim, Frodo decide aceitar a ajuda dele como um guia para Valfenda. Merry, que saiu para pegar um ar fresco antes, agora volta e conta que viu os Cavaleiros Negros, e parece que eles têm espiões em Bri. Eles decidem não ir para os quartos designados a eles, e dormem no quarto de hóspedes, depois de trancarem as janelas e a porta.",
          "Capítulo 11: Uma Faca no Escuro\nNaquela mesma noite, os Cavaleiros Negros arrombam a casa de Frodo em Cricôncavo, descobrem que Frodo não esta lá, e cavalgam para Bri com grande pressa. Eles arrombam a hospedaria, ou mais especificamente o quarto onde os hóspedes hobbits normalmente dormem. Os hobbits não são descobertos, mas todos os cavalos e pôneis da hospedaria fugiram com medo. No dia seguinte eles compram um pônei e mantimentos [muito mais do que eles poderiam carregar em suas costas]; eles vão em direção a Valfenda, e Passolargo os conduz pela floresta para uma colina chamada Topo do Vento, que oferece uma visão de cima de uma área circunvizinha bem grande. Parece que Gandalf tinha estado lá três dias antes deles. Naquela noite eles são atacados por cinco dos Cavaleiros em uma depressão debaixo do Topo do Vento; Frodo não consegue resistir ao desejo de colocar o Anel, e imediatamente depois de fazer isso percebe que ele pode ver os Cavaleiros muito claramente apesar da escuridão. O capitão dos Cavaleiros ataca Frodo, que o golpeia nos pés mas acaba ferido e perde a consciência .",
          "Capítulo 12: Fuga para o Vau\nPassolargo faz o melhor possível para curar Frodo, mas este só poderia receber o tratamento em Valfenda, que eles deveriam alcançar o mais cedo possível. Eles cruzam o Rio Fontegris e, evitando a estrada, caminham pelos ermos e acabam alcançando a região dos trolls onde Bilbo tivera a sua primeira aventura tantos anos atrás. Eles têm que cruzar uma linha de colinas para se pôr mais perto novamente da Estrada, já que a única esperança deles de alcançar Valfenda a tempo é seguir a Estrada que cruza o rio Ruidoságua, ou Bruinen, no vau de Bruinen. Na Estrada eles conhecem Glorfindel, um Senhor Élfico que foi enviado de Valfenda para achá-los e ajudá-los. Eles se aproximam do Vau de Bruinen e são emboscados pelos Cavaleiros Negros. Frodo consegue escapar e cruzar o rio no cavalo de Glorfindel. Então uma grande inundação vem rio abaixo e leva os Cavaleiros."
]

# Cria instância
vect = TfidfVectorizer()

X = vect.fit_transform(corpus)  # <Compressed Sparse Row sparse matrix of dtype 'float64'	with 1312 stored elements and shape (12, 716)>

print(vect.get_feature_names_out())

print(X.toarray())
```

### Analisando pesos de cada documento
```python
import pandas as pd

# Pega o vetor do primeiro documento
primeiroDocVec = X[0]

# Mostra os valores em um Dataframe do pandas
pd.set_option('display.max_rows', None)
df = pd.DataFrame(primeiroDocVec.T.todense(), index=vect.get_feature_names_out(), columns=["tfidf"])
df.sort_values(by=["tfidf"],ascending=False)
```

DICA: Vale a pena olhar a [documentação do TfidfVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html), pois existem diversos parâmetros úteis que podemos utilizar.

## **Limitações do TF-IDF**
Apesar do bom funcionamento em diversos cenários e tarefas de PLN, o TF-IDF tem algumas limitações de uso, entre elas:

* Baseia-se exclusivamente em evidências de frequência como evidência de similaridade/importância, portanto, **não captura semântica ou posição de palavras**
* Pode ter queda de performance de execução em grandes vocabulários (**maldição da dimensionalidade**)

## **Aplicações do TF-IDF**
A seguir alguns exemplos em que podemos usar o TF-IDF:

* **Recuperação de Informação**: sua principal funcionalidade é voltada para mecanismos de busca, pois consegue encontrar os resultado mais relevantes. e.g., imagine que você busque pela palavra "programação", basta você obter os documentos onde esta palavra tem uma pontuação TF-IDF mais alta.
* **Extração de palavras-chave**: você pode utilizar as palavras com maior pontuação TF-IDF de um documento como palavras-chave (*keywords*) que representam aquele documento.
* **Sumarização de textos**: podemos extrair sentenças que possuam palavras com as maiores pontuações TF-IDF seguindo a intuição de que ela representam melhor os temas centrais do texto, portanto podem ser utilizadas na construção de um sumário (resumo) do texto.
---
# Classificação de textos
## Processamento de Linguagem Natural
Nesta aula trabalharemos com Classificação de textos. Neste momento teremos nosso primeiro contato com técnicas de Machine Learning ou Aprendizagem de Máquina, que são algoritmos responsáveis por "ensinar" a máquina a realizar tarefas, sem que o programador tenha que explicitamente explicar as regras de funcionamento.

O objetivo é que ao final desta aula você:

1. Entenda o que é a Machine Learning
2. Saiba utilizar um algoritmo de classificação simples baseado em aprendizado supervisionado
3. Compreenda e aplique um pipeline simples de coleta/organização dos dados, treinamento, predição e avaliação para textos

NÃO está no escopo desta aula:

1. Explicar especificidades e o porquê da escolha dos classificadores utilizados
2. Detalhar diferenças entre algoritmos de Machine Learning
3. Utilizar classificadores para dados que não sejam textuais
4. Trabalhar com aprendizado não-supervisionado
5. Apresentar técnicas de Redes Neurais e Deep Learning

## O que é Machine Learning?
É uma área da Inteligência Artificial que provê a sistemas a habilidade de automaticamente aprender tarefas sem que seja explicitamente programada para tal.

**Mas, quando usar?**
Qualquer tarefa computacional em que não seja factível explicitamente definir regras de funcionamento ou que esta programação demande muito tempo, o Machine Learning (ML) pode ser aplicado.

Por exemplo, eu gostaria que meu sistema receba uma imagem e diga o nome dos objetos encontrados. Seria humanamente impossível criar regras de reconhecimento de padrões para todos objetos existentes. O ML seria capaz de tentar compreender estas imagens e automaticamente generalizar estes padrões.

## Aprendizado Supervisionado vs. Não Supervisionado
Existem duas maneiras principais de se trabalhar com ML.

A primeira delas é o **Aprendizado Supervisionado**, onde um humano gera uma base de dados rotulada para ensinar o algoritmo como executar a tarefa. Estes dados são inputados ao classificador que "aprende" a fazer a mesma rotulação, e é capaz de predizer os valores para novos dados. Por exemplo, eu gostaria que meu sistema recebesse um texto e diga qual o sentimento associado a este texto (alegria, tristeza, neutro). Neste caso um humano prepara uma base de dados com vários textos, associando os sentimentos a cada um deles. Assim, esta base de dados pode ser utilizada para treinar do algoritmo de ML para realizar a mesma tarefa quuando receber novos textos.

Uma outra maneira é o Aprendizado **Não-supervisionado** (ou clusterização), onde o algoritmo não precisa de dados para descobrir padrões ou encontrar clusters de informações de dados. Por exemplo, ao receber uma coleção de textos o algoritmo é capaz de categorizá-los (e.g., esportes, política, entretenimento).

Nós iremos aqui abordar apenas alguns algoritmos de classificação associados ao aprendizado supervisionado.

![ml-supervised-unsupervised](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/ml-supervised-unsupervised.png)

## Etapas de desenvolvimento
Assim como todas tarefas de PLN, aqui também se faz necessária a etapa de obtenção e organização (**pré-processamento**) dos dados.

Para o aprendizado supervisionado é preciso criar uma **base de dados rotulada** com uma série de **features** (atributos) que possam ajudar o algoritmo a encontrar padrões.

Então esta base é inputada ao classificador, que aprende a generalizar a tarefa, e **predizer valores para novos dados**.

Ao final, temos a etapa de **avaliação de nosso classificador**.

![ml-workflow](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/ml-workflow.png)

### Exemplos de aplicação de ML para textos
O ML é capaz de lidar com todos tipos de dados, numéricos ou textuais, contínuos ou categóricos. Para a disciplina de PLN é óbvio que focaremos apenas em **dados textuais**.

Diversos são os exemplos de aplicação de ML para classificação de textos, entre eles:

1. Análise de Sentimentos em redes sociais
2. Detecção de SPAM
3. Categorização de mensagens de consumidores
4. Topificação de artigos de notícias
6. Codificação de doenças em prontuários do paciente

## Classificação de documentos
Iremos aqui classificar uma série de documentos provindos de notícias escritas em inglês. A ideia é que o algoritmo receba uma notícia e saiba dizer a qual categoria ela pertence.

Para tal iremos treinar o algoritmo utilizando uma base de dados rotulada (corpus anotado), que contém o texto da notícia e sua categoria.

Vamos também utilizar alguns classificadores de Machine Learning condizentes com a tarefa.

### Dados
A aquisição de dados geralmente é a pedra no sapato de todo cientista de dados, principalmente se tratando de aprendizado supervisionado, onde os dados "crus" não servem, precisamos que eles sejam rotulados.

Muitas vezes este processo é manual e toma muito tempo, portanto é de suma importância sempre tentarmos averiguar se já não existe algum corpus anotado disponível para a tarefa que queremos realizar. 

Para este exemplo iremos trabalhar com a base de dados ["20 Newsgroup"](http://qwone.com/~jason/20Newsgroups/), disponível na biblioteca sklearn, e já utilizada em nosso exemplo de Modelagem de tópicos. Este corpus tem aproximadamente 20,000 documentos, separados em 20 categorias.

```py
# O sklearn inclusive já disponibiliza uma sub-divisão pré-definida desse corpus. 
# Assim você utiliza uma parte dele para TREINAR seu classificador e outra para TESTAR
from sklearn.datasets import fetch_20newsgroups

# Obtém base de treinamento, embaralhada e utilizamos random_state para resultado sempre ser o mesmo
corpus_treinamento = fetch_20newsgroups(subset='train', shuffle=True, random_state=1)

# Vamos visualizar as categorias do corpus
print(corpus_treinamento.target_names) 
'''
['alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 'comp.sys.mac.hardware',
 'comp.windows.x',
 'misc.forsale',
 'rec.autos',
 'rec.motorcycles',
 'rec.sport.baseball',
 'rec.sport.hockey',
 'sci.crypt',
 'sci.electronics',
 'sci.med',
 'sci.space',
 'soc.religion.christian',
 'talk.politics.guns',
 'talk.politics.mideast',
 'talk.politics.misc',
 'talk.religion.misc']
'''

# Tamanho da base de treinamento - quantidade de documentos (instâncias)
len(corpus_treinamento.data) # 11314

# Mostra uma das instâncias do corpus
corpus_treinamento.data[600]

# Podemos visualizar melhor sem as quebras de linha
corpus_treinamento.data[600].split("\n")

```

**PERGUNTA**: OK, mas o classificador de Machine Learning não "entende" texto, então como podemos transformar o dado textual em números?

### Extração de atributos (feature extraction)
Neste caso, podemos extrair atributos do texto, usando as técnicas de Representação Vetorial de textos que vimos am aulas anteriores.

#### Bag of Words (BoW)
```py
from sklearn.feature_extraction.text import CountVectorizer

# Transforma o texto em um vetor (NxM) - matriz termo-documento
# Onde "N" é o número de documentos na base de treinamento
# E o "M" é o tamanho do vocabulário
bow = CountVectorizer()
X_train_bow = bow.fit_transform(corpus_treinamento.data)
X_train_bow.shape # (11314, 130107)

# Vamos visualizar algumas colunas da matriz termo-documento (vocabulário)
bow.get_feature_names_out()[0:10]

bow.get_feature_names_out()[100000:100010]

bow.get_feature_names_out()[50000:50010]
```

OBSERVAÇÃO: Podemos verificar que além de termos um vocabulário grande, temos muitas palavras que não talvez não agreguem valor semântico ao texto - vamos cuidar disso mais tarde...

#### TF-IDF
```py
# Visto que já temos o BoW, não precisamos do TfidfVectorizer, podemos utilizar o TfidfTransformer
from sklearn.feature_extraction.text import TfidfTransformer

# Transforma nosso BoW (matriz termo-documento) em um vetor contendo os pesos calculados para cada palavras (NxM)
# Onde "N" é o número de documentos na base de treinamento
# E o "M" é o tamanho do vocabulário
tfidf = TfidfTransformer()
X_train_tfidf = tfidf.fit_transform(X_train_bow)
X_train_tfidf.shape   # (11314, 130107)

# Temos uma matriz de mesmo tamanho, porém agora com valores decimais referentes aos pesos calculados e não apenas valores INTEIROS de frequência
```

**PRÓXIMO PASSO**: Já temos o texto transformado em atributos numéricos, e também sabemos a qual categoria (classe) cada documento pertence. Agora podemos treinar os classificadores de Machine Learning.

### Classificador 1: Naive Bayes
TREINAMENTO: 

```py
# Perceba que a biblioteca sklearn dispõe de vários classificadores
from sklearn.naive_bayes import MultinomialNB

# Treina o classificador de Naive Bayes
# Passamos por parâmetro:
#    1) matriz NxM contendo os pesos de cada palavra para cada documento
#    2) vetor Nx1 contendo a classe/categoria de cada documento
clf = MultinomialNB().fit(X_train_tfidf, corpus_treinamento.target)
```

**OBSERVAÇÃO**: É possível com menos linhas de código fazer toda etapa de extração de atributos e treinamento, basta usar o método [Pipeline](https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html) do sklearn. Outra vantagem deste método é que você não precisa explicitamente vetorizar a base de teste depois.

```py
from sklearn.pipeline import Pipeline

text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB())])

text_clf = text_clf.fit(corpus_treinamento.data, corpus_treinamento.target)
```

**Avaliação de Performance**:

```py
# Obtém trecho de teste do corpus
corpus_teste = fetch_20newsgroups(subset='test', shuffle=True, random_state=1)

# Tamanho do corpus de teste
len(corpus_teste.data)  # 7532

# Pede para o classificador tentar predizer toda base de teste
# Como usamos pipeline, ele irá primeiro aplicar o BoW, depois o TF-IDF e somente depois tentará predizer
predicted = text_clf.predict(corpus_teste.data)

from sklearn.metrics import accuracy_score

# Podemos imprimir de maneira bem simples a acurácia, ao comparar o vetor de valores preditos e o vetor com os valores rotulados da base de dados
print("Acurácia: ",accuracy_score(predicted, corpus_teste.target))    # Acurácia:  0.7738980350504514

from sklearn.metrics import classification_report

# Podemos também imprimir um relatório completo de várias métricas, não apenas a acurácia
print(classification_report(corpus_teste.target, predicted, target_names=corpus_teste.target_names))

from sklearn.metrics import confusion_matrix

# Podemos imprimir a matriz de confusão para tentar entender melhor os resultados
mat = confusion_matrix(corpus_teste.target, predicted)

print(mat)

```

A visualização não ficou muito boa, vamos utilizar a biblioteca seaborn para plotar de maneira mais agradável, em forma de heatmap e com o nome das categorias

```py
%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

fig, ax = plt.subplots(figsize=(10,10)) 
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=corpus_treinamento.target_names, yticklabels=corpus_treinamento.target_names )
plt.xlabel('Categoria verdadeira')
plt.ylabel('Categoria predita');
```

Aparentemente os tópicos que envolvem religião e política foram os que tiveram mais erros durante a classificação.

### Classificador 2: SVM
Treinamento:
```py
from sklearn.linear_model import SGDClassifier

text_clf_svm = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()),
                         ('clf-svm', SGDClassifier(loss='hinge', penalty='l2',alpha=1e-3, max_iter=5, random_state=42))])

text_clf_svm = text_clf_svm.fit(corpus_treinamento.data, corpus_treinamento.target)
predicted_svm = text_clf_svm.predict(corpus_teste.data)
```

Avaliação de Performance:

```py
print(classification_report(corpus_teste.target, predicted_svm, target_names=corpus_teste.target_names))
```

VEJA: O classificador SVM melhorou os resultados!

### Predizendo categorias de textos fora do corpus
O mais legal de um algoritmo de Machine Learning é que uma vez o modelo treinado, você pode utilizá-lo para predizer a categoria de qualquer novo texto que você queira.

Vamos construir uma função para isso!

```py
def predizer_categoria(texto):
    """Predicts the category of a given text using the trained SVM classifier."""
    predicted = text_clf_svm.predict([texto])
    return corpus_teste.target_names[predicted[0]]
    
predizer_categoria('NASA sent a payload to the ISS') # sci.space
predizer_categoria('The best screen resolution for image editing is 1920x1080') # comp.graphics
predizer_categoria('The president must make a statement about the incident')  # predizer_categoria('The president must make a statement about the incident')
```

### Considerações finais
Os resultados obtidos acima são preliminares, visto que não fizemos nenhuma intervenção visando a melhoria dos mesmos. A maior parte dos erros ficaram em categorias que já são naturalmente confusas como cristianismo vs religião.

Poderiamos explorar técnicas de Pré-processamento (e.g., stop-words, stemming) e analisar os resultados, visando obter melhorias.

Como dito no início, existem diversos classificadores de Machine Learning, e cada um contém uma série de parâmetros configuráveis. Então como podemos ter certeza de qual classificador e quais parâmetros tem os melhores resultados para minha base de dados?

Para facilitar este processo, a biblioteca sklearn implementa um método chamado GridSearch, que automaticamente treina e testa diversas possibilidades de classificadores e parâmetros, visando encontrar a melhor combinação.

Por fim, utilizamos apenas dois tipos de Representação vetorial de palavras (Bow e TF-IDF). Poderíamos:

Explorar os parâmetros do CountVectorizer para retirar palavras com certa frequência, gerar n-grams, etc.
Gerar vetores numéricos provindos de modelos pré-treinados de Word Embeddings, e utilizá-los como atributos de treinamento (e.g., Tutorial 1, Tutorial 2).
