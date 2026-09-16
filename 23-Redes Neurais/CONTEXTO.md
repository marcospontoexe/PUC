# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-09-15 (sem hora registada)
- **Sessão nº:** 2 (continuação da 1, após compactação do contexto)
- **Status geral:** pronto para revisão

## 1. Objetivo da tarefa
Duas frentes de trabalho na disciplina "Redes Neurais" (PUCPR): (a) construir um resumo de
estudo detalhado e didático dos 8 PDFs da disciplina, expandido ao longo de várias perguntas
de aprofundamento do utilizador; (b) executar de fato a **Atividade Somativa 1**
(`atividade_1/`), treinando os modelos MLP e CNN fornecidos, ajustando seus parâmetros, e
preenchendo o relatório final em Word com os resultados obtidos.

## 2. Já feito ✅

### Frente A — Resumo de estudo (`Resumo.md`)
- Leitura integral dos 8 PDFs da disciplina (unidades 01 a 08) e criação do `Resumo.md`
  detalhado (mapa da disciplina, resumo por unidade, tabelas de síntese, glossário, 20
  perguntas de autoavaliação, referências).
- Múltiplas rodadas de aprofundamento a pedido do utilizador, todas incorporadas ao
  `Resumo.md` (numeração de seções ajustada a cada inserção — ver arquivo para o índice
  atual completo):
  - Unidade 02: seção sobre dropout/L1/L2/early stopping/validação cruzada/walk-forward;
    seção detalhada sobre a atualização de pesos por lote (forward pass, backprop,
    otimizador), com exemplo numérico de uma amostra individual atravessando a rede.
  - Unidade 03 (CNN): reescrita quase completa — motivação MLP-vs-CNN, mecânica da
    convolução passo a passo com exemplo numérico, padding/stride/fórmula de dimensão,
    canais e profundidade (com subseção dedicada "O que é um canal?"), pooling, flatten,
    arquitetura MNIST completa comentada (contagem de parâmetros), como o mapa de
    características é gerado (deslizamento 2D + múltiplos canais + múltiplos filtros),
    weight sharing/backprop dentro da convolução, e uma seção específica mostrando como a
    2ª convolução (64 filtros) processa os 32 mapas empilhados pela 1ª convolução.
- Nenhuma pendência nesta frente; o resumo cobre profundamente MLP, CNN e RNC (unidade 05,
  ver Frentes F e G). As unidades 06-08 (RNT e duplo treinamento) ainda estão apenas no
  nível do resumo original.

### Frente B — Atividade Somativa 1 (`atividade_1/`)
- Lida a orientação (`atividade_1/Orientação.pdf`) e extraído o texto do template Word
  (`atividade_1/Template_AtividadeSomativa.docx`) via python-docx.
- Ambiente confirmado funcional: Anaconda em `C:\Users\marcos\anaconda3\python.exe`
  (Python 3.13.9) já tinha TensorFlow 2.21/Keras 3.15/scikit-learn/PIL/matplotlib
  instalados. Foi **instalado adicionalmente `python-docx`** nesse mesmo ambiente
  (`pip install python-docx`) para poder montar o relatório final.
- **Setup de dados**: copiadas as 20 imagens de `atividade_1/RN/RN/*.png` para `C:\RN\*.png`
  (raiz do disco C:), exatamente como a orientação da atividade instrui o aluno a fazer —
  os scripts fornecidos esperam esse caminho fixo (`HD='C'`, `pasta='RN'`).
- **Bateria de treinamentos** (scripts de busca de parâmetros ficaram no scratchpad da
  sessão, não fazem parte do entregável): testadas ~8 configurações de MLP e ~7 de CNN,
  variando ativações, função de perda, otimizador, nº de camadas/neurônios/filtros,
  tamanho do kernel, percentual de treino, épocas e batch size.
- **Melhor configuração MLP** (aplicada em `atividade_1/Python/S4_MLP.py`): 2 camadas
  ocultas (256 e 128 neurônios, tanh), saída softmax, `categorical_crossentropy`, `adam`,
  métrica `accuracy`, 20% teste, 15 épocas, batch 128. Resultado: loss=0.1059,
  accuracy=0.9716 no teste MNIST; **10/10 acertos** no 1º conjunto de imagens.
- **Melhor configuração CNN** (aplicada em `atividade_1/Python/S4_CNN.py`): kernels 3×3
  (trocado do 9×9 original, que encolhia demais a imagem), 32 e 64 filtros, densa de 128,
  `relu`/`softmax`, `adam`, `categorical_crossentropy`, `accuracy`, 40% treino, 5 épocas,
  batch 128. Resultado: loss=0.0578, accuracy=0.9819; **10/10 acertos** no 1º conjunto.
- Em ambos os scripts finais: corrigidos bugs do template original (saída `relu`+
  `mean_absolute_error` na MLP e `sigmoid`+`categorical_hinge` na CNN — inadequados para
  classificação —, e kernel 9×9 com só 2 filtros na CNN), fixada semente aleatória
  (`set_random_seed(42)`) para reprodutibilidade, e adicionado `print()` das previsões no
  console (além do gráfico) para conferência.
- Criadas as versões da **Parte 2** (segundo conjunto de imagens, sufixo "b", desenhado
  pelo professor, fora da distribuição do MNIST): `atividade_1/Python/S4_MLP_partB.py` e
  `S4_CNN_partB.py` — mesmos parâmetros, apenas os nomes das imagens trocados, retreinados
  do zero como a orientação pede ("execute os dois códigos novamente").
  - MLP Parte 2: **3/10 acertos** (0, 2, 5 corretos); loss/accuracy idênticos à Parte 1
    (mesma seed, mesmo split MNIST).
  - CNN Parte 2: **6/10 acertos** (1,2,3,4,5,8 corretos); loss/accuracy idênticos à Parte 1.
- Montado o relatório final `atividade_1/Atividade_Somativa_1_Respondida.docx` a partir do
  template (via python-docx), com: tabelas de parâmetros + previsões + loss/métrica para
  MLP e CNN nas Partes 1 e 2, e a análise da Parte 3 respondendo às duas perguntas da
  orientação (por que o desempenho numérico foi idêntico entre as partes — seed fixa +
  métricas calculadas sobre o split do MNIST, não sobre as imagens da pasta RN — e por que
  os números identificados mudaram — mudança de distribuição entre os dois conjuntos de
  imagens). Arquivo entregue ao utilizador via SendUserFile.
