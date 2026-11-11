# Builds year-3/cvp-medicine/mid-bank.html (arg2=mid) or final-bank.html (arg2=final) — cardiac part MCQs with print-to-PDF.
import random, html, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from data_bank import MID, FINAL
MODE = sys.argv[2] if len(sys.argv) > 2 else 'mid'
esc = lambda s: html.escape(s, quote=False)
BASE_CSS = re.search(r'<style>(.*?)</style>', open(os.path.join(HERE, 'base_template.html'), encoding='utf8').read(), re.S).group(1)
L = 'abcd'

def shuffle(text, opts):
    o = opts[:]; random.Random('cvpm|' + text).shuffle(o)
    return o, o.index(opts[0])

def section(sid, title, sub, groups, active):
    out = [f'<div class="section{" active" if active else ""}" id="{sid}">',
           f'<div class="paper-head"><div class="ph-title">{esc(title)}</div><div class="ph-sub">{esc(sub)}</div></div>']
    n, key = 0, []
    for gi, (gt, qs) in enumerate(groups, 1):
        out.append(f'<div class="topic-group"><div class="topic-header"><div class="topic-icon">{gi:02d}</div><div class="topic-title">{esc(gt)}</div><div class="topic-count">{len(qs)} Q</div></div>')
        for text, opts in qs:
            n += 1; o, ci = shuffle(text, opts); key.append(L[ci])
            out.append(f'<div class="xq"><div class="xq-t"><span class="xq-n">{n}.</span> {esc(text)}</div><ol class="xq-o">' +
                       ''.join(f'<li class="{"ans" if k == ci else ""}"><span class="xl">{L[k]})</span> {esc(t)}</li>' for k, t in enumerate(o)) + '</ol></div>')
        out.append('</div>')
    out.append('<div class="topic-group keybox"><div class="topic-header"><div class="topic-icon">✓</div><div class="topic-title">Answer Key</div></div><div class="key">' +
               ''.join(f'<span><b>{i}</b>{a}</span>' for i, a in enumerate(key, 1)) + '</div></div></div>')
    return ''.join(out), n

IS_MID = MODE == 'mid'
body_html, N = section('mid' if IS_MID else 'final', ('Midterm — 20 MCQs' if IS_MID else 'Final — 100 MCQs'), 'Internal Medicine (Cardiology) · Physical Therapy', MID if IS_MID else FINAL, True)
LABEL = 'Midterm' if IS_MID else 'Final'
SID = 'mid' if IS_MID else 'final'
TAB = '📝 Midterm (20)' if IS_MID else '📚 Final (100)'
OTHER = ('final-bank.html', '📚 أسئلة الفاينال (100)') if IS_MID else ('mid-bank.html', '📝 أسئلة الميد (20)')

