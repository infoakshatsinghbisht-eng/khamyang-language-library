"""
Tai Khamyang Traditional Birth-Order Naming System
==================================================
The Khamyang people of Assam have preserved an ancient Tai birth-order
naming convention for children, documented in ELDP materials and community archives.
Children receive a birth-order title for 1st through 8th born,
often paired with an individual name and clan surname (e.g., Thomung, Chowlik).
"""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass(frozen=True)
class BirthName:
    order: int
    gender: str
    name_roman: str
    lik_tai: str
    assamese: str
    meaning: str


MALE_BIRTH_NAMES: Dict[int, BirthName] = {
    1: BirthName(1, "male", "Aai", "ဢၢႆႈ", "আই", "First-born son (eldest son)"),
    2: BirthName(2, "male", "Ngi", "ငီႈ", "ঙী", "Second-born son"),
    3: BirthName(3, "male", "Saam", "သၢမ်", "সাম", "Third-born son"),
    4: BirthName(4, "male", "Sai", "သၢႆ", "সাই", "Fourth-born son"),
    5: BirthName(5, "male", "Ngow", "ငဝ်ႈ", "ঙও", "Fifth-born son"),
    6: BirthName(6, "male", "Nuk", "ၼုၵ်ႈ", "নুক", "Sixth-born son"),
    7: BirthName(7, "male", "Naak", "ၼၢၵ်ႈ", "নাক", "Seventh-born son"),
    8: BirthName(8, "male", "Koy", "ၵွႆ", "কয়", "Eighth-born son (youngest son)"),
}

FEMALE_BIRTH_NAMES: Dict[int, BirthName] = {
    1: BirthName(1, "female", "Ye", "ယေႈ", "য়ে", "First-born daughter (eldest daughter)"),
    2: BirthName(2, "female", "Ee", "ဢီႇ", "ঈ", "Second-born daughter"),
    3: BirthName(3, "female", "Aam", "ဢၢမ်", "আম", "Third-born daughter"),
    4: BirthName(4, "female", "Ai", "ဢၢႆ", "আই", "Fourth-born daughter"),
    5: BirthName(5, "female", "Wo", "ဝူဝ်", "ৱো", "Fifth-born daughter"),
    6: BirthName(6, "female", "Uk", "ဢုၵ်ႈ", "উক", "Sixth-born daughter"),
    7: BirthName(7, "female", "Eit", "ဢိတ်ႇ", "ইত", "Seventh-born daughter"),
    8: BirthName(8, "female", "Aat", "ဢၢတ်ႈ", "আত", "Eighth-born daughter (youngest daughter)"),
}

# Historic and traditional clan names of the Khamyang (Nora) community
KHAMYANG_CLANS: List[Dict[str, str]] = [
    {
        "clan": "Thomung",
        "variant": "Thaomung",
        "lik_tai": "ထၢဝ်ႈမိူင်း",
        "assamese": "থমুং",
        "significance": "Historic royal/ministerial clan; custodians of chieftaincy (e.g., Bhogeswar Thomung).",
    },
    {
        "clan": "Chowlik",
        "variant": "Chaulik",
        "lik_tai": "ၸဝ်ႈလိၵ်ႈ",
        "assamese": "চৌলিক",
        "significance": "Traditional literate/scribal clan, custodians of manuscripts and religious texts (e.g., Chaw Sa Myat Chowlik, Deben Chowlik).",
    },
    {
        "clan": "Chaohai",
        "variant": "Chowhai",
        "lik_tai": "ၸဝ်ႈႁႆး",
        "assamese": "চৌহাই",
        "significance": "Traditional agricultural leaders and village lineage.",
    },
    {
        "clan": "Pangyok",
        "variant": "Pangyauk",
        "lik_tai": "ပၢင်ယွၵ်း",
        "assamese": "পাংয়ক",
        "significance": "Historical clan tracing migration from Mung Mau through Patkai.",
    },
    {
        "clan": "Wailong",
        "variant": "Waylong",
        "lik_tai": "ဝၢႆးလူင်",
        "assamese": "ৱাইলং",
        "significance": "Elder council clan, settled in Powaimukh.",
    },
]


def get_birth_name(order: int, gender: str = "male") -> Optional[BirthName]:
    """
    Returns traditional birth-order name.
    Args:
        order: Birth order (1 to 8).
        gender: 'male' ('m') or 'female' ('f').
    """
    g = gender.strip().lower()
    if g in ("m", "male", "son"):
        return MALE_BIRTH_NAMES.get(order)
    elif g in ("f", "female", "daughter"):
        return FEMALE_BIRTH_NAMES.get(order)
    raise ValueError(f"Invalid gender '{gender}'. Use 'male' or 'female'.")


def list_birth_names(gender: Optional[str] = None) -> List[BirthName]:
    """Lists all birth-order names, optionally filtered by gender."""
    if gender:
        g = gender.strip().lower()
        if g in ("m", "male"):
            return list(MALE_BIRTH_NAMES.values())
        elif g in ("f", "female"):
            return list(FEMALE_BIRTH_NAMES.values())
    return list(MALE_BIRTH_NAMES.values()) + list(FEMALE_BIRTH_NAMES.values())


def generate_full_name(order: int, gender: str, personal_name: str = "", clan: str = "Thomung") -> Dict[str, str]:
    """Generates an authentic traditional Khamyang full name."""
    birth = get_birth_name(order, gender)
    if not birth:
        raise ValueError(f"Birth order must be 1 to 8, got {order}")
    honorific = "Chaw" if gender.lower() in ("m", "male") else "Nang"
    parts = [honorific, birth.name_roman]
    if personal_name:
        parts.append(personal_name)
    parts.append(clan)
    full_roman = " ".join(parts)
    return {
        "full_roman": full_roman,
        "honorific": honorific,
        "birth_order_name": birth.name_roman,
        "personal_name": personal_name,
        "clan": clan,
        "gender": birth.gender,
        "order": str(order),
        "meaning": birth.meaning,
    }
