"""Unit tests for script transliteration."""

import unittest
import khamyang


class TestTransliteration(unittest.TestCase):

    def test_roman_to_liktai(self):
        """Test conversion of Romanized syllables into Lik Tai script."""
        res = khamyang.roman_to_liktai("nam6")
        self.assertTrue(len(res) > 0)
        self.assertIn("ၼ", res)  # Shan/Khamti letter Na

    def test_roman_to_assamese(self):
        """Test conversion of Romanized syllables into Assamese script."""
        res = khamyang.roman_to_assamese("nam6")
        self.assertTrue(len(res) > 0)
        self.assertIn("ন", res)  # Assamese letter Na

    def test_roman_to_ipa(self):
        """Test conversion to IPA."""
        ipa = khamyang.roman_to_ipa("nam6")
        self.assertTrue(ipa.startswith("["))
        self.assertTrue(ipa.endswith("]"))
        self.assertIn("nam", ipa)

    def test_general_transliterate_function(self):
        """Test high-level transliterate dispatch."""
        out1 = khamyang.transliterate("khaw3", source_script="roman", target_script="liktai")
        self.assertTrue(bool(out1))

        out2 = khamyang.transliterate("khaw3", source_script="roman", target_script="assamese")
        self.assertTrue(bool(out2))


if __name__ == "__main__":
    unittest.main()
