"""
Tai Khamyang Natural Language Processing (NLP) Toolkit
Includes Unicode normalization, tokenization, POS tagging, lemmatization, and language identification.
"""

from typing import List, Dict, Any, Union

from khamyang.nlp.normalizer import (
    normalize,
    normalize_unicode,
    normalize_roman_tones,
    normalize_assamese_tones,
    DIGIT_TO_SUPERSCRIPT,
)
from khamyang.nlp.tokenizer import (
    tokenize,
    tokenize_roman,
    tokenize_liktai,
    detokenize,
)
from khamyang.nlp.lemmatizer import (
    KhamyangLemmatizer,
)
from khamyang.nlp.pos_tagger import (
    pos_tag,
)
from khamyang.nlp.language_detector import (
    detect_language,
)


class KhamyangNormalizer:
    """Class interface for Tai Khamyang text normalization."""
    @staticmethod
    def normalize(text: str) -> str:
        return normalize(text)

    @staticmethod
    def to_superscript_tones(text: str) -> str:
        for digit, super_char in DIGIT_TO_SUPERSCRIPT.items():
            text = text.replace(digit, super_char)
        return text


class KhamyangTokenizer:
    """Class interface for multi-script Tai Khamyang tokenization."""
    @staticmethod
    def tokenize(text: str) -> List[str]:
        return tokenize(text)

    @staticmethod
    def detokenize(tokens: List[str]) -> str:
        return detokenize(tokens)


class KhamyangPOSTagger:
    """Class interface for Universal Dependencies part-of-speech tagging."""
    @staticmethod
    def tag(tokens_or_text: Union[str, List[str]]) -> List[Any]:
        return pos_tag(tokens_or_text)


class KhamyangLanguageDetector:
    """Class interface for Tai Khamyang / Assamese / English language detection."""
    @staticmethod
    def detect(text: str) -> Dict[str, Any]:
        return detect_language(text)


__all__ = [
    "normalize",
    "normalize_unicode",
    "normalize_roman_tones",
    "normalize_assamese_tones",
    "tokenize",
    "tokenize_roman",
    "tokenize_liktai",
    "detokenize",
    "KhamyangNormalizer",
    "KhamyangTokenizer",
    "KhamyangPOSTagger",
    "KhamyangLemmatizer",
    "KhamyangLanguageDetector",
    "pos_tag",
    "detect_language",
]
