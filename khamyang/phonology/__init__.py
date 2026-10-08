"""Phonology module initialization."""

from khamyang.phonology.tones import (
    KhamyangTone,
    TONES,
    ToneSystem,
    get_tone,
    gedney_lookup,
)
from khamyang.phonology.phonemes import (
    Consonant,
    Vowel,
    CONSONANTS,
    VOWELS,
    SyllableStructure,
    parse_syllable,
)
from khamyang.phonology.synth import (
    generate_tone_audio_params,
    get_all_tone_audio_profiles,
)

__all__ = [
    "KhamyangTone",
    "TONES",
    "ToneSystem",
    "get_tone",
    "gedney_lookup",
    "Consonant",
    "Vowel",
    "CONSONANTS",
    "VOWELS",
    "SyllableStructure",
    "parse_syllable",
    "generate_tone_audio_params",
    "get_all_tone_audio_profiles",
]
