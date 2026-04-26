# Roteiro do Vídeo de Apresentação — AtendeBot (5 minutos)

> **Duração total:** 5:00  
> **Formato sugerido:** gravação de tela + narração (câmera do apresentador opcional)  
> **Ferramenta sugerida:** OBS Studio, Loom ou gravação do Google Meet/Zoom  

---

## ABERTURA [0:00 – 0:20] *(20 segundos)*

**[Tela: slide de título ou câmera do apresentador]**

> "Olá! Meu nome é [SEU NOME] e neste vídeo vou apresentar o **AtendeBot**, um agente conversacional de Serviço de Atendimento ao Cliente desenvolvido para a empresa fictícia TeleConecta Brasil, uma operadora de telecomunicações. Vou percorrer o cenário, o fluxo conversacional, as tecnologias utilizadas, uma demonstração ao vivo do agente funcionando e, por fim, o plano de avaliação proposto."

---

## PARTE 1 — DESCRIÇÃO DO CENÁRIO [0:20 – 1:10] *(50 segundos)*

**[Tela: mostrar o documento `docs/cenario.md` ou slides com os pontos abaixo]**

> "O AtendeBot foi projetado para a **TeleConecta Brasil**, uma operadora de médio porte com cerca de **5 milhões de clientes**, que oferece telefonia móvel, internet banda larga e TV por assinatura."

> "A central de atendimento recebe em média **15 mil chamados por dia**, e **60% deles são consultas simples e repetitivas** — como segunda via de boleto, consulta de plano ou dúvidas de cobertura. O tempo médio de espera é de **12 minutos**, o que gera insatisfação e uma taxa de abandono de 25%."

> "O objetivo do agente é **automatizar esse atendimento de primeiro nível**: consultar planos, verificar faturas, gerar segunda via de boleto, registrar chamados técnicos, oferecer upgrades de plano e responder perguntas frequentes — tudo disponível **24 horas por dia, 7 dias por semana**."

> "Com isso, esperamos reduzir 40% do volume de chamados para atendentes humanos e melhorar significativamente a experiência do cliente."

---

## PARTE 2 — FLUXO CONVERSACIONAL [1:10 – 2:00] *(50 segundos)*

**[Tela: mostrar o fluxograma Mermaid renderizado — abrir no VS Code com extensão Mermaid ou captura do GitHub/editor online]**

> "O fluxo conversacional segue esta estrutura. Ao iniciar a conversa, o agente **cumprimenta o usuário e solicita o CPF** para identificação. Se o CPF é válido e está no banco, o cliente é saudado pelo nome."

**[Apontar para os ramos do fluxograma]**

> "A partir daí, o agente **classifica a intenção** de cada mensagem. São **10 intenções** mapeadas: saudação, consulta de plano, consulta de fatura, segunda via de boleto, problema técnico, upgrade de plano, falar com atendente, FAQ, agradecimento e despedida."

> "Além das intenções, o agente **extrai entidades** da mensagem: o CPF, o tipo de serviço — internet, celular ou TV —, o tipo de problema — lentidão, queda ou sem sinal — e o mês de referência da fatura."

> "Se o agente não entende a mensagem, ele pede para reformular. Após **duas tentativas sem sucesso**, ele **transfere automaticamente para um atendente humano**. Isso garante que o cliente nunca fica preso num loop sem solução."

---

## PARTE 3 — TECNOLOGIAS ADOTADAS [2:00 – 2:50] *(50 segundos)*

**[Tela: mostrar brevemente o código dos módulos ou o documento `docs/tecnologias.md`]**

> "O AtendeBot usa uma **abordagem híbrida** com três pilares:"

> "Primeiro, **regras determinísticas** para saudações, despedidas e extração de entidades com expressões regulares — por exemplo, o padrão de CPF."

**[Mostrar rapidamente `entity_extractor.py`]**

> "Segundo, **aprendizado de máquina** para classificação de intenções. Usamos **TF-IDF** para vetorizar o texto e **similaridade de cosseno** para encontrar a intenção mais próxima. Todo o pré-processamento é feito com o **NLTK**: tokenização, remoção de stopwords em português e **stemming com o algoritmo RSLP**, que é específico para o português."

**[Mostrar rapidamente `intent_classifier.py` e `preprocessor.py`]**

> "Terceiro, o **gerenciamento de diálogo** é feito com uma **máquina de estados finita** que controla o fluxo da conversa e mantém o contexto — como qual cliente está identificado e qual o último serviço consultado."

**[Mostrar rapidamente `manager.py` — a enum State]**

> "O agente acessa um **banco de dados SQLite** simulado que contém clientes, planos, contratos, faturas e chamados técnicos. A interface é uma aplicação web com **Flask** no backend e **HTML, CSS e JavaScript** no frontend. Tudo roda com um único comando: `python -m app.main`."

