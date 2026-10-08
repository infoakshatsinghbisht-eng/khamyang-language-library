"""
Tai Khamyang Command-Line Interface
===================================
Interactive CLI for developers, linguists, and researchers.
"""

import sys
import os
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

console = Console()


@click.group()
@click.version_option(version=khamyang.__version__, prog_name="khamyang")
def cli():
    """Tai Khamyang (ksu) Language Revitalization & Linguistic Toolkit."""
    pass


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


if __name__ == "__main__":
    cli()
