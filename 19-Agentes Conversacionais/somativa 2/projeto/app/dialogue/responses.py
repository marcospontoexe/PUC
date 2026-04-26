"""Templates de respostas dinâmicas do AtendeBot."""

from datetime import datetime

MESES_PT = {
    1: "janeiro", 2: "fevereiro", 3: "março", 4: "abril",
    5: "maio", 6: "junho", 7: "julho", 8: "agosto",
    9: "setembro", 10: "outubro", 11: "novembro", 12: "dezembro",
}

STATUS_PT = {
    "pago": "✅ Pago",
    "pendente": "⏳ Pendente",
    "atrasado": "🔴 Atrasado",
}

TIPO_SERVICO_PT = {
    "internet": "Internet",
    "celular": "Celular/Telefonia Móvel",
    "tv": "TV por Assinatura",
    "combo": "Combo",
}

TIPO_PROBLEMA_PT = {
    "lentidao": "Lentidão na conexão",
    "queda": "Queda/Instabilidade",
    "sem_sinal": "Sem sinal/Sem funcionamento",
}


def resposta_planos(nome_cliente: str, planos: list[dict]) -> str:
    if not planos:
        return (
            f"{nome_cliente}, não encontrei planos ativos no seu cadastro. "
            "Deseja contratar um novo plano?"
        )

    linhas = [f"📋 **{nome_cliente}**, aqui estão seus planos ativos:\n"]
    for i, p in enumerate(planos, 1):
        tipo = TIPO_SERVICO_PT.get(p["tipo"], p["tipo"])
        linhas.append(f"**{i}. {p['nome']}** ({tipo})")
        if p.get("velocidade"):
            linhas.append(f"   Velocidade: {p['velocidade']}")
        if p.get("franquia_dados"):
            linhas.append(f"   Franquia de dados: {p['franquia_dados']}")
        linhas.append(f"   {p['descricao']}")
        linhas.append(f"   💰 Valor: R$ {p['preco']:.2f}/mês")
        linhas.append(f"   Contratado em: {p['data_inicio']}")
        linhas.append("")

    linhas.append("Posso ajudar com mais alguma coisa?")
    return "\n".join(linhas)


def resposta_faturas(nome_cliente: str, faturas: list[dict]) -> str:
    if not faturas:
        return (
            f"{nome_cliente}, não encontrei faturas no seu cadastro. "
            "Pode ser que ainda não haja fatura gerada para o período."
        )

    linhas = [f"💳 **{nome_cliente}**, aqui estão suas faturas:\n"]
    for f in faturas:
        mes_nome = MESES_PT.get(f["mes_referencia"], str(f["mes_referencia"]))
        status = STATUS_PT.get(f["status"], f["status"])
        venc = datetime.strptime(f["vencimento"], "%Y-%m-%d").strftime("%d/%m/%Y")

        linhas.append(f"• **{f['plano_nome']}** — {mes_nome}/{f['ano_referencia']}")
        linhas.append(f"  Valor: R$ {f['valor']:.2f} | Vencimento: {venc} | Status: {status}")

    linhas.append("\nPrecisa de mais alguma informação sobre suas faturas?")
    return "\n".join(linhas)


def resposta_segunda_via(dados_boleto: dict) -> str:
    return (
        f"🔗 Pronto! Gerei uma nova via do seu boleto:\n\n"
        f"**Link para pagamento:** {dados_boleto['link']}\n"
        f"**Código de barras:** `{dados_boleto['codigo_barras']}`\n"
        f"**Válido até:** {dados_boleto['validade']}\n\n"
        f"O boleto também foi enviado para seu e-mail cadastrado. "
        f"Posso ajudar com mais alguma coisa?"
    )


def resposta_chamado_criado(dados_chamado: dict, tipo_servico: str, tipo_problema: str) -> str:
    servico = TIPO_SERVICO_PT.get(tipo_servico, tipo_servico)
    problema = TIPO_PROBLEMA_PT.get(tipo_problema, tipo_problema)

    return (
        f"🔧 Chamado técnico registrado com sucesso!\n\n"
        f"**Protocolo:** {dados_chamado['protocolo']}\n"
        f"**Serviço:** {servico}\n"
        f"**Problema:** {problema}\n"
        f"**Aberto em:** {dados_chamado['data_abertura']}\n"
        f"**Previsão de resolução:** {dados_chamado['previsao_resolucao']}\n\n"
        f"Guarde o número do protocolo para acompanhamento. "
        f"Nossa equipe técnica entrará em contato caso seja necessário "
        f"agendar uma visita. Posso ajudar com mais alguma coisa?"
    )


def resposta_upgrade(planos_disponiveis: list[dict], tipo_filtro: str | None = None) -> str:
    if not planos_disponiveis:
        return "No momento não encontrei planos disponíveis para essa categoria. Deseja ver outras opções?"

    linhas = ["📦 Aqui estão os planos disponíveis:\n"]

    tipo_atual = None
    for p in planos_disponiveis:
        tipo = TIPO_SERVICO_PT.get(p["tipo"], p["tipo"])
        if tipo != tipo_atual:
            tipo_atual = tipo
            linhas.append(f"\n**{tipo}:**")

        linhas.append(f"  • **{p['nome']}** — R$ {p['preco']:.2f}/mês")
        if p.get("velocidade"):
            linhas.append(f"    {p['velocidade']}")
        if p.get("franquia_dados"):
            linhas.append(f"    {p['franquia_dados']} de dados")
        linhas.append(f"    {p['descricao']}")

    linhas.append(
        "\nGostou de algum plano? Me diga o nome do plano que deseja "
        "e eu faço a alteração para você!"
    )
    return "\n".join(linhas)


def resposta_upgrade_confirmado(plano_nome: str) -> str:
    return (
        f"✅ Seu plano foi alterado para **{plano_nome}** com sucesso!\n\n"
        f"A mudança será efetivada em até 24 horas. Você receberá uma "
        f"confirmação por e-mail e SMS. O novo valor será cobrado na "
        f"próxima fatura. Posso ajudar com mais alguma coisa?"
    )


def resposta_problema_pedir_detalhes(tipo_detectado: str | None = None) -> str:
    if tipo_detectado:
        servico = TIPO_SERVICO_PT.get(tipo_detectado, tipo_detectado)
        return (
            f"Entendo que você está com problema em **{servico}**. "
            f"Pode me descrever melhor o que está acontecendo? "
            f"Por exemplo: está sem sinal, lento ou caindo?"
        )
    return (
        "Sinto muito pelo transtorno! Para abrir um chamado técnico, "
        "preciso de algumas informações:\n\n"
        "1. Qual serviço está com problema? (Internet, Celular ou TV)\n"
        "2. O que está acontecendo? (sem sinal, lento, caindo, etc.)"
    )
