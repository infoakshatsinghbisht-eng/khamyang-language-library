"""
Interlinear Glossed Text (IGT) Engine
=====================================
Formats and parses 5-line interlinear linguistic glosses
following the Leipzig Glossing Rules:
Line 1: Vernacular Source (Lik Tai & Romanized)
Line 2: Morpheme Breakdown
Line 3: Grammatical Glosses (e.g. 1SG, CLF, PRF, NEG)
Line 4: Free English Translation
Line 5: Free Assamese Translation
"""

from typing import List, Dict, Any, Optional
from khamyang.core.models import InterlinearUnit


class InterlinearGloss:
    """Formatter and validator for interlinear glossed sentences."""

    @staticmethod
    def format_text(unit: InterlinearUnit, include_assamese: bool = True) -> str:
        """Renders standard ASCII-aligned interlinear gloss."""
        # Ensure morphemes and glosses align in column width
        morphemes = unit.morphemes
        glosses = unit.glosses

        max_len = max(len(morphemes), len(glosses))
        padded_morphemes = morphemes + [""] * (max_len - len(morphemes))
        padded_glosses = glosses + [""] * (max_len - len(glosses))

        col_widths = []
        for m, g in zip(padded_morphemes, padded_glosses):
            col_widths.append(max(len(m), len(g)) + 2)

        line_morpheme = "".join(m.ljust(w) for m, w in zip(padded_morphemes, col_widths))
        line_gloss = "".join(g.ljust(w) for g, w in zip(padded_glosses, col_widths))

        lines = [
            f"Source (Lik Tai):   {unit.lik_tai}",
            f"Romanization:       {unit.text_roman}",
            f"Morphemes:          {line_morpheme.strip()}",
            f"Glosses:            {line_gloss.strip()}",
            f"English:            '{unit.free_translation_en}'",
        ]
        if include_assamese and unit.free_translation_as:
            lines.append(f"Assamese:           '{unit.free_translation_as}'")

        return "\n".join(lines)

    @staticmethod
    def to_latex_gb4e(unit: InterlinearUnit) -> str:
        """Generates LaTeX code compatible with the gb4e package."""
        m_str = " ".join(unit.morphemes)
        g_str = " ".join(unit.glosses)
        return (
            "\\begin{exe}\n"
            "\\ex\n"
            f"\\gll {m_str} \\\\\n"
            f"     {g_str} \\\\\n"
            f"\\glt `{unit.free_translation_en}' (Assamese: `{unit.free_translation_as}')\n"
            "\\end{exe}"
        )

    @staticmethod
    def to_markdown(unit: InterlinearUnit) -> str:
        """Renders GitHub Markdown table format."""
        header = "| " + " | ".join(unit.morphemes) + " |"
        sep = "| " + " | ".join(["---"] * len(unit.morphemes)) + " |"
        gloss_row = "| " + " | ".join(unit.glosses) + " |"

        return (
            f"**Lik Tai:** `{unit.lik_tai}`  \n"
            f"**Romanized:** *{unit.text_roman}*  \n\n"
            f"{header}\n{sep}\n{gloss_row}\n\n"
            f"> **EN:** {unit.free_translation_en}  \n"
            f"> **AS:** {unit.free_translation_as}"
        )
