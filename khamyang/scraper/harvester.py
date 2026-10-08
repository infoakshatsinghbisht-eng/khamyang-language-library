"""
Web & Academic Resource Harvester
=================================
Utilities for researchers to scrape, ingest, and harmonize
additional Tai Khamyang lexical items from digital archives,
linguistic fieldwork databases, and comparative Tai datasets.
"""

import json
import csv
import re
from typing import List, Dict, Any, Optional
from khamyang.core.models import Word
from khamyang.transliteration.converter import (
    roman_to_liktai,
    roman_to_assamese,
    roman_to_ipa,
)
from khamyang.phonology.tones import ToneSystem


class LexiconHarvester:
    """Ingests and standardizes lexical records from external research files."""

    @staticmethod
    def ingest_csv(file_path: str, default_category: str = "fieldwork") -> List[Word]:
        """
        Reads CSV field lists containing columns such as:
        'roman', 'gloss_en', 'gloss_as', 'tone', 'pos', 'category'.
        Automatically computes missing Lik Tai, Assamese script, and IPA.
        """
        words: List[Word] = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for idx, row in enumerate(reader, 1):
                roman = row.get("roman", "").strip()
                if not roman:
                    continue

                tone = int(row.get("tone") or ToneSystem.extract_tone(roman) or 1)
                gloss_en = row.get("gloss_en", row.get("english", "")).strip()
                gloss_as = row.get("gloss_as", row.get("assamese", "")).strip()
                pos = row.get("pos", "noun").strip()
                cat = row.get("category", default_category).strip()

                lik_tai = row.get("lik_tai") or roman_to_liktai(roman)
                assamese_s = row.get("assamese_script") or roman_to_assamese(roman)
                ipa = row.get("ipa") or roman_to_ipa(roman)

                w = Word(
                    id=f"harvest_{idx:04d}",
                    roman=roman,
                    gloss_en=gloss_en,
                    pos=pos,
                    tone=tone,
                    lik_tai=lik_tai,
                    assamese=assamese_s,
                    ipa=ipa,
                    definition_en=f"Harvester entry: {gloss_en}",
                    gloss_as=gloss_as,
                    definition_as=f"সংগ্ৰহ কৰা ভাণ্ডাৰ: {gloss_as}",
                    category=cat,
                    notes="Ingested via LexiconHarvester.",
                )
                words.append(w)
        return words

    @staticmethod
    def ingest_toolbox_file(file_path: str) -> List[Word]:
        """
        Parses SIL Toolbox / Shoebox standard format markers (\\lx, \\ge, \\ps, \\xv).
        Commonly used in endangered language archives like ELAR and PARADISEC.
        """
        words: List[Word] = []
        current: Dict[str, str] = {}

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if not line:
                    if "lx" in current:
                        roman = current.get("lx", "")
                        gloss = current.get("ge", "")
                        pos = current.get("ps", "noun")
                        tone = ToneSystem.extract_tone(roman) or 1
                        w = Word(
                            id=f"toolbox_{len(words)+1:04d}",
                            roman=roman,
                            gloss_en=gloss,
                            pos=pos,
                            tone=tone,
                            lik_tai=roman_to_liktai(roman),
                            assamese=roman_to_assamese(roman),
                            ipa=roman_to_ipa(roman),
                            definition_en=gloss,
                            category="toolbox_archive",
                            notes="Imported from SIL Toolbox archive.",
                        )
                        words.append(w)
                        current = {}
                    continue

                if line.startswith("\\"):
                    parts = line.split(maxsplit=1)
                    marker = parts[0][1:]
                    val = parts[1] if len(parts) > 1 else ""
                    current[marker] = val

        return words
