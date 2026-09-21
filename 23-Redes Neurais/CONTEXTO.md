# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-09-20
- **Sessão nº:** 3
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
| **Resumo de estudo** | [DOCS/resumo-estudo.md](DOCS/resumo-estudo.md) | unidades 01 a 06 aprofundadas; **07 e 08 ainda no nível básico** |
| **Atividade Somativa 1** (MLP × CNN, unidade 04) | [DOCS/atividade-1-mlp-cnn.md](DOCS/atividade-1-mlp-cnn.md) | relatório `.docx` entregue; falta o nome na capa |
| **Notebook de portfólio e post do LinkedIn** | [DOCS/notebook-e-linkedin.md](DOCS/notebook-e-linkedin.md) | prontos e executados |
| **Atividade da unidade 05** (RNC) | [DOCS/atividade-unidade-5-rnc.md](DOCS/atividade-unidade-5-rnc.md) | parâmetros ajustados e saídas analisadas; **relatório não montado** |
| **As 8 figuras do Resumo** | [DOCS/figuras.md](DOCS/figuras.md) | todas geradas, conferidas e inseridas |

## 3. Em andamento 🔧

Nenhum. Nenhuma tarefa ficou pela metade neste checkpoint.

## 4. Próximos passos (planejado) 📋

1. **Aprofundar as unidades 07 e 08** no [Resumo.md](Resumo.md), no mesmo nível das unidades 02,
   03, 05 e 06. Ver o padrão seguido em [DOCS/resumo-estudo.md](DOCS/resumo-estudo.md).
2. **Montar o relatório da atividade da unidade 05** (DOCX ou PDF, para o AVA). Todos os dados,
   tabelas e a figura já existem — ver [DOCS/atividade-unidade-5-rnc.md](DOCS/atividade-unidade-5-rnc.md).
3. **Preencher "Nome Completo:"** na capa de
   [atividade_1/Atividade_Somativa_1_Respondida.docx](atividade_1/Atividade_Somativa_1_Respondida.docx).
4. **Decidir sobre os scripts geradores das figuras**, que hoje vivem só no scratchpad volátil
   (ver seção 7).
5. Opcional: limpar a pasta duplicada `C:\RN\RN`, resquício da extração do `.rar`.

## 5. Decisões e raciocínio 🧠

Decisões que valem para o projeto inteiro. As específicas de cada tópico estão nos ficheiros de
[DOCS/](DOCS/).

- **O [Resumo.md](Resumo.md) é material teórico.** Ele **não** menciona a pasta [RNC/](RNC/), o
  `S5_RNC.py`, a base de veículos nem resultados de atividade. O utilizador removeu esse conteúdo
  de propósito. **Não reintroduzir sem pedido explícito.** Referências ao código das unidades 07/08
  que já estavam lá são aceitáveis.
- **O utilizador vem removendo as ⭐ dos títulos** do Resumo. Não acrescentar estrelas em seções novas.
- **Todo número que entra no Resumo é conferido por script antes de ser escrito.** Vários achados da
  sessão vieram justamente de medir em vez de supor. Manter essa prática.
- **Toda figura é inspecionada renderizada antes de ser dada por pronta.** Em todas elas apareceram
  colisões de rótulo que só o olho pega. Ver [DOCS/figuras.md](DOCS/figuras.md).
- **Nunca inventar o nome do utilizador.** O e-mail não é um nome verificável.
- **Imprecisões dos materiais da disciplina sinalizadas no Resumo**, por valor pedagógico: unidade 08
  (`inshape3 = combinacao2.shape[1]`, deveria ser `combinacao3`), unidade 06 ("RMSdrop" é `RMSprop`)
  e a correção conceitual da seção 6.5 (BPTT, TBPTT e RTRL são **algoritmos de treinamento**; LSTM é
  **arquitetura de célula** — o PDF lista os quatro juntos).

## 6. Estado do projeto / ambiente

- **Diretório do projeto:** `c:\Users\marcos\Documents\GitHub\PUC\23-Redes Neurais`
- **Python:** usar sempre `C:\Users\marcos\anaconda3\python.exe` (TensorFlow 2.21, Keras 3.15,
  scikit-learn, Pillow, matplotlib, pandas, e `python-docx` instalado nesta sessão). O `python` do
  PATH (Windows Store, 3.14) **não tem TensorFlow** — não usar para nada de redes neurais.
- **Node.js não está instalado** nesta máquina. Isso importa para a skill `dataviz`, cujo validador
  de paleta é em Node; foi portado para Python (ver [DOCS/figuras.md](DOCS/figuras.md)).
- **Git:** branch `main`, **nada commitado** em nenhuma das sessões. Alterações pendentes:
  - Modificados: [Resumo.md](Resumo.md), [RNC/S5_RNC.py](RNC/S5_RNC.py),
    `atividade_1/Python/S4_MLP.py` e `S4_CNN.py`.
  - Novos na raiz: os 7 PNGs de figura, este `CONTEXTO.md` e a pasta [DOCS/](DOCS/).
  - Novos em `atividade_1/`: 4 scripts (`*_partB.py`, `*_aug.py`), o `.docx` do relatório, o
    notebook, o post do LinkedIn e a imagem dele.
  - Novo em [RNC/](RNC/): `resultado_rnc.png`.
- **Fora do git** (seguindo a orientação das atividades): `C:\RN\` contém as 20 imagens PNG do
  MNIST e o `base_veiculos.csv`.

## 7. Bloqueios e pendências ⚠️

- **Nenhum bloqueio técnico.**
- **Risco de perda:** os scripts que geram as 7 figuras do Resumo vivem no **scratchpad da sessão**
  (`AppData\Local\Temp\claude\...`), que é volátil. Se alguma figura precisar ser refeita numa
  sessão futura, ela terá de ser reescrita do zero. [DOCS/figuras.md](DOCS/figuras.md) guarda os
  parâmetros e decisões de cada uma para tornar isso possível, mas **mover os scripts para o
  repositório seria mais seguro** — decisão pendente do utilizador.
- Pendência do utilizador: preencher "Nome Completo:" na capa do `.docx` da Atividade Somativa 1.
- Os gráficos de treino dos 4 scripts da atividade 1 não foram salvos em arquivo (a execução usou
  backend `Agg`). Para tê-los, rodar no Spyder ou pedir para gerá-los.

## 8. Comandos úteis

```powershell
# rodar qualquer script da disciplina (sempre com o Python do Anaconda)
& "C:\Users\marcos\anaconda3\python.exe" "caminho\do\script.py"

# a atividade da unidade 05, já com os parâmetros ajustados
& "C:\Users\marcos\anaconda3\python.exe" "RNC\S5_RNC.py"

# rodar sem abrir janela de gráfico (útil em terminal)
$env:MPLBACKEND = "Agg"

# commitar o trabalho (ainda não feito em nenhuma sessão)
git add .; if ($?) { git commit -m "Resumo aprofundado ate a unidade 06, atividades 04 e 05" }
```

Reabrir o Spyder (fluxo oficial da disciplina): Anaconda Navigator → aba Home → Launch.

## 9. Como retomar

Leia este ficheiro e abra **apenas** o ficheiro de [DOCS/](DOCS/) correspondente ao que for pedido;
não é preciso ler todos. O caminho mais provável de continuação é o **passo 1 da seção 4**:
aprofundar as unidades 07 e 08 do [Resumo.md](Resumo.md), seguindo o padrão descrito em
[DOCS/resumo-estudo.md](DOCS/resumo-estudo.md).
