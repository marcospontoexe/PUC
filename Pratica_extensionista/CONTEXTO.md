# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-10-14 20:36
- **Sessão nº:** 2
- **Status geral:** em andamento

## 1. Objetivo da tarefa
Planejar e documentar as práticas extensionistas do curso Tecnologia em IA Aplicada (PUCPR EAD), que somam 224 h. O plano atual é Formação (30 h) + **duas Prestações de serviços** (100 h cada), totalizando 230 h:
1. Harness para rodar um LLM aberto num computador local de uma startup, reduzindo os gastos com assinaturas de IA.
2. Modelo de regressão que estima o peso da carga de um AGV a partir da corrente e da velocidade do motor.

## 2. Já feito ✅
- Criado e atualizado o [CLAUDE.md](CLAUDE.md), com as regras da extensão, o mapa dos PDFs, a estrutura do Conecta e os documentos.
- **Prestação 1 (harness):** plano completo em [DOCS/prestacao-1-harness-llm.md](DOCS/prestacao-1-harness-llm.md). Ele traz a descrição de 493 caracteres, as 12 etapas que somam 100 h, os campos do Conecta e o uso de Sistemas Especialistas no 1.11. A prática foi convertida de Projeto para Prestação de serviços em 2026-10-14.
- **Prestação 2 (AGV):** plano completo em [DOCS/prestacao-2-agv-regressao.md](DOCS/prestacao-2-agv-regressao.md), com a descrição de 490 caracteres, as 11 etapas que somam 100 h, o ODS, os pontos técnicos e a relação com a teoria.
- A Carta de apresentação e o Termo de aceite já foram emitidos e estão em [documentação/](documenta%C3%A7%C3%A3o/). Esse Termo serve para uma prática só, então a segunda vai precisar de outro.

## 3. Em andamento 🔧
- Nenhuma tarefa ficou pela metade.
- Próximo passo imediato: o usuário atualizar a Calculadora, mudando a prática do harness para Prestação de serviços (com a nova descrição) e cadastrando a prestação do AGV.

## 4. Próximos passos (planejado) 📋
1. **Na Calculadora** (feito pelo usuário):
   - trocar o tipo do harness para Prestação de serviços;
   - cadastrar a prestação do AGV;
   - gerar o relatório e postar na Formação.
2. Concluir a Formação: notas ≥ 7 nos testes, planejamento "apto" e simulação "apto".
3. Responder às pendências de elegibilidade do AGV (seção 7).
4. Redigir os campos do planejamento de cada prestação (1.1 a 1.11). Isso depende dos dados da seção 7.
5. Colher os Termos de aceite (um por prática), criar as práticas no Conecta, postar e aguardar "apto".
6. Executar, registrar as evidências e postar os campos 2.1 a 2.6.

## 5. Decisões e raciocínio 🧠
- "Até 500 linhas" foi interpretado como **500 caracteres**, o limite do campo no AVA.
- **Harness como Prestação de serviços:** decisão do usuário. O núcleo é entregar uma solução técnica a uma empresa, como nos exemplos do FAQ. Como Projeto, exigiria evidenciar pesquisa e ensino, com risco no critério 6.
- **ODS:**
  - harness: ODS 8, meta 8.2, e ESG de governança;
  - AGV: ODS 9, meta 9.4; a alternativa é ODS 8, meta 8.8, se o foco for segurança.
- **AGV, viabilidade técnica:** o sinal de massa aparece principalmente na aceleração (F = m·a). Usar validação cruzada agrupada por corrida.
- Sistemas Especialistas entra no 1.11 do harness só como apoio de método.

## 6. Estado do projeto / ambiente
- Pasta `Pratica_extensionista` do repo `PUC` (branch `main`). O `git` não está no PATH; o usuário commita pelo GitHub Desktop.
- Ainda não commitados (provavelmente): [CLAUDE.md](CLAUDE.md), este CONTEXTO.md, [DOCS/](DOCS/) e os PDFs adicionados pelo usuário.
- A [Calculadora.pdf](Calculadora.pdf) ainda mostra o estado antigo: 1 Projeto. Ela precisa ser reexportada depois da atualização.

## 7. Bloqueios e pendências ⚠️
- **Harness, dados da startup:** área de atuação, número de funcionários, gasto mensal com assinaturas de IA e hardware.
- **AGV, elegibilidade:**
  - em que empresa fica o AGV;
  - se é o local de trabalho do usuário;
  - se a atividade é tarefa remunerada do emprego (não pode ser);
  - se há política de propriedade intelectual da empresa em conflito com o Anexo 2.
- **AGV, dados técnicos:** quais sinais são registrados e com que taxa de amostragem.
- **Ambas:** confirmar que a Formação está concluída e que o usuário não é sócio das empresas.
- **Dados pessoais:** a [Calculadora.pdf](Calculadora.pdf) e a Carta têm nome e RA do usuário. Ele precisa decidir sobre o commit, caso o repositório seja público.

## 8. Comandos úteis
- Extrair o texto de um PDF (gravar em UTF-8 fora do repo; nomes com acento falham como argumento no PowerShell 5.1, então use `glob`):
  ```powershell
  python -c "import pypdf,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n=== PAGE ===\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" "<arquivo>.pdf" "<scratchpad>\saida.txt"
  ```
- Os PDFs de infográfico (guia, critérios, como registrar) não têm texto extraível: leia-os como imagem (Read com `pages`).

## 9. Como retomar
Leia este arquivo, o [CLAUDE.md](CLAUDE.md) e os dois planos em [DOCS/](DOCS/). Pergunte ao usuário se a Calculadora já foi atualizada e peça os dados da seção 7. Depois continue pelo passo 4 da seção 4: redigir os campos 1.1 a 1.11 de cada prestação.
