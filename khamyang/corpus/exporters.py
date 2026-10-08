"""
Linguistic Data Exporters for Khamyang Corpus
=============================================
Exports annotated texts into formats used in computational linguistics:
- FLEx / LIFT XML
- ELAN (.eaf) XML structure
- LaTeX gb4e format
- Markdown and plain text
"""

from typing import List
import xml.etree.ElementTree as ET
from xml.dom import minidom
from khamyang.core.models import FolkText, InterlinearUnit
from khamyang.corpus.igt import InterlinearGloss


def export_to_latex(text: FolkText) -> str:
    """Exports a folk text into a LaTeX document using the gb4e package."""
    lines = [
        f"% Tai Khamyang Corpus: {text.title_english}",
        f"% Informant: {text.informant}, Village: {text.village}",
        "\\documentclass{article}",
        "\\usepackage[utf8]{inputenc}",
        "\\usepackage{gb4e}",
        "\\begin{document}",
        f"\\section*{{{text.title_english} ({text.title_khamyang})}}",
        f"\\paragraph{{{text.description}}}",
        "\\bigskip",
    ]

    for sent in text.sentences:
        lines.append(InterlinearGloss.to_latex_gb4e(sent))
        lines.append("\\medskip")

    lines.append("\\end{document}")
    return "\n".join(lines)


def export_to_elan_eaf(text: FolkText) -> str:
    """
    Exports a text into a basic ELAN EAF 3.0 XML template
    compatible with ELAN transcription software.
    """
    root = ET.Element("ANNOTATION_DOCUMENT", {
        "AUTHOR": "Khamyang Language Revitalization Initiative",
        "DATE": "2026-10-08",
        "FORMAT": "3.0",
        "VERSION": "3.0",
    })

    header = ET.SubElement(root, "HEADER", {"MEDIA_FILE": "", "TIME_UNITS": "milliseconds"})

    time_order = ET.SubElement(root, "TIME_ORDER")

    tier_source = ET.SubElement(root, "TIER", {
        "LINGUISTIC_TYPE_REF": "default-lt",
        "TIER_ID": "Khamyang-Orthography",
    })
    tier_gloss = ET.SubElement(root, "TIER", {
        "LINGUISTIC_TYPE_REF": "default-lt",
        "TIER_ID": "English-Gloss",
    })

    cur_time = 0
    time_slot_id = 1

    for idx, sent in enumerate(text.sentences, 1):
        t1_id = f"ts{time_slot_id}"
        t2_id = f"ts{time_slot_id + 1}"
        time_slot_id += 2

        ET.SubElement(time_order, "TIME_SLOT", {"TIME_SLOT_ID": t1_id, "TIME_VALUE": str(cur_time)})
        cur_time += 3000
        ET.SubElement(time_order, "TIME_SLOT", {"TIME_SLOT_ID": t2_id, "TIME_VALUE": str(cur_time)})

        ann1 = ET.SubElement(tier_source, "ANNOTATION")
        align1 = ET.SubElement(ann1, "ALIGNABLE_ANNOTATION", {
            "ANNOTATION_ID": f"a{idx}",
            "TIME_SLOT_REF1": t1_id,
            "TIME_SLOT_REF2": t2_id,
        })
        val1 = ET.SubElement(align1, "ANNOTATION_VALUE")
        val1.text = sent.text_roman

        ann2 = ET.SubElement(tier_gloss, "ANNOTATION")
        align2 = ET.SubElement(ann2, "ALIGNABLE_ANNOTATION", {
            "ANNOTATION_ID": f"ag{idx}",
            "TIME_SLOT_REF1": t1_id,
            "TIME_SLOT_REF2": t2_id,
        })
        val2 = ET.SubElement(align2, "ANNOTATION_VALUE")
        val2.text = sent.free_translation_en

    xml_str = ET.tostring(root, encoding="utf-8")
    parsed = minidom.parseString(xml_str)
    return parsed.toprettyxml(indent="  ")
