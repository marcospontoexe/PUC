# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-09-05 (sem hora registada)
- **Sessão nº:** 1
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
- Nenhuma pendência nesta frente; o resumo está maduro e cobre profundamente MLP e CNN
  (RNC/RNT das unidades 05-08 ainda estão apenas no nível do resumo original, sem os
  aprofundamentos que MLP/CNN receberam).

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

## 3. Em andamento 🔧
Nenhuma tarefa em andamento no momento deste checkpoint. Ambas as frentes estão em ponto de
entrega/revisão.

## 4. Próximos passos (planejado) 📋
Nenhum passo obrigatório pendente. Possibilidades, caso o utilizador queira continuar:
1. Frente A: aplicar aos PDFs 05-08 (RNC/RNT) o mesmo nível de aprofundamento que MLP/CNN
   já receberam no `Resumo.md`.
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
  - Novo/atualizado: `CONTEXTO.md` (este ficheiro).
  - Novos em `atividade_1/Python/`: `S4_MLP_partB.py`, `S4_CNN_partB.py`,
    `S4_MLP_aug.py`, `S4_CNN_aug.py`.
  - Modificados em `atividade_1/Python/`: `S4_MLP.py`, `S4_CNN.py` (parâmetros ajustados,
    bugs de ativação/perda corrigidos, seed fixa, prints de previsão adicionados).
  - Novo em `atividade_1/`: `Atividade_Somativa_1_Respondida.docx` (relatório final).
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
maduro para MLP/CNN; RNC/RNT ainda no nível básico). Se for sobre a **atividade somativa**,
os 4 scripts finais e o `.docx` de resposta já estão prontos em `atividade_1/` — falta só
o utilizador preencher o nome na capa e, se quiser, revisar/rodar no Spyder para ver os
gráficos interativos.
