# As figuras do Resumo

Detalhe do tópico indexado em [../CONTEXTO.md](../CONTEXTO.md).

## ⚠️ Risco de perda

**Todos os scripts geradores vivem no scratchpad da sessão** (`AppData\Local\Temp\claude\...`), que
é volátil e não persiste entre sessões. Este ficheiro guarda os parâmetros e decisões de cada figura
para que possam ser refeitas, mas mover os scripts para o repositório seria mais seguro. **Decisão
pendente do utilizador.**

## As oito figuras

| Arquivo | Seção do Resumo | Script gerador | Variável de ambiente |
|---|---|---|---|
| `cnn_canal_filtro_kernel.png` | 3.2 | `cnn_vocabulario.py` | `DESTINO_CNN` |
| `arquitetura_rnc.png` | 5.3 | `arquitetura_rnc.py` | `DESTINO_RNC` |
| `similaridade_cosseno_euclidiana.png` | 5.2.1 | `similaridade.py` | `DESTINO_SIM` |
| `vizinhanca_h_sigma.png` | 5.4.2 | `vizinhanca.py` | `DESTINO_VIZ` |
| `voronoi_rnc.png` | 5.2.2 | `voronoi.py` | `DESTINO_VOR` |
| `arquitetura_rnt.png` | 6.3 | `arquitetura_rnt.py` | `DESTINO_RNT` |
| `treinamento_rnt.png` | 6.5 | `treinamento_rnt.py` | `DESTINO_TREINO` |
| `celula_lstm.png` | 6.6.1 | `celula_lstm.py` | `DESTINO_LSTM` |

Há ainda `atividade_1/arquitetura_mlp.png`, feita **por engano** (o utilizador queria a da RNC).
Nunca foi inserida em lugar nenhum e continua existindo.

## Dois procedimentos que sempre se repetem

### 1. Arquivo bloqueado ao regravar

Se o PNG estiver aberto no editor, o `savefig` falha com `OSError: [Errno 22] Invalid argument`. Por
isso **todo script lê o caminho de saída de uma variável de ambiente**. O contorno:

```powershell
$tmp = "...\scratchpad\tmp.png"; $env:DESTINO_XXX = $tmp
& "C:\Users\marcos\anaconda3\python.exe" -u "...\script.py"
if ($?) { Copy-Item -Force $tmp "...\figura.png" }
```

### 2. Sempre olhar o PNG renderizado

**Em todas as sete figuras apareceram colisões de layout que só a inspeção visual pega.** Nenhuma
saiu pronta na primeira tentativa. Os defeitos recorrentes:

- título e subtítulo de painel impressos um sobre o outro (`set_title` mais um texto em `transAxes`);
- legenda colidindo com o rótulo do eixo;
- caixas estourando a borda do painel;
- rótulo de uma série colando na série vizinha — o pior de todos, porque **troca a identidade**;
- texto de duas linhas descendo e cruzando uma linha do desenho.

**Lição de projeto, não de posição:** na figura do Voronoi, o rótulo da região colidia com o do
neurônio porque o neurônio fica perto do centroide da própria região, que é onde o rótulo
naturalmente cai. A solução foi **juntar os dois numa caixa só**, eliminando a colisão por
construção em vez de empurrar coordenadas.

## Paleta e a skill `dataviz`

A skill exige rodar `scripts/validate_palette.js` em vez de julgar cor a olho. **O Node não está
instalado nesta máquina**, então as checagens foram portadas para Python em `valida_paleta.py`
(scratchpad): OKLab, simulação de daltonismo por Viénot/Brettel/Mollon (1999) e contraste WCAG,
medindo contra a superfície real destes painéis (`#f6f8fb`), não contra a `#fcfcfb` padrão da skill.

### O resultado que mudou um desenho

Para `vizinhanca_h_sigma.png` eu queria 4 curvas. A rampa azul **ordinal** da skill só pode ir do
passo 250 ao 700 em fundo claro, e **4 passos nesse intervalo dão ΔE ≈ 14,5**, abaixo do piso 15 de
visão normal — que a skill trata como falha dura que nem codificação secundária desculpa. Como
re-espaçar não resolve (o intervalo está esgotado), apliquei o remédio prescrito: **cortar séries**,
de 4 curvas para 3.

Escolhidos `#86b6ef` (σ = 2,0), `#256abf` (σ = 1,0) e `#0d366b` (σ = 0,5): ΔE 24,2 e 19,5 na visão
normal, nunca abaixo de 19,5 sob daltonismo.

