import random, html, sys
sys.path.insert(0, '/home/claude/imm')
from data import LECS

# Doctor's slide questions: keep exact slide order
SLIDE = {
 "Movement of cells in response to a chemical stimulus is called:": (["Addressinazition", "Chemotaxis", "Diapedesis", "Marginalization", "Opsonization"], 1),
 "Opsonins include which one of the following?": (["Perforin", "C5a", "C9", "IFNγ", "C3b"], 4),
 "Which of the following is NOT characteristic of the innate immune response?": (["Acts immediately against infectious agents", "Responses are broad-spectrum (non-specific)", "There is memory or lasting protective immunity", "Such mechanisms are present since birth"], 2),
 "Which of the following is low molecular weight molecules that cannot induce specific immune response by themselves and need to combine with larger molecules to become antigenic?": (["Hapten", "Epitope", "Antigen", "Adjuvant"], 0),
 "Which of the following is non-antigenic substances that when mixed with an immunogen it will enhance the immune response against the immunogen?": (["Hapten", "Epitope", "Antigen", "Adjuvant"], 3),
 "Cold agglutinins is an example of:": (["Super antigen", "Heterophile antigen", "Adjuvant", "Epitope"], 1),
 "Which of the following immunoglobulins can cross placenta?": (["IgG", "IgM", "IgD", "IgE", "IgA"], 0),
 "Which of the following immunoglobulins present in high concentration in mucous secretion?": (["IgG", "IgM", "IgD", "IgE", "IgA"], 4),
 "The Fc portion of IgE usually:": (["Binds to an Fc receptor on mast cell", "Highly variable", "Part of antigen recognition and binding", "Mediates complement fixation"], 0),
}

def esc(s): return html.escape(s, quote=False)

TOTAL = sum(len(qs) for L in LECS for _, qs in L["groups"])
DR = sum(1 for L in LECS for _, qs in L["groups"] for q in qs if q[2] == "dr")
counts = {L["id"]: sum(len(qs) for _, qs in L["groups"]) for L in LECS}

ICONS = ["ic-a", "ic-b", "ic-c"]
dist = [0]*5
TARGETS = [0,1,2,3]*40
random.Random(7).shuffle(TARGETS)
def q_html(n, text, opts, tag):
    if text in SLIDE:
        options, ci = SLIDE[text]
    else:
        ci = TARGETS.pop()
        rnd = random.Random(text)
        wrong = opts[1:]; rnd.shuffle(wrong)
        options = wrong[:ci] + [opts[0]] + wrong[ci:]
    dist[ci] += 1
    badge = ""
    if tag == "dr": badge = '<span class="q-badge dr">★ سؤال الدكتور</span>'
    elif tag == "imp": badge = '<span class="q-badge imp">IMP</span>'
    out = [f'    <div class="q-card{" is-dr" if tag=="dr" else ""}" onclick="toggleQ(this)">',
           f'      <div class="q-header"><div class="q-num">Q{n}</div><div class="q-text">{badge}{esc(text)}</div><div class="q-toggle">▼</div></div>',
           '      <div class="q-body"><div class="options">']
    for k, o in enumerate(options):
        cls = "option correct" if k == ci else "option"
        out.append(f'        <div class="{cls}" onclick="selectOpt(event,this)"><div class="opt-letter">{"ABCDE"[k]}</div>{esc(o)}</div>')
    out.append('      </div></div>\n    </div>')
    return "\n".join(out)

sections = []
for li, L in enumerate(LECS):
    n = 0
    parts = [f'<div class="section{" active" if li==0 else ""}" id="{L["id"]}">',
             '  <div class="search-wrap"><span class="search-icon">🔍</span>',
             f'    <input class="search-input" placeholder="ابحث في أسئلة {esc(L["short"])}..." oninput="searchQ(this.value,\'{L["id"]}\')"></div>',
             f'  <div class="lec-banner"><div class="lec-icon">{L["icon"]}</div><div><div class="lec-title">{esc(L["title"])}</div><div class="lec-sub">{counts[L["id"]]} سؤال · {len(L["groups"])} مواضيع</div></div></div>']
    for gi, (gt, qs) in enumerate(L["groups"]):
        parts.append(f'  <div class="topic-group">\n    <div class="topic-header"><div class="topic-icon">{gi+1:02d}</div><div class="topic-title">{esc(gt)}</div><div class="topic-count">{len(qs)} أسئلة</div></div>')
        for text, opts, tag in qs:
            n += 1
            parts.append(q_html(n, text, opts, tag))
        parts.append('  </div>')
    parts.append('</div>')
    sections.append("\n".join(parts))

REVIEW = open('/home/claude/imm/review.html', encoding='utf8').read()
TPL = open('/home/claude/imm/template.html', encoding='utf8').read()
out = (TPL.replace('{{SECTIONS}}', "\n\n".join(sections))
          .replace('{{REVIEW}}', REVIEW)
          .replace('{{TOTAL}}', str(TOTAL)).replace('{{DR}}', str(DR))
          .replace('{{C1}}', str(counts['lec1'])).replace('{{C2}}', str(counts['lec2'])).replace('{{C3}}', str(counts['lec3'])))
open('/home/claude/imm/immunology_midterm.html', 'w', encoding='utf8').write(out)
print("total", TOTAL, "dr", DR, counts, "answer dist", dist)
