# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Pasta do repositório `PUC` (github.com/marcospontoexe/PUC) com o material da disciplina **IA Aplicada à Computação Forense** (PUCPR EAD). Contém:

- os PDFs das 8 unidades;
- um laudo real anonimizado, [Modelo de Laudo Técnico.pdf](Modelo%20de%20Laudo%20T%C3%A9cnico.pdf);
- o modelo de laudo a preencher, [Laudo pericial.docx](Laudo%20pericial.docx);
- três notebooks do Colab em [Códigos/](C%C3%B3digos/).

Não há build, testes nem arquivo de dependências: os notebooks usam numpy, pandas, scikit-learn e matplotlib. Escreva sempre em pt-BR. A pasta não tem o enunciado da atividade avaliativa nem os dados de um caso. Se for preciso preencher o laudo, o caso, as datas e os nomes dos peritos vêm do usuário.

## Como ler os PDFs

O texto sai limpo com `pypdf`. Grave a saída em UTF-8 no scratchpad, porque o console do PowerShell estraga os acentos:

```powershell
# Extrai o texto de um PDF, página a página (separador "=== PAGE ===")
python -c "import pypdf,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n=== PAGE ===\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" "<arquivo>.pdf" "<scratchpad>\saida.txt"
```

- As Unidades 6 e 7 pesam 5 MB e 11 MB por causa das imagens, mas o texto delas sai inteiro. As figuras (marcadas com `#ParaTodosVerem`) só se veem com Read e `pages`.
- Videoaulas e podcasts não estão nos PDFs. Do jogo "Forensic Lab: case #404" (Unidade 5, pp. 21–23), o PDF traz só a descrição das fases e a resposta comentada.
- As "Questões reflexivas" de cada unidade já vêm com a resposta sugerida logo em seguida.
- A referência mais citada em toda a disciplina é Dalla Vecchia (2019), *Perícia digital: da investigação à análise forense*.

## Onde está cada conceito

| Unidade | Págs. | Conceitos |
|---|---|---|
| [1](1-Objetivo%20da%20Computa%C3%A7%C3%A3o%20Forense.pdf) | 12 | Objetivos da forense (o quê, como, quem, quando); vestígio × evidência × indício; princípio de Locard; crimes cibernéticos próprios × impróprios |
| [2](2-Processo%20de%20Computa%C3%A7%C3%A3o%20Forense.pdf) | 11 | Processo em 4 etapas: coleta (pp. 4–6: post mortem × live forensics, RAM antes de desligar, espelhamento, cadeia de custódia), exame (p. 7), análise (pp. 8–9) e resultados (pp. 9–10) |
| [3](3-Per%C3%ADcia%20computacional%3B%20fundamentos,%20modalidades%20e%20su%C3%ADtes%20forenses.pdf) | 20 | Modalidades de perícia (pp. 3–9); suítes EnCase, FTK Imager, Oxygen e ProDiscover (pp. 10–14); caso prático com o FTK Imager (pp. 15–16) |
| [4](4-A%20intelig%C3%AAncia%20artificial%20empregada%20na%20investiga%C3%A7%C3%A3o%20forense.pdf) | 12 | Passos para aplicar IA; cenário de vazamento de dados bancários; IA na fase de análise (anomalias, PLN, clustering, classificação de documentos, visão) |
| [5](5-Aux%C3%ADlio%20da%20IA%20nas%20etapas%20da%20computa%C3%A7%C3%A3o%20forense%20%E2%80%93%20parte%201.pdf) | 27 | Árvore de decisão (pp. 3–6); sistema especialista e encadeamento para frente/trás (pp. 7–12); lógica fuzzy (pp. 13–16); perícia na internet (OSINT), na nuvem, em deepfakes e em redes sociais (pp. 17–20) |
| [6](6-Aux%C3%ADlio%20da%20IA%20nas%20etapas%20da%20Computa%C3%A7%C3%A3o%20Forense%20%E2%80%93%20parte%202.pdf) | 24 | Visão computacional e CNN: datasets, convolução, pooling, flattening, camada densa, backpropagation (pp. 4–16); forense em dispositivos móveis (pp. 17–20); YOLO (p. 20) |
| [7](7-Aux%C3%ADlio%20da%20IA%20nas%20etapas%20da%20Computa%C3%A7%C3%A3o%20Forense%20%E2%80%93%20parte%203.pdf) | 47 | Machine learning e tabela comparativa dos algoritmos (pp. 2–15); métricas (pp. 16–20); mineração de processos (pp. 21–27); laudo pericial (pp. 28–33); quesitos e erros comuns (pp. 34–35); antiforense (pp. 36–41) |
| [8](8-Fechamento.pdf) | 6 | Revisão e leituras (POP Perícia Criminal 2024 – Informática Forense, vol. 5) |

## Fio condutor: processo forense → laudo → IA

O [Laudo pericial.docx](Laudo%20pericial.docx) segue as 4 etapas da Unidade 2, e a Unidade 4 situa a IA na etapa de análise. As seções do modelo trazem instruções entre parênteses, que devem ser substituídas pelo texto do laudo:

- **Objeto da perícia:** tudo o que foi feito na coleta, com os itens coletados e os cuidados tomados.
- **Método utilizado:** o exame e a análise, mais a abordagem de IA. Diga por que ela foi escolhida, como ajuda na investigação e quais resultados deu.
- **Resultados obtidos:** narrativa técnica e imparcial, ainda sem conclusões, mostrando os resultados da IA.
- **Discussão e análise dos resultados:** a reconstrução da cena do crime.
- **Conclusões:** o envolvimento de cada pessoa, com data, hora e ação.
- **Anexos:** códigos, algoritmos, gráficos e tabelas.

