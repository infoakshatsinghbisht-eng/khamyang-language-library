"""
Tai Khamyang Syntax and TAM (Tense-Aspect-Modality) Engine
===========================================================
Tai Khamyang is an isolating SVO language:
- Subject + Verb + Object
- Modifiers follow head nouns (Head-Initial): [Noun] + [Adjective]
- TAM markers:
  - Completive / Perfective: 'yow3' (sentence final or post-verbal)
  - Irrealis / Future: 'te5' / 'cak4' (pre-verbal)
  - Continuous / Progressive: 'yu5' (post-verbal)
  - Negative: 'am1' (pre-verbal)
  - Interrogative: 'ka1' / 'hɯ1' (sentence final)
"""

from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class TAMMarker:
    name: str
    form_roman: str
    lik_tai: str
    assamese: str
    position: str  # pre-verbal, post-verbal, sentence-final
    meaning: str
    example: str
    translation: str


TAM_MARKERS: Dict[str, TAMMarker] = {
    "perfective": TAMMarker(
        name="Completive / Perfective",
        form_roman="yow3",
        lik_tai="ယဝ်ႉ",
        assamese="যৌ",
        position="sentence-final",
        meaning="Marks completed action (equivalent to Assamese -ল/হ'ল or already)",
        example="kaw1 kin1 khaw3 yow3",
        translation="I have eaten rice / I already ate.",
    ),
    "future": TAMMarker(
        name="Future / Irrealis",
        form_roman="te5",
        lik_tai="တေ",
        assamese="তে",
        position="pre-verbal",
        meaning="Marks future intent, plan or certainty (will / shall)",
        example="kaw1 te5 pai1 maan3",
        translation="I will go to the village.",
    ),
    "progressive": TAMMarker(
        name="Progressive / Continuous",
        form_roman="yu5",
        lik_tai="ယူႇ",
        assamese="য়ু",
        position="post-verbal",
        meaning="Marks ongoing action in progress (equivalent to -ing)",
        example="man1 kin1 khaw3 yu5",
        translation="He/She is eating rice.",
    ),
    "negative": TAMMarker(
        name="Negative Marker",
        form_roman="am1",
        lik_tai="ဢမ်ႇ",
        assamese="আম",
        position="pre-verbal",
        meaning="Standard verbal negation (not / don't)",
        example="kaw1 am1 hu3",
        translation="I do not know.",
    ),
    "question": TAMMarker(
        name="Polar Question Marker",
        form_roman="ka1",
        lik_tai="ၵႃး",
        assamese="কা",
        position="sentence-final",
        meaning="Turns statement into a yes/no polar question",
        example="maɯ2 yu5 di1 ka1?",
        translation="Are you doing well?",
    ),
    "experiential": TAMMarker(
        name="Experiential Aspect",
        form_roman="kye1",
        lik_tai="ၵေႇ",
        assamese="কে",
        position="pre-verbal",
        meaning="Marks having had an experience in the past (ever / have experienced)",
        example="kaw1 kye1 pai1 pat4 kai1",
        translation="I have once gone to the Patkai mountains.",
    ),
    "prohibitive": TAMMarker(
        name="Prohibitive Negative",
        form_roman="paai1",
        lik_tai="ပၢႆ",
        assamese="পাই",
        position="pre-verbal",
        meaning="Marks negative imperative command (do not / don't)",
        example="paai1 pai1 nai1 thɯn2",
        translation="Do not wander into the wild forest.",
    ),
    "optative": TAMMarker(
        name="Optative / Causative Marker",
        form_roman="hɯ3",
        lik_tai="ႁႂ်ႈ",
        assamese="হ্যৌ",
        position="sentence-initial / pre-verbal",
        meaning="Marks blessing, wish, optative mood, or causative action (may / let / cause)",
        example="hɯ3 khon1 maan3 yu5 di1 kin1 waan1",
        translation="May the villagers live well and prosper.",
    ),
}


class NounPhraseBuilder:
    """
    Constructs canonical Tai Khamyang Head-Initial Noun Phrases:
    [Head Noun] + [Adjective] + [Numeral] + [Classifier] + [Demonstrative]
    """

    @staticmethod
    def build_noun_phrase(
        noun: str,
        adjective: Optional[str] = None,
        numeral: Optional[str] = None,
        classifier: Optional[str] = None,
        demonstrative: Optional[str] = None,
    ) -> Dict[str, str]:
        parts = [noun]
        if adjective:
            parts.append(adjective)
        if numeral:
            parts.append(numeral)
        if classifier:
            parts.append(classifier)
        if demonstrative:
            parts.append(demonstrative)

        np_roman = " ".join(parts)
        from khamyang.transliteration.converter import roman_to_liktai, roman_to_assamese, roman_to_ipa

        return {
            "roman": np_roman,
            "lik_tai": roman_to_liktai(np_roman),
            "assamese": roman_to_assamese(np_roman),
            "ipa": roman_to_ipa(np_roman),
        }


class SentenceBuilder:
    """Helper to assemble grammatically valid Tai Khamyang sentences."""

    @staticmethod
    def build_simple_sentence(
        subject: str,
        verb: str,
        obj: Optional[str] = None,
        tam: Optional[str] = None,
        negated: bool = False,
        prohibitive: bool = False,
        directional_verb: Optional[str] = None,
        is_question: bool = False,
        is_optative: bool = False,
    ) -> Dict[str, str]:
        """
        Builds a sentence adhering to canonical Tai Khamyang syntax rules:
        - SVO word order
        - Head-initial NP architecture
        - Pre-verbal vs Post-verbal TAM placement
        - Serial Verb directional vectors (maa1, pai1, long1, khɯn3)
        """
        parts: List[str] = []

        if is_optative:
            parts.append("hɯ3")

        parts.append(subject)

        if prohibitive:
            parts.append("paai1")
        elif negated:
            parts.append("am1")

        if tam in ("future", "te5"):
            parts.append("te5")
        elif tam in ("experiential", "kye1"):
            parts.append("kye1")

        parts.append(verb)

        # Directional Serial Verb vector
        if directional_verb:
            parts.append(directional_verb)

        if tam in ("progressive", "yu5"):
            parts.append("yu5")

        if obj:
            parts.append(obj)

        if tam in ("perfective", "yow3"):
            parts.append("yow3")

        if is_question:
            parts.append("ka1")

        roman_sentence = " ".join(parts)
        from khamyang.transliteration.converter import roman_to_liktai, roman_to_assamese, roman_to_ipa

        return {
            "roman": roman_sentence,
            "lik_tai": roman_to_liktai(roman_sentence),
            "assamese": roman_to_assamese(roman_sentence),
            "ipa": roman_to_ipa(roman_sentence),
        }
