"""
Tai Khamyang Fieldwork & Corpus Export Tutorial
===============================================
Run with: python -X utf8 examples/05_fieldwork_and_corpus_export.py
"""

from khamyang.phrases.phrasebook import get_phrasebook
from khamyang.corpus.texts import get_corpus
from khamyang.corpus.igt import InterlinearGloss
from khamyang.corpus.exporters import export_to_latex, export_to_elan_eaf

print("=" * 65)
print("1. FIELDWORK ELICITATION & CONSENT PHRASES")
print("=" * 65)

pb = get_phrasebook()
fieldwork_phrases = pb.get_by_category("fieldwork")

for p in fieldwork_phrases[:5]:
    print(f"EN:        {p.english}")
    print(f"Khamyang:  {p.roman} ({p.lik_tai})")
    print(f"Assamese:  {p.assamese_trans}")
    print(f"Context:   {p.context}")
    print("-" * 65)

print("\n" + "=" * 65)
print("2. ANNOTATED CORPUS: INTERLINEAR GLOSSED TEXT (IGT)")
print("=" * 65)

corpus = get_corpus()
texts = corpus.get_all()

text1 = texts[0]
print(f"Title: {text1.title_english} ({text1.title_khamyang})")
print(f"Informant: {text1.informant} | Location: {text1.village}\n")

for i, sent in enumerate(text1.sentences, 1):
    print(f"--- Sentence {i} ---")
    print(InterlinearGloss.format_text(sent))
    print()

print("=" * 65)
print("3. EXPORTING TO LATEX (gb4e package format)")
print("=" * 65)
latex_sample = export_to_latex(text1)
print(latex_sample[:350] + "\n... [truncated] ...\n\\end{document}")

print("\n" + "=" * 65)
print("4. EXPORTING TO ELAN EAF XML FORMAT")
print("=" * 65)
elan_sample = export_to_elan_eaf(text1)
print(elan_sample[:300] + "\n... [truncated] ...")
print("=" * 65)
