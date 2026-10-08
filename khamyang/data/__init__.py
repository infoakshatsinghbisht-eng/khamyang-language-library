"""Data directory resource paths."""

import os

DATA_DIR = os.path.dirname(os.path.abspath(__file__))
LEXICON_PATH = os.path.join(DATA_DIR, "lexicon.json")
PHRASES_PATH = os.path.join(DATA_DIR, "phrases.json")
TEXTS_PATH = os.path.join(DATA_DIR, "texts.json")

__all__ = ["DATA_DIR", "LEXICON_PATH", "PHRASES_PATH", "TEXTS_PATH"]
