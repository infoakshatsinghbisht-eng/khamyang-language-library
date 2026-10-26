"""
Tai Khamyang Command-Line Interface
===================================
Interactive CLI for developers, linguists, and researchers.
"""

import sys
import os
from typing import Optional, List, Dict, Any
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

import khamyang
from khamyang.phonology.tones import ToneSystem, TONES
from khamyang.grammar.naming import list_birth_names, generate_full_name, KHAMYANG_CLANS
from khamyang.grammar.classifiers import ClassifierEngine
from khamyang.corpus.igt import InterlinearGloss

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console(highlight=False)



@click.group(
    epilog="Authored, Architected & Preserved by Akshat Singh Bisht (https://akshatsinghbisht.com/)."
)
@click.version_option(
    version=f"{khamyang.__version__} (Authored & Preserved by Akshat Singh Bisht | https://akshatsinghbisht.com/)",
    prog_name="khamyang"
)
def cli():
    """
    Tai Khamyang (ksu) Language Revitalization & Computational Toolkit.
    
    Authored, Architected & Preserved by Akshat Singh Bisht.
    Official Website: https://akshatsinghbisht.com/
    """
    pass


@cli.command("credits")
def credits_cmd():
    """Display official author credits, preservation struggles, and mandatory attribution requirements."""
    info = khamyang.AUTHOR_CREDITS
    
    panel_text = Text()
    panel_text.append("TAI KHAMYANG (ksu) COMPUTATIONAL LANGUAGE LIBRARY\n\n", style="bold cyan")
    panel_text.append("Lead Architect & Author : ", style="bold white")
    panel_text.append(f"{info['author']}\n", style="bold yellow")
    panel_text.append("Official Website         : ", style="bold white")
    panel_text.append(f"{info['website']}\n", style="bold green underline")
    panel_text.append("Direct Contact           : ", style="bold white")
    panel_text.append(f"{info['email']}\n", style="cyan")
    panel_text.append("Amazon Author Central    : ", style="bold white")
    panel_text.append(f"{info['amazon_author']}\n", style="blue underline")
    panel_text.append("LinkedIn Profile         : ", style="bold white")
    panel_text.append(f"{info['linkedin']}\n", style="blue underline")
    panel_text.append("ResearchGate             : ", style="bold white")
    panel_text.append(f"{info['researchgate']}\n", style="blue underline")
    panel_text.append("GitHub Repository        : ", style="bold white")
    panel_text.append(f"{info['github']}\n", style="magenta underline")
    panel_text.append("Copyright Notice         : ", style="bold white")
    panel_text.append(f"{info['copyright']}\n\n", style="bold red")
    
    panel_text.append("THE PRESERVATION MISSION & STRUGGLE:\n", style="bold yellow")
    panel_text.append(
        "Tai Khamyang is on the verge of silence with fewer than 50 fluent native elder speakers surviving\n"
        "in Powaimukh village, Assam. This computational library was built through immense personal struggles,\n"
        "retrieving rare 19th-century manuscripts, transcribing traditional songs, decoding the 6-tone phonology,\n"
        "and engineering software platforms from scratch to ensure this ancestral voice survives.\n\n",
        style="white"
    )
    
    panel_text.append("MANDATORY ATTRIBUTION REQUIREMENT:\n", style="bold yellow")
    panel_text.append(
        "Any software, mobile app, NLP model, research publication, or system utilizing this library or its\n"
        "datasets MUST explicitly credit and cite Akshat Singh Bisht as the primary author and creator.\n",
        style="bold green"
    )
    
    console.print(Panel(panel_text, title="[bold gold1]Author & Copyright Credits[/bold gold1]", border_style="cyan"))



