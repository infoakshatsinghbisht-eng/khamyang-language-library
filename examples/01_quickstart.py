"""
Tai Khamyang Language Library - Quickstart Tutorial
===================================================
Run with: python -X utf8 examples/01_quickstart.py
"""

import sys
import khamyang

print("=" * 60)
print(f"Tai Khamyang (ksu) Library v{khamyang.__version__}")
print("=" * 60)

# 1. Access the dictionary
dict_db = khamyang.get_dictionary()
print(f"Total vocabulary items: {len(dict_db)}")

# 2. Look up a core word
word = dict_db.lookup("nam6")[0]
print(f"\nWord Details for 'nam6':")
print(f"  • Romanized:     {word.roman}")
print(f"  • Lik Tai:       {word.lik_tai}")
print(f"  • Assamese:      {word.assamese}")
print(f"  • IPA:           {word.ipa}")
print(f"  • Tone:          Tone {word.tone}")
print(f"  • Meaning (EN):  {word.gloss_en}")
print(f"  • Meaning (AS):  {word.gloss_as}")
print(f"  • Cognates:      {word.cognates}")

# 3. Transliterate across scripts
roman_text = "kaw1 kin1 khaw3 yow3"
lik_tai = khamyang.transliterate(roman_text, "roman", "liktai")
assamese = khamyang.transliterate(roman_text, "roman", "assamese")
ipa = khamyang.transliterate(roman_text, "roman", "ipa")

print(f"\nScript Transliteration:")
print(f"  • Roman:    {roman_text}")
print(f"  • Lik Tai:  {lik_tai}")
print(f"  • Assamese: {assamese}")
print(f"  • IPA:      {ipa}")

# 4. Tai Numeral phrase
num_str = khamyang.num_to_khamyang(24)
print(f"\nTai Numeral 24: {num_str}")

# 5. Traditional naming
birth_name = khamyang.get_birth_name(1, gender="male")
print(f"\nTraditional 1st-born son name: {birth_name.name_roman} ({birth_name.meaning})")
print("=" * 60)
