# Plano do Projeto: harness de LLM local numa startup (100 h)

Prática extensionista do tipo **Projeto**, registrada na [Calculadora](../Calculadora.pdf) para o 3º módulo. Fontes das regras: [guia.pdf](../guia.pdf), [critérios avaliativos](../crit%C3%A9rios%20avaliativos%20das%20praticas%20extensionistas.pdf), [como registrar](../como%20registrar%20suas%20pr%C3%A1ticas%20extensionistas.pdf) e [Perguntas e Respostas.pdf](../Perguntas%20e%20Respostas.pdf).

## Descrição registrada na Calculadora (≤ 500 caracteres)

> Implantação de um modelo de linguagem aberto (LLM) em um computador local de uma startup, por meio de um harness: software que executa o modelo e o integra às ferramentas da equipe. A partir de um levantamento presencial das necessidades, o projeto vai comparar modelos abertos, instalar a solução e capacitar os funcionários para usá-la. O objetivo é reduzir gastos com assinaturas mensais de IA, manter os dados da empresa em ambiente interno e otimizar o tempo dos projetos (ODS 8, meta 8.2).

## 0. Pré-requisitos

1. Concluir a Formação (30 h): nota ≥ 7 em cada teste, relatório da Calculadora "apto" e simulação no Conecta "apto". A Calculadora ainda mostra a Formação como "PLANEJADA".
2. O usuário não pode ser sócio nem o único funcionário da startup, e não pode receber pagamento.
3. Levar a Carta de apresentação e o Termo de aceite (em [documentação/](../documenta%C3%A7%C3%A3o/)) à startup. O responsável preenche nome, CNPJ, endereço e contatos e assina. O estudante também assina. Tirar foto nessa reunião.
4. Criar o projeto no Conecta: AVA > Home > Conecta > Desafios > Projeto > Criar Projeto.

## 1. Planejamento (campos 1.1 a 1.11 do Conecta)

| Campo | Conteúdo |
|---|---|
| 1.1 Contexto | Área da startup, nº de funcionários, gasto mensal com assinaturas de IA, usos atuais de IA, hardware (GPU/VRAM, RAM) |
| 1.2 Objetivos | Geral: implantar LLM aberto local. Específicos: comparar modelos, desenvolver e instalar o harness, capacitar a equipe, medir a economia |
| 1.3 Justificativa | Custo recorrente, dados que hoje saem da empresa (LGPD), autonomia tecnológica |
| 1.4 Público-alvo | Os N funcionários; expectativa de participação na capacitação |
| 1.5 ODS/ESG | ODS 8, meta 8.2 (produtividade por modernização tecnológica e inovação); ESG governança: dados no ambiente interno |
| 1.6 | Termo de aceite assinado |
| 1.7 Nome | Sugestão: "IA Local: implantação de LLM aberto para redução de custos em uma startup" |
| 1.8–1.10 | Tabela de etapas abaixo |
| 1.11 Teoria | PLN (13), Agentes Conversacionais (19), Redes Neurais (23), Segurança da informação (10), Ética (3) e Sistemas Especialistas (17), esta última como apoio de método (ver abaixo) |

Postar e **esperar "apto"** do tutor (até 15 dias) antes de executar.

## 2. Etapas e horas (somam 100 h; planejamento também conta)

| # | Etapa | Horas | Presencial |
|---|---|---|---|
| 1 | Reunião inicial e Termo de aceite | 2 | sim |
| 2 | Diagnóstico: entrevista com a equipe, tarefas, custos atuais (linha de base em R$/mês) e hardware | 6 | sim |
| 3 | Redação e postagem do planejamento | 6 | |
| 4 | **Pesquisa:** comparar 3–4 modelos abertos quantizados que caibam no hardware; checar licença de uso comercial; testar com 5–10 tarefas reais (qualidade, tokens/s, memória); planilha vira evidência | 16 | |
| 5 | **Serviço:** harness = runtime local (ex.: Ollama ou llama.cpp) + API e interface web só na rede interna + modelos de prompt para tarefas recorrentes; RAG com documentos internos é opcional | 30 | |
| 6 | Instalação e testes no computador da startup | 8 | sim |
| 7 | Preparar material da capacitação | 4 | |
| 8 | **Ensino:** oficina de uso (TCLE de cada participante, Termo de uso de imagem de quem aparecer, lista de presença) | 4 | sim |
| 9 | Acompanhamento e ajustes (2–4 semanas de uso real) | 8 | parcial |
| 10 | Medir resultados e entrega final (apresentação + manual) | 6 | sim |
| 11 | Coleta de feedback (Feedback da comunidade + questionário da equipe) | 2 | sim |
| 12 | Redação e postagem da execução | 8 | |

As etapas 4, 5 e 8 cobrem pesquisa, serviço e ensino. É isso que caracteriza o tipo Projeto (critério 6).

## 3. Execução (campos 2.1 a 2.7 do Conecta)

- 2.1 Evidências por etapa. Pelo menos uma foto ou vídeo do estudante na startup. A gravação de tela do harness não substitui essa foto. Borrar dados da empresa nas telas.
- 2.2–2.5: aprendizados, contribuições, obstáculos e objetivos. Comparar a economia com a linha de base da etapa 2.
- 2.6–2.7: questionário dos funcionários e Feedback da comunidade assinado pelo responsável (obrigatório).
- Conferir os 11 critérios antes de enviar. O critério 9 (alinhamento planejamento × execução) é o mais sensível.

## Sistemas Especialistas no 1.11

É apoio de método, não a base teórica principal. O harness não é um SE clássico.

- **Unidade 8:** os 5 estágios se encaixam nas etapas do projeto: identificação = etapa 2; conceitualização = escolha de tarefas e arquitetura; formalização = prompts e benchmark (etapa 4); implementação = etapas 5–6; testes = etapas 6 e 9. Só citar se a execução seguir de fato essa sequência.
- **Unidade 3:** técnicas de entrevista de aquisição de conhecimento aplicadas na etapa 2.
- **Unidade 2:** modelos de prompt transformam conhecimento tácito da equipe em explícito.
- **Unidade 7:** limites de explanação e incerteza do LLM (alucinação), tratados na capacitação.
- **Unidade 4:** base de conhecimento. Só vale se houver RAG.

Frase sugerida:

> Da disciplina de Sistemas Especialistas, o projeto aplica os estágios de desenvolvimento (identificação, conceitualização, formalização, implementação e testes) para organizar a implantação, e as técnicas de aquisição de conhecimento para conduzir as entrevistas com a equipe e transformar o conhecimento tácito das tarefas recorrentes em modelos de prompt explícitos.

## Riscos

- **Propriedade intelectual:** pelo Anexo 2 do [Manual](../Manual_de_Resposabilidades.pdf), o código do harness pertence à APC/PUCPR. Isso afeta publicar o código no portfólio.
- **Presencialidade:** o desenvolvimento é remoto, por isso os momentos marcados como presenciais na tabela precisam ter fotos ou vídeos.
