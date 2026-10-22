# Resumo — Sistemas Especialistas (SE)

Resumo de estudo das oito unidades da disciplina.

Trechos marcados como **Complemento** não estão no material da PUCPR. Eles foram acrescentados para facilitar o aprendizado. Os erros encontrados no material estão reunidos na seção [Erros e imprecisões do material](#erros-e-imprecisões-do-material).

| Fonte | Tema |
|---|---|
| [Unidade 1 (U1)](1-Quando%20a%20utiliza%C3%A7%C3%A3o%20de%20um%20sistema%20especialista%20%C3%A9%20apropriada.pdf) | Quando usar um SE; ética na computação |
| [Unidade 2 (U2)](2-Sistemas%20especialistas%20e%20conhecimento.pdf) | O que é um SE, tipos de SE, conhecimento tácito e explícito |
| [Unidade 3 (U3)](3-Aquisi%C3%A7%C3%A3o%20de%20conhecimento.pdf) | SE × programa convencional, heurísticas, ontologias, aquisição de conhecimento |
| [Unidade 4 (U4)](4-Base%20de%20conhecimento%20e%20sistemas%20especialistas.pdf) | Base de conhecimento |
| [Unidade 5 (U5)](5-Benef%C3%ADcios%2C%20vantagens%20e%20desvantagens%20do%20uso%20de%20sistemas%20especialistas.pdf) | Vantagens e desvantagens |
| [Unidade 6 (U6)](6-Motor%20de%20infer%C3%AAncia%20e%20interface%20do%20usu%C3%A1rio.pdf) | Motor de inferência e interface do usuário |
| [Unidade 7 (U7)](7-Mem%C3%B3ria%2C%20explana%C3%A7%C3%A3o%20e%20incerteza.pdf) | Memória de trabalho, explanação e incerteza |
| [Unidade 8 (U8)](8-Est%C3%A1gios%20de%20desenvolvimento%20de%20um%20sistema%20especialista.pdf) | Estágios de desenvolvimento |

---

## Visão geral: como as peças se encaixam

Antes de ler unidade por unidade, vale ter o mapa completo. Cada unidade aprofunda uma parte dele.

```
 Especialista humano ──► Engenheiro do conhecimento ──► ┌─────────── Sistema especialista ───────────┐
 (sabe resolver o         (extrai o conhecimento, U3,   │  Base de conhecimento  (U4)                │
  problema; muito do       e o transforma em regras,    │  Motor de inferência   (U6)  ◄─► Memória   │
  saber é tácito, U2)      frames, conjuntos fuzzy)     │  Interface do usuário  (U6)    de trabalho │
                                                        │  Explanação e incerteza (U7)        (U7)   │
                                                        └──────────────────────┬─────────────────────┘
                                                                               ▼
                                                                Usuário (não especialista)
```

- **U1** responde "quando vale a pena construir isso?".
- **U2** explica o que é cada parte, quais os tipos de SE e que tipo de conhecimento entra nele.
- **U3** mostra como tirar o conhecimento da cabeça do especialista.
- **U5** pesa os prós e contras.
- **U8** mostra a ordem em que tudo é construído.

---

## Unidade 1 — Quando a utilização de um SE é apropriada

### O que é um sistema especialista

- Um **sistema especialista (SE)** é um programa que resolve problemas e **justifica** a solução com conhecimento especializado.
- O nome vale quando a base de conhecimento vem de **especialistas humanos**, e não de livros ou bibliotecas.
- Na literatura também aparece como **Sistema Baseado em Conhecimento (SBC)**. O material diz que é o tipo de IA mais difundido.
- Para funcionar, precisa de duas coisas:
  - uma **base de conhecimento** do domínio, robusta;
  - um **mecanismo de raciocínio** que aplique esse conhecimento ao problema.

### Vocabulário básico (Jackson, 1999)

| Termo | Significado |
|---|---|
| **Tarefa** | A atividade orientada a metas, a resolução do problema em si |
| **Domínio** | A área em que a tarefa é realizada |
| **Domínio da tarefa** | O esforço intelectual que o SE precisa capturar e expressar |

As tarefas típicas de um SE são **diagnóstico, planejamento, programação, configuração e projeto**.

### SE dentro da IA

- A **IA** estuda e constrói agentes inteligentes, que percebem o ambiente e agem de forma a aumentar a chance de acertar. É estudada desde os anos 1950.
- Definição de Rich e Knight (1991): IA é fazer computadores realizarem tarefas que hoje os humanos fazem melhor.
- Os SEs são um subcampo da IA, ao lado de redes neurais e algoritmos genéticos, por exemplo.
- Um SE **simula o raciocínio humano sobre o problema**. Ele não simula o domínio em si: um SE de meteorologia imita como o meteorologista pensa, e não a física da atmosfera.

### Quando usar um SE

A resposta da unidade se apoia em três ideias:

1. O SE serve para **apoiar a decisão**. Ele não substitui o julgamento do especialista humano.
2. O público principal é o **usuário inexperiente**, na **ausência** de um especialista real.
3. O SE precisa **informar como chegou à decisão**, e não só dar a resposta.

**Exemplo do material:** você quer pescar, mas sempre chove na região. Não dá tempo de aprender meteorologia, e você tem um amigo meteorologista com 20 anos de experiência. Você extrai dele as regras de produção e monta um SE que ajuda a decidir se vale ir pescar, conforme a chance de chuva.

**Quando compensa:** quando faltam especialistas e treinar pessoas é caro e demorado. O SE resolve os problemas de rotina, elimina atrasos e pode ser copiado para vários locais, disponível 24 horas por dia.

### Áreas de aplicação

| Área | Exemplos |
|---|---|
| Finanças | Aprovação de empréstimos, avaliação de risco e preço de seguros, Serasa Score |
| Agronegócio | Irrigação, controle de pragas, seleção de grãos, manejo de culturas, época de adubação |
| Negócios | Melhor horário de postagem, entrada em mercado, desempenho de vendas, cargos e salários, logística |
| Engenharia | Manutenção preventiva e corretiva, desgaste de motores, falhas em semicondutores, controle de processos em plataformas de petróleo |
| Computação e redes | Diagnóstico de sistemas, localização de falhas, detecção de falhas de rede |

### Ética na computação

- Bynum e Rogerson (1996) falam em **"ética da informação global"**: os riscos são maiores, e a ética deve ajudar a construir uma tecnologia **democrática e fortalecedora**, e não escravizante.
- Exemplos atuais citados: reconhecimento facial capaz de achar uma pessoa entre milhões e drones armados.
- **Ética na informática** é o conjunto de princípios morais que regulam o uso de computadores. Temas comuns: propriedade, privacidade e o efeito dos algoritmos na sociedade (Baase, 2012).
- Ao decidir se uma ação é correta, há três **direcionadores**, nesta ordem:
  1. **a lei**, com sanções em caso de descumprimento;
  2. os **códigos de prática** da profissão;
  3. a **ética pessoal**: valores morais e religiosos.
- No Brasil há o **Código de Ética da Sociedade Brasileira de Computação (SBC)**.

> **Para pensar:** o exemplo de crédito do material cita "idade, gênero" como critérios. É um bom caso para a seção de ética, porque usar gênero para negar crédito pode ser discriminatório.

---

## Unidade 2 — Sistemas especialistas e conhecimento

### Histórico e definição

- Os SEs surgiram nos **anos 1960**, com **Edward Feigenbaum**, que queria entender o quanto um programa conseguia saber e decidir. Os primeiros sistemas resolviam testes de raciocínio infantis.
- **Toda IA usa conhecimento, mas o SE representa o conhecimento de forma explícita** e raciocina sobre ele. O paradigma por trás de toda a IA é a **busca**.
- Definição de Durkin (1994): um SE é um programa capaz de **modelar e resolver problemas com base no conhecimento humano**.
- O conhecimento e a lógica vêm da experiência do especialista. Problema de encanamento, entreviste um encanador. Problema de logística, um profissional de referência em logística.
- Rafea (1996): o SE resolve o problema de **transferir conhecimento** do especialista para quem sabe menos.
- **Benefício:** decisões mais consistentes e de melhor qualidade, com custo e tempo menores do que treinar uma pessoa.

### Fluxo de desenvolvimento (Figura 1 da unidade)

```
Especialista humano ──► Engenheiro do conhecimento ──► [ Base de conhecimento | Motor de inferência | Interface do usuário ] ──► Usuário
```

O especialista fornece o conhecimento. O engenheiro do conhecimento o transforma nos três componentes. O usuário recebe as conclusões pela interface.

### Os três tipos de SE

#### 1. SE baseado em regras

O conhecimento é escrito como regras **SE … ENTÃO** (*IF-THEN*), uma forma direta e flexível de expressar o que o especialista sabe. Segundo Nagori e Trivedi (2014), tem **cinco componentes**:

| Componente | Função |
|---|---|
| Base de conhecimento | O que se sabe sobre o domínio |
| Banco de dados | O conjunto de **fatos** sobre o caso atual |
| Motor de inferência | O raciocínio que leva à solução |
| Facilidade de explicação | Diz ao usuário **por que** chegou àquela solução |
| Interface do usuário | Permite interagir com os outros componentes |

Pode haver componentes extras, como interfaces externas e de desenvolvedor, para falar com outros bancos de dados e programas.

#### 2. SE fuzzy

- Usado quando o especialista fala com **termos vagos**: "muito perto", "não tão velho", "moderado".
- Na lógica fuzzy, a verdade é um **número real entre 0 e 1**: o grau em que algo pertence a um conjunto.
- Etapas de desenvolvimento, segundo Negnevitsky (2008):
  1. especificar o problema e definir as **variáveis linguísticas**;
  2. determinar os **conjuntos fuzzy**;
  3. construir as **regras fuzzy**;
  4. codificar conjuntos, regras e procedimentos para fazer a inferência;
  5. avaliar o sistema.

> **Complemento, exemplo de conjunto fuzzy:** a variável "distância" pode ter os conjuntos *perto*, *médio* e *longe*. Um obstáculo a 0,4 m pode pertencer a *perto* com grau 0,8 e a *médio* com grau 0,2. Na lógica clássica ele seria só "perto" ou só "não perto".

#### 3. SE baseado em frames (estruturas)

- Um **frame** representa um objeto ou conceito, com nome e atributos (Minsky, 1975). Junta, num lugar só, tudo o que se sabe sobre aquele conceito. A programação costuma ser orientada a objetos.
- **Vantagem sobre o SE de regras:** o motor só pesquisa os frames relevantes, enquanto o SE de regras faz uma busca geral em todas as regras.
- Os atributos ficam em **slots**. Um slot pode guardar um valor, um valor padrão, um ponteiro para outro frame ou um procedimento que calcula o valor.
- Informações típicas de um slot (Negnevitsky, 2008):
  - nome do frame;
  - relação com outros frames;
  - valor do slot;
  - valor padrão;
  - faixa de valores (*range*);
  - informação de procedimento.
- Aqui as **regras têm papel secundário**. O motor localiza o objetivo, examina as regras ligadas a ele e, se todas forem válidas, conclui a meta.
- Etapas de desenvolvimento:
  1. especificar o problema e o escopo;
  2. determinar classes e atributos;
  3. definir instâncias;
  4. projetar a tela (*display*);
  5. definir quando os métodos são modificados;
  6. definir as regras;
  7. avaliar o sistema.

> **Complemento, exemplo de frame:** o frame `Paciente` tem os slots `idade` (faixa 0–120), `temperatura` (padrão 36,5 °C) e `é-um → Pessoa` (relação com outro frame). Pode ter também um procedimento do tipo "se temperatura > 37,8, então febre = sim".

#### Comparação rápida

| Tipo | Representa o conhecimento como | Use quando |
|---|---|---|
| Regras | SE … ENTÃO | O especialista pensa em condições e ações |
| Fuzzy | Conjuntos com grau de pertinência | O especialista usa termos vagos e graduais |
| Frames | Objetos com atributos (slots) | O domínio tem muitos conceitos com propriedades e hierarquia |

### O que é conhecimento

**Cinco abordagens** do conhecimento:

| Tipo | Significado |
|---|---|
| Know-why | Conhecimento científico, as leis da natureza |
| Know-how | Habilidade de fazer algo |
| Know-where | Fatos e experiências acumulados |
| Know-when | Noção de tempo, de quando agir |
| Know-who | Saber quem sabe determinado assunto |

A classificação mais aceita é a de **Polanyi**, com dois tipos:

- **Tácito:** você sabe fazer, mas não sabe explicar como sabe.
  - Fica na cabeça da pessoa, não é facilmente capturado nem codificado, e muitas vezes só se vê na **ação** (Nonaka e Takeuchi, 1995; Sveiby, 1997).
  - Exemplos: o chá que cura a dor de cabeça sem que você saiba o mecanismo; o gol de falta.
  - Regras ajudam, mas não transmitem a arte toda: Roberto Carlos pode escrever regras para bater falta, mas ninguém herda a habilidade dele.
- **Explícito:** pode ser escrito em linguagem formal (livros, artigos, vídeos, manuais) e distribuído a muita gente (Koskinen et al., 2003).
  - Exemplo: o suporte técnico pede para reiniciar o roteador porque isso está no manual e funciona na maioria dos casos.

**Por que isso importa para o SE:** livros e manuais só dão o conhecimento explícito. A **entrevista de aquisição de conhecimento** com o especialista é o que capta o tácito, e sem ele o SE perde eficiência.

---

## Unidade 3 — Aquisição de conhecimento

### SE × programa convencional

- A diferença central é que o SE resolve problemas do mundo real usando **julgamento**.
- SE **não é modelagem cognitiva**. Ele não tenta imitar a arquitetura do pensamento humano. É um programa baseado em **heurísticas** criadas para problemas específicos.

Comparação segundo Lucas e Van der Gaag (1991):

| Aspecto | Sistema especialista | Programa convencional |
|---|---|---|
| Conhecimento | Fragmentado e implícito, dividido em pequenas partes | Completo e explícito, comunicável por fórmulas e algoritmos |
| Regras | Complexas, condicionais, mudam conforme o tipo de SE | Simples, com poucas condições |
| Solução de problemas | Dinâmica e contextualizada nos fatos; as regras se relacionam muito entre si | Previsível; depende de uma sequência repetida de ações |
| Medida de desempenho | A **exatidão** e o **caminho** percorrido até a resposta | — |

- Nenhum dos dois é superior. Cabe ao profissional analisar o problema e escolher.
- "Implícito", aqui, quer dizer que o conhecimento nasce da experiência do especialista e não de fórmulas fechadas. Depois de adquirido, ele vira regras **explícitas** na base de conhecimento (U4).

> **Complemento, exemplo:** calcular a folha de pagamento pede um programa convencional, porque a fórmula é completa e conhecida. Decidir se um paciente com sintomas vagos precisa de determinado exame pede um SE, porque o conhecimento é heurístico, depende do contexto, e o médico vai querer saber o porquê da sugestão.

### Heurísticas

Definição de Pearl (1984):

> "As heurísticas são critérios, métodos ou princípios para decidir quais entre vários cursos alternativos de ação promete ser o mais eficaz para atingir algum objetivo. Eles representam compromissos entre duas exigências: a necessidade de fazer tais critérios simples e, ao mesmo tempo, o desejo de vê-los discriminar corretamente entre boas e más escolhas."

- Uma heurística aponta o caminho mais promissor, mas **não garante** a solução.
- Precisa equilibrar duas exigências:
  - ser **simples**;
  - **distinguir bem** as escolhas boas das ruins.
- É uma **simplificação** de uma descrição formal completa do mundo real. Melhora o desempenho de programas de IA imitando os atalhos do pensamento humano (Boden, 1977).
- Nos humanos, as heurísticas são mecanismos práticos e automáticos que **economizam esforço mental** para as decisões mais complexas. Exemplos do material: dirigir depois de anos de prática, escovar os dentes sonolento, digitar sem olhar o teclado.

> **Atenção:** os exemplos do material são mais **hábitos automatizados**, ou seja, conhecimento tácito, do que heurísticas no sentido de IA. Num SE, heurística é uma **regra de bolso** que guia uma escolha. Exemplo: "se o carro só faz barulho quando está frio, comece verificando a correia". A ligação entre as duas ideias: muitas heurísticas do especialista são tácitas (U2), e por isso adquiri-las é difícil.

> **Complemento, heurística que falha:** para achar o caminho num mapa, "ande sempre na direção do destino" é simples e quase sempre ajuda. Mas pode levar a um beco sem saída. A heurística orienta a escolha sem garantir a solução.

### Ontologias

- **Na filosofia:** a ciência do que existe, ou seja, dos tipos e estruturas de objetos, propriedades, eventos, processos e relações.
- **Na informática:** um conjunto de representações que **modela um domínio de conhecimento**, com:
  - **classes**;
  - **propriedades ou atributos**;
  - **relações** entre os membros das classes.
- Pode modelar um domínio real ou imaginário.
- Fica num **nível de abstração acima dos modelos de dados**: usa lógica de primeira ordem e trabalha no **nível semântico**, isto é, do significado (Gruber, 1993).
- A IA adotou as ontologias porque permitem **raciocínio automatizado** e fornecem um **vocabulário comum**. As afirmações de entrada e saída de um agente de conhecimento, como um SE, passam a ter uma linguagem de comunicação compartilhada.

> **Complemento, mini-ontologia de uma clínica:**
> - classes: `Paciente`, `Sintoma`, `Doença`, `Exame`;
> - relações: `Paciente apresenta Sintoma`, `Doença causa Sintoma`, `Exame confirma Doença`;
> - atributos: `Paciente.idade`, `Sintoma.intensidade`.
>
> Os frames da U2 são uma forma de implementar uma ontologia dessas.

### Aquisição de conhecimento

**Por que é necessária:** o SE precisa de competência **profunda**, para lidar com a complexidade dos problemas reais, e **ampla**, para cobrir a variedade de tarefas do domínio.

**Como funciona:**

- Construir o conhecimento do sistema é uma atividade de **modelagem**:
  - começa **qualitativa**, explorando a parte do mundo real em que o sistema vai atuar;
  - envolve análise, construção e representação;
  - é feita pelo engenheiro junto com o especialista (Clancey, 1989; Ford et al., 1993).
- **Aquisição de conhecimento** é a fase em que se coletam informações sobre o domínio junto ao especialista humano, no nível de profundidade desejado.

**Dois níveis de profundidade** (Clancey, 1989):

| Nível | O que contém | Exemplo (complemento) |
|---|---|---|
| **Superficial** | Conhecimento declarativo e procedimentos heurísticos para resolver o problema rápido; é a base da maioria das regras de produção | "Se o carro não liga e as luzes do painel estão fracas, troque a bateria." |
| **Profundo** | Os fundamentos: definições, axiomas, leis, princípios de causalidade | Como funciona o circuito elétrico de partida do motor |

**Quem entrevistar:**

- Um especialista que **domine de fato a área** e saiba resolver os problemas que o SE vai tratar.
- A escolha se baseia na **reputação** dele.
- Ele precisa estar **disposto a cooperar** durante todo o desenvolvimento.
- O conhecimento precisa ser **validado**: se o que for coletado estiver errado, o SE vai atrapalhar mais do que ajudar (Ford et al., 1993).

**O usuário também participa** (Kidd, 1987). É preciso:

- a) identificar as **classes de usuários** que devem usar o sistema e as necessidades de cada uma;
- b) analisar as **necessidades**: perguntas e problemas comuns, o que o usuário espera (por exemplo, ele já tem uma solução em mente e quer mais segurança na decisão);
- c) analisar que **conhecimento o usuário já traz** para a solução do problema.

