"""
Tai Khamyang Part-of-Speech (POS) Tagger
Rule-based and lexicon-backed POS tagger using Universal Dependencies categories.
"""

from typing import List, Tuple
from khamyang.nlp.tokenizer import tokenize
from khamyang.nlp.lemmatizer import KhamyangLemmatizer
from khamyang.grammar.classifiers import CLASSIFIERS
from khamyang.grammar.pronouns import PRONOUNS
from khamyang.grammar.syntax import TAM_MARKERS


# Known function words
CLASSIFIER_SET = set(CLASSIFIERS.keys())
PRONOUN_SET = {p.form_roman for p in PRONOUNS}
TAM_SET = {t.form_roman for t in TAM_MARKERS.values()}



PREPOSITION_SET = {"rim1", "nai1", "bon1", "tai3", "theu1", "luk4", "kwaa5"}
CONJUNCTION_SET = {"tang1", "kap4", "le1", "ko1", "khaa3", "phe1"}
PARTICLE_SET = {"haa1", "nɔ1", "chaw1", "nang1", "hye5", "waa1"}


def pos_tag(text_or_tokens) -> List[Tuple[str, str]]:
    """
    Tags a sentence or token list with Universal Dependencies POS tags:
    NOUN, VERB, PRON, NUM, CLF, ADJ, ADV, PART, ADP, CCONJ, PUNCT.
    Returns list of (token, pos_tag) tuples.
    """
    if isinstance(text_or_tokens, str):
        tokens = tokenize(text_or_tokens)
    else:
        tokens = list(text_or_tokens)

    tagged = []
    for tok in tokens:
        clean = tok.strip().lower()

        # Punctuation check
        if clean in [".", ",", "!", "?", ";", ":", "-", '"', "'", "၊", "။"]:
            tagged.append((tok, "PUNCT"))
            continue

        # Check grammatical function words
        if clean in PRONOUN_SET:
            tagged.append((tok, "PRON"))
            continue
        if clean in CLASSIFIER_SET:
            tagged.append((tok, "CLF"))
            continue
        if clean in TAM_SET:
            tagged.append((tok, "PART"))
            continue
        if clean in PREPOSITION_SET:
            tagged.append((tok, "ADP"))
            continue
        if clean in CONJUNCTION_SET:
            tagged.append((tok, "CCONJ"))
            continue
        if clean in PARTICLE_SET:
            tagged.append((tok, "PART"))
            continue

        # Check dictionary
        info = KhamyangLemmatizer.get_lemma_info(clean)
        if info:
            raw_pos = info.get("pos", "").lower()
            if raw_pos == "noun":
                tagged.append((tok, "NOUN"))
            elif raw_pos == "verb":
                tagged.append((tok, "VERB"))
            elif raw_pos == "adj":
                tagged.append((tok, "ADJ"))
            elif raw_pos == "adv":
                tagged.append((tok, "ADV"))
            elif raw_pos == "pron":
                tagged.append((tok, "PRON"))
            elif raw_pos == "num":
                tagged.append((tok, "NUM"))
            elif raw_pos == "clf":
                tagged.append((tok, "CLF"))
            else:
                tagged.append((tok, "NOUN"))
        else:
            # Default heuristic: if contains digits, NUM; otherwise NOUN
            if any(c.isdigit() for c in clean):
                tagged.append((tok, "NUM"))
            else:
                tagged.append((tok, "NOUN"))

    return tagged
