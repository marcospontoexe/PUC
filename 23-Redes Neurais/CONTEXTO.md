# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-09-22
- **Sessão nº:** 5
- **Status geral:** pronto para revisão

> Este ficheiro é um **índice**. O detalhe de cada tópico está em [DOCS/](DOCS/), para não
> sobrecarregar a janela de contexto de quem só precisa saber onde as coisas estão.

## 1. Objetivo da tarefa

Estudar a disciplina **Redes Neurais** (PUCPR), com dois produtos: (a) o [Resumo.md](Resumo.md),
material de estudo aprofundado dos 8 PDFs da disciplina; (b) as atividades práticas, executadas de
verdade, com os modelos treinados e os resultados analisados.

## 2. Já feito ✅

| Tópico | Detalhe em | Estado |
|---|---|---|
| **Resumo de estudo** | [DOCS/resumo-estudo.md](DOCS/resumo-estudo.md) | unidades 01 a 06 aprofundadas; a **03 foi reorganizada por inteiro** (3.1 a 3.18); **07 e 08 ainda no nível básico** |
| **Atividade Somativa 1** (MLP × CNN, unidade 04) | [DOCS/atividade-1-mlp-cnn.md](DOCS/atividade-1-mlp-cnn.md) | relatório `.docx` entregue; falta o nome na capa |
| **Notebook de portfólio e post do LinkedIn** | [DOCS/notebook-e-linkedin.md](DOCS/notebook-e-linkedin.md) | prontos e executados |
| **Atividade da unidade 05** (RNC) | [DOCS/atividade-unidade-5-rnc.md](DOCS/atividade-unidade-5-rnc.md) | parâmetros ajustados e saídas analisadas; **relatório não montado** |
| **Atividade formativa da unidade 06** (RNT) | [DOCS/atividade-unidade-6-rnt.md](DOCS/atividade-unidade-6-rnt.md) | **concluída**: parâmetros ajustados e relatório entregue |
| **Atividade formativa da unidade 07** (RNC + RNT) | [DOCS/atividade-unidade-7.md](DOCS/atividade-unidade-7.md) | **concluída**: as duas partes ajustadas e relatório entregue |
| **Atividade Somativa 2** (unidade 08, RNC + RNT) | [DOCS/atividade-somativa-2.md](DOCS/atividade-somativa-2.md) | **concluída**: markdown e `.docx` entregues; falta o nome na capa |
| **As 8 figuras do Resumo** | [DOCS/figuras.md](DOCS/figuras.md) | todas geradas, conferidas e inseridas |

## 3. Em andamento 🔧

Nenhum. Nenhuma tarefa ficou pela metade neste checkpoint.

## 4. Próximos passos (planejado) 📋

1. **Aprofundar as unidades 07 e 08** no [Resumo.md](Resumo.md), no mesmo nível das unidades 02,
   03, 05 e 06. Ver o padrão em [DOCS/resumo-estudo.md](DOCS/resumo-estudo.md).
3. **Montar o relatório da atividade da unidade 05** (DOCX ou PDF, para o AVA). Todos os dados,
   tabelas e a figura já existem — ver [DOCS/atividade-unidade-5-rnc.md](DOCS/atividade-unidade-5-rnc.md).
4. **Preencher "Nome Completo:"** nas capas de
   [atividade_1/Atividade_Somativa_1_Respondida.docx](atividade_1/Atividade_Somativa_1_Respondida.docx)
   e [atividade_2/Atividade_Somativa_2_Respondida.docx](atividade_2/Atividade_Somativa_2_Respondida.docx).
5. **Decidir sobre `Resumo.md.bak`** (154 KB, na raiz) e sobre os scripts geradores das figuras
   (ver seção 7).
6. Opcional: limpar a pasta duplicada `C:\RN\RN`, resquício da extração do `.rar`.

## 5. Decisões e raciocínio 🧠

Decisões que valem para o projeto inteiro. As específicas de cada tópico estão nos ficheiros de
[DOCS/](DOCS/).

- **O [Resumo.md](Resumo.md) é material teórico.** Ele **não** menciona a pasta [RNC/](RNC/), o
  `S5_RNC.py`, as bases de dados nem resultados de atividade. O utilizador removeu esse conteúdo
  de propósito. **Não reintroduzir sem pedido explícito.** Referências ao código das unidades 07/08
  que já estavam lá são aceitáveis.
- **O utilizador vem removendo as ⭐ dos títulos** do Resumo. Não acrescentar estrelas em seções novas.
- **Todo número que entra no Resumo ou num relatório é conferido por script antes de ser escrito.**
  Vários dos achados mais importantes vieram de medir em vez de supor. Manter essa prática.
- **Em série temporal, comparar sempre com um preditor trivial.** Na atividade da unidade 06, a
  previsão ingênua ("amanhã = hoje") **bateu** a LSTM treinada nas três métricas. Um R² de 0,99
  isolado não demonstra aprendizado nenhum.
- **Toda figura é inspecionada renderizada antes de ser dada por pronta.** Em todas elas apareceram
  colisões de rótulo que só o olho pega. Ver [DOCS/figuras.md](DOCS/figuras.md).
- **Ao renumerar seções por script, textos autorais novos não podem passar pela função de correção
  de referências** — senão são remapeados duas vezes. Aconteceu na reorganização da unidade 03.
