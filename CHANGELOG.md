# Changelog

All notable changes to the **Tai Khamyang Language Library (`khamyang`)** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-10-08

### Added
- **Master Lexicon (1,099 authentic words):**
  - Full orthographic support across Lik Tai (Unicode Myanmar Extended-A), Romanization with tone markers 1–6, Assamese script, and International Phonetic Alphabet (IPA).
  - 6-Tone phonological classification with Gedney box coordinates (A1..DS4) and historical Tai cognates (Phake, Khamti, Ahom, Shan, Thai).
- **Phonology & 6-Tone Synthesizer:**
  - Full acoustic model implementation based on Stephen Morey (2005, 2008).
  - Web Audio API F0 frequency curve parameters for in-browser tone simulation.
- **Orthography & Transliteration:**
  - Bidirectional transliterator between Roman, Lik Tai, Assamese, and IPA.
- **Traditional Songs (*Fɯn*) Engine:**
  - 6 documented songs with parallel stanzas, glosses, and informant attributions (Wedding ballad *Fɯn Ao Nang*, Lullaby *Fɯn Nɔn Luk*, Rice pounding song *Fɯn Tam Khaw*, Sangken Water Festival ballad *Fɯn Poy Sangken*, Courting lyric *Fɯn Cholim / Kham Soi Yoi*, Rice transplanting chant *Fɯn Dam Khaw*).
- **Folklore & Oral History Corpus:**
  - Leipzig-compliant 5-line Interlinear Glossed Texts (IGT) for Patkai migration chronicle, Buffalo & Tiger moral tale, Sangken blessing chant, Hong Khwan soul-calling chant, and Mung Mau origin legend.
- **Kinship & Traditional Family System:**
  - Multi-generational kinship engine resolving relationships across generations (-3 to +3).
  - Documentation of the six historical Nora clans (*Chowlik*, *Thomung*, *Chaohai*, *Lungking*, *Pailung*, *Chowlu*).
- **Authentic Proverbs, Riddles & Sayings Corpus:**
  - 6 traditional moral proverbs (*Kham1 Thum3*) with morphemic segmentation and cultural context.
- **Conversational Corpus:**
  - Multi-turn authentic dialogue recordings in Powaimukh village settings.
- **Cultural & Botanical Corpus:**
  - Material culture documentation (stilted houses *hɯn1 thaai1*, frame looms, hearths) and botanical flora/fauna with binomial Latin scientific names (*Oryza sativa*, *Piper betle*, *Areca catechu*, *Calamus rotang*).
- **Audio Catalog Index:**
  - Curated metadata index for primary field recordings in PARADISEC (`SDM03`, `SDM07`) and ELAR deposits.
- **Natural Language Processing (NLP) Toolkit (`khamyang.nlp`):**
  - Multi-script tokenizer, Unicode normalizer, Universal Dependencies POS tagger, and language identification module.
- **Unified Developer Facade (`from khamyang import Khamyang`):**
  - One-stop interface for developers, linguists, and researchers.
- **CLI & Web Revitalization Platform:**
  - Rich CLI commands (`lookup`, `tone`, `transliterate`, `kinship`, `song`, `biblio`, `stats`, `export`, `web`).
  - Interactive FastAPI web platform with 10 tabs, virtual Lik Tai keyboard, and audio player.
- **Scholarly Bibliography & Download Downloader:**
  - 17 academic books, journal papers, and archives with automated BibTeX and Markdown exports.
- **AI Datasets:**
  - Aligned human-verified parallel corpus and instruction-response datasets.
