import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
scratch_dir = r'd:\Coding\PT12\scratch'

def print_section(filename):
    path = os.path.join(scratch_dir, filename)
    print(f"\n{'='*70}\nCONTENT OF: {filename}\n{'='*70}")
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())

if __name__ == '__main__':
    for fn in ['pain 2025.txt', 'organization of body tissue 2022 (1).txt']:
        print_section(fn)
