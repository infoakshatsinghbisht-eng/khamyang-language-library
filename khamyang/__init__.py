"""
Tai Khamyang (ksu) Language Library
===================================
A comprehensive Python library for the revitalization, documentation,
and computational processing of the critically endangered Tai Khamyang
language (ISO 639-3: ksu, Glottolog: kham1282) spoken in Assam, India.
"""

from khamyang.version import __version__, __author__, __license__
from khamyang.lexicon.dictionary import KhamyangDictionary, get_dictionary
from khamyang.phonology.tones import ToneSystem, KhamyangTone, gedney_lookup
from khamyang.transliteration.converter import (
    transliterate,
    roman_to_liktai,
    liktai_to_roman,
    roman_to_assamese,
    assamese_to_roman,
    roman_to_ipa,
)
from khamyang.grammar.classifiers import ClassifierEngine
from khamyang.grammar.naming import get_birth_name, list_birth_names
from khamyang.grammar.numerals import num_to_khamyang, khamyang_to_num
from khamyang.phrases.phrasebook import KhamyangPhrasebook, get_phrasebook
from khamyang.corpus.texts import KhamyangCorpus, get_corpus
from khamyang.corpus.igt import InterlinearGloss

__all__ = [
    "__version__",
    "__author__",
    "__license__",
    "KhamyangDictionary",
    "get_dictionary",
    "ToneSystem",
    "KhamyangTone",
    "gedney_lookup",
    "transliterate",
    "roman_to_liktai",
    "liktai_to_roman",
    "roman_to_assamese",
    "assamese_to_roman",
    "roman_to_ipa",
    "ClassifierEngine",
    "get_birth_name",
    "list_birth_names",
    "num_to_khamyang",
    "khamyang_to_num",
    "KhamyangPhrasebook",
    "get_phrasebook",
    "KhamyangCorpus",
    "get_corpus",
    "InterlinearGloss",
]