O passo mais claro fica em 1,98:1 de contraste, abaixo de 3:1. Mitigado como a skill manda (relief
rule): cada curva tem rótulo direto e a seção traz a tabela numérica completa.

**Mapeamento invertido de propósito:** σ maior recebeu o tom **mais claro**, contrariando o "maior =
mais escuro" intuitivo, porque a curva de σ pequeno é um pico estreito colado no eixo e precisa da
tinta mais forte para ser legível. O mapeamento continua monotônico em σ, que é o que a regra exige.

### Regras de cor seguidas nas outras figuras

- **Áreas grandes nunca em cor saturada** (anti-padrão). No Voronoi, as regiões usam a versão bem
  clara de cada tom e a cor cheia fica só no ponto do neurônio.
- **Identidade nunca depende só da cor**: toda região e toda curva tem rótulo direto.
- Para dispersão, só as **três primeiras fatias categóricas** da skill são validadas para "todos os
  pares", que é o caso quando qualquer par de grupos pode aparecer lado a lado.

## Conteúdo e números de cada figura

### `cnn_canal_filtro_kernel.png`
Feita para resolver a confusão entre os quatro termos da unidade 03. Três painéis: (1) as palavras
**encaixadas** — uma camada contém filtros, um filtro contém um kernel por canal de entrada, e cada
filtro produz um mapa; (2) como um filtro devolve **um** número, com os três canais somados pela
profundidade; (3) o pipeline do MNIST camada a camada, com os shapes e os parâmetros reais (320,
18.496, 206.218), deixando explícito que a profundidade de cada volume é o número de filtros da
camada que o produziu, e é ela que define quantos kernels o próximo filtro precisa ter.

### `arquitetura_rnc.png`
Grade 4×4 em perspectiva, vencedor e vizinhos coloridos por distância na grade, e o nó de bias
**riscado** — porque a RNC clássica não tem bias, o que foi depois confirmado pelo código do
professor. O `−b` tracejado mostra onde ele entraria na variante com consciência (DeSieno, 1988).
Exemplo numérico: x = (0,8; 0,3), distâncias A = 0,85, B = 0,28 (vence), C = 0,36; com η = 0,5, B
vai para (0,7; 0,4) e o vizinho C, com metade da força, para (0,575; 0,15).

### `similaridade_cosseno_euclidiana.png`
O exemplo foi escolhido para as duas medidas **discordarem**: x = (0,2; 0,4), w_B = (0,4; 0,8),
w_C = (0,5; 0,1). d(x,w_B) = 0,447 com cosseno 1,000; d(x,w_C) = 0,424 com cosseno 0,614. A
euclidiana escolhe C, o cosseno escolhe B. Normalizando, x̂ = ŵ_B e d(x̂,ŵ_C) = 0,879 = √(2(1−cos)).
As linhas de cota são deslocadas perpendicularmente de propósito, porque x e w_B são colineares.

### `vizinhanca_h_sigma.png`
Curvas de h por distância na grade para três σ, e a mesma grade 5×5 colorida por h com σ = 2,0 e
σ = 0,5.

### `voronoi_rnc.png`
Dois painéis: o espaço como ele é (mediatrizes inteiras tracejadas, fronteiras reais em cor,
segmentos entre neurônios com ponto médio) e o mesmo espaço com o atributo 1 medido numa unidade 3×
maior, com a área que trocou de dono hachurada.

**Lição de medição:** a primeira versão imprimia A 24,2% e B 44,9% porque calculava as áreas na
mesma malha do desenho (700 pontos), divergindo da tabela da seção. Passou a medir numa malha de
6001×6001 percorrida em blocos: **A 24,12%, B 45,00%, C 30,87%**, troca de dono 30,47%. Isso
**confirmou** os valores já escritos no texto. Se a figura for refeita, manter a malha fina.

### `arquitetura_rnt.png`
Quatro painéis: rede enrolada, rede desenrolada nos 5 instantes (com `W` e `U` idênticos em todas as
cópias), caminho completo do dado com a contagem de parâmetros do Keras, e o gráfico do eco de um
pulso único (0,4621 → 0,1367).

### `treinamento_rnt.png`
BPTT, TBPTT e RTRL sobre a **mesma** cadeia de oito instantes, de propósito: o que muda é só o
caminho do gradiente. Mais tabela comparativa.

### `celula_lstm.png`
Os quatro portões, a esteira do cell state, por que resolve o vanishing, e a tabela neurônio simples
× LSTM × denso (100 / 2.600 / 10.400 parâmetros — a LSTM é exatamente 4× o recorrente simples).
