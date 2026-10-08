"""
Tai Khamyang (ksu) Language Library — Alias Package
===================================================
Allows developers to import the library using `tai_khamyang` interchangeably with `khamyang`.

Examples:
    >>> import tai_khamyang
    >>> lang = tai_khamyang.Khamyang()
    >>> print(lang.lookup("nam6")[0]["gloss_en"])
    'water, river'

    >>> from tai_khamyang import TaiKhamyang
    >>> lang = TaiKhamyang()

    >>> from tai_khamyang.nlp import KhamyangTokenizer
"""

import sys
import khamyang as _khamyang

# Re-export all primary classes and functions from khamyang
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

# Re-export core submodules
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

# Friendly class alias
TaiKhamyang = Khamyang

# Map submodules so `import tai_khamyang.nlp` works transparently
sys.modules["tai_khamyang.lexicon"] = lexicon
sys.modules["tai_khamyang.nlp"] = nlp
sys.modules["tai_khamyang.phonology"] = phonology
sys.modules["tai_khamyang.transliteration"] = transliteration
sys.modules["tai_khamyang.grammar"] = grammar
sys.modules["tai_khamyang.corpus"] = corpus
sys.modules["tai_khamyang.phrases"] = phrases
sys.modules["tai_khamyang.export"] = export

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
