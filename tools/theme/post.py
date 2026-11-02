import re, sys, os
root = sys.argv[1]
PILL = '<a class="fx-home" href="../../index.html" aria-label="PT Hub"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/></svg>PT Hub</a>'
HEAD = '<meta name="theme-color" content="#590907">\n<link rel="icon" href="../../assets/favicon.svg" type="image/svg+xml">\n<link rel="stylesheet" href="../../assets/theme.css">\n'
LINKS = {'../index.html': '../../index.html', '../Midterm/electro1_midterm.html': 'midterm.html',
         'exam_pt10.html': 'final-pt10.html', 'exam_questions.html': 'final.html'}
for dp, _, fs in os.walk(root):
    for f in fs:
        if not f.endswith('.html') or dp == root: continue
        p = os.path.join(dp, f); s = open(p, encoding='utf8').read()
        if 'assets/theme.css' not in s:
            s = re.sub(r'</head>', HEAD + '</head>', s, count=1, flags=re.I) if re.search(r'</head>', s, re.I) else re.sub(r'(<body[^>]*>)', HEAD + r'\1', s, count=1, flags=re.I)
        for a, b in LINKS.items():
            s = s.replace('href="%s"' % a, 'href="%s"' % b)
        if 'fx-home' not in s:
            s = re.sub(r'(<body[^>]*>)', r'\1\n' + PILL, s, count=1, flags=re.I)
        open(p, 'w', encoding='utf8').write(s); print('post', p)