- **Pendência explícita para o utilizador**: o campo "Nome Completo:" na capa do `.docx`
  ficou como estava no template — não foi preenchido (não há um nome real disponível para
  inserir com segurança).

### Frente B (continuação) — Experimento complementar de Data Augmentation
- Diagnosticada a causa da queda de acerto no 2º conjunto: comparadas estatisticamente as
  20 imagens contra o MNIST. Os desenhos do professor têm **metade da tinta** (traço fino:
  0,083 vs 0,158), **quase nenhum anti-aliasing** (0,05 vs 0,39), caixa do dígito variando
  de 15 a 22 px (MNIST normaliza sempre para 20) e centro de massa deslocado até 3 px.
- Testadas duas estratégias de correção (script de teste no scratchpad): pré-processamento
  estilo MNIST na entrada, e data augmentation no treino. **Decisão do utilizador: usar
  apenas data augmentation**, mencionando no relatório que ele resolve parte do problema
  de padronização — o pré-processamento customizado foi descartado.
- Criados `atividade_1/Python/S4_MLP_aug.py` e `S4_CNN_aug.py`: mesmos parâmetros
  ajustáveis dos scripts entregues, acrescidos de `RandomRotation(0.08)`,
  `RandomTranslation(0.10, 0.10)` e `RandomZoom(0.10)`, com épocas triplicadas (MLP 15→45,
  CNN 5→15) porque augmentation torna a convergência mais lenta. Ambos testam os DOIS
  conjuntos de imagens na mesma execução, para permitir o comparativo.
- Resultados medidos (mesmo carregamento de dados dos scripts entregues, comparação
  válida): MLP 3/10 → **9/10** e CNN 6/10 → **9/10** no conjunto do professor; ambos
  mantiveram 10/10 no conjunto 1; a acurácia no teste MNIST também subiu (MLP 97,16% →
  98,27%; CNN 98,19% → 98,54%).
- Acrescentada ao relatório a seção "Experimento complementar — Data Augmentation", com
  3 tabelas novas (parâmetros das transformações, comparativo sem/com augmentation, e
  previsões detalhadas dígito a dígito) e 5 parágrafos de análise.

### Frente C — Notebook de portfólio (LinkedIn)
- Criado `atividade_1/mlp_vs_cnn_eficiencia.ipynb`, **já executado com as saídas
  embutidas** (tabelas, gráficos e figuras aparecem sem precisar rodar).
- Objetivo declarado pelo utilizador: comparar a eficiência de MLP e CNN para imagens sob
  a ótica de quantidade de parâmetros e taxa de acerto, com e sem data augmentation, num
  texto que atraia recrutadores de machine learning.
- Restrições de escrita pedidas pelo utilizador (respeitadas e verificadas por script):
  **nunca usar o caractere travessão** (U+2014), e não afirmar coisas sobre a origem
  demográfica da escrita do MNIST sem referência (o 7 cortado passou a ser descrito como
  "um jeito de escrever usado em vários países", com a inferência sobre sua raridade na
  base explicitamente apresentada como suspeita a partir do comportamento dos modelos).
- Setup do notebook difere dos scripts da atividade: usa MNIST completo (60k treino /
  10k teste oficial) e caminho **relativo** `RN/RN` em vez do `C:\RN` absoluto, para ser
  portátil em qualquer máquina. Por isso os números NÃO batem com os do relatório .docx.
- **Ordem final das seções** (reestruturada a pedido do utilizador): conceito MLP x CNN →
  arquiteturas em código → contagem de parâmetros → treino dos DOIS modelos base →
  resultados/previsões/eficiência → data augmentation **por último**, como melhoria →
  conclusão. Antes os quatro modelos treinavam numa célula só, o que impedia essa ordem.
- **Bug de reprodutibilidade encontrado e corrigido** (importante, não repetir): as
  camadas `RandomRotation/RandomTranslation/RandomZoom` eram criadas na avaliação do
  argumento, portanto **antes** do `set_random_seed()` que roda dentro de
  `roda_experimento`. Elas herdavam a semente do estado deixado pelo treino anterior e os
  resultados mudavam a cada execução (chegaram a variar de 8/10 para 7/10 e 9/10 entre
  rodadas). Correção: passar a **função** `camadas_de_augmentation` (sem parênteses) e
  construir as camadas dentro de `roda_experimento`, depois do reset, além de `seed=`
  explícito em cada camada. Determinismo verificado rodando a mesma config duas vezes e
  comparando previsões e soma dos pesos da primeira convolução (idênticos).
- Resultados finais do notebook (semente 42, MNIST completo, já reproduzíveis):

  | Modelo | Params | Épocas | Tempo | Perda | Acurácia MNIST | Conj.1 | Conj.2 |
  |---|---|---|---|---|---|---|---|
  | MLP | 235.146 | 15 | 29s | 0,0861 | 97,67% | 10/10 | 4/10 |
  | CNN | 225.034 | 5 | 69s | 0,0389 | 98,69% | 10/10 | 8/10 |
  | MLP + aug | 235.146 | 45 | 315s | 0,0588 | 98,20% | 10/10 | 9/10 |
  | CNN + aug | 225.034 | 15 | 258s | 0,0608 | 98,02% | 10/10 | 9/10 |

- Achados centrais: a CNN base (8/10, 69s) fica a um dígito da MLP com augmentation
  (9/10, 315s), com menos parâmetros. Das convoluções da CNN saem só 18.816 pesos (8% do
  modelo). O augmentation **piorou** a acurácia MNIST da CNN (98,69% → 98,02%) enquanto
  melhorou o conjunto difícil, uma troca de ajuste na distribuição de treino por robustez
  (e provável falta de épocas, já que a tarefa ficou mais difícil).
- O 7 cortado só a MLP base erra. Os dois modelos com augmentation (protocolo de época
  fixa) terminam com previsões idênticas, errando só o 6.
- **Seção "O número esquisito da CNN"**: o utilizador questionou o "provavelmente é falta
  de treino" que eu tinha escrito sem testar. Medido: treino de 45 épocas registrando a
  acurácia a cada época. A época 15 caiu num vale (98,02%), com a 13 em 98,60%, a 14 em
  98,40% e a 16 já em 98,86%. O melhor ponto foi 99,25% na época 32, acima do baseline
  sem augmentation (98,69%). Conclusão: o augmentation não piorou a CNN, eu medi no pior
  ponto da vizinhança.
