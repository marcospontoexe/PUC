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


### Como a similaridade semântica difere da léxica?
Além dos diversos métodos de cálculo de similaridade léxica, devemos estar atentos ao conceito de similaridade semântica, que está mais associado ao significado das palavras do que à sua forma. 

