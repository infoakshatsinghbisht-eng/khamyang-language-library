"""
Tai Khamyang Pronoun System & Honorifics
========================================
Documents personal pronouns, demonstratives, and interrogative pronouns.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class Pronoun:
    person: str          # 1st, 2nd, 3rd
    number: str          # singular, plural, dual
    form_roman: str
    lik_tai: str
    assamese: str
    gloss_en: str
    gloss_as: str
    politeness: str      # standard, polite, intimate, honorific


PRONOUNS: List[Pronoun] = [
    # 1st Person
    Pronoun("1", "singular", "kaw1", "ၵဝ်", "কাও", "I, me", "মই", "standard/informal"),
    Pronoun("1", "singular", "haaw1", "ႁဝ်း", "হাও", "I, me (humble/polite)", "মই (বিনম্ৰ)", "polite"),
    Pronoun("1", "plural", "haw1", "ႁဝ်း", "হাও", "we, us (inclusive/general)", "আমি", "standard"),
    Pronoun("1", "plural", "tu1 haw1", "တူဝ်ႁဝ်း", "তু হাও", "we, ourselves", "আমি সকলো", "emphatic"),
    # 2nd Person
    Pronoun("2", "singular", "maɯ2", "မႂ်း", "মাই", "you (singular)", "তই / তুমি", "standard"),
    Pronoun("2", "singular", "mɯŋ2", "မိုဝ်း", "মুং", "you (singular, colloquial)", "তই", "intimate"),
    Pronoun("2", "singular", "su1", "သု", "চু", "you (singular, respectful/elder)", "আপুনি", "polite/honorific"),
    Pronoun("2", "plural", "su1 haw1", "သုႁဝ်း", "চু হাও", "you all (plural)", "তোমালোক / আপোনালোক", "standard"),
    # 3rd Person
    Pronoun("3", "singular", "man1", "မၼ်း", "মান", "he, him, she, her, it", "সি / তাই / তেওঁ", "standard"),
    Pronoun("3", "plural", "khaw1", "ၶဝ်", "খাও", "they, them", "তেওঁলোক / সিহঁত", "standard"),
    Pronoun("3", "plural", "man1 haw1", "မၼ်းႁဝ်း", "মান হাও", "they, them (group)", "সিহঁত", "colloquial"),
    # Demonstratives
    Pronoun("dem", "proximal", "nai6", "ၼႆႉ", "নাই", "this, here", "এইটো / এই", "demonstrative"),
    Pronoun("dem", "distal", "nan6", "ၼၼ်ႉ", "নান", "that, there", "সেইটো / সেই", "demonstrative"),
    # Interrogatives
    Pronoun("wh", "person", "phɯ1", "ၽိုဝ်", "ফু", "who", "কোন", "interrogative"),
    Pronoun("wh", "thing", "sang1", "သင်", "চাং", "what", "কি", "interrogative"),
    Pronoun("wh", "place", "ti6 lau1", "တီႈလႂ်", "তি লাউ", "where", "ক'ত", "interrogative"),
    Pronoun("wh", "time", "mɯa5 lau1", "မိူဝ်ႈလႂ်", "মুৱা লাউ", "when", "কেতিয়া", "interrogative"),
    Pronoun("wh", "manner", "tsang1 hɯ1", "ၸင်ႇႁိုဝ်", "চাং হু", "how", "কেনেকৈ", "interrogative"),
]


def list_pronouns(person: Optional[str] = None) -> List[Pronoun]:
    """Filters pronouns by person or category ('1', '2', '3', 'dem', 'wh')."""
    if person:
        p = str(person).lower()
        return [pr for pr in PRONOUNS if pr.person == p]
    return PRONOUNS
