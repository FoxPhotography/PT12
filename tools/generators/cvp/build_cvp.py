import random, html, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data_past import PT9, PT12, PT7, PT7_CASE, PT7_CASE_INTRO, PREV_DOUBLE, PREV_MCQ, PREV_TF, PT10
from data_lectures import LECTURES
from data_topics import TOPICS, TOPICS_SUMMARY, TOPIC_QUESTIONS, TF_DRILL

esc = lambda s: html.escape(s, quote=False)
BASE_CSS = re.search(r'<style>(.*?)</style>', open(os.path.join(HERE, 'base_template.html'), encoding='utf8').read(), re.S).group(1)

TARGETS = [0, 1, 2, 3] * 80
random.Random(11).shuffle(TARGETS)
COUNT = {'q': 0}

def card(n, text, options, ci, tag, expl):
    COUNT['q'] += 1
    badge = {'dr': '<span class="q-badge dr">★ امتحان سابق</span>', 'imp': '<span class="q-badge imp">MIDTERM TOPIC</span>'}.get(tag, '')
    o = [f'<div class="q-card{" is-dr" if tag=="dr" else ""}" onclick="toggleQ(this)">',
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
            text, opts, ci, expl = q; tag = 'dr'
        else:
            text, opts, tag, expl = q
            opts, ci = shuffled(opts, text)
        out.append(card(i, text, opts, ci, tag, expl))
    out.append('</div>')
    return ''.join(out)

sections, nav = [], []

# ---- tab: past exams
tf = ["True ✓", "False ✗"]
past = ['<div class="section active" id="past">',
        '<div class="info-banner"><b>شكل امتحان الميدتيرم (د. محمود لبيب):</b> 30 دقيقة، وفيه MCQ و True/False و Double True/False و Case study. المصدر الكتاب والمحاضرات، والمنهج هو الـ 18 موضوع اللي في تاب "مواضيع الميدتيرم".<br>الامتحانات مترتبة من الأحدث للأقدم: <b>PT12 (دفعتنا)</b> ثم PT10 ثم PT9 (متجمع من اللي الدفعة افتكرته) ثم PT7، وفي الآخر امتحان سابق مش معروف هو بتاع أنهي دفعة. امتحان PT11 مش متاح عندنا، بنفس ترتيب الاختيارات، والإجابات متراجعة على الكتاب والمحاضرات.</div>',
        search('past') if False else '',
        ]
def search(sec):
    return f'<div class="search-wrap"><span class="search-icon">🔍</span><input class="search-input" placeholder="ابحث في الأسئلة..." oninput="searchQ(this.value,\'{sec}\')"></div>'
past[2] = search('past')
past.append(group('PT12 Mid-Term — امتحان دفعتنا', PT12, 1, fixed=True).replace('★ امتحان سابق', '★ PT12'))
past.append(group('PT10 Mid-Term — MCQ', PT10, 2, fixed=True).replace('★ امتحان سابق', '★ PT10'))
past.append(group('PT9 Mid-Term — من النقط اللي افتكرتها الدفعة', [(t, o, '', e) for t, o, c, e in PT9], 3))
past.append(group('PT7 Mid-Term (Form D) — MCQ', PT7, 4, fixed=True).replace('★ امتحان سابق', '★ PT7'))
past.append(f'<div class="case-intro">🩺 <b>Case study (PT7):</b> {esc(PT7_CASE_INTRO)}</div>')
past.append(group('PT7 — Case (True / False)', PT7_CASE, 5, fixed=True).replace('★ امتحان سابق', '★ PT7'))
past.append(group('امتحان سابق (الدفعة مش معروفة) — Double True / False', PREV_DOUBLE, 6, fixed=True))
past.append(group('امتحان سابق (الدفعة مش معروفة) — Choose', PREV_MCQ, 7, fixed=True))
past.append(group('امتحان سابق (الدفعة مش معروفة) — True / False', PREV_TF, 8, fixed=True))
past.append('</div>')
sections.append(''.join(past)); nav.append(('past', '🎯 امتحانات سابقة'))
PAST_N = sum(len(x) for x in (PT9, PT12, PT7, PT7_CASE, PREV_DOUBLE, PREV_MCQ, PREV_TF, PT10))

# ---- tab: 18 topics
lec_short = {L['id']: L['short'] for L in LECTURES}
def _go(w):
    if w == 't': return "document.getElementById('topics-sum').scrollIntoView({behavior:'smooth'})"
    return f"showSection('{w}')"
lst = ''.join(f'<li><span>{esc(t)}</span><button class="go" onclick="{_go(w)}">{"⬇ تحت" if w=="t" else lec_short.get(w, w)}</button></li>' for t, w in TOPICS)
top = [f'<div class="section" id="topics"><div class="info-banner">دي الـ <b>18 موضوع</b> اللي اتحددوا للميدتيرم ومتغطيين في الكتاب. جنب كل موضوع زرار بيوديك لمكان شرحه، والمواضيع اللي مش في المحاضرات متلخصة تحت.</div>',
       f'<div class="summary"><div class="card"><h4>قائمة المواضيع</h4><ol class="topics ltr">{lst}</ol></div></div>',
       '<div class="summary" id="topics-sum">' + TOPICS_SUMMARY + '</div>', '<h3 class="quiz-title">اختبر نفسك</h3>', search('topics')]
for i, (gt, qs) in enumerate(TOPIC_QUESTIONS, 1):
    top.append(group(gt, qs, i))
top.append('</div>')
sections.append(''.join(top)); nav.append(('topics', '📋 مواضيع الميدتيرم'))

# ---- lecture tabs
for L in LECTURES:
    n = sum(len(q) for _, q in L['groups'])
    s = [f'<div class="section" id="{L["id"]}">',
         f'<div class="lec-banner"><div class="lec-icon">{L["icon"]}</div><div><div class="lec-title">{esc(L["title"])}</div><div class="lec-sub">المصدر: {esc(L["source"])} · {n} سؤال</div></div></div>',
         '<details class="summary-box" open><summary>📖 الملخص</summary><div class="summary">' + L['summary'] + '</div></details>',
         '<h3 class="quiz-title">اختبر نفسك</h3>', search(L['id'])]
    for i, (gt, qs) in enumerate(L['groups'], 1):
        s.append(group(gt, qs, i))
    s.append('</div>')
    sections.append(''.join(s)); nav.append((L['id'], f'{L["icon"]} {L["short"]}'))

# ---- T/F drill
tfq = [(t, tf, ci, e) for t, ci, e in TF_DRILL]
sections.append('<div class="section" id="tf"><div class="info-banner">الامتحان فيه جزء صح وغلط. ده تدريب سريع على أكتر الجمل اللي ممكن تتقلب.</div>' + search('tf') +
                group('True or False', [(t, o, c, e) for t, o, c, e in tfq], 1, fixed=True).replace('★ امتحان سابق', 'تدريب') + '</div>')
nav.append(('tf', '✅ صح وغلط'))

TOTAL = COUNT['q']
nav_html = '<a href="../../index.html" class="nav-btn">🔙 الرئيسية</a>' + ''.join(
    f'<button class="nav-btn{" active" if i==0 else ""}" onclick="showSection(\'{sid}\')" id="btn-{sid}">{esc(lbl)}</button>' for i, (sid, lbl) in enumerate(nav)) + \
    '<a href="sections.html" class="nav-btn">🩺 العملي والسكاشن</a><button class="nav-btn" onclick="showAllAnswers()">👁️ إظهار الإجابات</button><button class="nav-btn" onclick="retest()">🔄 إعادة</button>'

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
"""

TPL = f"""<!DOCTYPE html>
<html lang="ar" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CVP PT — Theory Midterm</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>{BASE_CSS}{EXTRA_CSS}</style>
</head>
<body>
<header>
  <div class="header-badge">🫁 CVP PT · ميدتيرم النظري</div>
  <h1>Cardiovascular &amp; Pulmonary PT</h1>
  <p class="subtitle">Chest · Heart · COPD · Asthma · Chest pain · Clinical examination</p>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">{len(LECTURES)}</div><div class="stat-label">ملخصات</div></div>
    <div class="stat"><div class="stat-num">{TOTAL}</div><div class="stat-label">سؤال</div></div>
    <div class="stat"><div class="stat-num">{PAST_N}</div><div class="stat-label">من امتحانات سابقة</div></div>
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
print('questions', TOTAL, 'past', PAST_N, 'lectures', len(LECTURES), '->', out)
