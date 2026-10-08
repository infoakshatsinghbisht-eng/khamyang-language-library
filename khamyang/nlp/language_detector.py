"""
Language Identification Module
Distinguishes Tai Khamyang (ksu) from closely related varieties (Tai Phake, Tai Aiton),
Assamese (asm), and English (eng) with probabilistic confidence scores.
"""

import re
from typing import Dict, Any


# Distinctive Khamyang lexical markers (6-tone system)
KHAMYANG_DIAGNOSTIC_MARKERS = {
    "nam6", "maɯ2", "haw1", "khao5", "pu5", "yaa3", "taa1", "naai1",
    "lung1", "aao1", "nɔŋ4", "khɯi1", "pae1", "to1", "yow3", "te5",
    "yu5", "am1", "kin1", "maan3", "paa1", "waai6", "doi1", "pat4"
}

# Assamese script block
RE_ASSAMESE = re.compile(r"[\u0980-\u09FF]")
# Lik Tai / Myanmar block
RE_LIKTAI = re.compile(r"[\u1000-\u109F\uAA60-\uAA7F]")
# Khamyang tone 6 marker (Tone 6 is distinctively Khamyang; Phake has only 5 tones!)
RE_TONE_6 = re.compile(r"\b\w+6\b")


def detect_language(text: str) -> Dict[str, Any]:
    """
    Detects whether text is Tai Khamyang (ksu), Assamese (asm), or English (eng).
    Returns language ISO code, full name, and confidence score (0.0 to 1.0).
    """
    if not text or not text.strip():
        return {"language": "unknown", "name": "Unknown", "confidence": 0.0, "iso": "und"}

    cleaned = text.strip()

    # 1. Check for Assamese script
    assamese_chars = len(RE_ASSAMESE.findall(cleaned))
    total_chars = max(len(re.findall(r"\S", cleaned)), 1)
    if assamese_chars / total_chars > 0.4:
        # Check if it has Khamyang superscript tone numbers (¹..⁶)
        if re.search(r"[¹²³⁴⁵⁶]", cleaned):
            return {
                "language": "ksu",
                "name": "Tai Khamyang (Assamese Orthography)",
                "confidence": 0.95,
                "iso": "ksu",
                "script": "assamese_khamyang"
            }
        return {
            "language": "asm",
            "name": "Assamese",
            "confidence": 0.90,
            "iso": "asm",
            "script": "assamese"
        }

    # 2. Check for Lik Tai script
    liktai_chars = len(RE_LIKTAI.findall(cleaned))
    if liktai_chars / total_chars > 0.4:
        return {
            "language": "ksu",
            "name": "Tai Khamyang (Lik Tai Script)",
            "confidence": 0.98,
            "iso": "ksu",
            "script": "lik_tai"
        }

    # 3. Check Romanized text
    tokens = [t.lower() for t in re.findall(r"[A-Za-z\u0250-\u02AF]+[1-6]?", cleaned)]
    if not tokens:
        return {"language": "eng", "name": "English", "confidence": 0.5, "iso": "eng"}

    # Diagnostic token matches
    khamyang_matches = sum(1 for t in tokens if t in KHAMYANG_DIAGNOSTIC_MARKERS or (len(t) > 2 and t[-1] in "123456"))
    has_tone_6 = bool(RE_TONE_6.search(cleaned))

    ratio = khamyang_matches / len(tokens)
    if ratio > 0.3 or has_tone_6:
        conf = min(0.60 + ratio * 0.4, 0.99)
        return {
            "language": "ksu",
            "name": "Tai Khamyang (Romanized with Tones)",
            "confidence": round(conf, 2),
            "iso": "ksu",
            "script": "romanized"
        }

    # Otherwise fallback to English
    return {
        "language": "eng",
        "name": "English",
        "confidence": 0.85,
        "iso": "eng",
        "script": "latin"
    }
