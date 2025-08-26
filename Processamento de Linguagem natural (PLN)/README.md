# Natural Language Toolkit - NLTK
Como o nome já diz, o NLTK é um toolkit para processamento de linguagem natural. Ele fornece várioas funcionalidades para criação de programas de PLN. O NLTK foi desenvolvido com 4 objetivos principais:

1. Simplicidade: Fornecer um framework intuitivo junto a substanciais blocos de construção, dotando os usuários de um conhecimento prático de PLN sem prender-se nas tediosas tarefas de "arrumação da casa" geralmente associadas com o processamento de dados linguísticos anotados.
2. Consistência: Fornecer um framework unificado com interfaces e estruturas de dados consistentes, e nomes de método facilmente conjecturáveis
3. Extensibilidade: Fornecer uma estrutura na qual novos módulos de software possam ser acomodados facilmente, incluindo implementações alternativas a abordagens diversas para uma mesma tarefa
4. Modularidade: Fornecer componentes que possam ser utilizados independentemente sem a necessidade de compreender o restante do toolkit

## Operações Básicas ou Pré-processamento
As operações a seguir geralmente fazem parte de uma etapa do PLN chamada de **Pré-processamento**, e já se tornaram triviais a todos programas de PLN, pois preparam o texto bruto para ser realmente processado e "entendido" pela máquina.

* Tokenização
* Segmentação de sentenças
* Normalização
* Stemming
* Lematização

### Tokenização
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

### Segmentação de sentenças
As regras principais de segmentação de sentenças contam com a divisão a partir de pontuações encontradas no texto ou quebras de linha.

![nltk-segmentacao-sentencas](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/nltk-segmentacao-sentencas.png)

```python
from nltk import sent_tokenize

texto = "Definição da sentença 1. Mais uma sentença. Última sentença."

sents = sent_tokenize(texto)    # ['Definição da sentença 1.', 'Mais uma sentença.', 'Última sentença.']
```

### Stemming
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

### Lematização
Similar ao processo de Stemming, porém, faz uma análise morfológica completa para identificar e remover os sufixos. Geralmente leva os verbos ao infinitivo e substantivos/adjetivos ao masculino singular. Se diferencia do Stemming pois sempre gera uma palavra válida.

Infelizmente, esta funcionalidade não é suportada pelo NLTK.

Para nossa disciplina iremos utilizar o stemmer, caso queira saber um pouco mais sobre o impacto dessa decisão, você pode ler [este capítulo](https://nlp.stanford.edu/IR-book/html/htmledition/stemming-and-lemmatization-1.html) do livro de Information Retrieval da Universidade de Stanford.

### Retirada de Stop-words
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

### Normalização
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

### Part-of-speech Tagging (POS-Tagging)
Esta também pode ser considerada uma das operações básicas de PLN, e tem por objetivo definir o valor morfológico de cada palavra no texto (e.g., substantivo, adjetivo, verbo, artigo, advérbio).

O objetivo da morfologia é estudar a estrutura interna e a variabilidade das palavras em uma língua, como conjugações verbais, plurais, nominalização, etc.

Ao contrário dos processos mostrados até agora, este depende do treinamento de um algoritmo supervisionado de *Machine Learning*, treinado a partir de **corpus anotado com as informações morfológicas de cada palavra**.
> **DEFINIÇÃO**: Um corpus anotado, é uma coleção de documentos etiquetada por humanos para identificar determinado valor morfológico, sintático ou semântico do texto.

No caso a seguir, estaremos trabalhando com um corpus anotado com informações morfológicas de palavras.

#### Principais dificuldades
As principais dificuldades na realização deste processo são:

* Ambiguidade: uma mesma palavra pode ter papéis diferentes de acordo com o contexto (e.g., "Ele deu um parecer" - "O verbo parecer")
* Palavras fora do vocabulário: quando nosso corpus não contém alguma palavra, fica difícil para o POS-Tagger "adivinhar" o valor morfológico da palavra. Isso é especialmente comum quando utilizar um POS-Tagger treinado em um domínio em textos de algum domínio específico, por exemplo, utilizar um POS-Tagger treinado em textos jornalísticos para marcação de um texto de prontuários de pacientes.


## Similaridade Léxica
O conceito de similaridade textual é muito importante para diversas tarefas de PLN e existem diversos métodos de cálculo de similaridade. 

Existe uma série de diferentes cálculos/medidas que indicam a similaridade léxica entre palavras, as chamamos de string-based.

![similarity-measures](https://github.com/marcospontoexe/PUC/blob/main/Processamento%20de%20Linguagem%20natural%20(PLN)/imagens/similarity-measures.png)

### Como a similaridade semântica difere da léxica?
Além dos diversos métodos de cálculo de similaridade léxica, devemos estar atentos ao conceito de similaridade semântica, que está mais associado ao significado das palavras do que à sua forma. 

### Levenshtein (edit) distance
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

### N-grams
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

#### 1) Reconhecimento de entidades / Chunking
Imagine que você tenha um corpus (conjunto de documentos) e visualize os seguintes n-grams:

1.   São Paulo (2-gram)
2.   processamento de linguagem natural (4-gram)
3.   o presidente alega que é inocente (6-gram)

Ao fazermos um levantamento de frequência, possivelmente os exemplos 1 e 2 ocorram com mais frequência no corpus. Agora se aplicarmos um modelo de probabilidade podemos **encontrar entidades** compostas por múltiplas palavras no texto.

#### 2) Predição de palavras
Seguindo a mesma linha anterior, é possível também utilizar os n-grams para fazer **predições de palavras**. Por exemplo, se houver a sentença parcial "*Meu beatle favorito é*", a probabilidade da próxima palavra ser "*John*", "*Paul*", "*George*" ou "*Ringo*" é bem maior que o restante das palavras do vocabulário.

#### 3) Correção ortográfica
A sentença "*beba vino*" poderia ser corrigida para "*beba vinho*" se você soubesse que a palavra "*vinho*" tem uma alta probabilidade de ocorrência após a palavra "*beba*". Além disso, a sobreposição de letras entre "*vino*" e "*vinho*" é alta (i.e., baixa distância de edição).

#### 4) Similaridade léxica
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

### Jaccard distance
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

## Similaridade semântica
A Similaridade semântica é medida através da semelhança de significado ou conteúdo semântico entre palavras/sentenças/documentos.

**WordNet** é a rede semântica mais popular na área de medir a similaridade knowledge-based; O WordNet é um grande banco de dados léxico, disponível em diversos idiomas. Substantivos, verbos, adjetivos e advérbios são agrupados em conjuntos de sinônimos cognitivos (synsets), cada um expressando um conceito distinto. 

O que é um **synset**? É um conjunto de sinônimos que compartilham um mesmo significado.
Os synsets são interligados por meio de relações conceitual-semânticas e léxicas.

Cada synset possui um ou mais **lemmas**, que representam um significado particular de uma palavra específica.

### Acessando o WordNet utilizando o NLTK
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

### Utilizando synsets e lemmas em português através do Open Multilingual Wordnet
```python
# Busca synsets em português
wordnet.synsets("cão", lang="por")

# Busca lemmas em português
wordnet.lemmas("cão", lang="por")
```