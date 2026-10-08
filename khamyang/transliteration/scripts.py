"""
Mapping Tables for Tai Khamyang Scripts
=======================================
Supports:
1. Lik Tai (Shan / Myanmar Extended-A Unicode)
2. Assamese Script (অসমীয়া লিপি used locally in Assam)
3. Romanization (Stephen Morey's standard with tone digits 1-6)
4. International Phonetic Alphabet (IPA)
"""

from typing import Dict

# Consonant Mappings: Roman -> Lik Tai (Shan/Khamti Unicode)
ROMAN_TO_LIKTAI_CONSONANTS: Dict[str, str] = {
    "k": "ၵ",
    "kh": "ၶ",
    "ng": "င",
    "ts": "ၸ",
    "c": "ၸ",
    "ch": "သ",
    "s": "ꩢ",
    "ny": "ၺ",
    "t": "တ",
    "th": "ထ",
    "n": "ၼ",
    "p": "ပ",
    "ph": "ၽ",
    "f": "ꩯ",
    "m": "မ",
    "y": "ယ",
    "w": "ဝ",
    "l": "လ",
    "r": "ရ",
    "h": "ႁ",
    "?": "ဢ",
}

# Consonant Mappings: Roman -> Assamese
ROMAN_TO_ASSAMESE_CONSONANTS: Dict[str, str] = {
    "k": "ক",
    "kh": "খ",
    "ng": "ঙ",
    "ts": "চ",
    "c": "চ",
    "ch": "ছ",
    "s": "স",
    "ny": "ঞ",
    "t": "ত",
    "th": "থ",
    "n": "ন",
    "p": "প",
    "ph": "ফ",
    "f": "ফ়",
    "m": "ম",
    "y": "য",
    "w": "ৱ",
    "l": "ল",
    "r": "ৰ",
    "h": "হ",
    "?": "অ",
}

# Vowel Mappings: Roman -> Lik Tai (Dependent vowels)
ROMAN_TO_LIKTAI_VOWELS: Dict[str, str] = {
    "aa": "ႃ",
    "a": "ႃ",
    "i": "ိ",
    "e": "ေ",
    "ɛ": "ႄ",
    "ee": "ႄ",
    "u": "ု",
    "o": "ူ",
    "ɔ": "ွ",
    "oo": "ွ",
    "ɯ": "ို",
    "ʉ": "ို",
    "eu": "ို",
    "ə": "ိုဝ်",
    "ai": "ႆ",
    "aai": "ႃႆ",
    "au": "ဝ်",
    "aau": "ႃဝ်",
    "oi": "ူႆ",
    "ui": "ုႆ",
    "ɯi": "ိုႆ",
    "ia": "ျႃ",
    "ɯa": "ိုဝ်ႃ",
    "ua": "ွႃ",
}

# Vowel Mappings: Roman -> Assamese (Dependent matras)
ROMAN_TO_ASSAMESE_VOWELS: Dict[str, str] = {
    "aa": "া",
    "a": "া",
    "i": "ি",
    "e": "ে",
    "ɛ": "ে",
    "ee": "ে",
    "u": "ু",
    "o": "ো",
    "ɔ": "অ",
    "oo": "ো",
    "ɯ": "ু",
    "ʉ": "ু",
    "eu": "ু",
    "ə": "ো",
    "ai": "াই",
    "aai": "াই",
    "au": "াও",
    "aau": "াও",
    "oi": "ওই",
    "ui": "ুই",
    "ɯi": "ুই",
    "ia": "িয়া",
    "ɯa": "ুৱা",
    "ua": "ুৱা",
}

# Final Coda Mappings: Roman -> Lik Tai (with asat / virama U+103A)
ROMAN_TO_LIKTAI_CODAS: Dict[str, str] = {
    "k": "ၵ်",
    "t": "တ်",
    "p": "ပ်",
    "m": "မ်",
    "n": "ၼ်",
    "ng": "င်",
    "w": "ဝ်",
    "y": "ႆ",
    "?": "ဢ်",
}

# Final Coda Mappings: Roman -> Assamese (with hasant / virama)
ROMAN_TO_ASSAMESE_CODAS: Dict[str, str] = {
    "k": "ক্‌",
    "t": "ত্‌",
    "p": "প্‌",
    "m": "ম",
    "n": "ন",
    "ng": "ঙ",
    "w": "ৱ",
    "y": "য়",
    "?": "’",
}

# Lik Tai Tone Marks
LIKTAI_TONE_MARKS: Dict[int, str] = {
    1: "",      # Tone 1 is unmarked in traditional orthography
    2: "ႇ",     # U+1087 Shan tone 2
    3: "ႈ",     # U+1088 Shan tone 3
    4: "း",     # U+1038 Myanmar sign visarga
    5: "ႉ",     # U+1089 Shan tone 5
    6: "ႊ",     # U+108A Shan tone 6
}

# Superscript tone numbers for Assamese / Latin typography
SUPERSCRIPT_TONES: Dict[int, str] = {
    1: "¹",
    2: "²",
    3: "³",
    4: "⁴",
    5: "⁵",
    6: "⁶",
}

# Reverse mapping: Lik Tai -> Roman
LIKTAI_TO_ROMAN_CONSONANTS: Dict[str, str] = {v: k for k, v in ROMAN_TO_LIKTAI_CONSONANTS.items()}
# Add standard Myanmar fallback shapes
LIKTAI_TO_ROMAN_CONSONANTS.update({
    "က": "k",
    "ခ": "kh",
    "စ": "ts",
    "ဆ": "ch",
    "န": "n",
    "ဖ": "ph",
    "ဟ": "h",
    "အ": "?",
})
