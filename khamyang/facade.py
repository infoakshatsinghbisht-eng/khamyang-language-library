"""
Unified Developer & Researcher Facade for the Tai Khamyang Language Library.
Provides intuitive, one-stop access to dictionary, phonology, transliteration,
grammar, kinship, folklore, songs, proverbs, audio records, and NLP tools.
"""

import os
import json
from typing import List, Dict, Any, Optional

from khamyang.lexicon.dictionary import get_dictionary
from khamyang.phonology.tones import gedney_lookup, ToneSystem
from khamyang.transliteration.converter import (
    transliterate,
    roman_to_liktai,
    liktai_to_roman,
    roman_to_assamese,
    assamese_to_roman,
    roman_to_ipa,
)
from khamyang.grammar.classifiers import ClassifierEngine
from khamyang.grammar.naming import generate_full_name, list_birth_names
from khamyang.grammar.kinship import KinshipEngine
from khamyang.corpus.texts import get_corpus
from khamyang.corpus.songs import SongEngine
from khamyang.scraper.downloader import BibliographyManager
from khamyang.nlp import (
    normalize,
    tokenize,
    detokenize,
    pos_tag,
    detect_language,
)


from khamyang.version import (
    __version__,
    __author__,
    __copyright__,
    __website__,
    AUTHOR_CREDITS,
    get_credits_text,
)


