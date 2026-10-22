# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Pasta do repositório `PUC` (github.com/marcospontoexe/PUC) com o material da **Formação para Práticas Extensionistas** da PUCPR EAD. O curso do usuário é **Tecnologia em Inteligência Artificial Aplicada**. Só há PDFs exportados do AVA, sem código, build ou testes.

O uso esperado desta pasta é ajudar o usuário a **planejar e redigir práticas extensionistas** que serão postadas na plataforma **Conecta** (AVA > Home > Conecta) e validadas por um professor-tutor. Escrever sempre em pt-BR.

## Como ler os PDFs

- São prints de páginas do AVA. O texto extraído traz, em toda página, o menu lateral repetido e glifos de ícones (caracteres de uso privado). Ignore esse ruído.
- Diagramas e tabelas desenhadas só aparecem lendo o PDF como imagem (Read com `pages`).
- Em [Escopo por cursos.pdf](Escopo%20por%20cursos.pdf) e [Perguntas e Respostas.pdf](Perguntas%20e%20Respostas.pdf), as páginas 1–2 estão em branco.
- Para extrair o texto (com `pypdf`, já instalado), grave em UTF-8 fora do repo. Imprimir no console do PowerShell quebra por causa dos glifos:

```powershell
python -c "import pypdf,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n=== PAGE ===\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" "<arquivo>.pdf" "<scratchpad>\saida.txt"
```

## Onde está cada informação

| Arquivo | Conteúdo útil |
|---|---|
| [Escopo por cursos.pdf](Escopo%20por%20cursos.pdf) | Págs. 6–10: perfil do egresso de IA Aplicada, 28 ideias de práticas do curso, 6 ideias comuns à computação, ODS e ESG sugeridos |
| [Perguntas e Respostas.pdf](Perguntas%20e%20Respostas.pdf) | Regras: tipos e horas, locais, grupo, o que não conta, critérios da Formação |
| [Manual_de_Resposabilidades.pdf](Manual_de_Resposabilidades.pdf) | Deveres do estudante (1.1–1.26), da comunidade e da PUCPR; Anexo 1 (LGPD) e Anexo 2 (propriedade intelectual) |
| Módulos 1–4 | 1: o que é e o que não é extensão; 2: aponta para FAQ/Manual/Resoluções; 3: Calculadora e postagem do planejamento; 4: documentos, evidências, Conecta e critérios de avaliação |
| [Exemplos de Práticas/](Exemplos%20de%20Pr%C3%A1ticas/) | Modelos preenchidos do relatório do Conecta. O de **Projeto** é do próprio curso de IA (mentoria em IA responsável numa escola estadual, ODS 4, meta 4.4). O de **Prestação de serviços** é de Marketing (ODS 5, meta 5.2). |
| [guia.pdf](guia.pdf) | Etapas oficiais (Definição → Planejamento → Execução) em checklist; o tempo de planejamento conta na carga horária |
| [critérios avaliativos das praticas extensionistas.pdf](crit%C3%A9rios%20avaliativos%20das%20praticas%20extensionistas.pdf) | Os 11 critérios do tutor: aderência, impacto, presencialidade, ODS/ESG, experiência, tipo, postagem, qualidade, alinhamento, evidências, documentos |
| [como registrar suas práticas extensionistas.pdf](como%20registrar%20suas%20pr%C3%A1ticas%20extensionistas.pdf) | Evidências obrigatórias e complementares. Produto digital exige gravação de tela, mas isso não substitui foto do estudante junto à comunidade |
| [Calculadora.pdf](Calculadora.pdf) | **224 h** de extensão no total. O PDF ainda mostra 1 Projeto. O plano atual é Formação (30 h) + 2 Prestações de serviços de 100 h cada, detalhadas em [DOCS/](DOCS/) |
| [documentação/](documenta%C3%A7%C3%A3o/) | Modelos em branco: Carta de apresentação + Termo de aceite (já emitidos em nome do usuário), Atestado de matrícula, TCLE, Termo de uso de imagem, Feedback da comunidade |

## Regras que toda proposta precisa cumprir