@cli.command("lookup")
@click.argument("term")
def lookup_cmd(term: str):
    """Search for a word in Tai Khamyang (by Roman, Lik Tai, Assamese, or English)."""
    d = khamyang.get_dictionary()
    results = d.lookup(term)

    if not results:
        console.print(f"[bold red]No entries found for:[/bold red] '{term}'")
        return

    for w in results[:5]:
        tone_obj = TONES.get(w.tone)
        tone_str = f"Tone {w.tone} ({tone_obj.name if tone_obj else ''}) [chao: {tone_obj.pitch_chao if tone_obj else ''}]"

        panel_content = Text()
        panel_content.append(f"Lik Tai:     ", style="bold cyan")
        panel_content.append(f"{w.lik_tai}\n", style="bold yellow")
        panel_content.append(f"Romanized:   ", style="bold cyan")
        panel_content.append(f"{w.roman}\n", style="bold green")
        panel_content.append(f"Assamese:    ", style="bold cyan")
        panel_content.append(f"{w.assamese}\n", style="bold magenta")
        panel_content.append(f"IPA:         ", style="bold cyan")
        panel_content.append(f"{w.ipa}\n", style="italic")
        panel_content.append(f"Part of Speech: ", style="bold cyan")
        panel_content.append(f"{w.pos}\n")
        panel_content.append(f"Tone:        ", style="bold cyan")
        panel_content.append(f"{tone_str}\n", style="bold blue")
        panel_content.append(f"English:     ", style="bold cyan")
        panel_content.append(f"{w.gloss_en}\n", style="bold white")
        panel_content.append(f"Assamese:    ", style="bold cyan")
        panel_content.append(f"{w.gloss_as}\n", style="bold white")
        panel_content.append(f"Category:    ", style="bold cyan")
        panel_content.append(f"{w.category}\n")

        if w.cognates:
            cogs = ", ".join(f"{k}: {v}" for k, v in w.cognates.items())
            panel_content.append(f"Cognates:    ", style="bold cyan")
            panel_content.append(f"{cogs}\n", style="dim")

        console.print(Panel(panel_content, title=f"[bold]Tai Khamyang: {w.roman}[/bold]", border_style="cyan"))


@cli.command("search")
@click.argument("query")
@click.option("--category", "-c", default=None, help="Filter by category (e.g. nature, body, food, kinship)")
@click.option("--tone", "-t", default=None, type=int, help="Filter by tone (1 to 6)")
@click.option("--limit", "-n", default=20, help="Max number of results")
def search_cmd(query: str, category: str, tone: int, limit: int):
    """Full-text search across dictionary meanings and transcriptions."""
    d = khamyang.get_dictionary()
    results = d.search(query, category=category, tone=tone, limit=limit)

    if not results:
        console.print(f"[yellow]No matches found for query:[/yellow] '{query}'")
        return

    table = Table(title=f"Khamyang Search Results: '{query}' ({len(results)} found)")
    table.add_column("Lik Tai", style="yellow")
    table.add_column("Roman", style="bold green")
    table.add_column("Assamese", style="magenta")
    table.add_column("Tone", style="cyan")
    table.add_column("IPA", style="dim")
    table.add_column("POS", style="italic")
    table.add_column("English", style="bold white")
    table.add_column("Assamese Gloss", style="white")

    for w in results:
        table.add_row(
            w.lik_tai,
            w.roman,
            w.assamese,
            str(w.tone),
            w.ipa,
            w.pos,
            w.gloss_en,
            w.gloss_as,
        )

    console.print(table)


@cli.command("transliterate")
@click.argument("text")
@click.option("--to", "target", default="liktai", type=click.Choice(["liktai", "assamese", "roman", "ipa"], case_sensitive=False))
@click.option("--from", "source", default="roman", type=click.Choice(["roman", "liktai", "assamese"], case_sensitive=False))
def transliterate_cmd(text: str, target: str, source: str):
    """Convert text between Romanization, Lik Tai, Assamese, and IPA."""
    out = khamyang.transliterate(text, source_script=source, target_script=target)
    console.print(f"[bold cyan]Input ({source}):[/bold cyan]  {text}")
    console.print(f"[bold yellow]Output ({target}):[/bold yellow] {out}")


