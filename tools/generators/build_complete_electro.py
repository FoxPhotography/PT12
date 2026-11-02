# -*- coding: utf-8 -*-
import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

# Import data modules
from data_mcq import mcq_topics
from data_shortnotes import short_notes_list
from data_summaries import summary_tables, flashcards_list

output_path = r"d:\Coding\PT12\Midterm\electro1_midterm.html"

# Count statistics
total_mcq = sum(len(topic["questions"]) for topic in mcq_topics)
total_topics = len(mcq_topics)
total_sn = len(short_notes_list)
total_tables = len(summary_tables)
total_flashcards = len(flashcards_list)

print(f"Building Electrotherapy 1 Midterm Hub (MacBook & Cross-Platform Particle Fix):")
print(f" - {total_mcq} MCQs across {total_topics} topics")
print(f" - {total_sn} Short Notes & Clinical Cases")
print(f" - High-DPI Retina Canvas + Dual-layer DOM Confetti")

# Format Arabic question count
def format_q_count(n):
    if 3 <= n <= 10:
        return f"{n} أسئلة"
    else:
        return f"{n} سؤال"

# Build MCQ HTML
mcq_html_parts = []
global_q_index = 1
mock_mcq_data = []

for topic_idx, topic in enumerate(mcq_topics):
    topic_title = topic["title"]
    topic_icon = topic["icon"]
    topic_color = topic["color"]
    q_count = len(topic["questions"])
    
    mcq_html_parts.append(f'''
    <div class="topic-group" data-topic>
      <div class="topic-header">
        <div class="topic-icon {topic_color}">{topic_icon}</div>
        <div class="topic-title">{topic_title}</div>
        <div class="topic-count">{format_q_count(q_count)}</div>
      </div>
    ''')
    
    for q in topic["questions"]:
        q_num = global_q_index
        q_text = q["q"]
        options = q["options"]
        correct_idx = q["correct"]
        note = q.get("note", "")
        
        # Save for mock exam
        mock_mcq_data.append({
            "num": q_num,
            "topic": topic_title,
            "q": q_text,
            "options": options,
            "correct": correct_idx,
            "note": note
        })
        
        opts_html = []
        for opt_i, opt_text in enumerate(options):
            is_corr = (opt_i == correct_idx)
            opt_cls = "correct" if is_corr else "wrong"
            opts_html.append(f'          <div class="option {opt_cls}"><div class="opt-letter"></div><div class="opt-content">{opt_text}</div></div>')
            
        note_html = f'<div class="note-box">{note}</div>' if note else ''
        
        mcq_html_parts.append(f'''
      <div class="q-card" onclick="toggleQ(this)" data-q-id="{q_num}">
        <div class="q-header">
          <div class="q-num">Q{q_num}</div>
          <div class="q-text">{q_text}</div>
          <div class="q-toggle">▼</div>
        </div>
        <div class="q-body">
          <div class="options">
{chr(10).join(opts_html)}
          </div>
          {note_html}
        </div>
      </div>
        ''')
        global_q_index += 1
        
    mcq_html_parts.append('    </div>')

mcq_full_html = "\n".join(mcq_html_parts)

# Build Short Notes HTML
sn_html_parts = []
mock_sn_data = []

for idx, sn in enumerate(short_notes_list):
    sn_id = sn["id"]
    sn_topic = sn["topic"]
    sn_title = sn["title"]
    sn_icon = sn["icon"]
    sn_badge = sn["badge"]
    sn_answer = sn["answer_html"]
    
    mock_sn_data.append({
        "id": sn_id,
        "topic": sn_topic,
        "title": sn_title,
        "icon": sn_icon,
        "badge": sn_badge,
        "answer_html": sn_answer
    })
    
    sn_html_parts.append(f'''
    <div class="sn-card" onclick="toggleCard(this)" data-sn-id="{sn_id}">
      <div class="sn-header">
        <div class="sn-badge-tag">{sn_badge}</div>
        <div class="sn-header-main">
          <span class="sn-icon">{sn_icon}</span>
          <div class="sn-title">{sn_title}</div>
        </div>
        <div class="sn-toggle">▼ إظهار الإجابة النموذجية</div>
      </div>
      <div class="sn-body">
        <div class="sn-topic-ref">📌 المحاضرة: {sn_topic}</div>
        {sn_answer}
      </div>
    </div>
    ''')

sn_full_html = "\n".join(sn_html_parts)

# Build Summaries HTML
sum_html_parts = []
for idx, tbl in enumerate(summary_tables):
    sum_html_parts.append(f'''
    <div class="summary-card">
      <div class="summary-title"><span class="sum-icon">{tbl["icon"]}</span> {tbl["title"]}</div>
      <div class="summary-table-wrap">
        {tbl["html"]}
      </div>
    </div>
    ''')
sum_full_html = "\n".join(sum_html_parts)

# Build Flashcards HTML
fc_html_parts = []
for idx, fc in enumerate(flashcards_list):
    fc_html_parts.append(f'''
    <div class="fc-card" onclick="flipCard(this)">
      <div class="fc-inner">
        <div class="fc-front">
          <div class="fc-badge">سؤال فلاش كارد #{idx+1}</div>
          <div class="fc-q">{fc["q"]}</div>
          <div class="fc-hint">👆 اضغط لرؤية الإجابة</div>
        </div>
        <div class="fc-back">
          <div class="fc-badge ans">الإجابة النموذجية</div>
          <div class="fc-a">{fc["a"]}</div>
          <div class="fc-hint">👆 اضغط للعودة للسؤال</div>
        </div>
      </div>
    </div>
    ''')
fc_full_html = "\n".join(fc_html_parts)

# Build Mock Exam Initial Template (populated via JS)
mock_json_mcq = json.dumps(mock_mcq_data, ensure_ascii=False)
mock_json_sn = json.dumps(mock_sn_data, ensure_ascii=False)

