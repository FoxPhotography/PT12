# Internal Medicine (Cardiology) — the 120 MCQs (20 midterm + 100 final) as ONE interactive page.
# Built with ../common/build_simple.py from data_bank.py
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_bank import MID, FINAL
META = {'title': 'Internal Medicine (Cardiology) — 120 MCQs', 'badge': '🫀 Internal Medicine · Cardiology', 'h1': 'بنك الـ 120 سؤال',
        'subtitle': 'Anatomy & Physiology · Embryology & CHD · CAD · Valvular Heart Diseases · Cardiac Rehabilitation',
        'statnum': 5, 'statlabel': 'محاضرات'}
ICON = ['🫀', '👶', '💔', '🚪', '🏃']
groups = []
for (title, mq), (_, fq) in zip(MID, FINAL):
    groups.append((title, [(q, o, '', '') for q, o in mq + fq]))
NOTE = """<div class="card"><h4>📌 اقرا دي الأول</h4>
<ul><li>دول الـ <b>120 سؤال</b> كلهم في مكان واحد، مترتبين على الـ 5 محاضرات بتاعة الـ cardiology.</li>
<li>الدكتور قال الميد هييجي <b>من الأسئلة دي</b>، فحلهم كلهم لحد ما تجيبهم صح.</li>
<li>دوس على السؤال، اختار إجابة، وهيبان الصح. زرار <b>إظهار الإجابات</b> بيوريك الحل كله مرة واحدة للمراجعة السريعة.</li></ul></div>"""
TABS = [("bank", "بنك الأسئلة — 120 MCQ", "بنك الأسئلة (120)", "🫀", "الـ 5 ملفات الرسمية بتاعة الـ cardiac", NOTE, groups)]
