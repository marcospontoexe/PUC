"""Extrator de entidades baseado em regex e dicionários."""

import re

CPF_PATTERN = re.compile(
    r"(\d{3}[\.\s]?\d{3}[\.\s]?\d{3}[\-\s]?\d{2})"
)

MESES = {
    "janeiro": 1, "fevereiro": 2, "março": 3, "marco": 3,
    "abril": 4, "maio": 5, "junho": 6,
    "julho": 7, "agosto": 8, "setembro": 9,
    "outubro": 10, "novembro": 11, "dezembro": 12,
    "jan": 1, "fev": 2, "mar": 3, "abr": 4,
    "mai": 5, "jun": 6, "jul": 7, "ago": 8,
    "set": 9, "out": 10, "nov": 11, "dez": 12,
}

SERVICOS_MAP = {
    "internet": "internet",
    "net": "internet",
    "wifi": "internet",
    "wi-fi": "internet",
    "wi fi": "internet",
    "fibra": "internet",
    "banda larga": "internet",
    "roteador": "internet",
    "modem": "internet",
    "celular": "celular",
    "cel": "celular",
    "telefone": "celular",
    "móvel": "celular",
    "movel": "celular",
    "linha": "celular",
    "chip": "celular",
    "tv": "tv",
    "televisão": "tv",
    "televisao": "tv",
    "canais": "tv",
    "canal": "tv",
}

PROBLEMAS_MAP = {
    "lenta": "lentidao",
    "lento": "lentidao",
    "devagar": "lentidao",
    "velocidade baixa": "lentidao",
    "caiu": "queda",
    "caindo": "queda",
    "cai": "queda",
    "queda": "queda",
    "instável": "queda",
    "instavel": "queda",
    "oscilando": "queda",
    "sem sinal": "sem_sinal",
    "não funciona": "sem_sinal",
    "nao funciona": "sem_sinal",
    "parou": "sem_sinal",
    "não liga": "sem_sinal",
    "nao liga": "sem_sinal",
    "fora do ar": "sem_sinal",
    "sem conexão": "sem_sinal",
    "sem conexao": "sem_sinal",
}


def extract_cpf(text: str) -> str | None:
    """Extrai CPF do texto e retorna apenas os dígitos."""
    match = CPF_PATTERN.search(text)
    if match:
        cpf_raw = match.group(1)
        digits = re.sub(r"\D", "", cpf_raw)
        if len(digits) == 11:
            return digits
    return None


def validate_cpf(cpf: str) -> bool:
    """Validação simplificada de CPF (verifica formato e dígitos iguais)."""
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    if cpf == cpf[0] * 11:
        return False
    return True


def extract_tipo_servico(text: str) -> str | None:
    text_lower = text.lower()
    for keyword, servico in SERVICOS_MAP.items():
        if keyword in text_lower:
            return servico
    return None


def extract_tipo_problema(text: str) -> str | None:
    text_lower = text.lower()
    for keyword, problema in PROBLEMAS_MAP.items():
        if keyword in text_lower:
            return problema
    return None


def extract_mes(text: str) -> int | None:
    text_lower = text.lower()
    if "mês passado" in text_lower or "mes passado" in text_lower:
        from datetime import datetime, timedelta
        last_month = datetime.now().replace(day=1) - timedelta(days=1)
        return last_month.month

    for nome, num in MESES.items():
        if nome in text_lower:
            return num
    return None


def extract_all(text: str) -> dict:
    """Extrai todas as entidades de uma mensagem."""
    return {
        "cpf": extract_cpf(text),
        "tipo_servico": extract_tipo_servico(text),
        "tipo_problema": extract_tipo_problema(text),
        "mes_referencia": extract_mes(text),
    }
