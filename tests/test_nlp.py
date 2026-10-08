"""Tests for Tai Khamyang NLP module (tokenizer, normalizer, pos_tagger, language_detector)."""

import unittest
from khamyang.nlp import (
    normalize,
    tokenize,
    detokenize,
    pos_tag,
    detect_language,
)


class TestNLP(unittest.TestCase):

    def test_normalize_superscripts(self):
        text = "pu⁵ yaa³ haw¹ khao⁵ maa¹"
        norm = normalize(text)
        self.assertEqual(norm, "pu5 yaa3 haw1 khao5 maa1")

    def test_tokenize_roman(self):
        sentence = "pu5 yaa3 haw1 khao5 maa1 thaang1 doi1 pat4 kai1."
        tokens = tokenize(sentence)
        self.assertIn("pu5", tokens)
        self.assertIn("pat4", tokens)
        self.assertIn(".", tokens)

    def test_detokenize(self):
        tokens = ["pu5", "yaa3", "haw1", "maa1", "."]
        detok = detokenize(tokens)
        self.assertEqual(detok, "pu5 yaa3 haw1 maa1.")

    def test_pos_tagger(self):
        sentence = "pu5 yaa3 haw1 khao5 maa1"
        tagged = pos_tag(sentence)
        self.assertEqual(len(tagged), 5)
        # Check pronoun
        self.assertEqual(tagged[2][1], "PRON")  # haw1
        # Check verb
        self.assertEqual(tagged[4][1], "VERB")  # maa1

    def test_detect_language_khamyang_roman(self):
        res = detect_language("pu5 yaa3 haw1 khao5 maa1 thaang1 doi1 pat4 kai1")
        self.assertEqual(res["language"], "ksu")
        self.assertGreaterEqual(res["confidence"], 0.8)

    def test_detect_language_liktai(self):
        res = detect_language("ပူႈယႃႈႁဝ်းၶဝ်မႃး")
        self.assertEqual(res["language"], "ksu")
        self.assertEqual(res["script"], "lik_tai")

    def test_detect_language_english(self):
        res = detect_language("This is an English sentence for language testing.")
        self.assertEqual(res["language"], "eng")


if __name__ == "__main__":
    unittest.main()