- **Nunca inventar o nome do utilizador.** O e-mail não é um nome verificável.
- **Ao montar um `.docx` a partir de um template cujo corpo é esvaziado, renumerar os `<wp:docPr>`
  das imagens** para ids altos. Sem isso o Word recusa o arquivo como "aparentemente corrompido" a
  partir da quarta imagem, enquanto o `python-docx` o abre sem reclamar. Receita e diagnóstico em
  [DOCS/atividade-somativa-2.md](DOCS/atividade-somativa-2.md).
- **Imprecisões dos materiais da disciplina sinalizadas no Resumo**, por valor pedagógico: unidade 08
  (`inshape3 = combinacao2.shape[1]`, deveria ser `combinacao3`), unidade 06 ("RMSdrop" é `RMSprop`)
  e a correção conceitual da seção 6.5 (BPTT, TBPTT e RTRL são **algoritmos de treinamento**; LSTM é
  **arquitetura de célula** — o PDF lista os quatro juntos).

## 6. Estado do projeto / ambiente

- **Diretório do projeto:** `c:\Users\marcos\Documents\GitHub\PUC\23-Redes Neurais`
  (o repositório git é a pasta-mãe, `...\GitHub\PUC`).
- **Python:** usar sempre `C:\Users\marcos\anaconda3\python.exe` (TensorFlow 2.21, Keras 3.15,
  scikit-learn, Pillow, matplotlib, pandas, `python-docx`). O `python` do PATH (Windows Store, 3.14)
  **não tem TensorFlow** — não usar para nada de redes neurais.
- **Git não está no PATH.** Usar o binário do GitHub Desktop:
  `C:\Users\marcos\AppData\Local\GitHubDesktop\app-3.6.5\resources\app\git\cmd\git.exe`
- **Node.js não está instalado.** Isso importa para a skill `dataviz`, cujo validador de paleta é em
  Node; foi portado para Python (ver [DOCS/figuras.md](DOCS/figuras.md)).
- **Git, estado real:** branch `main`. **O utilizador vem commitando o trabalho** (ao contrário do
  que este ficheiro afirmava até a sessão 3). Pendente de commit neste momento:
  - Modificados: `CONTEXTO.md`, `DOCS/figuras.md`, `cnn_canal_filtro_kernel.png`, `rascunho.md`.
  - Novos: `DOCS/atividade-unidade-6-rnt.md`, `atividade formativa-s6/`, `atividade formativa-s7/`,
    `foto.png`.
  - Não versionado e pendente de decisão: `Resumo.md.bak`.
- **Fora do git** (seguindo a orientação das atividades): `C:\RN\` contém as 20 imagens PNG do
  MNIST, o `base_veiculos.csv` e as séries `serie_treinamento.csv` / `serie_teste.csv`.

## 7. Bloqueios e pendências ⚠️

- **Nenhum bloqueio técnico.**
- **Risco de perda:** os scripts que geram as 8 figuras do Resumo, e os de busca de parâmetros das
  atividades, vivem no **scratchpad da sessão** (`AppData\Local\Temp\claude\...`), que é volátil.
  [DOCS/figuras.md](DOCS/figuras.md) guarda os parâmetros e decisões de cada figura para permitir
  refazê-las, mas **mover os scripts para o repositório seria mais seguro** — decisão pendente.
- `Resumo.md.bak` (154 KB) continua na raiz, backup da reorganização da unidade 03. Apagar ou manter.
- Pendência do utilizador: preencher "Nome Completo:" na capa do `.docx` da Atividade Somativa 1.
- Os gráficos de treino dos 4 scripts da atividade 1 não foram salvos em arquivo (a execução usou
  backend `Agg`). Para tê-los, rodar no Spyder ou pedir para gerá-los.

## 8. Comandos úteis

```powershell
# rodar qualquer script da disciplina (sempre com o Python do Anaconda)
& "C:\Users\marcos\anaconda3\python.exe" "caminho\do\script.py"

# rodar sem abrir janela de gráfico (útil em terminal)
$env:MPLBACKEND = "Agg"

# as atividades já ajustadas
& "C:\Users\marcos\anaconda3\python.exe" "RNC\S5_RNC.py"
& "C:\Users\marcos\anaconda3\python.exe" "atividade formativa-s6\S6_RNT.py"

# git (não está no PATH)
$git = "C:\Users\marcos\AppData\Local\GitHubDesktop\app-3.6.5\resources\app\git\cmd\git.exe"
& $git -C "C:\Users\marcos\Documents\GitHub\PUC" status
```

Reabrir o Spyder (fluxo oficial da disciplina): Anaconda Navigator → aba Home → Launch.

## 9. Como retomar

Leia este ficheiro e abra **apenas** o ficheiro de [DOCS/](DOCS/) correspondente ao que for pedido;
não é preciso ler todos.

**Todas as atividades da disciplina estão concluídas.** O caminho mais provável de continuação é o
**passo 1 da seção 4**: aprofundar as unidades 07 e 08 no [Resumo.md](Resumo.md), que continuam no
nível básico enquanto as unidades 01 a 06 já foram trabalhadas a fundo.

O roteiro que funcionou nas quatro atividades práticas — ler o enunciado, rodar o código como está,
diagnosticar, buscar parâmetros por varredura com semente fixa e critério declarado antes de ver os
números, comparar com um preditor trivial, e só então escrever o relatório — está documentado em
[DOCS/atividade-unidade-6-rnt.md](DOCS/atividade-unidade-6-rnt.md) e
[DOCS/atividade-somativa-2.md](DOCS/atividade-somativa-2.md).
