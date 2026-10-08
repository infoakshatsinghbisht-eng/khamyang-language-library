"""Tests for Tai Khamyang traditional songs engine."""

import unittest
from khamyang.corpus.songs import SongEngine


class TestSongEngine(unittest.TestCase):

    def test_all_songs_loaded(self):
        songs = SongEngine.all_songs()
        self.assertGreaterEqual(len(songs), 6)
        ids = [s["id"] for s in songs]
        self.assertIn("song_001", ids)
        self.assertIn("song_002", ids)
        self.assertIn("song_004", ids)

    def test_get_song_by_id(self):
        wedding = SongEngine.get_song("song_001")
        self.assertIsNotNone(wedding)
        self.assertEqual(wedding["genre"], "wedding_ceremonial")
        self.assertIn("Ao Nang", wedding["title_khamyang"])
        self.assertGreaterEqual(len(wedding["stanzas"]), 2)

    def test_search_songs(self):
        results = SongEngine.search("Sangken")
        self.assertGreaterEqual(len(results), 1)
        self.assertEqual(results[0]["id"], "song_004")

    def test_filter_by_genre(self):
        lullabies = SongEngine.filter_by_genre("lullaby")
        self.assertGreaterEqual(len(lullabies), 1)
        self.assertEqual(lullabies[0]["id"], "song_002")

    def test_format_song_text(self):
        song = SongEngine.get_song("song_002")
        formatted = SongEngine.format_song_text(song)
        self.assertIn("Fɯn Nɔn Luk", formatted)
        self.assertIn("Stanza 1", formatted)
        self.assertIn("English:", formatted)


if __name__ == "__main__":
    unittest.main()
