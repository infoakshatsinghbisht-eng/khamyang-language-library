"""
Audio Synthesizer Parameters and Pitch Profile Generator
=========================================================
Generates Web Audio API parameter sequences and acoustic pitch models
for the six lexical tones of Tai Khamyang.
"""

from typing import Dict, List, Any
from khamyang.phonology.tones import TONES, KhamyangTone


def generate_tone_audio_params(tone_num: int, base_frequency: float = 165.0, duration_sec: float = 0.5) -> Dict[str, Any]:
    """
    Generates Web Audio API synthesis parameter points for a given tone.
    Used by the interactive web application to synthesize pitch contours in real-time.
    """
    tone = TONES.get(tone_num, TONES[1])
    contour = tone.f0_contour_normalized
    num_points = len(contour)
    time_step = duration_sec / (num_points - 1)

    points: List[Dict[str, float]] = []
    for i, mult in enumerate(contour):
        freq = base_frequency * mult
        time = i * time_step
        points.append({"time": round(time, 3), "freq": round(freq, 2)})

    return {
        "tone_number": tone.number,
        "tone_name": tone.name,
        "pitch_contour": tone.pitch_chao,
        "ipa_symbol": tone.ipa_symbol,
        "duration_sec": duration_sec,
        "base_hz": base_frequency,
        "creaky_voice": tone.creaky,
        "glottal_stop": tone.glottalized,
        "points": points,
    }


def get_all_tone_audio_profiles(base_frequency: float = 165.0) -> List[Dict[str, Any]]:
    """Returns audio synthesis curves for all 6 tones."""
    return [generate_tone_audio_params(t, base_frequency) for t in range(1, 7)]
