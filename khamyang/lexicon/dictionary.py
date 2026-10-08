"""
Tai Khamyang Dictionary Engine
==============================
Provides high-performance indexing, lookup, filtering, and management
of the Tai Khamyang lexical database.
"""

import json
import os
import random
from typing import Dict, List, Optional, Set, Any
from khamyang.core.models import Word, ExampleSentence
from khamyang.phonology.tones import ToneSystem


DATA_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "lexicon.json")


class KhamyangDictionary:
    """Core Dictionary manager for Tai Khamyang."""

    def __init__(self, data_path: Optional[str] = None):
        self.data_path = data_path or DATA_FILE
        self._words: List[Word] = []
        self._by_id: Dict[str, Word] = {}
        self._by_roman: Dict[str, List[Word]] = {}
        self._by_roman_notone: Dict[str, List[Word]] = {}
        self._by_liktai: Dict[str, List[Word]] = {}
        self._by_assamese: Dict[str, List[Word]] = {}
        self._by_category: Dict[str, List[Word]] = {}
        self._by_tone: Dict[int, List[Word]] = {}
        self._load()

    def _load(self):
        """Loads entries from the JSON database file if present."""
        if os.path.exists(self.data_path):
            with open(self.data_path, "r", encoding="utf-8") as f:
                raw_data = json.load(f)
                for item in raw_data:
                    word = Word.from_dict(item)
                    self.add_word(word, reindex=False)
            self._rebuild_indices()

    def _rebuild_indices(self):
        """Rebuilds internal search indices."""
        self._by_id.clear()
        self._by_roman.clear()
        self._by_roman_notone.clear()
        self._by_liktai.clear()
        self._by_assamese.clear()
        self._by_category.clear()
        self._by_tone.clear()

        for w in self._words:
            # By ID
            self._by_id[w.id] = w

            # By Roman (exact)
            r_lower = w.roman.strip().lower()
            self._by_roman.setdefault(r_lower, []).append(w)

            # By Roman without tone number (e.g., 'nam6' -> 'nam')
            r_notone = ToneSystem.strip_tone(r_lower)
            self._by_roman_notone.setdefault(r_notone, []).append(w)

            # By Lik Tai
            if w.lik_tai:
                self._by_liktai.setdefault(w.lik_tai.strip(), []).append(w)

            # By Assamese
            if w.assamese:
                self._by_assamese.setdefault(w.assamese.strip(), []).append(w)

            # By Category
            self._by_category.setdefault(w.category.lower(), []).append(w)

            # By Tone
            if w.tone in range(1, 7):
                self._by_tone.setdefault(w.tone, []).append(w)

    def add_word(self, word: Word, reindex: bool = True):
        """Adds a new word to the dictionary."""
        self._words.append(word)
        if reindex:
            self._rebuild_indices()

    def get_by_id(self, word_id: str) -> Optional[Word]:
        return self._by_id.get(word_id)

    def lookup(self, term: str) -> List[Word]:
        """
        Fast lookup across Romanization, Lik Tai, Assamese, and English.
        """
        clean = term.strip()
        lower = clean.lower()

        # 1. Exact Roman match
        if lower in self._by_roman:
            return self._by_roman[lower]

        # 2. Tone-stripped Roman match
        notone = ToneSystem.strip_tone(lower)
        if notone in self._by_roman_notone:
            return self._by_roman_notone[notone]

        # 3. Lik Tai match
        if clean in self._by_liktai:
            return self._by_liktai[clean]

        # 4. Assamese match
        if clean in self._by_assamese:
            return self._by_assamese[clean]

        # 5. Gloss lookup
        return self.search(lower)

    def search(
        self,
        query: str,
        category: Optional[str] = None,
        tone: Optional[int] = None,
        limit: int = 50,
    ) -> List[Word]:
        """
        Full-text search across English definitions, Assamese, Roman, and Lik Tai.
        """
        q = query.strip().lower()
        results: List[Tuple_Score] = []

        pool = self._words
        if category:
            pool = self._by_category.get(category.lower(), [])
        if tone:
            pool = [w for w in pool if w.tone == tone]

        for w in pool:
            score = 0
            w_roman = w.roman.lower()
            w_gloss_en = w.gloss_en.lower()
            w_gloss_as = w.gloss_as
            w_def_en = w.definition_en.lower()

            # Exact matches get highest score
            if q == w_roman or q == ToneSystem.strip_tone(w_roman):
                score += 100
            elif q in w_gloss_en.split(", "):
                score += 90
            elif q == w.lik_tai or q == w.assamese:
                score += 85
            elif q in w_roman:
                score += 60
            elif q in w_gloss_en:
                score += 50
            elif q in w_gloss_as:
                score += 45
            elif q in w_def_en:
                score += 20

            if score > 0:
                results.append((score, w))

        # Sort descending by score
        results.sort(key=lambda x: x[0], reverse=True)
        return [w for _, w in results[:limit]]

    def filter_by_category(self, category: str) -> List[Word]:
        return self._by_category.get(category.lower(), [])

    def filter_by_tone(self, tone_num: int) -> List[Word]:
        return self._by_tone.get(tone_num, [])

    def get_swadesh_list(self) -> List[Word]:
        """Returns foundational Swadesh core vocabulary."""
        return [w for w in self._words if w.category in ("nature", "body", "swadesh", "kinship")]

    def random_word(self) -> Optional[Word]:
        """Returns a random word from the dictionary."""
        if not self._words:
            return None
        return random.choice(self._words)

    def get_all_words(self) -> List[Word]:
        return list(self._words)

    def list_categories(self) -> List[str]:
        return sorted(list(self._by_category.keys()))

    def statistics(self) -> Dict[str, Any]:
        """Returns dataset metrics for researchers and developers."""
        tone_counts = {t: len(self._by_tone.get(t, [])) for t in range(1, 7)}
        cat_counts = {cat: len(words) for cat, words in self._by_category.items()}
        return {
            "total_words": len(self._words),
            "total_categories": len(self._by_category),
            "tones_distribution": tone_counts,
            "category_distribution": cat_counts,
        }

    def __len__(self) -> int:
        return len(self._words)

    def __iter__(self):
        return iter(self._words)


# Global singleton instance
_GLOBAL_DICT: Optional[KhamyangDictionary] = None


def get_dictionary() -> KhamyangDictionary:
    """Returns singleton instance of KhamyangDictionary."""
    global _GLOBAL_DICT
    if _GLOBAL_DICT is None:
        _GLOBAL_DICT = KhamyangDictionary()
    return _GLOBAL_DICT


# Helper type for scoring
Tuple_Score = Any
