import re
import os

cns_html_path = r"d:\Coding\PT12\final\cns_questions.html"
muscletest_md_path = r"d:\Coding\PT12\muscletest2.md"
output_html_path = r"d:\Coding\PT12\final\muscletest2.html"

# Step 1: Read cns_questions.html to extract styles and scripts
with open(cns_html_path, 'r', encoding='utf-8') as f:
    cns_content = f.read()

# Extract from start to end of </style>
style_match = re.search(r'(<!DOCTYPE html>.*?</style>)', cns_content, re.DOTALL | re.IGNORECASE)
if not style_match:
    raise ValueError("Could not find style block in cns_questions.html")
head_and_style = style_match.group(1)

# Extract <script>...</script>
script_match = re.search(r'(<script>.*?</script>)', cns_content, re.DOTALL | re.IGNORECASE)
if not script_match:
    raise ValueError("Could not find script block in cns_questions.html")
script_block = script_match.group(1)

# Step 2: Parse muscletest2.md
with open(muscletest_md_path, 'r', encoding='utf-8') as f:
    md_content = f.read()

lines = md_content.split('\n')
sections = []
current_section = None
current_question = None

for line in lines:
    line_str = line.strip()
    if not line_str:
        continue
    
    # Ignore horizontal rules
    if line_str.startswith('---') or line_str == '---':
        continue
        
    # Check if section header
    if (line_str.startswith('# ') or line_str.startswith('## ')) and not line_str.startswith('###'):
        title = line_str.lstrip('#').strip()
        current_section = {
            'title': title,
            'questions': []
        }
        sections.append(current_section)
        current_question = None
        continue
        
    # Check if question header
    if line_str.startswith('###'):
        q_text = line_str.lstrip('#').strip()
        # Clean question number like "1) " or "1. "
        q_match = re.match(r'^(\d+)\s*[\)\.]\s*(.*)$', q_text)
        q_num = None
        if q_match:
            q_num = int(q_match.group(1))
            q_text = q_match.group(2).strip()
        
        current_question = {
            'num': q_num,
            'text': q_text,
            'options': []
        }
        if current_section is None:
            current_section = {'title': 'General', 'questions': []}
            sections.append(current_section)
        current_section['questions'].append(current_question)
        continue
        
    # Check if option
    if line_str.startswith('*') or (line_str.startswith('-') and not line_str.startswith('---')):
        opt_text = line_str[1:].strip()
        is_correct = False
        if '✅' in opt_text:
            is_correct = True
            opt_text = opt_text.replace('✅', '').strip()
        
        if current_question is not None:
            current_question['options'].append({
                'text': opt_text,
                'correct': is_correct
            })

# Remove sections with 0 questions (if any)
sections = [s for s in sections if len(s['questions']) > 0]

# Calculate total questions
total_questions = sum(len(s['questions']) for s in sections)
total_topics = len(sections)

print(f"Parsed {total_questions} questions across {total_topics} sections.")

# Helper for Arabic question count pluralization
def format_q_count(n):
    if 3 <= n <= 10:
        return f"{n} أسئلة"
    else:
        return f"{n} سؤال"

# Section configurations for color and icons
section_configs = [
    {"icon": "🦵", "color": "ic-blue"},      # Hip
    {"icon": "🎭", "color": "ic-green"},     # Face Muscles
    {"icon": "💪", "color": "ic-yellow"},    # MMT
    {"icon": "🧠", "color": "ic-red"},       # Nerves
    {"icon": "🧍", "color": "ic-purple"},    # Neck & Trunk
    {"icon": "🦶", "color": "ic-cyan"},      # Knee + Foot & Ankle
    {"icon": "🔥", "color": "ic-orange"},    # MCQ 61-80
    {"icon": "⚠️", "color": "ic-pink"},      # MCQ 81-100
    {"icon": "🏆", "color": "ic-red"}        # MCQ 101-120
]

# Generate MCQ HTML
mcq_html = []
global_q_index = 1

for idx, sec in enumerate(sections):
    config = section_configs[idx % len(section_configs)]
    sec_title = sec['title']
    sec_q_count = len(sec['questions'])
    
    mcq_html.append(f'  <div class="topic-group" data-topic>')
    mcq_html.append(f'    <div class="topic-header">')
    mcq_html.append(f'      <div class="topic-icon {config["color"]}">{config["icon"]}</div>')
    mcq_html.append(f'      <div class="topic-title">{sec_title}</div>')
    mcq_html.append(f'      <div class="topic-count">{format_q_count(sec_q_count)}</div>')
    mcq_html.append(f'    </div>')
    
    for q in sec['questions']:
        mcq_html.append(f'    <div class="q-card" onclick="toggleQ(this)">')
        mcq_html.append(f'      <div class="q-header">')
        mcq_html.append(f'        <div class="q-num">Q{global_q_index}</div>')
        mcq_html.append(f'        <div class="q-text">{q["text"]}</div>')
        mcq_html.append(f'        <div class="q-toggle">▼</div>')
        mcq_html.append(f'      </div>')
        mcq_html.append(f'      <div class="q-body">')
        mcq_html.append(f'        <div class="options">')
        
        for opt in q['options']:
            opt_class = "correct" if opt['correct'] else "wrong"
            mcq_html.append(f'          <div class="option {opt_class}"><div class="opt-letter"></div>{opt["text"]}</div>')
            
        mcq_html.append(f'        </div>')
        mcq_html.append(f'      </div>')
        mcq_html.append(f'    </div>')
        global_q_index += 1
        
    mcq_html.append(f'  </div>')

