"""
Tai Khamyang Lemmatizer & Stemmer
Resolves lexical surface forms to canonical dictionary lemmas and roots.
"""

from typing import Optional, Dict, Any
from khamyang.lexicon.dictionary import get_dictionary
from khamyang.nlp.normalizer import normalize_roman_tones


class KhamyangLemmatizer:
    """Lemmatizes Tai Khamyang words against the verified lexical database."""

    _dict_cache: Optional[Dict[str, Any]] = None

    @classmethod
    def _get_dict_map(cls) -> Dict[str, Any]:
        if cls._dict_cache is None:
            d = get_dictionary()
            cls._dict_cache = {}
            for w in d.get_all_words():
                cls._dict_cache[w.roman.lower()] = w
                cls._dict_cache[w.lik_tai] = w
                cls._dict_cache[w.assamese] = w
        return cls._dict_cache

    @classmethod
    def lemmatize(cls, token: str) -> str:
        """
        Returns the canonical lemma for a token.
        If the word is already a valid dictionary form, returns it.
        Otherwise strips punctuation or normalizes tones.
        """
        clean = normalize_roman_tones(token.strip()).lower()
        dict_map = cls._get_dict_map()
        if clean in dict_map:
            return dict_map[clean].roman
        # Return normalized form as base fallback
        return clean

    @classmethod
    def get_lemma_info(cls, token: str) -> Optional[Dict[str, Any]]:
        """Returns the full lexical object for a token if found."""
        clean = normalize_roman_tones(token.strip()).lower()
        dict_map = cls._get_dict_map()
        if clean in dict_map:
            return dict_map[clean].to_dict()
        return None