Levantar os requisitos do usuário é difícil. A técnica mais usada é a **investigação contextual**: observar o usuário interagindo com o sistema e fazer perguntas a partir do que se vê.

O **engenheiro do conhecimento** precisa entender o básico da área, para conseguir avaliar a qualidade do que está coletando.

**Processo de aquisição (Figura 2 da unidade):**

```
                ┌────────── interação ──────────┐
                ▼                               │
   Prática do especialista            Engenheiro do conhecimento ──► Base de conhecimento
                │                               ▲
                └──── entrevistas sistemáticas ─┘
```

O engenheiro interage com a prática do especialista, as entrevistas sistemáticas trazem essa prática até ele, e ele alimenta a base de conhecimento.

**O que o engenheiro faz na prática:**

- **Observa o especialista em ação** e anota que informação ele usa para resolver cada problema.
- Monta um **fluxo de trabalho**, perguntando **por que** cada ação acontece e **qual é o próximo passo**.
- Considera **decisões típicas e atípicas**. Com a experiência, muita coisa vira automática para o especialista, e ele nem lembra de mencionar.
- A aquisição pode vir de duas fontes:
  - **observação** do especialista resolvendo problemas no dia a dia;
  - **discussão** do problema: que tipo de dado, informação e conhecimento são necessários.
