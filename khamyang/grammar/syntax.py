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
        is_question: bool = False,
    ) -> Dict[str, str]:
        """
        Builds a sentence adhering to Tai Khamyang syntax rules.
        """
        parts: List[str] = [subject]

        if negated:
            parts.append("am1")

        if tam == "future":
            parts.append("te5")

        parts.append(verb)

        if tam == "progressive":
            parts.append("yu5")

        if obj:
            parts.append(obj)

        if tam == "perfective":
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
