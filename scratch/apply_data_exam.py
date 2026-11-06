# -*- coding: utf-8 -*-
import sys, os

HERE = r"d:\Coding\PT12\tools\generators\thera"
sys.path.insert(0, r"d:\Coding\PT12\scratch")
from update_thera_cases import ALL_CASES

DATA_EXAM_PATH = os.path.join(HERE, "data_exam.py")
content = open(DATA_EXAM_PATH, encoding="utf-8").read()

# Replace CASES = [...]
import re

cases_code = ["CASES = ["]
for idx, (txt, qs) in enumerate(ALL_CASES, 1):
    cases_code.append(f" # Case {idx} (20 MCQs)")
    cases_code.append(f" ({repr(txt)}, [")
    for q_text, opts, expl in qs:
        cases_code.append(f"   ({repr(q_text)}, {repr(opts)}, {repr(expl)}),")
    cases_code.append(" ]),")
cases_code.append("]\n")

cases_str = "\n".join(cases_code)

# Replace between '# ---- Case sets (MCQ)' and '# ---- Written cases'
pattern = r"# ---- Case sets \(MCQ\).*?# ---- Written cases"
replacement = cases_str + "\n# ---- Written cases"

new_content, count = re.subn(pattern, replacement, content, flags=re.S)
if count != 1:
    print(f"Error replacing CASES, count={count}")
    sys.exit(1)

open(DATA_EXAM_PATH, "w", encoding="utf-8").write(new_content)
print(f"Successfully updated {DATA_EXAM_PATH} with {len(ALL_CASES)} cases!")