class Khamyang:
    """
    Master interface for the Tai Khamyang Computational Language Platform.
    
    Authored, Architected & Preserved by Akshat Singh Bisht (https://akshatsinghbisht.com/).
    
    Usage:
        >>> from khamyang import Khamyang
        >>> lang = Khamyang()
        >>> lang.print_credits()  # Display author credit & attribution
        >>> lang.lookup("nam6")
        >>> lang.kinship("FaElBr")
        >>> lang.quantify("kwaai1", 2)
        >>> lang.tokenize("pu5 yaa3 haw1 khao5 maa1")
        >>> lang.detect_language("ၵႂၢႆးမီႈပၺ်ၺႃ")
    """

    def __init__(self):
        self._dict = get_dictionary()
        self._corpus = get_corpus()
        self._data_dir = os.path.join(os.path.dirname(__file__), "data")
        self._root_data_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))
        self.author = __author__
        self.copyright = __copyright__
        self.website = __website__
        self.author_info = AUTHOR_CREDITS

    @property
    def credits(self) -> str:
        """Returns the mandatory author credit notice and attribution text."""
        return get_credits_text()

    def get_credits(self) -> str:
        """Returns the formatted author credits and citation instructions."""
        return get_credits_text()

    def print_credits(self) -> None:
        """Prints the full author credits and preservation struggle notice to stdout."""
        print(get_credits_text())

    # --- DICTIONARY & SEARCH ---
    def lookup(self, term: str) -> List[Any]:
        """Look up a word across Romanized, Lik Tai, Assamese, or English."""
        return self._dict.lookup(term)

    def search(self, query: str, category: Optional[str] = None, tone: Optional[int] = None, limit: int = 50) -> List[Any]:
        """Search words with optional category and tone filters."""
        return self._dict.search(query, category=category, tone=tone, limit=limit)

    def translate(self, text: str, target: str = "en") -> Optional[str]:
        """Translates single words or known parallel sentences."""
        # Check dictionary
        res = self._dict.lookup(text)
        if res:
            if target == "en":
                return res[0].gloss_en
            elif target in ("as", "assamese"):
                return res[0].gloss_as
        return None

    # --- SCRIPT & TRANSLITERATION ---
    def to_liktai(self, text: str) -> str:
        """Converts Romanized Khamyang text to Lik Tai script."""
        return roman_to_liktai(text)

    def to_roman(self, text: str) -> str:
        """Converts Lik Tai or Assamese text to standard Romanized form."""
        return liktai_to_roman(text)

    def to_assamese(self, text: str) -> str:
        """Converts Romanized text to Assamese script with tone marks."""
        return roman_to_assamese(text)

    def to_ipa(self, text: str) -> str:
        """Converts Romanized text to International Phonetic Alphabet (IPA)."""
        return roman_to_ipa(text)

    def transliterate(self, text: str, source: str = "roman", target: str = "liktai") -> str:
        """Bidirectional script transliterator."""
        return transliterate(text, source=source, target=target)

    # --- PHONOLOGY & TONES ---
    def tone_info(self, tone_number: int) -> Dict[str, Any]:
        """Returns acoustic metrics, Chao pitch, and description for a tone (1 to 6)."""
        return ToneSystem.get_tone_metrics(tone_number)

    def gedney_box(self, initial_class: str, proto_tone: str) -> Dict[str, Any]:
        """Calculates tone outcome in Gedney's 20-box tone matrix."""
        return gedney_lookup(initial_class, proto_tone)

    # --- GRAMMAR & KINSHIP ---
    def quantify(self, noun: str, count: int) -> str:
        """Generates quantified noun phrase in Noun + Numeral + Classifier order."""
        return ClassifierEngine.quantify(noun, count)

    def kinship(self, relation_code: str) -> Optional[Dict[str, Any]]:
        """Resolves a genealogical relation code (e.g. 'FaElBr', 'MoFa', 'YoBr') to Tai term."""
        return KinshipEngine.resolve(relation_code)

    def clans(self) -> List[Dict[str, Any]]:
        """Returns the 6 historical Nora clans and their traditional roles."""
        return KinshipEngine.list_clans()

    def birth_name(self, order: int, gender: str = "male", personal_name: str = "", clan: str = "Chowlik") -> Dict[str, Any]:
        """Generates a complete birth-order name with clan surname."""
        return generate_full_name(order, gender, personal_name=personal_name, clan=clan)

    # --- ORAL LITERATURE, SONGS & FOLKLORE ---
    def songs(self) -> List[Dict[str, Any]]:
        """Returns all documented traditional songs (Fɯn)."""
        return SongEngine.all_songs()

    def song(self, song_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves a specific song by ID."""
        return SongEngine.get_song(song_id)

    def stories(self) -> List[Any]:
        """Returns all annotated interlinear glossed folk texts (IGT)."""
        return self._corpus.get_all()

    def books(self) -> List[Dict[str, Any]]:
        """Returns summarized catalog of all digitalized books and texts."""
        return self._corpus.list_books()

    def book(self, book_id: str) -> Optional[Any]:
        """Retrieves a digitalized book by its identifier."""
        return self._corpus.get_book(book_id)

    def read_book(self, book_id: str) -> str:
        """Renders an authentic digitalized book in readable markdown format."""
        return self._corpus.read_book(book_id)

    def _resolve_data_path(self, subpath: str) -> Optional[str]:
        """Resolves path from packaged corpora or repository root."""
        pkg_path = os.path.join(os.path.dirname(__file__), "corpora", subpath)
        if os.path.exists(pkg_path):
            return pkg_path
        root_path = os.path.join(self._root_data_dir, subpath)
        if os.path.exists(root_path):
            return root_path
        return None

    def proverbs(self) -> List[Dict[str, Any]]:
        """Returns authentic Tai Khamyang proverbs and sayings."""
        path = self._resolve_data_path(os.path.join("proverbs", "proverbs.json"))
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def conversations(self) -> List[Dict[str, Any]]:
        """Returns multi-turn everyday conversation dialogs."""
        path = self._resolve_data_path(os.path.join("conversations", "conversations.json"))
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def culture(self) -> Dict[str, Any]:
        """Returns material culture, ethnobotany, and festival records."""
        path = self._resolve_data_path(os.path.join("culture", "material_culture.json"))
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return {}

    def geography(self) -> List[Dict[str, Any]]:
        """Returns traditional toponyms, sacred rivers, and historical sites."""
        path = self._resolve_data_path(os.path.join("geography", "geography.json"))
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def audio_records(self) -> List[Dict[str, Any]]:
        """Returns catalog of documented audio recordings in PARADISEC & ELAR."""
        path = self._resolve_data_path(os.path.join("audio_metadata", "audio_index.json"))
        if path and os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    # --- NLP & AI TOOLS ---
    def normalize(self, text: str) -> str:
        """Unicode and tone normalizer."""
        return normalize(text)

    def tokenize(self, text: str) -> List[str]:
        """Multi-script word/syllable tokenizer."""
        return tokenize(text)

    def detokenize(self, tokens: List[str]) -> str:
        """Detokenizer."""
        return detokenize(tokens)

    def pos_tag(self, text: str) -> List[Any]:
        """Universal Dependencies POS tagger."""
        return pos_tag(text)

    def detect_language(self, text: str) -> Dict[str, Any]:
        """Language identification."""
        return detect_language(text)

    # --- SOURCES & CITATIONS ---
    def sources(self) -> List[Dict[str, Any]]:
        """Returns the primary source registry."""
        pkg_src = os.path.join(os.path.dirname(__file__), "corpora", "sources", "source_registry.json")
        if os.path.exists(pkg_src):
            with open(pkg_src, "r", encoding="utf-8") as f:
                return json.load(f)
        root_src = os.path.join(os.path.dirname(__file__), "..", "sources", "source_registry.json")
        if os.path.exists(root_src):
            with open(root_src, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def bibliography(self) -> List[Dict[str, Any]]:
        """Returns all scholarly bibliographic entries."""
        return BibliographyManager.all_entries()

    def export_bibtex(self) -> str:
        """Exports all references in BibTeX format."""
        return BibliographyManager.export_all_bibtex()

    # --- METRICS & STATS ---
    def stats(self) -> Dict[str, Any]:
        """Calculates comprehensive database statistics."""
        d_stats = self._dict.statistics()
        return {
            "author": __author__,
            "author_url": __website__,
            "copyright": __copyright__,
            "citation": f"{__author__}. (2026). Khamyang: A Python Language Library and Revitalization Platform for Tai Khamyang (ksu) (v{__version__}). {__website__}",
            "credits": f"Authored and Preserved by {__author__} ({__website__})",
            "lexical_entries": d_stats["total_words"],
            "categories": d_stats["total_categories"],
            "tones_distribution": d_stats["tones_distribution"],
            "traditional_songs": len(self.songs()),
            "stories_and_folktales": len(self.stories()),
            "proverbs_and_sayings": len(self.proverbs()),
            "conversations": len(self.conversations()),
            "audio_recordings_indexed": len(self.audio_records()),
            "geographic_toponyms": len(self.geography()),
            "scholarly_sources": len(self.sources()),
        }

    @property
    def metadata(self) -> Dict[str, Any]:
        """Returns library metadata, author information, and licensing."""
        return {
            "name": "khamyang",
            "version": __version__,
            "author": __author__,
            "website": __website__,
            "copyright": __copyright__,
            "author_profile": AUTHOR_CREDITS,
            "license": "MIT with Mandatory Author Attribution",
        }

    def __repr__(self) -> str:
        return f"<Khamyang v{__version__} (Authored & Preserved by {__author__} - {__website__})>"

    def __str__(self) -> str:
        return (
            f"Tai Khamyang Language Library v{__version__}\n"
            f"Authored, Architected & Preserved by: {__author__} ({__website__})\n"
            f"Copyright: {__copyright__}"
        )