@cli.command("tone")
@click.argument("tone_or_syllable")
def tone_cmd(tone_or_syllable: str):
    """Explain one of the 6 tones or analyze a syllable's pitch."""
    if tone_or_syllable.isdigit():
        t_num = int(tone_or_syllable)
    else:
        t_num = ToneSystem.extract_tone(tone_or_syllable) or 1

    t_info = ToneSystem.explain_tone(t_num)
    p = Text()
    p.append(f"Tone Number:     ", style="bold")
    p.append(f"{t_info['number']}\n", style="bold yellow")
    p.append(f"Linguistic Name: ", style="bold")
    p.append(f"{t_info['name']}\n", style="bold green")
    p.append(f"Chao Contour:    ", style="bold")
    p.append(f"{t_info['pitch_contour']}\n", style="bold cyan")
    p.append(f"IPA Symbol:      ", style="bold")
    p.append(f"{t_info['ipa']}\n", style="bold magenta")
    p.append(f"Creaky Voice:    ", style="bold")
    p.append(f"{t_info['creaky_voice']}\n")
    p.append(f"Glottal Stop:    ", style="bold")
    p.append(f"{t_info['glottal_stop']}\n")
    p.append(f"Gedney Box:      ", style="bold")
    p.append(f"{t_info['gedney_origin']}\n", style="dim")
    p.append(f"Description:     ", style="bold")
    p.append(f"{t_info['description']}\n")

    console.print(Panel(p, title=f"Tone {t_num} Analysis", border_style="blue"))


@cli.command("phrase")
@click.option("--category", "-c", default=None, help="Category (fieldwork, greeting, daily, food, identity, culture)")
@click.option("--search", "-s", default=None, help="Search text in phrases")
def phrase_cmd(category: str, search: str):
    """Browse the conversational phrasebook and fieldwork elicitation sentences."""
    pb = khamyang.get_phrasebook()
    if search:
        phrases = pb.search(search)
    elif category:
        phrases = pb.get_by_category(category)
    else:
        phrases = pb.get_all()

    table = Table(title=f"Khamyang Phrasebook ({len(phrases)} phrases)")
    table.add_column("Lik Tai", style="yellow")
    table.add_column("Roman", style="bold green")
    table.add_column("Assamese", style="magenta")
    table.add_column("English Meaning", style="bold white")
    table.add_column("Assamese Meaning", style="cyan")

    for p in phrases[:25]:
        table.add_row(
            p.lik_tai,
            p.roman,
            p.assamese,
            p.english,
            p.assamese_trans,
        )

    console.print(table)


@cli.command("num")
@click.argument("number", type=int)
@click.option("--script", default="roman", type=click.Choice(["roman", "liktai", "assamese"]))
def num_cmd(number: int, script: str):
    """Convert an integer (0 to 1,000,000) into Tai Khamyang words."""
    result = khamyang.num_to_khamyang(number, script=script)
    console.print(f"[bold cyan]Number {number}:[/bold cyan] [bold yellow]{result}[/bold yellow]")


@cli.command("name")
@click.option("--gender", "-g", default="m", type=click.Choice(["m", "f", "male", "female"]))
@click.option("--order", "-o", default=1, type=int, help="Birth order (1 to 8)")
@click.option("--personal", "-p", default="", help="Optional personal name")
@click.option("--clan", default="Thomung", help="Clan surname (Thomung, Chowlik, Chaohai, Pangyok, Wailong)")
def name_cmd(gender: str, order: int, personal: str, clan: str):
    """Generate or look up traditional Tai Khamyang birth-order names."""
    full = generate_full_name(order, gender, personal_name=personal, clan=clan)
    p = Text()
    p.append(f"Full Name:        ", style="bold")
    p.append(f"{full['full_roman']}\n", style="bold yellow")
    p.append(f"Birth Order Name: ", style="bold")
    p.append(f"{full['birth_order_name']}\n", style="bold green")
    p.append(f"Clan Surname:     ", style="bold")
    p.append(f"{full['clan']}\n", style="bold cyan")
    p.append(f"Significance:     ", style="bold")
    p.append(f"{full['meaning']}\n", style="white")

    console.print(Panel(p, title=f"Khamyang Birth-Order Name ({gender.upper()} #{order})", border_style="green"))


