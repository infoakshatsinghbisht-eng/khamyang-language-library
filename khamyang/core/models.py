"""Core data models for Tai Khamyang language entities."""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any


@dataclass
class ExampleSentence:
    """An example sentence demonstrating word usage."""
    khamyang_roman: str
    lik_tai: str = ""
    assamese_script: str = ""
    english: str = ""
    assamese_meaning: str = ""
    literal_gloss: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class Word:
    """Lexical item in Tai Khamyang."""
    id: str
    roman: str
    gloss_en: str
    pos: str
    tone: int
    lik_tai: str = ""
    assamese: str = ""
    ipa: str = ""
    definition_en: str = ""
    gloss_as: str = ""
    definition_as: str = ""
    category: str = "general"
    gedney_box: str = ""
    cognates: Dict[str, str] = field(default_factory=dict)
    examples: List[ExampleSentence] = field(default_factory=list)
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        res = asdict(self)
        res["examples"] = [ex.to_dict() if isinstance(ex, ExampleSentence) else ex for ex in self.examples]
        return res

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Word":
        examples = []
        for ex in data.get("examples", []):
            if isinstance(ex, dict):
                examples.append(ExampleSentence(**ex))
            elif isinstance(ex, ExampleSentence):
                examples.append(ex)
        data_copy = dict(data)
        data_copy["examples"] = examples
        return cls(**data_copy)


@dataclass
class Phrase:
    """Conversational phrase or fieldwork elicitation expression."""
    id: str
    roman: str
    english: str
    category: str
    lik_tai: str = ""
    assamese: str = ""
    ipa: str = ""
    assamese_trans: str = ""
    literal: str = ""
    context: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Phrase":
        return cls(**data)


@dataclass
class GlossUnit:
    """Morpheme and its linguistic gloss."""
    morpheme: str
    gloss: str


@dataclass
class InterlinearUnit:
    """A sentence with interlinear glossing for linguistic research."""
    id: str
    text_roman: str
    lik_tai: str
    assamese_script: str
    morphemes: List[str]
    glosses: List[str]
    free_translation_en: str
    free_translation_as: str
    speaker: str = "Traditional / Elder"
    location: str = "Powaimukh, Assam"
    audio_ref: str = ""
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class FolkText:
    """A cultural narrative, folktale, or chant in Khamyang."""
    id: str
    title_khamyang: str
    title_english: str
    genre: str  # folktale, migration_history, buddhist_chant, oral_history
    informant: str
    village: str
    sentences: List[InterlinearUnit] = field(default_factory=list)
    description: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title_khamyang": self.title_khamyang,
            "title_english": self.title_english,
            "genre": self.genre,
            "informant": self.informant,
            "village": self.village,
            "description": self.description,
            "sentences": [s.to_dict() for s in self.sentences],
        }