- **Seção "O jeito honesto: early stopping"**: implementa a verificação que o texto
  propunha. Validação de 6 mil imagens separada do treino (sobram 54 mil), `EarlyStopping`
  com `monitor="val_accuracy"`, `patience=10`, `restore_best_weights=True`, teste intocado
  até o fim. Resultados:

  | Modelo | Época (chute) | Acurácia (chute) | Conj.2 | Época (early stop) | Acurácia | Conj.2 |
  |---|---|---|---|---|---|---|
  | MLP + aug | 45 | 98,20% | 9/10 | 23 | 98,08% | **10/10** |
  | CNN + aug | 15 | 98,02% | 9/10 | **32** | **99,31%** | **10/10** |

- Achado que fecha o notebook: o early stopping escolheu a **época 32** para a CNN, a mesma
  que a curva anterior tinha identificado como melhor **espiando o conjunto de teste**. A
  validação chegou na mesma resposta sem ver o teste.
- **Correção importante na conclusão**: a versão anterior afirmava que o dígito 6 era
  impossível para todos os modelos e que só coletando dados novos daria pra resolver. Os
  dois modelos com early stopping acertaram o 6 (10/10). A conclusão foi reescrita para
  registrar o erro: não era limite do dado, era modelo parado no lugar errado.

### Frente D — Post para o LinkedIn
- Criados `atividade_1/post_linkedin.md` (texto em duas versões, longa e curta) e
  `atividade_1/post_linkedin_mlp_cnn.png` (1096x1315, retrato, ~211 KB).
- A imagem combina a tabela dos 6 modelos (parâmetros, acurácia MNIST, acertos na
  caligrafia) com a curva de acurácia por época, destacando em vermelho a época 15 (o
  vale onde eu tinha medido) e em verde a época 32 (o melhor ponto, e a que o early
  stopping escolheu sozinho). Script gerador: `imagem_post.py` no scratchpad.
- **Ajuste de terminologia**: o utilizador pediu para falar do "vale local do gradiente".
  Corrigido no texto, porque o modelo não ficou preso em mínimo local (ele se recuperou
  sozinho na época seguinte, sem intervenção). É oscilação da curva de acurácia entre
  épocas, causada pelo ruído do SGD com augmentation. O post usa "um vale da curva".
- Cuidado tomado na imagem: a curva atinge 99,25% na época 32 (rodada sem separar
  validação, 60k de treino) e a tabela mostra 99,31% (rodada com early stopping, 54k de
  treino). Para não parecer contradição na mesma imagem, a anotação verde não repete o
  número, só aponta a época.
- O LinkedIn não renderiza markdown, então o texto foi escrito em texto puro, com títulos
  de seção em caixa alta em vez de asteriscos.

### Frente E — Ilustração da arquitetura da MLP
- Criada `atividade_1/arquitetura_mlp.png` (gerada por `arquitetura_mlp.py` no
  scratchpad). Mostra a MLP do notebook (784 → 256 → 128 → 10): imagem real `sete7.png`
  sendo achatada em 784 entradas, ligações totalmente conectadas entre camadas, um nó de
  bias (+1) por camada ligado a todos os neurônios da camada seguinte (linhas laranja
  tracejadas), destaque em azul de tudo que chega no neurônio h₁, saída softmax com o 7
  destacado, e contagem de parâmetros entre cada par de camadas (total 235.146, conferido
  por script).
- Painel de zoom no neurônio h₁: entradas x₁..x₇₈₄ com pesos w, bias +1 com peso b,
  soma Σ, ativação tanh, fórmula z = Σwx + b, conta de 785 parâmetros por neurônio
  (× 256 = 200.960) e explicação do bias pela analogia com o b de y = ax + b.
- **Mal-entendido**: a ilustração da MLP foi feita por engano. O utilizador queria a da
  **RNC** (Rede Neural Competitiva). O arquivo `arquitetura_mlp.png` continua existindo,
  não foi apagado nem inserido em lugar nenhum.

### Frente F: Ilustração da arquitetura da RNC (a que foi pedida de fato)
- Criada `arquitetura_rnc.png` na raiz de `23-Redes Neurais` (gerada por
  `arquitetura_rnc.py` no scratchpad, 1760x2200).
- Quando a ilustração foi feita, o código Python da RNC do curso não existia nesta máquina
  (procurado no repositório, em Downloads, Desktop e Documentos). Ela foi baseada no PDF da
  unidade 5 (Kohonen/SOM, grade bidimensional, distância euclidiana, vizinhança) e nos dados
  das unidades 7 e 8 (cilindrada e eficiência como as 2 entradas). **O código apareceu depois,
  em `RNC/S5_RNC.py` — ver Frente H**, que confirma a decisão sobre o bias e levanta uma
  diferença entre o PDF e o código.
- **Decisão sobre o bias (importante)**: na RNC clássica **não existe bias**. O neurônio
  competitivo não faz soma ponderada nem aplica ativação, ele calcula a distância
  ‖x − w‖ e vence o de menor distância. A ilustração mostra isso explicitamente (nó +1
  riscado) e, para responder à pergunta "como o bias está conectado", mostra onde ele entra
  na única variante que tem um: a rede com consciência (DeSieno, 1988), em que cada
  neurônio competitivo recebe um −b_j somado à distância, antes da comparação. **Confirmado
  depois pelo código do professor** (`RNC/S5_RNC.py`): a classe guarda só a matriz de pesos,
  calcula a norma e pega o argmin, sem bias, sem soma ponderada e sem ativação. A ilustração
  está correta como está e não precisa de revisão.
- Conteúdo: (1) arquitetura com base de veículos ilustrativa, 2 entradas, grade 4×4 em
  perspectiva com ligações de vizinhança, vencedor e vizinhos coloridos por distância na
  grade, pesos w₁ e w₂ do vencedor destacados, saída como mapa com 1 no vencedor;
  (2) painel "como a competição é calculada" com a fórmula da distância e o −b tracejado
  entrando na junção; (3) exemplo numérico verificado por script: x = (0,8; 0,3), distâncias
  A = 0,85, B = 0,28 (vence), C = 0,36; com η = 0,5, B vai para (0,7; 0,4) e o vizinho C,
  com metade da força, vai para (0,575; 0,15); (4) tabela MLP × RNC; (5) referências
  (Kohonen, 2001; DeSieno, 1988).
