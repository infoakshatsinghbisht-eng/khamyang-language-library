"""Tests for Tai Khamyang scholarly bibliography and archive downloader engine."""

import unittest
from khamyang.scraper.downloader import BibliographyManager


class TestBibliographyManager(unittest.TestCase):

    def test_all_entries_loaded(self):
        entries = BibliographyManager.all_entries()
        self.assertGreaterEqual(len(entries), 15)

    def test_get_entry_by_id(self):
        morey_book = BibliographyManager.get_entry("morey2005grammar")
        self.assertIsNotNone(morey_book)
        self.assertEqual(morey_book["year"], 2005)
        self.assertIn("Stephen Morey", morey_book["authors"])

    def test_search_morey(self):
        results = BibliographyManager.search("Morey")
        self.assertGreaterEqual(len(results), 3)

    def test_search_nath(self):
        results = BibliographyManager.search("Palash Kumar Nath")
        self.assertGreaterEqual(len(results), 2)

    def test_filter_by_type(self):
        books = BibliographyManager.filter_by_type("book")
        self.assertGreaterEqual(len(books), 4)
        archives = BibliographyManager.filter_by_type("archive")
        self.assertGreaterEqual(len(archives), 3)

    def test_to_bibtex_entry(self):
        entry = BibliographyManager.get_entry("morey2005grammar")
        bib = BibliographyManager.to_bibtex_entry(entry)
        self.assertIn("@book{morey2005grammar,", bib)
        self.assertIn("author = {Stephen Morey},", bib)

    def test_export_all_bibtex(self):
        all_bib = BibliographyManager.export_all_bibtex()
        self.assertIn("@book{morey2005grammar", all_bib)
        self.assertIn("@misc{paradisec_sdm03", all_bib)

    def test_format_apa(self):
        entry = BibliographyManager.get_entry("morey2008tones")
        apa = BibliographyManager.format_apa(entry)
        self.assertIn("Stephen Morey (2008)", apa)
        self.assertIn("Linguistics of the Tibeto-Burman Area", apa)


    def test_generate_markdown_bibliography(self):
        md = BibliographyManager.generate_markdown_bibliography()
        self.assertIn("# 📚 Tai Khamyang (ksu) Scholarly Bibliography", md)
        self.assertIn("Foundational Books & Grammars", md)


if __name__ == "__main__":
    unittest.main()
