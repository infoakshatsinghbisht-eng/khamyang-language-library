"""
Tai Khamyang Script Transliteration Tutorial
============================================
Run with: python -X utf8 examples/03_transliteration_and_scripts.py
"""

from khamyang.transliteration.converter import (
    roman_to_liktai,
    roman_to_assamese,
    roman_to_ipa,
    liktai_to_roman,
    transliterate,
)

print("=" * 65)
print("MULTI-SCRIPT TRANSLITERATION ENGINE")
print("=" * 65)

phrases = [
    "nam6",
    "khaw3",
    "maan3 paa1 waai6",
    "kaw1 kin1 khaw3 yow3",
    "pu5 yaa3 haw1 maa1 thaang1 doi1 pat4 kai1",
]

for phr in phrases:
    lik_tai = roman_to_liktai(phr)
    assamese = roman_to_assamese(phr)
    ipa = roman_to_ipa(phr)

    print(f"Roman:     {phr}")
    print(f"Lik Tai:   {lik_tai}")
    print(f"Assamese:  {assamese}")
    print(f"IPA:       {ipa}")
    print("-" * 65)

# Bidirectional roundtrip test
lik_sample = "ၵဝ် ၵိၼ် ၶဝ်ႈ"
back_to_roman = liktai_to_roman(lik_sample)
print(f"Reverse Transliteration:")
print(f"Lik Tai Input:  {lik_sample}")
print(f"Romanized Back: {back_to_roman}")
print("=" * 65)
