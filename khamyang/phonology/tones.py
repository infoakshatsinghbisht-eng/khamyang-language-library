"""
Tai Khamyang 6-Tone System
==========================
Based on linguistic documentation by Dr. Stephen Morey:
- "The Tai Languages of Assam: A Grammar and Texts" (2005)
- "Tonal change in the Tai languages of Northeast India" (2005)

Khamyang has six phonemic tones:
1. Mid-level with slight fall [33]
2. High level then falling [54]
3. Low falling creaky [21̰]
4. High level then falling with final glottal closure [54ʔ]
5. Low falling [21]
6. Level with possible final rise [35]
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class KhamyangTone:
    """Represents one of the six lexical tones of Tai Khamyang."""
    number: int
    name: str
    pitch_chao: str          # Chao tone numerals, e.g., '33', '54'
    ipa_symbol: str          # IPA tone contour letters, e.g., '˧˧', '˥˦'
    description: str
    gedney_cells: Tuple[str, ...]
    creaky: bool = False
    glottalized: bool = False
    f0_contour_normalized: Tuple[float, ...] = (1.0, 1.0)  # relative f0 multiplier for synthesis

    def get_hz_curve(self, base_hz: float = 160.0) -> List[float]:
        """Calculates approximate pitch curve in Hertz for audio synthesis."""
        return [base_hz * m for m in self.f0_contour_normalized]


TONES: Dict[int, KhamyangTone] = {
    1: KhamyangTone(
        number=1,
        name="Mid Level",
        pitch_chao="33",
        ipa_symbol="˧˧",
        description="Mid level with a slight fall at the very end.",
        gedney_cells=("A1", "A3", "B1"),
        creaky=False,
        glottalized=False,
        f0_contour_normalized=(1.05, 1.02, 1.00, 0.96),
    ),
    2: KhamyangTone(
        number=2,
        name="High Falling",
        pitch_chao="54",
        ipa_symbol="˥˦",
        description="High level onset transitioning into a noticeable fall.",
        gedney_cells=("B2", "C2"),
        creaky=False,
        glottalized=False,
        f0_contour_normalized=(1.35, 1.30, 1.15, 0.95),
    ),
    3: KhamyangTone(
        number=3,
        name="Low Creaky",
        pitch_chao="21",
        ipa_symbol="˨˩̰",
        description="Low falling tone with distinctive creaky/laryngealized voice.",
        gedney_cells=("A4", "B4"),
        creaky=True,
        glottalized=False,
        f0_contour_normalized=(0.88, 0.82, 0.74, 0.68),
    ),
    4: KhamyangTone(
        number=4,
        name="High Falling Glottalized",
        pitch_chao="54ʔ",
        ipa_symbol="˥˦ʔ",
        description="High level then falling with an abrupt final glottal stop closure [ʔ].",
        gedney_cells=("C1", "C4", "DL1", "DS1", "DL4", "DS4"),
        creaky=False,
        glottalized=True,
        f0_contour_normalized=(1.35, 1.30, 1.18, 1.05),
    ),
    5: KhamyangTone(
        number=5,
        name="Low Falling",
        pitch_chao="31",
        ipa_symbol="˧˩",
        description="Low falling pitch contour without the creaky voice characteristic of Tone 3.",
        gedney_cells=("B3", "C3", "DL3", "DS3"),
        creaky=False,
        glottalized=False,
        f0_contour_normalized=(0.95, 0.88, 0.78, 0.70),
    ),
    6: KhamyangTone(
        number=6,
        name="Level Rising",
        pitch_chao="35",
        ipa_symbol="˧˥",
        description="Mid level pitch with a clear rising contour toward the syllable end.",
        gedney_cells=("A2",),
        creaky=False,
        glottalized=False,
        f0_contour_normalized=(1.00, 1.04, 1.15, 1.28),
    ),
}

# Gedney Tone Box Mapping (Proto-Tai consonant series x proto-tone categories)
# Gedney boxes: A, B, C (open/sonorant codas), DL (checked long), DS (checked short)
# Rows:
# 1 = Proto-Tai voiceless friction sounds / voiceless aspirated stops
# 2 = Proto-Tai voiceless unaspirated stops
# 3 = Proto-Tai preglottalized / voiced implosives (*ʔb, *ʔd, *ʔj)
# 4 = Proto-Tai voiced obstruents / sonorants (*b, *d, *g, *m, *n, etc.)
GEDNEY_BOX_MAPPING: Dict[Tuple[str, int], int] = {
    ("A", 1): 1,
    ("A", 2): 6,
    ("A", 3): 1,
    ("A", 4): 3,
    ("B", 1): 1,
    ("B", 2): 2,
    ("B", 3): 5,
    ("B", 4): 3,
    ("C", 1): 4,
    ("C", 2): 2,
    ("C", 3): 5,
    ("C", 4): 4,
    ("DL", 1): 4,
    ("DL", 2): 2,
    ("DL", 3): 5,
    ("DL", 4): 4,
    ("DS", 1): 4,
    ("DS", 2): 2,
    ("DS", 3): 5,
    ("DS", 4): 4,
}


def get_tone(tone_num: int) -> KhamyangTone:
    """Returns the KhamyangTone object for a tone number 1-6."""
    if tone_num not in TONES:
        raise ValueError(f"Invalid Tai Khamyang tone number: {tone_num}. Valid tones are 1 to 6.")
    return TONES[tone_num]


def gedney_lookup(category: str, row: int) -> int:
    """
    Looks up modern Tai Khamyang tone from historical Gedney box coordinates.

    Args:
        category: 'A', 'B', 'C', 'DL' (Dead long), or 'DS' (Dead short).
        row: Proto-Tai initial series (1, 2, 3, or 4).

    Returns:
        Khamyang tone number (1-6).
    """
    key = (category.upper(), int(row))
    if key in GEDNEY_BOX_MAPPING:
        return GEDNEY_BOX_MAPPING[key]
    raise KeyError(f"Unknown Gedney box coordinate: {category}{row}")


class ToneSystem:
    """High-level interface for inspecting and converting Khamyang tones."""

    @staticmethod
    def get_all_tones() -> List[KhamyangTone]:
        return list(TONES.values())

    @staticmethod
    def extract_tone(syllable_or_word: str) -> Optional[int]:
        """
        Extracts tone number from Romanized syllable ending with digit (e.g. 'nam6' -> 6).
        """
        if not syllable_or_word:
            return None
        last_char = syllable_or_word.strip()[-1]
        if last_char in "123456":
            return int(last_char)
        return None

    @staticmethod
    def strip_tone(syllable_or_word: str) -> str:
        """Removes trailing tone number from syllable (e.g. 'nam6' -> 'nam')."""
        clean = syllable_or_word.strip()
        if clean and clean[-1] in "123456":
            return clean[:-1]
        return clean

    @staticmethod
    def to_ipa_tone(tone_num: int) -> str:
        """Converts tone number (1-6) to IPA pitch letter contour."""
        return TONES.get(tone_num, TONES[1]).ipa_symbol

    @staticmethod
    def explain_tone(tone_num: int) -> Dict[str, str]:
        """Returns detailed linguistic explanation of the specified tone."""
        t = get_tone(tone_num)
        return {
            "number": str(t.number),
            "name": t.name,
            "pitch_contour": t.pitch_chao,
            "ipa": t.ipa_symbol,
            "description": t.description,
            "creaky_voice": "Yes" if t.creaky else "No",
            "glottal_stop": "Yes" if t.glottalized else "No",
            "gedney_origin": ", ".join(t.gedney_cells),
        }
