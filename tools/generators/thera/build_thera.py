import random, html, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data_l1 import LECTURES
import data_l2
import data_sec
MODE = sys.argv[2] if len(sys.argv) > 2 else 'mid'
SEC = [x for x in LECTURES if x['id'] == 'sec'][0]
LECTURES[:] = [x for x in LECTURES if x['id'] != 'sec']
from data_exam import QUIZ_WRITTEN, EXPECTED_WRITTEN, CASES, CASES_WRITTEN, TF_DRILL, PREDICTED

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
    n = sum(len(q) for _, q in groups)
    s_ = [f'<div class="section{" active" if active else ""}" id="{tid}">',
         f'<div class="lec-banner"><div class="lec-icon">{icon}</div><div><div class="lec-title">{esc(title)}</div><div class="lec-sub">المصدر: {esc(source)} · {n} سؤال</div></div></div>',
         '<details class="summary-box" open><summary>📖 الملخص</summary><div class="summary">' + summary + '</div></details>',
         '<h3 class="quiz-title">اختبر نفسك</h3>', search(tid)]
    for i, (gt, qs) in enumerate(groups, 1):
        s_.append(group(gt, qs, i))
    s_.append('</div>')
    sections.append(''.join(s_)); nav.append((tid, f'{icon} {short}'))

if MODE == 'sec':
    cards = ['<div class="card">' + c for c in SEC['summary'].split('<div class="card">')[1:]]
    G = SEC['groups']
    SRC = SEC['source']
    TABS = [('basics', 'Basics & Landmarks — أساسيات السكشن', 'Landmarks', '📍', [0, 1], [0, 1]),
            ('mait', 'Maitland — Cervical, Thoracic & Lumbar', 'Maitland', '🖐️', [2, 3, 4], [2, 3]),
            ('ribs', 'Ribs — Assessment & Mobilization', 'Ribs', '🫁', [5, 6], [4]),
            ('mull', 'Mulligan — Cervical, Thoracic & Lumbar', 'Mulligan', '🤝', [7, 8], [5]),
            ('nerve', 'Nerve Entrapment & Traction', 'Nerve & Traction', '🧵', [9], [6])]
    for k, (tid, title, short, icon, ci, gi) in enumerate(TABS):
        lec_tab(tid, title, short, icon, SRC, ''.join(cards[i] for i in ci), [G[i] for i in gi], active=(k == 0))
else:
    # ---- tab: predicted exam
    pe = ['<div class="section active" id="pred">',
          '<div class="info-banner"><b>شكل الميدتيرم الجديد (د. ياسمين):</b> <b>Case واحدة وعليها 20 سؤال MCQ</b>، ورقي في المدرج، يوم <b>الاتنين الساعة 9</b>، وبعده الدكتورة هتشرح المحاضرة. وميد <b>العملي</b> الأسبوع اللي بعد الجاي (د. ياسمين هتحدد).<br>'
          'هنا <b>3 نماذج متوقعة</b> بنفس الشكل بالظبط (case + 20 MCQ)، ومغطيين كل المحاضرات: الأول على الـ <b>Kyphosis</b> والـ thoracic والـ ribs (الأرجح)، والتاني على الـ safety tests والـ Maitland والـ Mulligan والـ Manipulation والـ Fryette، والتالت على الـ <b>barrel chest</b> والـ posture والـ Fryette 1st law وباقي الأساسيات. حل كل نموذج في <b>نص ساعة</b> كأنك في الامتحان.</div>', search('pred')]
    for i, (title, txt, qs) in enumerate(PREDICTED, 1):
        pe.append(f'<h3 class="quiz-title" style="margin-top:{18 if i>1 else 0}px">{esc(title)}</h3>')
        pe.append(f'<div class="case-intro">🩺 <b>Case:</b> {esc(txt)}</div>')
        pe.append(group(f'نموذج {i} — 20 سؤال', [(q, o, '', e) for q, o, e in qs], i))
    pe.append('</div>')
    sections.append(''.join(pe)); nav.append(('pred', '🎯 الامتحان المتوقع'))

    # ---- tab: exam & quizzes
    ex = ['<div class="section" id="exam">',
          '<div class="info-banner"><b>تحديث:</b> الامتحان بقى <b>case + 20 MCQ</b> بس (شوف تاب الامتحان المتوقع)، فالـ written هنا للفهم والمراجعة. المنهج لحد آخر حاجة وقفنا عندها في الأسبوع اللي قبل الميد. الكويزات اللي فاتت عليها 3 درجات، واللي جاية 3، والميد حوالي 7.<br>'
          'التقسيم هنا: <b>Posture</b> (محاضرة 1 و 2)، <b>Maitland</b> (2 و 3)، <b>Thoracic &amp; Ribs</b> (3 و 4)، <b>Mulligan</b> (4 و 5)، <b>Manipulation</b> (5)، <b>Kyphosis</b> (11/2، لحد سلايد 27). الـ Scoliosis لسه مخدناهوش. والعملي في صفحة لوحده: <b>العملي والسكاشن</b>.</div>',
          '<h3 class="quiz-title">أسئلة كويزات الدكتورة (written)</h3>',
          '<p class="hint">دي الأسئلة اللي الدكتورة سألتها في الكويزات بالنص. اكتب إجابتك الأول وبعدين افتح الإجابة النموذجية.</p>']
    for i, (q, src, a) in enumerate(QUIZ_WRITTEN, 1):
        ex.append(written(i, q, src, a))
    ex.append('<h3 class="quiz-title" style="margin-top:28px">أسئلة written متوقعة</h3>')
    for i, (q, src, a) in enumerate(EXPECTED_WRITTEN, len(QUIZ_WRITTEN) + 1):
        ex.append(written(i, q, src, a))
    ex.append('</div>')
    sections.append(''.join(ex)); nav.append(('exam', '📝 كويزات الدكتورة'))

    # ---- lecture tabs
    for L in LECTURES:
        n = sum(len(q) for _, q in L['groups'])
        s_ = [f'<div class="section" id="{L["id"]}">',
             f'<div class="lec-banner"><div class="lec-icon">{L["icon"]}</div><div><div class="lec-title">{esc(L["title"])}</div><div class="lec-sub">المصدر: {esc(L["source"])} · {n} سؤال</div></div></div>',
             '<details class="summary-box" open><summary>📖 الملخص</summary><div class="summary">' + L['summary'] + '</div></details>',
             '<h3 class="quiz-title">اختبر نفسك</h3>', search(L['id'])]
        for i, (gt, qs) in enumerate(L['groups'], 1):
            s_.append(group(gt, qs, i))
        s_.append('</div>')
        sections.append(''.join(s_)); nav.append((L['id'], f'{L["icon"]} {L["short"]}'))

    # ---- cases
    cs = ['<div class="section" id="cases"><div class="info-banner">نص الامتحان أسئلة على <b>cases</b>. هنا cases MCQ بنفس الفكرة، وتحتها cases written بإجابات نموذجية.</div>', search('cases')]
    for i, (txt, qs) in enumerate(CASES, 1):
        cs.append(f'<div class="case-intro">🩺 <b>Case {i}:</b> {esc(txt)}</div>')
        cs.append(group(f'أسئلة Case {i}', [(q, o, '', e) for q, o, e in qs], i))
    cs.append('<h3 class="quiz-title" style="margin-top:28px">Cases — written</h3>')
    for i, (txt, q, a) in enumerate(CASES_WRITTEN, 1):
        cs.append(written(f'C{i}', f'{txt} — {q}', 'case', a))
    cs.append('</div>')
    sections.append(''.join(cs)); nav.append(('cases', '🩺 Cases'))

    # ---- T/F drill
    tf = ["True ✓", "False ✗"]
    sections.append('<div class="section" id="tf"><div class="info-banner">تدريب سريع على الجمل اللي ممكن تتقلب في الـ MCQ.</div>' + search('tf') +
                    group('True or False', [(t, tf, c, e) for t, c, e in TF_DRILL], 1, fixed=True) + '</div>')
    nav.append(('tf', '✅ صح وغلط'))