- **Tipos e carga horária fixos:** Evento 30 h · Workshop/Oficina 30 h · Curso 60 h · Projeto 100 h · Prestação de serviços 100 h. A soma tem de bater com a matriz curricular (10% da carga total do curso; no exemplo da FAQ, Formação 30 h + Aplicação 270 h). Confirme o número na matriz do usuário (AVA > Guia do Estudante > Meu Curso).
- **Presencial obrigatório:** pelo menos uma foto ou vídeo deve mostrar o estudante no local. Rádio, TV e internet servem só como meio de veiculação.
- Precisa de pelo menos **um ODS**, citando a meta específica. ESG entra quando couber.
- Precisa estar alinhada ao **perfil do egresso** e aplicar conhecimentos do curso.
- Precisa gerar **impacto social, ambiental, econômico ou cultural** no contexto local.
- **Não contam como extensão:**
  - atividade 100% a distância;
  - prática na empresa de que o estudante é dono ou único colaborador;
  - estágio;
  - atividades complementares;
  - assistir a um curso como aluno;
  - prática sem ODS ou sem impacto;
  - autobeneficiamento.
- O Termo de aceite é assinado por um terceiro responsável, nunca pelo próprio estudante. O local de trabalho é permitido.
- A prática pode ser individual ou em grupo de até 4 pessoas do mesmo curso, todas presentes. Não há remuneração nem reembolso.
- **Mais de uma prática no mesmo local ou do mesmo tipo:** cada uma precisa de objetivos e entregas finais distintos. Aplicar a mesma prática em dois locais exige um Desafio separado no Conecta para cada local.

## Estrutura do relatório no Conecta

Siga a numeração dos [exemplos](Exemplos%20de%20Pr%C3%A1ticas/), pois o tutor avalia campo a campo:

- **Planejamento:**
  - caracterização do contexto;
  - objetivos (geral e específicos);
  - justificativa;
  - público-alvo e expectativa de participação;
  - ODS/ESG;
  - Termo de aceite;
  - nome do projeto (só no tipo Projeto);
  - etapas com as pessoas envolvidas;
  - materiais e recursos por etapa;
  - cronograma em semanas e horas de dedicação, somando a carga do tipo;
  - resultados esperados (só em Prestação de serviços);
  - relação com a teoria.
- **Execução:**
  - evidências por etapa;
  - feedback do estudante: aprendizados, contribuições, obstáculos e se os objetivos foram atingidos;
  - feedback dos participantes e da comunidade.
- **Relação com a teoria:** deve citar disciplinas que o usuário cursou. Elas são as pastas irmãs em `PUC/`, como `13-Processamento de Linguagem natural (PLN)`, `14-Técnicas de machine learning`, `16-IA aplicada à Saúde` e `19-Agentes Conversacionais`.
- **Coerência:** o tutor confere se planejamento e execução batem entre si. Ao revisar textos, verifique essa coerência.

## Documentos e evidências

- **Carta de apresentação e Termo de aceite:** emitidos juntos. O [guia.pdf](guia.pdf), mais recente, indica AVA > Home > Portal do Estudante > Menu > Protocolos > Incluir Protocolo > "Grad EAD Carta de Apresentação Ativ de Extensão". O Módulo 4 indica AVA > Vida Acadêmica > Minhas Solicitações. É preciso um Termo de aceite por prática.
- **Atestado de matrícula:** emitido pelo mesmo caminho.
- **TCLE:** assinado por cada participante ou entrevistado.
- **Termo de autorização de uso de imagem:** obrigatório para menores, assinado pelos responsáveis.
- **Feedback da comunidade:** preenchido pela própria comunidade, não pelo estudante.
- Os modelos estão em [documentação/](documenta%C3%A7%C3%A3o/) e em AVA > Home > Práticas Extensionistas > Documentos.
- **Ordem obrigatória:** concluir a Formação, depois ter o planejamento considerado "apto" pelo tutor no Conecta (até 15 dias para a correção), e só então executar.
- **Documentos obrigatórios na avaliação:** Termo de aceite e Feedback da comunidade, completos e assinados, mais fotos ou vídeos da aplicação.

## Atenção para o portfólio

Pelo Anexo 2 do Manual, toda **propriedade intelectual nova** criada numa prática extensionista (por exemplo, código ou modelo de ML) pertence à APC/PUCPR. Avise o usuário antes de sugerir publicar esse material como projeto próprio no portfólio. Dados pessoais coletados seguem a LGPD (Anexo 1) e não devem ir para o repositório.