EXTRA = """
  main { max-width:900px; margin:0 auto; padding:32px 20px 80px; position:relative; z-index:1; }
  .section { display:none; } .section.active { display:block; }
  .paper-head { text-align:center; margin-bottom:22px; }
  .ph-title { font-size:22px; font-weight:900; color:var(--beige); }
  .ph-sub { font-size:13px; color:var(--muted); margin-top:4px; }
  .xq { background:var(--card); border:1px solid var(--border2); border-radius:12px; padding:14px 18px; margin-bottom:10px; direction:ltr; break-inside:avoid; }
  .xq-t { font-weight:700; font-size:15px; line-height:1.6; }
  .xq-n { color:var(--accent); font-weight:900; margin-right:4px; }
  .xq-o { list-style:none; margin:8px 0 0; padding:0 0 0 22px; display:grid; gap:4px; }
  .xq-o li { font-size:14px; line-height:1.55; color:var(--muted); padding:3px 10px; border-radius:7px; border:1px solid transparent; }
  .xl { font-weight:800; margin-right:4px; color:var(--dim); }
  body.show .xq-o li.ans { color:var(--ok); background:var(--ok-bg); border-color:var(--ok-bd); font-weight:700; }
  body.show .xq-o li.ans::after { content:' ✓'; }
  .keybox { display:none; } body.show .keybox { display:block; }
  .key { display:grid; grid-template-columns:repeat(auto-fill,minmax(64px,1fr)); gap:6px; direction:ltr; }
  .key span { background:var(--card); border:1px solid var(--border2); border-radius:8px; padding:6px 8px; text-align:center; font-weight:800; text-transform:uppercase; color:var(--ok); }
  .key b { color:var(--muted); margin-right:6px; font-weight:600; }
  .nav { flex-wrap:wrap; }
  @media print {
    *, *::before, *::after { animation:none !important; transition:none !important; opacity:1 !important; }
    @page { size:A4; margin:14mm 12mm; }
    html, body, body.show { background:#fff !important; color:#111 !important; min-height:0 !important; height:auto !important; }
    body > *:not(main) { display:none !important; }
    body::before, header, .nav, .fx-band, .fx-home, [class^="fx-"], [class*=" fx-"] { display:none !important; }
    main { padding:0; max-width:none; }
    .section { display:block !important; }
    .paper-head { border-bottom:2px solid #590907; padding-bottom:8px; margin-bottom:12px; }
    .ph-title { color:#590907; } .ph-sub { color:#444; }
    .topic-header { border-color:#ccc; margin-bottom:8px; } .topic-title { color:#590907 !important; } .topic-count { background:none !important; border:1px solid #bbb !important; color:#590907 !important; }
    .topic-icon { background:#590907 !important; color:#fff !important; }
    .xq { background:#fff; border:none; border-bottom:1px solid #ddd; border-radius:0; padding:6px 2px 8px; margin:0; }
    .xq-t { font-size:12.5px; color:#111; } .xq-n { color:#590907; }
    .xq-o { grid-template-columns:1fr 1fr; gap:2px 14px; margin-top:4px; }
    .xq-o li { font-size:11.5px; color:#222; padding:1px 4px; }
    .xl { color:#555; }
    body.show .xq-o li.ans { color:#0b5d1e; background:none; border:none; font-weight:800; text-decoration:underline; }
    .keybox { break-inside:avoid; margin-top:14px; } body.show .keybox { display:block; }
    .key { grid-template-columns:repeat(10,1fr); }
    .key span { background:#fff; color:#0b5d1e; border-color:#bbb; }
    .key b { color:#333; }
  }
"""

TPL = f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Internal Medicine (Cardiology) — {LABEL} Questions</title>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&display=swap" rel="stylesheet">
<style>{BASE_CSS}{EXTRA}</style>
</head>
<body class="show">
<header>
  <div class="header-badge">🫀 Internal Medicine · Cardiology</div>
  <h1>{LABEL} Questions</h1>
  <p class="subtitle">Anatomy &amp; Physiology · Embryology &amp; CHD · CAD · Valvular Heart Diseases · Cardiac Rehabilitation</p>
  <div class="stats-bar">
    <div class="stat"><div class="stat-num">{N}</div><div class="stat-label">MCQs</div></div>
    <div class="stat"><div class="stat-num">5</div><div class="stat-label">Lectures</div></div>
  </div>
</header>
<nav class="nav">
  <a href="../../index.html" class="nav-btn">🔙 الرئيسية</a>
  <button class="nav-btn active" id="btn-{SID}" onclick="showSection('{SID}')">{TAB}</button>
  <a href="{OTHER[0]}" class="nav-btn">{OTHER[1]}</a>
  <button class="nav-btn" id="btn-ans" onclick="toggleAns()">🙈 إخفاء الإجابات</button>
  <button class="nav-btn" onclick="window.print()">🖨️ طباعة / PDF</button>
</nav>
<main>
{body_html}
</main>
<script>
  function showSection(id) {{ document.getElementById(id).classList.add('active'); }}
  function toggleAns() {{
    const on = document.body.classList.toggle('show');
    document.getElementById('btn-ans').textContent = on ? '🙈 إخفاء الإجابات' : '👁️ إظهار الإجابات';
  }}
</script>
</body>
</html>
"""
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'mid-bank.html' if IS_MID else 'final-bank.html')
open(out, 'w', encoding='utf8').write(TPL)
# theme_post: same as tools/theme/post.py (theme.css/js + PT Hub pill)
_T = open(out, encoding='utf8').read()
if 'assets/theme.css' not in _T:
    _T = _T.replace('</head>', '<meta name="theme-color" content="#5c5e54">\n<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">\n<link rel="stylesheet" href="../../assets/theme.css?v=3">\n<script src="../../assets/theme.js?v=3" defer></script>\n</head>', 1)
if 'class="fx-home"' not in _T:
    _T = re.sub(r'(<body[^>]*>)', r'\1\n<div class="fx-band" aria-hidden="true"></div>\n<a class="fx-home" href="../../index.html" aria-label="PT Hub"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>PT Hub</a>', _T, count=1)
open(out, 'w', encoding='utf8').write(_T)
print(MODE, N, '->', out)
