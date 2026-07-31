# -*- coding: utf-8 -*-
"""
Conteudo textual do relatorio da disciplina "IA na Gestao de Negocios" (PUCPR).

O texto fica separado do gerador (gerar_relatorio.py) para que revisoes de
conteudo nao exijam mexer na logica de formatacao ABNT.

Formato dos blocos: cada elemento de BLOCOS e uma tupla (tipo, dado).
    ("t1",  texto)   -> titulo de secao primaria   (ex.: "1 INTRODUCAO")
    ("t2",  texto)   -> titulo de secao secundaria (ex.: "1.1 Enquadramento")
    ("t3",  texto)   -> titulo de secao terciaria
    ("p",   texto)   -> paragrafo de corpo de texto
    ("cit", texto)   -> citacao longa (recuo 4 cm, fonte 10, entrelinhas simples)
    ("quadro", dict) -> quadro/tabela com titulo acima e fonte abaixo
    ("figura", dict) -> figura com legenda acima e fonte abaixo

Marcacao inline aceita nos textos de "p" e "cit":
    **negrito**   e   _italico_
Nao ha suporte a aninhamento (nao usar italico dentro de negrito).
A marcacao nao e aplicada nas celulas dos quadros, que contem nomes de campos
com underline.
"""

# ---------------------------------------------------------------------------
# Metadados da capa
# ---------------------------------------------------------------------------
INSTITUICAO = "PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ"
CURSO = "Bacharelado em Ciência da Computação"
DISCIPLINA = "IA na Gestão de Negócios"
AUTOR = "Marcos Daniel Santana"
LOCAL_ANO = "Curitiba\n2026"

TITULO = (
    "INTELIGÊNCIA ARTIFICIAL APLICADA À OTIMIZAÇÃO DA SEPARAÇÃO DE PEDIDOS "
    "(ORDER PICKING) EM CENTROS DE DISTRIBUIÇÃO: PROPOSTA DE ABORDAGEM COM "
    "META-HEURÍSTICAS BIOINSPIRADAS E APRENDIZADO DE MÁQUINA"
)

FONTE_AUTOR = "Fonte: o autor (2026)."

