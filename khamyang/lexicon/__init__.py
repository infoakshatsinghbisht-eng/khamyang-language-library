"""Lexicon module initialization."""

from khamyang.lexicon.dictionary import (
    KhamyangDictionary,
    get_dictionary,
)
from khamyang.lexicon.search import (
    fuzzy_search,
    cognate_search,
)

__all__ = [
    "KhamyangDictionary",
    "get_dictionary",
    "fuzzy_search",
    "cognate_search",
]
