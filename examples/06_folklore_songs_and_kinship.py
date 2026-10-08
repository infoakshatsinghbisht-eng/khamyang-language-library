"""
Example 06: Folklore, Traditional Songs, Kinship & Bibliography
================================================================
Demonstrates working with Tai Khamyang oral literature (Fɯn),
multi-generational kinship resolution, clan lineages, and
scholarly bibliography retrieval.
"""

from khamyang import (
    SongEngine,
    KinshipEngine,
    BibliographyManager,
    KhamyangCorpus,
    get_corpus,
)


def main():
    print("=== Tai Khamyang Folklore, Songs & Kinship Demo ===\n")

    # 1. Traditional Songs & Oral Literature (Fɯn)
    print("--- 1. Traditional Songs (Fɯn) ---")
    songs = SongEngine.all_songs()
    print(f"Total authentic documented songs: {len(songs)}")
    for s in songs:
        print(f"  • [{s['id']}] {s['title_khamyang']} ({s['title_english']}) - Genre: {s['genre']}")

    # Inspect Wedding Ballad
    wedding_song = SongEngine.get_song("song_001")
    print(f"\nExcerpt from '{wedding_song['title_khamyang']}' (Stanza 1):")
    st1 = wedding_song["stanzas"][0]
    for line in st1["lines"][:2]:
        print(f"  Roman:    {line['roman']}")
        print(f"  Lik Tai:  {line['lik_tai']}")
        print(f"  English:  {line['translation_en']}\n")

    # 2. Kinship System & Relative Resolution
    print("--- 2. Kinship & Family System ---")
    test_relations = [
        ("Fa", "Father"),
        ("Mo", "Mother"),
        ("FaFa", "Paternal Grandfather"),
        ("MoFa", "Maternal Grandfather"),
        ("FaElBr", "Father's Elder Brother (Senior Uncle)"),
        ("FaYoBr", "Father's Younger Brother (Junior Uncle)"),
        ("ElBr", "Elder Brother"),
        ("YoSi", "Younger Sister"),
        ("DaHu", "Son-in-Law"),
        ("SoWi", "Daughter-in-Law"),
    ]

    for code, desc in test_relations:
        term = KinshipEngine.resolve(code)
        if term:
            print(f"  {code:<8} ({desc:<42}) -> {term['khamyang_roman']:<12} | Lik Tai: {term['lik_tai']:<10} | Tone {term['tone']}")

    # 3. Traditional Clans
    print("\n--- 3. Ancestral Clans of Powaimukh ---")
    for clan in KinshipEngine.list_clans():
        print(f"  • {clan['name_tai']} ({clan['lik_tai']}): {clan['meaning']} - {clan['role'][:60]}...")

    # 4. Folklore & Annotated Chants
    print("\n--- 4. Annotated Oral Folklore & Chants ---")
    corpus = get_corpus()
    for text in corpus.get_all():
        print(f"  • [{text.id}] {text.title_english} ({text.title_khamyang}) - {len(text.sentences)} glossed units")

    # 5. Scholarly Bibliography & Archival Downloads
    print("\n--- 5. Scholarly Bibliography & Resource Links ---")
    entries = BibliographyManager.all_entries()
    print(f"Total curated bibliographic entries: {len(entries)}")
    for e in entries[:4]:
        apa = BibliographyManager.format_apa(e)
        print(f"  [{e['entry_type'].upper()}] {apa}")

    print("\nBibTeX sample for Morey (2005):")
    morey = BibliographyManager.get_entry("morey2005grammar")
    print(BibliographyManager.to_bibtex_entry(morey))


if __name__ == "__main__":
    main()
