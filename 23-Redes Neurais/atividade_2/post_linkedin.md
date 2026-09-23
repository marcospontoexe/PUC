# Post do LinkedIn: target leakage numa atividade da faculdade

Texto puro, para colar direto no LinkedIn (não renderiza markdown).
Sem travessão. Imagem: `post_linkedin_leakage.png`.

---

Target leakage é quando a resposta que você está tentando prever já está escondida nos
dados de entrada. O modelo fica com uma métrica linda e não serve para nada.

Eu já tinha lido sobre isso. Só entendi de verdade quando aconteceu comigo, numa
atividade de redes neurais da faculdade.

A base tinha 37.967 veículos e eu precisava ajustar três regressões: cilindrada contra
eficiência, cilindrada contra emissão de CO2, e eficiência contra emissão de CO2.

As duas primeiras empacaram em R² de 0,64 e 0,66, mesmo com polinômio de ordem 10. A
terceira deu 0,987 já na ordem 4.

Fiquei desconfiado. Por que justamente essa daria tão certo?

Resolvi multiplicar as duas colunas só para ver no que dava. Eficiência em km/L vezes
emissão em g/km dá gramas de CO2 por litro de combustível. Rodei para os 37.967 veículos
e o resultado ficou todo amontoado em torno de 2.350.

Aí montei um histograma, e não era um amontoado só. Eram dois.

88,5% dos veículos ficaram em 2.347,7 g/L. Outros 2,6% ficaram em 2.689,6 g/L.

Fui atrás desses números. A EPA usa 8.887 gramas de CO2 por galão de gasolina queimada,
valor fixado num acordo com o Departamento de Transportes em 2010. Dividido por 3,785
litros, dá 2.347,7 g/L.

Exatamente o primeiro grupo. Quatro casas certas.

Para o diesel a EPA usa 10.180 g por galão, o que dá 2.689,3 g/L. O segundo grupo tinha
dado 2.689,6.

Fui olhar quais carros estavam nesse segundo grupo: Volkswagen Jetta, Golf, New Beetle,
picapes da Chevrolet e da GMC, Isuzu Pickup. Todos modelos com versão a diesel.

E na própria página da EPA está escrito que eles medem o consumo em testes de laboratório
e calculam o CO2 a partir disso. Não medem o escapamento.

Então a coluna que eu estava tentando prever era a minha variável de entrada dividindo
uma constante, com a constante trocando conforme o combustível. Não tinha modelo nenhum
ali. Era uma regra de três que já estava no dado desde o começo.

Para confirmar, testei a conta direta: CO2 = 2.354 dividido pela eficiência. Um
parâmetro só. Deu R² de 0,9884.

O polinômio de ordem 10, com onze coeficientes, deu 0,9886.

Na mesma atividade eu quase caí numa armadilha parecida.

A segunda parte pedia para prever a cotação do dólar com uma LSTM. Ajustei os
parâmetros, cheguei a R² de 0,92 no teste tendo começado com valor negativo, e fiquei bem
satisfeito comigo mesmo.

Antes de escrever a conclusão, testei a coisa mais boba que consegui pensar: chutar que a
cotação de amanhã é a de hoje. Sem treinar nada, sem modelo.

Deu R² de 0,9251.

A LSTM, com 101 parâmetros e 50 épocas de treinamento, deu 0,9280 na média de cinco
execuções. Ganho de 0,003. E no erro médio absoluto o chute ganhou, 0,0772 contra 0,0859.

Dá para ver o motivo no gráfico: a linha de previsão acompanha a real com um atraso de um
dia. A rede aprendeu a repetir o último valor, que é o melhor que dá para fazer quando a
variação do dia seguinte é quase ruído.

O QUE EU LEVO DAS DUAS

Quando a métrica vem melhor do que devia, vale parar e procurar o motivo antes de
comemorar. No meu caso bastou multiplicar duas colunas e olhar o resultado.

E em série temporal eu não apresento mais número nenhum sem comparar com "amanhã é igual
a hoje". É uma linha de código e derruba muito modelo bonito.

Nenhuma das duas coisas estava no enunciado da atividade.

Fonte do fator de emissão: EPA, Greenhouse Gas Emissions from a Typical Passenger Vehicle.

#MachineLearning #DataScience #RedesNeurais #Python

---

## Versão curta

Target leakage é quando a resposta que você quer prever já está escondida nos dados de
entrada. O modelo fica com uma métrica linda e não serve para nada.

Aconteceu comigo numa atividade da faculdade, com uma base de 37.967 veículos.

Das três regressões que eu precisava ajustar, duas empacaram em R² de 0,64 e 0,66, mesmo
com polinômio de ordem 10. A terceira, entre eficiência e emissão de CO2, deu 0,987.

Desconfiei e fui olhar. Multipliquei as duas colunas: eficiência (km/L) vezes emissão
(g/km) dá gramas de CO2 por litro. No histograma apareceram dois grupos bem definidos.

88,5% dos veículos em 2.347,7 g/L. Outros 2,6% em 2.689,6 g/L.

A EPA usa 8.887 g de CO2 por galão de gasolina, que dá 2.347,7 g/L. Para diesel usa
10.180, que dá 2.689,3. Os dois bateram. E os carros do segundo grupo eram Jetta, Golf,
New Beetle e picapes, todos com versão a diesel.

O CO2 dessa base não é medido, é calculado a partir do consumo. Eu estava prevendo minha
própria variável de entrada dividindo uma constante.

Testei a conta direta, CO2 = 2.354 dividido pela eficiência: um parâmetro só, R² de
0,9884. O polinômio de ordem 10, com onze coeficientes, deu 0,9886.

Quando a métrica vem melhor do que devia, vale procurar o motivo antes de comemorar.

#MachineLearning #DataScience #RedesNeurais

---

## Notas

**Fonte do fator de emissão, confirmada.** EPA, "Greenhouse Gas Emissions from a Typical
Passenger Vehicle": https://www.epa.gov/greenvehicles/greenhouse-gas-emissions-typical-passenger-vehicle

- O valor **8.887 g CO2 por galão de gasolina** foi fixado no rulemaking conjunto
  EPA/DOT de 7 de maio de 2010, que estabeleceu os padrões de economia de combustível
  para os modelos 2012 a 2016. Assume que todo o carbono da gasolina vira CO2.
- 8.887 / 3,785411784 = **2.347,7 g/L**.
- A mesma página afirma que a EPA e as montadoras medem economia de combustível e CO2 em
  testes padronizados de laboratório, e que o CO2 é derivado do consumo. **Isso confirma
  por documentação a inferência que eu tinha feito só pela estatística.**

**Demais números**, todos medidos sobre `base_veiculos_2.csv` e as séries do dólar desta
atividade: produto 2.353,8 ± 77,0 g/L (3,3%); R² 0,6429 / 0,6574 na ordem 10 para as duas
primeiras regressões; 0,9872 na ordem 4 e 0,9886 na ordem 10 para a terceira; hipérbole
de um parâmetro 0,9884; LSTM 0,9280 contra 0,9251 do preditor ingênuo, MAE 0,0859 contra
0,0772.

**O que ficou de fora, de propósito:**

- O ajuste de hiperparâmetros em si. É o que qualquer estudante faz numa atividade.
- Os bugs no código da disciplina. Criticar material de aula em público não demonstra
  habilidade e pega mal.
- O achado das duas redes competitivas chegarem à mesma partição (99,99% dos veículos no
  mesmo grupo, porque a distância euclidiana ignora o eixo de menor amplitude). É bom,
  mas diluiria a tese do post.
