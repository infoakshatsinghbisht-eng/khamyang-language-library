/**
 * Tai Khamyang Platform - Client Application
 * Features:
 * - Web Audio API pitch synthesizer for 6 Khamyang tones
 * - Real-time dictionary search, filtering, and audio play
 * - Virtual Lik Tai keyboard and transliterator
 * - Dynamic grammar tools (Classifiers, Naming, Numerals)
 * - Interlinear glossed texts
 */

let audioCtx = null;
let toneProfiles = [];

function getAudioContext() {
  if (!audioCtx) {
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    audioCtx = new AudioContext();
  }
  if (audioCtx.state === 'suspended') {
    audioCtx.resume();
  }
  return audioCtx;
}

// -------------------------------------------------------------
// WEB AUDIO SYNTHESIZER: 6 TONES OF KHAMYANG
// -------------------------------------------------------------
function playTonePitch(toneNum, baseHz = 165.0) {
  const ctx = getAudioContext();
  const profile = toneProfiles.find(p => p.tone_number === toneNum);
  if (!profile) return;

  const now = ctx.currentTime;
  const duration = profile.duration_sec || 0.55;

  const osc = ctx.createOscillator();
  const gain = ctx.createGain();

  // Voicing filter
  const filter = ctx.createBiquadFilter();
  filter.type = "lowpass";
  filter.frequency.setValueAtTime(1200, now);

  osc.type = "sawtooth"; // Gives natural vocal harmonic texture
  osc.connect(filter);
  filter.connect(gain);
  gain.connect(ctx.destination);

  // Apply pitch trajectory
  const points = profile.points;
  if (points && points.length > 0) {
    osc.frequency.setValueAtTime(points[0].freq, now);
    for (let i = 1; i < points.length; i++) {
      osc.frequency.linearRampToValueAtTime(points[i].freq, now + points[i].time);
    }
  } else {
    osc.frequency.setValueAtTime(baseHz, now);
  }

  // Amplitude Envelope
  gain.gain.setValueAtTime(0.001, now);
  gain.gain.exponentialRampToValueAtTime(0.2, now + 0.04);

  if (profile.glottal_stop) {
    // Sharp abrupt cutoff for Tone 4 (54ʔ)
    gain.gain.setValueAtTime(0.2, now + duration - 0.08);
    gain.gain.linearRampToValueAtTime(0.0001, now + duration - 0.01);
  } else if (profile.creaky_voice) {
    // Tone 3 (21̰) low and creaky fading
    gain.gain.setValueAtTime(0.18, now + duration * 0.5);
    gain.gain.exponentialRampToValueAtTime(0.001, now + duration);
  } else {
    // Smooth natural decay
    gain.gain.setValueAtTime(0.18, now + duration * 0.6);
    gain.gain.exponentialRampToValueAtTime(0.001, now + duration);
  }

  osc.start(now);
  osc.stop(now + duration + 0.05);
}

// -------------------------------------------------------------
// TAB NAVIGATION
// -------------------------------------------------------------
function initTabs() {
  const tabs = document.querySelectorAll('.nav-tab');
  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      tabs.forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));

      tab.classList.add('active');
      const targetId = tab.getAttribute('data-tab');
      const pane = document.getElementById(targetId);
      if (pane) pane.classList.add('active');
    });
  });
}

// -------------------------------------------------------------
// DICTIONARY MODULE
// -------------------------------------------------------------
async function loadCategories() {
  try {
    const res = await fetch('/api/categories');
    const categories = await res.json();
    const select = document.getElementById('categoryFilter');
    categories.forEach(cat => {
      const opt = document.createElement('option');
      opt.value = cat;
      opt.textContent = cat.charAt(0).toUpperCase() + cat.slice(1);
      select.appendChild(opt);
    });
  } catch (err) {
    console.error('Failed to load categories', err);
  }
}

