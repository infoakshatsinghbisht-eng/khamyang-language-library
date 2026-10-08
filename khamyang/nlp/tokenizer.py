"""
Tai Khamyang Tokenizer
Tokenizes Romanized, Lik Tai, and Assamese sentences into constituent words and morphemes.
"""

import re
from typing import List
from khamyang.nlp.normalizer import normalize_roman_tones


def tokenize_roman(text: str) -> List[str]:
    """
    Tokenizes Romanized Tai Khamyang text, preserving tone numbers (1-6) attached to syllables.
    Example: "pu5 yaa3 haw1, khao5 maa1!" -> ["pu5", "yaa3", "haw1", ",", "khao5", "maa1", "!"]
    """
    norm = normalize_roman_tones(text)
    # Match words with optional attached tone digits, or punctuation
    tokens = re.findall(r"[A-Za-z\u0250-\u02AF]+[1-6]?|[0-9]+|[^\w\s]", norm)
    return tokens


def tokenize_liktai(text: str) -> List[str]:
    """
    Tokenizes Lik Tai text (Unicode Myanmar/Shan blocks U+1000..U+109F, U+AA60..U+AA7F).
    Splits by whitespace, Shan punctuation (U+104A, U+104B), or syllable boundaries.
    """
    tokens = []
    # If text has spaces or danda punctuation, split by that first
    chunks = re.findall(r"[\u1000-\u109F\uAA60-\uAA7F]+|[၊။]|[\.,!?;:]|\S", text)
    return chunks


def tokenize(text: str) -> List[str]:
    """
    General tokenizer detecting script and returning token list.
    """
    if not text:
        return []
    # If contains Myanmar script
    if re.search(r"[\u1000-\u109F\uAA60-\uAA7F]", text):
        return tokenize_liktai(text)
    # Default Romanized or Assamese
    return tokenize_roman(text)


def detokenize(tokens: List[str]) -> str:
    """Reconstructs a sentence string from a token list with proper punctuation spacing."""
    if not tokens:
        return ""
    result = []
    for i, tok in enumerate(tokens):
        if tok in [".", ",", "!", "?", ";", ":", "၊", "။"]:
            if result:
                result[-1] = result[-1] + tok
            else:
                result.append(tok)
        else:
            result.append(tok)
    return " ".join(result)