- Descreve um **problema típico** para cada categoria de problema, com as diferentes formas de resolvê-lo.
- **Refinamento** (Waterman, 1986): antes de desenvolver, o engenheiro propõe um problema e o especialista o resolve usando só o conhecimento adquirido até aquele ponto do cronograma. Isso mostra se ainda falta conhecimento.

**Técnicas de aquisição (Figura 3 da unidade):**

| Oral | Escrita | Diagrama |
|---|---|---|
| Entrevista | Questionários | Curvas |
| Hipóteses | | Diagramas |
| *Brainstorm* | | Fluxos |

**Três métodos de entrevista** (Waterman, 1986):

| Método | Como funciona |
|---|---|
| **Observação** | O engenheiro observa o especialista resolvendo um problema, **sem interromper**, e transcreve tudo depois |
| **Intuitivo** | O engenheiro interage com o especialista e também estuda a literatura; juntos, constroem a teoria e o comportamento que ocorre na prática |
| **Combinado** | Junta os dois anteriores: o engenheiro faz perguntas durante a solução, estimula o especialista a contar experiências, testa o conhecimento dele em problemas específicos e sugere bases lógicas que facilitam transformar tudo em regras |

**Conclusão da unidade:** heurísticas e ontologias dão a base teórica dos SEs. Mas, como toda heurística, nem sempre bastam para resolver o problema.

