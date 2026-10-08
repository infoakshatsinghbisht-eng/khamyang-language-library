"""
Tai Khamyang Grammar, Classifiers & Naming Tutorial
===================================================
Run with: python -X utf8 examples/04_grammar_and_classifiers.py
"""

from khamyang.grammar.classifiers import ClassifierEngine, CLASSIFIERS
from khamyang.grammar.naming import (
    get_birth_name,
    list_birth_names,
    generate_full_name,
    KHAMYANG_CLANS,
)
from khamyang.grammar.numerals import num_to_khamyang, khamyang_to_num
from khamyang.grammar.syntax import SentenceBuilder

print("=" * 65)
print("1. CLASSIFIER AGREEMENT ENGINE (Noun + Numeral + Classifier)")
print("=" * 65)

test_nouns = [
    ("maa1", 2, "two dogs"),
    ("nok4", 3, "three birds"),
    ("paa1", 1, "one fish"),
    ("khon1", 4, "four people"),
    ("luk4", 2, "two children"),
    ("hɯn1", 5, "five houses"),
    ("ton3 mai6", 1, "one tree"),
    ("mit4", 2, "two knives"),
    ("lik4", 3, "three books"),
    ("nam6 saa1", 2, "two cups of tea"),
]

for noun, count, gloss in test_nouns:
    phrase = ClassifierEngine.quantify(noun, count)
    clf = ClassifierEngine.get_classifier(noun)
    print(f"{gloss:<20} -> {phrase:<22} [Classifier: {clf.roman} ({clf.meaning})]")

print("\n" + "=" * 65)
print("2. TRADITIONAL BIRTH-ORDER NAMING (1st to 8th Born)")
print("=" * 65)

print("SONS (MALE):")
for i in range(1, 9):
    bn = get_birth_name(i, "male")
    print(f"  #{i} {bn.name_roman:<8} Lik Tai: {bn.lik_tai:<6} Assamese: {bn.assamese:<6} -> {bn.meaning}")

print("\nDAUGHTERS (FEMALE):")
for i in range(1, 9):
    bn = get_birth_name(i, "female")
    print(f"  #{i} {bn.name_roman:<8} Lik Tai: {bn.lik_tai:<6} Assamese: {bn.assamese:<6} -> {bn.meaning}")

print("\nFULL NAME GENERATION:")
full1 = generate_full_name(1, "male", personal_name="Deben", clan="Chowlik")
print(f"  • {full1['full_roman']} ({full1['meaning']}, Clan: {full1['clan']})")

full2 = generate_full_name(2, "female", personal_name="Mainu", clan="Thomung")
print(f"  • {full2['full_roman']} ({full2['meaning']}, Clan: {full2['clan']})")

print("\n" + "=" * 65)
print("3. TAI NUMERAL GENERATOR")
print("=" * 65)
numbers = [1, 2, 5, 10, 11, 20, 24, 50, 100, 365, 1000]
for n in numbers:
    print(f"  {n:>5} -> {num_to_khamyang(n):<25} (Lik Tai: {num_to_khamyang(n, 'liktai')})")

print("\n" + "=" * 65)
print("4. SVO SENTENCE BUILDER WITH TAM MARKERS")
print("=" * 65)
s1 = SentenceBuilder.build_simple_sentence("kaw1", "kin1", "khaw3", tam="perfective")
print(f"Perfective:  {s1['roman']} (Lik Tai: {s1['lik_tai']})")

s2 = SentenceBuilder.build_simple_sentence("man1", "pai1", "maan3", tam="future")
print(f"Future:      {s2['roman']}")

s3 = SentenceBuilder.build_simple_sentence("tu1 haw1", "kin1", "nam6 saa1", tam="progressive")
print(f"Progressive: {s3['roman']}")

s4 = SentenceBuilder.build_simple_sentence("kaw1", "hu3", tam=None, negated=True)
print(f"Negative:    {s4['roman']}")

s5 = SentenceBuilder.build_simple_sentence("maɯ2", "yu5 di1", tam=None, is_question=True)
print(f"Question:    {s5['roman']}")
print("=" * 65)
