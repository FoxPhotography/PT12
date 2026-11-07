import random, html, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data_nutri import TABS, TF_DRILL, MID
MIDONLY = '--mid' in sys.argv
if MIDONLY:
    sys.argv.remove('--mid'); TABS = [MID]
MODE = 'sec'

esc = lambda s: html.escape(s, quote=False)
BASE_CSS = re.search(r'<style>(.*?)</style>', open(os.path.join(HERE, 'base_template.html'), encoding='utf8').read(), re.S).group(1)

TARGETS = [0, 1, 2, 3] * 120
random.Random(11).shuffle(TARGETS)
COUNT = {'q': 0}

def card(n, text, options, ci, tag, expl):
    COUNT['q'] += 1
    badge = {'qz': '<span class="q-badge dr">★ كويز الدكتورة</span>', 'imp': '<span class="q-badge imp">مهم</span>', 'tf': '<span class="q-badge imp">T / F</span>'}.get(tag, '')
    o = [f'<div class="q-card{" is-dr" if tag=="qz" else ""}" onclick="toggleQ(this)">',
         f'<div class="q-header"><div class="q-num">Q{n}</div><div class="q-text">{badge}{esc(text)}</div><div class="q-toggle">▼</div></div>',
         '<div class="q-body"><div class="options">']
    for k, opt in enumerate(options):
        o.append(f'<div class="option{" correct" if k==ci else ""}" onclick="selectOpt(event,this)"><div class="opt-letter">{"ABCDE"[k]}</div>{esc(opt)}</div>')
    o.append('</div>')
    if expl: o.append(f'<div class="q-explain">💡 {esc(expl)}</div>')
    o.append('</div></div>')
    return ''.join(o)

def shuffled(opts, text):
    if any(x in o for o in opts for x in ('All of the above', 'None of the above', 'A+B', 'A + B')):
        return opts, 0
    ci = TARGETS.pop()
    wrong = opts[1:]; random.Random(text).shuffle(wrong)
    ci = min(ci, len(opts) - 1)
    return wrong[:ci] + [opts[0]] + wrong[ci:], ci

def group(title, qs, icon_n, fixed=False):
    out = [f'<div class="topic-group"><div class="topic-header"><div class="topic-icon">{icon_n:02d}</div><div class="topic-title">{esc(title)}</div><div class="topic-count">{len(qs)} أسئلة</div></div>']
    for i, q in enumerate(qs, 1):
        if fixed:
            text, opts, ci, expl = q; tag = 'tf'
        else:
            text, opts, tag, expl = q
            opts, ci = shuffled(opts, text)
        out.append(card(i, text, opts, ci, tag, expl))
    out.append('</div>')
    return ''.join(out)

sections, nav = [], []

def search(sec):
    return f'<div class="search-wrap"><span class="search-icon">🔍</span><input class="search-input" placeholder="ابحث في الأسئلة..." oninput="searchQ(this.value,\'{sec}\')"></div>'

WCOUNT = {'w': 0}
def written(n, q, src, ans):
    WCOUNT['w'] += 1
    return (f'<details class="w-card"><summary><span class="q-num">W{n}</span><span class="w-q">{esc(q)}</span>'
            f'<span class="w-src">{esc(src)}</span></summary><div class="w-ans"><div class="w-lbl">✍️ الإجابة النموذجية</div>{ans}</div></details>')


def lec_tab(tid, title, short, icon, source, summary, groups, active=False):
    n = sum(len(g[1]) for g in groups)
    s_ = [f'<div class="section{" active" if active else ""}" id="{tid}">',
         f'<div class="lec-banner"><div class="lec-icon">{icon}</div><div><div class="lec-title">{esc(title)}</div><div class="lec-sub">المصدر: {esc(source)} · {n} سؤال</div></div></div>',
         '<details class="summary-box" open><summary>📖 الملخص</summary><div class="summary">' + summary + '</div></details>',
         '<h3 class="quiz-title">اختبر نفسك</h3>', search(tid)]
    for i, g in enumerate(groups, 1):
        s_.append(group(g[0], g[1], i, fixed=(len(g) > 2)).replace('<span class="q-badge imp">T / F</span>', '<span class="q-badge dr">★ أسئلة الدفعة</span>') if len(g) > 2 else group(g[0], g[1], i))
    s_.append('</div>')
    sections.append(''.join(s_)); nav.append((tid, f'{icon} {short}'))

