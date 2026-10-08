"""
Tai Khamyang Traditional Songs and Ballads Engine
Provides querying, bilingual stanza rendering, and cultural documentation
for authentic Tai Khamyang oral poetry, wedding ballads, lullabies, and work songs.
"""

import json
import os
from typing import Dict, List, Optional, Any


class SongEngine:
    """
    Manages and renders Tai Khamyang traditional songs (Fɯn).
    """

    _data_cache: Optional[List[Dict[str, Any]]] = None

    @classmethod
    def _load_data(cls) -> List[Dict[str, Any]]:
        if cls._data_cache is None:
            path = os.path.join(os.path.dirname(__file__), "..", "data", "songs.json")
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as f:
                    cls._data_cache = json.load(f)
            else:
                cls._data_cache = []
        return cls._data_cache

    @classmethod
    def all_songs(cls) -> List[Dict[str, Any]]:
        """Returns all traditional songs."""
        return cls._load_data()

    @classmethod
    def get_song(cls, song_id: str) -> Optional[Dict[str, Any]]:
        """Retrieves a song by its unique ID (e.g. 'song_001', 'wedding')."""
        sid = song_id.strip().lower()
        for s in cls._load_data():
            if s["id"].lower() == sid or sid in s.get("title_khamyang", "").lower():
                return s
        return None

    @classmethod
    def filter_by_genre(cls, genre: str) -> List[Dict[str, Any]]:
        """Filters songs by genre (e.g. 'wedding_ceremonial', 'lullaby', 'work_song', 'festival_celebration')."""
        g = genre.strip().lower()
        return [s for s in cls._load_data() if g in s.get("genre", "").lower()]

    @classmethod
    def search(cls, query: str) -> List[Dict[str, Any]]:
        """Searches across titles, descriptions, informants, and lyrics."""
        q = query.strip().lower()
        results = []
        for s in cls._load_data():
            # Check title, description, genre
            if (
                q in s.get("title_khamyang", "").lower()
                or q in s.get("title_english", "").lower()
                or q in s.get("title_assamese", "").lower()
                or q in s.get("genre", "").lower()
                or q in s.get("description", "").lower()
            ):
                results.append(s)
                continue

            # Check inside lyrics
            found_in_lyrics = False
            for stanza in s.get("stanzas", []):
                for line in stanza.get("lines", []):
                    if (
                        q in line.get("roman", "").lower()
                        or q in line.get("translation_en", "").lower()
                        or q in line.get("translation_as", "").lower()
                        or q in line.get("lik_tai", "")
                    ):
                        found_in_lyrics = True
                        break
                if found_in_lyrics:
                    break
            if found_in_lyrics:
                results.append(s)

        return results

    @classmethod
    def format_song_text(cls, song: Dict[str, Any], show_liktai: bool = True, show_assamese: bool = True) -> str:
        """Formats a song into a readable multi-line presentation string."""
        lines = []
        lines.append(f"============================================================")
        lines.append(f"🎵 {song.get('title_khamyang')} ({song.get('title_english')})")
        lines.append(f"Lik Tai:   {song.get('title_liktai')}")
        lines.append(f"Assamese:  {song.get('title_assamese')}")
        lines.append(f"Genre:     {song.get('genre')} | Village: {song.get('village')}")
        lines.append(f"Informant: {song.get('informant')} | Ref: {song.get('archive_ref')}")
        lines.append(f"------------------------------------------------------------")
        lines.append(f"Description: {song.get('description')}")
        lines.append(f"Cultural Context: {song.get('cultural_context')}")
        lines.append(f"============================================================")

        for stanza in song.get("stanzas", []):
            lines.append(f"\n[Stanza {stanza.get('stanza_number', 1)}]")
            for line in stanza.get("lines", []):
                lines.append(f"  Khamyang:  {line.get('roman')}")
                if show_liktai:
                    lines.append(f"  Lik Tai:   {line.get('lik_tai')}")
                if show_assamese:
                    lines.append(f"  Assamese:  {line.get('assamese_script')} ({line.get('translation_as')})")
                lines.append(f"  English:   {line.get('translation_en')}")
                lines.append(f"  Gloss:     {line.get('gloss')}\n")

        return "\n".join(lines)
