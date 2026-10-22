# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Pasta do repositório `PUC` (github.com/marcospontoexe/PUC) com o material da disciplina **Sistemas Especialistas** (PUCPR EAD, curso Tecnologia em Inteligência Artificial Aplicada). Há os PDFs das 8 unidades e as entregas de duas atividades formativas. Não há código, build nem testes. Escrever sempre em pt-BR.

## Como ler os arquivos

- Os PDFs das unidades têm texto limpo, sem o ruído de menu do AVA que aparece em outras disciplinas. Figuras, como o ciclo de desenvolvimento da Unidade 8, só aparecem lendo o PDF como imagem (Read com `pages`).
- O Read não abre `.docx`. Use `python-docx` (já instalado) e grave a saída em UTF-8 no scratchpad, porque o console do PowerShell estraga os acentos:

```powershell
# Extrai o texto de um PDF, página a página
python -c "import pypdf,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n=== PAGE ===\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" "<arquivo>.pdf" "<scratchpad>\saida.txt"
# Extrai os parágrafos de um Roteiro.docx (imagens embutidas ficam de fora)
python -c "import docx,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n'.join(p.text for p in docx.Document(sys.argv[1]).paragraphs))" "<arquivo>.docx" "<scratchpad>\saida.txt"
```

## Onde está cada conceito

O resumo de estudo das 8 unidades fica em [resumo.md](resumo.md). Ele não cobre as atividades formativas. O estado da sessão fica em [CONTEXTO.md](CONTEXTO.md).

| Unidade | Conceitos |
|---|---|
| 1 | O que é um SE (ou SBC), quando ele é a escolha certa, ética |
| 2 | Histórico, os três componentes (base de conhecimento, motor de inferência, interface), tipos de SE, conhecimento tácito × explícito |
| 3 | SE × programa convencional, heurísticas, ontologias, entrevista de aquisição de conhecimento |
| 4 | Base de conhecimento |
| 5 | Vantagens e desvantagens |
| 6 | Motor de inferência (encadeamento progressivo e regressivo), interface do usuário |
| 7 | Memória de trabalho, explanação, incerteza (grau de certeza) |
| 8 | Estágios de desenvolvimento, papéis do engenheiro do conhecimento e do especialista de domínio |

## Atividades formativas

Os enunciados não estão na pasta. Só há as respostas do usuário, e as perguntas atendidas aparecem no topo de cada Roteiro.

- [1° atividade formativa/Roteiro.docx](1%C2%B0%20atividade%20formativa/Roteiro.docx): roteiro de entrevista para adquirir conhecimento sobre **navegação autônoma de AMR em ambiente interno**, domínio de robótica do usuário. Cobre técnicas de entrevista por etapa, perguntas por tópico, captação do conhecimento tácito e quais especialistas entrevistar. Recomenda um SE híbrido: regras + fuzzy/neuro-fuzzy + módulos probabilísticos.
- [2° atividade formativa/Roteiro.docx](2%C2%B0%20atividade%20formativa/Roteiro.docx): diagrama e desenho metodológico de um **SE para diagnóstico médico**, com as mesmas três famílias de técnicas.
  - O diagrama embutido no `.docx` é [Knowledge Deployment-2026-03-10-021611.png](2%C2%B0%20atividade%20formativa/Knowledge%20Deployment-2026-03-10-021611.png). Os outros dois PNGs da pasta são versões anteriores.
  - O código-fonte do diagrama não está no repositório. Para mudá-lo, é preciso redesenhá-lo.

## Pontos de atenção no material

- **Número de estágios:** a [Unidade 8](8-Est%C3%A1gios%20de%20desenvolvimento%20de%20um%20sistema%20especialista.pdf) define 5 estágios: identificação, conceitualização, formalização, implementação e testes. A 2ª atividade usa 6 fases, porque separa deploy e manutenção, e acrescenta governança como bloco transversal. Quando a resposta precisar seguir a disciplina, use os 5 da Unidade 8.
- **Encadeamento trocado:** um parágrafo da [Unidade 6](6-Motor%20de%20infer%C3%AAncia%20e%20interface%20do%20usu%C3%A1rio.pdf) inverte os termos e chama de *backward chaining* o raciocínio que parte das condições. O próprio PDF corrige isso mais adiante, citando Durkin (1994):
  - progressivo (*forward*): dos fatos para a conclusão;
  - regressivo (*backward*): da hipótese para os fatos.
- **Engenheiro de dados:** a Unidade 8 usa "engenheiro de dados" como sinônimo de "engenheiro do conhecimento". Os Roteiros usam "engenheiro do conhecimento", que é o termo padrão.