# High Yield Facts Summary Table Content (defined explicitly)
high_yield_facts = [
    ("Prime mover of Hip Flexion", "Iliopsoas"),
    ("Nerve supply of Iliacus", "Femoral nerve (L2, L3, L4)"),
    ("Positive Trendelenburg test", "Indicates weakness of Gluteus Medius"),
    ("Positive Ober test", "Indicates TFL / IT Band tightness"),
    ("Positive Ely test", "Indicates Rectus Femoris tightness"),
    ("Thomas test", "Detects Hip Flexor tightness"),
    ("Sartorius action", "Hip Flexion + Abduction + ER (and Knee Flexion + IR)"),
    ("TFL action", "Hip Flexion + Abduction + IR"),
    ("Hip Abduction nerve", "Superior Gluteal nerve"),
    ("Hip Extension nerve", "Inferior Gluteal nerve"),
    ("Frontalis action", "Raise eyebrows / Wrinkle forehead"),
    ("Orbicularis Oculi", "Close eye"),
    ("Levator Palpebrae weakness", "Causes Ptosis (drooping eyelid)"),
    ("Kissing muscle", "Orbicularis Oris"),
    ("Smiling muscle", "Zygomaticus Major"),
    ("Blow cheeks / Puff cheeks", "Buccinator"),
    ("Pouting expression", "Mentalis"),
    ("LR6", "Lateral Rectus CN VI (Abducens)"),
    ("SO4", "Superior Oblique CN IV (Trochlear)"),
    ("AO3", "All others CN III (Oculomotor)"),
    ("Grade 0 MMT", "No contraction"),
    ("Grade 1 MMT", "Contraction only (Trace)"),
    ("Grade 2 MMT", "Full ROM Gravity Eliminated (GE)"),
    ("Grade 3 MMT", "Full ROM Against Gravity (AG)"),
    ("Grade 4 MMT", "Full ROM AG + Moderate Resistance"),
    ("Grade 5 MMT", "Full ROM AG + Max resistance"),
    ("Concentric contraction", "Muscle shortens"),
    ("Eccentric contraction", "Muscle lengthens while contracting"),
    ("Isometric contraction", "No movement / No change in length"),
    ("Prime mover", "Main muscle producing movement"),
    ("Synergist", "Helper / Assisting muscle"),
    ("Antagonist", "Opposite action muscle"),
    ("Neutralizer", "Prevents unwanted movement"),
    ("Stabilizer", "Provides stable base"),
    ("Femoral nerve roots", "L2-3-4"),
    ("Obturator action", "Hip Adduction"),
    ("Superior Gluteal roots", "L4-5-S1"),
    ("Inferior Gluteal roots", "L5-S1-S2"),
    ("Largest nerve", "Sciatic nerve"),
    ("Foot Drop", "Common Peroneal (Fibular) nerve injury"),
    ("Tibial nerve action", "Plantar Flexion"),
    ("Meralgia Paresthetica", "Lateral Femoral Cutaneous nerve compression"),
    ("Cannot stand on toes", "Tibial nerve injury"),
    ("Cervical Flexion", "SCM (Sternocleidomastoid)"),
    ("Right SCM rotates head to", "Left side"),
    ("Weak SCM substitution", "Platysma"),
    ("Trunk Flexion", "Rectus Abdominis"),
    ("Trunk Extension", "Erector Spinae"),
    ("Rotate trunk right", "Left External Oblique + Right Internal Oblique"),
    ("Rotate trunk left", "Right External Oblique + Left Internal Oblique"),
    ("Umbilicus deviation", "Deviates toward the strong/stronger side"),
    ("Grade 5 trunk flexion", "Hands behind head"),
    ("Cervical Extension", "Look up"),
    ("Grade 3 Cervical Extension", "Prone with head off table"),
    ("Knee Extension prime mover", "Quadriceps"),
    ("Knee Flexion nerve", "Sciatic nerve"),
    ("Biceps Femoris rotation", "Lateral rotation of knee (flexed)"),
    ("Semitendinosus rotation", "Medial rotation of knee (flexed)"),
    ("Tibialis Anterior", "Dorsiflexion (DF) + Inversion"),
    ("Tibialis Posterior", "Plantar Flexion (PF) + Inversion"),
    ("Gastrocnemius / Soleus", "Plantar Flexion"),
    ("Peroneus Longus", "Plantar Flexion (PF) + Eversion"),
    ("Great Toe Flexion", "Flexor Hallucis Brevis"),
    ("Great Toe Extension", "EHL (Extensor Hallucis Longus)"),
    ("Toe extensors nerve", "Deep Peroneal nerve"),
    ("Toe flexors nerve", "Tibial nerve"),
    ("Hip Abduction Normal ROM", "45°"),
    ("Hip Internal Rotation ROM", "45°"),
    ("Hip Flexion Normal ROM", "120°"),
    ("Knee Flexion Normal ROM", "135°"),
    ("Ankle Dorsiflexion Normal ROM", "20°"),
    ("Ankle Eversion Normal ROM", "15°"),
    ("FABER meaning", "Flexion Abduction External Rotation"),
    ("Piriformis group", "Hip External Rotators"),
    ("Tibial nerve sensory area", "Sole of foot"),
    ("Common Peroneal sensory", "Dorsum of foot"),
    ("Risorius expression", "Grimace"),
    ("Buccinator test", "Puff / Blow cheeks"),
    ("Break Test", "Patient holds position against resistance"),
    ("Active Resistance Test", "Patient moves against resistance"),
    ("Outer Range", "Full stretch → Mid ROM"),
    ("Inner Range", "Mid → Full shortening"),
    ("Empty End Feel", "Pain limits movement (no physical end feel)"),
    ("Springy End Feel", "Meniscus lesion"),
    ("Firm End Feel", "Capsule / Ligament stretch / tightness"),
    ("Soft Approximation", "Soft tissue contact (e.g. knee flexion)"),
    ("Bony End Feel", "Bone to bone contact (e.g. elbow extension)"),
    ("Soft Tissue Stretch", "Muscle/Ligament stretch")
]

