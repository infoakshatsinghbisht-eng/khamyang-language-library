# Tai Khamyang (`khamyang`) — Comprehensive Developer Guide

Welcome to the **Tai Khamyang Python Developer Guide**. This document is designed for software engineers, computational linguists, and NLP researchers building applications, language preservation platforms, and machine-learning pipelines with `khamyang`.

---

## Table of Contents
1. [Architecture & Design Principles](#1-architecture--design-principles)
2. [Installation & Setup](#2-installation--setup)
3. [Quickstart: The Unified Facade API](#3-quickstart-the-unified-facade-api)
4. [Dictionary & Search APIs](#4-dictionary--search-apis)
5. [NLP Toolkit (`khamyang.nlp`)](#5-nlp-toolkit-khamyangnlp)
6. [Phonetics & The 6-Tone Acoustic Engine](#6-phonetics--the-6-tone-acoustic-engine)
7. [Multi-Script Transliteration](#7-multi-script-transliteration)
8. [Grammar, Syntax & Classifier Engines](#8-grammar-syntax--classifier-engines)
9. [Sub-Corpora Access (Songs, Folklore, Proverbs, Dialogues)](#9-sub-corpora-access)
10. [Archival Audio Metadata & Field Provenance](#10-archival-audio-metadata--field-provenance)
11. [Data Exporters (Anki, CSV, HTML, LaTeX, ELAN)](#11-data-exporters)
12. [CLI Reference](#12-cli-reference)
13. [AI & LLM Integration Patterns](#13-ai--llm-integration-patterns)
14. [Windows Encoding & Best Practices](#14-windows-encoding--best-practices)

---

## 1. Architecture & Design Principles

The library is organized into decoupled domain modules with a high-level facade pattern:

```text
khamyang/
├── khamyang/
│   ├── __init__.py           # Package exports (Khamyang facade + core submodules)
│   ├── facade.py             # High-level unified developer interface (Khamyang)
│   ├── lexicon/              # Dictionary lookups, fuzzy search, Gedney box
│   ├── nlp/                  # Normalizer, Tokenizer, Lemmatizer, POS Tagger, Language Detector
│   ├── phonology/            # 6 tones, IPA pitch contours, syllable parser, synth
│   ├── transliteration/      # Bidirectional Lik Tai <-> Roman <-> Assamese converters
│   ├── grammar/              # Classifiers, Syntax/TAM, Numerals, Kinship, Naming
│   ├── corpus/               # Interlinear glossed texts (IGT), Songs (Fɯn), Exporters
│   ├── phrases/              # Fieldwork phrasebook & dialog elicitation
│   ├── export/               # Anki TSV, CSV, and HTML standalone exporters
│   ├── web/                  # FastAPI + Web Audio API interactive revitalization studio
│   └── data/                 # Packaged JSON databases (lexicon, songs, texts, kinship)
│
├── data/                     # Sub-corpora datasets (JSON, JSONL)
│   ├── proverbs/             # Traditional proverbs (Kham Thum)
│   ├── conversations/        # Multi-turn fieldwork everyday dialogues
│   ├── culture/              # Material culture, architecture & binomial taxa
│   ├── geography/            # Historical toponyms & sacred places
│   ├── audio_metadata/       # PARADISEC / ELAR archival recording index
│   ├── parallel_corpus/      # Aligned tri-lingual sentences (KHY <-> ENG <-> ASM)
│   └── ai/                   # Quarantined instruction datasets (human-verified)
│
├── sources/                  # Source registry and licensing metadata
├── tests/                    # Unit test suite (62 passing tests)
├── pyproject.toml / setup.py # Package metadata & console scripts
└── README.md / STATISTICS.md # Documentation & quality metrics
```

### Core Design Rules
1. **Zero External Heavy Dependencies for Core NLP:** The dictionary, tokenization, POS tagging, normalization, and transliteration require only the Python standard library.
2. **Multi-Script Parity:** Every lexical entity simultaneously provides Romanized form, Lik Tai script, Assamese script, and IPA.
3. **Data Provenance:** Every corpus item carries source IDs (`src_morey2005`, `src_paradisec_sdm03`, etc.) and informant credits.

---

## 2. Installation & Setup

### Requirements
- Python 3.8+ (Compatible with Python 3.9, 3.10, 3.11, 3.12, 3.13)
- Windows, macOS, or Linux

### Install in Editable Development Mode
```bash
git clone https://github.com/khamyang-revitalization/khamyang.git
cd khamyang
pip install -e .
```

### Verify Installation
```bash
python -c "import khamyang; print(khamyang.__version__)"
# Output: 1.0.0
```

---

## 3. Quickstart: The Unified Facade API

The `Khamyang` class acts as the single primary entry point:

```python
from khamyang import Khamyang

# Initialize the facade
lang = Khamyang()

# 1. Dictionary lookup (exact Romanized tone form or script)
entry = lang.lookup("nam6")[0]
print(entry["gloss_en"])    # "water, river"
print(entry["lik_tai"])     # "ၼမ်ႊ"
print(entry["assamese"])    # "নাম⁶"
print(entry["ipa"])         # "[nam˧˥]"

# 2. Semantic search
results = lang.search("buffalo")
for r in results:
    print(r["roman"], r["gloss_en"])  # kwaai1: water buffalo

# 3. Text Normalization
clean_text = lang.normalize("kaw¹ kin¹ khaw³")
print(clean_text)           # "kaw1 kin1 khaw3"

# 4. Transliterate across scripts
lik_tai = lang.to_liktai("kaw1 yu5 maan3 paa1 waai6")
print(lik_tai)              # "ၵဝ် ယူႇ မၢၼ်ႈ ပႃ ဝၢႆး"

# 5. Grammar: Counting with numeral classifiers
phrase = lang.quantify("kwaai1", 2)
print(phrase)               # "kwaai1 sɔŋ1 to1" (two buffaloes)
```

---

## 4. Dictionary & Search APIs

For fine-grained dictionary access, use `khamyang.lexicon`:

```python
from khamyang.lexicon.dictionary import get_dictionary
from khamyang.lexicon.search import fuzzy_search, cognate_search

d = get_dictionary()

# Filter by semantic category (48 available categories)
agriculture_words = d.filter_by_category("agriculture")
print(f"Agriculture terms: {len(agriculture_words)}")

# Filter by tone (1 to 6)
tone4_words = d.filter_by_tone(4)
print(f"Tone 4 glottalized words: {len(tone4_words)}")

# Comparative Tai cognate search
cognates = cognate_search("thai", "nam")
for entry in cognates:
    print(f"Khamyang: {entry.roman} <-> Thai: {entry.cognates.get('thai')}")
```

---

## 5. NLP Toolkit (`khamyang.nlp`)

The package includes lightweight linguistic processors designed for pipeline integration:

### A. Tokenizer
```python
from khamyang.nlp import KhamyangTokenizer

tok = KhamyangTokenizer()
tokens = tok.tokenize("kaw1 kin1 khaw3 yow3.")
print(tokens)  # ['kaw1', 'kin1', 'khaw3', 'yow3']

# Detokenization
sentence = tok.detokenize(tokens)
print(sentence)  # "kaw1 kin1 khaw3 yow3"
```

### B. Normalizer
Handles Unicode NFC normalization, whitespace cleaning, and superscript tone conversion (`¹`..`⁶` $\leftrightarrow$ `1`..`6`):
```python
from khamyang.nlp import KhamyangNormalizer

norm = KhamyangNormalizer()
print(norm.normalize("nam⁶"))           # "nam6"
print(norm.to_superscript_tones("nam6")) # "nam⁶"
```

### C. Part-of-Speech Tagger (Universal Dependencies)
Assigns UD tags (`NOUN`, `VERB`, `ADJ`, `PRON`, `NUM`, `PART`, `ADV`):
```python
from khamyang.nlp import KhamyangPOSTagger

tagger = KhamyangPOSTagger()
tags = tagger.tag(["kaw1", "kin1", "khaw3", "yow3"])
print(tags)
# [('kaw1', 'PRON'), ('kin1', 'VERB'), ('khaw3', 'NOUN'), ('yow3', 'PART')]
```

### D. Lemmatizer
```python
from khamyang.nlp import KhamyangLemmatizer

lem = KhamyangLemmatizer()
print(lem.lemmatize("kin1"))  # "kin1"
```

### E. Language Detector
Detects whether input text is Tai Khamyang (`ksu`), Assamese (`asm`), or English (`eng`):
```python
from khamyang.nlp import KhamyangLanguageDetector

det = KhamyangLanguageDetector()
result = det.detect("kaw1 kin1 khaw3")
print(result)
# {'language': 'ksu', 'confidence': 1.0, 'scores': {'ksu': 3, 'asm': 0, 'eng': 0}}
```

---

## 6. Phonetics & The 6-Tone Acoustic Engine

### The 6 Contrastive Tones
```python
from khamyang.phonology.tones import get_tone, gedney_lookup

# Inspect Tone 4 (High Falling Glottalized)
t4 = get_tone(4)
print(t4.name)            # High Falling Glottalized
print(t4.pitch_chao)      # 54ʔ
print(t4.glottalized)     # True

# Resolve historical Gedney tone boxes (A1-4, B1-4, C1-4, DL1-4, DS1-4)
print(gedney_lookup("A", 1))   # Returns 1 (Tone 1)
print(gedney_lookup("A", 2))   # Returns 6 (Tone 6)
print(gedney_lookup("C", 1))   # Returns 4 (Tone 4)
```

### Syllable Analysis
Deconstructs any syllable into Onset, Medial, Nucleus, Coda, and Tone:
```python
from khamyang.phonology.phonemes import parse_syllable

s = parse_syllable("kwaai1")
print(s.onset)   # 'k'
print(s.medial)  # 'w'
print(s.nucleus) # 'aai'
print(s.tone)    # 1
print(s.ipa)     # '[kwaːi˧˧]'
```

---

## 7. Multi-Script Transliteration

Convert bidirectionally between Romanization, Lik Tai script, Assamese script, and IPA:

```python
from khamyang.transliteration.converter import (
    roman_to_liktai,
    liktai_to_roman,
    roman_to_assamese,
    roman_to_ipa,
)

text = "kaw1 yu5 maan3 paa1 waai6"

print(roman_to_liktai(text))
# ၵဝ် ယူႇ မၢၼ်ႈ ပႃ ဝၢႆး

print(roman_to_assamese(text))
# কাৱ¹ য়ু⁵ মান³ পা¹ ৱাই⁶

print(roman_to_ipa(text))
# [kaw˧˧] [ju˧˩] [maːn˨˩̰] [paː˧˧] [waːi˧˥]
```

---

## 8. Grammar, Syntax & Classifier Engines

### A. Classifier Agreement
```python
from khamyang.grammar.classifiers import ClassifierEngine

# Animals take 'to1'
print(ClassifierEngine.quantify("maa1", 2))   # 'maa1 sɔŋ1 to1' (2 dogs)

# People take 'ko5'
print(ClassifierEngine.quantify("khon1", 3))  # 'khon1 saam1 ko5' (3 people)

# Houses take 'lung1'
print(ClassifierEngine.quantify("hɯn1", 1))   # 'hɯn1 nɯŋ5 lung1' (1 house)
```

### B. Number Engine
```python
from khamyang.grammar.numerals import num_to_khamyang

print(num_to_khamyang(24))                    # 'saaw1 si5'
print(num_to_khamyang(105, script="liktai"))  # 'ပၢၵ်ႇ ႁႃႈ'
```

### C. Traditional Birth-Order Naming
```python
from khamyang.grammar.naming import generate_full_name

name = generate_full_name(order=1, gender="male", personal_name="Deben", clan="Chowlik")
print(name["full_roman"])
# 'Chaw Aai Deben Chowlik'
```

---

## 9. Sub-Corpora Access

Access all specialized corpora through the unified facade or dedicated JSON loaders:

```python
from khamyang import Khamyang

lang = Khamyang()

# 1. Traditional Songs (Fɯn)
songs = lang.songs()
for s in songs:
    print(f"{s['title']} ({s['genre']}): {len(s['stanzas'])} stanzas")

# 2. Interlinear Glossed Texts (IGT Stories)
stories = lang.stories()
first_story = stories[0]
print(first_story["title_en"])
for sentence in first_story["sentences"]:
    print(sentence["roman"])
    print(sentence["gloss"])
    print(sentence["free_en"])

# 3. Traditional Proverbs (Kham Thum)
proverbs = lang.proverbs()
print(proverbs[0]["proverb_khamyang"])
print(proverbs[0]["translation_english"])

# 4. Everyday Dialogues
dialogues = lang.conversations()
for turn in dialogues[0]["turns"]:
    print(f"{turn['speaker']}: {turn['khamyang']} ({turn['english']})")
```

---

## 10. Archival Audio Metadata & Field Provenance

To protect elder copyright and depositor restrictions, original high-resolution audio binaries are indexed via archival URIs:

```python
from khamyang import Khamyang

lang = Khamyang()
recordings = lang.audio_recordings()

for rec in recordings:
    print(f"ID: {rec['id']}")
    print(f"Collection: {rec['archive_collection']}")
    print(f"Collector: {rec['collector']}")
    print(f"Speakers: {[s['name'] for s in rec['speakers']]}")
    print(f"URL: {rec['archive_url']}")
    print("---")
```

---

## 11. Data Exporters

Export the Khamyang dictionary and corpora to external educational and linguistic tools:

```python
from khamyang.export.exporter import (
    export_to_anki_tsv,
    export_to_csv,
    export_to_html,
)

# 1. Spaced Repetition (Anki Deck)
export_to_anki_tsv("khamyang_anki.tsv")

# 2. Tabular Data Science (CSV)
export_to_csv("khamyang_lexicon.csv")

# 3. Interactive Offline HTML Dictionary
export_to_html("dictionary.html")

# 4. Interlinear Texts to LaTeX gb4e / ELAN EAF
from khamyang.corpus.texts import get_corpus
from khamyang.corpus.exporters import export_to_latex, export_to_elan_eaf

corpus = get_corpus()
latex_code = export_to_latex(corpus.get_all()[0])
elan_xml = export_to_elan_eaf(corpus.get_all()[0])
```

---

## 12. CLI Reference

The package installs a `khamyang` command-line executable:

```bash
# Dictionary Lookup
khamyang lookup nam6
khamyang lookup "elephant"

# Filtered Search
khamyang search "rice" --category agriculture
khamyang search "" --tone 3

# Script Transliteration
khamyang transliterate "kaw1 kin1 khaw3" --to liktai
khamyang transliterate "kaw1 kin1 khaw3" --to assamese

# Tonal Pitch Analysis
khamyang tone 4
khamyang tone kwaai1

# Naming Generator
khamyang name --gender m --order 1 --personal "Deben" --clan "Chowlik"

# Numbers
khamyang num 24 --script liktai

# Corpus Statistics
khamyang stats

# Export Formats
khamyang export --format anki --output deck.tsv
khamyang export --format csv --output words.csv
khamyang export --format html --output dict.html

# Launch Web Studio
khamyang web --port 8000
```

---

## 13. AI & LLM Integration Patterns

### Fine-Tuning Machine Translation
Use [`data/parallel_corpus/parallel_corpus.jsonl`](file:///c:/Users/digit_lgfi273/OneDrive/Desktop/Khamyang/data/parallel_corpus/parallel_corpus.jsonl) for supervised fine-tuning:

```python
import json

parallel_pairs = []
with open("data/parallel_corpus/parallel_corpus.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)
        parallel_pairs.append({
            "khamyang": item["khamyang_roman"],
            "lik_tai": item["khamyang_liktai"],
            "english": item["english"],
            "assamese": item["assamese"]
        })
print(f"Loaded {len(parallel_pairs)} verified parallel pairs.")
```

### Instruction Tuning
Access quarantined instruction data in [`data/ai/instruction_dataset.jsonl`](file:///c:/Users/digit_lgfi273/OneDrive/Desktop/Khamyang/data/ai/instruction_dataset.jsonl):
```python
import json

with open("data/ai/instruction_dataset.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        sample = json.loads(line)
        # sample['prompt'], sample['completion'], sample['verification_status']
```

---

## 14. Windows Encoding & Best Practices

1. **Terminal Encoding on Windows:**  
   Windows PowerShell and CMD default to code page 1252, which causes encoding crashes when printing Lik Tai script (`U+1000..U+109F`) or IPA characters (`[ɯː]`, `[˥˦ʔ]`).  
   **Always execute Python scripts using:**
   ```bash
   python -X utf8 your_script.py
   ```
   Or set the environment variable:
   ```powershell
   $env:PYTHONUTF8 = "1"
   ```

2. **Tone Preservation:**  
   Never strip tones (1–6) during normalization unless explicitly conducting unaccented acoustic matching. Tones distinguish minimal pairs (e.g. `maa1` dog vs. `maa3` horse).

---

*For contributions, questions, or field data submissions, please consult [CONTRIBUTING.md](CONTRIBUTING.md) and [CITATION.cff](CITATION.cff).*
