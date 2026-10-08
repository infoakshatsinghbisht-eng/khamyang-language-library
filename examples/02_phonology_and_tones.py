"""
Tai Khamyang Phonology & 6-Tone Engine Tutorial
===============================================
Run with: python -X utf8 examples/02_phonology_and_tones.py
"""

from khamyang.phonology.tones import ToneSystem, get_tone, gedney_lookup, TONES
from khamyang.phonology.phonemes import parse_syllable
from khamyang.phonology.synth import generate_tone_audio_params

print("=" * 65)
print("TAI KHAMYANG 6-TONE SYSTEM (STEPHEN MOREY 2005)")
print("=" * 65)

for i in range(1, 7):
    t = get_tone(i)
    features = []
    if t.creaky:
        features.append("Creaky Voice")
    if t.glottalized:
        features.append("Glottal Stop [ʔ]")
    feat_str = f"({', '.join(features)})" if features else "(Modal)"

    print(f"Tone {t.number}: {t.name:<25} Pitch: {t.pitch_chao:<4} IPA: {t.ipa_symbol:<4} {feat_str}")
    print(f"  → Gedney: {', '.join(t.gedney_cells)}")
    print(f"  → {t.description}\n")

print("-" * 65)
print("GEDNEY TONE BOX LOOKUP")
print(f"Proto-Tai *A1  -> Tone {gedney_lookup('A', 1)} [33]")
print(f"Proto-Tai *A2  -> Tone {gedney_lookup('A', 2)} [35]")
print(f"Proto-Tai *B2  -> Tone {gedney_lookup('B', 2)} [54]")
print(f"Proto-Tai *C1  -> Tone {gedney_lookup('C', 1)} [54ʔ]")
print(f"Proto-Tai *C3  -> Tone {gedney_lookup('C', 3)} [31]")

print("-" * 65)
print("SYLLABLE PHONETIC PARSING")
syllables = ["kwaai1", "nam6", "luk4", "tsaw3", "hɯn1"]
for syl in syllables:
    p = parse_syllable(syl)
    print(f"Syllable: {syl:<8} Onset: {p.onset:<3} Medial: {str(p.medial):<5} Nucleus: {p.nucleus:<4} Coda: {str(p.coda):<4} Tone: {p.tone} IPA: {p.ipa}")

print("-" * 65)
print("AUDIO SYNTHESIS FREQUENCY CONTOUR (Tone 4 [54ʔ])")
audio_data = generate_tone_audio_params(4, base_frequency=165.0)
for pt in audio_data["points"]:
    print(f"  Time: {pt['time']:.2f}s  -> Frequency: {pt['freq']:.1f} Hz")
print("=" * 65)