> **Ligações:**
> - O ciclo da Figura 2 da Unidade 8 (o especialista descreve, o engenheiro redige, "isso descreve o problema?") é esta mesma aquisição, vista como parte do estágio de identificação.
> - O [Roteiro da 1ª atividade formativa](1%C2%B0%20atividade%20formativa/Roteiro.docx) aplica esta unidade à navegação de robôs móveis.

---

## Unidade 4 — Base de conhecimento

O material usa "base de conhecimento" em dois sentidos. Vale separar.

### Sentido geral (gestão do conhecimento)

- É uma biblioteca de informações sobre um produto, serviço ou tema, voltada ao **autosserviço**: FAQs, manuais, guias de solução de problemas, *runbooks*.
- Pode ser uma enciclopédia indexada, uma base legível por máquina ou uma base com IA que conversa com o usuário.
- As respostas usam **raciocínio dedutivo automatizado**: a cada pergunta, o software estreita as soluções possíveis. Exemplo: o chatbot da PUCPR.
- Não é um depósito estático. É um recurso **dinâmico**, que cresce com a contribuição de quem sabe.

### Sentido de SE (o que importa na disciplina)

- É onde o conhecimento adquirido fica **armazenado**, com símbolos e estruturas de dados.
- A forma mais comum são as **regras de produção**, um jeito fácil de expressar **conhecimento heurístico**, isto é, regras práticas (Ford et al., 1993).
- Esse conhecimento é **declarativo**: está escrito de forma explícita, e o especialista de domínio pode lê-lo e conferi-lo. Tornar o conhecimento legível é um dos serviços mais importantes de um sistema de representação.
- A base guarda dois tipos de conhecimento:
  - **factual**: os fatos do domínio;
  - **heurístico**: as regras de bolso do especialista.
- Formas de representação: regras de produção, frames, lógica, redes semânticas.
- A base é considerada o **coração do SE**. O motor e a interface são vitais, mas sem uma boa base não há o que inferir.
- As regras **não precisam** ser só `IF <situação> THEN <ação>`. Também dá para usar expressões lógicas.

**Dois parâmetros** caracterizam uma base de conhecimento:

1. o quanto o conhecimento é **tácito ou explícito**;
2. o quanto esse conhecimento existe num **ambiente competitivo**.

**Requisitos** de uma base para SE:

- **Representação:** parecida com um banco de dados, com regras simples que permitem representar os fatos deduzidos a partir delas.
- **Organização:** se a base for grande ou externa, é preciso **metaconhecimento** (conhecimento sobre o próprio conhecimento) para garantir integridade e definir as interfaces.

Leitura indicada: Hoppen e Trahand (1990), "Os Sistemas Especialistas em gestão no Brasil: um desafio", *Revista de Administração de Empresas*.

---

## Unidade 5 — Benefícios, vantagens e desvantagens

### Vantagens

| Vantagem | Por quê |
|---|---|
| Difunde conhecimento a baixo custo | Torna o saber do especialista acessível a mais pessoas |
| Libera o especialista | O SE faz a rotina (análises, diagnósticos simples) e o humano cuida do complexo |
| Mais flexível que um programa comum | Mudar a regra muda o comportamento, sem reescrever código; o motor de regras se adapta rápido a cada organização |
| Preserva o conhecimento | O saber continua lá quando o especialista sai de férias ou deixa a empresa |
| Reduz custos | Menos treinamento, menos tempo, menos custo administrativo |
| Documenta as decisões | Fica um registro permanente do caminho da decisão |
| Consistência | O mesmo caso recebe a mesma resposta |
| Precisão e rapidez | Focado num domínio estreito, processa muita informação seguindo regras |
| Explicação | O usuário entende como a decisão foi tomada |

### Desvantagens

| Desvantagem | Por quê |
|---|---|
| Não tem bom senso | Ainda não se sabe como dar bom senso a uma máquina |
| Não tem criatividade | Não improvisa quando não existe solução perfeita |
| Não reconhece os próprios limites | Não percebe quando não há resposta ou quando o problema está fora do seu domínio |
| Domínio estreito | Não serve para problemas que cruzam várias áreas |
| Depende da qualidade do conhecimento | Conhecimento errado, incompleto ou desatualizado gera decisões erradas |
| Lida mal com incerteza e nuance | Pode dar respostas imprecisas |
| Construção e manutenção caras | Exigem programador experiente ou equipe, e conhecimento técnico especializado |

### Por que os SEs não são mais usados

- **Custo e prazo** de desenvolvimento muitas vezes proibitivos.
- **Shells** difíceis de usar.
  - **Complemento:** um *shell* é um SE "vazio", com o motor de inferência e a interface prontos, faltando só a base de conhecimento. O material o descreve apenas como "uma interface para acessar sistemas".
- **Forma restrita** de representar: a maioria dos shells só aceita regras de produção, e nem todo conhecimento cabe nesse formato.
- O especialista tem **dificuldade de converter intuição em regras**.
- **Conflitos entre regras:** quanto maior a base, mais regras se contradizem, e atualizar ou expandir o sistema fica difícil. É o principal problema de manutenção.

