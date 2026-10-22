# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Pasta do repositório `PUC` (github.com/marcospontoexe/PUC) com o material da disciplina **Cloud Computing** (PUCPR EAD). Há os PDFs das 8 unidades e o resumo de estudo [resumo.md](resumo.md). Não há código, build, testes nem entregas de atividades. Escrever sempre em pt-BR. O estado da sessão fica em [CONTEXTO.md](CONTEXTO.md).

No [resumo.md](resumo.md), o que não está nos PDFs fica marcado como **Nota do resumo**. Mantenha essa marcação ao editar, para separar o conteúdo da disciplina dos complementos.

A disciplina usa o **Microsoft Azure** (conta Azure for Students, com crédito de US$ 100) e faz tudo pelo portal web. O material não tem scripts de Azure CLI, Terraform nem Bicep. AWS e Google Cloud aparecem só como comparação.

## Como ler os PDFs

O texto sai limpo com `pypdf`, sem ruído de menu do AVA. Grave a saída em UTF-8 no scratchpad, porque o console do PowerShell estraga os acentos:

```powershell
# Extrai o texto de um PDF, página a página (separador "=== PAGE ===")
python -c "import pypdf,sys; open(sys.argv[2],'w',encoding='utf-8').write('\n=== PAGE ===\n'.join(p.extract_text() or '' for p in pypdf.PdfReader(sys.argv[1]).pages))" "<arquivo>.pdf" "<scratchpad>\saida.txt"
```

- Boa parte do conteúdo é imagem: capturas do portal do Azure (marcadas com `#ParaTodosVerem`) e diagramas. Para vê-las, use Read com `pages`, um intervalo por chamada (ex.: `"3-4"`).
- Os vídeos não estão nos PDFs. Nas Unidades 4 a 7, o passo a passo prático está quase todo neles, e o PDF traz só o título (`Vídeo 01/14 – Criação da VM`) e uma ou duas frases. Por isso a Unidade 4 tem 53 páginas e pouco texto.
- Os visualizadores embutidos (Canva/PDF) foram capturados cortados, e o texto deles não sai na extração:
  - Unidade 2, p. 10, "Nuvem, estrutura local e nuvem privada": só o Exemplo 1 (nuvem pública) aparece inteiro. O Exemplo 2 (on-premises) é cortado no meio e o seguinte não aparece.
  - Unidade 2, p. 12, glossário: os cartões de nuvem privada, nuvem pública e servidores locais são legíveis. O cartão verde (pelo contexto, nuvem híbrida) e o de infraestrutura de nuvem saem cortados na lateral.
  - Unidade 3, p. 20, infográfico "Do que preciso saber para provisionar serviços na nuvem?": está cortado, mas as mesmas perguntas estão em texto nas pp. 15–18.

## Onde está cada conceito

| Unidade | Págs. | Conceitos |
|---|---|---|
| [1](1-A%20nuvem%20que%20%C3%A9%20feita%20de...%20bits%20e%20bytes.pdf) | 14 | Por que usar nuvem; IaaS, PaaS e SaaS (FaaS e CaaS só citados); exercício com 6 situações e gabarito |
| [2](2-TIC%20na%20ess%C3%AAncia%20da%20nuvem.pdf) | 16 | TIC e nuvem; portal do Azure; região (custo × latência × LGPD/GDPR); licença própria; nuvem pública, privada, híbrida e servidores locais; multicloud; case de agronegócio |
| [3](3-Provisionando%20na%20nuvem%20o%20provisionamento%20do%20papel.pdf) | 33 | Provisionar VM: região, imagem (licença Windows custa mais), x64 × Arm64; perguntas de levantamento; séries de VM e IOPS; abordagens de sizing; grupo de recursos; exercício do sistema de crédito |
| [4](4-sistema%20l%C3%A1%20na%20nuvem.pdf) | 53 | Prática: duas VMs Linux (chave `.pem`, IP privado × público, ping/telnet), Banco de Dados SQL e firewall, Aplicativo de Funções (plano de consumo, gatilho HTTP), Aplicativo Web (CI/CD com GitHub, FTP) |
| [5](5-Gerenciar%20o%20gerenciamento%20e%20monitorar%20o%20monitoramento.pdf) | 18 | Monitoramento: interface de rede e IP público, alertas, métricas (diagnóstico e planejamento), desligamento automático de dev/homologação, plano de ação × plano de contingência, gestão à vista; quiz de 4 questões |
| [6](6-Protegendo%20seus%20custos%20com%20firewall%20e%20login.pdf) | 20 | Segurança × custo: WAF global (Front Door) × regional (Application Gateway), modo detecção × prevenção (HTTP 403), Gateway de Aplicativo |
| [7](7-Traga%20mais%20servidores%20e%20sua%20carteira.pdf) | 21 | Alta disponibilidade: redundância pelo gateway, escala horizontal × vertical, VMSS (imagem personalizada ou script PowerShell), resiliência, backup e restore, plano de disaster recovery e seu teste |
| [8](8-Cinco%20bilh%C3%B5es%20de%20d%C3%B3lares%20perdidos%20por%20um%20update%20na%20nuvem.pdf) | 9 | Revisão, tagueamento, case CrowdStrike (19/07/2024), ISO 27017 |