async function searchDictionary() {
  const q = document.getElementById('dictSearchInput').value.trim();
  const cat = document.getElementById('categoryFilter').value;
  const tone = document.getElementById('toneFilter').value;
  const container = document.getElementById('wordsContainer');
  const loader = document.getElementById('dictLoading');

  loader.style.display = 'flex';
  container.innerHTML = '';

  const params = new URLSearchParams();
  if (q) params.set('q', q);
  if (cat) params.set('category', cat);
  if (tone) params.set('tone', tone);
  params.set('limit', '60');

  try {
    const res = await fetch(`/api/words?${params.toString()}`);
    const words = await res.json();
    loader.style.display = 'none';

    if (words.length === 0) {
      container.innerHTML = `<div style="grid-column: 1/-1; text-align: center; color: var(--text-muted); padding: 3rem;">
        No Tai Khamyang words found matching your query.
      </div>`;
      return;
    }

    words.forEach(w => {
      const card = document.createElement('div');
      card.className = 'word-card';
      card.innerHTML = `
        <div class="card-top">
          <div class="card-scripts">
            <span class="script-liktai">${w.lik_tai || '—'}</span>
            <span class="script-roman">${w.roman}</span>
            <span class="script-assamese">${w.assamese || ''}</span>
            <span class="script-ipa">${w.ipa || ''}</span>
          </div>
          <span class="tone-badge t${w.tone}">Tone ${w.tone}</span>
        </div>
        <div class="card-meanings">
          <div class="meaning-en">${w.gloss_en}</div>
          <div class="meaning-as">${w.gloss_as || ''}</div>
        </div>
        <div class="card-bottom">
          <span class="card-pos">${w.pos} • ${w.category}</span>
          <button class="btn-play-tone" onclick="playTonePitch(${w.tone})">🔊 Hear Tone ${w.tone}</button>
        </div>
      `;
      container.appendChild(card);
    });
  } catch (err) {
    loader.style.display = 'none';
    container.innerHTML = `<div style="grid-column: 1/-1; color: var(--t3-color);">Error loading words.</div>`;
    console.error(err);
  }
}

// -------------------------------------------------------------
// 6-TONE STUDIO MODULE
// -------------------------------------------------------------
async function loadTonesStudio() {
  try {
    const res = await fetch('/api/tones');
    toneProfiles = await res.json();
    const container = document.getElementById('tonesContainer');
    container.innerHTML = '';

    toneProfiles.forEach(t => {
      const card = document.createElement('div');
      card.className = 'tone-card';
      card.innerHTML = `
        <div class="tone-card-header">
          <div>
            <div class="tone-title">Tone ${t.tone_number}: ${t.tone_name}</div>
            <div style="font-size: 0.85rem; color: var(--text-dim);">Chao: <b>${t.pitch_contour}</b> • IPA: <b>${t.ipa_symbol}</b></div>
          </div>
          <span class="tone-badge t${t.tone_number}">Tone ${t.tone_number}</span>
        </div>
        <div class="tone-canvas-container">
          <canvas id="canvasTone${t.tone_number}" class="tone-canvas" width="300" height="100"></canvas>
        </div>
        <div class="tone-details">
          <div><b>Gedney Class:</b> ${t.gedney_origin}</div>
          <div><b>Phonetic Feature:</b> ${t.creaky_voice ? 'Creaky Voice (Laryngealized)' : (t.glottal_stop ? 'Glottal Stop Closure [ʔ]' : 'Modal Voice')}</div>
          <div><b>Description:</b> ${t.description}</div>
        </div>
        <button class="btn btn-primary" onclick="playTonePitch(${t.tone_number})">
          🔊 Synthesize Tone ${t.tone_number} Contour
        </button>
      `;
      container.appendChild(card);

      // Draw pitch curve on canvas
      setTimeout(() => drawToneContour(`canvasTone${t.tone_number}`, t), 50);
    });
  } catch (err) {
    console.error('Failed to load tones studio', err);
  }
}

