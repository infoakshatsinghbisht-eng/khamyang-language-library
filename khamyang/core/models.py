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
                ex_filtered = {k: v for k, v in ex.items() if k in ExampleSentence.__dataclass_fields__}
                examples.append(ExampleSentence(**ex_filtered))
            elif isinstance(ex, ExampleSentence):
                examples.append(ex)
        data_copy = {k: v for k, v in data.items() if k in cls.__dataclass_fields__}
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
    text_roman: str = ""
    lik_tai: str = ""
    assamese_script: str = ""
    morphemes: List[str] = field(default_factory=list)
    glosses: List[str] = field(default_factory=list)
    free_translation_en: str = ""
    free_translation_as: str = ""
    speaker: str = "Traditional / Elder"
    location: str = "Powaimukh, Assam"
    audio_ref: str = ""
    notes: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "InterlinearUnit":
        d = dict(data)
        uid = d.get("id") or d.get("unit_id") or ""
        roman = d.get("text_roman") or d.get("romanization") or ""
        tai = d.get("lik_tai") or d.get("surface_tai") or ""
        as_scr = d.get("assamese_script") or d.get("surface_assamese") or ""
        morphs = d.get("morphemes") or []
        gloss = d.get("glosses") or d.get("gloss") or []
        tr_en = d.get("free_translation_en") or d.get("translation_en") or d.get("translation") or ""
        tr_as = d.get("free_translation_as") or d.get("translation_as") or d.get("translation_assamese") or ""
        spk = d.get("speaker") or "Traditional / Elder"
        loc = d.get("location") or "Powaimukh, Assam"
        audio = d.get("audio_ref") or d.get("audio_file") or ""
        notes = d.get("notes") or ""

        return cls(
            id=uid,
            text_roman=roman,
            lik_tai=tai,
            assamese_script=as_scr,
            morphemes=morphs,
            glosses=gloss,
            free_translation_en=tr_en,
            free_translation_as=tr_as,
            speaker=spk,
            location=loc,
            audio_ref=audio,
            notes=notes
        )


@dataclass
class FolkText:
    """A cultural narrative, folktale, chant, or digitalized book in Khamyang."""
    id: str
    title_khamyang: str = ""
    title_english: str = ""
    genre: str = "traditional"  # folktale, migration_history, buddhist_chant, etc.
    informant: str = "Traditional"
    village: str = "Powaimukh"
    sentences: List[InterlinearUnit] = field(default_factory=list)
    description: str = ""
    audio_file: str = ""
    full_translation: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title_khamyang": self.title_khamyang,
            "title_english": self.title_english,
            "genre": self.genre,
            "informant": self.informant,
            "village": self.village,
            "description": self.description,
            "audio_file": self.audio_file,
            "full_translation": self.full_translation,
            "sentences": [s.to_dict() if hasattr(s, "to_dict") else s for s in self.sentences],
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "FolkText":
        raw_sents = data.get("sentences") or data.get("units") or []
        sents = []
        for s in raw_sents:
            if isinstance(s, dict):
                sents.append(InterlinearUnit.from_dict(s))
            elif isinstance(s, InterlinearUnit):
                sents.append(s)

        title_kh = data.get("title_khamyang") or data.get("title_tai") or ""
        title_en = data.get("title_english") or data.get("title") or data.get("id", "")
        genre = data.get("genre") or "traditional"
        informant = data.get("informant") or data.get("author") or "Traditional"
        village = data.get("village") or data.get("category") or "Powaimukh"
        desc = data.get("description") or data.get("notes") or ""
        audio = data.get("audio_file") or ""
        full_tr = data.get("full_translation") or ""

        return cls(
            id=data.get("id") or data.get("book_id", ""),
            title_khamyang=title_kh,
            title_english=title_en,
            genre=genre,
            informant=informant,
            village=village,
            sentences=sents,
            description=desc,
            audio_file=audio,
            full_translation=full_tr
        )