summary_html = []
summary_html.append('<div class="topic-group">')
summary_html.append('  <div class="topic-header">')
summary_html.append('    <div class="topic-icon ic-cyan">⚡</div>')
summary_html.append('    <div class="topic-title">ملخص سريع — أهم النقاط</div>')
summary_html.append('  </div>')
summary_html.append('  <div class="summary-grid">')

for key, val in high_yield_facts:
    summary_html.append('    <div class="sum-row">')
    summary_html.append(f'      <div class="sum-key">{key}</div>')
    summary_html.append(f'      <div class="sum-val">{val}</div>')
    summary_html.append('    </div>')

summary_html.append('  </div>')
summary_html.append('</div>')

# Title adjustment in head
head_and_style = re.sub(r'<title>.*?</title>', '<title>أسئلة الامتحان — Muscle Test 2</title>', head_and_style, flags=re.IGNORECASE)

# Construct final HTML
final_html = []
final_html.append(head_and_style)
final_html.append('<body>')
final_html.append('<header>')
final_html.append('  <div class="header-badge">Muscle Test 2 Exam</div>')
final_html.append('  <h1>أسئلة الامتحان المجمّعة</h1>')
final_html.append('  <p class="subtitle">Hip · Face Muscles · MMT · Nerves · Neck & Trunk · Knee + Foot & Ankle · MCQs</p>')
final_html.append('  <div class="stats-bar">')
final_html.append('    <div class="stat">')
final_html.append(f'      <div class="stat-num">{total_questions}</div>')
final_html.append('      <div class="stat-label">سؤال MCQ</div>')
final_html.append('    </div>')
final_html.append('    <div class="stat">')
final_html.append(f'      <div class="stat-num">{total_topics}</div>')
final_html.append('      <div class="stat-label">موضوع</div>')
final_html.append('    </div>')
final_html.append('    <div class="stat" id="score-stat">')
final_html.append(f'      <div class="stat-num">0/{total_questions}</div>')
final_html.append('      <div class="stat-label">الإجابات الصحيحة</div>')
final_html.append('    </div>')
final_html.append('  </div>')
final_html.append('</header>')

final_html.append('<nav class="nav">')
final_html.append('  <button class="nav-btn active" onclick="showSection(\'mcq\')">📋 MCQ</button>')
final_html.append('  <button class="nav-btn" onclick="showSection(\'summary\')">⚡ ملخص سريع</button>')
final_html.append('  <button class="nav-btn" onclick="showAllAnswers()">👁️ إظهار كل الإجابات</button>')
final_html.append('  <button class="nav-btn" onclick="retest()">🔄 إعادة الاختبار</button>')
final_html.append('</nav>')

final_html.append('<main>')
final_html.append('  <div class="section active" id="mcq">')
final_html.append('    <div class="search-wrap">')
final_html.append('      <span class="search-icon">🔍</span>')
final_html.append('      <input class="search-input" placeholder="... ابحث عن سؤال" oninput="searchQ(this.value)">')
final_html.append('    </div>')
final_html.append('\n'.join(mcq_html))
final_html.append('  </div>')

final_html.append('  <div class="section" id="summary">')
final_html.append('\n'.join(summary_html))
final_html.append('  </div>')
final_html.append('</main>')

final_html.append(script_block)
final_html.append('</body>')
final_html.append('</html>')

# Write to file
with open(output_html_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(final_html))

print("Successfully generated muscletest2.html in final folder!")