---

## PARTE 4 — DEMONSTRAÇÃO AO VIVO [2:50 – 4:20] *(1 minuto e 30 segundos)*

**[Tela: abrir o navegador em http://localhost:5000 — interface do chat]**

> "Agora vou demonstrar o agente funcionando. A interface é esta janela de chat. Vou simular um atendimento completo."

### Demo 1: Identificação + Consulta de Plano *(~25s)*

**[Digitar: "Olá"]**

> "Começo com uma saudação. O agente se apresenta e pede o CPF."

**[Digitar: "123.456.789-01"]**

> "Informo o CPF da Maria Silva. O agente busca no banco de dados, encontra o cadastro e a cumprimenta **pelo nome**. Mostra também um menu com as opções disponíveis."

**[Digitar: "Qual é o meu plano?"]**

> "Peço para ver o plano. Ele retorna os dois planos ativos da Maria — o **Essencial Móvel** de 59,90 e o **Fibra 300** de 119,90 — com velocidade, franquia e data de contratação. Essas informações vieram do banco de dados."

### Demo 2: Consulta de Fatura *(~15s)*

**[Digitar: "Quero ver minha fatura"]**

> "Agora consulto a fatura. O agente mostra as faturas dos últimos meses, com **valor, vencimento e status de pagamento** — pago ou pendente. Tudo consultado no SQLite."

### Demo 3: Problema Técnico com Extração de Entidades *(~25s)*

**[Digitar: "Minha internet está lenta"]**

> "Agora relato um problema técnico. Notem que eu disse 'internet' e 'lenta' — o agente **extraiu automaticamente** a entidade **tipo de serviço** como 'internet' e o **tipo de problema** como 'lentidão'. Com essas informações, ele registrou um chamado técnico, gerou um **número de protocolo** e informou a **previsão de resolução**. Tudo em uma única mensagem, sem perguntas adicionais."

### Demo 4: Upgrade + Despedida *(~25s)*

**[Digitar: "Quero trocar de plano"]**

> "Peço para trocar de plano. O agente lista todos os planos disponíveis organizados por categoria, com preços e descrições."

**[Digitar: "Fibra 500"]**

> "Escolho o Fibra 500 e o agente confirma a alteração."

**[Digitar: "Obrigado, tchau"]**

> "Me despeço e o agente encerra o atendimento com uma mensagem amigável."

---

## PARTE 5 — PLANO DE AVALIAÇÃO [4:20 – 4:50] *(30 segundos)*

**[Tela: mostrar o documento `docs/plano_avaliacao.md` ou slides com resumo]**

> "Para avaliar o agente, propomos **três dimensões**:"

> "A **avaliação técnica**, automática, mede acurácia, precisão, recall e F1-Score da classificação de intenções, com meta de pelo menos 85% de acurácia, além de taxa de fallback e tempo de resposta."

> "A **avaliação funcional** define 12 cenários de teste end-to-end que cobrem todos os fluxos do fluxograma — desde consulta de plano até fallback para atendente humano."

> "E a **avaliação de usabilidade**, com 10 a 15 usuários reais de perfis variados, aplicando o questionário **SUS** adaptado e entrevistas semiestruturadas para medir facilidade de uso, satisfação e confiança no agente."

---

## ENCERRAMENTO [4:50 – 5:00] *(10 segundos)*

**[Tela: slide de encerramento ou câmera do apresentador]**

> "E esse foi o AtendeBot — um agente conversacional de SAC funcional, construído com técnicas de PLN e aprendizado de máquina, com acesso a banco de dados e uma interface web completa. Obrigado pela atenção!"

---

## Checklist de Preparação para a Gravação

- [ ] Iniciar o servidor: `cd projeto && python -m app.main`
- [ ] Abrir o navegador em http://localhost:5000
- [ ] Ter os documentos da pasta `docs/` abertos para mostrar
- [ ] Ter o fluxograma renderizado (VS Code com extensão Mermaid ou https://mermaid.live)
- [ ] Ter o código aberto no editor para mostrar os módulos rapidamente
- [ ] Testar o fluxo completo uma vez antes de gravar
- [ ] Verificar que o áudio do microfone está funcionando

## Dicas para a Gravação

1. **Ensaie pelo menos 2 vezes** antes de gravar — a fluidez melhora muito
2. **Fale com calma** — é melhor falar devagar e claro do que correr
3. **Aponte o cursor** para as partes relevantes da tela enquanto explica
4. **Não leia o roteiro literalmente** — use como guia e fale naturalmente
5. Se errar, **pause, respire e retome** — é mais fácil cortar depois
6. Mantenha o **zoom do navegador em 110-125%** para as letras ficarem legíveis na gravação
