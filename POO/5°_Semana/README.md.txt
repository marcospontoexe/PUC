Um banco geralmente faz tipos diferentes de financiamento. Casas, apartamentos e terrenos possuem características diferentes e, naturalmente, regras diferentes. Agora será a hora de colocar tais regras em nosso projeto.

O que devo desenvolver?

1. Todos os requisitos das semanas anteriores.

2. Crie três subclasses para Financiamento:

	a. Casa:

		i. O banco inclui um valor do seguro obrigatório do financiamento para cada casa financiada. Portanto, inclua um valor adicional de R$ 80 para cada parcela.

		ii. Este valor de R$ 80 deve ser adicionado depois de ter calculado o valor de cada parcela com os juros. Ou seja: este valor adicional não substitui os juros, mas é uma taxa extra.

	b. Apartamento:

		i. De acordo com as regras do banco, todos os financiamentos de apartamentos deverão usar um sistema de amortização chamado PRICE. Este sistema já é usado por vários bancos.

		ii. Por isso, substitua a equação do cálculo do pagamento mensal para apartamentos. A nova fórmula deverá ser:

1. Vamos calcular primeiro a taxa mensal. Ela é: 
 
 

2. Vamos calcular o valor em meses do financiamento. Ela é: 

3. A nova fórmula será: 
 
 

c. Terreno:

i. Financiar terrenos possui um risco de inadimplência maior por parte dos compradores.

ii. Por isso, cada parcela precisa ter um acréscimo de 2% sobre o seu valor com os juros já incluídos previamente.

3. No método main() substitua os quatro financiamentos de financiamento por dois financiamentos de casa, dois financiamentos de apartamento e um de terreno.

a. Todos os financiamentos deverão permanecer em um único ArrayList.

b. Digitar todas as informações a cada teste é chato. Somente peça os dados do usuário para um financiamento.

c. Para os demais financiamentos você poderá informar os dados diretamente no código dentro do seu método main().

d. Mantenha ainda o texto que mostra a soma dos valores dos imóveis e a soma dos valores dos financiamentos.





Vamos ver um exemplo para que você possa entender melhor o enunciado, comparar e testar o seu código?

1. Imóvel de R$ 500.000,00, 10% de juros, 10 anos

a. Financiamento (lógica da semana 2):

i. (500000 / (10*12)) * (1 + (0,10 / 12)) = 4201,388...

b. Nova lógica para casa:

i. Financiamento + 80 = 4281,388...

c. Nova lógica para apartamento:

i. (500000 * (1 + (0,10 / 12) * (0,10 / 12)) ^ (10 * 12)) / ((1 + (0,10 / 12)) ^ (10 * 12) - 1) =  6607,537…

d. Nova lógica para terreno:

i. Financiamento * 1,02 = 4285,416...