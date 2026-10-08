"""
Tai Khamyang (ksu) Language Library — Alias Package
===================================================
Allows developers to import the library using `taikhamyang` interchangeably with `khamyang`.
"""

import sys
import khamyang as _khamyang

from khamyang import (
    Khamyang,
    KhamyangDictionary,
    get_dictionary,
    ToneSystem,
    KhamyangTone,
    gedney_lookup,
    transliterate,
    roman_to_liktai,
    liktai_to_roman,
    roman_to_assamese,
    assamese_to_roman,
    roman_to_ipa,
    ClassifierEngine,
    get_birth_name,
    list_birth_names,
    num_to_khamyang,
    khamyang_to_num,
    KhamyangPhrasebook,
    get_phrasebook,
    KhamyangCorpus,
    get_corpus,
    InterlinearGloss,
    SongEngine,
    KinshipEngine,
    CLANS,
    BibliographyManager,
    normalize,
    tokenize,
    detokenize,
    pos_tag,
    detect_language,
    __version__,
    __author__,
    __license__,
)

from khamyang import (
    lexicon,
    nlp,
    phonology,
    transliteration,
    grammar,
    corpus,
    phrases,
    export,
)

TaiKhamyang = Khamyang

sys.modules["taikhamyang.lexicon"] = lexicon
sys.modules["taikhamyang.nlp"] = nlp
sys.modules["taikhamyang.phonology"] = phonology
sys.modules["taikhamyang.transliteration"] = transliteration
sys.modules["taikhamyang.grammar"] = grammar
sys.modules["taikhamyang.corpus"] = corpus
sys.modules["taikhamyang.phrases"] = phrases
sys.modules["taikhamyang.export"] = export

__all__ = [
    "Khamyang",
    "TaiKhamyang",
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
    "SongEngine",
    "KinshipEngine",
    "CLANS",
    "BibliographyManager",
    "normalize",
    "tokenize",
    "detokenize",
    "pos_tag",
    "detect_language",
    "lexicon",
    "nlp",
    "phonology",
    "transliteration",
    "grammar",
    "corpus",
    "phrases",
    "export",
    "__version__",
    "__author__",
    "__license__",
]