- Correções de layout feitas até a versão final: o −b ficava solto sem encostar no fluxo
  (redesenhado com uma junção explícita); as linhas até o vencedor atravessavam outros
  neurônios (resolvido buscando por script um espaçamento de grade e uma posição de vencedor
  com folga de 3,25 unidades); e um texto encostava no rótulo "cilindrada".
- **Segunda rodada, a pedido do utilizador**:
  - Legenda: "peso w" e "ligação de vizinhança" tinham cores quase iguais (dois cinzas).
    A vizinhança passou a roxo (`#8e44ad`, linha mais grossa) e os pesos continuam em cinza claro.
  - Painel "Como a competição é calculada": a fórmula usava a letra j, mas os blocos só
    tinham números (1, 2, 16). O bloco do meio virou "neurônio j" em destaque, com as
    ligações das entradas destacadas, o rótulo "pesos w_j1 e w_j2" e a legenda "onde j é um
    neurônio qualquer da grade (1 a 16)". Há reticências entre 1 e j e entre j e 16.
  - Painel do exemplo numérico: ganhou escala nos dois eixos (marcas a cada 0,1, números a
    cada 0,2), grade leve, projeções tracejadas de cada ponto até os eixos e as coordenadas
    ao lado de cada letra: A (0,2; 0,9), B (0,6; 0,5), C (0,5; 0,1) e x (0,8; 0,3).
  - Gravação do PNG: o arquivo final estava bloqueado (`OSError Errno 22`), provavelmente
    por estar aberto no IDE. O script agora lê o caminho de saída da variável de ambiente
    `DESTINO_RNC` (com o caminho do projeto como padrão). A renderização vai para um PNG
    temporário no scratchpad, que depois é copiado por cima do original.
- **Resumo.md**:
  - A figura foi incluída na seção 5.3 (`![...](arquitetura_rnc.png)`), com um parágrafo
    que explica a figura e reforça que não há bias.
  - Criada a seção **5.2.1 "Mapeamento de entradas para neurônios, em detalhe"**, que
    parte da frase do PDF da unidade 5. Tópicos, com números conferidos por script:
    (1) o vetor de pesos tem a dimensão da entrada e é um ponto no espaço dos dados (tabela
    comparando o peso na MLP e na RNC; perfis de A, B e C); (2) sensibilidade como região de
    Voronoi, mapeando 4 veículos (0,8;0,3)→B, (0,25;0,85)→A, (0,45;0,15)→C, (0,55;0,55)→B,
    e a menor distância como indicador de anomalia; (3) euclidiana × cosseno, com
    u=(0,2;0,4) e v=(0,4;0,8): euclidiana 0,447 e cosseno 1,0; (4) escala dos atributos:
    carros (1,6 L; 150 g/km) e (3,6 L; 160 g/km) têm distância 10,20 sem normalizar, dominada
    pelo CO₂, e 0,401 normalizada, dominada pela cilindrada (faixas hipotéticas 1–6 L e
    100–400 g/km); (5) especialização: com η = 0,1, depois de 30 passadas, o peso vai de
    (0,6;0,5) para (0,811;0,285), perto da média (0,810;0,287) dos 3 veículos que ele vence;
    (6) preservação da topologia pela vizinhança; (7) armadilhas (neurônio morto, poucos ou
    muitos neurônios, escala) e a ligação com o `inshape = 2` das unidades 7 e 8.
  - A linha "Mapeamento entradas → neurônios" da tabela 5.2 agora aponta para a 5.2.1.
- Outras correções aplicadas ao notebook: trocado `input_shape=` por camada `Input()`
  explícita (eliminou UserWarning do Keras 3), removida célula de código vazia no fim, e
  reordenada a seção de augmentation que antes aparecia depois do código que já a usava.

### Frente G — Atualização dos pesos e figura de similaridade (unidade 5)
Pedido do utilizador: "como os pesos sinápticos dos neurônios na camada competitiva são
alterados?" e "faça outra ilustração para representar a similaridade do cosseno e a
distância euclidiana".
- Criada `similaridade_cosseno_euclidiana.png` na raiz de `23-Redes Neurais` (gerada por
  `similaridade.py` no scratchpad, 1760x2090), na mesma paleta da `arquitetura_rnc.png`.
  O caminho de saída também é parametrizado por variável de ambiente (`DESTINO_SIM`), pelo
  mesmo motivo da figura anterior (arquivo bloqueado quando aberto no IDE).
- Exemplo escolhido para a figura, com números conferidos por
  `numeros_pesos_similaridade.py` (scratchpad): x = (0,2 ; 0,4), w_B = (0,4 ; 0,8) e
  w_C = (0,5 ; 0,1). Resultado: d(x, w_B) = 0,447 com cosseno 1,000 (0°), e
  d(x, w_C) = 0,424 com cosseno 0,614 (52,1°). **As duas medidas elegem vencedores
  diferentes** com os mesmos dois neurônios: a euclidiana escolhe C, o cosseno escolhe B.
  Foi esse contraste que definiu a figura inteira. Depois de normalizar para módulo 1,
  x̂ = ŵ_B (d = 0) e d(x̂, ŵ_C) = 0,879, que é √(2 · (1 − cos θ)).
- Painéis da figura: (1) euclidiana, com linhas de cota entre as pontas — deslocadas
  perpendicularmente de propósito, porque x e w_B são colineares e a cota cairia em cima
  dos próprios vetores; (2) cosseno, com o arco de 52,1° e a reta comum a x e w_B;
  (3) tabela de quem vence em cada medida; (4) círculo unitário e d² = 2 · (1 − cos θ);
  (5) tabela "quando usar cada uma"; referências Kohonen (2001) e Haykin (2007).
- `Resumo.md`, seção 5.2.1 item 3: reescrito. Antes era um exemplo curto com u e v; agora
  traz a figura, a tabela com os dois vencedores e o parágrafo sobre normalização.
