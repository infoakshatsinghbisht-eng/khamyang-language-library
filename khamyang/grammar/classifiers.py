"""
Tai Khamyang Classifier Agreement Engine
========================================
In Tai languages, numerals and demonstratives cannot directly modify nouns.
They require an appropriate numeral classifier:
    Noun + Numeral + Classifier
    Example: maa1 (dog) + sɔŋ1 (two) + to1 (CLF:animal) -> 'maa1 sɔŋ1 to1'
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass
class Classifier:
    roman: str
    lik_tai: str
    assamese: str
    meaning: str
    categories: List[str]
    sample_nouns: List[str]
    example: str
    translation: str


CLASSIFIERS: Dict[str, Classifier] = {
    "to1": Classifier(
        roman="to1",
        lik_tai="တူဝ်",
        assamese="টো",
        meaning="Living animals, creatures, insects, clothing, quadrupeds",
        categories=["animal", "bird", "fish", "insect", "clothing"],
        sample_nouns=["maa1 (dog)", "meo1 (cat)", "kwaai1 (buffalo)", "nok4 (bird)", "paa1 (fish)", "sɯa1 (shirt)"],
        example="maa1 sɔŋ1 to1",
        translation="two dogs",
    ),
    "ko5": Classifier(
        roman="ko5",
        lik_tai="ၵေႃႉ",
        assamese="জন / গৰাকী",
        meaning="Human beings, persons, children, elders, respected individuals",
        categories=["person", "human", "child", "kinship"],
        sample_nouns=["khon1 (person)", "luk4 (child)", "po5 (father)", "me5 (mother)", "tsaw3 (elder/lord)"],
        example="khon1 saam1 ko5",
        translation="three people",
    ),
    "ton3": Classifier(
        roman="ton3",
        lik_tai="တူၼ်ႈ",
        assamese="ডাল / জোপা",
        meaning="Trees, standing plants, trunks, bamboo groves",
        categories=["tree", "plant", "flora"],
        sample_nouns=["ton3 mai6 (tree)", "ton3 waai6 (rattan plant)", "ton3 saa1 (tea bush)"],
        example="ton3 mai6 nɯŋ5 ton3",
        translation="one tree",
    ),
    "lem3": Classifier(
        roman="lem3",
        lik_tai="လႅမ်ႈ",
        assamese="খন / পাত / ডাল",
        meaning="Long, slender, pointed objects, tools, weapons, manuscripts, books",
        categories=["tool", "weapon", "book", "manuscript", "needle"],
        sample_nouns=["mit4 (knife)", "khem1 (needle)", "lik4 (book/manuscript)", "hɔ4 (spear)"],
        example="lik4 saam1 lem3",
        translation="three books",
    ),
    "lung1": Classifier(
        roman="lung1",
        lik_tai="လင်",
        assamese="ঘৰ / খন",
        meaning="Houses, architectural structures, huts, monastery buildings",
        categories=["building", "house", "dwelling"],
        sample_nouns=["hɯn1 (house)", "wat4 (monastery)", "tsong1 (hall)"],
        example="hɯn1 sɔŋ1 lung1",
        translation="two houses",
    ),
    "bai1": Classifier(
        roman="bai1",
        lik_tai="မႂ်",
        assamese="খন / পাত",
        meaning="Leaves, flat thin sheets, papers, documents",
        categories=["leaf", "paper", "sheet"],
        sample_nouns=["bai1 mai6 (leaf)", "bai1 tsia1 (paper)", "bai1 lik4 (page)"],
        example="bai1 mai6 haa3 bai1",
        translation="five leaves",
    ),
    "phɯn1": Classifier(
        roman="phɯn1",
        lik_tai="ၽိုၼ်",
        assamese="খন",
        meaning="Woven textile pieces, cloth, sarongs, mats, traditional blankets",
        categories=["textile", "cloth", "garment"],
        sample_nouns=["phaa3 (cloth)", "phaa3 sin3 (sarong)", "phɯk4 (mat)"],
        example="phaa3 sin3 sɔŋ1 phɯn1",
        translation="two sarongs",
    ),
    "maak4": Classifier(
        roman="maak4",
        lik_tai="မၢၵ်ႇ",
        assamese="টো / গুটি",
        meaning="Fruits, spherical round objects, seeds",
        categories=["fruit", "round_object", "seed"],
        sample_nouns=["maak4 mai6 (fruit)", "maak4 muang3 (mango)", "maak4 phe4 (chilli)"],
        example="maak4 mai6 si5 maak4",
        translation="four fruits",
    ),
    "tsɔk4": Classifier(
        roman="tsɔk4",
        lik_tai="ၸွၵ်း",
        assamese="কাপ",
        meaning="Cups, small drinking vessels, cups of beverage",
        categories=["cup", "vessel", "drink"],
        sample_nouns=["nam6 saa1 (tea)", "nam6 (water)", "lao3 (rice wine)"],
        example="nam6 saa1 nɯŋ5 tsɔk4",
        translation="one cup of tea",
    ),
    "an1": Classifier(
        roman="an1",
        lik_tai="ဢၼ်",
        assamese="টো",
        meaning="General default classifier for miscellaneous inanimate items",
        categories=["general", "inanimate", "abstract"],
        sample_nouns=["kho1 (thing)", "ti6 (place)", "kham1 (word)"],
        example="kho1 nɯŋ5 an1",
        translation="one thing",
    ),
}

# Noun-to-Classifier lookup mapping
NOUN_CLASSIFIER_MAP: Dict[str, str] = {
    # Animals -> to1
    "maa": "to1", "maa1": "to1",
    "meo": "to1", "meo1": "to1",
    "kwaai": "to1", "kwaai1": "to1",
    "wo": "to1", "wo1": "to1",
    "mu": "to1", "mu1": "to1",
    "nok": "to1", "nok4": "to1",
    "paa": "to1", "paa1": "to1",
    "tsaang": "to1", "tsaang3": "to1",
    "sɯa": "to1", "sɯa1": "to1",
    "ling": "to1", "ling1": "to1",
    "ngu": "to1", "ngu1": "to1",
    "kai": "to1", "kai5": "to1",
    "pet": "to1", "pet4": "to1",
    # Humans -> ko5
    "khon": "ko5", "khon1": "ko5",
    "luk": "ko5", "luk4": "ko5",
    "po": "ko5", "po5": "ko5",
    "me": "ko5", "me5": "ko5",
    "pi": "ko5", "pi3": "ko5",
    "nɔŋ": "ko5", "nɔŋ3": "ko5",
    "chaopha": "ko5", "chaopha1": "ko5",
    # Trees / Plants -> ton3
    "ton": "ton3", "ton3": "ton3",
    "ton mai": "ton3", "ton3 mai6": "ton3",
    "mai": "ton3", "mai6": "ton3",
    # Houses / Buildings -> lung1
    "hɯn": "lung1", "hɯn1": "lung1",
    "wat": "lung1", "wat4": "lung1",
    # Tools / Books -> lem3
    "mit": "lem3", "mit4": "lem3",
    "lik": "lem3", "lik4": "lem3",
    "khem": "lem3", "khem1": "lem3",
    # Flat / Cloth -> phɯn1 / bai1
    "phaa": "phɯn1", "phaa3": "phɯn1",
    "sin": "phɯn1", "sin3": "phɯn1",
    "bai mai": "bai1", "bai1 mai6": "bai1",
    # Fruits -> maak4
    "maak mai": "maak4", "maak4 mai6": "maak4",
}


class ClassifierEngine:
    """Validates and constructs Tai Khamyang classifier phrases."""

    @staticmethod
    def get_classifier(noun: str) -> Optional[Classifier]:
        """Finds the appropriate classifier for a noun."""
        clean = noun.strip().lower()
        clf_code = NOUN_CLASSIFIER_MAP.get(clean)
        if clf_code:
            return CLASSIFIERS.get(clf_code)
        # Check substring matches
        for k, v in NOUN_CLASSIFIER_MAP.items():
            if k in clean:
                return CLASSIFIERS.get(v)
        return CLASSIFIERS["an1"]  # default

    @classmethod
    def quantify(cls, noun_roman: str, count: int) -> str:
        """
        Builds a canonical Tai phrase: Noun + Numeral + Classifier.
        Example: quantify('maa1', 2) -> 'maa1 sɔŋ1 to1'
        """
        from khamyang.grammar.numerals import num_to_khamyang
        num_word = num_to_khamyang(count)
        clf = cls.get_classifier(noun_roman)
        clf_roman = clf.roman if clf else "an1"
        return f"{noun_roman} {num_word} {clf_roman}"

    @classmethod
    def list_all_classifiers(cls) -> List[Classifier]:
        return list(CLASSIFIERS.values())
