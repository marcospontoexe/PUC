# 1. Descrição do Cenário

## a) Objetivo do Agente

O **AtendeBot** é um agente conversacional de **Serviço de Atendimento ao Cliente (SAC)** desenvolvido para a empresa fictícia **TeleConecta Brasil**, uma operadora de telecomunicações que oferece serviços de telefonia móvel, internet banda larga e TV por assinatura.

O objetivo principal do agente é **automatizar o atendimento de primeiro nível**, resolvendo as demandas mais frequentes dos clientes de forma rápida, eficiente e disponível 24 horas por dia, 7 dias por semana. O agente é capaz de:

- **Consultar informações de planos** contratados pelo cliente
- **Verificar status de faturas** e informar valores, vencimentos e status de pagamento
- **Registrar e acompanhar chamados técnicos** (problemas de conexão, sinal, etc.)
- **Oferecer upgrade de planos** com base no perfil do cliente
- **Responder perguntas frequentes** sobre serviços, cobertura e políticas da empresa
- **Encaminhar para atendente humano** quando a demanda extrapola sua capacidade

## b) Contexto da Organização

A **TeleConecta Brasil** é uma operadora de telecomunicações de médio porte que atua em todo o território nacional, atendendo aproximadamente 5 milhões de clientes. A empresa oferece três categorias de serviços:

- **Telefonia Móvel**: planos pré-pago e pós-pago
- **Internet Banda Larga**: planos residenciais de fibra óptica
- **TV por Assinatura**: pacotes de canais e streaming

A central de atendimento da empresa recebe, em média, **15.000 chamados por dia**, dos quais aproximadamente **60% são consultas simples e repetitivas** (segunda via de fatura, status de plano, dúvidas sobre cobertura). O tempo médio de espera para atendimento humano é de **12 minutos**, gerando insatisfação significativa entre os clientes.

## c) Motivação e Problemas a Resolver

A construção do AtendeBot é motivada pelos seguintes problemas identificados:

### Problemas Operacionais
1. **Alto volume de chamados repetitivos**: 60% das demandas são consultas simples que poderiam ser automatizadas
2. **Tempo de espera elevado**: média de 12 minutos para atendimento humano
3. **Custo operacional alto**: manutenção de uma equipe grande de atendentes para demandas de baixa complexidade
4. **Indisponibilidade fora do horário comercial**: clientes não conseguem resolver problemas à noite ou em fins de semana

### Problemas de Experiência do Cliente
5. **Baixa satisfação (NPS)**: o NPS da empresa está em 35, abaixo da média do setor (45)
6. **Alta taxa de abandono**: 25% dos clientes desistem da ligação antes de ser atendidos
7. **Inconsistência nas respostas**: diferentes atendentes fornecem informações conflitantes

### Benefícios Esperados
- **Redução de 40% no volume** de chamados direcionados a atendentes humanos
- **Atendimento 24/7** sem custo adicional
- **Tempo de resposta inferior a 5 segundos** para consultas automatizadas
- **Padronização das respostas** e informações fornecidas aos clientes
- **Melhoria de 15 pontos no NPS** da empresa
- **Escalabilidade**: capacidade de atender picos de demanda sem contratações adicionais