function drawToneContour(canvasId, toneData) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const w = canvas.width;
  const h = canvas.height;

  ctx.clearRect(0, 0, w, h);

  // Background grid
  ctx.strokeStyle = "rgba(255, 255, 255, 0.05)";
  ctx.lineWidth = 1;
  for (let y = 20; y < h; y += 20) {
    ctx.beginPath();
    ctx.moveTo(0, y);
    ctx.lineTo(w, y);
    ctx.stroke();
  }

  // Draw frequency curve
  const points = toneData.points;
  if (!points || points.length === 0) return;

  const minFreq = 100;
  const maxFreq = 240;

  ctx.strokeStyle = "#38bdf8";
  ctx.lineWidth = 3;
  ctx.beginPath();

  points.forEach((pt, i) => {
    const x = 20 + (pt.time / toneData.duration_sec) * (w - 40);
    // Invert y: high freq = top (low y)
    const normalizedY = (pt.freq - minFreq) / (maxFreq - minFreq);
    const y = h - 15 - normalizedY * (h - 30);

    if (i === 0) ctx.moveTo(x, y);
    else ctx.lineTo(x, y);
  });
  ctx.stroke();

  // Glow points
  points.forEach(pt => {
    const x = 20 + (pt.time / toneData.duration_sec) * (w - 40);
    const normalizedY = (pt.freq - minFreq) / (maxFreq - minFreq);
    const y = h - 15 - normalizedY * (h - 30);
    ctx.fillStyle = "#fbbf24";
    ctx.beginPath();
    ctx.arc(x, y, 4, 0, Math.PI * 2);
    ctx.fill();
  });
}

// -------------------------------------------------------------
// TRANSLITERATION & VIRTUAL KEYBOARD MODULE
// -------------------------------------------------------------
function initTransliteration() {
  const btn = document.getElementById('btnTransliterate');
  const input = document.getElementById('transInput');
  const output = document.getElementById('transOutput');
  const sourceSel = document.getElementById('transSource');
  const targetSel = document.getElementById('transTarget');

  btn.addEventListener('click', async () => {
    const text = input.value.trim();
    if (!text) {
      output.value = "";
      return;
    }
    const params = new URLSearchParams({
      text: text,
      source: sourceSel.value,
      target: targetSel.value,
    });
    try {
      const res = await fetch(`/api/transliterate?${params.toString()}`);
      const data = await res.json();
      output.value = data.result;
    } catch (err) {
      output.value = "Transliteration error: " + err.message;
    }
  });

  // Virtual keyboard key clicks
  const keys = document.querySelectorAll('.key-btn');
  keys.forEach(k => {
    k.addEventListener('click', () => {
      const char = k.getAttribute('data-char');
      input.value += char;
      input.focus();
    });
  });
}

// -------------------------------------------------------------
// PHRASEBOOK MODULE
// -------------------------------------------------------------
async function loadPhrases() {
  const cat = document.getElementById('phraseCatFilter').value;
  const container = document.getElementById('phrasesContainer');
  const params = cat ? `?category=${encodeURIComponent(cat)}` : "";

  try {
    const res = await fetch(`/api/phrases${params}`);
    const phrases = await res.json();
    container.innerHTML = "";

    phrases.forEach(p => {
      const card = document.createElement('div');
      card.className = 'phrase-card';
      card.innerHTML = `
        <div class="phr-top">
          <span class="phr-cat">${p.category}</span>
        </div>
        <div class="phr-liktai">${p.lik_tai}</div>
        <div class="phr-roman">${p.roman}</div>
        <div class="phr-en">${p.english}</div>
        <div class="phr-as">${p.assamese_trans || ''}</div>
        ${p.context ? `<div class="phr-context">${p.context}</div>` : ''}
      `;
      container.appendChild(card);
    });
  } catch (err) {
    console.error('Failed to load phrases', err);
  }
}