for k, (tid, title, short, icon, src, summary, groups) in enumerate(TABS):
    summary = re.sub(r'(\d+(?:\.\d+)?\s?:\s?\d+(?:\.\d+)?)', r'<span dir="ltr">\1</span>', summary)
    lec_tab(tid, title, short, icon, src, summary, groups, active=(k == 0))
tfo = ["True ✓", "False ✗"]
if not MIDONLY: sections.append('<div class="section" id="tf"><div class="info-banner">جمل صح وغلط من الـ 6 محاضرات، على الحاجات اللي ممكن تتقلب في الامتحان.</div>' + search('tf') +
    group('True or False', [(t, tfo, c_, e) for t, c_, e in TF_DRILL], 1, fixed=True) + '</div>')
if not MIDONLY: nav.append(('tf', '✅ صح وغلط'))
WN = WCOUNT['w']
TOTAL = COUNT['q']
nav_html = '<a href="../../index.html" class="nav-btn">🔙 الرئيسية</a>' + ''.join(
    f'<button class="nav-btn{" active" if i==0 else ""}" onclick="showSection(\'{sid}\')" id="btn-{sid}">{esc(lbl)}</button>' for i, (sid, lbl) in enumerate(nav)) + \
'<button class="nav-btn" onclick="showAllAnswers()">👁️ إظهار الإجابات</button><button class="nav-btn" onclick="retest()">🔄 إعادة</button>'