- `Resumo.md`, nova seção **5.4.1 "Como os pesos sinápticos são alterados, passo a passo"**,
  logo após os 6 passos de Kohonen. Conteúdo: a regra
  `w_j(t+1) = w_j(t) + η(t) · h_jv(t) · [x(t) − w_j(t)]` com o papel de cada termo; o que a
  taxa de aprendizado faz (η = 1 / 0,5 / 0,1 / 0,01 partindo de (0,6 ; 0,5) até x =
  (0,8 ; 0,3)); a função de vizinhança gaussiana, com o alerta de que `dist_grade` é medida
  **na grade** e não no espaço dos dados; o passo completo com os 3 neurônios da figura da
  5.3; as duas fases do treino (ordenação e convergência) com o decaimento de η e σ ao longo
  de 100 épocas; por que o peso acaba na média do grupo; um esboço de código comentado; e
  uma tabela de variações (on-line, batch, vizinhança retangular, cosseno, consciência).
- Três observações que valem manter: nenhum neurônio é empurrado para longe do dado (não há
  ajuste negativo, quem perde só fica parado); todos os neurônios são atualizados a cada
  dado, mas com forças tão diferentes que na prática só o vencedor e a vizinhança se movem;
  e encolher σ rápido demais congela o mapa torcido, sem conserto.
- Coerência com a figura `arquitetura_rnc.png`: lá o vizinho imediato anda com metade da
  força e "A não é vizinho: fica parado". No texto isso virou h = 0,5 para o vizinho
  imediato (equivale a uma gaussiana com σ ≈ 0,849, conferido) e A a 4 casas na grade, com
  h = 0,000015. Se a figura for refeita, esses dois valores precisam continuar batendo.

### Frente G (continuação) — Seção 5.4.2 e o gráfico da vizinhança
Pergunta do utilizador: "explique o que é σ e h", seguida de "quero" para transformar a
explicação em seção do resumo, com gráfico.
- Criada a seção **5.4.2 "A vizinhança em detalhe: o que são h e σ"** no `Resumo.md`, logo
  após a 5.4.1. Conteúdo: h como "volume" e σ como "alcance" (analogia da lanterna apontada
  para a grade, em que o vencedor é o centro do facho); leitura dos índices de `h_jv(t)`;
  tabela com o perfil de h para σ = 3,0 / 2,0 / 1,0 / 0,85 / 0,5 nas distâncias 0 a 5;
  σ₀ perto de metade do lado da grade, caindo para abaixo de 1; as duas fases; e duas
  confusões comuns (h não é η; a gaussiana não é obrigatória, existe a retangular).
- Criada a figura `vizinhanca_h_sigma.png` na raiz (gerada por `vizinhanca.py` no
  scratchpad, variável de ambiente `DESTINO_VIZ`). Dois painéis: as curvas de h por
  distância na grade para três σ, e a mesma grade 5×5 colorida por h com σ = 2,0 e σ = 0,5.
- **Processo de cor (vale repetir em qualquer gráfico futuro):** a skill `dataviz` foi
  carregada e exige rodar `scripts/validate_palette.js` em vez de julgar a olho. **O node
  não está instalado nesta máquina**, então as checagens foram portadas para Python em
  `valida_paleta.py` (scratchpad): OKLab, simulação de daltonismo por Viénot/Brettel/Mollon
  (1999) e contraste WCAG, medindo contra a superfície real destes painéis (`#f6f8fb`), e
  não contra a `#fcfcfb` padrão da skill.
- Resultado da validação, que mudou o desenho: a rampa azul **ordinal** da skill só pode ir
  do passo 250 ao 700 no fundo claro, e **4 passos nesse intervalo dão ΔE ≈ 14,5**, abaixo
  do piso 15 de visão normal, que a skill trata como falha dura que nem codificação
  secundária desculpa. Como re-espaçar não resolve (o intervalo está esgotado), aplicou-se o
  remédio prescrito: **cortar séries**, de 4 curvas para 3. Escolhidos `#86b6ef` (σ = 2,0),
  `#256abf` (σ = 1,0) e `#0d366b` (σ = 0,5), com ΔE 24,2 e 19,5 na visão normal e nunca
  abaixo de 19,5 sob daltonismo.
- O passo mais claro fica em 1,98:1 de contraste contra o fundo, abaixo de 3:1. Mitigado
  como a skill manda (relief rule): cada curva tem rótulo direto e a seção traz a tabela
  numérica completa, então nenhum valor depende só da cor.
- σ maior recebeu o tom **mais claro**, invertendo o "maior = mais escuro" intuitivo, porque
  a curva de σ pequeno é um pico estreito colado no eixo e precisa da tinta mais forte para
  ser legível. O mapeamento continua monotônico em σ, que é o que a regra exige.

### Frente H — O código da RNC da disciplina (pasta `RNC/`)
Pedido do utilizador: "me fale sobre o conteúdo de RNC". A pasta apareceu na raiz do projeto
em 15/09/2026 e traz o material da atividade da unidade 5, que antes não existia aqui.
- Conteúdo: `RNC/S5_RNC.py` (9,6 KB), `RNC/base_veiculos.csv` (1,7 MB) e
  `RNC/template da atividade.docx`.
- **Dúvida do bias resolvida:** a classe `RNC` do professor guarda só
  `weights = np.random.rand(num_neurons, input_shape)`, calcula
  `np.linalg.norm(input_sample - weights, axis=1)` e pega o `argmin`. Sem bias, sem soma
  ponderada, sem ativação. A `arquitetura_rnc.png` está correta como está.
- **Descoberta mais importante:** `update_weights` atualiza **apenas o vencedor**. Não há
  grade, não há vizinhança, não há h nem σ. O código implementa **aprendizado competitivo
  puro** (quantização vetorial on-line), e não um mapa de Kohonen, embora o PDF da unidade 5
  descreva vizinhança topológica e traga o passo 5 "atualização dos pesos dos neurônios
  vizinhos". As seções 5.4.1 e 5.4.2 do `Resumo.md` descrevem o SOM completo, que é o que o
  PDF pede. **Pendente de decisão do utilizador:** incluir ou não uma nota no `Resumo.md`
  registrando essa diferença entre o PDF e o código, como já foi feito com outras duas
  imprecisões dos materiais.
