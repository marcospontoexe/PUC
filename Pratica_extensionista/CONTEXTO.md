# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-10-13 22:48
- **Sessão nº:** 1
- **Status geral:** em andamento

## 1. Objetivo da tarefa
Planejar e documentar as práticas extensionistas do curso Tecnologia em IA Aplicada (PUCPR EAD), que somam 224 h. A prática atual é um **Projeto (100 h)**: implantar um harness para rodar um LLM aberto num computador local de uma startup, reduzindo os gastos com assinaturas de IA.

## 2. Já feito ✅
- Criado e depois atualizado o [CLAUDE.md](CLAUDE.md). Ele traz as regras da extensão, o mapa dos PDFs, a estrutura do relatório do Conecta, os documentos exigidos e a ordem obrigatória (Formação → planejamento "apto" → execução).
- Escrita a descrição curta do projeto (≤ 500 caracteres). O usuário já a registrou na [Calculadora.pdf](Calculadora.pdf).
- Definido o passo a passo completo do projeto, com 12 etapas que somam 100 h, o conteúdo de cada campo do Conecta e as evidências: [DOCS/plano-projeto-harness.md](DOCS/plano-projeto-harness.md).
- Confirmado que Sistemas Especialistas entra no campo 1.11 como apoio de método (detalhes no mesmo DOCS).
- A Carta de apresentação e o Termo de aceite já foram emitidos e estão em [documentação/](documenta%C3%A7%C3%A3o/).

## 3. Em andamento 🔧
- Nenhuma tarefa ficou pela metade.
- Próximo passo imediato: redigir os textos dos campos 1.1 a 1.11 do planejamento. Isso depende de dados da startup (ver seção 7).

## 4. Próximos passos (planejado) 📋
1. Concluir a Formação: notas ≥ 7 nos testes, planejamento "apto" e simulação "apto". A Calculadora ainda mostra a Formação como "PLANEJADA".
2. Colher a assinatura do Termo de aceite na startup, presencialmente, e tirar foto.
3. Criar o projeto no Conecta (Desafios > Projeto).
4. Redigir os campos 1.1 a 1.11 com base em [DOCS/plano-projeto-harness.md](DOCS/plano-projeto-harness.md), postar e aguardar "apto".
5. Executar as etapas 4 a 11 do plano, registrando as evidências.
6. Redigir e postar os campos 2.1 a 2.7.
7. Planejar as **94 h restantes** (224 − 30 − 100) em outras práticas.

## 5. Decisões e raciocínio 🧠
- O pedido de "até 500 linhas" foi interpretado como **500 caracteres**, porque é o limite de campo do AVA e o pedido era de uma descrição breve.
- ODS escolhido: **ODS 8, meta 8.2**. Ele não está na lista de destaque do curso, mas os 17 ODS são aceitos. ESG pelo lado da governança (dados ficam internos).
- O tipo Projeto se justifica porque o plano combina pesquisa (comparar modelos), serviço (harness) e ensino (oficina).
- Sistemas Especialistas não é a base teórica principal. A base é PLN, Agentes Conversacionais e Redes Neurais. A Unidade 4 só vale se houver RAG.
- Todo o material fica em pt-BR, como as pastas irmãs.

## 6. Estado do projeto / ambiente
- Pasta `Pratica_extensionista` do repo `PUC` (branch `main`). O `git` não está no PATH; o usuário commita pelo GitHub Desktop.
- Ainda não commitados (provavelmente): [CLAUDE.md](CLAUDE.md), este CONTEXTO.md, [DOCS/](DOCS/) e os PDFs novos que o usuário adicionou (guia, critérios, como registrar, Calculadora, [documentação/](documenta%C3%A7%C3%A3o/)).
- O mapa de onde está cada informação nos PDFs fica no [CLAUDE.md](CLAUDE.md).
- `pypdf` e `python-docx` já estão instalados.

## 7. Bloqueios e pendências ⚠️
- **Dados da startup para redigir o 1.1–1.11:** área de atuação, número de funcionários, gasto mensal com assinaturas de IA e hardware disponível (GPU/VRAM, RAM).
- **Confirmar com o usuário:**
  - se a Formação já foi concluída;
  - que ele não é sócio nem único funcionário da startup.
- **Propriedade intelectual:** pelo Anexo 2 do Manual, o código do harness pertence à PUCPR, o que afeta publicá-lo no portfólio.
- **Dados pessoais:** a [Calculadora.pdf](Calculadora.pdf) e a Carta têm nome e RA do usuário. Ele precisa decidir se vai commitá-los, caso o repositório seja público.

## 8. Comandos úteis
- Extrair o texto de um PDF (gravar em UTF-8 fora do repo; nomes com acento falham como argumento no PowerShell 5.1, então use `glob`):
  ```powershell
  python -c "import pypdf,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n=== PAGE ===\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" "<arquivo>.pdf" "<scratchpad>\saida.txt"
  ```
- Os PDFs de infográfico (guia, critérios, como registrar) não têm texto extraível: leia-os como imagem (Read com `pages`).

## 9. Como retomar
Leia este arquivo, o [CLAUDE.md](CLAUDE.md) e o [DOCS/plano-projeto-harness.md](DOCS/plano-projeto-harness.md). Depois peça ao usuário os dados da seção 7 e continue pelo passo 4 da seção 4: redigir os campos 1.1 a 1.11 do planejamento no Conecta.
