"""Classificador de intenções baseado em TF-IDF + Similaridade de Cosseno."""

import json
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .preprocessor import preprocess

CONFIDENCE_THRESHOLD = 0.35


class IntentClassifier:
    def __init__(self, training_data_path: str | None = None):
        if training_data_path is None:
            base = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            training_data_path = os.path.join(base, "data", "training_data.json")

        with open(training_data_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.intents_data = data["intents"]
        self.faq_data = data.get("faq", [])

        self._corpus: list[str] = []
        self._labels: list[str] = []

        for intent in self.intents_data:
            tag = intent["tag"]
            for pattern in intent["patterns"]:
                processed = preprocess(pattern)
                self._corpus.append(processed)
                self._labels.append(tag)

        self._vectorizer = TfidfVectorizer()
        self._tfidf_matrix = self._vectorizer.fit_transform(self._corpus)

        self._faq_corpus: list[str] = []
        self._faq_answers: list[str] = []
        for item in self.faq_data:
            self._faq_corpus.append(preprocess(item["question"]))
            self._faq_answers.append(item["answer"])

        if self._faq_corpus:
            self._faq_vectorizer = TfidfVectorizer()
            self._faq_matrix = self._faq_vectorizer.fit_transform(self._faq_corpus)
        else:
            self._faq_vectorizer = None
            self._faq_matrix = None

    def classify(self, text: str) -> tuple[str, float]:
        """Retorna (intent_tag, confidence_score)."""
        processed = preprocess(text)
        if not processed.strip():
            return "nao_compreendido", 0.0

        vec = self._vectorizer.transform([processed])
        similarities = cosine_similarity(vec, self._tfidf_matrix).flatten()

        best_idx = similarities.argmax()
        best_score = float(similarities[best_idx])

        if best_score < CONFIDENCE_THRESHOLD:
            return "nao_compreendido", best_score

        return self._labels[best_idx], best_score

    def search_faq(self, text: str) -> str | None:
        """Busca na base de FAQ por similaridade."""
        if self._faq_vectorizer is None:
            return None

        processed = preprocess(text)
        if not processed.strip():
            return None

        vec = self._faq_vectorizer.transform([processed])
        similarities = cosine_similarity(vec, self._faq_matrix).flatten()

        best_idx = similarities.argmax()
        best_score = float(similarities[best_idx])

        if best_score >= 0.25:
            return self._faq_answers[best_idx]
        return None

    def get_responses(self, tag: str) -> list[str]:
        for intent in self.intents_data:
            if intent["tag"] == tag:
                return intent.get("responses", [])
        return []
