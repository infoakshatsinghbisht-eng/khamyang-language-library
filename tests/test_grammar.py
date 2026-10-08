"""Unit tests for Tai Khamyang grammar, classifiers, numerals, and naming."""

import unittest
import khamyang
from khamyang.grammar.classifiers import ClassifierEngine
from khamyang.grammar.naming import get_birth_name, generate_full_name
from khamyang.grammar.syntax import SentenceBuilder


class TestKhamyangGrammar(unittest.TestCase):

    def test_classifier_agreement(self):
        """Test Tai Noun + Numeral + Classifier construction."""
        phrase1 = ClassifierEngine.quantify("maa1", 2)
        self.assertEqual(phrase1, "maa1 sɔŋ1 to1")

        phrase2 = ClassifierEngine.quantify("hɯn1", 1)
        self.assertEqual(phrase2, "hɯn1 nɯŋ5 lung1")

        phrase3 = ClassifierEngine.quantify("khon1", 3)
        self.assertEqual(phrase3, "khon1 saam1 ko5")

    def test_birth_order_naming(self):
        """Test traditional birth-order naming for sons and daughters."""
        son1 = get_birth_name(1, "male")
        self.assertEqual(son1.name_roman, "Aai")

        daughter1 = get_birth_name(1, "female")
        self.assertEqual(daughter1.name_roman, "Ye")

        full = generate_full_name(1, "male", personal_name="Deben", clan="Chowlik")
        self.assertEqual(full["full_roman"], "Chaw Aai Deben Chowlik")

    def test_numerals(self):
        """Test numeral generator."""
        self.assertEqual(khamyang.num_to_khamyang(1), "nɯŋ5")
        self.assertEqual(khamyang.num_to_khamyang(2), "sɔŋ1")
        self.assertEqual(khamyang.num_to_khamyang(10), "sip4")
        self.assertEqual(khamyang.num_to_khamyang(20), "saaw1")
        self.assertEqual(khamyang.num_to_khamyang(24), "saaw1 si5")
        self.assertEqual(khamyang.num_to_khamyang(100), "nɯŋ5 pak4")

    def test_sentence_builder(self):
        """Test SVO sentence construction with TAM markers."""
        sent = SentenceBuilder.build_simple_sentence(
            subject="kaw1",
            verb="kin1",
            obj="khaw3",
            tam="perfective",
        )
        self.assertEqual(sent["roman"], "kaw1 kin1 khaw3 yow3")


if __name__ == "__main__":
    unittest.main()