@cli.command("stats")
def stats_cmd():
    """Display comprehensive linguistic metrics of the Khamyang language library."""
    d = khamyang.get_dictionary()
    st = d.statistics()

    table = Table(title="Tai Khamyang Linguistic Database Metrics")
    table.add_column("Metric", style="bold cyan")
    table.add_column("Value", style="bold yellow")

    table.add_row("Total Lexical Entries", str(st["total_words"]))
    table.add_row("Total Categories", str(st["total_categories"]))
    for t_num, count in st["tones_distribution"].items():
        table.add_row(f"  • Tone {t_num} words", str(count))

    console.print(table)


@cli.command("export")
@click.option("--format", "-f", default="csv", type=click.Choice(["csv", "anki", "html"]))
@click.option("--output", "-o", required=True, help="Output destination file path")
def export_cmd(format: str, output: str):
    """Export dictionary to CSV, Anki flashcard TSV, or interactive HTML."""
    from khamyang.export.exporter import export_to_csv, export_to_anki_tsv, export_to_html
    if format == "csv":
        export_to_csv(output)
    elif format == "anki":
        export_to_anki_tsv(output)
    elif format == "html":
        export_to_html(output)
    console.print(f"[bold green]Successfully exported dictionary ({format}) to:[/bold green] {output}")


@cli.command("web")
@click.option("--port", "-p", default=8000, help="Web server port (default: 8000)")
@click.option("--host", "-h", default="127.0.0.1", help="Host address (default: 127.0.0.1)")
def web_cmd(port: int, host: str):
    """Start the interactive Tai Khamyang web revitalization interface."""
    from khamyang.web.server import run_server
    console.print(f"[bold green]Starting Tai Khamyang Web Platform at[/bold green] [bold cyan]http://{host}:{port}[/bold cyan]")
    run_server(host=host, port=port)


@cli.command("song")
@click.argument("action", default="list", type=click.Choice(["list", "show", "search"]))
@click.argument("query", required=False, default="")
def song_cmd(action: str, query: str):
    """Browse, view lyrics, and search authentic Tai Khamyang traditional songs."""
    from khamyang.corpus.songs import SongEngine

    if action == "list":
        songs = SongEngine.all_songs()
        table = Table(title="Tai Khamyang Traditional Songs & Ballads (Fɯn)")
        table.add_column("ID", style="bold cyan")
        table.add_column("Title (Khamyang)", style="bold yellow")
        table.add_column("English Title", style="bold green")
        table.add_column("Genre", style="magenta")
        table.add_column("Informant / Origin", style="white")

        for s in songs:
            table.add_row(s["id"], s["title_khamyang"], s["title_english"], s["genre"], s["informant"])
        console.print(table)
        console.print("\n[italic dim]Use 'khamyang song show <id>' to read complete lyrics, glosses, and cultural context.[/italic dim]")

    elif action == "show":
        if not query:
            console.print("[bold red]Please specify a song ID, e.g.:[/bold red] 'khamyang song show song_001'")
            return
        s = SongEngine.get_song(query)
        if not s:
            console.print(f"[bold red]Song not found:[/bold red] '{query}'")
            return
        text = SongEngine.format_song_text(s)
        console.print(Panel(text, title=f"🎵 {s['title_khamyang']} ({s['title_english']})", border_style="yellow"))

    elif action == "search":
        if not query:
            console.print("[bold red]Please provide a search term.[/bold red]")
            return
        res = SongEngine.search(query)
        if not res:
            console.print(f"[bold red]No songs found matching:[/bold red] '{query}'")
            return
        for s in res:
            console.print(f"[bold yellow]{s['id']}[/bold yellow] - [bold cyan]{s['title_khamyang']}[/bold cyan] ({s['title_english']}): {s['description']}")


