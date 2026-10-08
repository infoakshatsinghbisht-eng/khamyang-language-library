"""Advanced search and fuzzy matching utilities for Khamyang lexicon."""

import difflib
from typing import List, Dict, Any, Optional
from khamyang.core.models import Word
from khamyang.lexicon.dictionary import get_dictionary


def fuzzy_search(query: str, threshold: float = 0.6, limit: int = 20) -> List[Word]:
    """
    Performs fuzzy search against Romanized words and English meanings.
    Helpful when transcribing uncertain speech from field recordings.
    """
    dictionary = get_dictionary()
    q = query.strip().lower()
    matches = []

    for word in dictionary.get_all_words():
        # Match against Roman
        roman_sim = difflib.SequenceMatcher(None, q, word.roman.lower()).ratio()
        # Match against English gloss
        gloss_sim = difflib.SequenceMatcher(None, q, word.gloss_en.lower()).ratio()
        best_score = max(roman_sim, gloss_sim)

        if best_score >= threshold:
            matches.append((best_score, word))

    matches.sort(key=lambda x: x[0], reverse=True)
    return [w for _, w in matches[:limit]]


def cognate_search(language: str, query: str) -> List[Word]:
    """
    Finds Khamyang words sharing cognates with a related language (e.g., 'phake', 'thai', 'khamti', 'ahom').
    """
    dictionary = get_dictionary()
    lang = language.strip().lower()
    q = query.strip().lower()
    results = []

    for word in dictionary.get_all_words():
        cog_val = word.cognates.get(lang, "").lower()
        if q in cog_val:
            results.append(word)

    return results
