"""Unit tests for Interlinear Glossed Text (IGT) and Corpus."""

import unittest
from khamyang.corpus.texts import get_corpus
from khamyang.corpus.igt import InterlinearGloss
from khamyang.corpus.exporters import export_to_latex, export_to_elan_eaf


class TestKhamyangIGT(unittest.TestCase):

    def setUp(self):
        self.corpus = get_corpus()

    def test_corpus_texts_exist(self):
        texts = self.corpus.get_all()
        self.assertGreater(len(texts), 0)

    def test_igt_formatting(self):
        text = self.corpus.get_all()[0]
        sentence = text.sentences[0]
        formatted = InterlinearGloss.format_text(sentence)
        self.assertIn("pu5 yaa3", formatted)
        self.assertIn("ancestor", formatted)

    def test_latex_export(self):
        text = self.corpus.get_all()[0]
        latex = export_to_latex(text)
        self.assertIn("\\documentclass", latex)
        self.assertIn("\\gll", latex)

    def test_elan_export(self):
        text = self.corpus.get_all()[0]
        elan = export_to_elan_eaf(text)
        self.assertIn("ANNOTATION_DOCUMENT", elan)
        self.assertIn("Khamyang-Orthography", elan)


if __name__ == "__main__":
    unittest.main()
