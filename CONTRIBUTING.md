# Contributing to the Tai Khamyang Language Library

Thank you for your interest in preserving, documenting, and reviving the **Tai Khamyang** (ISO 639-3: `ksu`, Glottolog: `kham1282`) language.

Tai Khamyang is a critically endangered Southwestern Tai language spoken primarily in **Powaimukh** village (near Margherita, Tinsukia district, Assam, India). Because fewer than 50 fluent mother-tongue speakers remain, preserving authenticity and provenance is paramount.

---

## Core Principle: No Data Fabrication

Every linguistic addition (word, gloss, sentence, song, proverb, grammar rule, or audio reference) must be grounded in **verifiable evidence**.
- **NEVER** invent Khamyang words, meanings, tone markings, sentences, or translations.
- **NEVER** reconstruct song lyrics or cultural folklore using artificial intelligence without explicit human community validation.
- If an exact translation or pronunciation is unknown, mark it as `not_documented` or `requires_verification`.

---

## The Three Data Levels

All records in this project are classified into one of three strict levels:

| Level | Classification | Criteria |
| :---: | :--- | :--- |
| **Level 1** | `level_1_verified` | Directly supported by authoritative published linguistic documentation (e.g., Stephen Morey, Palash Kumar Nath, G.A. Grierson) or audio archive field recordings with native speakers. |
| **Level 2** | `level_2_documented_review` | Recorded in historical wordlists, secondary manuscripts, or community recollections requiring ongoing review by elders. |
| **Level 3** | `level_3_derived` | Computationally generated or synthetic splits for AI evaluation and NLP modeling. **Must be strictly isolated in `data/ai/` and never mixed into verified corpora.** |

---

## How to Contribute

### 1. Contributing Vocabulary & Kinship Terms
- Submit entries in `khamyang/data/lexicon.json` or `khamyang/data/kinship.json`.
- Provide:
  - Romanized form with tone number (1–6, e.g. `nam6`)
  - Lik Tai script (Unicode Myanmar/Shan blocks `U+1000..U+109F`, `U+AA60..U+AA7F`)
  - Assamese script with tone superscripts (`¹`..`⁶`, e.g. `নাম⁶`)
  - International Phonetic Alphabet (IPA)
  - Part of speech (POS)
  - English and Assamese meanings
  - Provenance: `source_id` matching an entry in `sources/source_registry.json`
  - Speaker / consultant name where ethically appropriate

### 2. Contributing Oral Narratives & Songs (*Fɯn*)
- Submit songs in `khamyang/data/songs.json` and stories in `khamyang/data/texts.json`.
- Provide stanzas with parallel interlinear lines (Romanized, Lik Tai, Assamese, English line glosses).
- Attribute village, recording year, informant, and archive deposit URI.

### 3. Audio & Ethical Guidelines
- Do not redistribute restricted or private community recordings.
- Instead, submit structured metadata to `data/audio_metadata/audio_index.json` with catalog URLs pointing to permanent archives (e.g. PARADISEC, ELAR).

---

## Code Style & Testing
- Shell/Terminal commands must be executed with `-X utf8` on Windows systems to preserve IPA characters (`ɯ`).
- Run the automated test suite before opening a pull request:
  ```bash
  python -X utf8 -m unittest discover tests
  ```
- All tests must pass.