@cli.command("kinship")
@click.argument("action", default="resolve", type=click.Choice(["resolve", "search", "generation", "clans"]))
@click.argument("query", required=False, default="")
def kinship_cmd(action: str, query: str):
    """Solve and inspect Tai Khamyang kinship relations, terms, and clan lineages."""
    from khamyang.grammar.kinship import KinshipEngine

    if action == "resolve":
        if not query:
            console.print("[bold cyan]Common codes:[/bold cyan] Fa (father), Mo (mother), FaFa (paternal grandfather), MoMo (maternal grandmother), FaElBr (elder paternal uncle), YoBr (younger brother), So (son), DaHu (son-in-law)")
            query = "FaElBr"
        res = KinshipEngine.resolve(query)
        if not res:
            console.print(f"[bold red]Could not resolve code:[/bold red] '{query}'")
            return
        explanation = KinshipEngine.explain_relationship(query)
        console.print(Panel(explanation, title=f"👨‍👩‍👧‍👦 Kinship Term: {res['khamyang_roman']}", border_style="cyan"))

    elif action == "search":
        if not query:
            console.print("[bold red]Please provide a search term (e.g. 'uncle', 'grandmother', 'lung1').[/bold red]")
            return
        matches = KinshipEngine.lookup(query)
        if not matches:
            console.print(f"[bold red]No kinship terms matching:[/bold red] '{query}'")
            return
        table = Table(title=f"Kinship Search Results for '{query}'")
        table.add_column("Roman", style="bold cyan")
        table.add_column("Lik Tai", style="yellow")
        table.add_column("Assamese", style="magenta")
        table.add_column("English", style="green")
        table.add_column("Generation", style="blue")
        for m in matches:
            table.add_row(m["khamyang_roman"], m["lik_tai"], m["assamese_script"], m["english"], str(m["generation"]))
        console.print(table)

    elif action == "generation":
        gen = int(query) if query.lstrip("-").isdigit() else 1
        terms = KinshipEngine.list_by_generation(gen)
        table = Table(title=f"Generation {gen} Relatives ({'Ancestors' if gen > 0 else 'Descendants' if gen < 0 else 'Ego Generation'})")
        table.add_column("Roman", style="bold cyan")
        table.add_column("Lik Tai", style="yellow")
        table.add_column("English", style="green")
        table.add_column("Assamese", style="magenta")
        table.add_column("Relation Codes", style="dim")
        for t in terms:
            table.add_row(t["khamyang_roman"], t["lik_tai"], t["english"], t["assamese"], ", ".join(t.get("relation_codes", [])))
        console.print(table)

    elif action == "clans":
        clans = KinshipEngine.list_clans()
        table = Table(title="Tai Khamyang Historical Clans (Khɯa1)")
        table.add_column("Clan Name", style="bold yellow")
        table.add_column("Lik Tai", style="bold cyan")
        table.add_column("Meaning", style="bold green")
        table.add_column("Traditional Hereditary Role", style="white")
        for c in clans:
            table.add_row(c["name_tai"], c["lik_tai"], c["meaning"], c["role"])
        console.print(table)


@cli.command("biblio")
@click.argument("action", default="list", type=click.Choice(["list", "search", "bibtex", "markdown"]))
@click.argument("query", required=False, default="")
@click.option("--output", "-o", default="", help="Optional output file destination")
def biblio_cmd(action: str, query: str, output: str):
    """Browse scholarly literature, books, articles, and export BibTeX citations."""
    from khamyang.scraper.downloader import BibliographyManager

    if action == "list":
        entries = BibliographyManager.all_entries()
        table = Table(title="Tai Khamyang Scholarly Bibliography & Resource Archive")
        table.add_column("ID", style="bold cyan")
        table.add_column("Year", style="bold yellow")
        table.add_column("Type", style="magenta")
        table.add_column("Author(s)", style="green")
        table.add_column("Title", style="white")

        for e in entries:
            authors = ", ".join(e.get("authors", []))
            table.add_row(e["id"], str(e.get("year", "")), e.get("entry_type", ""), authors[:28], e["title"][:48])
        console.print(table)

    elif action == "search":
        if not query:
            console.print("[bold red]Please enter search term (e.g. 'Morey', 'songs', 'tones', 'Nath').[/bold red]")
            return
        matches = BibliographyManager.search(query)
        if not matches:
            console.print(f"[bold red]No entries found matching:[/bold red] '{query}'")
            return
        for m in matches:
            apa = BibliographyManager.format_apa(m)
            console.print(f"• [bold cyan]{m['id']}[/bold cyan] ({m['entry_type']}):\n  {apa}\n  [dim]{m.get('description', '')}[/dim]\n")

    elif action == "bibtex":
        content = BibliographyManager.export_all_bibtex()
        if output:
            with open(output, "w", encoding="utf-8") as f:
                f.write(content)
            console.print(f"[bold green]BibTeX citations successfully saved to:[/bold green] {output}")
        else:
            console.print(content)

    elif action == "markdown":
        out = output or "BIBLIOGRAPHY.md"
        BibliographyManager.save_markdown_file(out)
        console.print(f"[bold green]Markdown bibliography saved to:[/bold green] {out}")


