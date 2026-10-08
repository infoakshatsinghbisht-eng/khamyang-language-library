"""Unit tests for Tai Khamyang dictionary and search."""

import unittest
import khamyang
from khamyang.lexicon.dictionary import get_dictionary
from khamyang.lexicon.search import fuzzy_search, cognate_search


class TestKhamyangDictionary(unittest.TestCase):

    def setUp(self):
        self.dict = get_dictionary()

    def test_lexicon_size(self):
        """Ensure dictionary contains at least 1,000 authentic words."""
        self.assertGreaterEqual(len(self.dict), 1000)

    def test_lookup_exact_roman(self):
        """Test exact Roman lookup."""
        res = self.dict.lookup("nam6")
        self.assertGreater(len(res), 0)
        self.assertEqual(res[0].roman, "nam6")
        self.assertIn("water", res[0].gloss_en.lower())

    def test_lookup_tone_agnostic(self):
        """Test tone-agnostic Roman lookup (e.g., 'nam' finds 'nam6')."""
        res = self.dict.lookup("nam")
        self.assertGreater(len(res), 0)
        matches = [w.roman for w in res]
        self.assertTrue(any("nam" in r for r in matches))

    def test_lookup_english(self):
        """Test looking up an English gloss (e.g. 'fire' finds 'fai1')."""
        res = self.dict.search("fire")
        self.assertGreater(len(res), 0)
        matches = [w.roman for w in res]
        self.assertIn("fai1", matches)

    def test_filter_by_tone(self):
        """Test filtering by all 6 tones."""
        for t in range(1, 7):
            words = self.dict.filter_by_tone(t)
            self.assertGreater(len(words), 0, f"Tone {t} has no words!")

    def test_filter_by_category(self):
        """Test category filtering."""
        nature_words = self.dict.filter_by_category("nature")
        self.assertGreater(len(nature_words), 0)

    def test_fuzzy_search(self):
        """Test fuzzy phonetic search."""
        matches = fuzzy_search("naam", threshold=0.5)
        self.assertGreater(len(matches), 0)

    def test_cognate_search(self):
        """Test cognate lookup."""
        thai_cogs = cognate_search("thai", "nam")
        self.assertGreater(len(thai_cogs), 0)


if __name__ == "__main__":
    unittest.main()