- **Parâmetros padrão do código:** `taxa_aprend_rnc = 2.0`, `epocas_rnc = 1`,
  `num_neur_rnc = 4`, `ordem_pol = 1`, `cilindrada_info = 1.0`.
- **η = 2,0 é destrutivo, e isso foi medido** (`analisa_rnc_curso.py` no scratchpad, que
  replica a classe do professor): 78,4% das atualizações jogam o peso para fora da faixa dos
  dados; os pesos finais param em (30,97; 37,00) e (−1,51; 48,59), sendo que a base vai só
  até 8,4 L e 24,7 km/L; 2 dos 4 neurônios ficam vazios e 37.962 dos 37.967 veículos caem num
  único grupo. Com η = 1,0 os 4 grupos se formam; com η = 0,1 sobra um neurônio morto (5
  elementos). Razão aritmética: `w + η(x − w)` com η = 2 devolve `2x − w`, que fica à mesma
  distância do dado, do lado oposto (medido: 2,24 antes, 2,24 depois).
- **A base:** 37.967 linhas; colunas Make, Model, Cilindrada, Eficiencia, CO2; 125 montadoras
  e 3.681 modelos. Nenhum valor ausente e nenhum zero, então o `dropna()` e o filtro de zeros
  do código não removem nada. **23.179 linhas (61%) são duplicadas.** Cilindrada vai de 0,6 a
  8,4 L e eficiência de 2,98 a 24,66 km/L, amplitudes 2,78× diferentes, e o código **não
  normaliza**, ao contrário do que o próprio PDF exige (seção 5.5 do Resumo).
