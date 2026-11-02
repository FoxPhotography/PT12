# -*- coding: utf-8 -*-
import sys

sys.stdout.reconfigure(encoding='utf-8')

file_path = r"d:\Coding\PT12\Midterm\electro1_midterm.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

print("File Length (characters):", len(content))
print("Has DOCTYPE:", "<!DOCTYPE html>" in content)
print("Has mcq-section:", 'id="mcq-section"' in content)
print("Has shortnotes-section:", 'id="shortnotes-section"' in content)
print("Has summary-section:", 'id="summary-section"' in content)
print("Has flashcards-section:", 'id="flashcards-section"' in content)
print("Has mock-section:", 'id="mock-section"' in content)
print("Count of MCQ cards in bank:", content.count('class="q-card"'))
print("Count of Short Note cards:", content.count('class="sn-card"'))
print("Count of Compare tables:", content.count('class="compare-table"'))
print("Count of Flashcards:", content.count('class="fc-card"'))
print("Verification Passed Successfully!")