> **Ponto de atenção:** o material lista como ponto forte a "capacidade de aprender e se adaptar a novos dados". Isso só vale se o SE tiver um componente de aprendizado de máquina. Num SE clássico baseado em regras, quem "ensina" é o engenheiro do conhecimento, editando a base. Ao mesmo tempo, o próprio material cita a dificuldade de atualização como desvantagem.

---

## Unidade 6 — Motor de inferência e interface do usuário

### O que o motor de inferência faz

- É o módulo de software que **aplica o conhecimento para gerar informação nova** sobre o problema.
- Num sistema de regras de produção, funciona em ciclo:
  1. compara as **condições** (o lado SE) de cada regra com os **fatos conhecidos** na memória de trabalho, que o material chama de "arquivo de contexto";
  2. se as condições forem atendidas, a regra **dispara** e a **conclusão** (o lado ENTÃO) vira um fato novo;
  3. o fato novo entra na memória de trabalho e pode ativar outras regras.
- Segundo Minsky (1986), conhecimento só é útil quando serve para alcançar objetivos. O motor é o que coloca o conhecimento da base para trabalhar sobre os fatos do caso.

### Arquitetura de um sistema de produção (Gevarter, 1982)

| Parte | Função |
|---|---|
| Conjunto de regras | O conhecimento, na forma SE … ENTÃO |
| Base de dados global | Os fatos do caso; equivale à memória de trabalho |
| Interpretador | Usa uma **estratégia de controle** para achar as regras aplicáveis e **decidir qual aplicar** |

Aplicar uma regra muda o estado da base de dados, o que habilita algumas regras e desabilita outras.

> **Complemento:** escolher qual regra disparar quando várias se aplicam ao mesmo tempo chama-se **resolução de conflitos**. Critérios comuns: prioridade da regra, regra mais específica, fato mais recente.

### Encadeamento progressivo × regressivo

| | **Progressivo** (*forward chaining*) | **Regressivo** (*backward chaining*) |
|---|---|---|
| Começa por | Os **fatos** conhecidos | Uma **hipótese** ou meta |
| Direção | Dos dados para a conclusão | Da conclusão para os dados que a comprovam |
| Pergunta que faz | "O que posso concluir com o que sei?" | "O que precisa ser verdade para essa hipótese valer?" |
| Também chamado | Orientado por dados (*data-driven*), de baixo para cima | Orientado por objetivos (*goal-driven*), de cima para baixo |

O material diz que a máquina de inferência tenta simular como o especialista pensa:

- às vezes ele parte de uma **conclusão** e busca evidências que a comprovem (regressivo);
- às vezes parte da **evidência** e chega a uma conclusão (progressivo).

**Abordagem combinada:** a estratégia de controle pode ser de cima para baixo, de baixo para cima ou as duas ao mesmo tempo, convergindo para um ponto intermediário.

**Dificuldade do regressivo:** quando a meta exige várias submetas ao mesmo tempo (uma conjunção, "A **e** B **e** C"), achar um caso que satisfaça todas pode gerar uma **explosão combinatória**. Por isso cada tipo de problema precisa de **heurísticas de domínio** e de uma arquitetura de inferência adequada.

**Modelo × dados:**

- Raciocinar de um modelo **abstrato** do domínio para afirmações mais detalhadas é o comportamento ***model-driven***, de cima para baixo. Ele gera expectativas.
- O caminho inverso, dos detalhes do problema para níveis mais abstratos ("o que tudo isso significa?"), é o ***data-driven***, de baixo para cima.

> **Complemento, exemplo resolvido** (usando o caso da pescaria da Unidade 1).
>
> Regras:
> - **R1:** SE céu nublado E umidade alta ENTÃO chance de chuva alta
> - **R2:** SE chance de chuva alta ENTÃO não ir pescar
> - **R3:** SE chance de chuva baixa E vento fraco ENTÃO ir pescar
>
> Fatos iniciais: céu nublado, umidade alta.
>
> **Progressivo:**
> 1. A memória de trabalho tem {nublado, umidade alta}.
> 2. As condições de R1 são atendidas, R1 dispara e adiciona "chance de chuva alta".
> 3. Agora as condições de R2 são atendidas, R2 dispara e adiciona "não ir pescar".
> 4. Nenhuma regra nova se aplica, e o motor para.
>
> **Regressivo:**
> 1. Meta: "não ir pescar?".
> 2. R2 conclui isso se "chance de chuva alta", que vira a submeta.
> 3. R1 conclui "chance de chuva alta" se "nublado" E "umidade alta", que viram duas submetas.
> 4. As duas estão nos fatos (ou o sistema pergunta ao usuário). Meta provada.
>
> **Ligação com a explanação:** no regressivo, se o usuário perguntar "**por que** você quer saber a umidade?", o sistema responde mostrando a regra que está testando (R1). Depois da conclusão, se ele perguntar "**como** chegou nisso?", o sistema mostra a cadeia R1 → R2.
>
> **Regra prática:** o regressivo combina com **diagnóstico** (há poucas hipóteses e ele só pergunta o que importa). O progressivo combina com **monitoramento e controle** (os dados chegam o tempo todo e é preciso reagir).

### Interface do usuário

- **Objetivo:** obter informações sobre o problema do usuário e mostrar as soluções.
- **Entrada:** a interface pode fazer perguntas, por exemplo num terminal.
- **Saída:** textos, diagramas, listas; nas interfaces mais elaboradas, gráficos e hipertexto.
- **Explicação:** o usuário pode querer saber **por que** uma pergunta está sendo feita ou **como** um fato foi concluído. A interface contém os procedimentos que geram essas explicações.
- **Usuários não humanos:** cada vez mais SEs conversam com outros softwares e com dispositivos de controle de processos.
- **Boa interface:** fácil de usar, para **reduzir a carga cognitiva** do usuário.

Leitura indicada: capítulo "Projeto de interface com o usuário" de Alves et al., *Sistemas Especialistas* (SAGAH, 2019).

---

## Unidade 7 — Memória, explanação e incerteza

### Memória de trabalho

- Armazena o **estado atual** do raciocínio: os fatos do caso que está sendo resolvido.
- É **temporária**: muda durante a consulta. A base de conhecimento, ao contrário, é **permanente**.
- Quando a condição de uma regra casa com o conteúdo da memória de trabalho, a regra pode ser executada (Luger).
- O **ciclo de controle** é o agente que **dispara as regras** e **modifica a memória de trabalho**.

| | Base de conhecimento | Memória de trabalho |
|---|---|---|
| Guarda | Regras e conhecimento do domínio | Fatos do caso atual |
| Duração | Permanente | Só durante a consulta |
| Exemplo médico | "SE tosse E febre E raio-X alterado ENTÃO suspeita de pneumonia" | "Paciente de 62 anos, tosse, febre 38,5 °C" |

### Explanação

