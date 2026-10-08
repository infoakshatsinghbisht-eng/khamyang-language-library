"""
Tai Khamyang Consonants, Vowels, and Syllable Structure
======================================================
Based on Stephen Morey's phonological analysis:
- 16 core consonant phonemes + glottal stop /ʔ/
- 9 basic vowel qualities + length contrast between /a/ and /aː/
- Canonical syllable shape: C(w)V(C) + Tone (1-6)
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple
import re


@dataclass(frozen=True)
class Consonant:
    symbol: str
    ipa: str
    name: str
    manner: str
    place: str
    voicing: bool
    aspirated: bool = False
    lik_tai: str = ""
    assamese: str = ""


CONSONANTS: Dict[str, Consonant] = {
    "k": Consonant("k", "k", "Voiceless velar stop", "stop", "velar", False, False, "ၵ", "ক"),
    "kh": Consonant("kh", "kʰ", "Voiceless aspirated velar stop", "stop", "velar", False, True, "ၶ", "খ"),
    "ng": Consonant("ng", "ŋ", "Velar nasal", "nasal", "velar", True, False, "င", "ঙ"),
    "ts": Consonant("ts", "tɕ", "Voiceless alveolo-palatal affricate", "affricate", "palatal", False, False, "ၸ", "চ"),
    "c": Consonant("c", "tɕ", "Voiceless palatal affricate", "affricate", "palatal", False, False, "ၸ", "চ"),
    "ch": Consonant("ch", "tɕʰ", "Voiceless aspirated palatal affricate", "affricate", "palatal", False, True, "သ", "ছ"),
    "s": Consonant("s", "s", "Voiceless alveolar fricative", "fricative", "alveolar", False, False, "ꩢ", "স"),
    "ny": Consonant("ny", "ɲ", "Palatal nasal", "nasal", "palatal", True, False, "ၺ", "ঞ"),
    "t": Consonant("t", "t", "Voiceless alveolar stop", "stop", "alveolar", False, False, "တ", "ত"),
    "th": Consonant("th", "tʰ", "Voiceless aspirated alveolar stop", "stop", "alveolar", False, True, "ထ", "থ"),
    "n": Consonant("n", "n", "Alveolar nasal", "nasal", "alveolar", True, False, "ၼ", "ন"),
    "p": Consonant("p", "p", "Voiceless bilabial stop", "stop", "bilabial", False, False, "ပ", "প"),
    "ph": Consonant("ph", "pʰ", "Voiceless aspirated bilabial stop", "stop", "bilabial", False, True, "ၽ", "ফ"),
    "f": Consonant("f", "f", "Voiceless labiodental fricative", "fricative", "labiodental", False, False, "ꩯ", "ফ়"),
    "m": Consonant("m", "m", "Bilabial nasal", "nasal", "bilabial", True, False, "မ", "ম"),
    "y": Consonant("y", "j", "Palatal approximant", "approximant", "palatal", True, False, "ယ", "য"),
    "w": Consonant("w", "w", "Labio-velar approximant", "approximant", "labio-velar", True, False, "ဝ", "ৱ"),
    "l": Consonant("l", "l", "Alveolar lateral approximant", "lateral", "alveolar", True, False, "လ", "ল"),
    "r": Consonant("r", "r", "Alveolar trill (regional/loan)", "trill", "alveolar", True, False, "ရ", "ৰ"),
    "h": Consonant("h", "h", "Voiceless glottal fricative", "fricative", "glottal", False, False, "ႁ", "হ"),
    "?": Consonant("?", "ʔ", "Glottal stop", "stop", "glottal", False, False, "ဢ", "অ"),
}


@dataclass(frozen=True)
class Vowel:
    symbol: str
    ipa: str
    name: str
    height: str
    backness: str
    rounded: bool
    long: bool
    lik_tai: str = ""
    assamese: str = ""


VOWELS: Dict[str, Vowel] = {
    "i": Vowel("i", "i", "Close front unrounded", "close", "front", False, False, "ိ", "ি"),
    "e": Vowel("e", "e", "Close-mid front unrounded", "close-mid", "front", False, False, "ေ", "ে"),
    "ɛ": Vowel("ɛ", "ɛ", "Open-mid front unrounded", "open-mid", "front", False, False, "ႄ", "ে"),
    "ee": Vowel("ee", "ɛ", "Open-mid front unrounded", "open-mid", "front", False, True, "ႄ", "ে"),
    "ɯ": Vowel("ɯ", "ɯ", "Close back unrounded", "close", "back", False, False, "ို", "ু"),
    "ʉ": Vowel("ʉ", "ɯ", "Close back unrounded", "close", "back", False, False, "ို", "ু"),
    "eu": Vowel("eu", "ɯ", "Close back unrounded", "close", "back", False, False, "ို", "ু"),
    "ə": Vowel("ə", "ə", "Mid central unrounded", "mid", "central", False, False, "ိုဝ်", "ো"),
    "a": Vowel("a", "a", "Open central short", "open", "central", False, False, "ႃ", "া"),
    "aa": Vowel("aa", "aː", "Open central long", "open", "central", False, True, "ႃ", "া"),
    "u": Vowel("u", "u", "Close back rounded", "close", "back", True, False, "ု", "ু"),
    "o": Vowel("o", "o", "Close-mid back rounded", "close-mid", "back", True, False, "ူ", "ো"),
    "ɔ": Vowel("ɔ", "ɔ", "Open-mid back rounded", "open-mid", "back", True, False, "ွ", "অ"),
    "oo": Vowel("oo", "ɔ", "Open-mid back rounded", "open-mid", "back", True, True, "ွ", "অ"),
    "ai": Vowel("ai", "ai", "Diphthong a + i", "diphthong", "fronting", False, False, "ႆ", "াই"),
    "aai": Vowel("aai", "aːi", "Diphthong aa + i", "diphthong", "fronting", False, True, "ႃႆ", "াই"),
    "au": Vowel("au", "au", "Diphthong a + u", "diphthong", "backing", True, False, "ဝ်", "াও"),
    "aau": Vowel("aau", "aːu", "Diphthong aa + u", "diphthong", "backing", True, True, "ႃဝ်", "াও"),
    "oi": Vowel("oi", "oi", "Diphthong o + i", "diphthong", "fronting", False, False, "ူႆ", "ওই"),
    "ui": Vowel("ui", "ui", "Diphthong u + i", "diphthong", "fronting", False, False, "ုႆ", "ুই"),
    "ɯi": Vowel("ɯi", "ɯi", "Diphthong ɯ + i", "diphthong", "fronting", False, False, "ိုႆ", "ুই"),
    "ia": Vowel("ia", "ia", "Centering diphthong i + a", "diphthong", "centering", False, False, "ျႃ", "িয়া"),
    "ɯa": Vowel("ɯa", "ɯa", "Centering diphthong ɯ + a", "diphthong", "centering", False, False, "ိုဝ်ႃ", "ুৱা"),
    "ua": Vowel("ua", "ua", "Centering diphthong u + a", "diphthong", "centering", True, False, "ွႃ", "ুৱা"),
}


@dataclass
class SyllableStructure:
    """Parsed phonetic structure of a Tai Khamyang syllable."""
    original: str
    onset: str
    medial: Optional[str]
    nucleus: str
    coda: Optional[str]
    tone: int
    ipa: str


def parse_syllable(syllable: str) -> SyllableStructure:
    """
    Parses a Romanized Khamyang syllable into onset, medial, nucleus, coda, and tone.
    Example: 'kwaai1' -> onset='k', medial='w', nucleus='aai', coda=None, tone=1
    Example: 'nam6' -> onset='n', medial=None, nucleus='a', coda='m', tone=6
    """
    s = syllable.strip().lower()
    tone = 1
    if s and s[-1] in "123456":
        tone = int(s[-1])
        s = s[:-1]

    # Pattern for Tai syllable:
    # Optional onset consonants: kh, ph, th, ts, ch, ny, ng, k, t, p, f, s, m, n, y, w, l, r, h, ?
    consonant_regex = r"^(kh|ph|th|ts|ch|ny|ng|[ktpfsmn ywlr h\?])"
    onset_match = re.match(consonant_regex, s)
    onset = onset_match.group(1) if onset_match else ""
    remainder = s[len(onset):]

    # Check for medial -w- (e.g. kwaai, kwaang, swa)
    medial = None
    if remainder.startswith("w") and len(remainder) > 1 and remainder[1] in "aeiouɯʉəɛɔ":
        medial = "w"
        remainder = remainder[1:]

    # Coda consonants at end of syllable: ng, m, n, p, t, k, w, y, ?
    coda_regex = r"(ng|[mnptkwy\?])$"
    coda_match = re.search(coda_regex, remainder)
    coda = coda_match.group(1) if coda_match else None
    if coda:
        nucleus = remainder[:-len(coda)]
    else:
        nucleus = remainder

    # Compute approximate IPA
    onset_ipa = CONSONANTS.get(onset, Consonant(onset, onset, "", "", "", False)).ipa if onset else ""
    medial_ipa = "w" if medial else ""
    nucleus_ipa = VOWELS.get(nucleus, Vowel(nucleus, nucleus, "", "", "", False, False)).ipa
    coda_ipa = CONSONANTS.get(coda, Consonant(coda, coda, "", "", "", False)).ipa if coda else ""
    from khamyang.phonology.tones import TONES
    tone_symbol = TONES[tone].ipa_symbol

    full_ipa = f"[{onset_ipa}{medial_ipa}{nucleus_ipa}{coda_ipa}{tone_symbol}]"

    return SyllableStructure(
        original=syllable,
        onset=onset,
        medial=medial,
        nucleus=nucleus,
        coda=coda,
        tone=tone,
        ipa=full_ipa,
    )
