import re
import os

md_path = r"d:\Coding\PT12\muscletest2.md"

with open(md_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Let's split by section headers
# We can find all section headers. They start with # or ## but not ###
# Let's write a robust parser.

lines = content.split('\n')
sections = []
current_section = None
current_question = None

for line in lines:
    line_str = line.strip()
    if not line_str:
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
    if line_str.startswith('*') or line_str.startswith('-'):
        opt_text = line_str[1:].strip()
        is_correct = False
        if '✅' in opt_text:
            is_correct = True
            opt_text = opt_text.replace('✅', '').strip()
        
        # Also handle checked/unchecked marks in text if any
        if current_question is not None:
            current_question['options'].append({
                'text': opt_text,
                'correct': is_correct
            })

print(f"Total Sections: {len(sections)}")
total_q = 0
for sec in sections:
    print(f"Section: {sec['title']} -> {len(sec['questions'])} questions")
    total_q += len(sec['questions'])
print(f"Total Questions: {total_q}")