- Responde às perguntas do usuário: **por que** e **como** algo aconteceu.
- É onde ficam as **justificativas** da solução.
- É essencial para que um especialista humano, como um médico ou engenheiro, **aceite** a recomendação do computador.

Um SE pode responder de **três formas**:

| Forma | Exemplo do material (achar um peixe) |
|---|---|
| a. Indica **em que universo** a resposta está | Sabe a espécie e o tipo de lugar, mas não em que região do lago |
| b. Determina a resposta **com precisão** | Diz onde está o peixe e em que região do lago ou mar |
| c. **Não conclui** nada, só interage com o usuário | — |

### SE × programa tradicional diante de conhecimento novo

- **Programa tradicional:** a busca se baseia em dados fixos no código. Conhecimento novo exige **alterar o código-fonte**.
- **SE:** basta acrescentar fatos e regras à base, **sem alterar a estratégia de busca** (Fernandes, 2008). É a separação entre conhecimento (base) e controle (motor).

Segundo Luger (2010), um SE heurístico:

- a) deixa o raciocínio **aberto à inspeção**: mostra as etapas intermediárias, o estado da solução e por que tomou cada decisão;
- b) permite **edição fácil** da base, acrescentando ou removendo conhecimento;
- c) **raciocina heuristicamente**, usando regras práticas para achar soluções úteis.

### Incerteza

- O SE calcula um **grau de certeza** para cada conclusão, com base na confiabilidade das informações. Isso dá ao usuário uma medida de quanto confiar na recomendação.
- **Exemplo do material:** num SE de diagnóstico, um exame de sangue anormal **reduz o grau de certeza** de um diagnóstico de "sem doença", porque sugere que algo está errado.
- No exemplo completo, as três ideias aparecem juntas:
  - a **memória de trabalho** guarda idade, histórico e exames do paciente;
  - a **incerteza** gera o grau de certeza do diagnóstico;
  - a **explanação** mostra ao médico como o sistema chegou ali, o que aumenta a confiança dele.

> **Complemento, fator de certeza (MYCIN):** o SE médico clássico MYCIN usava **fatores de certeza (FC)** entre −1 (certamente falso) e +1 (certamente verdadeiro). Quando duas regras independentes apoiam a mesma conclusão com FC₁ e FC₂ positivos, o resultado é FC₁ + FC₂ × (1 − FC₁). Exemplo: 0,6 e 0,5 resultam em 0,6 + 0,5 × 0,4 = **0,8**. Duas evidências fracas somadas dão mais certeza, mas nunca passam de 1.

---

## Unidade 8 — Estágios de desenvolvimento de um SE

### Quem participa

- **Engenheiro do conhecimento:** especialista em IA (cientista da computação ou programador) que sabe construir SEs. Não há critério universal para definir a profissão, que é relativamente nova. O material também o chama de "engenheiro de dados".
- **Especialista de domínio:** tem experiência significativa na área. **Não precisa entender de IA**, pois traduzir o conhecimento dele é tarefa do engenheiro.
- Os dois trabalham **juntos durante todo o ciclo de vida**.

### Os cinco estágios (Figura 1, adaptada de Sylvester et al., 2014)

| Estágio | O que faz (rótulo da figura) |
|---|---|
| 1. Identificação | Determinar as características do problema |
| 2. Conceitualização | Buscar o conceito da solução do problema |
| 3. Formalização (*design*) | Projetar as estruturas que organizam o conhecimento |
| 4. Implementação | Formular as regras que dão suporte ao conhecimento |
| 5. Teste | Validar as regras (validação, verificação e manutenção) |

O ciclo **não é linear**. O resultado do teste pode mandar o projeto de volta para qualquer estágio anterior:

```
Identificação ─► Conceitualização ─► Formalização ─► Implementação ─► Teste
      ▲                 ▲                  ▲                ▲            │
      │                 │                  │                └ refinamento┤
      │                 │                  └──────── redesign ───────────┤
      │                 └─────────────── reformular ─────────────────────┤
      └──────────────────────────────────────────────────────────────────┘
```

- **Refinamento:** ajustar as regras (volta à implementação).
- **Redesign:** mudar a estrutura do conhecimento (volta à formalização).
- **Reformular:** repensar o conceito da solução (volta à conceitualização) ou o próprio problema (volta à identificação).

### 1. Identificação

- Definir com clareza **o problema** que o SE vai resolver e **os objetivos**.
- Levantar as **características** e **limitações** do problema.
- Analisar os **recursos** disponíveis: tempo, equipamentos, dados e informações.
- Quebrar o problema em **subtarefas**, com as etapas intermediárias e os recursos de cada uma.
- Definir os recursos para **adquirir o conhecimento**: dados, entrevistas com especialistas, pesquisa bibliográfica.
- **Documentar as metas por escrito.** Abordagens como busca heurística, busca em largura, busca em profundidade e raciocínio dirigido são todas orientadas por objetivos.

**Figura 2, ciclo de descrição do problema:**

1. O especialista descreve o caso.
2. O engenheiro do conhecimento redige a descrição do problema.
3. Pergunta: "isso descreve o problema adequadamente?"
   - **Não:** volta ao especialista.
   - **Sim:** a descrição está completa.

### 2. Conceitualização

- **Tarefa central:** diagramar os principais **conceitos e relações** do sistema, criando a base conceitual de um protótipo.
- Decompor o problema em **subproblemas**, separando a análise do problema do motor de inferência.
- Identificar os **conceitos-chave**.
- **Testar** conceitos e relações com exemplos concretos de resolução de problemas, para garantir que cobrem todos os casos gerais.

**Figura 3:** o mesmo ciclo de verificação, agora entre Identificação e Conceitualização. Pergunta: "isso identifica o problema adequadamente?" Se não, volta à identificação. Se sim, a descrição está completa.

### 3. Formalização (projeto lógico)

- Mapear os conceitos, subproblemas e o fluxo de informação da conceitualização em **representações formais**, com ferramentas de engenharia do conhecimento.
- Identificar três coisas:
  - o **espaço de hipóteses**: o conjunto de todas as soluções possíveis;
  - o **modelo subjacente** do domínio;
  - as **características dos dados**.
- Os conceitos dão pistas sobre o espaço de hipóteses: é finito? Tem hierarquia? Admite níveis de abstração?
- Especificar **como o sistema vai atender aos requisitos** das fases anteriores. Primeiro se definem as **saídas** (relatórios e resultados).
- **Na prática:**
  1. organizar o conhecimento num **esquema, diagrama hierárquico, matriz ou tabela de decisão**;
  2. converter esse material em **regras SE … ENTÃO**, seguindo o procedimento recomendado pela ferramenta escolhida.

### 4. Implementação (projeto físico)

1. Construir um **protótipo de um segmento** do sistema: traduzir uma parte do conhecimento em regras e testar essa parte.
2. Quando o protótipo funcionar, **expandir um segmento de cada vez** até chegar ao sistema final.

### 5. Testes

