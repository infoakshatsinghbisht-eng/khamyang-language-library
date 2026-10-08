"""Unit tests for Tai Khamyang phonology and 6-tone system."""

import unittest
from khamyang.phonology.tones import ToneSystem, get_tone, gedney_lookup, TONES
from khamyang.phonology.phonemes import parse_syllable
from khamyang.phonology.synth import generate_tone_audio_params


class TestKhamyangPhonology(unittest.TestCase):

    def test_six_tones_exist(self):
        """Ensure all 6 tones are defined."""
        self.assertEqual(len(TONES), 6)
        for i in range(1, 7):
            t = get_tone(i)
            self.assertEqual(t.number, i)
            self.assertTrue(bool(t.pitch_chao))
            self.assertTrue(bool(t.ipa_symbol))

    def test_gedney_box(self):
        """Test Gedney tone box mappings from Stephen Morey's paper."""
        self.assertEqual(gedney_lookup("A", 1), 1)
        self.assertEqual(gedney_lookup("A", 2), 6)
        self.assertEqual(gedney_lookup("A", 4), 3)
        self.assertEqual(gedney_lookup("B", 2), 2)
        self.assertEqual(gedney_lookup("C", 1), 4)
        self.assertEqual(gedney_lookup("C", 3), 5)

    def test_syllable_parser(self):
        """Test parsing of onset, medial, nucleus, coda, and tone."""
        parsed = parse_syllable("kwaai1")
        self.assertEqual(parsed.onset, "k")
        self.assertEqual(parsed.medial, "w")
        self.assertEqual(parsed.nucleus, "aai")
        self.assertEqual(parsed.tone, 1)

        parsed2 = parse_syllable("nam6")
        self.assertEqual(parsed2.onset, "n")
        self.assertIsNone(parsed2.medial)
        self.assertEqual(parsed2.nucleus, "a")
        self.assertEqual(parsed2.coda, "m")
        self.assertEqual(parsed2.tone, 6)

    def test_audio_params_generation(self):
        """Test synthesis parameter curves."""
        params = generate_tone_audio_params(4)
        self.assertEqual(params["tone_number"], 4)
        self.assertTrue(params["glottal_stop"])
        self.assertGreater(len(params["points"]), 0)


if __name__ == "__main__":
    unittest.main()