EXTRA_CSS = """
  .vit { border:1px solid var(--border); border-radius:10px; padding:10px 14px; margin:10px 0; background:rgba(232,210,181,.03); }
  .vit-h { font-weight:800; color:var(--beige); margin-bottom:4px; }
  .vit ul { margin:0; }
  .info-banner { background:linear-gradient(135deg,rgba(89,9,7,.55),rgba(43,44,38,.9)); border:1px solid var(--border2); border-right:4px solid #8c1a12; border-radius:12px; padding:14px 18px; font-size:14px; line-height:1.9; margin-bottom:22px; direction:rtl; }
  .info-banner b { color:var(--beige); }
  .case-intro { background:var(--card); border:1px dashed var(--border2); border-radius:10px; padding:12px 16px; margin:-8px 0 14px; direction:ltr; font-size:14px; line-height:1.7; }
  .q-explain { display:none; margin-top:12px; padding:10px 14px; border-radius:8px; background:rgba(232,210,181,.06); border:1px solid var(--border); font-size:13.5px; line-height:1.8; color:var(--muted); direction:rtl; }
  .q-card.answered .q-explain, .show-all-mode .q-explain { display:block; }
  .summary-box { margin-bottom:26px; }
  .summary-box > summary { cursor:pointer; list-style:none; font-weight:800; font-size:16px; padding:12px 18px; border-radius:12px; background:linear-gradient(135deg,#43443b,#2b2c26); border:1px solid var(--border2); }
  .summary-box > summary::-webkit-details-marker { display:none; }
  .summary-box[open] > summary { border-radius:12px 12px 0 0; }
  .summary { direction:rtl; }
  .summary-box .summary { border:1px solid var(--border2); border-top:none; border-radius:0 0 12px 12px; padding:16px; background:rgba(43,44,38,.55); }
  .summary .card { background:linear-gradient(150deg,#33342d,#26271f); border:1px solid var(--border); border-radius:12px; padding:16px 18px; margin-bottom:14px; font-size:14px; line-height:1.95; }
  .summary h4 { font-size:16px; color:var(--beige); margin-bottom:8px; font-weight:800; }
  .summary ul, .summary ol { padding-right:20px; } .summary li { margin-bottom:4px; }
  .summary .ltr, .ltr { direction:ltr; text-align:left; }
  .summary ol.ltr, .topics { padding-left:22px; padding-right:0; }
  .summary b { color:var(--accent); }
  .summary .key { margin-top:10px; padding:10px 14px; border-radius:8px; background:linear-gradient(135deg,rgba(140,26,18,.35),rgba(89,9,7,.18)); border:1px solid rgba(240,147,127,.35); }
  .summary table { width:100%; border-collapse:collapse; margin:8px 0; font-size:13px; }
  .summary th { background:linear-gradient(135deg,#7a1e18,#590907); color:var(--beige); padding:8px 10px; text-align:right; font-weight:700; }
  .summary td { padding:8px 10px; border-bottom:1px solid var(--border); vertical-align:top; }
  .summary td:first-child { color:var(--accent); font-weight:700; }
  .summary .card { overflow-x:auto; }
  .topics li { display:flex; justify-content:space-between; align-items:center; gap:10px; padding:7px 0; border-bottom:1px dashed var(--border); }
  .topics .go { all:unset; cursor:pointer; font-family:'Cairo',sans-serif; font-size:12px; font-weight:700; padding:3px 12px; border-radius:100px; background:linear-gradient(135deg,#8a2a1f,#590907); color:var(--beige); white-space:nowrap; }
  .quiz-title { font-size:20px; font-weight:900; margin:6px 0 16px; direction:rtl; }
  .hint { direction:rtl; color:var(--muted); font-size:13.5px; margin:-8px 0 14px; }
  .w-card { background:var(--card); border:1px solid var(--border2); border-radius:14px; margin-bottom:12px; overflow:hidden; }
  .w-card > summary { cursor:pointer; list-style:none; display:flex; gap:12px; align-items:flex-start; padding:16px 18px; direction:ltr; }
  .w-card > summary::-webkit-details-marker { display:none; }
  .w-card .q-num { flex-shrink:0; }
  .w-q { flex:1; font-weight:700; font-size:15px; line-height:1.6; }
  .w-src { flex-shrink:0; font-size:11.5px; font-weight:700; padding:3px 10px; border-radius:100px; background:linear-gradient(135deg,#8a2a1f,#590907); color:var(--beige); direction:rtl; }
  .w-ans { border-top:1px dashed var(--border2); padding:14px 18px 18px; direction:rtl; font-size:14px; line-height:1.95; }
  .w-ans .ltr { direction:ltr; text-align:left; }
  .w-ans ul, .w-ans ol { padding-right:20px; } .w-ans ul.ltr, .w-ans ol.ltr { padding-left:20px; padding-right:0; }
  .w-ans b { color:var(--accent); }
  .w-ans table { width:100%; border-collapse:collapse; margin:8px 0; font-size:13px; direction:ltr; }
  .w-ans th { background:linear-gradient(135deg,#7a1e18,#590907); color:var(--beige); padding:7px 9px; text-align:left; }
  .w-ans td { padding:7px 9px; border-bottom:1px solid var(--border); }
  .w-lbl { font-weight:800; color:var(--beige); margin-bottom:8px; }
  .xgrid { display:grid; grid-template-columns:repeat(auto-fit,minmax(280px,1fr)); gap:12px; margin-top:10px; direction:ltr; }
  .xbox { background:linear-gradient(150deg,#33342d,#26271f); border:1px solid var(--border); border-radius:12px; padding:12px; }
  .xt { font-weight:800; color:var(--beige); text-align:center; margin-bottom:8px; }
  .xd { position:relative; height:200px; }
  @media (max-width:420px) { .xl { font-size:11px; padding:3px 6px; } .xd { height:215px; } }
  .xd svg { position:absolute; inset:0; width:100%; height:100%; }
  .xd line { stroke-width:2.2; stroke-linecap:round; vector-effect:non-scaling-stroke; }
  .xd line.lt { stroke:#e0604f; stroke-width:4; } .xd line.lw { stroke:#d9c9a3; stroke-width:4; stroke-dasharray:8 6; }
  .xl { position:absolute; max-width:47%; font-size:12px; line-height:1.35; font-weight:600; background:rgba(30,31,26,.88); padding:4px 8px; border-radius:8px; }
  .xl.t { color:#f3a594; border:1px solid rgba(224,96,79,.6); } .xl.w { color:#e8d2b5; border:1px dashed rgba(232,210,181,.55); }
  .xl.tl { top:0; left:0; } .xl.tr { top:0; right:0; text-align:right; } .xl.bl { bottom:0; left:0; } .xl.br { bottom:0; right:0; text-align:right; }
  .xr { font-size:13px; color:var(--muted); margin-top:8px; text-align:center !important; }
"""

