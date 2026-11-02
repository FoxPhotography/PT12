import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

scratch_dir = r'd:\Coding\PT12\scratch'
files = [
    'Electromagntic spectrum 1st lecture.txt',
    '4_5771686230433467148.txt',
    'uv+edited+2025.txt',
    'ultrasound+2025.txt',
    'Short+wave+2025.txt',
    'pain 2025.txt',
    'organization of body tissue 2022 (1).txt'
]

for f in files:
    path = os.path.join(scratch_dir, f)
    with open(path, 'r', encoding='utf-8') as fl:
        text = fl.read()
    print('================================================================')
    print(f'FILE: {f} (Length: {len(text)} chars)')
    print('================================================================')
    pages = text.split('=== PAGE ')
    print(f'Total Pages: {len(pages)-1}')
    for p in pages[1:]:
        p_lines = [l.strip() for l in p.split('\n') if l.strip()]
        if p_lines:
            p_num = p_lines[0].split(' ===')[0]
            summary = ' | '.join(p_lines[1:4])
            print(f'  Page {p_num}: {summary[:120]}')
    print()