- O material resume esta fase como **validação, verificação e manutenção** (na figura: validação das regras).
- A conclusão da unidade reforça:
  - a necessidade de **equipe interdisciplinar**;
  - a **avaliação contínua** do desempenho, para adaptar o SE às mudanças do ambiente;
  - o uso de **diagramas** para acompanhar o processo.

> **Complemento, verificação × validação:**
> - **Verificação** pergunta "construí o sistema **corretamente**?": as regras estão consistentes, sem contradições, sem regras redundantes ou que nunca disparam?
> - **Validação** pergunta "construí o sistema **certo**?": as respostas batem com as do especialista em casos reais?

---

## Erros e imprecisões do material

| Onde | O que o material diz | O correto |
|---|---|---|
| U2, SE fuzzy | "A lógica fuzzy opera com dois valores de verdade, 1 e 0" | Isso é a lógica **clássica** (booleana). A fuzzy usa qualquer valor entre 0 e 1, como o próprio texto diz logo depois. |
| U2, referência | "Negnetsky" | **Negnevitsky** (2008), autor de *Artificial Intelligence: A Guide to Intelligent Systems*. |
| U3, referência | "LUCAS VAN DER GRAAL, 1991" | **Lucas e Van der Gaag** (1991), *Principles of Expert Systems*, como a própria U2 cita. |
| U3, referência | Clancey aparece como 1989 no texto e 1986 na lista de referências | O artigo "Viewing knowledge bases as qualitative models" (*IEEE Expert*) é de **1989**. |
| U3, referência | A definição de Pearl (1984) aponta para *Probabilistic reasoning in intelligent systems* | Essa definição vem de *Heuristics: Intelligent Search Strategies for Computer Problem Solving* (**1984**). O outro livro é de 1988. |
| U3, ontologias | A ontologia "é considerada no nível do semântico ou físico" | Para Gruber, a ontologia fica no nível **semântico**. Os modelos de dados é que ficam no nível lógico ou físico. |
| U3, aquisição | A modelagem é feita por "um engenheiro de software" com o especialista | Quem faz a aquisição é o **engenheiro do conhecimento**, como o resto da unidade diz. |
| U3, heurísticas | Dirigir, escovar os dentes e digitar sem olhar são "heurísticas" | São mais **hábitos automatizados** (conhecimento tácito). Em IA, heurística é uma regra prática que orienta uma escolha, sem garantia de acerto. |
| U4 e U5 | A base ou o SE "aprende" sozinho | Só com um componente de aprendizado de máquina. No SE clássico, o conhecimento é editado pelo engenheiro. |
| U6, 1º parágrafo sobre encadeamento | Chama de *backward* o raciocínio que parte das condições, e chama o raciocínio de trás para frente de "para frente ou regressivo" | Progressivo (*forward*) parte dos fatos. Regressivo (*backward*) parte da hipótese. O próprio PDF acerta mais adiante. |
| U6 | "driven esperado" | ***Data-driven*** (orientado por dados), o oposto de *model-driven*. |
| U6 | "subguias conjuntivas" | **Submetas conjuntivas** (*conjunctive subgoals*): várias metas que precisam ser satisfeitas ao mesmo tempo. |
| U7 | "etapas intermediárias servem para tirar dúvidas sobre o processo de cobrança" | Provável erro de tradução. Luger fala do **processo de raciocínio**, que deve ficar aberto à inspeção. |
| U7 | O exemplo médico aparece duas vezes, a primeira com doenças "pulmonares" e a segunda com "cardíacas" | É o mesmo exemplo repetido. |
| U8 | "Engenheiro de dados" | O termo padrão é **engenheiro do conhecimento**, que a própria unidade usa no primeiro parágrafo. |

---

## Glossário

| Termo | Definição curta |
|---|---|
| **SE / SBC** | Sistema especialista / sistema baseado em conhecimento: programa que resolve problemas de um domínio com conhecimento de especialistas humanos e explica a solução |
| **Domínio** | Área em que a tarefa é realizada |
| **Tarefa** | Atividade orientada a metas: diagnóstico, planejamento, programação, configuração, projeto |
| **Heurística** | Regra prática ou "regra de bolso" do especialista, que costuma funcionar, mas sem garantia |
| **Regra de produção** | Regra no formato SE condição ENTÃO ação ou conclusão |
| **Fato** | Informação sobre o caso atual, guardada na memória de trabalho |
| **Base de conhecimento** | Onde fica o conhecimento permanente do domínio, factual e heurístico |
| **Memória de trabalho** | Onde ficam os fatos temporários da consulta atual |
| **Motor de inferência** | Aplica as regras aos fatos para gerar conclusões |
| **Encadeamento progressivo** | Dos fatos para as conclusões (*forward chaining*, *data-driven*) |
| **Encadeamento regressivo** | Da hipótese para os fatos que a sustentam (*backward chaining*, *goal-driven*) |
| **Ciclo de controle** | Laço que escolhe e dispara regras e atualiza a memória de trabalho |
| **Frame / slot** | Estrutura que representa um conceito (frame) com seus atributos (slots) |
| **Conjunto fuzzy** | Conjunto em que cada elemento pertence com um grau entre 0 e 1 |
| **Variável linguística** | Variável cujos valores são palavras ("perto", "longe") ligadas a conjuntos fuzzy |
| **Grau de certeza** | Número que expressa o quanto o SE confia numa conclusão |
| **Explanação** | Capacidade de responder "por quê?" e "como?" sobre o raciocínio |
| **Conhecimento tácito** | Sabe fazer, mas não sabe explicar; aparece na ação |
| **Conhecimento explícito** | Pode ser escrito e transmitido em linguagem formal |
| **Conhecimento declarativo** | Conhecimento escrito de forma explícita e legível, como as regras na base |
| **Metaconhecimento** | Conhecimento sobre o próprio conhecimento: organização, integridade, interfaces da base |
| **Shell** | SE sem base de conhecimento: motor e interface prontos, à espera das regras |
| **Engenheiro do conhecimento** | Quem extrai o conhecimento do especialista e o transforma no SE |
| **Especialista de domínio** | Quem detém o conhecimento da área; não precisa saber IA |
| **Aquisição de conhecimento** | Fase em que o engenheiro coleta o conhecimento do especialista para construir a base |
| **Conhecimento superficial** | Heurísticas e fatos para resolver rápido; origem da maioria das regras de produção |
| **Conhecimento profundo** | Fundamentos do domínio: definições, axiomas, leis, causalidade |
| **Ontologia** | Modelo de um domínio com classes, atributos e relações, no nível semântico |
| **Investigação contextual** | Observar o usuário ou o especialista em ação e fazer perguntas a partir do que se vê |
| **Espaço de hipóteses** | Conjunto de todas as soluções possíveis, definido na formalização |

---

## Perguntas para revisar

Tente responder antes de abrir a resposta.

<details>
<summary>1. Em que situação um SE é a escolha apropriada?</summary>

