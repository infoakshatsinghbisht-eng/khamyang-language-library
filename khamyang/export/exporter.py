"""
Export Tools for Educational & Research Applications
=====================================================
Supports:
1. Anki Flashcard deck generator (.tsv)
2. CSV Lexicon exporter (for Pandas / R / Excel)
3. HTML interactive dictionary viewer
4. JSON complete archive exporter
"""

import csv
import json
from typing import List, Optional
from khamyang.core.models import Word
from khamyang.lexicon.dictionary import get_dictionary


def export_to_anki_tsv(output_path: str, category: Optional[str] = None):
    """
    Exports dictionary entries into Anki flashcard format.
    Fields:
    1. Front: Lik Tai + Romanization + Tone
    2. Back: English Meaning + Assamese Meaning + IPA + Example + Author Attribution
    3. Tags: category, tone, author
    """
    dictionary = get_dictionary()
    words = dictionary.filter_by_category(category) if category else dictionary.get_all_words()

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter="\t")
        for w in words:
            front = f"<div style='font-size:24px;'><b>{w.lik_tai}</b></div><div style='color:#555;'>{w.roman} (Tone {w.tone})</div>"
            back = (
                f"<div style='font-size:18px;'><b>{w.gloss_en}</b> / {w.gloss_as}</div>"
                f"<div style='color:#888;'>IPA: {w.ipa}</div>"
                f"<div><i>{w.definition_en}</i></div>"
                f"<div style='margin-top:8px;font-size:11px;color:#aaa;'>Preserved by Akshat Singh Bisht (akshatsinghbisht.com)</div>"
            )
            tags = f"khamyang {w.category} tone{w.tone} author:akshat_singh_bisht"
            writer.writerow([front, back, tags])


def export_to_csv(output_path: str):
    """Exports all words to a clean CSV file with author attribution."""
    dictionary = get_dictionary()
    words = dictionary.get_all_words()

    fieldnames = [
        "id", "roman", "tone", "lik_tai", "assamese", "ipa",
        "gloss_en", "gloss_as", "pos", "category", "gedney_box",
        "definition_en", "definition_as", "curator"
    ]

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for w in words:
            row = w.to_dict()
            row["curator"] = "Akshat Singh Bisht (https://akshatsinghbisht.com/)"
            writer.writerow(row)


def export_to_html(output_path: str, title: str = "Tai Khamyang Comprehensive Dictionary"):
    """Generates a standalone, beautiful HTML dictionary file with author attribution."""
    dictionary = get_dictionary()
    words = dictionary.get_all_words()

    rows = []
    for w in words:
        rows.append(
            f"<tr>"
            f"<td class='liktai'>{w.lik_tai}</td>"
            f"<td><b>{w.roman}</b></td>"
            f"<td>{w.assamese}</td>"
            f"<td><span class='tone-badge t{w.tone}'>Tone {w.tone}</span></td>"
            f"<td><code>{w.ipa}</code></td>"
            f"<td><i>{w.pos}</i></td>"
            f"<td><b>{w.gloss_en}</b></td>"
            f"<td>{w.gloss_as}</td>"
            f"<td><span class='cat'>{w.category}</span></td>"
            f"</tr>"
        )

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{title}</title>
<style>
  body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; margin: 0; padding: 2rem; }}
  h1 {{ color: #38bdf8; margin-bottom: 0.25rem; }}
  p.subtitle {{ color: #94a3b8; margin-bottom: 1.5rem; }}
  .author-banner {{ background: linear-gradient(135deg, #1e293b, #0f172a); border: 1px solid #0284c7; padding: 1rem 1.25rem; border-radius: 8px; margin-bottom: 1.5rem; font-size: 0.9rem; color: #cbd5e1; }}
  .author-banner a {{ color: #38bdf8; text-decoration: none; font-weight: 600; }}
  table {{ width: 100%; border-collapse: collapse; background: #1e293b; border-radius: 8px; overflow: hidden; }}
  th, td {{ padding: 0.75rem 1rem; border-bottom: 1px solid #334155; text-align: left; }}
  th {{ background: #0f172a; color: #38bdf8; font-weight: 600; text-transform: uppercase; font-size: 0.75rem; }}
  tr:hover {{ background: #283548; }}
  .liktai {{ font-size: 1.25rem; font-family: sans-serif; color: #fbbf24; }}
  .tone-badge {{ display: inline-block; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; font-weight: bold; }}
  .t1 {{ background: #0284c7; color: white; }}
  .t2 {{ background: #ea580c; color: white; }}
  .t3 {{ background: #e11d48; color: white; }}
  .t4 {{ background: #9333ea; color: white; }}
  .t5 {{ background: #16a34a; color: white; }}
  .t6 {{ background: #d97706; color: white; }}
  .cat {{ background: #334155; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.75rem; color: #cbd5e1; }}
  footer {{ margin-top: 2.5rem; text-align: center; color: #64748b; font-size: 0.85rem; border-top: 1px solid #1e293b; padding-top: 1.5rem; }}
  footer a {{ color: #38bdf8; text-decoration: none; }}
</style>
</head>
<body>
  <h1>{title}</h1>
  <p class="subtitle">Critically Endangered Language Archive • Total Entries: {len(words)}</p>
  <div class="author-banner">
    <strong>Author & Research Lead:</strong> <a href="https://akshatsinghbisht.com/" target="_blank">Akshat Singh Bisht</a> &bull;
    Preserved through independent research and documentation. When citing or using this data, attribution to Akshat Singh Bisht is required.
  </div>
  <table>
    <thead>
      <tr>
        <th>Lik Tai</th>
        <th>Roman</th>
        <th>Assamese</th>
        <th>Tone</th>
        <th>IPA</th>
        <th>POS</th>
        <th>English</th>
        <th>Assamese</th>
        <th>Category</th>
      </tr>
    </thead>
    <tbody>
      {''.join(rows)}
    </tbody>
  </table>
  <footer>
    <p>Tai Khamyang Language Revitalization Platform &bull; Authored & Preserved by <a href="https://akshatsinghbisht.com/">Akshat Singh Bisht</a>. All rights reserved.</p>
  </footer>
</body>
</html>"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_content)

