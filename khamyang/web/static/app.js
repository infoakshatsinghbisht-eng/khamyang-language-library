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
});
