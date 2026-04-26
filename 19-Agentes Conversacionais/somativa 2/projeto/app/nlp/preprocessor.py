"""Módulo de pré-processamento de texto para o AtendeBot."""

import re
import string
import unicodedata

import nltk
from nltk.corpus import stopwords
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

for _pkg in ("punkt", "punkt_tab", "stopwords", "rslp"):
    try:
        nltk.data.find(f"tokenizers/{_pkg}" if "punkt" in _pkg else f"stemmers/{_pkg}" if _pkg == "rslp" else f"corpora/{_pkg}")
    except LookupError:
        nltk.download(_pkg, quiet=True)

_stemmer = RSLPStemmer()
_stopwords_pt = set(stopwords.words("portuguese"))

# Palavras que NÃO devem ser removidas como stopwords no contexto de SAC
_keep_words = {
    "não", "nao", "sem", "mais", "menos", "quando", "como",
    "qual", "quero", "preciso", "meu", "minha",
}
_effective_stopwords = _stopwords_pt - _keep_words


def remove_accents(text: str) -> str:
    nfkd = unicodedata.normalize("NFKD", text)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def preprocess(text: str, use_stemming: bool = True) -> str:
    """Pipeline completo de pré-processamento."""
    text = text.lower().strip()
    text = remove_accents(text)
    text = re.sub(r"[{}]".format(re.escape(string.punctuation)), " ", text)
    text = re.sub(r"\d+", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    tokens = word_tokenize(text, language="portuguese")
    tokens = [t for t in tokens if t not in _effective_stopwords and len(t) > 1]

    if use_stemming:
        tokens = [_stemmer.stem(t) for t in tokens]

    return " ".join(tokens)


def tokenize_simple(text: str) -> list[str]:
    """Tokenização simples sem stemming, para extração de entidades."""
    text = text.lower().strip()
    return word_tokenize(text, language="portuguese")