# Full HTML template
html_template = f'''<!DOCTYPE html>
<html lang="ar" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>أسئلة الميدتيرم — Electrotherapy 1</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;600;700;900&family=JetBrains+Mono:wght@400;600;700;800&family=Outfit:wght@400;600;700&display=swap" rel="stylesheet">
<style>
  :root {{
    --bg: #0a0c10;
    --bg2: #0f1218;
    --bg3: #141820;
    --card: #13171f;
    --card2: #1a1f2a;
    --border: #1e2535;
    --border2: #2a3248;
    --text: #e2e8f0;
    --muted: #8892a4;
    --dim: #4a5568;
    --blue: #3b82f6;
    --blue2: #1d4ed8;
    --cyan: #06b6d4;
    --green: #10b981;
    --yellow: #f59e0b;
    --red: #ef4444;
    --purple: #8b5cf6;
    --pink: #ec4899;
    --orange: #f97316;
    --glow-blue: 0 0 20px rgba(59, 130, 246, 0.25);
    --glow-cyan: 0 0 20px rgba(6, 182, 212, 0.2);
    --glow-green: 0 0 20px rgba(16, 185, 129, 0.2);
    --glow-yellow: 0 0 20px rgba(245, 158, 11, 0.2);
  }}

  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  
  html {{
    scroll-behavior: smooth;
    overflow-y: auto;
    overflow-x: hidden;
  }}

  body {{
    font-family: 'Cairo', sans-serif;
    background: var(--bg);
    color: var(--text);
    min-height: 100vh;
    overflow-x: hidden;
    overflow-y: auto;
    -webkit-font-smoothing: antialiased;
  }}

  /* Grid background */
  body::before {{
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(59, 130, 246, 0.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(59, 130, 246, 0.04) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }}

  /* Ambient glow */
  body::after {{
    content: '';
    position: fixed;
    top: -200px;
    left: 50%;
    transform: translateX(-50%);
    width: 900px;
    height: 500px;
    background: radial-gradient(ellipse, rgba(59, 130, 246, 0.1) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }}

  /* Canvas Particles - WebKit GPU & Retina Ready */
  #particles-canvas {{
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 999999;
    transform: translate3d(0, 0, 0);
    -webkit-transform: translate3d(0, 0, 0);
    will-change: transform;
  }}

  /* DOM Confetti Particle Fallback Style */
  .dom-confetti-particle {{
    position: fixed;
    pointer-events: none;
    z-index: 999999;
    will-change: transform, opacity;
    -webkit-transform-style: preserve-3d;
  }}

  /* HEADER */
  header {{
    position: relative;
    z-index: 10;
    padding: 45px 20px 35px;
    text-align: center;
    border-bottom: 1px solid var(--border);
    background: linear-gradient(180deg, rgba(59, 130, 246, 0.08) 0%, transparent 100%);
  }}

  .header-badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(59, 130, 246, 0.12);
    border: 1px solid rgba(59, 130, 246, 0.35);
    color: var(--blue);
    padding: 6px 18px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 16px;
    animation: fadeDown 0.6s ease both;
  }}

  .header-badge::before {{
    content: '';
    width: 7px;
    height: 7px;
    background: var(--blue);
    border-radius: 50%;
    animation: pulse 2s infinite;
  }}

  @keyframes pulse {{
    0%, 100% {{ opacity: 1; transform: scale(1); }}
    50% {{ opacity: 0.4; transform: scale(0.8); }}
  }}

  h1 {{
    font-size: clamp(26px, 5vw, 44px);
    font-weight: 900;
    letter-spacing: -1px;
    line-height: 1.2;
    background: linear-gradient(135deg, #fff 0%, rgba(255, 255, 255, 0.65) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    animation: fadeDown 0.6s 0.1s ease both;
  }}

  .subtitle {{
    color: var(--muted);
    margin-top: 8px;
    font-size: 14px;
    direction: ltr;
    font-family: 'Outfit', sans-serif;
    letter-spacing: 0.5px;
    animation: fadeDown 0.6s 0.2s ease both;
  }}

  .stats-bar {{
    display: flex;
    justify-content: center;
    gap: 32px;
    margin-top: 25px;
    flex-wrap: wrap;
    animation: fadeDown 0.6s 0.3s ease both;
  }}

  .stat {{ text-align: center; }}
  .stat-num {{
    font-size: 26px;
    font-weight: 900;
    color: var(--blue);
    font-family: 'JetBrains Mono', monospace;
  }}
  .stat-label {{
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-top: 2px;
  }}

  /* NAVIGATION */
  .nav {{
    position: sticky;
    top: 0;
    z-index: 100;
    background: rgba(10, 12, 16, 0.95);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border);
    padding: 0 16px;
    display: flex;
    gap: 4px;
    justify-content: center;
    overflow-x: auto;
    scrollbar-width: none;
  }}
  .nav::-webkit-scrollbar {{ display: none; }}

  .nav-btn {{
    background: none;
    border: none;
    color: var(--muted);
    font-family: 'Cairo', sans-serif;
    font-size: 13px;
    font-weight: 600;
    padding: 13px 16px;
    cursor: pointer;
    white-space: nowrap;
    border-bottom: 2px solid transparent;
    transition: all 0.2s;
    text-decoration: none;
    display: flex;
    align-items: center;
    gap: 6px;
  }}
  .nav-btn:hover {{ color: var(--text); }}
  .nav-btn.active {{
    color: var(--blue);
    border-bottom-color: var(--blue);
  }}

  /* MAIN LAYOUT */
  main {{
    position: relative;
    z-index: 1;
    max-width: 1100px;
    margin: 0 auto;
    padding: 35px 20px 80px;
  }}

  .section {{
    display: none;
    animation: fadeIn 0.4s ease;
  }}
  .section.active {{ display: block; }}

  @keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}
  @keyframes fadeDown {{
    from {{ opacity: 0; transform: translateY(-15px); }}
    to {{ opacity: 1; transform: translateY(0); }}
  }}

  /* SEARCH */
  .search-wrap {{
    margin-bottom: 25px;
    position: relative;
  }}
  .search-input {{
    width: 100%;
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 10px;
    color: var(--text);
    font-family: 'Cairo', sans-serif;
    font-size: 14px;
    padding: 13px 20px 13px 48px;
    outline: none;
    transition: border-color 0.2s, box-shadow 0.2s;
  }}
  .search-input::placeholder {{ color: var(--dim); }}
  .search-input:focus {{
    border-color: rgba(59, 130, 246, 0.4);
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.08);
  }}
  .search-icon {{
    position: absolute;
    left: 16px;
    top: 50%;
    transform: translateY(-50%);
    color: var(--dim);
    font-size: 16px;
    pointer-events: none;
  }}

  /* TOPIC GROUPS & MCQ CARDS */
  .topic-group {{ margin-bottom: 35px; }}
  .topic-header {{
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
  }}
  .topic-icon {{
    width: 38px;
    height: 38px;
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    flex-shrink: 0;
  }}
  .ic-blue {{ background: rgba(59, 130, 246, 0.15); color: var(--blue); }}
  .ic-red {{ background: rgba(239, 68, 68, 0.15); color: var(--red); }}
  .ic-purple {{ background: rgba(139, 92, 246, 0.15); color: var(--purple); }}
  .ic-cyan {{ background: rgba(6, 182, 212, 0.15); color: var(--cyan); }}
  .ic-yellow {{ background: rgba(245, 158, 11, 0.15); color: var(--yellow); }}
  .ic-pink {{ background: rgba(236, 72, 153, 0.15); color: var(--pink); }}
  .ic-green {{ background: rgba(16, 185, 129, 0.15); color: var(--green); }}

  .topic-title {{
    font-size: 17px;
    font-weight: 700;
    color: var(--text);
    flex: 1;
  }}
  .topic-count {{
    margin-right: auto;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid var(--border);
    color: var(--muted);
    font-size: 11px;
    font-family: 'JetBrains Mono', monospace;
    padding: 3px 10px;
    border-radius: 100px;
  }}

  /* QUESTION CARD */
  .q-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 12px;
    overflow: hidden;
    transition: border-color 0.2s, box-shadow 0.2s;
  }}
  .q-card:hover {{
    border-color: var(--border2);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.3);
  }}
  .q-header {{
    display: flex;
    align-items: flex-start;
    gap: 14px;
    padding: 16px 20px;
    cursor: pointer;
  }}
  .q-num {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 4px 10px;
    flex-shrink: 0;
    margin-top: 1px;
  }}
  .q-text {{
    font-size: 14.5px;
    font-weight: 600;
    line-height: 1.6;
    flex: 1;
  }}
  .q-toggle {{
    width: 24px;
    height: 24px;
    border-radius: 6px;
    background: var(--bg3);
    border: 1px solid var(--border);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    color: var(--muted);
    font-size: 12px;
    transition: all 0.2s;
    margin-top: 1px;
  }}
  .q-card.open .q-toggle {{
    background: rgba(59, 130, 246, 0.1);
    border-color: rgba(59, 130, 246, 0.3);
    color: var(--blue);
    transform: rotate(180deg);
  }}
  .q-body {{
    display: none;
    padding: 0 20px 18px 20px;
    border-top: 1px solid var(--border);
  }}
  .q-card.open .q-body {{ display: block; }}

  /* OPTIONS */
  .options {{
    display: flex;
    flex-direction: column;
    gap: 8px;
    margin-top: 14px;
  }}
  .option {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 14px;
    border-radius: 8px;
    border: 1px solid var(--border);
    background: var(--bg2);
    font-size: 13.5px;
    line-height: 1.5;
    transition: all 0.2s;
    cursor: pointer;
  }}
  .option:hover {{
    border-color: var(--border2);
    background: var(--card2);
  }}
  .opt-content {{ flex: 1; }}

  .q-card.answered .option, .show-all-mode .option {{
    pointer-events: none;
  }}
  .q-card.answered .option.correct, .show-all-mode .option.correct {{
    border-color: rgba(16, 185, 129, 0.45);
    background: rgba(16, 185, 129, 0.08);
    color: #6ee7b7;
    opacity: 1;
  }}
  .q-card.answered .option:not(.correct):not(.wrong-selected), .show-all-mode .option:not(.correct) {{
    opacity: 0.45;
  }}

  .opt-letter {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    font-weight: 700;
    width: 22px;
    height: 22px;
    border-radius: 5px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    background: var(--bg3);
    border: 1px solid var(--border);
    color: var(--muted);
    transition: all 0.2s;
  }}
  .q-card.answered .option.correct .opt-letter, .show-all-mode .option.correct .opt-letter {{
    background: rgba(16, 185, 129, 0.2);
    border-color: rgba(16, 185, 129, 0.5);
    color: var(--green);
  }}
  .q-card.answered .option.correct .opt-letter::after, .show-all-mode .option.correct .opt-letter::after {{
    content: '✓';
  }}

  .option.wrong-selected {{
    border-color: rgba(239, 68, 68, 0.45);
    background: rgba(239, 68, 68, 0.08);
    color: #fca5a5;
    opacity: 1 !important;
  }}
  .option.wrong-selected .opt-letter {{
    background: rgba(239, 68, 68, 0.2);
    border-color: rgba(239, 68, 68, 0.5);
    color: var(--red);
  }}
  .option.wrong-selected .opt-letter::after {{
    content: '✗';
  }}

  @keyframes popCorrect {{
    0% {{ transform: scale(1); }}
    50% {{ transform: scale(1.02); background: rgba(16, 185, 129, 0.15); }}
    100% {{ transform: scale(1); }}
  }}
  .pop-animation {{ animation: popCorrect 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275); }}

  /* NOTE BOX - HIDDEN BY DEFAULT, SHOWN ONLY AFTER ANSWERING */
  .note-box {{
    display: none;
    margin-top: 12px;
    background: rgba(245, 158, 11, 0.08);
    border: 1px solid rgba(245, 158, 11, 0.3);
    border-right: 4px solid var(--yellow);
    border-radius: 8px;
    padding: 12px 16px;
    font-size: 13px;
    color: #fcd34d;
    line-height: 1.65;
    direction: rtl;
    text-align: right;
    animation: fadeIn 0.35s ease;
  }}
  .q-card.answered .note-box,
  .show-all-mode .note-box,
  .q-card.graded .note-box {{
    display: block !important;
  }}

  /* SHORT NOTES SECTION */
  .sn-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    margin-bottom: 18px;
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
  }}
  .sn-card:hover {{
    border-color: var(--border2);
    box-shadow: 0 6px 28px rgba(0, 0, 0, 0.35);
  }}
  .sn-header {{
    padding: 18px 22px;
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.05) 0%, rgba(139, 92, 246, 0.03) 100%);
    border-bottom: 1px solid transparent;
    transition: border-color 0.2s;
  }}
  .sn-card.open .sn-header {{
    border-bottom-color: var(--border);
  }}
  .sn-badge-tag {{
    display: inline-block;
    background: rgba(59, 130, 246, 0.12);
    border: 1px solid rgba(59, 130, 246, 0.3);
    color: var(--blue);
    font-size: 11px;
    font-weight: 700;
    padding: 2px 10px;
    border-radius: 100px;
    margin-bottom: 8px;
    text-transform: uppercase;
  }}
  .sn-header-main {{
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }}
  .sn-icon {{ font-size: 20px; }}
  .sn-title {{
    font-size: 15.5px;
    font-weight: 700;
    line-height: 1.5;
    color: #fff;
    flex: 1;
  }}
  .sn-toggle {{
    margin-top: 10px;
    font-size: 12px;
    color: var(--muted);
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }}
  .sn-card.open .sn-toggle {{
    color: var(--cyan);
  }}
  .sn-body {{
    display: none;
    padding: 20px 24px;
    background: var(--bg2);
    line-height: 1.7;
    font-size: 14px;
  }}
  .sn-card.open .sn-body {{ display: block; }}
  .sn-topic-ref {{
    font-size: 12px;
    color: var(--dim);
    margin-bottom: 14px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border);
    direction: rtl;
    text-align: right;
  }}
  .sn-section {{ margin-bottom: 16px; }}
  .sn-subtitle {{
    font-size: 14px;
    font-weight: 700;
    color: var(--cyan);
    margin-bottom: 6px;
  }}
  .sn-list {{
    margin-left: 20px;
    margin-top: 6px;
  }}
  .sn-list li {{ margin-bottom: 6px; }}

  /* COMPARISON TABLES */
  .summary-card {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 14px;
    margin-bottom: 24px;
    overflow: hidden;
    padding: 20px;
  }}
  .summary-title {{
    font-size: 17px;
    font-weight: 800;
    color: var(--text);
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
  }}
  .summary-table-wrap {{
    overflow-x: auto;
  }}
  .compare-table {{
    width: 100%;
    border-collapse: collapse;
    font-size: 13.5px;
    line-height: 1.5;
  }}
  .compare-table th, .compare-table td {{
    padding: 12px 14px;
    border: 1px solid var(--border);
    text-align: left;
  }}
  .compare-table th {{
    background: var(--bg3);
    color: var(--cyan);
    font-weight: 700;
    font-family: 'Outfit', sans-serif;
  }}
  .compare-table tr:hover td {{
    background: rgba(255, 255, 255, 0.02);
  }}

  /* FLASHCARDS */
  .fc-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 18px;
  }}
  .fc-card {{
    background: transparent;
    perspective: 1000px;
    height: 190px;
    cursor: pointer;
  }}
  .fc-inner {{
    position: relative;
    width: 100%;
    height: 100%;
    text-align: center;
    transition: transform 0.6s cubic-bezier(0.4, 0, 0.2, 1);
    transform-style: preserve-3d;
    border-radius: 14px;
    border: 1px solid var(--border);
    background: var(--card);
  }}
  .fc-card.flipped .fc-inner {{
    transform: rotateY(180deg);
    border-color: var(--cyan);
    box-shadow: 0 0 20px rgba(6, 182, 212, 0.15);
  }}
  .fc-front, .fc-back {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 18px;
    border-radius: 14px;
  }}
  .fc-back {{
    transform: rotateY(180deg);
    background: linear-gradient(135deg, rgba(6, 182, 212, 0.08), rgba(59, 130, 246, 0.05));
  }}
  .fc-badge {{
    font-size: 11px;
    font-weight: 700;
    color: var(--blue);
    text-transform: uppercase;
    letter-spacing: 1px;
  }}
  .fc-badge.ans {{ color: var(--cyan); }}
  .fc-q {{
    font-size: 14.5px;
    font-weight: 700;
    color: #fff;
    line-height: 1.5;
  }}
  .fc-a {{
    font-size: 13.5px;
    font-weight: 600;
    color: #93c5fd;
    line-height: 1.5;
  }}
  .fc-hint {{
    font-size: 11px;
    color: var(--dim);
  }}

  /* MOCK EXAM SECTION */
  .mock-panel {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 24px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }}
  .mock-badge {{
    display: inline-block;
    background: rgba(245, 158, 11, 0.12);
    border: 1px solid rgba(245, 158, 11, 0.35);
    color: var(--yellow);
    padding: 4px 14px;
    border-radius: 100px;
    font-size: 12px;
    font-weight: 700;
    margin-bottom: 12px;
  }}
  .mock-title {{
    font-size: 22px;
    font-weight: 800;
    color: #fff;
    margin-bottom: 8px;
  }}
  .mock-desc {{
    font-size: 13.5px;
    color: var(--muted);
    max-width: 600px;
    margin: 0 auto 20px;
    line-height: 1.6;
  }}
  .mock-controls {{
    display: flex;
    justify-content: center;
    gap: 16px;
    flex-wrap: wrap;
    align-items: center;
  }}
  .btn-start-exam {{
    background: linear-gradient(135deg, var(--blue), var(--blue2));
    color: #fff;
    border: none;
    padding: 12px 28px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
    font-family: 'Cairo', sans-serif;
    cursor: pointer;
    box-shadow: 0 4px 18px rgba(59, 130, 246, 0.35);
    transition: all 0.2s;
  }}
  .btn-start-exam:hover {{
    transform: translateY(-2px);
    box-shadow: 0 6px 24px rgba(59, 130, 246, 0.5);
  }}
  .btn-submit-exam {{
    background: linear-gradient(135deg, var(--green), #059669);
    color: #fff;
    border: none;
    padding: 12px 28px;
    border-radius: 10px;
    font-size: 14px;
    font-weight: 700;
    font-family: 'Cairo', sans-serif;
    cursor: pointer;
    display: none;
    box-shadow: 0 4px 18px rgba(16, 185, 129, 0.35);
    transition: all 0.2s;
  }}
  .mock-timer {{
    font-family: 'JetBrains Mono', monospace;
    font-size: 20px;
    font-weight: 900;
    color: var(--yellow);
    background: var(--bg3);
    border: 1px solid var(--border);
    padding: 8px 18px;
    border-radius: 8px;
    display: none;
  }}
  .mock-score-report {{
    display: none;
    margin-top: 20px;
    padding: 18px;
    background: rgba(16, 185, 129, 0.1);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 12px;
  }}
  .mock-score-num {{
    font-size: 32px;
    font-weight: 900;
    font-family: 'JetBrains Mono', monospace;
    color: var(--green);
  }}

  /* RESPONSIVE */
  @media (max-width: 640px) {{
    .stats-bar {{ gap: 20px; }}
    .nav-btn {{ padding: 10px 10px; font-size: 12px; }}
    .q-header {{ padding: 14px 16px; }}
    .sn-header {{ padding: 14px 16px; }}
    .compare-table {{ font-size: 12px; }}
  }}

  ::-webkit-scrollbar {{ width: 5px; height: 5px; }}
  ::-webkit-scrollbar-track {{ background: var(--bg); }}
  ::-webkit-scrollbar-thumb {{ background: var(--border2); border-radius: 10px; }}
</style>
</head>
<body>

<canvas id="particles-canvas"></canvas>

<header>
  <div class="header-badge">Midterm Exam Hub 2026</div>
  <h1>Electrotherapy 1 Midterm</h1>
  <p class="subtitle">Radiation Physics · IRR · UVR · Ultrasound · Shortwave · Pain Physiology · Bio-electricity</p>
  <div class="stats-bar">
    <div class="stat">
      <div class="stat-num">{total_mcq}</div>
      <div class="stat-label">سؤال MCQ</div>
    </div>
    <div class="stat">
      <div class="stat-num">{total_sn}</div>
      <div class="stat-label">Short Notes & Cases</div>
    </div>
    <div class="stat">
      <div class="stat-num">{total_tables}</div>
      <div class="stat-label">جداول مقارنة</div>
    </div>
    <div class="stat" id="score-stat">
      <div class="stat-num">0/{total_mcq}</div>
      <div class="stat-label">النتيجة الحالية</div>
    </div>
  </div>
</header>

<nav class="nav">
  <a href="../index.html" class="nav-btn">🔙 الرئيسية</a>
  <button class="nav-btn active" onclick="showSection('mcq-section')">📋 بنك الـ MCQ</button>
  <button class="nav-btn" onclick="showSection('shortnotes-section')">✍️ Short Notes & Cases</button>
  <button class="nav-btn" onclick="showSection('summary-section')">📊 جداول المقارنة</button>
  <button class="nav-btn" onclick="showSection('flashcards-section')">🗂️ فلاش كاردز</button>
  <button class="nav-btn" onclick="showSection('mock-section')">⏱️ محاكاة الامتحان</button>
  <button class="nav-btn" onclick="showAllAnswers()">👁️ إظهار الإجابات</button>
  <button class="nav-btn" onclick="retest()">🔄 إعادة الاختبار</button>
</nav>

<main>

  <!-- SECTION 1: MCQ BANK -->
  <div class="section active" id="mcq-section">
    <div class="search-wrap">
      <span class="search-icon">🔍</span>
      <input class="search-input" placeholder="ابحث في جميع أسئلة الـ MCQ والملاحظات..." oninput="searchQ(this.value)">
    </div>
{mcq_full_html}
  </div>

  <!-- SECTION 2: SHORT NOTES & CASES -->
  <div class="section" id="shortnotes-section">
    <div class="search-wrap">
      <span class="search-icon">🔍</span>
      <input class="search-input" placeholder="ابحث في الأسئلة المقالية ونماذج الحالات..." oninput="searchSN(this.value)">
    </div>
{sn_full_html}
  </div>

  <!-- SECTION 3: SUMMARY TABLES -->
  <div class="section" id="summary-section">
{sum_full_html}
  </div>

  <!-- SECTION 4: FLASHCARDS -->
  <div class="section" id="flashcards-section">
    <div class="fc-grid">
{fc_full_html}
    </div>
  </div>

  <!-- SECTION 5: MOCK MIDTERM EXAM -->
  <div class="section" id="mock-section">
    <div class="mock-panel">
      <div class="mock-badge">Real Midterm Simulator</div>
      <div class="mock-title">محاكاة امتحان الميدتيرم الحقيقي (20 MCQ + 5 Short Notes)</div>
      <div class="mock-desc">
        سيتم اختيار <strong>20 سؤال اختياري</strong> و <strong>5 أسئلة مقالية</strong> عشوائياً من بنك الأسئلة الشامل، مع مؤقت زمني مدته 30 دقيقة لاختبار جاهزيتك التامة للامتحان!
      </div>
      <div class="mock-controls">
        <button class="btn-start-exam" id="btn-start-mock" onclick="startMockExam()">🚀 ابدأ الامتحان التجريبي الآن</button>
        <button class="btn-submit-exam" id="btn-submit-mock" onclick="submitMockExam()">✅ تسليم الامتحان وتصحيح النتيجة</button>
        <div class="mock-timer" id="mock-timer-display">⏱️ 30:00</div>
      </div>
      <div class="mock-score-report" id="mock-score-report">
        <div class="mock-score-num" id="mock-final-score">0 / 20</div>
        <div style="color: var(--text); font-weight: 700; margin-top: 6px;" id="mock-feedback-text">تم تصحيح الامتحان بنجاح! تفقد إجاباتك بالأسفل.</div>
      </div>
    </div>

    <div id="mock-exam-container" style="display: none;">
      <h3 style="color: var(--cyan); margin-bottom: 16px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
        Part I: Multiple Choice Questions (20 Questions - 1 Mark each)
      </h3>
      <div id="mock-mcq-list"></div>

      <h3 style="color: var(--yellow); margin: 30px 0 16px; border-bottom: 1px solid var(--border); padding-bottom: 8px;">
        Part II: Short Notes & Clinical Cases (5 Questions)
      </h3>
      <div id="mock-sn-list"></div>
    </div>
  </div>

</main>

<script>
  let correctScore = 0;
  let totalQuestions = {total_mcq};

  // Mock exam data
  const allMockMCQ = {mock_json_mcq};
  const allMockSN = {mock_json_sn};

  let mockTimerInterval = null;
  let mockTimeLeft = 30 * 60; // 30 mins
  let currentMockMCQ = [];
  let currentMockSN = [];
  let mockMCQAnswered = {{}};

  // === DUAL-ENGINE PARTICLES (RETINA CANVAS + WEBKIT HARDWARE ACCELERATED DOM CONFETTI) ===
  const pCanvas = document.getElementById('particles-canvas');
  const pCtx = pCanvas.getContext('2d');
  let pList = [];
  let pAnimId = null;
  let dpr = window.devicePixelRatio || 1;

  function resizeParticles() {{
    dpr = window.devicePixelRatio || 1;
    pCanvas.width = Math.floor(window.innerWidth * dpr);
    pCanvas.height = Math.floor(window.innerHeight * dpr);
    pCanvas.style.width = window.innerWidth + 'px';
    pCanvas.style.height = window.innerHeight + 'px';
    pCtx.setTransform(1, 0, 0, 1, 0, 0);
    pCtx.scale(dpr, dpr);
  }}
  window.addEventListener('resize', resizeParticles);
  window.addEventListener('orientationchange', resizeParticles);
  resizeParticles();

  function spawnCanvasParticles(x, y, count = 50) {{
    const colors = ['#10b981', '#34d399', '#06b6d4', '#3b82f6', '#fbbf24', '#f59e0b', '#a855f7', '#ec4899'];
    for (let i = 0; i < count; i++) {{
      const angle = Math.random() * Math.PI * 2;
      const speed = Math.random() * 8 + 3;
      pList.push({{
        x: x,
        y: y,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed - 2.5,
        size: Math.random() * 6 + 3,
        color: colors[Math.floor(Math.random() * colors.length)],
        alpha: 1,
        decay: Math.random() * 0.022 + 0.015,
        shape: Math.random() > 0.4 ? 'circle' : 'rect',
        rotation: Math.random() * Math.PI * 2,
        vRot: (Math.random() - 0.5) * 0.3
      }});
    }}
    if (!pAnimId) {{
      updateParticles();
    }}
  }}

  function updateParticles() {{
    pCtx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for (let i = pList.length - 1; i >= 0; i--) {{
      const p = pList[i];
      p.x += p.vx;
      p.y += p.vy;
      p.vy += 0.28; // gravity
      p.vx *= 0.98; // friction
      p.alpha -= p.decay;
      p.rotation += p.vRot;

      if (p.alpha <= 0 || p.y > window.innerHeight + 50) {{
        pList.splice(i, 1);
        continue;
      }}

      pCtx.save();
      pCtx.globalAlpha = Math.max(0, p.alpha);
      pCtx.translate(p.x, p.y);
      pCtx.rotate(p.rotation);
      pCtx.fillStyle = p.color;

      if (p.shape === 'circle') {{
        pCtx.beginPath();
        pCtx.arc(0, 0, p.size, 0, Math.PI * 2);
        pCtx.fill();
      }} else {{
        pCtx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size * 1.5);
      }}
      pCtx.restore();
    }}

    if (pList.length > 0) {{
      pAnimId = requestAnimationFrame(updateParticles);
    }} else {{
      pAnimId = null;
      pCtx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    }}
  }}

  // DOM Confetti Layer for 100% Guaranteed cross-platform rendering (MacBook Safari, iOS, Chrome)
  function spawnDomConfetti(x, y, count = 30) {{
    const colors = ['#10b981', '#34d399', '#06b6d4', '#3b82f6', '#fbbf24', '#f59e0b', '#a855f7', '#ec4899'];
    for (let i = 0; i < count; i++) {{
      const el = document.createElement('div');
      el.className = 'dom-confetti-particle';
      const size = Math.random() * 8 + 4;
      const angle = Math.random() * Math.PI * 2;
      const distance = Math.random() * 110 + 40;
      const destX = Math.cos(angle) * distance;
      const destY = Math.sin(angle) * distance - 25;
      const rot = (Math.random() - 0.5) * 720;
      const color = colors[Math.floor(Math.random() * colors.length)];
      const isCircle = Math.random() > 0.5;

      el.style.cssText = `
        position: fixed;
        left: ${{x}}px;
        top: ${{y}}px;
        width: ${{size}}px;
        height: ${{size * (isCircle ? 1 : 1.4)}}px;
        background: ${{color}};
        border-radius: ${{isCircle ? '50%' : '2px'}};
        box-shadow: 0 0 10px ${{color}};
        pointer-events: none;
        z-index: 999999;
        transform: translate3d(-50%, -50%, 0) scale(1);
        -webkit-transform: translate3d(-50%, -50%, 0) scale(1);
        transition: transform 0.8s cubic-bezier(0.12, 0.8, 0.33, 1), opacity 0.8s ease;
        -webkit-transition: -webkit-transform 0.8s cubic-bezier(0.12, 0.8, 0.33, 1), opacity 0.8s ease;
        opacity: 1;
      `;

      document.body.appendChild(el);

      requestAnimationFrame(() => {{
        el.style.transform = `translate3d(calc(-50% + ${{destX}}px), calc(-50% + ${{destY}}px), 0) rotate(${{rot}}deg) scale(0.3)`;
        el.style.webkitTransform = `translate3d(calc(-50% + ${{destX}}px), calc(-50% + ${{destY}}px), 0) rotate(${{rot}}deg) scale(0.3)`;
        el.style.opacity = '0';
      }});

      setTimeout(() => {{
        if (el && el.parentNode) el.parentNode.removeChild(el);
      }}, 850);
    }}
  }}

  function triggerCelebration(x, y) {{
    spawnCanvasParticles(x, y, 45);
    spawnDomConfetti(x, y, 25);
  }}

  document.addEventListener('DOMContentLoaded', () => {{
    // Letter numbering for MCQ options
    const letters = ['A', 'B', 'C', 'D', 'E'];
    document.querySelectorAll('#mcq-section .options').forEach(opts => {{
      opts.querySelectorAll('.opt-letter').forEach((letterEl, index) => {{
        letterEl.innerText = letters[index] || '';
      }});
    }});

    // Click handler for MCQ options
    document.querySelectorAll('#mcq-section .option').forEach(opt => {{
      opt.addEventListener('click', (e) => {{
        e.stopPropagation();
        const card = opt.closest('.q-card');
        if (card.classList.contains('answered') || document.body.classList.contains('show-all-mode')) return;

        card.classList.add('answered');

        if (opt.classList.contains('correct')) {{
          opt.classList.add('pop-animation');
          correctScore++;
          
          // Get exact viewport coordinates from bounding rect
          const rect = opt.getBoundingClientRect();
          const x = rect.left + rect.width / 2;
          const y = rect.top + rect.height / 2;
          triggerCelebration(x, y);
        }} else {{
          opt.classList.add('wrong-selected');
        }}
        updateScore();
      }});
    }});
  }});

  function updateScore() {{
    const scoreNum = document.querySelector('#score-stat .stat-num');
    if (scoreNum) scoreNum.innerText = `${{correctScore}}/${{totalQuestions}}`;
  }}

  function toggleQ(card) {{ card.classList.toggle('open'); }}
  function toggleCard(card) {{ card.classList.toggle('open'); }}
  function flipCard(card) {{ card.classList.toggle('flipped'); }}

  function showSection(id) {{
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(b => {{
      if (b.getAttribute('onclick') && b.getAttribute('onclick').includes('showSection')) {{
        b.classList.remove('active');
      }}
    }});
    const target = document.getElementById(id);
    if (target) target.classList.add('active');
    if (event && event.target) event.target.classList.add('active');
    resizeParticles();
  }}

  function showAllAnswers() {{
    document.body.classList.add('show-all-mode');
    document.querySelectorAll('.q-card, .sn-card').forEach(c => c.classList.add('open'));
  }}

  function retest() {{
    document.body.classList.remove('show-all-mode');
    correctScore = 0;
    updateScore();
    document.querySelectorAll('.q-card').forEach(card => card.classList.remove('answered'));
    document.querySelectorAll('.option').forEach(opt => opt.classList.remove('wrong-selected', 'pop-animation'));
  }}

  function searchQ(val) {{
    const q = val.trim().toLowerCase();
    document.querySelectorAll('#mcq-section .q-card').forEach(card => {{
      const text = card.innerText.toLowerCase();
      card.style.display = (!q || text.includes(q)) ? '' : 'none';
    }});
    document.querySelectorAll('#mcq-section .topic-group').forEach(group => {{
      const visible = [...group.querySelectorAll('.q-card')].some(c => c.style.display !== 'none');
      group.style.display = visible ? '' : 'none';
    }});
  }}

  function searchSN(val) {{
    const q = val.trim().toLowerCase();
    document.querySelectorAll('#shortnotes-section .sn-card').forEach(card => {{
      const text = card.innerText.toLowerCase();
      card.style.display = (!q || text.includes(q)) ? '' : 'none';
    }});
  }}

  // === MOCK EXAM LOGIC ===
  function shuffle(array) {{
    let cur = array.slice();
    for (let i = cur.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [cur[i], cur[j]] = [cur[j], cur[i]];
    }}
    return cur;
  }}

  function startMockExam() {{
    document.getElementById('btn-start-mock').style.display = 'none';
    document.getElementById('btn-submit-mock').style.display = 'inline-block';
    document.getElementById('mock-timer-display').style.display = 'inline-block';
    document.getElementById('mock-score-report').style.display = 'none';
    document.getElementById('mock-exam-container').style.display = 'block';

    // Pick 20 MCQs and 5 SN
    currentMockMCQ = shuffle(allMockMCQ).slice(0, 20);
    currentMockSN = shuffle(allMockSN).slice(0, 5);
    mockMCQAnswered = {{}};

    // Render Mock MCQs
    const mcqList = document.getElementById('mock-mcq-list');
    mcqList.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D', 'E'];

    currentMockMCQ.forEach((qItem, idx) => {{
      let optsHtml = '';
      qItem.options.forEach((opt, optIdx) => {{
        optsHtml += `
          <div class="option" onclick="selectMockOption(${{idx}}, ${{optIdx}}, this)">
            <div class="opt-letter">${{letters[optIdx]}}</div>
            <div class="opt-content">${{opt}}</div>
          </div>
        `;
      }});

      mcqList.innerHTML += `
        <div class="q-card open" id="mock-q-${{idx}}">
          <div class="q-header">
            <div class="q-num">Q${{idx + 1}}</div>
            <div class="q-text">${{qItem.q}}</div>
          </div>
          <div class="q-body" style="display: block;">
            <div class="options">${{optsHtml}}</div>
            <div class="note-box">${{qItem.note || ''}}</div>
          </div>
        </div>
      `;
    }});

    // Render Mock Short Notes
    const snList = document.getElementById('mock-sn-list');
    snList.innerHTML = '';
    currentMockSN.forEach((snItem, idx) => {{
      snList.innerHTML += `
        <div class="sn-card" onclick="toggleCard(this)">
          <div class="sn-header">
            <div class="sn-badge-tag">Short Note #${{idx + 1}} · ${{snItem.badge}}</div>
            <div class="sn-header-main">
              <span class="sn-icon">${{snItem.icon}}</span>
              <div class="sn-title">${{snItem.title}}</div>
            </div>
            <div class="sn-toggle">▼ اضغط للاطلاع على الإجابة النموذجية بعد إجابتك</div>
          </div>
          <div class="sn-body">
            <div class="sn-topic-ref">📌 الموضوع: ${{snItem.topic}}</div>
            ${{snItem.answer_html}}
          </div>
        </div>
      `;
    }});

    // Start timer
    mockTimeLeft = 30 * 60;
    if (mockTimerInterval) clearInterval(mockTimerInterval);
    mockTimerInterval = setInterval(() => {{
      mockTimeLeft--;
      if (mockTimeLeft <= 0) {{
        clearInterval(mockTimerInterval);
        submitMockExam();
      }}
      const mins = Math.floor(mockTimeLeft / 60);
      const secs = mockTimeLeft % 60;
      document.getElementById('mock-timer-display').innerText = `⏱️ ${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
    }}, 1000);
  }}

  function selectMockOption(qIdx, optIdx, optEl) {{
    const card = document.getElementById(`mock-q-${{qIdx}}`);
    if (card.classList.contains('graded')) return;

    card.querySelectorAll('.option').forEach(o => o.style.borderColor = 'var(--border)');
    optEl.style.borderColor = 'var(--blue)';
    optEl.style.background = 'rgba(59, 130, 246, 0.1)';
    mockMCQAnswered[qIdx] = optIdx;
  }}

  function submitMockExam() {{
    if (mockTimerInterval) clearInterval(mockTimerInterval);
    document.getElementById('btn-submit-mock').style.display = 'none';
    document.getElementById('btn-start-mock').style.display = 'inline-block';
    document.getElementById('btn-start-mock').innerText = '🔄 إعادة محاكاة الامتحان التجريبي';

    let score = 0;
    currentMockMCQ.forEach((qItem, idx) => {{
      const card = document.getElementById(`mock-q-${{idx}}`);
      card.classList.add('graded');
      const selected = mockMCQAnswered[idx];
      const correct = qItem.correct;
      const opts = card.querySelectorAll('.option');

      opts.forEach((o, oIdx) => {{
        o.style.pointerEvents = 'none';
        if (oIdx === correct) {{
          o.classList.add('correct');
        }} else if (oIdx === selected && selected !== correct) {{
          o.classList.add('wrong-selected');
        }} else {{
          o.style.opacity = '0.4';
        }}
      }});

      if (selected === correct) {{
        score++;
      }}
    }});

    // Celebrate with particles if passed
    if (score >= 12) {{
      for (let i = 0; i < 5; i++) {{
        setTimeout(() => {{
          const rx = Math.random() * window.innerWidth;
          const ry = Math.random() * (window.innerHeight / 2) + 100;
          triggerCelebration(rx, ry);
        }}, i * 250);
      }}
    }}

    // Open short notes answers
    document.querySelectorAll('#mock-sn-list .sn-card').forEach(c => c.classList.add('open'));

    // Show score report
    const report = document.getElementById('mock-score-report');
    report.style.display = 'block';
    document.getElementById('mock-final-score').innerText = `${{score}} / 20 (${{Math.round((score/20)*100)}}%)`;

    let feedback = "ممتاز جداً! جاهز تماماً للميدتيرم وقفلته بنجاح 🎯";
    if (score < 12) feedback = "راجع الأسئلة والملاحظات اللي غلطت فيها وذاكرها كويس وحاول تاني 💪";
    else if (score < 17) feedback = "مستوى جيد جداً! محتاج تركز على بعض التفاصيل البسيطة في الملاحظات وتدخل تقفل الامتحان 🔥";
    document.getElementById('mock-feedback-text').innerText = feedback;
  }}
</script>

</body>
</html>
'''

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_template)

print(f"Successfully generated: {output_path}")
print(f"File size: {os.path.getsize(output_path)} bytes")