# ---------------------------------------------------------------------------
# Corpo do relatorio
# ---------------------------------------------------------------------------
BLOCOS = [

    # =======================================================================
    # SECAO 1 - INTRODUCAO
    # =======================================================================
    ("t1", "1 INTRODUÇÃO"),

    ("p",
     "A consolidação do comércio eletrônico e das estratégias omnichannel converteu o prazo de "
     "entrega em atributo competitivo central: o consumidor que não encontra o produto disponível "
     "migra para o concorrente a um custo de troca praticamente nulo. A cadeia de suprimentos "
     "passa a operar com respostas mais rápidas e entregas mais frequentes, na lógica do "
     "_Just-in-Time_. Nesse cenário, o Centro de Distribuição (CD) deixou de ser um depósito para "
     "se tornar o principal ativo de nível de serviço da rede. Sua missão é dupla e internamente "
     "contraditória: amortecer a variação entre a programação dos fornecedores e a demanda real "
     "das lojas e, ao mesmo tempo, repor os pontos de venda sem gerar ruptura nem superestocagem. "
     "Para cumpri-la, executa quatro atividades básicas — recebimento, estocagem, separação e "
     "expedição —, além de acessórias como _packing_ e _cross-docking_."),

    ("p",
     "Dentre elas, a separação de pedidos, ou _order picking_, é a mais crítica economicamente. De "
     "Koster, Le-Duc e Roodbergen (2007) estimam que responda por até 55% da despesa operacional "
     "de um armazém, e que a maior parcela desse custo seja consumida pelo deslocamento do "
     "separador entre os endereços de coleta — tempo que não agrega valor algum ao produto. "
     "Reduzir a distância percorrida é, portanto, a alavanca mais direta de que o gestor logístico "
     "dispõe para melhorar simultaneamente custo e nível de serviço."),

    ("p",
     "O problema tratado neste relatório é exatamente esse. As decisões que determinam a distância "
     "percorrida — em que endereço armazenar cada item, como agrupar pedidos em lotes, em que "
     "sequência visitar os endereços e qual operador executa cada tarefa — são tomadas, na maior "
     "parte das operações brasileiras de porte médio, por regras estáticas embutidas no sistema de "
     "gerenciamento de armazém (WMS). São regras que desconsideram a sazonalidade da demanda, a "
     "afinidade entre produtos comprados em conjunto e o congestionamento gerado por dezenas de "
     "tarefas simultâneas nos mesmos corredores. O resultado é uma operação que consome mais mão "
     "de obra, equipamento e tempo do que o necessário para entregar o mesmo nível de serviço."),

    ("p",
     "Os pontos de negócio abordados são: **(i)** o custo operacional por linha separada; "
     "**(ii)** a produtividade da mão de obra; **(iii)** o cumprimento da janela de corte para "
     "expedição; **(iv)** o nível de serviço às lojas, aferido pela ausência de ruptura; **(v)** o "
     "congestionamento interno; e **(vi)** a decisão entre otimizar o processo existente e "
     "adquirir tecnologia de automação."),

    ("t2", "1.1 Enquadramento do setor de mercado"),

    ("p",
     "O problema é característico do varejo e da distribuição atacadista, mas manifesta-se com "
     "igual intensidade em comércio eletrônico puro, operadores logísticos terceirizados (3PL), "
     "distribuição farmacêutica e autopeças. O denominador comum é a combinação de elevado número "
     "de SKUs ativos, alta frequência de pedidos com poucas linhas cada e janelas de expedição "
     "rígidas — condições que, coexistindo, tornam o deslocamento o gargalo dominante."),

    ("p",
     "Para conferir concretude à proposta, adota-se como objeto uma empresa fictícia, porém "
     "dimensionada de forma representativa do porte médio brasileiro: a **Rede Vetor Varejo S.A.**, "
     "rede varejista omnichannel que opera um CD central próprio. O Quadro 1 sintetiza a operação, "
     "cujos parâmetros serão retomados ao longo do relatório."),

    ("quadro", {
        "numero": 1,
        "titulo": "Caracterização do centro de distribuição objeto da proposta",
        "cabecalho": ["Parâmetro", "Valor"],
        "linhas": [
            ["Área útil de armazenagem", "14.000 m²"],
            ["Número de ruas (corredores)", "42"],
            ["Estrutura vertical", "3 níveis de picking + 4 níveis de armazenagem aérea"],
            ["SKUs ativos", "22.000"],
            ["Lojas atendidas", "120 lojas em 6 estados"],
            ["Pedidos por dia", "3.200 (2.100 de reposição de lojas + 1.100 de e-commerce)"],
            ["Linhas por pedido (média)", "18,0 (lojas) / 3,2 (e-commerce)"],
            ["Linhas de separação por dia", "aproximadamente 46.000"],
            ["Separadores por turno", "68, em 3 turnos"],
            ["Equipamentos de movimentação", "34 transpaleteiras, 12 empilhadeiras, 9 selecionadoras de pedidos"],
            ["Sistema de gestão", "WMS comercial integrado ao ERP corporativo"],
        ],
        "larguras": [5.0, 10.0],
    }),

    ("p",
     "A convivência de dois perfis de separação no mesmo armazém torna o caso especialmente "
     "ilustrativo. A reposição de lojas produz pedidos grandes, previsíveis e majoritariamente em "
     "caixa fechada; o comércio eletrônico, pedidos pequenos, voláteis e em unidade de venda "
     "(_each picking_). Ambos disputam os mesmos corredores, equipamentos e equipe, mas respondem "
     "de forma distinta às técnicas de otimização — o que justifica, na Seção 3, a proposição de "
     "duas abordagens complementares em vez de uma solução única."),

    # =======================================================================
    # SECAO 2 - PROBLEMA E DADOS
    # =======================================================================
    ("t1", "2 DESCRIÇÃO DO PROBLEMA E DADOS ASSOCIADOS"),

    ("t2", "2.1 Decomposição do problema em subproblemas acoplados"),

    ("p",
     "O que se descreve genericamente como “otimização do _picking_” é, na realidade, um conjunto "
     "de quatro problemas de decisão acoplados. Tratá-los como bloco único é a origem de boa parte "
     "das tentativas malsucedidas de melhoria observadas na prática empresarial."),

    ("p",
     "**(1) SLAP — Storage Location Assignment Problem.** Define em qual endereço físico cada SKU "
     "será armazenado. É a decisão de maior alcance, porque estabelece a geografia sobre a qual "
     "todas as demais operam: um item de altíssimo giro alocado no extremo oposto à doca impõe um "
     "custo de deslocamento que se repete em todas as viagens, todos os dias."),

    ("p",
     "**(2) OBP — Order Batching Problem.** Define como agrupar pedidos em lotes de separação. "
     "Separar cada pedido de e-commerce isoladamente significa percorrer o armazém para coletar, "
     "em média, 3,2 itens; agrupar pedidos que compartilham regiões amortiza a mesma viagem entre "
     "vários pedidos."),

    ("p",
     "**(3) PRP — Picker Routing Problem.** Define a sequência de visita aos endereços de um lote; "
     "é o subproblema mais estudado na literatura e o mais diretamente ligado à distância "
     "percorrida. **(4) Designação de tarefas e controle de congestionamento.** Define qual "
     "operador e qual equipamento executam cada tarefa e quando. Como separação, ressuprimento e "
     "armazenagem ocorrem simultaneamente nos mesmos corredores, a má distribuição das tarefas no "
     "tempo produz filas e bloqueios — fenômeno análogo ao congestionamento urbano."),

    ("p",
     "O acoplamento entre eles é o que torna o conjunto difícil: o endereçamento altera a matriz "
     "de distâncias que alimenta a roteirização, a formação de lotes determina quais endereços "
     "serão visitados na mesma viagem e a designação define quantos operadores disputarão o mesmo "
     "corredor. Otimizar cada subproblema isoladamente pode, inclusive, deteriorar o resultado "
     "global. O Quadro 2 apresenta a situação atual de cada um no CD analisado, que constitui a "
     "linha de base contra a qual os ganhos serão medidos."),

    ("quadro", {
        "numero": 2,
        "titulo": "Subproblemas de decisão e situação atual (linha de base)",
        "cabecalho": ["Subproblema", "Decisão envolvida", "Situação atual no CD analisado"],
        "linhas": [
            ["SLAP – Endereçamento", "Em que endereço armazenar cada SKU",
             "Alocação estática por categoria mercadológica, revista uma vez por ano"],
            ["OBP – Formação de lotes", "Como agrupar pedidos em lotes",
             "Agrupamento por ordem de chegada (FIFO) na onda, sem otimização"],
            ["PRP – Roteirização", "Em que sequência visitar os endereços",
             "Heurística S-shape fixa, embutida no WMS"],
            ["Designação de tarefas", "Qual operador executa qual tarefa e quando",
             "Por disponibilidade do operador, sem previsão de congestionamento"],
        ],
        "larguras": [3.6, 4.8, 6.6],
    }),

    ("p",
     "Do ponto de vista computacional, o PRP é uma variante do Problema do Caixeiro Viajante de "
     "Steiner e pertence à classe NP-difícil: um lote com 30 endereços admite, no limite teórico, "
     "30! (cerca de 2,65 × 10³²) sequências possíveis. Somando-se a isso as 46.000 linhas diárias "
     "e a entrada e o cancelamento contínuos de pedidos, conclui-se que a solução precisa ser não "
     "apenas boa, mas obtida em segundos e capaz de se ajustar em tempo real — nicho das "
     "meta-heurísticas e das técnicas de inteligência artificial."),

    ("figura", {
        "numero": 1,
        "titulo": "Representação esquemática do centro de distribuição como grafo de roteirização",
        "arquivo": "fig1_layout_cd.png",
        "largura_cm": 15.0,
    }),

    ("p",
     "A Figura 1 ilustra a modelagem adotada: os vértices são os endereços de _picking_ e a doca de "
     "expedição, e as arestas são os trechos de corredor, ponderados pela distância real. Toda a "
     "proposta consiste, em última análise, em encurtar o percurso destacado — seja escolhendo uma "
     "sequência melhor, seja mudando os endereços que precisam ser visitados."),

    ("t2", "2.2 Dados de entrada necessários"),

    ("p",
     "Os Quadros 3 a 7 descrevem as cinco estruturas de dados necessárias, com campos, tipos e "
     "conteúdos. Duas são tabelas dimensionais — cadastro de produtos e mapa de endereçamento —, "
     "que descrevem o estado do sistema; as demais são tabelas de fatos, que registram o "
     "ocorrido."),

    ("quadro", {
        "numero": 3,
        "titulo": "Cadastro de SKU (dimensão de produto)",
        "cabecalho": ["Campo", "Tipo", "Descrição"],
        "linhas": [
            ["sku_id", "texto (13)", "Código EAN/GTIN"],
            ["descricao", "texto (120)", "Descrição comercial"],
            ["categoria", "texto (40)", "Categoria mercadológica"],
            ["curva_abc", "caractere (1)", "Classificação A, B ou C por giro"],
            ["comprimento_cm, largura_cm, altura_cm", "decimal", "Dimensões da unidade de venda"],
            ["peso_kg", "decimal", "Peso bruto unitário"],
            ["tipo_embalagem", "texto (20)", "Unidade, caixa fechada ou palete"],
            ["giro_medio_dia", "decimal", "Média móvel de 90 dias"],
            ["exige_cuidado", "booleano", "Item frágil, controlado ou de alto valor"],
        ],
        "larguras": [5.2, 2.8, 7.0],
    }),

    ("quadro", {
        "numero": 4,
        "titulo": "Mapa de endereçamento (dimensão de localização)",
        "cabecalho": ["Campo", "Tipo", "Descrição"],
        "linhas": [
            ["endereco_id", "texto (12)", "Formato rua-módulo-nível-posição"],
            ["rua", "inteiro", "Corredor de 1 a 42"],
            ["modulo", "inteiro", "Posição longitudinal na rua"],
            ["nivel", "inteiro", "1 a 3: picking; 4 a 7: aéreo"],
            ["coord_x, coord_y, coord_z", "decimal", "Coordenadas cartesianas (m)"],
            ["tipo", "texto (10)", "picking ou aereo"],
            ["capacidade_un", "inteiro", "Capacidade em unidades"],
            ["sku_alocado", "texto (13)", "SKU alocado (chave estrangeira)"],
        ],
        "larguras": [5.2, 2.8, 7.0],
    }),

    ("quadro", {
        "numero": 5,
        "titulo": "Histórico de linhas de separação (tabela de fatos transacional)",
        "cabecalho": ["Campo", "Tipo", "Descrição"],
        "linhas": [
            ["linha_id", "inteiro", "Identificador da linha"],
            ["pedido_id", "inteiro", "Pedido de origem"],
            ["sku_id, endereco_id", "texto", "Item e endereço de coleta"],
            ["quantidade", "decimal", "Quantidade solicitada"],
            ["data_hora_pedido", "timestamp", "Entrada do pedido no sistema"],
            ["canal", "texto (10)", "loja ou ecommerce"],
            ["destino_id", "texto (8)", "Loja destino ou CEP do consumidor"],
            ["onda_id", "inteiro", "Onda de separação atribuída"],
        ],
        "larguras": [5.2, 2.8, 7.0],
    }),

    ("quadro", {
        "numero": 6,
        "titulo": "Log de tarefas do WMS (tabela de fatos operacional)",
        "cabecalho": ["Campo", "Tipo", "Descrição"],
        "linhas": [
            ["tarefa_id", "inteiro", "Identificador da tarefa"],
            ["operador_id, equipamento_id", "texto", "Executante e equipamento"],
            ["tipo_tarefa", "texto (20)", "separacao, ressuprimento, armazenagem"],
            ["endereco_origem, endereco_destino", "texto (12)", "Início e término"],
            ["ts_inicio, ts_fim", "timestamp", "Marcações do coletor"],
            ["distancia_percorrida_m", "decimal", "Distância medida ou estimada"],
            ["status", "texto (15)", "concluida, cancelada, interrompida"],
        ],
        "larguras": [5.2, 2.8, 7.0],
    }),

    ("quadro", {
        "numero": 7,
        "titulo": "Cadastro de operadores e equipamentos",
        "cabecalho": ["Campo", "Tipo", "Descrição"],
        "linhas": [
            ["operador_id", "texto (8)", "Identificador do separador"],
            ["turno", "texto (10)", "Turno de trabalho"],
            ["nivel_experiencia", "inteiro", "Tempo de casa (variável preditora)"],
            ["equipamento_id, tipo_equipamento", "texto", "Transpaleteira, empilhadeira, selecionadora"],
            ["velocidade_media_m_s", "decimal", "Velocidade média de deslocamento"],
            ["capacidade_kg, capacidade_volume_m3", "decimal", "Limites físicos por viagem"],
            ["disponibilidade", "booleano", "Situação operacional"],
        ],
        "larguras": [5.2, 2.8, 7.0],
    }),

    ("t2", "2.3 Obtenção dos dados, formatos e volumetria"),

    ("p",
     "Todos os dados são gerados nativamente pela operação, o que elimina a coleta primária e "
     "constitui a principal vantagem econômica da proposta: o insumo já existe e está "
     "subutilizado. O mapa de endereçamento, o histórico de linhas e o log de tarefas provêm do "
     "WMS; o cadastro de produtos, do ERP; os dados de operadores, do sistema de gestão de "
     "pessoas. A captura no armazém já ocorre por coletores de radiofrequência, código de barras "
     "e, nos itens de maior valor, etiquetas RFID."),

    ("p",
     "A extração recomendada é uma rotina de ETL noturna, incremental por data de modificação, que "
     "carrega um _data warehouse_ dimensional em esquema estrela — com as tabelas de fatos de "
     "linhas e de tarefas ao centro e as dimensões de produto, localização, tempo e operador ao "
     "redor. O formato CSV atende às cargas iniciais; para o histórico, recomenda-se Parquet "
     "particionado por data. A integração pode usar API REST e, no intercâmbio com fornecedores e "
     "transportadores, o padrão EDI (_Electronic Data Interchange_). Em volumetria, o CD gera "
     "cerca de 46.000 linhas e 30.000 tarefas por dia — 17 e 11 milhões de registros anuais —, e "
     "recomenda-se janela histórica de 24 meses, para capturar dois ciclos sazonais."),

    ("p",
     "O pré-processamento é a etapa mais crítica e a mais subestimada: se os dados de entrada "
     "forem ruins, nenhuma técnica de inteligência artificial produzirá resultado confiável. Os "
     "tratamentos indispensáveis são a remoção de valores atípicos de tempo de tarefa decorrentes "
     "de pausas e incidentes não registrados, por critério de intervalo interquartílico; a "
     "imputação de coordenadas ausentes; a reconciliação entre o endereço registrado na tarefa e o "
     "vigente na data, uma vez que reendereçamentos corrompem análises retroativas ingênuas; e a "
     "normalização de unidades. Essa sequência corresponde às etapas de seleção, pré-processamento "
     "e transformação do processo de KDD (_Knowledge Discovery in Databases_), no qual a mineração "
     "e a otimização representam apenas uma fração do esforço."),

    # =======================================================================
    # SECAO 3 - METODOS DE IA
    # =======================================================================
    ("t1", "3 MÉTODOS DE INTELIGÊNCIA ARTIFICIAL PROPOSTOS"),

    ("p",
     "Propõem-se duas abordagens complementares, ambas apoiadas em técnicas consolidadas de busca "
     "e aprendizado (NORVIG, 2013). A primeira, estritamente prescritiva, atua no ciclo "
     "operacional e responde a “dada a configuração atual do armazém, qual é a melhor forma de "
     "executar a separação de hoje?”. A segunda, preditiva e prescritiva, atua no ciclo tático e "
     "responde a uma pergunta anterior: “qual deveria ser a configuração do armazém para que a "
     "separação de amanhã já nasça mais curta?”."),

    ("t2", "3.1 Abordagem A — meta-heurísticas bioinspiradas para lotes e roteirização"),

    ("t3", "3.1.1 Justificativa da escolha"),

    ("p",
     "As heurísticas construtivas clássicas de roteirização — _S-shape_, _return_, _midpoint_, "
     "_largest gap_ e _combined_ — têm custo computacional desprezível e são adequadas a layouts "
     "de bloco único com armazenagem aleatória, mas degradam em armazéns com múltiplos corredores "
     "transversais e armazenagem orientada por classe, em que a distância obtida pode superar "
     "consideravelmente a da solução ótima. Com 42 ruas e endereçamento por categoria "
     "mercadológica, o CD analisado situa-se justamente nessa faixa."),

    ("p",
     "As meta-heurísticas, ao contrário, exploram o espaço de soluções sem enumerá-lo. A "
     "otimização por colônia de formigas (ACO), formalizada por Dorigo e Stützle (2004), é "
     "particularmente adequada por três razões: "
     "constrói soluções de forma incremental, permitindo interromper a busca a qualquer momento e "
     "ainda dispor de rota válida; mantém memória adaptativa na forma de trilhas de feromônio, de "
     "modo que a qualidade melhora ao longo de execuções sucessivas sobre o mesmo layout; e reage "
     "bem a alterações em tempo real, pois a estrutura de feromônio acumulada dispensa a "
     "reotimização a partir do zero."),

    ("p",
     "Essa adequação é respaldada pela literatura: De Santis _et al._ (2018) propuseram o "
     "algoritmo FW-ACO, que combina Floyd–Warshall com colônia de formigas para minimizar a "
     "distância percorrida em armazéns manuais, obtendo desempenho superior ao das heurísticas "
     "tradicionais, e trabalhos posteriores estenderam a formulação para múltiplos separadores com "
     "consideração explícita do congestionamento. O algoritmo genético (AG), por sua vez, atua na "
     "formação de lotes, para a qual sua representação por cromossomos de atribuição é "
     "naturalmente adequada."),

    ("t3", "3.1.2 Proposta metodológica"),

    ("p",
     "**Etapas 1 e 2 — Grafo, matriz de distâncias e formação de lotes.** O armazém é representado "
     "como grafo não direcionado G(V, E), em que V reúne os endereços de _picking_ ativos e a "
     "doca, e E os trechos de corredor ponderados pela distância real. Aplica-se Floyd–Warshall "
     "para obter a distância mínima entre todos os pares de vértices; por ter complexidade O(n³), "
     "o cálculo roda fora de linha e é refeito apenas quando layout ou endereçamento mudam. Sobre "
     "essa matriz, um algoritmo genético resolve a formação de lotes: o cromossomo é um vetor de "
     "inteiros em que a posição i indica o lote atribuído ao pedido i, e a função de aptidão soma "
     "a distância total estimada às penalidades por violação de capacidade e por descumprimento da "
     "janela de corte. Empregam-se seleção por torneio, _crossover_ uniforme, mutação por "
     "realocação de pedido e elitismo."),

    ("p",
     "**Etapa 3 — Roteirização por colônia de formigas.** Para cada lote, m formigas artificiais "
     "constroem rotas escolhendo o próximo endereço com probabilidade proporcional ao produto "
     "τ^α · η^β, em que τ é a intensidade de feromônio na aresta, η é o inverso da distância e os "
     "expoentes α e β ponderam memória coletiva e visibilidade local. A cada iteração o feromônio "
     "evapora à taxa ρ e é reforçado nas arestas das melhores rotas."),

    ("p",
     "**Etapas 4 e 5 — Congestionamento e reotimização.** A ocupação prevista de cada trecho é "
     "estimada a partir das tarefas já designadas para a mesma janela de tempo; trechos acima de "
     "um limiar recebem penalização dinâmica no feromônio, dispersando os separadores por "
     "corredores distintos. A cada evento relevante — pedido urgente, cancelamento, "
     "indisponibilidade de equipamento — dispara-se nova execução a partir da matriz de feromônio "
     "corrente, garantindo resposta em segundos; ao final da onda, as distâncias reais medidas "
     "pelos coletores realimentam a recalibração de α, β e ρ."),

    ("t2", "3.2 Abordagem B — aprendizado de máquina e endereçamento dinâmico"),

    ("t3", "3.2.1 Justificativa da escolha"),

    ("p",
     "Enquanto a Abordagem A otimiza a rota dado um endereçamento, a Abordagem B ataca a causa a "
     "montante. Se os itens de maior giro estiverem próximos à doca e os frequentemente pedidos em "
     "conjunto estiverem próximos entre si, a rota já nasce curta, e o ganho passa a ser "
     "estrutural e permanente, independentemente da qualidade do roteirizador. Trata-se de "
     "resolver o SLAP, e não o PRP."),

    ("p",
     "O elo entre previsão e endereçamento é direto: a posição ótima de um SKU depende do seu giro "
     "futuro, não do passado. Um item de curva C durante onze meses pode ser de curva A na semana "
     "que antecede uma data comemorativa, e a classificação ABC anual praticada hoje no CD é "
     "incapaz de acompanhar esse fenômeno."),

    ("p",
     "A escolha dos métodos de previsão precisa considerar a heterogeneidade do catálogo: os "
     "22.000 SKUs não se comportam da mesma forma — alguns têm demanda regular, outros são "
     "intermitentes, com longos períodos de demanda nula —, e aplicar um único método a todos é "
     "erro recorrente e causa frequente de baixa acurácia. Syntetos e Boylan (2005) propõem "
     "classificar as séries por duas métricas: o ADI (_Average Inter-Demand Interval_), medida de "
     "intermitência, e o CV² (coeficiente de variação ao quadrado das demandas não nulas), medida "
     "da variabilidade do tamanho. Disso resultam quatro categorias — _smooth_, _erratic_, _lumpy_ "
     "e _slow-moving_ —, cada uma com método de previsão recomendado."),

    ("t3", "3.2.2 Proposta metodológica"),

    ("p",
     "**Etapas 1 e 2 — Classificação do padrão de demanda e previsão.** Calculam-se ADI e CV² de "
     "cada SKU sobre a janela de 24 meses, segmentando o catálogo nos quatro quadrantes — etapa de "
     "baixo custo que, isoladamente, já revela quais itens são inerentemente imprevisíveis e "
     "exigem estoque de segurança em vez de previsão refinada. Às séries _smooth_ e _erratic_ "
     "aplicam-se o alisamento exponencial com correção de tendência e sazonalidade (métodos de "
     "Holt e de Winter) ou modelos ARIMA e SARIMA (MORETTIN, 2018); às séries _lumpy_ e "
     "_slow-moving_, o método de Croston (1972) e sua variante SBA, que corrigem o viés que o "
     "alisamento exponencial "
     "produz em séries com muitos valores nulos. A escolha final é feita por erro acumulado em "
     "janela de validação, e não por preferência a priori."),

    ("p",
     "**Etapa 3 — Curva ABC dinâmica e afinidade entre itens.** A classificação ABC é recalculada "
     "a cada período de sazonalidade com base na demanda **prevista**, e não na realizada. Em "
     "paralelo, aplica-se mineração de regras de associação por FP-Growth sobre o histórico de "
     "pedidos, identificando SKUs frequentemente separados na mesma viagem, e agrupamento por "
     "k-médias sobre giro previsto, volume, peso e frequência de coocorrência, formando famílias "
     "de armazenagem."),

    ("p",
     "**Etapas 4 e 5 — Realocação de endereços e predição do tempo de tarefa.** O reendereçamento "
     "é formulado como problema de designação e resolvido por programação linear inteira (STEIN "
     "_et al._, 2018), minimizando a soma das distâncias esperadas — distância à doca ponderada "
     "pela demanda prevista do SKU alocado —, sujeito a capacidade volumétrica, limite de peso por "
     "nível, compatibilidade de manuseio, proximidade das famílias e um teto de realocações por "
     "ciclo, que garante que o ganho supere o custo físico da movimentação. Por fim, um modelo de "
     "regressão (_Random Forest_ ou _Gradient Boosting_) treinado sobre o log de tarefas prevê o "
     "tempo de execução a partir da distância, do número de linhas, do equipamento, da experiência "
     "do operador e da ocupação do corredor, alimentando o dimensionamento da equipe por onda."),

    ("t2", "3.3 Comparação e integração das abordagens"),

    ("p",
     "O Quadro 8 confronta as duas abordagens segundo critérios relevantes para a decisão de "
     "implantação. A comparação não visa eleger uma vencedora: elas atacam subproblemas diferentes "
     "e operam em horizontes distintos."),

    ("quadro", {
        "numero": 8,
        "titulo": "Comparação entre as abordagens propostas",
        "cabecalho": ["Critério", "Abordagem A (AG + ACO)", "Abordagem B (aprendizado de máquina)"],
        "linhas": [
            ["Subproblema atacado", "OBP e PRP", "SLAP e designação de tarefas"],
            ["Natureza", "Prescritiva (otimização)", "Preditiva e prescritiva"],
            ["Técnicas principais", "Algoritmo genético, colônia de formigas, Floyd–Warshall",
             "Croston/SBA, Holt-Winters, ARIMA, k-médias, FP-Growth, programação inteira"],
            ["Horizonte de decisão", "Operacional (por onda, segundos)", "Tático (sazonal, horas)"],
            ["Dados exigidos", "Endereçamento, pedidos da onda, equipamentos",
             "Histórico de 24 meses de linhas e tarefas"],
            ["Ganho esperado", "Imediato e reversível", "Estrutural e permanente"],
            ["Complexidade de implantação", "Média (integração em tempo real com o WMS)",
             "Alta (governança de dados e movimentação física de estoque)"],
            ["Interpretabilidade", "Baixa (entrega a rota, não a explicação)",
             "Média a alta (curva ABC e regras de associação são auditáveis)"],
        ],
        "larguras": [3.4, 5.3, 6.3],
    }),

    ("figura", {
        "numero": 2,
        "titulo": "Framework integrado das abordagens propostas",
        "arquivo": "fig2_framework.png",
        "largura_cm": 15.5,
    }),

    ("p",
     "Como mostra a Figura 2, as abordagens operam em frequências distintas e se alimentam "
     "mutuamente. A Abordagem B entrega um mapa de endereçamento atualizado, que passa a ser o "
     "insumo da matriz de distâncias consumida pela Abordagem A, executada a cada onda. Os "
     "resultados reais realimentam ambas: tempos e distâncias efetivos recalibram os parâmetros do "
     "ACO e do AG, enquanto a demanda realizada alimenta a próxima rodada de previsão. É um ciclo "
     "fechado de melhoria contínua, não um projeto com data de encerramento."),

    ("p",
     "Essa arquitetura sustenta-se sobre o processo de KDD: a seleção e o pré-processamento "
     "descritos na Seção 2.3 antecedem qualquer técnica; a mineração e a otimização correspondem "
     "às etapas de cada abordagem; e a interpretação dos resultados e sua conversão em decisão "
     "gerencial — objeto da Seção 4 — constituem a etapa final, sem a qual o esforço anterior "
     "permanece exercício técnico sem consequência para o negócio."),

    ("t2", "3.4 Extensão futura: aprendizado por reforço"),

    ("p",
     "Registra-se, como evolução natural, a possibilidade de tratar a designação dinâmica de "
     "tarefas por aprendizado por reforço, usando um simulador de eventos discretos do CD como "
     "ambiente e um agente que aprende, por tentativa e erro simulados, a política que minimiza "
     "espera e congestionamento. A vantagem é antecipar consequências de longo prazo que regras "
     "míopes não capturam; a desvantagem é exigir simulador fiel e maturidade analítica ainda "
     "inexistente na empresa, razão pela qual se recomenda posicioná-la como terceira onda de "
     "evolução."),

    # =======================================================================
    # SECAO 4 - RESULTADOS
    # =======================================================================
    ("t1", "4 RESULTADOS ESPERADOS E ANÁLISE DE IMPACTO"),

    ("t2", "4.1 Indicadores de desempenho propostos"),

    ("p",
     "A definição dos indicadores precede a implantação e é parte dela: não se trata apenas de "
     "medir o resultado ao final, mas de estabelecer a linha de base contra a qual o ganho será "
     "aferido — sem ela, qualquer discussão sobre a eficácia do modelo se reduz a opinião. O "
     "Quadro 9 apresenta os indicadores propostos, com valores atuais e metas estimadas."),

    ("quadro", {
        "numero": 9,
        "titulo": "Indicadores de desempenho: linha de base e metas esperadas",
        "cabecalho": ["Indicador", "Unidade", "Base", "Meta", "Variação"],
        "linhas": [
            ["Distância média percorrida por pedido", "m", "780", "560", "−28%"],
            ["Linhas separadas por hora por operador", "linhas/h", "62", "78", "+26%"],
            ["Tempo de ciclo do pedido (entrada até expedição)", "min", "41", "29", "−29%"],
            ["Tempo improdutivo por congestionamento", "% da jornada", "11,0", "5,0", "−55%"],
            ["Acuracidade de separação", "%", "99,2", "99,6", "+0,4 p.p."],
            ["Custo operacional por linha separada", "R$", "0,84", "0,63", "−25%"],
            ["Pedidos concluídos dentro da janela de corte", "%", "91", "97", "+6 p.p."],
            ["Ruptura em loja por falha de abastecimento do CD", "%", "3,8", "2,1", "−45%"],
        ],
        "larguras": [6.0, 2.4, 2.2, 1.8, 2.6],
    }),

    ("p",
     "Aplicada ao volume do CD, uma redução de 25% no custo por linha representa, sobre 46.000 "
     "linhas diárias, economia da ordem de R$ 9,7 mil por dia, ou cerca de R$ 2,9 milhões por ano "
     "considerados 300 dias úteis — magnitude suficiente para justificar o investimento em "
     "capacitação analítica e integração de sistemas, ainda que nenhum equipamento novo seja "
     "adquirido."),

    ("t2", "4.2 Influência dos indicadores na decisão gerencial"),

    ("p",
     "A leitura conjunta desses indicadores altera a natureza das decisões disponíveis ao gestor. "
     "A mais relevante é **a escolha entre mudar o processo e investir em automação**: é prática "
     "comum responder a um aumento de demanda comprando equipamentos ou ampliando o armazém, mas "
     "se a distância percorrida cai 28% apenas com reendereçamento e roteirização inteligentes, a "
     "mesma estrutura física absorve volume substancialmente maior e o investimento em imobilizado "
     "pode ser adiado. É decisão de elevado impacto financeiro, possível apenas quando o ganho "
     "potencial da otimização está previamente quantificado."),

    ("p",
     "Seguem-se outras três. **O dimensionamento da equipe por onda** deixa de basear-se na média "
     "histórica e passa a apoiar-se na carga prevista pelo modelo de tempo de tarefa, reduzindo "
     "ociosidade nos vales e hora extra nos picos. **A renegociação da janela de corte** torna-se "
     "viável quando o tempo de ciclo cai de 41 para 29 minutos: o horário-limite para pedidos das "
     "lojas pode ser postergado sem comprometer a partida do veículo, e pedidos emitidos mais "
     "tarde incorporam mais informação de venda do dia, reduzindo a ruptura por caminho "
     "independente do da otimização física. Por fim, **o acompanhamento da acurácia da previsão**, "
     "com registro do previsto contra o realizado período a período, é a única forma de arbitrar "
     "objetivamente a disputa entre a recomendação do modelo e o julgamento experiente do gestor — "
     "sem ele, a discussão tende a ser decidida pela hierarquia, e não pela evidência."),

    ("t2", "4.3 Riscos e barreiras à implantação"),

    ("p",
     "A proposta enfrenta quatro riscos, todos com mitigação conhecida. O primeiro é a **qualidade "
     "dos dados**: marcações de tempo imprecisas ou endereçamento desatualizado inviabilizam a "
     "medição da linha de base e o treinamento dos modelos, o que exige auditoria prévia. O "
     "segundo é a **resistência organizacional**: profissionais experientes tendem a confiar no "
     "conhecimento tácito em detrimento de uma recomendação que não explica suas razões, e a "
     "mitigação mais eficaz é o teste comparativo por onda — metade roteirizada pelo modelo, "
     "metade pela regra vigente. O terceiro é o **custo físico do reendereçamento**, contido pelo "
     "limite de movimentações por ciclo. O quarto é a **dependência de calibração** dos parâmetros "
     "do ACO e do AG."),

    ("t2", "4.4 Exemplo de aplicação real: Amazon Robotics"),

    ("p",
     "Um exemplo documentado de aplicação de técnicas correlatas em escala industrial é o caso da "
     "Amazon, publicado por Allgor, Çezik e Chen (2023) no _INFORMS Journal on Applied Analytics_. "
     "Os autores, pesquisadores da própria empresa, descrevem o redesenho do algoritmo de "
     "separação dos centros de distribuição robotizados da companhia."),

    ("p",
     "Nesses armazéns, o modelo tradicional é invertido: em vez de o operador se deslocar até a "
     "mercadoria, prateleiras móveis chamadas _pods_ são transportadas por robôs autônomos até "
     "estações fixas, nas quais os separadores permanecem parados. A decisão crítica passa a ser "
     "outra: dado um conjunto de pedidos, quais unidades retirar de quais _pods_ e em que "
     "sequência trazê-los às estações. Como um mesmo SKU está replicado em dezenas de _pods_ e "
     "cada _pod_ contém dezenas de SKUs, o número de combinações é imenso e a escolha determina "
     "quantas viagens de robô serão necessárias."),

    ("p",
     "O algoritmo anterior tratava a decisão de forma míope, otimizando pedido a pedido. A "
     "reformulação passou a considerar o conjunto de pedidos simultaneamente, maximizando o número "
     "de unidades aproveitadas por viagem de _pod_ — ou seja, converteu um problema local em um "
     "problema de designação global. É a mesma mudança de perspectiva que a Abordagem B propõe ao "
     "acoplar o endereçamento à formação de lotes."),

    ("p",
     "Os resultados são expressivos: a distância percorrida pelos _pods_ caiu 62%, sem impacto "
     "operacional negativo; a frota de robôs foi reduzida em 31%, com economia direta estimada em "
     "cerca de meio bilhão de dólares; e os centros robotizados passaram a operar com área de "
     "armazenagem 29% menor que a dos equivalentes não robotizados. O algoritmo foi implantado em "
     "todos os centros robotizados da empresa."),

    ("p",
     "Dois aspectos merecem destaque por sua transferibilidade. O primeiro é que o ganho não "
     "decorreu da automação física em si — os robôs já estavam instalados —, mas da decisão "
     "algorítmica sobre como utilizá-los, o que reforça o argumento da Seção 4.2: antes de "
     "investir em equipamento, convém avaliar quanto ainda pode ser extraído do ativo existente. "
     "O segundo é o caráter colaborativo: o algoritmo não substituiu o trabalho humano, mas "
     "reorganizou-o para eliminar o deslocamento improdutivo, elevando a produtividade sem "
     "intensificar o esforço do separador — o que endereça a barreira de resistência discutida na "
     "Seção 4.3. O artigo está disponível em "
     "https://pubsonline.informs.org/doi/10.1287/inte.2022.1143 (DOI: 10.1287/inte.2022.1143)."),

    # =======================================================================
    # SECAO 5 - CONSIDERACOES FINAIS
    # =======================================================================
    ("t1", "5 CONSIDERAÇÕES FINAIS"),

    ("p",
     "Este relatório propôs a aplicação de inteligência artificial à otimização da separação de "
     "pedidos em centros de distribuição, decompondo o problema em quatro subproblemas acoplados, "
     "especificando as estruturas de dados necessárias e apresentando duas abordagens "
     "complementares: meta-heurísticas bioinspiradas para o ciclo operacional e aprendizado de "
     "máquina com endereçamento dinâmico para o ciclo tático. Duas conclusões merecem registro. A "
     "primeira é que o insumo necessário já existe — os dados são gerados nativamente pela "
     "operação e estão subutilizados —, o que desloca a barreira de implantação do campo "
     "tecnológico para o da governança de dados. A segunda é que a escolha da técnica deve derivar "
     "das características do problema, e não do prestígio do método: aplicar uma rede neural a uma "
     "série intermitente, ou uma heurística de bloco único a um armazém de 42 ruas, produz "
     "resultado inferior ao de alternativas mais simples e adequadas."),
]