Quando há conhecimento especializado **escasso ou caro**, num **domínio estreito**, e se quer **apoiar** a decisão de quem não é especialista, na ausência dele, com **explicação** do raciocínio. O SE não substitui o julgamento do especialista.
</details>

<details>
<summary>2. Qual a diferença entre tarefa, domínio e domínio da tarefa?</summary>

**Tarefa** é a atividade orientada a metas (por exemplo, diagnosticar). **Domínio** é a área em que ela é feita (por exemplo, medicina pulmonar). **Domínio da tarefa** é o esforço intelectual que o SE precisa capturar para executá-la.
</details>

<details>
<summary>3. Quais são os três componentes essenciais de um SE? E os cinco do SE baseado em regras?</summary>

**Essenciais:** base de conhecimento, motor de inferência e interface do usuário.

**Baseado em regras:** base de conhecimento, banco de dados (fatos), motor de inferência, facilidade de explicação e interface do usuário.
</details>

<details>
<summary>4. Por que a entrevista com o especialista é indispensável, se existem livros sobre o assunto?</summary>

Livros e manuais só trazem o conhecimento **explícito**. O conhecimento **tácito** (as regras de bolso, o "faro" do especialista) não está escrito em lugar nenhum e só aparece na conversa ou na observação da ação. Sem ele o SE perde eficiência.
</details>

<details>
<summary>5. Quando usar um SE fuzzy? E um baseado em frames?</summary>

**Fuzzy:** quando o especialista raciocina com termos vagos e graduais ("muito perto", "moderado").

**Frames:** quando o domínio tem muitos conceitos com atributos e hierarquia. O motor pesquisa só os frames relevantes, em vez de todas as regras.
</details>

<details>
<summary>6. Cite três diferenças entre um SE e um programa convencional.</summary>

- **Conhecimento:** no SE é fragmentado e vem da experiência; no programa convencional é completo e cabe em fórmulas e algoritmos.
- **Regras:** no SE são complexas e condicionais; no convencional são simples.
- **Solução:** no SE é dinâmica e depende do contexto dos fatos; no convencional é previsível e repetitiva.
- **Desempenho:** o SE é medido pela exatidão **e** pelo caminho até a resposta.

Nenhum dos dois é superior; depende do problema.
</details>

<details>
<summary>7. O que é uma heurística e quais as duas exigências que ela precisa equilibrar, segundo Pearl?</summary>

É um critério, método ou princípio para escolher, entre várias ações possíveis, a mais promissora para atingir um objetivo. Não garante a solução.

As duas exigências: ser **simples** e **distinguir bem** as escolhas boas das ruins.
</details>

<details>
<summary>8. O que é uma ontologia em informática e para que ela serve num SE?</summary>

É um conjunto de representações que modela um domínio, com **classes, atributos e relações**, no nível semântico.

Num SE, permite **raciocínio automatizado** e dá um **vocabulário comum** para o que entra e sai do sistema.
</details>

<details>
<summary>9. Qual a diferença entre conhecimento superficial e profundo?</summary>

**Superficial:** fatos e heurísticas para resolver o problema rápido. É a base da maioria das regras de produção.

**Profundo:** os fundamentos do domínio, como definições, axiomas, leis e princípios de causalidade.
</details>

<details>
<summary>10. Como funcionam os métodos de entrevista de observação, intuitivo e combinado?</summary>

- **Observação:** o engenheiro assiste ao especialista resolvendo um problema, sem interromper, e transcreve tudo depois.
- **Intuitivo:** o engenheiro interage com o especialista e estuda a literatura; juntos, constroem a teoria e o comportamento prático.
- **Combinado:** o engenheiro faz perguntas durante a solução, estimula o especialista a contar experiências, testa o conhecimento dele e sugere bases lógicas que facilitam criar as regras.
</details>

<details>
<summary>11. Por que a base de conhecimento é chamada de "coração" do SE?</summary>

Porque é ela que contém o conhecimento factual e heurístico do especialista. O motor só aplica esse conhecimento, e a interface só o comunica. Uma base ruim gera conclusões ruins, por melhor que seja o motor.
</details>

<details>
<summary>12. Por que uma base de regras grande é difícil de manter?</summary>

Com muitas regras surgem **conflitos** entre elas: regras que se contradizem ou se sobrepõem. Atualizar ou expandir o sistema fica complexo, e o conhecimento muda com o tempo. Além disso, nem todo conhecimento intuitivo cabe bem no formato de regra.
</details>

<details>
<summary>13. Qual a diferença entre encadeamento progressivo e regressivo? Qual combina com diagnóstico?</summary>

O **progressivo** parte dos fatos e deriva conclusões até não haver mais regras aplicáveis. O **regressivo** parte de uma hipótese e procura os fatos que a comprovam, criando submetas.

Para diagnóstico, o **regressivo** costuma ser melhor: testa hipóteses e só pergunta ao usuário o que é relevante para elas.
</details>

<details>
<summary>14. Qual a diferença entre base de conhecimento e memória de trabalho?</summary>

A **base** guarda o conhecimento **permanente** do domínio (as regras). A **memória de trabalho** guarda os fatos **temporários** do caso em consulta, inclusive os fatos novos que o motor vai inferindo.
</details>

<details>
<summary>15. Quais são as três formas de resposta de um SE?</summary>

1. Indicar em que **universo** a resposta está, sem precisar o ponto exato.
2. Dar a resposta **precisa**.
3. **Não concluir** nada, apenas interagir com o usuário.
</details>

<details>
<summary>16. Por que adicionar conhecimento a um SE é mais simples que num programa tradicional?</summary>

Porque o SE **separa o conhecimento (base) do controle (motor)**. Basta adicionar fatos ou regras à base, sem mexer na estratégia de busca. No programa tradicional, o conhecimento está no próprio código, que precisa ser alterado.
</details>

<details>
<summary>17. Quais são os cinco estágios de desenvolvimento e para onde o teste pode mandar o projeto de volta?</summary>

Identificação → conceitualização → formalização → implementação → teste.

Depois do teste, o projeto pode voltar:
- por **refinamento**, para a implementação;
- por **redesign**, para a formalização;
- por **reformulação**, para a conceitualização ou até a identificação.
</details>

<details>
<summary>18. Qual o papel do engenheiro do conhecimento e do especialista de domínio?</summary>

O **especialista de domínio** tem o conhecimento da área e não precisa entender de IA. O **engenheiro do conhecimento** sabe construir SEs: extrai o conhecimento do especialista e o transforma em regras, frames e outras estruturas. Os dois trabalham juntos durante todo o ciclo de vida.
</details>

<details>
<summary>19. Na formalização, o que é o espaço de hipóteses?</summary>

É o conjunto de **todas as soluções possíveis** do domínio. Os conceitos formalizados mostram como ele é: finito ou não, se tem hierarquia, se admite níveis de abstração. Isso orienta a busca do motor de inferência.
</details>
