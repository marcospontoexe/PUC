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

![nltk-segmentacao-sentencas]