TPL = f"""<!DOCTYPE html>
<html lang="ar" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{"Nutrition — تجميعة الميد" if MIDONLY else "Nutrition — Summaries & MCQ"}</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{BASE_CSS}{EXTRA_CSS}</style>
</head>
<body>
<header>
  <div class="header-badge">🍎 Nutrition · د. سيد حنورة</div>
  <h1>{"تجميعة الميد" if MIDONLY else "Nutrition"}</h1>
  <p class="subtitle">{"Water · Beverage levels · Healthy eating · Eat smart" if MIDONLY else "Macronutrients · Vitamins · Minerals · Water · Healthy diet"}</p>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">{len(TABS)}</div><div class="stat-label">{"ورقة أرقام" if MIDONLY else "ملخصات"}</div></div>
    <div class="stat"><div class="stat-num">{TOTAL}</div><div class="stat-label">سؤال</div></div>
{"" if MODE == "sec" else f'    <div class="stat"><div class="stat-num">{WN}</div><div class="stat-label">سؤال written</div></div>'}
    <div class="stat"><div class="stat-num" id="score-display">0/{TOTAL}</div><div class="stat-label">إجابات صحيحة</div></div>
  </div>
</header>
<nav class="nav">{nav_html}</nav>
<main>
{''.join(sections)}
</main>
<script>
  let score = 0, showAllMode = false; const TOTAL = {TOTAL};
  function showSection(id) {{
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.getElementById(id).classList.add('active');
    document.getElementById('btn-' + id)?.classList.add('active');
    window.scrollTo({{top: document.querySelector('.nav').offsetTop, behavior: 'smooth'}});
  }}
  function toggleQ(card) {{ if (card.classList.contains('answered')) return; card.classList.toggle('open'); }}
  function selectOpt(e, opt) {{
    e.stopPropagation(); const card = opt.closest('.q-card');
    if (card.classList.contains('answered') || showAllMode) return;
    if (opt.classList.contains('correct')) {{ score++; opt.classList.add('pop-animation'); }} else opt.classList.add('wrong-selected');
    card.classList.add('answered', 'open'); updateScore();
  }}
  function updateScore() {{ document.getElementById('score-display').textContent = score + '/' + TOTAL; }}
  function showAllAnswers() {{ showAllMode = true; document.querySelectorAll('.q-card').forEach(c => c.classList.add('open')); document.body.classList.add('show-all-mode'); }}
  function retest() {{
    score = 0; showAllMode = false; document.body.classList.remove('show-all-mode');
    document.querySelectorAll('.q-card').forEach(c => {{ c.classList.remove('answered', 'open', 'pop-animation'); c.querySelectorAll('.option').forEach(o => o.classList.remove('wrong-selected', 'pop-animation')); }});
    updateScore();
  }}
  function searchQ(val, sec) {{
    const v = val.trim().toLowerCase();
    document.querySelectorAll('#' + sec + ' .q-card').forEach(card => {{ card.style.display = (!v || card.textContent.toLowerCase().includes(v)) ? '' : 'none'; }});
  }}
</script>
</body>
</html>
"""
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'midterm.html')
open(out, 'w', encoding='utf8').write(TPL)
print('mcq', TOTAL, '->', out)
