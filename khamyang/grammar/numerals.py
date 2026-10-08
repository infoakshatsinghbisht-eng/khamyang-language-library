"""
Tai Khamyang Numeral System
===========================
Generates and parses Tai Khamyang cardinal numbers from 1 to 1,000,000.
Follows the Southwestern Tai decimal numeral system:
1: nɯŋ5 (isolated) / et4 (compound 11, 21, 31...)
2: sɔŋ1
3: saam1
4: si5
5: haa3
6: hok4
7: cet4
8: pet4
9: kaw3
10: sip4
20: saaw1
100: pak4 / hɔi3
1,000: heŋ1 / phan1
10,000: mɯn5
100,000: seen1
1,000,000: laan3
"""

from typing import Dict, List, Tuple

BASE_DIGITS_ROMAN: Dict[int, str] = {
    0: "suun1",
    1: "nɯŋ5",
    2: "sɔŋ1",
    3: "saam1",
    4: "si5",
    5: "haa3",
    6: "hok4",
    7: "cet4",
    8: "pet4",
    9: "kaw3",
}

BASE_DIGITS_LIKTAI: Dict[int, str] = {
    0: "သုၼ်",
    1: "ၼိုင်ႈ",
    2: "သွင်",
    3: "သၢမ်",
    4: "သီႇ",
    5: "ႁႃႈ",
    6: "ႁူၵ်း",
    7: "ၸဵတ်း",
    8: "ပႅတ်ႇ",
    9: "ၵဝ်ႈ",
}

BASE_DIGITS_ASSAMESE: Dict[int, str] = {
    0: "চুন",
    1: "নুং",
    2: "চং",
    3: "সাম",
    4: "চি",
    5: "হা",
    6: "হক",
    7: "চেত",
    8: "পেত",
    9: "কাও",
}

# Tai numeral digits (Myanmar block symbols often used in Tai manuscripts)
LIKTAI_DIGIT_GLYPHS: Dict[int, str] = {
    0: "႐",
    1: "႞",
    2: "႟",
    3: "၃",
    4: "၄",
    5: "၅",
    6: "၆",
    7: "၇",
    8: "၈",
    9: "၉",
}


def num_to_khamyang(n: int, script: str = "roman") -> str:
    """
    Converts an integer (0 to 1,000,000) into Tai Khamyang words.

    Args:
        n: Integer number.
        script: 'roman', 'liktai', or 'assamese'.
    """
    if n < 0:
        raise ValueError("Negative numbers not supported")
    if n == 0:
        return BASE_DIGITS_ROMAN[0] if script == "roman" else (
            BASE_DIGITS_LIKTAI[0] if script == "liktai" else BASE_DIGITS_ASSAMESE[0]
        )

    parts: List[str] = []

    # Millions: laan3
    if n >= 1_000_000:
        millions = n // 1_000_000
        n %= 1_000_000
        parts.append(f"{num_to_khamyang(millions, 'roman')} laan3")

    # Hundred thousands: seen1
    if n >= 100_000:
        h_thousands = n // 100_000
        n %= 100_000
        parts.append(f"{BASE_DIGITS_ROMAN[h_thousands]} seen1")

    # Ten thousands: mɯn5
    if n >= 10_000:
        ten_thousands = n // 10_000
        n %= 10_000
        parts.append(f"{BASE_DIGITS_ROMAN[ten_thousands]} mɯn5")

    # Thousands: heŋ1 / phan1
    if n >= 1_000:
        thousands = n // 1_000
        n %= 1_000
        parts.append(f"{BASE_DIGITS_ROMAN[thousands]} heŋ1")

    # Hundreds: pak4
    if n >= 100:
        hundreds = n // 100
        n %= 100
        parts.append(f"{BASE_DIGITS_ROMAN[hundreds]} pak4")

    # Tens and units
    if n >= 20:
        tens = n // 10
        units = n % 10
        if tens == 2:
            tens_word = "saaw1"
        else:
            tens_word = f"{BASE_DIGITS_ROMAN[tens]} sip4"

        if units == 0:
            parts.append(tens_word)
        elif units == 1:
            parts.append(f"{tens_word} et4")
        else:
            parts.append(f"{tens_word} {BASE_DIGITS_ROMAN[units]}")
    elif n >= 10:
        units = n % 10
        if units == 0:
            parts.append("sip4")
        elif units == 1:
            parts.append("sip4 et4")
        else:
            parts.append(f"sip4 {BASE_DIGITS_ROMAN[units]}")
    elif n > 0:
        parts.append(BASE_DIGITS_ROMAN[n])

    roman_res = " ".join(parts)
    if script == "roman":
        return roman_res
    elif script in ("liktai", "lik_tai"):
        from khamyang.transliteration.converter import roman_to_liktai
        return roman_to_liktai(roman_res)
    elif script in ("assamese", "as"):
        from khamyang.transliteration.converter import roman_to_assamese
        return roman_to_assamese(roman_res)
    return roman_res


def khamyang_to_num(khamyang_str: str) -> int:
    """
    Parses a Tai Khamyang number phrase back into an integer.
    Supports basic compounds from 0 up to 1000.
    """
    tokens = khamyang_str.strip().lower().split()
    total = 0
    current = 0

    rev_digits = {v: k for k, v in BASE_DIGITS_ROMAN.items()}
    rev_digits["et4"] = 1
    rev_digits["saaw1"] = 20

    for tok in tokens:
        if tok in rev_digits:
            val = rev_digits[tok]
            if val == 20:
                current += 20
            else:
                current += val
        elif tok == "sip4":
            current = 10 if current == 0 else current * 10
        elif tok == "pak4":
            mult = current if current > 0 else 1
            total += mult * 100
            current = 0
        elif tok in ("heŋ1", "phan1"):
            mult = current if current > 0 else 1
            total += mult * 1000
            current = 0
    total += current
    return total
