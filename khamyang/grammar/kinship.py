"""
Tai Khamyang Kinship and Traditional Family System
Implements multi-generational relative resolution, birth-order titles,
clan lineage structures, and address etiquette for Tai Khamyang (ksu).
"""

import json
import os
from typing import Dict, List, Optional, Any


CLANS = [
    {
        "clan_id": "chowlik",
        "name_tai": "Chowlik",
        "lik_tai": "ၸဝ်ႈလိၵ်ႈ",
        "assamese": "চৌলিক",
        "ipa": "t͡ɕaːu³³ lik⁵⁴ʔ",
        "meaning": "Lords of Letters / Scribes & Scholars",
        "role": "Traditional custodians of Buddhist scriptures, chronicles (Lik Pung), and astrological manuscripts. Many prominent Powaimukh scholars belong to this clan.",
        "historical_origin": "Descended from the royal scribe lineage of Mung Mau."
    },
    {
        "clan_id": "thomung",
        "name_tai": "Thomung",
        "lik_tai": "ထေႃႈမုင်း",
        "assamese": "থমুং",
        "ipa": "tʰɔː³¹ muŋ³³",
        "meaning": "Lords of the Country / Ministers & Chiefs",
        "role": "Traditional administrative rulers and village chieftains who governed administrative affairs and foreign embassies.",
        "historical_origin": "Descendants of noble state counselors of the ancient Nora kingdom."
    },
    {
        "clan_id": "chaohai",
        "name_tai": "Chaohai",
        "lik_tai": "ၸဝ်ႈႁႆႈ",
        "assamese": "চাওহাই",
        "ipa": "t͡ɕaːu³³ haːi²¹̰",
        "meaning": "Lords of the Uplands / Cultivators of the Clearings",
        "role": "Masters of agriculture, seasonal calendar calculations, and paddy harvesting ceremonies.",
        "historical_origin": "Associated with ancestral highland cultivation settlements."
    },
    {
        "clan_id": "lungking",
        "name_tai": "Lungking",
        "lik_tai": "လုင်ၵိင်ႇ",
        "assamese_script": "লুংকিম",
        "assamese": "লুংকিম / লুংকিং",
        "ipa": "luŋ³³ kiŋ³¹",
        "meaning": "Ancient Lineage Branch",
        "role": "Custodians of ancestral spirit altars (Phi Dam) and clan genealogies.",
        "historical_origin": "One of the earliest documented Nora groups crossing the Patkai range."
    },
    {
        "clan_id": "pailung",
        "name_tai": "Pailung",
        "lik_tai": "ပၢႆလုင်",
        "assamese": "পাইলোং",
        "ipa": "paːi³³ luŋ³³",
        "meaning": "Commanders / Lineage Leaders",
        "role": "Traditional military defense leaders, border guides, and elephant handlers.",
        "historical_origin": "Militarized vanguard clan during early Tai migrations."
    },
    {
        "clan_id": "chowlu",
        "name_tai": "Chowlu",
        "lik_tai": "ၸဝ်ႈလူႇ",
        "assamese": "চৌলু",
        "ipa": "t͡ɕaːu³³ luː³¹",
        "meaning": "Lords of Ritual Offerings",
        "role": "Organizers of community monastery feasts, Sangken water libations, and Kathina robes.",
        "historical_origin": "Specialized ritual lineage linked to Buddhist temple foundations."
    }
]