WN = WCOUNT['w']
TOTAL = COUNT['q']
nav_html = '<a href="../../index.html" class="nav-btn">🔙 الرئيسية</a>' + ''.join(
    f'<button class="nav-btn{" active" if i==0 else ""}" onclick="showSection(\'{sid}\')" id="btn-{sid}">{esc(lbl)}</button>' for i, (sid, lbl) in enumerate(nav)) + \
    ('<a href="midterm.html" class="nav-btn">📘 الميدتيرم النظري</a>' if MODE == 'sec' else '<a href="sections.html" class="nav-btn">👐 العملي والسكاشن</a>') + '<button class="nav-btn" onclick="showAllAnswers()">👁️ إظهار الإجابات</button><button class="nav-btn" onclick="retest()">🔄 إعادة</button>'

EXTRA_CSS = """
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
<title>Therapeutic Exercises II — {'Practical & Sections' if MODE == 'sec' else 'Midterm'}</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{BASE_CSS}{EXTRA_CSS}</style>
</head>
<body>
<header>
  <div class="header-badge">🧍 Therapeutic Exercises II · {"العملي والسكاشن" if MODE == "sec" else "الميدتيرم"}</div>
  <h1>Therapeutic Exercises II</h1>
  <p class="subtitle">{"Landmarks · Maitland · Ribs · Mulligan · Nerve entrapment · Traction" if MODE == "sec" else "Posture · Maitland · Ribs · Mulligan · Manipulation · Kyphosis"}</p>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">{5 if MODE == "sec" else len(LECTURES)}</div><div class="stat-label">ملخصات</div></div>
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
# theme_post: same as tools/theme/post.py (theme.css/js → فهرس المذاكرة + PT Hub pill)
_T = open(out, encoding='utf8').read()
if 'assets/theme.css' not in _T:
    _T = _T.replace('</head>', '<meta name="theme-color" content="#5c5e54">\n<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">\n<link rel="stylesheet" href="../../assets/theme.css?v=3">\n<script src="../../assets/theme.js?v=3" defer></script>\n</head>', 1)
if 'fx-home' not in _T:
    _T = re.sub(r'(<body[^>]*>)', r'\1\n<div class="fx-band" aria-hidden="true"></div>\n<a class="fx-home" href="../../index.html" aria-label="PT Hub"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>PT Hub</a>', _T, count=1)
open(out, 'w', encoding='utf8').write(_T)
print('mcq', TOTAL, 'written', WN, 'lectures', len(LECTURES), '->', out)