# ---------------------------------------------------------------------------
# Referencias (ABNT, ordem alfabetica)
# ---------------------------------------------------------------------------
REFERENCIAS = [
    "ALLGOR, R. J.; ÇEZIK, T.; CHEN, D. Algorithm for robotic picking in Amazon fulfillment "
    "centers enables humans and robots to work together effectively. **INFORMS Journal on Applied "
    "Analytics**, v. 53, n. 4, p. 266-282, 2023. DOI: 10.1287/inte.2022.1143. Disponível em: "
    "https://pubsonline.informs.org/doi/10.1287/inte.2022.1143. Acesso em: 30 jul. 2026.",

    "CROSTON, J. D. Forecasting and stock control for intermittent demands. **Operational "
    "Research Quarterly**, v. 23, n. 3, p. 289-303, 1972.",

    "DE KOSTER, R.; LE-DUC, T.; ROODBERGEN, K. J. Design and control of warehouse order picking: "
    "a literature review. **European Journal of Operational Research**, v. 182, n. 2, p. 481-501, "
    "2007.",

    "DE SANTIS, R.; MONTANARI, R.; VIGNALI, G.; BOTTANI, E. An adapted ant colony optimization "
    "algorithm for the minimization of the travel distance of pickers in manual warehouses. "
    "**European Journal of Operational Research**, v. 267, n. 1, p. 120-137, 2018.",

    "DORIGO, M.; STÜTZLE, T. **Ant colony optimization**. Cambridge: MIT Press, 2004.",

    "MORETTIN, P. A. **Análise de séries temporais**. São Paulo: Blucher, 2018.",

    "NORVIG, P. **Inteligência artificial**. Rio de Janeiro: LTC, 2013.",

    "STEIN, R. et al. **Modelagem e otimização de sistemas da produção**. Porto Alegre: SAGAH, "
    "2018.",

    "SYNTETOS, A. A.; BOYLAN, J. E. The accuracy of intermittent demand estimates. "
    "**International Journal of Forecasting**, v. 21, n. 2, p. 303-314, 2005.",
]
