# Prestação de serviços 1: harness de LLM local numa startup (100 h)

Prática do tipo **Prestação de serviços**. Até 2026-10-14 ela estava registrada como Projeto. O usuário escolheu trocar porque o núcleo do trabalho é entregar uma solução técnica a uma empresa, que é o caso típico de prestação de serviços segundo o [Perguntas e Respostas.pdf](../Perguntas%20e%20Respostas.pdf). **A troca de tipo precisa ser feita na Calculadora antes de postar o planejamento.**

Fontes das regras: [guia.pdf](../guia.pdf), [critérios avaliativos](../crit%C3%A9rios%20avaliativos%20das%20praticas%20extensionistas.pdf), [como registrar](../como%20registrar%20suas%20pr%C3%A1ticas%20extensionistas.pdf) e o [exemplo de Prestação de serviços](../Exemplos%20de%20Pr%C3%A1ticas/Exemplo_PraticasExtensionistas_Prestacao_Servicos_3.pdf).

## Descrição para a Calculadora (493 caracteres)

> Implantação de um modelo de linguagem aberto (LLM) em um computador local de uma startup, por meio de um harness: software que executa o modelo e o integra às ferramentas da equipe. A partir de um levantamento presencial das necessidades, o serviço vai comparar modelos abertos, instalar a solução e treinar os funcionários para usá-la. O objetivo é reduzir gastos com assinaturas mensais de IA, manter os dados da empresa em ambiente interno e otimizar o tempo dos projetos (ODS 8, meta 8.2).

## 0. Pré-requisitos

1. Concluir a Formação (30 h): nota ≥ 7 em cada teste, relatório da Calculadora "apto" e simulação no Conecta "apto".
2. O usuário não pode ser sócio nem o único funcionário da startup, e não pode receber pagamento.
3. Levar a Carta de apresentação e o Termo de aceite (em [documentação/](../documenta%C3%A7%C3%A3o/)) à startup. O responsável preenche e assina, e o estudante também. Tirar foto na reunião.
4. Criar a prática no Conecta: AVA > Home > Conecta > Desafios > Prestação de serviços > Criar Projeto.

## 1. Planejamento (campos do Conecta, numeração do exemplo de prestação)

| Campo | Conteúdo |
|---|---|
| 1.1 Contexto | Área da startup, nº de funcionários, gasto mensal com assinaturas de IA, usos atuais de IA, hardware (GPU/VRAM, RAM) |
| 1.2 Objetivos da prestação | Geral: implantar um LLM aberto local. Específicos: selecionar o modelo adequado ao hardware, instalar o harness, treinar a equipe, medir a economia |
| 1.3 Justificativa | Custo recorrente, dados que hoje saem da empresa (LGPD), autonomia tecnológica |
| 1.4 Público-alvo e pessoas impactadas | Os N funcionários que vão usar o harness |
| 1.5 ODS/ESG | ODS 8, meta 8.2 (produtividade por modernização tecnológica e inovação); ESG governança: dados no ambiente interno |
| 1.6 | Termo de aceite assinado |
| 1.7–1.9 | Etapas, recursos e cronograma: tabela abaixo |
| 1.10 Resultados esperados | Meta de redução do gasto mensal (definida no diagnóstico, por exemplo cancelar X assinaturas) e número de funcionários usando a ferramenta |
| 1.11 Teoria | PLN (13), Agentes Conversacionais (19), Redes Neurais (23), Segurança da informação (10), Ética (3) e Sistemas Especialistas (17) como apoio de método (ver abaixo) |

Este tipo **não tem** o campo "Nome do projeto". Postar e **esperar "apto"** do tutor (até 15 dias) antes de executar.

## 2. Etapas e horas (somam 100 h; planejamento também conta)

| # | Etapa | Horas | Presencial |
|---|---|---|---|
| 1 | Reunião inicial e Termo de aceite | 2 | sim |
| 2 | Diagnóstico: tarefas, custos atuais (linha de base em R$/mês) e hardware | 6 | sim |
| 3 | Redação e postagem do planejamento | 6 | |
| 4 | Seleção técnica: comparar 3–4 modelos abertos quantizados que caibam no hardware; checar licença de uso comercial; testar com 5–10 tarefas reais (qualidade, tokens/s, memória) | 16 | |
| 5 | Desenvolvimento do harness: runtime local (ex.: Ollama ou llama.cpp) + API e interface web só na rede interna + modelos de prompt para tarefas recorrentes | 30 | |
| 6 | Instalação e testes no computador da startup | 8 | sim |
| 7 | Preparar o manual de uso | 4 | |
| 8 | Treinamento de uso na entrega (TCLE de cada participante, Termo de uso de imagem de quem aparecer, lista de presença) | 4 | sim |
| 9 | Acompanhamento e ajustes (2–4 semanas de uso real) | 8 | parcial |
| 10 | Medir a economia e apresentar os resultados | 6 | sim |
| 11 | Coleta de feedback (Feedback da comunidade + questionário da equipe) | 2 | sim |
| 12 | Redação e postagem da execução | 8 | |

## 3. Execução (campos 2.1 a 2.6 do Conecta)

- 2.1 Evidências por etapa. Pelo menos uma foto ou vídeo do estudante na startup. A gravação de tela do harness não substitui essa foto. Borrar dados da empresa nas telas.
- 2.2 Aprendizados · 2.3 Obstáculos · 2.4 Objetivos alcançados (comparar a economia com a linha de base da etapa 2).
- 2.5 Percepções do público-alvo (questionário da equipe) · 2.6 Feedback da comunidade assinado pelo responsável (obrigatório).
- Conferir os 11 critérios antes de enviar. O critério 9 (alinhamento planejamento × execução) é o mais sensível.

## Sistemas Especialistas no 1.11

É apoio de método, não a base teórica principal.

- **Unidade 8:** os 5 estágios se encaixam nas etapas: identificação = etapa 2; conceitualização = escolha de tarefas e arquitetura; formalização = prompts e comparativo (etapa 4); implementação = etapas 5–6; testes = etapas 6 e 9. Só citar se a execução seguir de fato essa sequência.
- **Unidade 3:** entrevista de aquisição de conhecimento na etapa 2.
- **Unidade 2:** modelos de prompt transformam conhecimento tácito da equipe em explícito.
- **Unidade 7:** limites de explanação e incerteza do LLM (alucinação), tratados no treinamento.
- **Unidade 4:** base de conhecimento. Só vale se houver RAG.

## Riscos

- **Propriedade intelectual:** pelo Anexo 2 do [Manual](../Manual_de_Resposabilidades.pdf), o código do harness pertence à APC/PUCPR.
- **Presencialidade:** o desenvolvimento é remoto, por isso as etapas presenciais precisam de fotos ou vídeos.
