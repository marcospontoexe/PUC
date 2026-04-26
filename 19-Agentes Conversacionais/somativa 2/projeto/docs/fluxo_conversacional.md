# 2. Definição do Fluxo Conversacional

## Fluxograma Principal

O fluxo conversacional do AtendeBot segue a estrutura abaixo. O diagrama pode ser
visualizado em ferramentas compatíveis com Mermaid (GitHub, VS Code com extensão, etc.).

```mermaid
flowchart TD
    A([Início]) --> B[Saudação e Boas-vindas]
    B --> C{Solicitar CPF<br/>para identificação}
    C --> D{CPF válido?}
    D -- Não --> E[Solicitar CPF novamente<br/>até 3 tentativas]
    E --> D
    D -- Falhou 3x --> F[Encaminhar atendente humano]
    D -- Sim --> G[Identificar cliente no banco]
    G --> H{Cliente encontrado?}
    H -- Não --> I[Informar que CPF não<br/>está cadastrado]
    I --> F
    H -- Sim --> J[Saudar cliente pelo nome]
    J --> K{Aguardar mensagem<br/>do cliente}

    K --> L{Classificar Intenção}

    L -- consultar_plano --> M[Buscar dados do plano<br/>no banco de dados]
    M --> N[Exibir informações<br/>do plano atual]
    N --> K

    L -- consultar_fatura --> O[Buscar faturas<br/>do cliente]
    O --> P[Exibir valor, vencimento<br/>e status de pagamento]
    P --> K

    L -- segunda_via --> Q[Gerar link de<br/>segunda via da fatura]
    Q --> R[Enviar link<br/>ao cliente]
    R --> K

    L -- problema_tecnico --> S{Coletar detalhes<br/>do problema}
    S --> S1[Identificar tipo:<br/>internet/celular/TV]
    S1 --> S2[Registrar chamado<br/>técnico no sistema]
    S2 --> S3[Informar protocolo<br/>e prazo de resolução]
    S3 --> K

    L -- upgrade_plano --> T[Buscar planos<br/>disponíveis para upgrade]
    T --> U[Apresentar opções<br/>com preços]
    U --> V{Cliente aceita?}
    V -- Sim --> W[Confirmar alteração<br/>do plano]
    W --> K
    V -- Não --> K

    L -- falar_atendente --> F

    L -- faq --> X[Buscar resposta na<br/>base de conhecimento]
    X --> Y[Exibir resposta]
    Y --> K

    L -- despedida --> Z[Mensagem de despedida<br/>e pesquisa de satisfação]
    Z --> AA([Fim])

    L -- não_compreendido --> AB[Pedir para reformular]
    AB --> AC{Tentativa > 2?}
    AC -- Sim --> F
    AC -- Não --> K

    F --> AD[Transferir para<br/>atendente humano]
    AD --> AA
```

## Descrição das Intenções (Intents)

| Intent | Descrição | Exemplos de Frases |
|--------|-----------|-------------------|
| `saudacao` | Cliente cumprimenta o agente | "Olá", "Bom dia", "Oi, tudo bem?" |
| `consultar_plano` | Consulta sobre plano contratado | "Qual meu plano?", "Quero ver meu plano atual" |
| `consultar_fatura` | Consulta sobre faturas/contas | "Quanto é minha fatura?", "Qual o valor da conta?" |
| `segunda_via` | Solicita segunda via de boleto | "Preciso da segunda via", "Quero reimprimir o boleto" |
| `problema_tecnico` | Relata problema técnico | "Minha internet caiu", "Sem sinal no celular" |
| `upgrade_plano` | Interesse em mudar de plano | "Quero um plano melhor", "Como faço upgrade?" |
| `falar_atendente` | Solicita atendente humano | "Quero falar com atendente", "Me transfere para alguém" |
| `faq` | Perguntas gerais | "Qual a área de cobertura?", "Como cancelar?" |
| `despedida` | Cliente se despede | "Tchau", "Obrigado, é só isso", "Até mais" |
| `agradecimento` | Cliente agradece | "Obrigado", "Valeu", "Agradeço" |

## Descrição das Entidades

| Entidade | Descrição | Exemplos |
|----------|-----------|----------|
| `cpf` | CPF do cliente | "123.456.789-00", "12345678900" |
| `tipo_servico` | Tipo de serviço referido | "internet", "celular", "TV", "telefone" |
| `tipo_problema` | Natureza do problema técnico | "sem sinal", "lento", "caindo", "não funciona" |
| `mes_referencia` | Mês de referência da fatura | "janeiro", "março", "mês passado" |
| `nome_plano` | Nome de um plano específico | "Plano Turbo 200", "Básico Fibra" |

## Regras de Fallback

1. Se a intenção não for identificada com confiança (score < 0.4), o agente pede para o usuário reformular.
2. Após 2 tentativas sem compreensão, o agente transfere para atendente humano.
3. Se o cliente ficar inativo por mais de 5 minutos, o agente pergunta se ainda precisa de ajuda.
4. Palavras ofensivas são detectadas e geram uma resposta educada solicitando respeito.
