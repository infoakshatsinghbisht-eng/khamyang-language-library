"""
Tai Khamyang Bidirectional Script Transliteration Engine
========================================================
Supports converting between:
- Romanized (Morey's orthography, e.g. "nam6", "khaw3")
- Lik Tai script (Shan/Khamti Unicode characters)
- Assamese script (অসমীয়া লিপি)
- IPA (International Phonetic Alphabet with pitch letters)
"""

import re
from typing import List, Optional
from khamyang.phonology.phonemes import parse_syllable
from khamyang.phonology.tones import TONES
from khamyang.transliteration.scripts import (
    ROMAN_TO_LIKTAI_CONSONANTS,
    ROMAN_TO_LIKTAI_VOWELS,
    ROMAN_TO_LIKTAI_CODAS,
    LIKTAI_TONE_MARKS,
    ROMAN_TO_ASSAMESE_CONSONANTS,
    ROMAN_TO_ASSAMESE_VOWELS,
    ROMAN_TO_ASSAMESE_CODAS,
    SUPERSCRIPT_TONES,
)


def syllable_to_liktai(syllable: str) -> str:
    """Converts a single Romanized syllable into Lik Tai script."""
    parsed = parse_syllable(syllable)
    onset_char = ROMAN_TO_LIKTAI_CONSONANTS.get(parsed.onset, "ဢ" if not parsed.onset else parsed.onset)
    medial_char = "ႂ" if parsed.medial == "w" else ""

    # In Lik Tai, if there is a coda, the vowel may combine or take standard vowel sign
    vowel_char = ""
    if parsed.coda:
        # Syllables with coda
        if parsed.nucleus in ("a", "aa"):
            # short a before coda often has implicit or asat
            vowel_char = "ႃ" if parsed.nucleus == "aa" else ""
        else:
            vowel_char = ROMAN_TO_LIKTAI_VOWELS.get(parsed.nucleus, "")
        coda_char = ROMAN_TO_LIKTAI_CODAS.get(parsed.coda, parsed.coda)
    else:
        # Open syllable
        vowel_char = ROMAN_TO_LIKTAI_VOWELS.get(parsed.nucleus, "ႃ" if parsed.nucleus == "a" else "")
        coda_char = ""

    tone_mark = LIKTAI_TONE_MARKS.get(parsed.tone, "")

    # For leading vowels like 'e' (ေ) and 'ɛ' (ႄ), in Burmese/Tai script they appear before consonant visually
    if vowel_char in ("ေ", "ႄ"):
        return f"{vowel_char}{onset_char}{medial_char}{coda_char}{tone_mark}"
    return f"{onset_char}{medial_char}{vowel_char}{coda_char}{tone_mark}"


def syllable_to_assamese(syllable: str, use_superscript_tone: bool = True) -> str:
    """Converts a single Romanized syllable into Assamese script."""
    parsed = parse_syllable(syllable)
    if not parsed.onset:
        # Independent vowel form
        independent_vowels = {
            "a": "অ",
            "aa": "আ",
            "i": "ই",
            "u": "উ",
            "e": "এ",
            "o": "ও",
            "ai": "ঐ",
            "au": "ঔ",
            "ɯ": "উ",
        }
        base = independent_vowels.get(parsed.nucleus, "অ" + ROMAN_TO_ASSAMESE_VOWELS.get(parsed.nucleus, ""))
    else:
        onset_char = ROMAN_TO_ASSAMESE_CONSONANTS.get(parsed.onset, parsed.onset)
        medial_char = "্ব" if parsed.medial == "w" else ""
        if parsed.coda:
            vowel_matra = "া" if parsed.nucleus in ("a", "aa") else ROMAN_TO_ASSAMESE_VOWELS.get(parsed.nucleus, "")
        else:
            vowel_matra = ROMAN_TO_ASSAMESE_VOWELS.get(parsed.nucleus, "")
        base = f"{onset_char}{medial_char}{vowel_matra}"

    coda_char = ROMAN_TO_ASSAMESE_CODAS.get(parsed.coda, parsed.coda) if parsed.coda else ""
    tone_indicator = SUPERSCRIPT_TONES.get(parsed.tone, str(parsed.tone)) if use_superscript_tone else str(parsed.tone)

    return f"{base}{coda_char}{tone_indicator}"


def syllable_to_ipa(syllable: str) -> str:
    """Converts a Romanized syllable into standard IPA."""
    parsed = parse_syllable(syllable)
    return parsed.ipa