@cli.command("books")
@click.option("--genre", default=None, help="Filter books by genre (e.g. 'novel', 'jataka', 'fable', 'chronicle', 'folktale').")
@click.option("--limit", default=25, help="Number of books to display (default 25).")
def books_cmd(genre: Optional[str], limit: int):
    """List all digitalized Tai Khamyang books and interlinear texts (2,000+ available)."""
    from khamyang.corpus.texts import get_corpus
    corpus = get_corpus()
    books = corpus.list_books()

    if genre:
        g = genre.strip().lower()
        books = [b for b in books if g in b["genre"].lower()]

    table = Table(title=f"[Books] Tai Khamyang Digital Library & Archive ({len(books)} books found)", style="bold cyan")
    table.add_column("ID", style="bold yellow")
    table.add_column("Title (English)", style="bold white")
    table.add_column("Tai Title", style="cyan")
    table.add_column("Genre", style="green")
    table.add_column("Sentences", justify="right", style="magenta")

    for b in books[:limit]:
        table.add_row(
            b["id"],
            b["title_english"][:40],
            b["title_khamyang"][:30],
            b["genre"],
            str(b["sentence_count"])
        )
    console.print(table)
    if len(books) > limit:
        console.print(f"\n[dim]Showing {limit} of {len(books)} books. Use --limit {len(books)} or --genre <type> to filter.[/dim]")
    console.print(f"[dim]Read any book with:[/dim] [bold green]khamyang read <book_id>[/bold green]")



@cli.command("read")
@click.argument("book_id")
@click.option("--limit", default=10, help="Number of sentences to display.")
def read_cmd(book_id: str, limit: int):
    """Read a digitalized book with interlinear glosses."""
    from khamyang.corpus.texts import get_corpus
    corpus = get_corpus()
    book = corpus.get_book(book_id)
    if not book:
        console.print(f"[bold red]Book '{book_id}' not found.[/bold red] Use 'khamyang books' to see available books.")
        return

    console.print(Panel(
        f"[bold yellow]{book.title_english}[/bold yellow]\n"
        f"[cyan]{book.title_khamyang}[/cyan]\n\n"
        f"[dim]{book.description}[/dim]\n\n"
        f"[bold]Informant:[/bold] {book.informant} | [bold]Location:[/bold] {book.village} | [bold]Total Sentences:[/bold] {len(book.sentences)}",
        title=f"[Book] {book.id}",
        border_style="cyan"
    ))


    for idx, s in enumerate(book.sentences[:limit], 1):
        console.print(f"\n[bold green]Sentence {idx}[/bold green] [dim]({s.id})[/dim]:")
        console.print(f"  [bold yellow]Lik Tai:[/bold yellow]   {s.lik_tai}")
        console.print(f"  [bold cyan]Roman:[/bold cyan]     {s.text_roman}")
        console.print(f"  [bold magenta]Assamese:[/bold magenta]  {s.assamese_script}")
        if s.morphemes and s.glosses:
            console.print(f"  [dim]Gloss:[/dim]     {' | '.join(s.glosses)}")
        console.print(f"  [bold white]English:[/bold white]   \"{s.free_translation_en}\"")
        if s.notes:
            console.print(f"  [italic dim]Note:[/italic dim]      {s.notes}")

    if len(book.sentences) > limit:
        console.print(f"\n[dim]Showing {limit} of {len(book.sentences)} sentences. Use --limit {len(book.sentences)} to view all.[/dim]")


if __name__ == "__main__":
    cli()

