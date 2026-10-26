# Tai Khamyang (`khamyang`) Language & Cultural Corpus ꩯမ်ထႃႆၶင်

[![PyPI version](https://img.shields.io/badge/pypi-v1.1.0-blue.svg)](https://pypi.org/project/khamyang/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-green.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Amazon Author](https://img.shields.io/badge/Amazon-Author_Page-FF9900.svg)](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28)
[![Website](https://img.shields.io/badge/Website-akshatsinghbisht.com-purple.svg)](https://akshatsinghbisht.com/)
[![Endangered Status: Critical](https://img.shields.io/badge/UNESCO-Critically%20Endangered-red.svg)](https://en.wikipedia.org/wiki/Khamyang_language)
[![ISO 639-3: ksu](https://img.shields.io/badge/ISO%20639--3-ksu-orange.svg)](https://iso639-3.sil.org/code/ksu)
[![Glottolog: kham1282](https://img.shields.io/badge/Glottolog-kham1282-lightgrey.svg)](https://glottolog.org/resource/languoid/id/kham1282)

A comprehensive Python language library, computational linguistic toolkit, and cultural corpus for **Tai Khamyang** (also known as *Khamjang* or *Nora*), a critically endangered Southwestern Tai language spoken in Assam, Northeast India (predominantly in **Powaimukh** village near Margherita, Tinsukia district).

Developed under strict linguistic documentation standards: **Accuracy > volume**, **Authenticity > generation**, and **Provenance > convenience**.

> 📖 **Developer Documentation:** For complete architecture details, API references, NLP pipeline guides, and AI dataset integration, see the [Developer Guide](DEVELOPER_GUIDE.md).

---

## Table of Contents
1. [Language Background & Sociolinguistics](#language-background--sociolinguistics)
2. [Phonological & 6-Tone System](#phonological--6-tone-system)
3. [Writing Systems & Orthography](#writing-systems--orthography)
4. [Installation](#installation)
5. [Unified Developer Facade (`Khamyang`)](#unified-developer-facade-khamyang)
6. [NLP Toolkit (`khamyang.nlp`)](#nlp-toolkit-khamyangnlp)
7. [Sub-Corpora & Cultural Resources](#sub-corpora--cultural-resources)
   - [Dictionary & Lexicon](#dictionary--lexicon)
   - [Traditional Songs (*Fɯn*)](#traditional-songs-fɯn)
   - [Folklore & Interlinear Texts (IGT)](#folklore--interlinear-texts-igt)
   - [Proverbs & Sayings (*Kham1 Thum3*)](#proverbs--sayings-kham1-thum3)
   - [Everyday Fieldwork Conversations](#everyday-fieldwork-conversations)
   - [Material Culture & Ethnobotany](#material-culture--ethnobotany)
   - [Geographic Toponyms](#geographic-toponyms)
   - [Kinship & Ancestral Clans](#kinship--ancestral-clans)
   - [Archival Audio Metadata Index](#archival-audio-metadata-index)
   - [Parallel Sentence Corpus](#parallel-sentence-corpus)
   - [AI Datasets & Partitioning](#ai-datasets--partitioning)
8. [Data Verification Hierarchy](#data-verification-hierarchy)
9. [Command-Line Interface (CLI)](#command-line-interface-cli)
10. [Interactive Web Studio (`khamyang web`)](#interactive-web-studio-khamyang-web)
11. [Data Quality & Statistics](#data-quality--statistics)
12. [Academic Sources & Citations](#academic-sources--citations)
13. [License & Ethics](#license--ethics)

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
| **Key Custodians** | Late Chaw Sa Myat Chowlik, Late Nang Mya Chowlik, Deben Chowlik, Ai Che |
| **Etymology** | *kham* (gold / ၶမ်) + *yang* (to have / য়োং) = *"People who possess gold"* |

---

## Phonological & 6-Tone System

Tai Khamyang possesses **six contrastive phonemic lexical tones** corresponding to the Proto-Southwestern Tai Gedney tone box:

| Tone # | Name | Chao Pitch | IPA | Pitch Description | Gedney Box Category |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | Mid Level | `33` | ˧˧ | Mid level with slight final fall | `A1`, `A3`, `B1` |
| **2** | High Falling | `54` | ˥˦ | High level onset with noticeable descent | `B2`, `C2` |
| **3** | Low Creaky | `21` | ˨˩̰ | Low falling pitch with distinct creaky laryngealization | `A4`, `B4` |
| **4** | High Falling Glottal | `54ʔ` | ˥˦ʔ | High falling pitch terminated by abrupt glottal closure `[ʔ]` | `C1`, `C4`, `DL1`, `DS1`, `DL4`, `DS4` |
| **5** | Low Falling | `31` | ˧˩ | Low falling pitch without creaky phonation | `B3`, `C3`, `DL3`, `DS3` |
| **6** | Level Rising | `35` | ˧˥ | Mid level pitch with a clear terminal rise | `A2` |

---

## Writing Systems & Orthography

The Tai Khamyang language uses three primary writing systems:
1. **Lik Tai Script:** A variant of the Myanmar/Shan script utilizing the Myanmar Unicode block (`U+1000..U+109F`) and Myanmar Extended-A (`U+AA60..U+AA7F`) for Khamti/Phake characters (e.g., `ꩯ`, `ꩢ`, `ၸ`, `ၼ`, `ဢ`).
2. **Standardized Romanization:** Dr. Stephen Morey's standardized linguistic Romanization using digits `1` to `6` for tone representation (e.g., `nam6`, `fai1`, `khaw3`, `maan3`).
3. **Assamese Script (অসমীয়া লিপি):** Historically and widely used in Assam for community education and local publication. Tone is represented with superscripts (`¹` to `⁶`).

---

## Installation

```bash
# Clone the repository
git clone https://github.com/khamyang-revitalization/khamyang.git
cd khamyang

# Install package in editable mode
pip install -e .
```

---

## Unified Developer Facade (`Khamyang`)

The primary developer entry point provides access to all modules and sub-corpora:

```python
from khamyang import Khamyang

# Initialize the corpus facade
lang = Khamyang()

# 1. Dictionary Lookup
entries = lang.lookup("nam6")
print(entries[0]["gloss_en"])    # "water, river"
print(entries[0]["lik_tai"])     # "ၼမ်ႊ"
print(entries[0]["ipa"])         # "[nam˧˥]"

# 2. English / Assamese Search
results = lang.search("elephant")
for r in results:
    print(r["roman"], r["lik_tai"], r["gloss_en"])

# 3. Text Normalization & Romanization
norm = lang.normalize("kaw¹ kin¹ khaw³ yow³")
print(norm)                      # "kaw1 kin1 khaw3 yow3"

# 4. Multi-Script Transliteration
lik_tai = lang.to_liktai("kaw1 yu5 maan3 paa1 waai6")
print(lik_tai)                   # "ၵဝ် ယူႇ မၢၼ်ႈ ပႃ ဝၢႆး"

# 5. Traditional Songs (Fɯn)
songs = lang.songs(genre="wedding")
print(songs[0]["title"])         # "Fɯn Ao Nang"

# 6. Stories & Interlinear Texts
stories = lang.stories()
print(stories[0]["title_en"])    # "The Quail and the Egret"

# 7. Traditional Proverbs (Kham Thum)
proverbs = lang.proverbs()
print(proverbs[0]["proverb_khamyang"])

# 8. Everyday Fieldwork Conversations
dialogues = lang.conversations()
print(dialogues[0]["topic"])

# 9. Classifier Quantification
phrase = lang.quantify("maa1", 2)
print(phrase)                    # "maa1 sɔŋ1 to1" (two dogs)

# 10. Archival Audio Recordings
recordings = lang.audio_recordings()
print(recordings[0]["archive_collection"])  # "PARADISEC SDM03"
```

---

## NLP Toolkit (`khamyang.nlp`)

The package includes lightweight, zero-external-dependency linguistic processors:

```python
from khamyang.nlp import (
    KhamyangNormalizer,
    KhamyangTokenizer,
    KhamyangLemmatizer,
    KhamyangPOSTagger,
    KhamyangLanguageDetector,
)

# Tokenization
tok = KhamyangTokenizer()
tokens = tok.tokenize("kaw1 kin1 khaw3 yow3")
print(tokens)  # ['kaw1', 'kin1', 'khaw3', 'yow3']

# Normalization (superscript numbers to ASCII digits, Unicode NFC)
norm = KhamyangNormalizer()
clean = norm.normalize("nam⁶")
print(clean)   # "nam6"

# Part-of-Speech Tagging (Universal Dependencies)
tagger = KhamyangPOSTagger()
tagged = tagger.tag(["kaw1", "kin1", "khaw3", "yow3"])
print(tagged)  # [('kaw1', 'PRON'), ('kin1', 'VERB'), ('khaw3', 'NOUN'), ('yow3', 'PART')]

# Lemmatization
lem = KhamyangLemmatizer()
lemma = lem.lemmatize("kin1")
print(lemma)   # "kin1"

# Language Detection
det = KhamyangLanguageDetector()
res = det.detect("kaw1 kin1 khaw3")
print(res)     # {'language': 'ksu', 'confidence': 1.0, ...}
```

---

## Sub-Corpora & Cultural Resources

### Dictionary & Lexicon
- **1,099 verified lexical entries** across 48 semantic domains (kinship, flora, fauna, agriculture, religion, bodily anatomy).
- Every entry contains: `id`, `roman`, `lik_tai`, `assamese`, `ipa`, `tone`, `pos`, `definition_en`, `definition_as`, `category`, and `gedney_box`.

### Traditional Songs (*Fɯn*)
- **6 authentic traditional songs** transcribed in metric verse from audio recorded by Stephen Morey (`SDM03`, `SDM07`):
  1. *Fɯn Ao Nang* (Song of Courting / Welcoming the Bride)
  2. *Fɯn Nɔn Luk* (Tai Lullaby / Rocking the Baby to Sleep)
  3. *Fɯn Tam Khaw* (Rice Pounding Rhythm Song)
  4. *Fɯn Poy Sangken* (Song of the New Year Water Sprinkling Festival)
  5. *Fɯn Cholim* (Song of the Welcoming Courtyard Dance)
  6. *Fɯn Dam Khaw* (Song of Rice Seedling Transplantation)

### Folklore & Interlinear Texts (IGT)
- **5 complete narratives** formatted in Leipzig-compliant interlinear glosses (IGT):
  - *The Quail and the Egret* (*Lik Pung: Nok4 Kot4 Kap4 Nok4 Yang1*)
  - *The Hornbill and the Drongo* (*Lik Pung: Nok4 Kok4 Kap4 Nok4 Te3*)
  - *The Water Buffalo and the Tiger* (*Lik Pung: Kwaai1 Kap4 Sɯa1*)
  - *The Five Siblings Journeying* (*Lik Pung: Khon1 Haa3 Luk4 Phaai1*)
  - *Mahosadha Jataka* (*Lik Chau: Mahosadha*)

### Proverbs & Sayings (*Kham1 Thum3*)
- Moral aphorisms preserving traditional wisdom, agricultural advice, and filial duty:
  - *"Kin1 khaw3 haam1 luang1, kin1 nam6 haam1 thung1"* (Eat rice respecting the grain, drink water respecting the stream).

### Material Culture & Ethnobotany
- **Traditional architecture & implements:** Raised stilt house (*hɯn1 thaai1*), center pillar (*saaw1 mai6 luang1*), domestic hearth (*khaang1 fai1*), handloom (*huuk4 phaa3*), handwoven skirt (*sin3 thaai1*), foot-lever mortar (*khrɔk4 tam1 khaw3*).
- **Ethnobotanical & Zoological taxa:** Documented with binomial Latin taxonomy (*Oryza sativa*, *Piper betle*, *Areca catechu*, *Calamus rotang*, *Bubalus bubalis*, *Elephas maximus*, *Panthera tigris*, *Pavo cristatus*).
- **Festivals:** *Poy Sangken* (Water Festival), *Mai-ko-shum-phai* (Monastic Firewood Tower), *Poy Lu Phraa* (Buddha Consecration), *Me Dam Me Phi* (Ancestor Worship).

### Archival Audio Metadata Index
- Indices of permanent archival recordings held in **PARADISEC** (`SDM03`, `SDM07`) and **ELAR** (`MPI1029884`).
- Catalogs recording dates, durations, informants, locations, and persistent archive URLs. (Audio binaries are preserved via source links to honor depositor rights).

### Parallel Sentence Corpus
- 16 fully aligned Tai Khamyang <-> English <-> Assamese sentence pairs with full morphemic breakdown and provenance.

### AI Datasets & Partitioning
- AI instruction and evaluation sets are stored strictly separately in `data/ai/instruction_dataset.jsonl`.
- Explicitly labeled with `source_type: "human_verified"` to prevent data poisoning.

---

## Data Verification Hierarchy

Every record in the library adheres to a 3-tier epistemological classification:

1. **Level 1 — Verified Authentic (`level_1_verified`):** Directly attested in peer-reviewed fieldwork or published academic archives (Morey, Grierson, Buragohain, Nath).
2. **Level 2 — Documented Historical (`level_2_documented_review`):** Found in archival manuscripts requiring ongoing elder review.
3. **Level 3 — Computationally Derived (`level_3_derived`):** Generated or augmented data for AI benchmarking; strictly quarantined in `data/ai/`.

---

## Command-Line Interface (CLI)

The `khamyang` command provides rich terminal tooling:

```bash
# Look up words
khamyang lookup nam6
khamyang lookup "water"

# Search by tone or category
khamyang search "" --tone 3
khamyang search "rice" --category food

# Transliteration
khamyang transliterate "kaw1 yu5 maan3 paa1 waai6" --to liktai
khamyang transliterate "kaw1 kin1 khaw3" --to assamese

# Analyze tones
khamyang tone 4
khamyang tone kwaai1

# Traditional naming
khamyang name --gender m --order 1 --personal "Deben" --clan "Chowlik"

# Numbers
khamyang num 24 --script liktai

# Browse songs & folklore
khamyang stats
khamyang export --format csv --output khamyang_lexicon.csv

# Launch interactive Web Platform
khamyang web --port 8000
```

---

## Interactive Web Studio (`khamyang web`)

Launch the built-in web revitalization studio:
```bash
khamyang web --port 8000
```
Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to access:
- 🔍 **Multi-Script Dictionary:** Live search with category filters and tone badges.
- 🎵 **6-Tone Studio:** Interactive Web Audio API synthesizer modeling the 6 Gedney pitch curves.
- 🔤 **Virtual Lik Tai Keyboard:** Type in Lik Tai script or Romanization.
- 📜 **Corpus Reader:** Folktales and songs with 5-line interlinear glosses.
- 📥 **Export Center:** Download Anki decks, CSVs, LaTeX glosses, and ELAN EAF files.

---

## Data Quality & Statistics

See [STATISTICS.md](STATISTICS.md) and [DATA_QUALITY_REPORT.md](DATA_QUALITY_REPORT.md) for full metrics:
- **Lexical Entries:** 1,099 words (100% verified with IPA, Lik Tai, Assamese, and 6-tone classification).
- **Songs & Poems:** 6 songs (8 stanzas, 34 metric lines).
- **Folktales & Texts:** 5 Leipzig-glossed texts (14 interlinear sentences).
- **Proverbs:** 6 traditional proverbs.
- **Archival Audio Sessions:** 5 indexed recording sessions (102.5 minutes).
- **Scholarly Sources:** 13 primary academic sources in registry.

---

## Academic Sources & Citations

For academic attribution, see [BIBLIOGRAPHY.md](BIBLIOGRAPHY.md) and [CITATION.cff](CITATION.cff).

Primary references:
- **Morey, Stephen (2005).** *The Tai Languages of Assam: A Grammar and Texts.* Pacific Linguistics 565. Canberra: Australian National University.
- **Morey, Stephen (2008).** "The traditional songs of the Tai Khamyang." In *The Tai-Kadai Languages*, Routledge.
- **Nath, Palash Kumar (2015–2026).** *Documentation and Digitization of Tai Khamyang Oral Literature and Manuscripts.* ELAR & ABILAC.
- **Grierson, George A. (1904).** *Linguistic Survey of India*, Vol. II: *Mon-Khmer and Tai Families*. Calcutta: Office of the Superintendent of Government Printing.
- **Buragohain, Yehom (1998).** *The Tai-Khamyangs of Assam: A Study in Social and Cultural Continuity and Change.* Dibrugarh University.

---

---

## 👨‍💻 Author, Creator & Preservation Mission

> ### *"Preserving an endangered voice is not just engineering—it is an act of deep resistance against cultural extinction."*

This entire computational infrastructure, language corpus, multi-script transliteration engine, and digital revitalization platform was authored, architected, and developed by:

### **Akshat Singh Bisht**
*Author, Language Technologist & Computational Linguistic Preservationist*

* 🌐 **Official Website:** [https://akshatsinghbisht.com/](https://akshatsinghbisht.com/)
* 📧 **Direct Contact:** [infoakshatsinghbisht@gmail.com](mailto:infoakshatsinghbisht@gmail.com)
* 💼 **LinkedIn Profile:** [Akshat Singh Bisht on LinkedIn](https://www.linkedin.com/in/akshat-singh-bisht-digital-performance-marketing-specialist/)
* 📚 **Amazon Author Central:** [Akshat Singh Bisht on Amazon](https://www.amazon.com/stores/Akshat-Singh-Bisht/author/B0D5TYDT28)
* 🔬 **ResearchGate Profile:** [Akshat Bisht on ResearchGate](https://www.researchgate.net/profile/Akshat-Bisht-8)
* 🐙 **GitHub:** [@infoakshatsinghbisht-eng](https://github.com/infoakshatsinghbisht-eng)
* 📦 **PyPI Library:** [khamyang on PyPI](https://pypi.org/project/khamyang/)

---

### The Story Behind This Project & The Struggle for Preservation

**Tai Khamyang** (ISO 639-3: `ksu`, Glottolog: `kham1282`) is on the knife-edge of silence, with **fewer than 50 fluent native elder speakers** surviving in Powaimukh village, Assam. 

Preserving this language has demanded tireless dedication and immense struggles:
1. **Pioneering Archival Retrieval:** Hunting down rare 19th and early 20th-century palm-leaf manuscripts, sanchi-bark chronicles, historical Buranjis, and colonial monographs scattered across remote archives and libraries.
2. **Fieldwork & Interlinear Precision:** Analyzing thousands of lines of raw field recordings, transcribing metric syllabic songs (*Kham Fɯn*), and decoding complex 6-tone pitch contours (Gedney Box A1..DS4) to ensure **0.0% hallucination** and total linguistic authenticity.
3. **Computational Engineering from Scratch:** Designing custom phonetic synthesizers, multi-script transliterators across Lik Tai (Unicode Myanmar Extended-A), Roman, Assamese, and IPA, and building a full 10-tab web revitalizer and NLP suite without existing commercial tools.

This project represents a personal mission to ensure that the rich cultural memory, ancestral wisdom, Buddhist philosophy, and unique linguistic heritage of the Tai Khamyang people never disappear from the human record.

---

## ⚖️ Copyright & Mandatory Attribution Notice

**Copyright © 2026 Akshat Singh Bisht. All rights reserved.**

If you use this library, source code, lexical datasets, parallel corpora, grammatical rules, or models for:
* Academic research or journal papers
* Computational linguistics or NLP training / fine-tuning
* Language documentation or educational materials
* Software applications, mobile apps, or web platforms

**You MUST give explicit credit and cite Akshat Singh Bisht as the primary author and creator.**

### How to Cite This Work

#### APA Format:
```text
Bisht, A. S. (2026). Tai Khamyang Language Library & Cultural Corpus (Version 1.1.0) [Computer software]. 
PyPI & GitHub. https://github.com/infoakshatsinghbisht-eng/khamyang-language-library
```

#### BibTeX:
```bibtex
@software{bisht2026khamyang,
  author       = {Bisht, Akshat Singh},
  title        = {{Tai Khamyang Language Library & Cultural Corpus: Computational Revitalization Toolkit for Endangered Southwestern Tai}},
  version      = {1.1.0},
  year         = {2026},
  url          = {https://github.com/infoakshatsinghbisht-eng/khamyang-language-library},
  doi          = {10.5281/zenodo.khamyang.v1.1.0},
  publisher    = {PyPI & GitHub},
  keywords     = {Tai Khamyang, ksu, Endangered Languages, Assam, Computational Linguistics}
}
```

---

## License & Community Ethics

- **Software Code:** Released under the [MIT License](LICENSE) with mandatory attribution clause (Copyright © 2026 Akshat Singh Bisht).
- **Linguistic Heritage:** Preserved in respectful tribute to the native elders, chanters, and speakers of Powaimukh village.