def roman_to_liktai(text: str) -> str:
    """
    Transliterates Romanized Tai Khamyang text into Lik Tai script.
    Tokens separated by spaces or punctuation are processed individually.
    """
    tokens = re.findall(r"[A-Za-z0-9\?ɯʉəɛɔ]+|[^\s\w]+|\s+", text)
    result = []
    for token in tokens:
        if re.match(r"^[A-Za-z\?ɯʉəɛɔ]+[1-6]?$", token):
            result.append(syllable_to_liktai(token))
        else:
            result.append(token)
    return "".join(result)


def roman_to_assamese(text: str, superscript_tones: bool = True) -> str:
    """
    Transliterates Romanized Tai Khamyang text into Assamese script.
    """
    tokens = re.findall(r"[A-Za-z0-9\?ɯʉəɛɔ]+|[^\s\w]+|\s+", text)
    result = []
    for token in tokens:
        if re.match(r"^[A-Za-z\?ɯʉəɛɔ]+[1-6]?$", token):
            result.append(syllable_to_assamese(token, use_superscript_tone=superscript_tones))
        else:
            result.append(token)
    return "".join(result)


def roman_to_ipa(text: str) -> str:
    """Transliterates Romanized text to IPA."""
    tokens = text.strip().split()
    return " ".join(syllable_to_ipa(tok) for tok in tokens)


def liktai_to_roman(text: str) -> str:
    """
    Approximate reverse transliteration from Lik Tai script to Romanization.
    """
    # Look up known words or syllabify Lik Tai characters
    # Mapping of common graphemes
    char_map = {
        "ၵ": "k",
        "ၶ": "kh",
        "င": "ng",
        "ၸ": "ts",
        "သ": "ch",
        "ꩢ": "s",
        "ၺ": "ny",
        "တ": "t",
        "ထ": "th",
        "ၼ": "n",
        "ပ": "p",
        "ၽ": "ph",
        "ꩯ": "f",
        "မ": "m",
        "ယ": "y",
        "ဝ": "w",
        "လ": "l",
        "ရ": "r",
        "ႁ": "h",
        "ဢ": "",
        "ႃ": "aa",
        "ိ": "i",
        "ေ": "e",
        "ႄ": "ɛ",
        "ု": "u",
        "ူ": "o",
        "ို": "ɯ",
        "ႆ": "ai",
        "်": "",
        "ႇ": "2",
        "ႈ": "3",
        "း": "4",
        "ႉ": "5",
        "ႊ": "6",
    }
    out = []
    for char in text:
        out.append(char_map.get(char, char))
    return "".join(out)


def assamese_to_roman(text: str) -> str:
    """
    Converts Assamese-script Khamyang text into Romanization.
    """
    # Reverse mapping dictionary
    as_map = {
        "ক": "k", "খ": "kh", "ঙ": "ng", "চ": "ts", "ছ": "ch", "স": "s",
        "ঞ": "ny", "ত": "t", "থ": "th", "ন": "n", "প": "p", "ফ": "ph",
        "ফ়": "f", "ম": "m", "য": "y", "য়": "y", "ৱ": "w", "ল": "l",
        "ৰ": "r", "হ": "h", "অ": "a", "আ": "aa", "ই": "i", "উ": "u",
        "এ": "e", "ও": "o", "া": "a", "ি": "i", "ী": "i", "ু": "u",
        "ূ": "u", "ে": "e", "ো": "o", "ৌ": "au", "ৈ": "ai",
        "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6",
        "্": "",
    }
    out = []
    for ch in text:
        out.append(as_map.get(ch, ch))
    return "".join(out)


def transliterate(text: str, source_script: str = "roman", target_script: str = "liktai") -> str:
    """
    General entry point for script transliteration.

    Args:
        text: Input string.
        source_script: 'roman', 'liktai', or 'assamese'.
        target_script: 'roman', 'liktai', 'assamese', or 'ipa'.

    Returns:
        Transliterated string.
    """
    source = source_script.lower()
    target = target_script.lower()

    if source == target:
        return text

    # Step 1: Normalize source to roman
    if source == "roman":
        roman_text = text
    elif source in ("liktai", "lik_tai", "shan"):
        roman_text = liktai_to_roman(text)
    elif source in ("assamese", "as"):
        roman_text = assamese_to_roman(text)
    else:
        raise ValueError(f"Unsupported source script: {source_script}")

    # Step 2: Convert roman to target
    if target == "roman":
        return roman_text
    elif target in ("liktai", "lik_tai", "shan"):
        return roman_to_liktai(roman_text)
    elif target in ("assamese", "as"):
        return roman_to_assamese(roman_text)
    elif target == "ipa":
        return roman_to_ipa(roman_text)
    else:
        raise ValueError(f"Unsupported target script: {target_script}")