Mais detalhes sobre o modelo e o exemplo:

- O modelo tem capa (caso, peritos e data), informações do perito e quatro blocos de assinatura. Todos os parágrafos usam o estilo Normal, e não há tabelas nem imagens. O `python-docx` está instalado.
- A Unidade 7 (pp. 28–31) descreve os mesmos tópicos do modelo, um a um.
- O [Modelo de Laudo Técnico.pdf](Modelo%20de%20Laudo%20T%C3%A9cnico.pdf) usa outra estrutura: preâmbulo, ferramenta (FTK Imager, hash MD5, imagem `.E01`), objetivo, material, exame, considerações técnicas (Autopsy, checksums, `HASH_DO_HASH.txt`), conclusão e anexos. Ele não usa IA e serve como referência de linguagem para a coleta e o exame.
- A Unidade 8 resume as técnicas de IA da disciplina: árvores de decisão, sistemas especialistas, lógica fuzzy, visão computacional, machine learning, Q-Learning, clustering e mineração de processos. Ela também reforça que o laudo feito com IA precisa ser transparente, tecnicamente justificável e de responsabilidade do perito.

## Notebooks em Códigos/

Os três notebooks foram exportados do Colab e têm uma única célula de código cada. O de clusterização tem também uma célula markdown. Cada um gera dados sintéticos com semente fixa, treina o modelo e depois pede um caso por `input()`. Provavelmente vieram do `Códigos.zip` anexado na Unidade 7 (p. 42).

| Notebook | Técnica | Cenário | Entradas, na ordem |
|---|---|---|---|
| [Supervisionado](C%C3%B3digos/AlgoritmoSupervisionadoClassificacao.ipynb) | `StandardScaler` + `LogisticRegression` | Login suspeito | falhas 24h, hora, país novo, IP externo, VPN/proxy, dispositivo novo, distância (km) |
| [Não supervisionado](C%C3%B3digos/AlgoritmoN%C3%A3oSupervisionadoClusterizacao.ipynb) | `StandardScaler` + `KMeans` (k=4) + gráfico de dispersão | Triagem de transações, com 50 suspeitas injetadas entre 900 | valor (R$), hora, tentativas 24h, local novo, online |
| [Q-Learning](C%C3%B3digos/AlgoritmoAprendizagemPorReforcoQLearning.ipynb) | Q-table 6 estados × 3 ações (investigar, fila, ignorar) | Triagem de alertas num SOC | risco (0/1/2), pressão (0/1), depois `s`/`n` para repetir |

### Rodar sem Jupyter

O `nbconvert --execute` para no primeiro `input()`. Passar a entrada por pipe do PowerShell também falha, porque o pipe insere um BOM (`int('﻿0')`). Por isso, injete o stdin no próprio Python, com os valores separados por `;` na ordem dos `input()`:

```powershell
$env:MPLBACKEND = 'Agg'; $env:PYTHONIOENCODING = 'utf-8'
$run = "import glob,io,json,sys; sys.stdin=io.StringIO(sys.argv[2].replace(';',chr(10))+chr(10)); nb=json.load(open(glob.glob(sys.argv[1])[0],encoding='utf-8')); exec(compile(''.join(''.join(c['source'])+chr(10) for c in nb['cells'] if c['cell_type']=='code'),'nb','exec'),{'__name__':'__main__'})"
python -I -c $run "Códigos\AlgoritmoSupervisionado*.ipynb" "0;10;0;1;0;0;12"
python -I -c $run "Códigos\*QLearning.ipynb" "2;1;n"
python -I -c $run "Códigos\*Clusterizacao.ipynb" "15000;3;12;1;1"
```

Cuidados ao rodar:

- O padrão `*Supervisionado*` também casa com `AlgoritmoNãoSupervisionado...`. Mantenha o prefixo `AlgoritmoSupervisionado`.
- No Python local (3.14, com scikit-learn 1.8 e pandas 3.0), as saídas batem com as que estão salvas nos notebooks: probabilidade 0.013 e "NORMAL" no supervisionado, e a mesma Q-table no Q-Learning.

### Pontos de atenção nos notebooks

- **Clusterização:** a célula markdown numera os perfis de 1 a 4, sendo o 4 o anômalo. Já os rótulos do KMeans vão de 0 a 3 e não seguem essa ordem. Na execução, o cluster prioritário é o **1**, que reúne exatamente as 50 transações suspeitas injetadas. Para interpretar, use o resumo e o `score_prioridade` impressos, não a numeração do markdown.
- **Q-Learning:** o próximo alerta é sorteado sem depender da ação. Por isso, a política ótima é a de maior recompensa esperada em cada estado: ignorar no risco baixo, fila no médio e investigar no alto, com qualquer pressão. É também o que os comentários do código pretendem. A política salva (semente 123) erra em 3 dos 6 estados:
  - risco 0 e pressão 1 → fila;
  - risco 1 e pressão 1 → investigar;
  - risco 2 e pressão 0 → fila.

  A causa provável é a taxa de aprendizado constante (alpha = 0,2) combinada com recompensas de alta variância, o que deixa a Q-table ruidosa. Não apresente essa política como correta sem essa ressalva.
- **Supervisionado:** o notebook separa `X_test`/`y_test`, mas não calcula nenhuma métrica. As métricas para avaliar o modelo estão na Unidade 7 (pp. 16–20).

## Arquivos citados nos PDFs que não estão na pasta

- `ExemploSistemaEspecialistaEFuzzyAula5.ipynb` (Unidade 5, p. 2).
- `DetectorDeObjetosComYOLO.ipynb` e `Exemplo_Visao_Computacional_Deteccao_de_Bordas_V2.ipynb` (Unidade 6, p. 2).
