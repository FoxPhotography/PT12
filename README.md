# PT Hub — بنك أسئلة العلاج الطبيعي (دفعة PT12)

موقع static (HTML بس) فيه أسئلة الميدتيرم والفاينال والشفوي لكل مادة، مترتب بالسنين حسب لايحة كلية العلاج الطبيعي — جامعة كفر الشيخ.

## ترتيب الفولدر

```
PT12/
├── index.html              ← الصفحة الرئيسية (اختيار السنة + المواد)
├── assets/
│   ├── theme.css           ← ثيم الموقع المشترك (#590907 / #e8d2b5 / #a5a79b + gradients)
│   └── favicon.svg
├── year-1/<مادة>/<صفحة>.html   ← صفحات السنة الأولى
├── year-2/<مادة>/<صفحة>.html   ← صفحات السنة التانية
├── year-3/<مادة>/<صفحة>.html   ← صفحات السنة التالتة
├── data/                   ← المحاضرات والـ PDFs والصور (مش بتترفع على Vercel)
│   ├── year-2/ …  year-3/ …
│   └── اللائحة.pdf
├── tools/                  ← سكريبتات التوليد والثيم (مش بتترفع)
│   ├── theme/retheme.py    ← يحوّل أي صفحة قديمة غامقة للثيم الجديد
│   ├── theme/post.py       ← يضيف theme.css وزرار PT Hub ويظبط اللينكات
│   ├── generators/         ← سكريبتات بناء الصفحات (منها immunology/)
│   └── moves.log           ← كل ملف اتنقل من فين لفين
├── archive/                ← حاجات قديمة (pt-exam-hub، rar/zip، نسخ مكررة)
├── vercel.json             ← Clean URLs + redirects من اللينكات القديمة
└── .vercelignore
```

## إضافة مادة/امتحان جديد

1. حط ملفات المحاضرات في `data/year-N/<subject>/`.
2. حط صفحة الامتحان في `year-N/<subject>/midterm.html` (أو `final.html` / `oral.html`).
3. في `<head>` ضيف:
   `<link rel="stylesheet" href="../../assets/theme.css">` وزرار الرجوع `../../index.html`.
4. افتح `index.html` وضيف اللينك جوه `YEARS` تحت المادة: `['mid', 'ميدتيرم', 'وصف قصير', 'year-N/subject/midterm.html']`.
   الأنواع: `mid` ميدتيرم · `fin` فاينال · `oral` شفوي · `rev` مراجعة.
5. لو السنة الحالية اتغيرت، غيّر `const CURRENT = 3;`.

## النشر على Vercel

- Framework Preset: **Other** — مفيش build.
- `vercel.json` بيشيل `.html` من اللينكات وبيحوّل اللينكات القديمة (`/Midterm/...`, `/final/...`, `/oral/...`) للأماكن الجديدة، فاللينكات اللي اتبعتت قبل كده لسه شغالة.
