"""
Tai Khamyang Interactive Web Revitalization Platform
=====================================================
FastAPI & Web server providing:
- Multi-script dictionary search & filter
- Interactive 6-Tone Audio Synthesizer (Web Audio API)
- Bidirectional script transliterator with virtual Lik Tai keyboard
- Fieldwork elicitation & phrasebook
- Classifier agreement & Naming system tools
- Interlinear glossed folk texts
- Data export endpoints (CSV, Anki, JSON)
"""

import os
import json
from typing import Optional, List
from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

import khamyang
from khamyang.lexicon.dictionary import get_dictionary
from khamyang.phrases.phrasebook import get_phrasebook
from khamyang.corpus.texts import get_corpus
from khamyang.phonology.tones import TONES, ToneSystem
from khamyang.phonology.synth import get_all_tone_audio_profiles
from khamyang.grammar.classifiers import ClassifierEngine
from khamyang.grammar.naming import list_birth_names, generate_full_name, KHAMYANG_CLANS
from khamyang.grammar.numerals import num_to_khamyang
from khamyang.export.exporter import export_to_csv, export_to_anki_tsv

WEB_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(WEB_DIR, "static")
TEMPLATES_DIR = os.path.join(WEB_DIR, "templates")

app = FastAPI(
    title="Tai Khamyang Language Platform",
    description="Computational language toolkit and revitalization platform for Tai Khamyang (ksu)",
    version=khamyang.__version__,
)

if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
async def index_page():
    index_file = os.path.join(TEMPLATES_DIR, "index.html")
    if os.path.exists(index_file):
        with open(index_file, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse("<h1>Tai Khamyang Platform</h1><p>Template loading...</p>")


@app.get("/api/words")
async def api_get_words(
    q: Optional[str] = Query(None, description="Search query"),
    category: Optional[str] = Query(None, description="Category filter"),
    tone: Optional[int] = Query(None, description="Tone filter (1-6)"),
    limit: int = Query(50, description="Results limit"),
):
    d = get_dictionary()
    if q:
        results = d.search(q, category=category, tone=tone, limit=limit)
    else:
        results = d.get_all_words()
        if category:
            results = [w for w in results if w.category.lower() == category.lower()]
        if tone:
            results = [w for w in results if w.tone == tone]
        results = results[:limit]

    return [w.to_dict() for w in results]


@app.get("/api/categories")
async def api_get_categories():
    d = get_dictionary()
    return d.list_categories()


@app.get("/api/tones")
async def api_get_tones():
    profiles = get_all_tone_audio_profiles()
    for prof in profiles:
        t_num = prof["tone_number"]
        t_obj = TONES[t_num]
        prof["gedney_origin"] = ", ".join(t_obj.gedney_cells)
        prof["description"] = t_obj.description
    return profiles


@app.get("/api/transliterate")
async def api_transliterate(
    text: str = Query(..., description="Input text"),
    source: str = Query("roman", description="Source script (roman, liktai, assamese)"),
    target: str = Query("liktai", description="Target script (liktai, assamese, roman, ipa)"),
):
    try:
        converted = khamyang.transliterate(text, source_script=source, target_script=target)
        return {"input": text, "source": source, "target": target, "result": converted}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/phrases")
async def api_get_phrases(category: Optional[str] = None):
    pb = get_phrasebook()
    if category:
        phrases = pb.get_by_category(category)
    else:
        phrases = pb.get_all()
    return [p.to_dict() for p in phrases]


@app.get("/api/phrase_categories")
async def api_get_phrase_categories():
    pb = get_phrasebook()
    return pb.list_categories()


@app.get("/api/quantify")
async def api_quantify(noun: str = Query(...), count: int = Query(1)):
    res = ClassifierEngine.quantify(noun, count)
    clf = ClassifierEngine.get_classifier(noun)
    return {
        "noun": noun,
        "count": count,
        "phrase_roman": res,
        "lik_tai": khamyang.transliterate(res, "roman", "liktai"),
        "assamese": khamyang.transliterate(res, "roman", "assamese"),
        "classifier": clf.roman if clf else "an1",
        "classifier_meaning": clf.meaning if clf else "general",
    }


@app.get("/api/naming")
async def api_naming(
    order: int = Query(1, ge=1, le=8),
    gender: str = Query("m"),
    personal: str = Query(""),
    clan: str = Query("Thomung"),
):
    return generate_full_name(order, gender, personal_name=personal, clan=clan)


@app.get("/api/clans")
async def api_clans():
    return KHAMYANG_CLANS


@app.get("/api/numeral")
async def api_numeral(num: int = Query(..., ge=0, le=1000000)):
    return {
        "number": num,
        "roman": num_to_khamyang(num, "roman"),
        "lik_tai": num_to_khamyang(num, "liktai"),
        "assamese": num_to_khamyang(num, "assamese"),
    }


@app.get("/api/texts")
async def api_get_texts():
    corpus = get_corpus()
    return [t.to_dict() for t in corpus.get_all()]


@app.get("/api/export/csv")
async def api_export_csv():
    temp_p = os.path.join(STATIC_DIR, "khamyang_lexicon.csv")
    export_to_csv(temp_p)
    return FileResponse(temp_p, filename="khamyang_lexicon.csv", media_type="text/csv")


@app.get("/api/export/anki")
async def api_export_anki():
    temp_p = os.path.join(STATIC_DIR, "khamyang_anki_deck.tsv")
    export_to_anki_tsv(temp_p)
    return FileResponse(temp_p, filename="khamyang_anki_deck.tsv", media_type="text/tab-separated-values")


def run_server(host: str = "127.0.0.1", port: int = 8000):
    """Runs the FastAPI server with uvicorn."""
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
