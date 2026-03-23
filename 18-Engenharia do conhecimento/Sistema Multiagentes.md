# Sistema Multiagentes — resumo completo

Um **sistema multiagentes** é formado por vários **agentes inteligentes e autônomos** que interagem entre si e com o ambiente para resolver problemas, executar tarefas ou simular comportamentos complexos. Diferente de um sistema centralizado, onde uma única entidade controla tudo, no sistema multiagentes cada agente possui certa independência para perceber, decidir e agir.

Esses sistemas são úteis quando o problema é grande, distribuído ou dinâmico demais para ser resolvido por apenas um agente. Nesses casos, os agentes podem dividir tarefas, cooperar, competir ou negociar para atingir objetivos individuais ou coletivos.

## Principais características

* **Autonomia:** cada agente age por conta própria.
* **Interação:** os agentes trocam mensagens e informações.
* **Cooperação:** agentes podem trabalhar juntos para um objetivo comum.
* **Competição:** agentes também podem disputar recursos ou decisões.
* **Distribuição:** as tarefas podem estar espalhadas entre vários agentes.
* **Adaptabilidade:** o sistema pode reagir a mudanças no ambiente.
* **Descentralização:** não depende de um único controlador central.

## Tipos de agentes

No contexto dos multiagentes, foram vistos dois tipos principais:

### Agentes reativos

São agentes que respondem diretamente ao ambiente, com base no estado atual, sem raciocínio complexo. Eles são rápidos e simples.

* funcionam por estímulo e resposta
* não mantêm grande modelo interno do mundo
* são bons para respostas imediatas

**Exemplo:** um robô que desvia de um obstáculo assim que o sensor detecta algo à frente.

### Agentes cognitivos

São agentes que possuem capacidade de raciocinar, planejar e tomar decisões mais elaboradas. Eles usam conhecimento, memória e, em alguns casos, aprendizado.

* analisam situações
* podem planejar ações
* usam mais contexto para decidir

**Exemplo:** um agente que escolhe a melhor rota levando em conta tempo, custo e prioridade.

## Inteligência nos agentes

Os dois tipos possuem inteligência, mas em níveis diferentes:

* o **agente reativo** tem uma inteligência mais simples e direta;
* o **agente cognitivo** tem uma inteligência mais avançada, com raciocínio e planejamento.

## Comunicação em sistemas multiagentes

A comunicação é uma parte central desses sistemas. Ela pode ser feita de duas formas:

### Comunicação síncrona

O agente envia uma mensagem e **espera a resposta** antes de continuar.

* há bloqueio até receber retorno
* exige coordenação temporal
* é mais simples de controlar

**Exemplo:** um agente pergunta algo e só prossegue depois que o outro responde.

### Comunicação assíncrona

O agente envia a mensagem e **continua executando outras tarefas**, sem esperar resposta imediata.

* maior independência entre agentes
* melhor para sistemas distribuídos
* mais flexível e escalável

**Exemplo:** um agente envia uma solicitação e segue trabalhando, recebendo a resposta depois.

## Vantagens dos sistemas multiagentes

* resolvem problemas complexos de forma distribuída
* permitem paralelismo
* aumentam a flexibilidade do sistema
* facilitam a adaptação a mudanças
* melhoram a escalabilidade

## Desvantagens / desafios

* coordenação entre agentes pode ser difícil
* comunicação pode gerar atraso ou conflito
* implementação é mais complexa
* exige controle de cooperação, competição e consistência

## Aplicações

Sistemas multiagentes são usados em:

* robótica
* automação
* simulações
* logística
* controle de tráfego
* redes inteligentes
* tomada de decisão distribuída

---

# Em uma frase

Um **sistema multiagentes** é um conjunto de agentes autônomos que interagem entre si, podendo ser reativos ou cognitivos, e se comunicam de forma síncrona ou assíncrona para resolver problemas complexos de maneira distribuída.
