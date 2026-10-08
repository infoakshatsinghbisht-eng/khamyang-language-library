"""Tests for top-level Khamyang developer facade."""

import unittest
from khamyang import Khamyang


class TestKhamyangFacade(unittest.TestCase):

    def setUp(self):
        self.lang = Khamyang()

    def test_lookup_and_search(self):
        res = self.lang.lookup("nam6")
        self.assertGreaterEqual(len(res), 1)
        self.assertEqual(res[0].gloss_en, "water, river")

    def test_quantify(self):
        quant = self.lang.quantify("kwaai1", 2)
        self.assertEqual(quant, "kwaai1 sɔŋ1 to1")

    def test_kinship(self):
        uncle = self.lang.kinship("FaElBr")
        self.assertIsNotNone(uncle)
        self.assertEqual(uncle["khamyang_roman"], "lung1")

    def test_transliterate(self):
        liktai = self.lang.to_liktai("nam6")
        self.assertTrue(len(liktai) > 0)

    def test_songs_and_proverbs(self):
        songs = self.lang.songs()
        self.assertGreaterEqual(len(songs), 6)
        proverbs = self.lang.proverbs()
        self.assertGreaterEqual(len(proverbs), 5)

    def test_nlp_facade(self):
        tokens = self.lang.tokenize("pu5 yaa3 haw1")
        self.assertEqual(tokens, ["pu5", "yaa3", "haw1"])
        det = self.lang.detect_language("nam6")
        self.assertEqual(det["language"], "ksu")

    def test_stats(self):
        st = self.lang.stats()
        self.assertGreaterEqual(st["lexical_entries"], 1000)
        self.assertGreaterEqual(st["traditional_songs"], 6)
        self.assertGreaterEqual(st["proverbs_and_sayings"], 5)


if __name__ == "__main__":
    unittest.main()
