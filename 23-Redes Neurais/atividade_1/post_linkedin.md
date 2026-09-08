# Post para o LinkedIn

Imagem para anexar: `post_linkedin_mlp_cnn.png` (1096x1315, formato retrato)

Observação sobre formatação: o LinkedIn não renderiza markdown. O texto abaixo já está
em texto puro, é só copiar e colar. Se quiser negrito nos títulos das seções, precisa
usar caracteres unicode em negrito (tem geradores online para isso).

---

Treinei duas redes para ler dígitos escritos à mão. As duas passaram de 97% de acurácia no teste do MNIST.

Aí mostrei pra elas dez dígitos que outra pessoa escreveu, fora da base. Uma acertou 4.

Três coisas que eu tirei desse experimento.


1) MAIS PARÂMETROS NÃO DEIXAM O MODELO MELHOR

A MLP tem 235 mil pesos. A CNN tem 225 mil, ou seja, menos. Mesmo assim a CNN acertou 8 dos 10 dígitos, contra 4 da MLP.

O motivo é estrutural. A MLP achata a imagem numa fila de 784 números, e nisso os pixels que eram vizinhos deixam de ser vizinhos: dois pontos que juntos formavam um traço vertical terminam a 28 posições de distância. A CNN não achata nada no começo, ela desliza filtros de 3x3 pela imagem inteira e reaproveita os mesmos 9 pesos em toda posição.

O detalhe que eu achei mais bonito: das convoluções da CNN saem só 18.816 pesos, 8% do modelo. É essa fatia pequena que faz o trabalho de enxergar. Todo o resto é a camada densa decidindo o que fazer com o que já foi extraído.


2) DATA AUGMENTATION COBRIU O QUE A ARQUITETURA NÃO COBRIA

Girei, desloquei e dei zoom aleatório nas imagens de treino. Nenhum peso a mais, nenhuma camada nova.

A MLP saltou de 4 para 9 acertos.

Só que a CNN sem ajuda nenhuma já entregava 8, gastando um quarto do tempo de treino que a MLP turbinada precisou. Dá pra resolver na arquitetura ou dá pra resolver no dado. Uma das rotas é bem mais barata.


3) O VALE QUE QUASE ME FEZ ESCREVER BESTEIRA

A CNN com augmentation apareceu com 98,02%, pior que os 98,69% que ela fazia sem augmentation. Não fazia sentido.

Eu quase escrevi "provavelmente são poucas épocas" e segui em frente. Resolvi medir: treinei 45 épocas registrando a acurácia em cada uma.

A época 15, onde eu tinha medido, era um vale. A 13 deu 98,60%, a 14 deu 98,40%, a 15 deu 98,02%, e a 16 já voltou pra 98,86%.

Não era o augmentation atrapalhando. Era eu lendo um ponto isolado de uma curva que oscila quase meio ponto percentual entre épocas vizinhas.

A correção preguiçosa seria trocar 15 por 32 na tabela, já que 32 foi o melhor ponto. Mas escolher a época olhando o conjunto de teste é vazar informação, mesmo que ninguém perceba. Então separei um conjunto de validação, liguei early stopping e deixei ele decidir.

Ele parou na época 32. Exatamente a mesma que eu tinha identificado espiando o teste, só que sem nunca olhar pra ele. E chegou a 99,31%.

Os dois modelos foram para 10 de 10 na caligrafia nova. Inclusive o dígito 6, que errou o notebook inteiro e sobre o qual eu já tinha escrito que só coletando dados novos daria pra resolver. Não era limite do dado. Era modelo parado no lugar errado.

Notebook completo, com o código e todos os resultados, no link nos comentários.

#MachineLearning #DeepLearning #ComputerVision #Python #TensorFlow #DataScience


---

## Versão curta (caso queira algo mais enxuto)

Treinei uma MLP e uma CNN pra ler dígitos escritos à mão. As duas passaram de 97% no teste do MNIST.

Mostrei dez dígitos escritos por outra pessoa, fora da base. A MLP acertou 4. A CNN acertou 8, com menos parâmetros que a MLP.

Aí veio a parte esquisita: quando liguei data augmentation na CNN, a acurácia CAIU de 98,69% para 98,02%.

Quase escrevi "devem ser poucas épocas" e segui em frente. Resolvi medir. Treinei 45 épocas anotando a acurácia em cada uma, e descobri que a época 15, onde eu tinha medido, era um vale da curva. A 16 já dava 98,86%.

Não era o augmentation. Era eu lendo um ponto isolado de uma curva que oscila.

Podia simplesmente trocar 15 por 32 na tabela, já que 32 era o melhor. Mas escolher a época olhando o teste é vazar informação. Separei validação, liguei early stopping, e ele parou sozinho na época 32. A mesma. Sem nunca ver o teste. 99,31% e 10 de 10 na caligrafia nova.

Se um número te surpreender, vale medir antes de escrever a explicação pra ele.

Notebook com o código nos comentários.

#MachineLearning #DeepLearning #Python #DataScience