## Projeto de referência (Unidades 3 a 8)

Da Unidade 3 em diante, tudo gira em torno de um **sistema web de liberação de crédito**. No Azure, os recursos se chamam `LiberacaoCredito`, `LiberacaoCredito2` e `LiberacaoCredito3`.

- **Fluxo** (diagrama na Unidade 3, p. 4): inserir dados do cliente → processar crédito → se aprovado, enviar dados ao **Sistema X** e gerar contrato; se não, registrar no histórico e avisar o cliente.
- **Arquitetura base** (Unidade 3, p. 5): cliente e atendente acessam a página web. Ela é servida por uma VM Linux de front-end, que fala com uma VM Linux de back-end. O back-end consulta o banco e o Sistema X, que é externo. O diagrama desenha o banco como "SQL Data Warehouse", mas o texto fala em três VMs, sendo a terceira a do banco.
- **Regras de negócio do exercício** (Unidade 3, pp. 28–29; respostas nas pp. 30–31): 30 atendentes com 20 clientes/dia cada (pico de 40), análise de crédito assíncrona, 3 sistemas externos consultando por API (100 requisições/dia cada), sem redundância mas sem deixar todos os atendentes parados, e o Sistema X em servidores locais no Brasil.
- **Evolução:**
  - Unidade 4: o projeto é implantado no Azure.
  - Unidade 6: o gateway com WAF é posto na frente do app web (Node.js e HTML).
  - Unidade 7: `LiberacaoCredito3` é criado só para demonstrar redundância, e o app é escalado horizontalmente.
  - Unidade 8: o exercício final pergunta o que fazer se o gateway falhar.

## Pontos de atenção no material

- **"Login" na Unidade 6:** o título fala em login, mas o PDF só cobre WAF e gateway. Autenticação (SSO, IAM) aparece apenas como pergunta de levantamento na Unidade 3. A videoaula da Unidade 6 tem o mesmo título da Unidade 7 e pede anotações sobre redundância, balanceadores, resiliência, mensageria e alta disponibilidade, temas que o PDF só desenvolve na Unidade 7.
- **Promessas não cumpridas:** a Unidade 1 diz que CaaS será visto depois, e nenhuma unidade volta a ele. FaaS só reaparece na prática, como Aplicativo de Funções (Unidade 4). A Unidade 8 chama o tagueamento de "parte fundamental do gerenciamento", mas o conteúdo dele está só na videoaula.
- **Números do material** (cite a unidade ao usá-los):
  - Unidade 3: a VM B1s custa quase o dobro na região Brazil South em relação à West US 2. A B2as_v2 custa US$ 54,90/mês.
  - Unidade 3: os tamanhos que entram no gratuito são Standard_B1s e Standard_B2ats_v2, marcados como "serviços gratuitos qualificados".
  - Unidades 4 e 6: o Aplicativo Web, o gateway, o WAF e os IPs desses recursos não são gratuitos.
  - Unidade 8: as empresas afetadas pela CrowdStrike tiveram US$ 5 bilhões de prejuízo, e a própria CrowdStrike perdeu US$ 2 bilhões em ações num só dia.
