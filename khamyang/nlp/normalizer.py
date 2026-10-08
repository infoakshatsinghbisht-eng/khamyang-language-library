"""
Tai Khamyang NLP Normalizer
Provides Unicode normalization, script unification, and tone mark standardization.
"""

import unicodedata
import re


SUPERSCRIPT_TONE_MAP = {
    "¹": "1",
    "²": "2",
    "³": "3",
    "⁴": "4",
    "⁵": "5",
    "⁶": "6",
}

DIGIT_TO_SUPERSCRIPT = {v: k for k, v in SUPERSCRIPT_TONE_MAP.items()}


def normalize_unicode(text: str) -> str:
    """Performs Unicode NFC normalization and strips invisible formatting artifacts."""
    if not text:
        return ""
    # NFC normalization
    norm = unicodedata.normalize("NFC", text)
    # Remove zero-width spaces, zero-width non-joiners unless necessary
    norm = norm.replace("\u200b", "").replace("\ufeff", "")
    # Normalize multiple whitespace
    norm = re.sub(r"[ \t]+", " ", norm)
    return norm.strip()


def normalize_roman_tones(text: str) -> str:
    """Converts superscript tone numbers (¹..⁶) to standard trailing ASCII digits (1..6)."""
    norm = normalize_unicode(text)
    for sup, dig in SUPERSCRIPT_TONE_MAP.items():
        norm = norm.replace(sup, dig)
    return norm


def normalize_assamese_tones(text: str) -> str:
    """Ensures Assamese script representations use consistent superscript tone numbers."""
    norm = normalize_unicode(text)
    # Replace trailing ASCII digits after Assamese characters with superscripts
    pattern = r"([\u0980-\u09FF])([1-6])"
    return re.sub(pattern, lambda m: m.group(1) + DIGIT_TO_SUPERSCRIPT.get(m.group(2), m.group(2)), norm)


def normalize(text: str) -> str:
    """Master normalization function across all scripts."""
    return normalize_roman_tones(text)
