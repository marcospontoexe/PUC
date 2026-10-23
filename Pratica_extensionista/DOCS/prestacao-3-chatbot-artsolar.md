# Prestação de serviços 3: chatbot de atendimento para a ArtSolar (100 h)

Candidata a substituir a [prestação do AGV](prestacao-2-agv-regressao.md), caso aquela seja tarefa do emprego do usuário. Com a Formação (30 h) e o harness (100 h), o total chega a **230 h**.

## A empresa

A ArtSolar é uma pequena empresa de engenharia criada por dois jovens empreendedores. Trabalha com:
- energia solar (geração distribuída);
- laudo de inspeção elétrica;
- projetos elétricos;
- plano de eficiência energética.

Os clientes falam com a empresa hoje por WhatsApp, e-mail e pela página de contato do site. Missão, visão e valores foram fornecidos pelo usuário em 2026-10-22. O foco é sustentabilidade, economia do cliente e esclarecer as informações dos processos.

## Descrição para a Calculadora

Tem cerca de 484 caracteres com os valores de exemplo; os colchetes devem ser trocados por dados reais. O texto segue o formato que atende ao feedback do tutor sobre o harness: comunidade, atividades, interação e presencialidade explícitas.

> Na ArtSolar, empresa de energia solar e projetos elétricos em [Curitiba], a equipe de [4] pessoas responde [80] contatos/mês por WhatsApp, e-mail e site. Em 4 visitas presenciais vou: 1) levantar com os engenheiros as dúvidas comuns e os dados de cada orçamento; 2) instalar no site um chatbot que tira dúvidas, estima a economia e encaminha o cliente; 3) treinar a equipe para atualizar o bot; 4) medir resultados e coletar feedback. Meta: ampliar o acesso à energia solar (ODS 7.2).

## O que o chatbot faz

| Função | Detalhe |
|---|---|
| Triagem por serviço | Pergunta o que o cliente procura (solar, laudo, projeto elétrico, eficiência) e abre o fluxo correspondente |
| Qualificação do pedido de orçamento solar | Coleta cidade, tipo de imóvel (residencial, comercial, rural), consumo médio em kWh ou valor médio da conta, tipo de telhado e contato |
| Estimativa prévia de economia | Calcula a potência aproximada do sistema e a economia a partir do consumo. A fórmula e os parâmetros são validados pelos engenheiros, e o resultado aparece sempre como "estimativa preliminar, sujeita a visita técnica" |
| Perguntas frequentes | Como funciona a energia solar, créditos de energia, manutenção, prazos, garantia, financiamento, o que é um laudo de inspeção e um plano de eficiência. O conteúdo é escrito e validado pela ArtSolar |
| Encaminhamento para a equipe | Botão "falar no WhatsApp" (link wa.me) com uma mensagem já preenchida que resume os dados coletados. Integra o WhatsApp sem precisar da API paga |
| Registro de contatos | Envia os dados do cliente por e-mail ou para uma planilha da equipe |

**Fora do escopo inicial:** bot dentro do próprio WhatsApp. Exige a API oficial da Meta, que tem aprovação e custo. Automação não oficial do WhatsApp viola os termos e pode levar ao banimento do número.

## Técnica

Arquitetura híbrida, partindo do [AtendeBot](../../19-Agentes%20Conversacionais/somativa%202/projeto/README.md):
- **Fluxos fixos** (máquina de estados) para a triagem e a qualificação.
- **Classificador de intenções** (TF-IDF) ou **RAG** para as perguntas frequentes, sempre com a regra "não sei, vou chamar a equipe".

**LGPD:**
- Não pedir foto da conta de luz, CPF nem número da unidade consumidora. A conta vai direto para a equipe, pelo WhatsApp.
- Mostrar aviso de privacidade antes de coletar dados.
- Os dados ficam só com a ArtSolar e não vão para o repositório.

## Etapas e horas (somam 100 h)

| # | Etapa | Horas | Presencial |
|---|---|---|---|
| 1 | Reunião inicial e Termo de aceite | 2 | sim |
| 2 | Diagnóstico com a equipe: dúvidas mais frequentes (amostra anonimizada de conversas), dados que cada orçamento exige, volume de contatos e tempo de resposta atual (linha de base) | 6 | sim |
| 3 | Redação e postagem do planejamento | 6 | |
| 4 | Base de conhecimento: redigir as respostas e os fluxos por serviço e validar com os engenheiros | 12 | parcial |
| 5 | Desenvolvimento: fluxos, perguntas frequentes, estimativa prévia, encaminhamento e registro de contatos | 32 | |
| 6 | Testes com a equipe (simulações de atendimento) e ajustes | 8 | sim |
| 7 | Publicação no site, com aviso de privacidade | 6 | sim |
| 8 | Manual para atualizar o bot | 4 | |
| 9 | Treinamento da equipe | 3 | sim |
| 10 | Acompanhamento (2–4 semanas de uso real) | 8 | |
| 11 | Medição dos resultados e apresentação | 5 | sim |
| 12 | Coleta de feedback (Feedback da comunidade) | 2 | sim |
| 13 | Redação e postagem da execução | 6 | |

## Campos específicos da prestação

- **ODS:** 7, meta 7.2 (aumentar a participação das energias renováveis). Como secundários, 7.3 (eficiência energética) e 8.3 (crescimento de micro e pequenas empresas). ESG ambiental, que combina com os valores da empresa.
- **Resultados esperados (1.10):** metas comparadas com a linha de base da etapa 2:
  - tempo da primeira resposta;
  - percentual de pedidos de orçamento que já chegam com os dados completos;
  - número de contatos qualificados por mês.
- **Relação com a teoria (1.11):**
  - Agentes Conversacionais (19), com o AtendeBot;
  - PLN (13);
  - Engenharia do Conhecimento (18): base de conhecimento;
  - Sistemas Especialistas (17), Unidade 3: aquisição de conhecimento com especialistas de domínio, que aqui são os engenheiros;
  - Segurança da Informação (10): LGPD;
  - IA na Gestão de Negócios (22): atendimento e captação de clientes.

## Pendências

- **Elegibilidade:** confirmar que o usuário não é sócio nem funcionário da ArtSolar e não será pago.
- **Dados para a descrição:** cidade, tamanho da equipe e volume de contatos por mês.
- **Site:** descobrir a plataforma (WordPress, Wix etc.) para saber como embutir o chat e onde hospedar.
- **Propriedade intelectual:** o código do AtendeBot entra como propriedade intelectual anterior (Anexo 2, item 5).
