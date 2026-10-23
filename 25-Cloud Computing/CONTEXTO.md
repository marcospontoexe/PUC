# CONTEXTO DA SESSÃO

- **Última atualização:** 2026-10-22 22:03
- **Sessão nº:** 2
- **Status geral:** pronto para revisão

## 1. Objetivo da tarefa
Estudar a disciplina Cloud Computing (PUCPR EAD). O usuário quer **aprender** o conteúdo, então o material de apoio é um resumo detalhado das 8 unidades em PDF.

## 2. Já feito ✅
- Sessão 1: criados [CLAUDE.md](CLAUDE.md) e [resumo.md](resumo.md), o resumo detalhado das 8 unidades com diagramas mermaid, perguntas de fixação, lições de custo e glossário.
- Entre as sessões, o usuário editou o título da Unidade 2 no resumo para incluir "TIC (Tecnologia da Informação e Comunicação)".
- Sessão 2: o usuário reexportou o PDF da Unidade 2 e adicionou o PDF 3.1. O [resumo.md](resumo.md) foi atualizado:
  - Unidade 2: tabela com os 3 exemplos completos de "como escolher" (pública × local × privada), a definição oficial de nuvem híbrida e uma pergunta de fixação nova.
  - Unidade 3: tabela de levantamento alinhada às 15 perguntas do infográfico do PDF 3.1.
  - Sumário: link da Unidade 2 corrigido e link do PDF 3.1 adicionado.
- [CLAUDE.md](CLAUDE.md) atualizado: os infográficos não estão mais cortados, como ler a p. 10 da Unidade 2 e uma linha nova para o PDF 3.1.
- Sessão 2: resolvida a [atividade formativa 1](atividade%20forrmativa/atividade_1.md), sobre a estratégia de TIC na nuvem para uma agência de marketing de 15 pessoas. A solução usa Microsoft 365 e Azure (Brazil South), separa os recursos por modelo (SaaS, PaaS, IaaS, FaaS) e por local (nuvem ou escritório) e inclui segurança, custos e a ordem de implantação.

## 3. Em andamento 🔧
- nenhum

## 4. Próximos passos (planejado) 📋
- Aguardar a revisão do usuário sobre o [resumo.md](resumo.md) e sobre a solução da [atividade 1](atividade%20forrmativa/atividade_1.md).
- Se o usuário trocar mais PDFs por versões completas, reler as imagens e atualizar o resumo.
- Possíveis extensões, só se o usuário pedir: um simulado com mais questões e um roteiro de prática no Azure.

## 5. Decisões e raciocínio 🧠
- O resumo segue a ordem do material e usa os exemplos do professor.
- Complementos que não estão nos PDFs (CaaS, BYOL, health probes, tags, comandos ssh/ping/telnet) ficam marcados como **Nota do resumo**.
- Nuvem híbrida: o cartão do glossário define como "nuvens públicas e privadas integradas"; o texto da unidade inclui também os servidores locais. O resumo registra as duas formas.
- O PDF antigo da Unidade 3 continua com o infográfico cortado na p. 20; a fonte das 15 perguntas é o PDF 3.1.
- Atividade 1: "em limite no orçamento" foi lido como **sem** limite, porque o enunciado continua com "o que tiver que ser contratado, será!". O provedor escolhido foi a Microsoft (Azure + Microsoft 365), pela identidade única, pela região no Brasil (LGPD e latência) e por ser o provedor usado no curso.

## 6. Estado do projeto / ambiente
- Pasta `25-Cloud Computing` dentro do repositório `PUC` (branch `main`). Contém 9 PDFs (8 unidades e o 3.1), [CLAUDE.md](CLAUDE.md), [resumo.md](resumo.md) e este arquivo.
- O `git` não está no PATH; o usuário commita pelo GitHub Desktop.

## 7. Bloqueios e pendências ⚠️
- nenhum

## 8. Comandos úteis
- Extrair o texto de um PDF: veja o comando `pypdf` em [CLAUDE.md](CLAUDE.md#como-ler-os-pdfs).
- Infográfico com letra miúda: extrair a imagem embutida com `pypdf` (`page.images`), recortar e ampliar com o PIL (detalhes em [CLAUDE.md](CLAUDE.md#como-ler-os-pdfs)).

## 9. Como retomar
Leia este arquivo e o [CLAUDE.md](CLAUDE.md). Depois, pergunte ao usuário o que achou das atualizações no [resumo.md](resumo.md) e siga a seção 4.
