# Notebook de portfólio e post do LinkedIn

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md).

## O notebook

[../atividade_1/mlp_vs_cnn_eficiencia.ipynb](../atividade_1/mlp_vs_cnn_eficiencia.ipynb), **já
executado com as saídas embutidas** (tabelas, gráficos e figuras aparecem sem precisar rodar).

**Objetivo declarado:** comparar a eficiência de MLP e CNN para imagens sob a ótica de quantidade de
parâmetros e taxa de acerto, com e sem data augmentation, num texto que prenda a atenção de
recrutadores de machine learning.

### Restrições de escrita pedidas pelo utilizador

1. **Nunca usar o caractere travessão** (U+2014). Verificado por script.
2. Escrever na voz do utilizador, sem soar como texto de modelo de linguagem.
3. Não afirmar nada sobre a origem demográfica da escrita do MNIST sem referência. O 7 cortado
   passou a ser descrito como "um jeito de escrever usado em vários países", e a inferência sobre
   sua raridade na base é apresentada explicitamente como suspeita levantada a partir do
   comportamento dos modelos.

### Diferença para os scripts da atividade

O notebook usa o **MNIST completo** (60k treino / 10k teste oficial) e caminho **relativo**
`RN/RN`, para ser portátil. Por isso **os números não batem** com os do relatório `.docx`.

### Bug de reprodutibilidade (importante, não repetir)

As camadas `RandomRotation/RandomTranslation/RandomZoom` eram criadas na avaliação do argumento,
portanto **antes** do `set_random_seed()` que roda dentro de `roda_experimento`. Elas herdavam a
semente do estado deixado pelo treino anterior, e os resultados mudavam a cada execução (variaram
de 8/10 para 7/10 e 9/10 entre rodadas).

**Correção:** passar a **função** `camadas_de_augmentation` (sem parênteses) e construir as camadas
dentro de `roda_experimento`, depois do reset, com `seed=` explícito em cada camada. Determinismo
verificado rodando a mesma configuração duas vezes e comparando previsões e soma dos pesos da
primeira convolução.

### Resultados (semente 42, MNIST completo)

| Modelo | Params | Épocas | Tempo | Perda | Acurácia MNIST | Conj.1 | Conj.2 |
|---|---|---|---|---|---|---|---|
| MLP | 235.146 | 15 | 29s | 0,0861 | 97,67% | 10/10 | 4/10 |
| CNN | 225.034 | 5 | 69s | 0,0389 | 98,69% | 10/10 | 8/10 |
| MLP + aug | 235.146 | 45 | 315s | 0,0588 | 98,20% | 10/10 | 9/10 |
| CNN + aug | 225.034 | 15 | 258s | 0,0608 | 98,02% | 10/10 | 9/10 |

**Achados centrais:** a CNN base (8/10, 69s) fica a um dígito da MLP com augmentation (9/10, 315s),
com menos parâmetros. Das convoluções da CNN saem só 18.816 pesos, 8% do modelo.

### A seção do vale, e a lição

O augmentation parecia ter **piorado** a acurácia da CNN (98,69% → 98,02%). Eu tinha escrito
"provavelmente é falta de treino" **sem testar**, e o utilizador questionou. Medido: treino de 45
épocas registrando a acurácia a cada uma. A época 15 caiu num **vale** (98,02%), com a 13 em 98,60%,
a 14 em 98,40% e a 16 já em 98,86%. O melhor ponto foi 99,25% na época 32.

Conclusão: o augmentation não piorou nada, eu tinha medido no pior ponto da vizinhança.

### A seção do early stopping

Implementa a verificação que o próprio texto propunha. Validação de 6 mil imagens separada do treino
(sobram 54 mil), `EarlyStopping` com `monitor="val_accuracy"`, `patience=10`,
`restore_best_weights=True`, teste intocado até o fim.

| Modelo | Época (chute) | Acurácia | Conj.2 | Época (early stop) | Acurácia | Conj.2 |
|---|---|---|---|---|---|---|
| MLP + aug | 45 | 98,20% | 9/10 | 23 | 98,08% | **10/10** |
| CNN + aug | 15 | 98,02% | 9/10 | **32** | **99,31%** | **10/10** |

**O achado que fecha o notebook:** o early stopping escolheu a época 32 para a CNN, exatamente a
mesma que a curva anterior tinha identificado como melhor **espiando o conjunto de teste**. A
validação chegou na mesma resposta sem nunca ver o teste.

### Correção na conclusão

A versão anterior afirmava que o dígito 6 era impossível para todos os modelos e que só coletando
dados novos daria para resolver. Os dois modelos com early stopping acertaram o 6 (10/10). A
conclusão foi reescrita registrando o erro: não era limite do dado, era modelo parado no lugar
errado.

### Outras correções aplicadas

`input_shape=` trocado por camada `Input()` explícita (eliminou UserWarning do Keras 3), removida
célula de código vazia no fim, e reordenada a seção de augmentation que aparecia depois do código
que já a usava.

## O post do LinkedIn

[../atividade_1/post_linkedin.md](../atividade_1/post_linkedin.md) (duas versões, longa e curta) e
[../atividade_1/post_linkedin_mlp_cnn.png](../atividade_1/post_linkedin_mlp_cnn.png) (1096×1315,
retrato). Script gerador: `imagem_post.py`, no scratchpad.

A imagem combina a tabela dos modelos com a curva de acurácia por época, destacando em vermelho a
época 15 (o vale) e em verde a época 32.

**Ajuste de terminologia:** o utilizador pediu para falar do "vale local do gradiente". Corrigi no
texto, porque o modelo não ficou preso em mínimo local — ele se recuperou sozinho na época seguinte.
É oscilação da curva de acurácia entre épocas, causada pelo ruído do SGD com augmentation. O post
usa "um vale da curva".

**Cuidado tomado:** a curva atinge 99,25% na época 32 (rodada sem separar validação, 60k de treino)
e a tabela mostra 99,31% (rodada com early stopping, 54k de treino). Para não parecer contradição na
mesma imagem, a anotação verde não repete o número, só aponta a época.

O LinkedIn não renderiza markdown, então o texto foi escrito em texto puro, com títulos de seção em
caixa alta.