class KinshipEngine:
    """
    Solves and manages Tai Khamyang kinship relations, family tree logic,
    and traditional clan lineage systems.
    """

    _data_cache: Optional[List[Dict[str, Any]]] = None

    @classmethod
    def _load_data(cls) -> List[Dict[str, Any]]:
        if cls._data_cache is None:
            path = os.path.join(os.path.dirname(__file__), "..", "data", "kinship.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    cls._data_cache = json.load(f)
            else:
                cls._data_cache = []
        return cls._data_cache

    @classmethod
    def all_terms(cls) -> List[Dict[str, Any]]:
        """Returns all registered kinship terms."""
        return cls._load_data()

    @classmethod
    def resolve(cls, relation_code: str) -> Optional[Dict[str, Any]]:
        """
        Resolves a standard kinship genealogical code to a Tai Khamyang term.
        Supported codes include:
        Fa, Mo, FaFa, FaMo, MoFa, MoMo,
        FaElBr, FaYoBr, MoElSi, MoYoSi, MoYoBr,
        ElBr, ElSi, YoBr, YoSi,
        Hu, Wi,
        So, Da,
        SoWi, DaHu,
        ElSiHu, YoSiHu, ElBrWi, YoBrWi,
        FaFaFa, FaFaMo,
        SoSo, DaSo, etc.
        """
        code = relation_code.strip()
        data = cls._load_data()

        # Direct code match
        for entry in data:
            if code in entry.get("relation_codes", []):
                return entry

        # Fallback normalizations
        code_map = {
            "father": "Fa",
            "mother": "Mo",
            "grandfather": "FaFa",
            "grandmother": "FaMo",
            "paternal_grandfather": "FaFa",
            "maternal_grandfather": "MoFa",
            "paternal_grandmother": "FaMo",
            "maternal_grandmother": "MoMo",
            "elder_brother": "ElBr",
            "younger_brother": "YoBr",
            "elder_sister": "ElSi",
            "younger_sister": "YoSi",
            "husband": "Hu",
            "wife": "Wi",
            "son": "So",
            "daughter": "Da",
            "son_in_law": "DaHu",
            "daughter_in_law": "SoWi",
            "uncle": "FaYoBr",
            "aunt": "MoYoSi",
        }
        normalized = code_map.get(code.lower())
        if normalized:
            for entry in data:
                if normalized in entry.get("relation_codes", []):
                    return entry

        return None

    @classmethod
    def lookup(cls, query: str) -> List[Dict[str, Any]]:
        """Searches kinship data across Romanized Tai, English, Assamese, or IPA."""
        q = query.strip().lower()
        results = []
        for entry in cls._load_data():
            if (
                q in entry.get("khamyang_roman", "").lower()
                or q in entry.get("english", "").lower()
                or q in entry.get("assamese", "").lower()
                or q in entry.get("lik_tai", "")
                or q in entry.get("assamese_script", "").lower()
                or any(q == code.lower() for code in entry.get("relation_codes", []))
            ):
                results.append(entry)
        return results

    @classmethod
    def list_by_generation(cls, generation_level: int) -> List[Dict[str, Any]]:
        """
        Returns all terms belonging to a given generation relative to Ego (0):
        +3: Great-grandparents
        +2: Grandparents
        +1: Parents, Uncles, Aunts, In-laws
         0: Ego, Siblings, Spouses, In-laws
        -1: Children, Nephews, Nieces, Children-in-law
        -2: Grandchildren
        -3: Great-grandchildren
        """
        return [e for e in cls._load_data() if e.get("generation") == generation_level]

    @classmethod
    def list_clans(cls) -> List[Dict[str, Any]]:
        """Returns the traditional Tai Khamyang clans and their roles."""
        return CLANS

    @classmethod
    def get_clan(cls, clan_id: str) -> Optional[Dict[str, Any]]:
        """Gets information for a specific clan."""
        cid = clan_id.strip().lower()
        for c in CLANS:
            if c["clan_id"] == cid or c["name_tai"].lower() == cid or c["assamese"] == cid:
                return c
        return None

    @classmethod
    def explain_relationship(cls, code: str) -> str:
        """Generates a human-readable explanation of the kinship term and cultural etiquette."""
        term = cls.resolve(code)
        if not term:
            return f"No kinship mapping found for relation '{code}'."
        lines = [
            f"=== Tai Khamyang Kinship: {term['english'].title()} ===",
            f"Khamyang (Roman): {term['khamyang_roman']}",
            f"Lik Tai Script:   {term['lik_tai']}",
            f"Assamese Script:  {term['assamese_script']}",
            f"IPA Tone:         /{term['ipa']}/ (Tone {term['tone']})",
            f"Assamese:         {term['assamese']}",
            f"Generation:       {term['generation']} ({'Ascending' if term['generation'] > 0 else 'Descending' if term['generation'] < 0 else 'Ego Generation'})",
            f"Lineage:          {term['line'].capitalize()} ({term['side'].capitalize()})",
            f"Address Form:     '{term['address_term']}'",
            f"Cultural Notes:   {term['cultural_notes']}"
        ]
        return "\n".join(lines)