// -------------------------------------------------------------
// GRAMMAR & TOOLS MODULE
// -------------------------------------------------------------
function initGrammarTools() {
  // Classifier
  document.getElementById('btnQuantify').addEventListener('click', async () => {
    const noun = document.getElementById('clfNounSelect').value;
    const count = document.getElementById('clfCountInput').value;
    const res = await fetch(`/api/quantify?noun=${encodeURIComponent(noun)}&count=${count}`);
    const data = await res.json();
    document.getElementById('clfResRoman').textContent = data.phrase_roman;
    document.getElementById('clfResScripts').innerHTML = `Lik Tai: <b>${data.lik_tai}</b> • Assamese: <b>${data.assamese}</b>`;
    document.getElementById('clfResMeaning').innerHTML = `Classifier: <code>${data.classifier}</code> (${data.classifier_meaning})`;
  });

  // Naming
  document.getElementById('btnGenerateName').addEventListener('click', async () => {
    const gender = document.getElementById('nameGender').value;
    const order = document.getElementById('nameOrder').value;
    const clan = document.getElementById('nameClan').value;
    const personal = document.getElementById('namePersonal').value;
    const res = await fetch(`/api/naming?gender=${gender}&order=${order}&clan=${clan}&personal=${encodeURIComponent(personal)}`);
    const data = await res.json();
    document.getElementById('nameResFull').textContent = data.full_roman;
    document.getElementById('nameResSignificance').textContent = `${data.meaning} • Clan: ${data.clan}`;
  });

  // Numerals
  document.getElementById('btnConvertNum').addEventListener('click', async () => {
    const num = document.getElementById('numInput').value;
    const res = await fetch(`/api/numeral?num=${num}`);
    const data = await res.json();
    document.getElementById('numResRoman').textContent = data.roman;
    document.getElementById('numResScripts').innerHTML = `Lik Tai: <b>${data.lik_tai}</b> • Assamese: <b>${data.assamese}</b>`;
  });
}

// -------------------------------------------------------------
// CORPUS & FOLK TEXTS MODULE
// -------------------------------------------------------------
async function loadCorpus() {
  const container = document.getElementById('corpusContainer');
  try {
    const res = await fetch('/api/texts');
    const texts = await res.json();
    container.innerHTML = "";

    texts.forEach(t => {
      const card = document.createElement('div');
      card.className = 'text-card';

      let sentencesHtml = "";
      t.sentences.forEach(s => {
        sentencesHtml += `
          <div class="sentence-block">
            <div class="sent-liktai">${s.lik_tai}</div>
            <div class="sent-roman">${s.text_roman}</div>
            <div class="sent-morphemes">${s.morphemes.join(' - ')}</div>
            <div class="sent-glosses">${s.glosses.join(' - ')}</div>
            <div class="sent-trans-en"><b>EN:</b> "${s.free_translation_en}"</div>
            <div class="sent-trans-as"><b>AS:</b> "${s.free_translation_as}"</div>
          </div>
        `;
      });

      card.innerHTML = `
        <h3>${t.title_english}</h3>
        <div style="color: var(--accent-gold); font-size: 1.1rem; margin-bottom: 0.4rem;">${t.title_khamyang}</div>
        <div class="text-meta">
          Genre: <b>${t.genre}</b> • Informant: <b>${t.informant}</b> • Village: <b>${t.village}</b>
        </div>
        <p style="color: var(--text-muted); margin-bottom: 1rem; font-size: 0.9rem;">${t.description}</p>
        <div class="sentences-list">
          ${sentencesHtml}
        </div>
      `;
      container.appendChild(card);
    });
  } catch (err) {
    console.error('Failed to load corpus', err);
  }
}

