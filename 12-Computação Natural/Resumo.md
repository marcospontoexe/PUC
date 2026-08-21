# Computação natural

* **Algoritmos evolutivos** (biologia evolucionária)
* Redes neurais artificiais (sistema nervoso)
* **Sistemas de enxame** (comportamento social de insetos/animais)
* Sistemas imunológicos artificiais (imunocomputação)
* Geometria fractal (sistemas de funções interativas, sistemas L)
* **Vida artificial**
* **Computação de DNA**
* Computação quântica

## Algoritmos evolutivos
A computação evolutiva emula esse processo adaptativo — cria uma população inicial de soluções candidatas, avalia cada uma por uma função de fitness, e itera por gerações, mantendo as soluções mais aptas e introduzindo variação para explorar novas alternativas

* Algoritmos Genéticos
* Estratégias Evolucionárias
* Evolução Diferencial
* Programação Genética
* Programação Evolucionária.

### Algoritmos Genéticos
Algoritmos Baseados na Evolução e Seleção Natural

1. Seleção
* Seleção por roleta
* Amostragem universal estocástica
* Seleção por torneio

2. Cruzamento (crossover)
* Ponto único
* Dois pontos
* Uniforme

3.Mutação: Evento aleatório de baixa probabilidade 
* Troca de bit
* Troca (swap)
* Inversão

4. Elitismo: Técnica que evita perder os melhores indivíduos durante seleção/cruzamento/mutação

## Algoritmos de enxame
inspirados nos benefícios da vida em grupo.

* Algoritmo da Colônia de Abelhas Artificial (ABC): baseado em inteligência de enxame que simula como abelhas buscam alimento
* Otimização da Colônia de Formigas (ACO):  formigas liberam feromônios ao se deslocar, e outras formigas tendem a seguir trilhas com maior concentração desse rastro químico.

### Algoritmo da Colônia de Abelhas Artificial (ABC)

1. mover empregadas/espectadoras às fontes;
2. calcular o néctar (fitness);
3. selecionar batedoras e direcioná-las a novas fontes.
4. Fontes esgotadas têm sua exploração encerrada.
5. Abelhas batedoras são enviadas para buscar aleatoriamente novas fontes.
6. O algoritmo memoriza a melhor fonte (melhor solução) encontrada até o momento.

Regra de abandono: se uma solução não melhora após um número predeterminado de iterações, a fonte é abandonada e a abelha empregada correspondente vira batedora 

### Otimização da Colônia de Formigas (ACO)

Como surge a rota mais eficiente:
1. Novas formigas (soluções) são geradas globalmente.
2. O desempenho/fitness de cada uma é avaliado.
3. Os níveis de feromônio são ajustados: reforçados em áreas de solução promissora, enfraquecidos nas menos eficazes.
4. Se há melhoria, as formigas são direcionadas para essa região; senão, uma nova direção é escolhida aleatoriamente.
5. Atualização dos feromônios e evaporação (simulando o processo natural).

## Vida artificial
 síntese de fenômenos semelhantes à vida.


## Computação de DNA
Fundamenta-se em substituir microchips tradicionais por moléculas de DNA, explorando a capacidade das moléculas orgânicas de processar informação

## Sistemas imunológicos artificiais
sistemas imunológicos artificiais são qualquer sistema ou ferramenta computacional que usa ideias e metáforas do sistema imunológico biológico para resolver problemas

1. Modelagem do sistema imunológico para desenvolver/testar teorias sobre seu funcionamento.
2. Uso de metáforas imunológicas para criar algoritmos computacionais.

## Evolução diferencial
Assim como a maioria dos algoritmos evolutivos, é um otimizador baseado em populações que:

* Aborda o problema a partir de múltiplos pontos iniciais aleatórios, amostrando a função objetivo em cada um.
* Integra mutação, recombinação e seleção com base no fitness.
* Gera iterativamente soluções eficazes manipulando uma população de soluções.
* Diferencial: capacidade de autoadaptação durante a mutação, gerando diversidade na população 