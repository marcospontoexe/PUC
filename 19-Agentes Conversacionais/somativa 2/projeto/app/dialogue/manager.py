"""Gerenciador de diálogo com máquina de estados finita."""

import random
from enum import Enum, auto

from ..database import db
from ..nlp.entity_extractor import (
    extract_all,
    extract_cpf,
    extract_tipo_problema,
    extract_tipo_servico,
    validate_cpf,
)
from ..nlp.intent_classifier import IntentClassifier
from . import responses


class State(Enum):
    INICIO = auto()
    AGUARDANDO_CPF = auto()
    IDENTIFICADO = auto()
    COLETANDO_PROBLEMA_SERVICO = auto()
    COLETANDO_PROBLEMA_DETALHE = auto()
    AGUARDANDO_UPGRADE_ESCOLHA = auto()


class DialogueManager:
    """Gerencia o estado e fluxo da conversa com um cliente."""

    def __init__(self):
        self.classifier = IntentClassifier()
        self.state = State.INICIO
        self.context: dict = {
            "cliente": None,
            "tentativas_cpf": 0,
            "tentativas_fallback": 0,
            "tipo_servico_problema": None,
            "tipo_problema": None,
            "ultimo_intent": None,
        }

    def process_message(self, user_message: str) -> str:
        """Processa a mensagem do usuário e retorna a resposta do agente."""
        user_message = user_message.strip()
        if not user_message:
            return "Não recebi sua mensagem. Pode repetir, por favor?"

        entities = extract_all(user_message)
        intent, confidence = self.classifier.classify(user_message)

        if self.state == State.INICIO:
            return self._handle_inicio(user_message, intent, entities)

        if self.state == State.AGUARDANDO_CPF:
            return self._handle_aguardando_cpf(user_message, entities)

        if self.state == State.COLETANDO_PROBLEMA_SERVICO:
            return self._handle_coletando_servico(user_message, entities)

        if self.state == State.COLETANDO_PROBLEMA_DETALHE:
            return self._handle_coletando_detalhe(user_message, entities)

        if self.state == State.AGUARDANDO_UPGRADE_ESCOLHA:
            return self._handle_upgrade_escolha(user_message, intent)

        return self._handle_identificado(user_message, intent, confidence, entities)

    def _handle_inicio(self, msg: str, intent: str, entities: dict) -> str:
        cpf = entities.get("cpf") or extract_cpf(msg)
        if cpf:
            return self._try_identify(cpf)

        resps = self.classifier.get_responses("saudacao")
        self.state = State.AGUARDANDO_CPF
        if resps:
            return random.choice(resps)
        return (
            "Olá! Bem-vindo à TeleConecta Brasil! Sou o AtendeBot. "
            "Para começar, por favor me informe seu CPF."
        )

    def _handle_aguardando_cpf(self, msg: str, entities: dict) -> str:
        cpf = entities.get("cpf") or extract_cpf(msg)
        if not cpf:
            digits = "".join(c for c in msg if c.isdigit())
            if len(digits) == 11:
                cpf = digits

        if not cpf:
            self.context["tentativas_cpf"] += 1
            if self.context["tentativas_cpf"] >= 3:
                self.state = State.INICIO
                return (
                    "Não consegui identificar seu CPF após algumas tentativas. "
                    "Vou transferir você para um atendente humano que poderá "
                    "ajudá-lo melhor. Aguarde um momento, por favor. 🔄"
                )
            return (
                "Não consegui identificar o CPF. Por favor, digite apenas os "
                "11 números do seu CPF (exemplo: 123.456.789-00)."
            )

        if not validate_cpf(cpf):
            self.context["tentativas_cpf"] += 1
            if self.context["tentativas_cpf"] >= 3:
                self.state = State.INICIO
                return (
                    "O CPF informado não é válido e atingimos o limite de tentativas. "
                    "Vou transferir para um atendente humano. Aguarde, por favor. 🔄"
                )
            return "O CPF informado não parece ser válido. Pode verificar e digitar novamente?"

        return self._try_identify(cpf)

    def _try_identify(self, cpf: str) -> str:
        cliente = db.buscar_cliente_por_cpf(cpf)
        if not cliente:
            self.state = State.INICIO
            return (
                f"Não encontrei um cadastro com o CPF {cpf[:3]}.***.***-{cpf[-2:]}. "
                "Verifique se digitou corretamente ou entre em contato pelo "
                "telefone *456 para atualizar seu cadastro."
            )

        self.context["cliente"] = cliente
        self.context["tentativas_cpf"] = 0
        self.context["tentativas_fallback"] = 0
        self.state = State.IDENTIFICADO

        nome = cliente["nome"].split()[0]
        return (
            f"Olá, **{nome}**! Encontrei seu cadastro. "
            f"Como posso te ajudar hoje?\n\n"
            f"Posso ajudar com:\n"
            f"• 📋 Consultar seu plano\n"
            f"• 💳 Ver suas faturas\n"
            f"• 🔗 Segunda via de boleto\n"
            f"• 🔧 Problemas técnicos\n"
            f"• 📦 Trocar de plano\n"
            f"• ❓ Dúvidas gerais"
        )

    def _handle_identificado(
        self, msg: str, intent: str, confidence: float, entities: dict
    ) -> str:
        cliente = self.context["cliente"]
        nome = cliente["nome"].split()[0]

        if intent == "consultar_plano":
            self.context["tentativas_fallback"] = 0
            planos = db.buscar_planos_cliente(cliente["id"])
            return responses.resposta_planos(nome, planos)

        if intent == "consultar_fatura":
            self.context["tentativas_fallback"] = 0
            mes = entities.get("mes_referencia")
            faturas = db.buscar_faturas_cliente(cliente["id"], mes)
            return responses.resposta_faturas(nome, faturas)

        if intent == "segunda_via":
            self.context["tentativas_fallback"] = 0
            planos = db.buscar_planos_cliente(cliente["id"])
            if planos:
                from ..database.db import get_connection
                conn = get_connection()
                contrato = conn.execute(
                    "SELECT id FROM contratos WHERE cliente_id = ? AND status = 'ativo' LIMIT 1",
                    (cliente["id"],),
                ).fetchone()
                conn.close()
                if contrato:
                    dados = db.gerar_segunda_via(contrato["id"])
                    return responses.resposta_segunda_via(dados)
            return f"{nome}, não encontrei faturas pendentes para gerar segunda via."

        if intent == "problema_tecnico":
            self.context["tentativas_fallback"] = 0
            tipo_servico = entities.get("tipo_servico")
            tipo_problema = entities.get("tipo_problema")

            if tipo_servico and tipo_problema:
                chamado = db.criar_chamado(
                    cliente["id"], tipo_servico, tipo_problema, msg
                )
                return responses.resposta_chamado_criado(chamado, tipo_servico, tipo_problema)

            self.context["tipo_servico_problema"] = tipo_servico
            self.context["tipo_problema"] = tipo_problema

            if not tipo_servico:
                self.state = State.COLETANDO_PROBLEMA_SERVICO
                return responses.resposta_problema_pedir_detalhes()
            else:
                self.state = State.COLETANDO_PROBLEMA_DETALHE
                return responses.resposta_problema_pedir_detalhes(tipo_servico)

        if intent == "upgrade_plano":
            self.context["tentativas_fallback"] = 0
            tipo = entities.get("tipo_servico")
            planos = db.buscar_planos_upgrade(tipo)
            self.state = State.AGUARDANDO_UPGRADE_ESCOLHA
            return responses.resposta_upgrade(planos, tipo)

        if intent == "falar_atendente":
            resps = self.classifier.get_responses("falar_atendente")
            self.state = State.INICIO
            self.context["cliente"] = None
            return random.choice(resps) if resps else (
                "Transferindo para atendente humano. Aguarde, por favor. 🔄"
            )

        if intent in ("faq_cobertura", "faq_cancelamento", "faq_horario"):
            self.context["tentativas_fallback"] = 0
            resps = self.classifier.get_responses(intent)
            return random.choice(resps) if resps else "Não encontrei essa informação."

        if intent == "agradecimento":
            self.context["tentativas_fallback"] = 0
            resps = self.classifier.get_responses("agradecimento")
            return random.choice(resps) if resps else "De nada! Posso ajudar com mais alguma coisa?"

        if intent == "despedida":
            resps = self.classifier.get_responses("despedida")
            self.state = State.INICIO
            self.context["cliente"] = None
            return random.choice(resps) if resps else "Até mais! Obrigado pelo contato."

        if intent == "saudacao":
            return f"Olá, {nome}! Em que posso ajudar?"

        faq_answer = self.classifier.search_faq(msg)
        if faq_answer:
            self.context["tentativas_fallback"] = 0
            return faq_answer

        self.context["tentativas_fallback"] += 1
        if self.context["tentativas_fallback"] >= 2:
            self.context["tentativas_fallback"] = 0
            self.state = State.INICIO
            self.context["cliente"] = None
            return (
                "Parece que não estou conseguindo entender sua solicitação. "
                "Vou transferir você para um atendente humano que poderá "
                "ajudá-lo melhor. Aguarde um momento, por favor. 🔄"
            )

        return (
            f"Desculpe, {nome}, não entendi bem. Pode reformular sua pergunta? "
            f"Lembre-se que posso ajudar com:\n"
            f"• Consulta de plano\n"
            f"• Faturas e boletos\n"
            f"• Problemas técnicos\n"
            f"• Troca de plano\n"
            f"• Dúvidas gerais"
        )

    def _handle_coletando_servico(self, msg: str, entities: dict) -> str:
        tipo_servico = entities.get("tipo_servico") or extract_tipo_servico(msg)

        if not tipo_servico:
            return (
                "Não identifiquei o serviço. Por favor, me diga se o problema "
                "é com **Internet**, **Celular** ou **TV**."
            )

        self.context["tipo_servico_problema"] = tipo_servico
        tipo_problema = entities.get("tipo_problema") or extract_tipo_problema(msg)

        if tipo_problema:
            self.state = State.IDENTIFICADO
            cliente = self.context["cliente"]
            chamado = db.criar_chamado(
                cliente["id"], tipo_servico, tipo_problema, msg
            )
            return responses.resposta_chamado_criado(chamado, tipo_servico, tipo_problema)

        self.state = State.COLETANDO_PROBLEMA_DETALHE
        return responses.resposta_problema_pedir_detalhes(tipo_servico)

    def _handle_coletando_detalhe(self, msg: str, entities: dict) -> str:
        tipo_problema = entities.get("tipo_problema") or extract_tipo_problema(msg)

        if not tipo_problema:
            tipo_problema = "sem_sinal"

        tipo_servico = self.context.get("tipo_servico_problema", "internet")
        self.state = State.IDENTIFICADO

        cliente = self.context["cliente"]
        chamado = db.criar_chamado(
            cliente["id"], tipo_servico, tipo_problema, msg
        )
        return responses.resposta_chamado_criado(chamado, tipo_servico, tipo_problema)

    def _handle_upgrade_escolha(self, msg: str, intent: str) -> str:
        msg_lower = msg.lower()

        if intent == "despedida" or any(w in msg_lower for w in ["não", "nao", "cancelar", "voltar", "deixa"]):
            self.state = State.IDENTIFICADO
            return "Tudo bem! Se mudar de ideia, é só falar. Posso ajudar com mais alguma coisa?"

        planos = db.buscar_planos_upgrade()
        for p in planos:
            if p["nome"].lower() in msg_lower:
                self.state = State.IDENTIFICADO
                return responses.resposta_upgrade_confirmado(p["nome"])

        if any(w in msg_lower for w in ["sim", "quero", "pode", "aceito", "ok"]):
            return "Ótimo! Qual plano você gostaria? Me diga o nome do plano desejado."

        self.state = State.IDENTIFICADO
        return (
            "Não identifiquei o plano escolhido. Se quiser ver as opções "
            "novamente, é só pedir. Posso ajudar com outra coisa?"
        )