// -------------------------------------------------------------
// KINSHIP & FAMILY MODULE
// -------------------------------------------------------------
async function initKinshipTools() {
  const kinSelect = document.getElementById('kinSelect');
  const resultCard = document.getElementById('kinResultCard');
  const clansList = document.getElementById('clansList');
  if (!kinSelect || !resultCard) return;

  async function resolveSelected() {
    const code = kinSelect.value;
    try {
      const res = await fetch(`/api/kinship/resolve?code=${encodeURIComponent(code)}`);
      if (!res.ok) return;
      const data = await res.json();
      const term = data.term;
      resultCard.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 0.5rem;">
          <span style="font-size: 1.5rem; font-weight: 700; color: var(--accent-gold);">${term.khamyang_roman}</span>
          <span style="font-size: 1.6rem; color: var(--primary);" class="tai-script">${term.lik_tai}</span>
        </div>
        <div style="font-size: 1.1rem; color: #c084fc; margin-bottom: 0.4rem;">${term.assamese_script} (${term.assamese})</div>
        <div style="font-size: 0.95rem; color: var(--text-main); margin-bottom: 0.4rem;">
          <b>English:</b> ${term.english} • <b>IPA:</b> <code>/${term.ipa}/</code> (Tone ${term.tone})
        </div>
        <div style="font-size: 0.85rem; color: var(--primary); margin-bottom: 0.4rem;">
          <b>Generation:</b> ${term.generation > 0 ? '+' + term.generation + ' Ascending' : (term.generation < 0 ? term.generation + ' Descending' : 'Ego Level')} • <b>Lineage:</b> ${term.line} (${term.side})
        </div>
        <div style="font-size: 0.85rem; color: var(--accent-gold); margin-bottom: 0.4rem;">
          <b>Address Form:</b> "${term.address_term}"
        </div>
        <p style="font-size: 0.85rem; color: var(--text-muted); line-height: 1.4; border-top: 1px solid var(--border-color); padding-top: 0.5rem; margin-top: 0.5rem;">
          ${term.cultural_notes}
        </p>
      `;
    } catch (err) {
      console.error('Error resolving kinship', err);
    }
  }

  kinSelect.addEventListener('change', resolveSelected);
  resolveSelected();

  // Load clans
  try {
    const cRes = await fetch('/api/kinship/clans');
    const clans = await cRes.json();
    if (clansList) {
      clansList.innerHTML = '';
      clans.forEach(c => {
        const el = document.createElement('div');
        el.className = 'clan-card';
        el.innerHTML = `
          <div class="clan-card-header">
            <span class="clan-name">${c.name_tai} <span class="tai-script">(${c.lik_tai})</span></span>
            <span class="clan-meaning">${c.meaning}</span>
          </div>
          <div class="clan-role">${c.role}</div>
        `;
        clansList.appendChild(el);
      });
    }
  } catch (err) {
    console.error('Error loading clans', err);
  }
}

// -------------------------------------------------------------
// TRADITIONAL SONGS (Fɯn) MODULE
// -------------------------------------------------------------
async function loadSongs(query = "") {
  const container = document.getElementById('songsContainer');
  if (!container) return;
  try {
    let url = '/api/songs';
    if (query) url += `?q=${encodeURIComponent(query)}`;
    const res = await fetch(url);
    const songs = await res.json();
    container.innerHTML = "";

    if (songs.length === 0) {
      container.innerHTML = "<p style='color: var(--text-muted); padding: 2rem;'>No songs found.</p>";
      return;
    }

    songs.forEach(s => {
      const card = document.createElement('div');
      card.className = 'song-card';

      let stanzasHtml = "";
      (s.stanzas || []).forEach(st => {
        let linesHtml = "";
        (st.lines || []).forEach(l => {
          linesHtml += `
            <div class="song-line">
              <div class="line-khamyang">${l.roman}</div>
              <div class="line-liktai">${l.lik_tai}</div>
              <div class="line-assamese">${l.assamese_script} (${l.translation_as})</div>
              <div class="line-en">EN: "${l.translation_en}"</div>
            </div>
          `;
        });

        stanzasHtml += `
          <div class="stanza-block">
            <div class="stanza-num">Stanza ${st.stanza_number}</div>
            ${linesHtml}
          </div>
        `;
      });

      card.innerHTML = `
        <div class="song-header">
          <div class="song-title-group">
            <h3>🎵 ${s.title_khamyang} (${s.title_english})</h3>
            <div class="song-subtitles">
              <span class="tai-script" style="color: var(--accent-gold); font-size: 1.2rem;">${s.title_liktai}</span>
              <span style="color: #c084fc;">${s.title_assamese}</span>
            </div>
          </div>
          <div>
            <span class="song-meta-pill">${s.genre}</span>
          </div>
        </div>
        <div style="font-size: 0.85rem; color: var(--text-dim); margin-bottom: 0.8rem;">
          Informant: <b>${s.informant}</b> • Village: <b>${s.village}</b> • Ref: <b>${s.archive_ref}</b>
        </div>
        <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 1.2rem; line-height: 1.45;">
          ${s.description}
        </p>
        <div class="song-stanzas">
          ${stanzasHtml}
        </div>
      `;
      container.appendChild(card);
    });
  } catch (err) {
    console.error('Failed to load songs', err);
  }
}

// -------------------------------------------------------------
// SCHOLARLY LIBRARY & BIBLIOGRAPHY MODULE
// -------------------------------------------------------------
async function loadBibliography(query = "") {
  const container = document.getElementById('bibContainer');
  if (!container) return;
  try {
    let url = '/api/bibliography';
    if (query) url += `?q=${encodeURIComponent(query)}`;
    const res = await fetch(url);
    const entries = await res.json();
    container.innerHTML = "";

    if (entries.length === 0) {
      container.innerHTML = "<p style='color: var(--text-muted); padding: 2rem;'>No bibliographic entries found.</p>";
      return;
    }

    entries.forEach(e => {
      const card = document.createElement('div');
      card.className = 'bib-card';

      const authorsStr = (e.authors || []).join(', ');
      const linkHtml = e.url ? `<a href="${e.url}" target="_blank" rel="noopener noreferrer" class="bib-link">🔗 Access Resource / Archive ↗</a>` : '';

      card.innerHTML = `
        <div class="bib-top">
          <span class="bib-type-badge">${e.entry_type}</span>
          <span style="font-size: 0.85rem; color: var(--accent-gold); font-weight: 600;">${e.year || ''}</span>
        </div>
        <h4 class="bib-title">${e.title}</h4>
        <div class="bib-authors">${authorsStr} • ${e.publisher || e.journal || ''}</div>
        <p class="bib-desc">${e.description || ''}</p>
        ${linkHtml}
      `;
      container.appendChild(card);
    });
  } catch (err) {
    console.error('Failed to load bibliography', err);
  }
}

// -------------------------------------------------------------
// INITIALIZATION
// -------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
  initTabs();
  loadCategories();
  searchDictionary();
  loadTonesStudio();
  initTransliteration();
  loadPhrases();
  initGrammarTools();
  initKinshipTools();
  loadSongs();
  loadBibliography();
  loadCorpus();

  // Search event listeners
  document.getElementById('dictSearchBtn').addEventListener('click', searchDictionary);
  document.getElementById('dictSearchInput').addEventListener('keyup', (e) => {
    if (e.key === 'Enter') searchDictionary();
  });
  document.getElementById('categoryFilter').addEventListener('change', searchDictionary);
  document.getElementById('toneFilter').addEventListener('change', searchDictionary);
  document.getElementById('dictResetBtn').addEventListener('click', () => {
    document.getElementById('dictSearchInput').value = '';
    document.getElementById('categoryFilter').value = '';
    document.getElementById('toneFilter').value = '';
    searchDictionary();
  });

  document.getElementById('phraseCatFilter').addEventListener('change', loadPhrases);

  // Songs listeners
  const songSearchBtn = document.getElementById('songSearchBtn');
  const songSearchInput = document.getElementById('songSearchInput');
  const songResetBtn = document.getElementById('songResetBtn');
  if (songSearchBtn && songSearchInput) {
    songSearchBtn.addEventListener('click', () => loadSongs(songSearchInput.value));
    songSearchInput.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') loadSongs(songSearchInput.value);
    });
  }
  if (songResetBtn) {
    songResetBtn.addEventListener('click', () => {
      if (songSearchInput) songSearchInput.value = '';
      loadSongs();
    });
  }

  // Bibliography listeners
  const bibSearchBtn = document.getElementById('bibSearchBtn');
  const bibSearchInput = document.getElementById('bibSearchInput');
  const bibResetBtn = document.getElementById('bibResetBtn');
  if (bibSearchBtn && bibSearchInput) {
    bibSearchBtn.addEventListener('click', () => loadBibliography(bibSearchInput.value));
    bibSearchInput.addEventListener('keyup', (e) => {
      if (e.key === 'Enter') loadBibliography(bibSearchInput.value);
    });
  }
  if (bibResetBtn) {
    bibResetBtn.addEventListener('click', () => {
      if (bibSearchInput) bibSearchInput.value = '';
      loadBibliography();
    });
  }
});

