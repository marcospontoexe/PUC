"""Testes automatizados para o AtendeBot."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app.nlp.preprocessor import preprocess, remove_accents
from app.nlp.entity_extractor import (
    extract_cpf,
    extract_tipo_problema,
    extract_tipo_servico,
    validate_cpf,
)
from app.nlp.intent_classifier import IntentClassifier
from app.database.db import init_db, buscar_cliente_por_cpf
from app.dialogue.manager import DialogueManager, State


class TestPreprocessor(unittest.TestCase):
    def test_remove_accents(self):
        self.assertEqual(remove_accents("ação"), "acao")
        self.assertEqual(remove_accents("não"), "nao")
        self.assertEqual(remove_accents("você"), "voce")

    def test_preprocess_lowercase(self):
        result = preprocess("QUAL MEU PLANO", use_stemming=False)
        self.assertEqual(result, result.lower())

    def test_preprocess_removes_punctuation(self):
        result = preprocess("olá, tudo bem?", use_stemming=False)
        self.assertNotIn(",", result)
        self.assertNotIn("?", result)


class TestEntityExtractor(unittest.TestCase):
    def test_extract_cpf_formatted(self):
        self.assertEqual(extract_cpf("Meu CPF é 123.456.789-01"), "12345678901")

    def test_extract_cpf_unformatted(self):
        self.assertEqual(extract_cpf("12345678901"), "12345678901")

    def test_extract_cpf_none(self):
        self.assertIsNone(extract_cpf("olá bom dia"))

    def test_validate_cpf_valid(self):
        self.assertTrue(validate_cpf("12345678901"))

    def test_validate_cpf_all_same(self):
        self.assertFalse(validate_cpf("11111111111"))

    def test_extract_tipo_servico(self):
        self.assertEqual(extract_tipo_servico("minha internet caiu"), "internet")
        self.assertEqual(extract_tipo_servico("celular sem sinal"), "celular")
        self.assertEqual(extract_tipo_servico("tv fora do ar"), "tv")
        self.assertEqual(extract_tipo_servico("wifi lento"), "internet")

    def test_extract_tipo_problema(self):
        self.assertEqual(extract_tipo_problema("internet lenta"), "lentidao")
        self.assertEqual(extract_tipo_problema("sinal caindo"), "queda")
        self.assertEqual(extract_tipo_problema("sem sinal"), "sem_sinal")


class TestIntentClassifier(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.classifier = IntentClassifier()

    def test_saudacao(self):
        intent, score = self.classifier.classify("oi bom dia")
        self.assertEqual(intent, "saudacao")
        self.assertGreater(score, 0.3)

    def test_consultar_plano(self):
        intent, _ = self.classifier.classify("qual é o meu plano atual")
        self.assertEqual(intent, "consultar_plano")

    def test_consultar_fatura(self):
        intent, _ = self.classifier.classify("quanto é minha fatura")
        self.assertEqual(intent, "consultar_fatura")

    def test_problema_tecnico(self):
        intent, _ = self.classifier.classify("minha internet parou de funcionar")
        self.assertEqual(intent, "problema_tecnico")

    def test_despedida(self):
        intent, _ = self.classifier.classify("tchau obrigado")
        self.assertIn(intent, ["despedida", "agradecimento"])

    def test_nao_compreendido(self):
        intent, score = self.classifier.classify("xyzabc123")
        self.assertEqual(intent, "nao_compreendido")


class TestDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        init_db()

    def test_buscar_cliente_existente(self):
        cliente = buscar_cliente_por_cpf("12345678901")
        self.assertIsNotNone(cliente)
        self.assertEqual(cliente["nome"], "Maria Silva")

    def test_buscar_cliente_inexistente(self):
        cliente = buscar_cliente_por_cpf("00000000000")
        self.assertIsNone(cliente)


class TestDialogueManager(unittest.TestCase):
    def setUp(self):
        init_db()
        self.dm = DialogueManager()

    def test_inicio_saudacao(self):
        resp = self.dm.process_message("olá")
        self.assertEqual(self.dm.state, State.AGUARDANDO_CPF)
        self.assertIn("CPF", resp)

    def test_identificacao_cliente(self):
        self.dm.process_message("oi")
        resp = self.dm.process_message("12345678901")
        self.assertEqual(self.dm.state, State.IDENTIFICADO)
        self.assertIn("Maria", resp)

    def test_cpf_invalido_repetido(self):
        self.dm.process_message("oi")
        self.dm.process_message("abc")
        self.dm.process_message("abc")
        resp = self.dm.process_message("abc")
        self.assertIn("atendente", resp.lower())

    def test_consultar_plano_apos_identificacao(self):
        self.dm.process_message("oi")
        self.dm.process_message("12345678901")
        resp = self.dm.process_message("qual meu plano")
        self.assertIn("plano", resp.lower())

    def test_consultar_fatura(self):
        self.dm.process_message("oi")
        self.dm.process_message("12345678901")
        resp = self.dm.process_message("quero ver minha fatura")
        self.assertIn("fatura", resp.lower())

    def test_fluxo_problema_tecnico_completo(self):
        self.dm.process_message("oi")
        self.dm.process_message("12345678901")
        resp = self.dm.process_message("minha internet está lenta")
        self.assertIn("protocolo", resp.lower())


if __name__ == "__main__":
    unittest.main()