- **O código não roda como está:** lê `C:/RN/base_veiculos.csv`, que não existe. `C:\RN\` tem
  apenas os 20 PNGs do MNIST da atividade_1. Copiar o CSV para lá resolve, seguindo a mesma
  convenção da atividade anterior.
- **A atividade (template .docx):** ajustar número de neurônios (sugere de 3 a 10), épocas,
  taxa de aprendizado e ordem do polinômio; depois entregar relatório em DOCX ou PDF no AVA
  com tabela de parâmetros, gráfico, tabela de agrupamentos, função polinomial, previsão de
  eficiência e um texto de análise. O template manda baixar "S5_RNC.spy", mas o arquivo
  entregue é `.py`.

### Frente H (continuação) — Execução e ajuste da atividade da unidade 5
O utilizador copiou `base_veiculos.csv` para `C:\RN\` e pediu para executar o código, buscar
os parâmetros por experimentação e analisar as saídas. Scripts de apoio no scratchpad:
`busca_parametros_rnc.py`, `diagnostico_rnc.py`, `escolhe_parametros_rnc.py`, `grafico_rnc.py`.
- **Linha de base (parâmetros de fábrica):** só 2 grupos não vazios de 4, um com 3 veículos e
  outro com 37.964. `f(x) = -1.18x + 12.41`, previsão de 11,23 km/L para 1,0 L.
- **Causa raiz descoberta e medida:** `np.random.rand` sorteia os pesos em [0,1) nos dois
  eixos, mas a eficiência dos dados começa em 2,98 km/L. **Todo neurônio nasce abaixo da
  nuvem de dados**, e só os poucos mais próximos conseguem vencer; os demais nunca são
  atualizados e ficam congelados na posição inicial. Com k = 6, quatro dos seis terminaram
  nas coordenadas exatas em que nasceram. É por isso que k de 3 a 10 dava erro idêntico.
- **Épocas são inertes neste código:** 1, 5, 20 e 50 dão resultado igual até a quarta casa,
  inclusive com os dados embaralhados. Com taxa constante e sem decaimento, a memória do
  modelo é de ~1/η amostras, então o que define os pesos finais é o fim da base, não quantas
  vezes ela foi percorrida. Se algum dia for preciso que épocas importem, é o decaimento de η
  (seção 5.4.1 do Resumo) que falta, não mais iterações.
- **Normalizar resolveria:** com min-max, os neurônios mortos somem e o erro passa a cair com
  k (1,229 em k=3 até 0,888 em k=10). Mas normalizar é mudar o código, e a atividade pede
  ajuste dos quatro parâmetros numéricos, então ficou como observação para o relatório.
- **Busca:** 56 configurações (k de 3 a 10 × 7 taxas), 3 sementes cada. **Só 6 não deixam
  nenhum grupo vazio.** Critério declarado antes de ver os números: descartar quem deixa
  grupo vazio, depois menor erro de quantização, desempate pelo menor k.
- **Parâmetros escolhidos e aplicados em `RNC/S5_RNC.py`** (valores originais entre
  parênteses): `num_neur_rnc = 3` (era 4), `taxa_aprend_rnc = 0.3` (era 2.0),
  `epocas_rnc = 5` (era 1), `ordem_pol = 5` (era 1). `cilindrada_info = 1.0` não mudou.
- **Ordem do polinômio validada contra a realidade**, não só por R²: comparada com a média
  real de eficiência por faixa de cilindrada. A ordem 5 prevê 15,44 km/L para 1,0 L contra
  15,38 km/L reais (186 veículos entre 0,9 e 1,1 L), e 5,84 em 8,0 L contra 5,49 reais. A
  ordem 7 ajusta as faixas um pouco melhor (0,2728 contra 0,3263) mas erra mais na ponta, onde
  há poucos dados para segurá-la.
- **Resultado final:** 3 grupos com 467, 14.659 e 22.841 veículos; pesos (1,92 ; 19,33),
  (2,00 ; 10,20) e (4,25 ; 7,93). `f(x) = -0.01x⁵ + 0.23x⁴ - 2.18x³ + 9.92x² - 23.03x + 30.51`,
  previsão de **15,44 km/L** para 1,0 L.
- **Reprodutibilidade, apesar de o código não fixar semente:** duas execuções seguidas deram
  particionamento idêntico (mesmos 467/14.659/22.841 e mesmas faixas). O que muda é só a
  **numeração** dos grupos, porque depende de qual neurônio sorteado ocupou cada região. Ao
  escrever o relatório, referir-se aos grupos pelo perfil, nunca pelo número.
- **Achado para a análise:** os grupos se separam quase só por eficiência (faixas limpas:
  2,98–10,20 / 7,23–14,45 / 14,88–24,66) enquanto a cilindrada se sobrepõe muito (1,3–8,4
  contra 0,9–4,3). É a falta de normalização: a eficiência tem amplitude 2,78× maior e domina
  a distância, exatamente o que a seção 5.2.1, item 4, do Resumo prevê.
- **Figura `RNC/resultado_rnc.png`** gerada por `grafico_rnc.py`, porque o código da
  disciplina só chama `plt.show()` e não deixa arquivo para o relatório.
- **Nota no `Resumo.md`** sobre competição pura × SOM: foi escrita na seção 5.4, mas o
  utilizador **removeu-a depois**, junto com todo o material da atividade que havia entrado no
  resumo. **Decisão editorial a respeitar: o `Resumo.md` é material teórico e não menciona a
  pasta `RNC/`, o `S5_RNC.py`, a base `base_veiculos.csv` nem os resultados da atividade.**
  Referências ao código das unidades 07/08 (como `inshape = combinacao.shape[1]`) continuam lá e
  são aceitáveis. Não reintroduzir o conteúdo removido sem pedido explícito.
- **Pendente:** montar o relatório em DOCX/PDF pedido pelo template, se o utilizador quiser.

### Frente I — Seção 5.2.2 do Resumo: o espaço de dados
Pedido: "me fale mais sobre o espaço de dados" e, em seguida, "transforme isso numa seção".
- Criada a seção **5.2.2 "O espaço de dados: onde os dados e os neurônios moram"**, entre a
  5.2.1 e a 5.3. Números conferidos por `numeros_secao_522.py` (scratchpad).
- Ancorada de propósito nos **mesmos neurônios didáticos da 5.2.1** — A = (0,2 ; 0,9),
  B = (0,6 ; 0,5), C = (0,5 ; 0,1) — e **não** nos pesos treinados da atividade, porque o
  utilizador tinha acabado de tirar o material da atividade do resumo.
- Conteúdo: um eixo por atributo e cada registro como ponto; pesos morando no mesmo espaço;
  divisão por Voronoi com as três mediatrizes calculadas (A×B a 45°, B×C quase horizontal),
  com a leitura de que a fronteira é perpendicular ao segmento entre os neurônios e portanto
  decidida pela direção em que eles mais diferem; a área que cada região ocupa (A 24,1%,
  B 45,0%, C 30,9%) e o alerta de que tamanho de região não é tamanho de grupo; o efeito da
  unidade de medida (multiplicar um eixo por 3 faz **30,5% do espaço trocar de dono**, e o
  ponto (0,40 ; 0,45) sai de B para C); a maldição da dimensionalidade medida (contraste das
  distâncias cai de 82,7× em 2D para 0,16× em 784D) com a ressalva honesta de que dados reais
  vivem numa superfície de dimensão menor; e uma tabela final traduzindo cada conceito da RNC
  para a sua leitura geométrica.
- A checagem cruzada confirmou que os quatro veículos da tabela da 5.2.1 vencem A, B e C
  exatamente como já estava escrito lá.
- **Figura `voronoi_rnc.png`** (gerada por `voronoi.py` no scratchpad, variável de ambiente
  `DESTINO_VOR`), inserida na 5.2.2 ao fim da subseção sobre a régua. Dois painéis:
  (1) o espaço como ele é, com as mediatrizes inteiras tracejadas, as fronteiras reais em
  cor, os segmentos entre cada par de neurônios com o ponto médio marcado e os quatro
  veículos da tabela da 5.2.1; (2) o mesmo espaço com o atributo 1 medido numa unidade 3×
  maior, com a área que trocou de dono hachurada e um ✕ no ponto (0,40 ; 0,45), que sai da
  região de B para a de C.
- Cor da figura: fatias categóricas 1 a 3 da skill `dataviz`, mas as áreas são preenchidas com
  a versão bem clara de cada tom (bloco grande saturado é anti-padrão) e a cor cheia fica só
  no ponto do neurônio; cada região tem rótulo direto, então a identidade nunca depende da cor.
- **Lição de medição:** a primeira versão imprimia A 24,2% e B 44,9% porque calculava as áreas
  na mesma malha do desenho (700 pontos), divergindo da tabela da seção. Passou a medir numa
  malha de 6001×6001 percorrida em blocos: **A 24,12%, B 45,00%, C 30,87%**, com a outra régua
  A 33,87%, B 50,49%, C 15,65%, e troca de dono de 30,47%. Isso **confirmou** os valores que já
  estavam no texto (24,1 / 45,0 / 30,9 e 30,5%). Se a figura for refeita, manter a malha fina.
- Achado visual que entrou na legenda: com o atributo 1 valendo 3× mais, as fronteiras ficam
  quase verticais, ou seja, o atributo 2 quase deixa de participar da decisão.

## 3. Em andamento 🔧
Nenhuma tarefa em andamento no momento deste checkpoint. Ambas as frentes estão em ponto de
entrega/revisão.

## 4. Próximos passos (planejado) 📋
Nenhum passo obrigatório pendente. Possibilidades, caso o utilizador queira continuar:
1. Frente A: a unidade 05 (RNC) já recebeu o aprofundamento (seções 5.2.1 e 5.4.1, mais
   duas figuras). Falta aplicar o mesmo às unidades 06-08 (RNT e duplo treinamento).
2. Frente B: revisar visualmente o `.docx` gerado no Word e preencher "Nome Completo:";
   opcionalmente também gerar os gráficos de treino (`plt.plot` do `S4_CNN.py`) como
   imagens para anexar ao relatório, já que a execução automatizada usou backend `Agg`
   (não interativo) e não salvou essas figuras em arquivo.
3. Rodar os 4 scripts finais (`S4_MLP.py`, `S4_CNN.py`, `S4_MLP_partB.py`,
   `S4_CNN_partB.py`) diretamente no Spyder, caso o utilizador quera ver as janelas de
   gráfico interativas (`plt.show()`) que a execução via linha de comando ignorou.
4. Considerar limpar a pasta duplicada `C:\RN\RN` (resquício da extração do .rar), já que
   as imagens úteis estão em `C:\RN\*.png` diretamente.

## 5. Decisões e raciocínio 🧠
- **Por que copiar para `C:\RN`** em vez de mudar os caminhos no código: os scripts
  fornecidos pelo professor usam `HD='C'` e `pasta='RN'` fixos, e a própria orientação da
  atividade instrui o aluno a colocar a pasta ali — replicar esse setup mantém os scripts
  idênticos ao que o aluno realmente usaria no Spyder.
- **Por que fixar `set_random_seed(42)`**: sem isso, cada execução geraria pesos iniciais
  diferentes e os resultados da Parte 1 vs Parte 2 variariam por acaso, dificultando
  separar "variação por aleatoriedade" de "variação por mudança de distribuição das
  imagens" — o que é justamente o ponto pedagógico da Parte 3 da atividade. Isso também
  gerou uma resposta mais rica e honesta na análise (explicando ambos os efeitos).
- **Por que criar `S4_MLP_partB.py`/`S4_CNN_partB.py` como arquivos separados** em vez de
  editar os originais in-place: a orientação pede resultados de AMBAS as partes no
  relatório final; manter os dois estados como arquivos runnable evita perder evidência/
  reprodutibilidade de uma das partes.
- **Por que não preencher "Nome Completo:"**: o e-mail do utilizador
  (marcos.skatevelho@gmail.com) não é um nome real verificável — nunca inferir/inventar
  nome de pessoa a partir de um endereço de e-mail.
- **Por que os resultados de loss/métrica são idênticos entre Parte 1 e Parte 2** (mesmo
  modelo, mesmo split MNIST — as imagens da pasta RN só entram no `model.predict()`
  qualitativo, nunca no `model.evaluate()`): detalhado na análise da Parte 3 do relatório.
- Foram sinalizadas duas imprecisões dos materiais originais (PDFs) no `Resumo.md`, por
  valor pedagógico: Unidade 08 (`inshape3 = combinacao2.shape[1]`, deveria ser
  `combinacao3`) e Unidade 06 ("RMSdrop" → nome correto é `RMSprop`).

## 6. Estado do projeto / ambiente
- Diretório do projeto: `c:\Users\marcos\Documents\GitHub\PUC\23-Redes Neurais`
- Branch git: `main`. Alterações não commitadas (nada foi commitado nesta sessão):
  - Modificados: `Resumo.md`.
  - Novos na raiz: `arquitetura_rnc.png` e `similaridade_cosseno_euclidiana.png` (as duas
    figuras da unidade 05, referenciadas pelo `Resumo.md`).
  - Novo/atualizado: `CONTEXTO.md` (este ficheiro).
  - Novos em `atividade_1/Python/`: `S4_MLP_partB.py`, `S4_CNN_partB.py`,
    `S4_MLP_aug.py`, `S4_CNN_aug.py`.
  - Modificados em `atividade_1/Python/`: `S4_MLP.py`, `S4_CNN.py` (parâmetros ajustados,
    bugs de ativação/perda corrigidos, seed fixa, prints de previsão adicionados).
  - Novos em `atividade_1/`: `Atividade_Somativa_1_Respondida.docx` (relatório final) e
    `mlp_vs_cnn_eficiencia.ipynb` (notebook de portfólio, já executado).
- Fora do repositório git (mudanças no sistema, feitas seguindo a própria orientação da
  atividade): pasta `C:\RN\` criada/populada com as 20 imagens PNG (e uma subpasta
  duplicada `C:\RN\RN\` que já existia antes, resquício da extração do .rar).
- Ambiente Python usado para TUDO nesta sessão:
  `C:\Users\marcos\anaconda3\python.exe` (Anaconda, base env) — já tinha TensorFlow
  2.21.0, Keras 3.15.1, scikit-learn 1.7.2, Pillow 12.0.0, matplotlib 3.10.6.
  **Instalado nesta sessão**: `python-docx` (via `pip install python-docx`).
- O Python "de sistema" (`python` no PATH, versão 3.14.3, Windows Store) **não** tem
  TensorFlow — não usar esse interpretador para nada relacionado a redes neurais; usar
  sempre o caminho completo do Anaconda acima.
- Scripts de busca de hiperparâmetros (`grid_mlp.py`, `grid_mlp2.py`, `grid_cnn.py`,
  `grid_cnn2.py`) e scripts auxiliares de inspeção/montagem do docx
  (`inspect_docx.py`, `list_styles.py`, `build_report.py`, `verify_report.py`,
  `verify_paragraphs.py`) ficaram no **scratchpad da sessão** (não persistem entre
  sessões, caminho volátil sob `AppData\Local\Temp\claude\...`) — não fazem parte do
  repositório do projeto.

## 7. Bloqueios e pendências ⚠️
- Nenhum bloqueio técnico.
- Pendência para o utilizador: preencher "Nome Completo:" na capa do
  `Atividade_Somativa_1_Respondida.docx` antes de submeter.
- Os gráficos de treino (`plt.plot`/`plt.show()` dos 4 scripts) não foram salvos em
  arquivo durante a execução automatizada (rodou com backend matplotlib `Agg`,
  não-interativo, só para não travar o terminal) — se o utilizador quiser esses gráficos
  no relatório, precisa rodar os scripts no Spyder (onde `plt.show()` funciona
  normalmente) ou pedir para gerá-los e salvá-los como imagem.

## 8. Comandos úteis
- Rodar qualquer um dos 4 scripts da atividade (da pasta `atividade_1/Python/`):
  `& "C:\Users\marcos\anaconda3\python.exe" S4_MLP.py` (ou `S4_CNN.py`,
  `S4_MLP_partB.py`, `S4_CNN_partB.py`). Sem `$env:MPLBACKEND="Agg"`, os `plt.show()`
  abrirão janelas interativas normalmente.
- Reabrir o Spyder (fluxo oficial da disciplina): Anaconda Navigator → aba Home → Launch.
- Commitar o trabalho desta sessão (ainda não feito):
  `git add "Resumo.md" "CONTEXTO.md" "atividade_1"; if ($?) { git commit -m "Aprofunda Resumo.md e conclui Atividade Somativa 1" }`

## 9. Como retomar
Leia este ficheiro. Se o pedido for sobre o **resumo de estudo**, vá a `Resumo.md` (já
maduro para MLP, CNN e RNC; RNT e as unidades 07-08 ainda no nível básico). Se for sobre a **atividade somativa**,
os 4 scripts finais e o `.docx` de resposta já estão prontos em `atividade_1/` — falta só
o utilizador preencher o nome na capa e, se quiser, revisar/rodar no Spyder para ver os
gráficos interativos.
