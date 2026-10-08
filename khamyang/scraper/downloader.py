"""
Tai Khamyang Scholarly Bibliography and Archive Downloader
Provides programmatic searching, BibTeX generation, citation formatting,
and resource access for books, articles, folklore, songs, and audio archives.
"""

import json
import os
import urllib.request
import urllib.error
from typing import Dict, List, Optional, Any


class BibliographyManager:
    """
    Manages scholarly books, papers, articles, and archive collections
    for the Tai Khamyang language.
    """

    _data_cache: Optional[List[Dict[str, Any]]] = None

    @classmethod
    def _load_data(cls) -> List[Dict[str, Any]]:
        if cls._data_cache is None:
            path = os.path.join(os.path.dirname(__file__), "..", "data", "bibliography.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    cls._data_cache = json.load(f)
            else:
                cls._data_cache = []
        return cls._data_cache

    @classmethod
    def all_entries(cls) -> List[Dict[str, Any]]:
        """Returns all bibliographic entries."""
        return cls._load_data()

    @classmethod
    def get_entry(cls, entry_id: str) -> Optional[Dict[str, Any]]:
        """Finds entry by unique ID (e.g. 'morey2005grammar')."""
        eid = entry_id.strip().lower()
        for e in cls._load_data():
            if e["id"].lower() == eid:
                return e
        return None

    @classmethod
    def search(cls, query: str) -> List[Dict[str, Any]]:
        """Searches across titles, authors, keywords, descriptions, and publishers."""
        q = query.strip().lower()
        results = []
        for e in cls._load_data():
            authors_str = " ".join(e.get("authors", [])).lower()
            keywords_str = " ".join(e.get("keywords", [])).lower()
            if (
                q in e.get("title", "").lower()
                or q in authors_str
                or q in keywords_str
                or q in e.get("description", "").lower()
                or q in str(e.get("year", ""))
                or q in e.get("entry_type", "").lower()
            ):
                results.append(e)
        return results

    @classmethod
    def filter_by_type(cls, entry_type: str) -> List[Dict[str, Any]]:
        """Filters entries by type ('book', 'article', 'archive', 'web_resource', 'chapter')."""
        t = entry_type.strip().lower()
        return [e for e in cls._load_data() if e.get("entry_type") == t]

    @classmethod
    def to_bibtex_entry(cls, entry: Dict[str, Any]) -> str:
        """Converts an entry to standard BibTeX format."""
        etype = entry.get("entry_type", "misc")
        bib_type = "misc"
        if etype == "book":
            bib_type = "book"
        elif etype == "article":
            bib_type = "article"
        elif etype == "chapter":
            bib_type = "incollection"
        elif etype in ("archive", "web_resource"):
            bib_type = "misc"

        eid = entry.get("id", "ref")
        lines = [f"@{bib_type}{{{eid},"]
        
        # Title
        lines.append(f'  title = {{{entry.get("title")}}},')
        
        # Authors
        authors = " and ".join(entry.get("authors", ["Tai Khamyang Community"]))
        lines.append(f'  author = {{{authors}}},')
        
        # Year
        if "year" in entry:
            lines.append(f'  year = {{{entry["year"]}}},')

        # Journal / Booktitle / Publisher
        if "journal" in entry:
            lines.append(f'  journal = {{{entry["journal"]}}},')
        if "booktitle" in entry:
            lines.append(f'  booktitle = {{{entry["booktitle"]}}},')
        if "publisher" in entry:
            lines.append(f'  publisher = {{{entry["publisher"]}}},')
        if "volume" in entry:
            lines.append(f'  volume = {{{entry["volume"]}}},')
        if "number" in entry:
            lines.append(f'  number = {{{entry["number"]}}},')
        if "pages" in entry:
            lines.append(f'  pages = {{{entry["pages"]}}},')
        if "doi" in entry:
            lines.append(f'  doi = {{{entry["doi"]}}},')
        if "url" in entry:
            lines.append(f'  url = {{{entry["url"]}}},')
        if "isbn" in entry:
            lines.append(f'  isbn = {{{entry["isbn"]}}},')
            
        lines.append("}")
        return "\n".join(lines)

    @classmethod
    def export_all_bibtex(cls) -> str:
        """Exports the entire bibliography as a consolidated BibTeX file content."""
        entries = cls.all_entries()
        return "\n\n".join(cls.to_bibtex_entry(e) for e in entries)

    @classmethod
    def format_apa(cls, entry: Dict[str, Any]) -> str:
        """Formats an entry in APA citation style."""
        authors = ", ".join(entry.get("authors", ["Unknown"]))
        year = entry.get("year", "n.d.")
        title = entry.get("title", "")
        
        etype = entry.get("entry_type", "")
        if etype == "book":
            pub = entry.get("publisher", "")
            return f"{authors} ({year}). *{title}*. {pub}."
        elif etype == "article":
            journal = entry.get("journal", "")
            vol = entry.get("volume", "")
            pages = entry.get("pages", "")
            vol_str = f", {vol}" if vol else ""
            pages_str = f", {pages}" if pages else ""
            return f"{authors} ({year}). {title}. *{journal}*{vol_str}{pages_str}."
        elif etype == "chapter":
            book = entry.get("booktitle", "")
            ed = entry.get("editor", "")
            pub = entry.get("publisher", "")
            return f"{authors} ({year}). {title}. In {ed} (Ed.), *{book}*. {pub}."
        else:
            url = entry.get("url", "")
            url_str = f" Retrieved from {url}" if url else ""
            return f"{authors} ({year}). *{title}*. {url_str}"

    @classmethod
    def generate_markdown_bibliography(cls) -> str:
        """Generates a complete, structured GitHub-Flavored Markdown bibliography document."""
        entries = cls.all_entries()
        md = []
        md.append("# 📚 Tai Khamyang (ksu) Scholarly Bibliography & Resource Archive\n")
        md.append(
            "> Curated open-access books, academic research articles, oral folklore recordings, "
            "traditional songs, and archival collections for the endangered Tai Khamyang language of Assam, India.\n"
        )
        md.append("## Table of Contents\n")
        md.append("- [1. Foundational Books & Grammars](#1-foundational-books--grammars)")
        md.append("- [2. Research Articles & Chapters](#2-research-articles--chapters)")
        md.append("- [3. Digital Repositories & Audio Archives](#3-digital-repositories--audio-archives)")
        md.append("- [4. Online Dictionaries & Portals](#4-online-dictionaries--portals)\n")

        # Categorize
        books = [e for e in entries if e.get("entry_type") == "book"]
        articles = [e for e in entries if e.get("entry_type") in ("article", "chapter")]
        archives = [e for e in entries if e.get("entry_type") == "archive"]
        web = [e for e in entries if e.get("entry_type") == "web_resource"]

        md.append("## 1. Foundational Books & Grammars\n")
        for b in books:
            md.append(f"### {b['title']} ({b['year']})")
            md.append(f"- **Authors**: {', '.join(b.get('authors', []))}")
            md.append(f"- **Publisher**: {b.get('publisher', '')}")
            if "isbn" in b:
                md.append(f"- **ISBN**: `{b['isbn']}`")
            if "url" in b:
                md.append(f"- **Access URL**: [{b['url']}]({b['url']})")
            md.append(f"- **Summary**: {b.get('description', '')}\n")

        md.append("## 2. Research Articles & Chapters\n")
        for a in articles:
            md.append(f"### {a['title']} ({a['year']})")
            md.append(f"- **Authors**: {', '.join(a.get('authors', []))}")
            if "journal" in a:
                md.append(f"- **Journal**: *{a['journal']}* (Vol. {a.get('volume', '')}, pp. {a.get('pages', '')})")
            if "booktitle" in a:
                md.append(f"- **Book**: *{a['booktitle']}*")
            if "url" in a:
                md.append(f"- **Direct Link**: [{a['url']}]({a['url']})")
            md.append(f"- **Summary**: {a.get('description', '')}\n")

        md.append("## 3. Digital Repositories & Audio Archives\n")
        for ar in archives:
            md.append(f"### 🎙️ {ar['title']} ({ar['year']})")
            md.append(f"- **Collector/PI**: {', '.join(ar.get('authors', []))}")
            md.append(f"- **Archive**: {ar.get('publisher', '')}")
            if "url" in ar:
                md.append(f"- **Archive Repository URI**: [{ar['url']}]({ar['url']})")
            md.append(f"- **Scope**: {ar.get('description', '')}\n")

        md.append("## 4. Online Dictionaries & Portals\n")
        for w in web:
            md.append(f"### 🌐 {w['title']}")
            md.append(f"- **Institution**: {w.get('publisher', '')}")
            if "url" in w:
                md.append(f"- **Portal**: [{w['url']}]({w['url']})")
            md.append(f"- **Description**: {w.get('description', '')}\n")

        return "\n".join(md)

    @classmethod
    def save_markdown_file(cls, output_path: str) -> str:
        """Saves the markdown bibliography to disk."""
        content = cls.generate_markdown_bibliography()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path

    @classmethod
    def save_bibtex_file(cls, output_path: str) -> str:
        """Saves the entire bibliography to a .bib file on disk."""
        content = cls.export_all_bibtex()
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        return output_path
