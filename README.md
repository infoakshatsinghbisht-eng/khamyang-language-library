# Tai Khamyang (`khamyang`) Language Library ꩯမ်ထႃႆၶင်

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/khamyang/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Endangered Status: Critical](https://img.shields.io/badge/UNESCO-Critically%20Endangered-red.svg)](https://en.wikipedia.org/wiki/Khamyang_language)
[![ISO 639-3: ksu](https://img.shields.io/badge/ISO%20639--3-ksu-orange.svg)](https://iso639-3.sil.org/code/ksu)
[![Glottolog: kham1282](https://img.shields.io/badge/Glottolog-kham1282-lightgrey.svg)](https://glottolog.org/resource/languoid/id/kham1282)

A comprehensive Python language processing library, revitalization toolkit, and computational dataset for **Tai Khamyang** (also known as *Khamjang* or *Nora*), a critically endangered Southwestern Tai language spoken by a small community in Assam, Northeast India (predominantly in **Powaimukh** village near Margherita, Tinsukia district).

The primary objective of this library is **language preservation, computational accessibility, and fieldwork empowerment**:
- **For Developers:** Build dictionary apps, translation systems, chat assistants, learning platforms, educational games, and text-to-speech tools.
- **For Linguists & Field Researchers:** Search phonetic and lexical databases, analyze the 6-tone phonological system with Gedney tone boxes, parse classifier constructions, query historical cognates, and export interlinear glossed texts (IGT) to LaTeX, FLEx/LIFT, and ELAN.
- **For the Community & Language Learners:** Access digital phrasebooks, practice traditional birth-order naming conventions, learn the Lik Tai script via virtual keyboards, and listen to synthesized pitch contours of the 6 lexical tones.

---

## Table of Contents
1. [Language Background & Sociolinguistics](#language-background--sociolinguistics)
2. [Phonological & Tonal Architecture](#phonological--tonal-architecture)
3. [Writing Systems & Orthography](#writing-systems--orthography)
4. [Installation](#installation)
5. [Quickstart Guide](#quickstart-guide)
6. [Core Modules & Python API](#core-modules--python-api)
   - [Dictionary & Lexical Search](#1-dictionary--lexical-search)
   - [Phonology & 6-Tone Engine](#2-phonology--6-tone-engine)
   - [Bidirectional Script Transliteration](#3-bidirectional-script-transliteration)
   - [Grammar, Classifiers & Naming System](#4-grammar-classifiers--naming-system)
   - [Phrasebook & Fieldwork Elicitation](#5-phrasebook--fieldwork-elicitation)
   - [Annotated Corpus & Interlinear Glossing (IGT)](#6-annotated-corpus--interlinear-glossing-igt)
   - [Data Exporters (Anki, CSV, HTML, LaTeX, ELAN)](#7-data-exporters-anki-csv-html-latex-elan)
7. [Command-Line Interface (CLI)](#command-line-interface-cli)
8. [Interactive Web Platform (`khamyang web`)](#interactive-web-platform-khamyang-web)
9. [Academic Sources & Citations](#academic-sources--citations)
10. [License](#license)

---

## Language Background & Sociolinguistics

| Attribute | Details |
| :--- | :--- |
| **Language Name** | Tai Khamyang / Khamjang / Nora (ꩯမ်ထႃႆၶင် / টাই খাময়াং) |
| **ISO 639-3** | `ksu` |
| **Glottolog** | `kham1282` |
| **Language Family** | Kra-Dai → Tai → Southwestern Tai → Northwestern Tai / Shan group → Assam Tai |
| **Primary Location** | Powaimukh (*Maan3 Paa1 Waai6*) village, Margherita, Tinsukia district, Assam, India |
| **Endangerment Status** | UNESCO: **Critically Endangered** (< 50 fluent mother-tongue speakers remaining) |
| **Prominent Custodians** | Chaw Sa Myat Chowlik, Deben Chowlik, Bhogeswar Thomung |
| **Etymology** | *kham* (gold / ၶမ်) + *yang* (to have / য়োং) = *"People who have gold"* |

---

## Phonological & Tonal Architecture

Khamyang is an isolating, monosyllabic tonal language with **six contrastive lexical tones**, rigorously documented by linguist Dr. Stephen Morey (*The Tai Languages of Assam*, 2005):

| Tone # | Name | Chao Pitch | IPA | Contour Description | Gedney Box Category |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | Mid Level | `33` | ˧˧ | Mid level with slight final fall | `A1`, `A3`, `B1` |
| **2** | High Falling | `54` | ˥˦ | High level onset with noticeable descent | `B2`, `C2` |
| **3** | Low Creaky | `21` | ˨˩̰ | Low falling pitch with distinct creaky laryngealization | `A4`, `B4` |
| **4** | High Falling Glottal | `54ʔ` | ˥˦ʔ | High falling pitch terminated by abrupt glottal closure `[ʔ]` | `C1`, `C4`, `DL1`, `DS1`, `DL4`, `DS4` |
| **5** | Low Falling | `31` | ˧˩ | Low falling pitch without creaky phonation | `B3`, `C3`, `DL3`, `DS3` |
| **6** | Level Rising | `35` | ˧˥ | Mid level pitch with a clear terminal rise | `A2` |

### Gedney Tone Box Mapping
The library provides automated Gedney box resolution from Proto-Tai initial classes (1–4) and tone classes (A, B, C, DL, DS):
```python
from khamyang import gedney_lookup

print(gedney_lookup("A", 1))   # Returns 1 (Tone 1)
print(gedney_lookup("A", 2))   # Returns 6 (Tone 6)
print(gedney_lookup("B", 2))   # Returns 2 (Tone 2)
print(gedney_lookup("C", 1))   # Returns 4 (Tone 4)
print(gedney_lookup("C", 3))   # Returns 5 (Tone 5)
```

---

## Writing Systems & Orthography

The Tai Khamyang language uses three primary writing systems:
1. **Lik Tai Script:** A variant of the Myanmar/Shan script utilizing the Myanmar Unicode block (`U+1000..U+109F`) and Myanmar Extended-A (`U+AA60..U+AA7F`) for Khamti/Phake characters (e.g., `ꩯ`, `ꩢ`, `ၸ`, `ၼ`, `ဢ`).
2. **Assamese Script (অসমীয়া লিপি):** Historically and widely used in Assam for community education and local publication. Tone is represented with superscripts (`¹` to `⁶`).
3. **Romanization & IPA:** Stephen Morey's standardized linguistic Romanization using digits `1` to `6` for tone representation (e.g., `nam6`, `fai1`, `khaw3`, `maan3`).

---

## Installation

Install directly in editable development mode or via pip:

```bash
# Clone the repository
git clone https://github.com/khamyang-revitalization/khamyang.git
cd khamyang

# Install package and dependencies
pip install -e .
```

Dependencies: `click`, `rich`, `fastapi`, `uvicorn` (all included).

---

## Quickstart Guide

```python
import khamyang

# 1. Access the dictionary
dict_db = khamyang.get_dictionary()
print(f"Total entries loaded: {len(dict_db)}")  # 1,027+ words

# 2. Look up a word across all scripts
entry = dict_db.lookup("nam6")[0]
print(entry.roman)        # nam6
print(entry.lik_tai)      # ၼမ်ႊ
print(entry.assamese)     # নাম⁶
print(entry.ipa)          # [nam˧˥]
print(entry.gloss_en)     # water, river

# 3. Transliterate across scripts
lik_tai = khamyang.transliterate("kaw1 kin1 khaw3 yow3", source_script="roman", target_script="liktai")
print(lik_tai)            # ၵဝ် ၵိၼ် ၶဝ်ႈ ယဝ်ႉ

# 4. Generate Tai numeral phrases
print(khamyang.num_to_khamyang(24))  # saaw1 si5

# 5. Traditional birth-order naming
name = khamyang.get_birth_name(1, gender="male")
print(name.name_roman)    # Aai (First-born son)
```

---

## Core Modules & Python API

### 1. Dictionary & Lexical Search

The dictionary engine provides tone-sensitive and tone-agnostic queries, category filtering, fuzzy search, and cognate comparisons:

```python
from khamyang.lexicon.dictionary import get_dictionary
from khamyang.lexicon.search import fuzzy_search, cognate_search

d = get_dictionary()

# Search by English meaning
results = d.search("elephant")
for w in results:
    print(f"{w.roman} ({w.lik_tai}): {w.gloss_en}")
    # tsaang3 (ၸၢင်ႉ): elephant

# Filter by semantic domain
nature_words = d.filter_by_category("nature")
print(f"Nature vocabulary: {len(nature_words)} words")

# Filter by tone
tone3_words = d.filter_by_tone(3)
print(f"Tone 3 (Low Creaky) words: {len(tone3_words)}")

# Comparative Tai cognate search
phake_cogs = cognate_search("phake", "nam")
for w in phake_cogs:
    print(f"Khamyang: {w.roman} <-> Phake: {w.cognates['phake']}")
```

### 2. Phonology & 6-Tone Engine

Access acoustic pitch models, Chao pitch numerals, and syllable structure analysis:

```python
from khamyang.phonology.tones import ToneSystem, get_tone
from khamyang.phonology.phonemes import parse_syllable
from khamyang.phonology.synth import generate_tone_audio_params

# Inspect Tone 4
t4 = get_tone(4)
print(t4.name)            # High Falling Glottalized
print(t4.pitch_chao)      # 54ʔ
print(t4.glottalized)     # True

# Parse syllable into onset, medial, nucleus, coda, and tone
parsed = parse_syllable("kwaai1")
print(parsed.onset)       # 'k'
print(parsed.medial)      # 'w'
print(parsed.nucleus)     # 'aai'
print(parsed.tone)        # 1
print(parsed.ipa)         # '[kwaːi˧˧]'

# Generate frequency curves (Hz) for audio synthesis
audio_params = generate_tone_audio_params(tone_num=2, base_frequency=165.0)
for pt in audio_params["points"]:
    print(f"Time: {pt['time']}s -> {pt['freq']} Hz")
```

### 3. Bidirectional Script Transliteration

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

### 4. Grammar, Classifiers & Naming System

#### Classifier Agreement Engine
In Tai grammar, counting requires: `[Noun] + [Numeral] + [Classifier]`:

```python
from khamyang.grammar.classifiers import ClassifierEngine

# Quantify animals with classifier 'to1'
print(ClassifierEngine.quantify("maa1", 2))       # 'maa1 sɔŋ1 to1' (2 dogs)
print(ClassifierEngine.quantify("nok4", 3))       # 'nok4 saam1 to1' (3 birds)

# Quantify humans with classifier 'ko5'
print(ClassifierEngine.quantify("khon1", 4))      # 'khon1 si5 ko5' (4 people)

# Quantify houses with classifier 'lung1'
print(ClassifierEngine.quantify("hɯn1", 1))       # 'hɯn1 nɯŋ5 lung1' (1 house)
```

#### Traditional Birth-Order Naming System
The Khamyang people name children according to birth order (1st to 8th):

```python
from khamyang.grammar.naming import get_birth_name, generate_full_name

# 1st son and 1st daughter
print(get_birth_name(1, "male").name_roman)     # Aai
print(get_birth_name(1, "female").name_roman)   # Ye

# Full name with clan surname
full = generate_full_name(order=1, gender="male", personal_name="Deben", clan="Chowlik")
print(full["full_roman"])
# Output: 'Chaw Aai Deben Chowlik'
```

### 5. Phrasebook & Fieldwork Elicitation

Essential conversational expressions designed for field researchers in Powaimukh:

```python
from khamyang.phrases.phrasebook import get_phrasebook

pb = get_phrasebook()
fieldwork_phrases = pb.get_by_category("fieldwork")

for p in fieldwork_phrases:
    print(f"EN: {p.english}")
    print(f"Khamyang: {p.roman} ({p.lik_tai})")
    print(f"Assamese: {p.assamese_trans}")
    print("---")
```

### 6. Annotated Corpus & Interlinear Glossing (IGT)

```python
from khamyang.corpus.texts import get_corpus
from khamyang.corpus.igt import InterlinearGloss
from khamyang.corpus.exporters import export_to_latex, export_to_elan_eaf

corpus = get_corpus()
texts = corpus.get_all()

# Print formatted interlinear text
sentence = texts[0].sentences[0]
print(InterlinearGloss.format_text(sentence))

# Export entire text to LaTeX gb4e format
latex_doc = export_to_latex(texts[0])

# Export to ELAN EAF XML for multimedia time-alignment
elan_xml = export_to_elan_eaf(texts[0])
```

### 7. Data Exporters (Anki, CSV, HTML, LaTeX, ELAN)

```python
from khamyang.export.exporter import export_to_anki_tsv, export_to_csv, export_to_html

# Export Anki deck (.tsv) for spaced repetition learning
export_to_anki_tsv("khamyang_anki.tsv")

# Export tabular dataset (.csv) for data science
export_to_csv("khamyang_lexicon.csv")

# Export standalone HTML dictionary
export_to_html("dictionary.html")
```

---

## Command-Line Interface (CLI)

The `khamyang` command provides rich terminal tooling:

```bash
# Look up words
khamyang lookup nam6
khamyang lookup "elephant"

# Full-text search with category or tone filter
khamyang search "rice" --category food
khamyang search "" --tone 3

# Transliteration
khamyang transliterate "kaw1 yu5 maan3 paa1 waai6" --to liktai
khamyang transliterate "kaw1 kin1 khaw3" --to assamese

# Analyze tones
khamyang tone 3
khamyang tone kwaai1

# Traditional naming
khamyang name --gender m --order 1 --personal "Deben" --clan "Chowlik"

# Numbers
khamyang num 24 --script liktai

# Browse phrasebook
khamyang phrase --category fieldwork

# Linguistic statistics
khamyang stats

# Export datasets
khamyang export --format csv --output khamyang.csv
khamyang export --format anki --output deck.tsv
khamyang export --format html --output dictionary.html

# Launch interactive Web Platform
khamyang web --port 8000
```

---

## Interactive Web Platform (`khamyang web`)

Launch the built-in web revitalization studio:
```bash
khamyang web --port 8000
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to access:
- 🔍 **Multi-Script Dictionary:** Live search with category tags and tone badges.
- 🎵 **6-Tone Studio:** Interactive Web Audio API frequency curves with live playback for all 6 tones.
- 🔤 **Virtual Lik Tai Keyboard & Transliteration:** Type directly in Lik Tai or Romanized text.
- 💬 **Fieldwork Phrasebook:** Audio prompts and community elicitation sentences.
- ⚖️ **Grammar & Classifier Assistant:** Test classifier agreement and generate traditional clan names.
- 📜 **Corpus Reader:** Read folktales and migration histories with 5-line interlinear glosses.
- 📥 **Export Center:** Download datasets with a single click.

---

## Academic Sources & Citations

If you use this library for linguistic, NLP, or anthropological research, please cite the foundational documentation:

- **Morey, Stephen (2005).** *The Tai Languages of Assam: A Grammar and Texts.* Pacific Linguistics 565. Canberra: Australian National University.
- **Morey, Stephen (2005).** "Tonal change in the Tai languages of Northeast India." *Linguistics of the Tibeto-Burman Area*, 28(2): 139–202.
- **Morey, Stephen (2008).** "The Tai languages of Assam." In Diller, Edmondson & Luo (eds.), *The Tai-Kadai Languages*, pp. 200–241. Routledge.
- **Nath, Palash Kumar (2015–2026).** *Documentation and Digitization of Tai Khamyang Oral Literature and Manuscripts.* Endangered Languages Documentation Programme (ELDP) & ABILAC.
- **Centre for Endangered Languages (CFEL) (2016).** *Linguistic Documentation of Tai-Khamyang.* Tezpur University, Assam, India.

---

## License

This project is licensed under the [MIT License](LICENSE). Dedicated to the speakers, elders, and youth of Powaimukh village striving to keep the Tai Khamyang language alive for generations to come.
