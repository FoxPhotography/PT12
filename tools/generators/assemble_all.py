# -*- coding: utf-8 -*-
"""
Assembler script for Anatomy 2 Lower Limb Master Page
"""

import os
from sec1 import get_section_1
from sec2 import get_section_2
from sec3 import get_section_3
from sec4 import get_section_4
from sec5 import get_section_5
from sec6 import get_section_6
from sec7 import get_section_7
from sec8 import get_section_8
from sec9 import get_section_9

output_file = r"d:\Coding\PT12\final\anatomy2_lower_limb.html"

# Read header from generate_full_anatomy2.py or define it directly
with open(r"d:\Coding\PT12\scratch\generate_full_anatomy2.py", "r", encoding="utf-8") as f:
    text = f.read()

# Extract the header string from the start of the write call to just after <div class="search-results-info"...></div>\n</div>
start_marker = '<!DOCTYPE html>'
end_marker = '<div class="search-results-info" id="searchInfo">تم العثور على <span id="searchCount">0</span> نتيجة</div>\n</div>'

header_html = text[text.find(start_marker):text.find(end_marker) + len(end_marker)]

# Footer, Modals, and Scripts
modals_and_scripts = """
</main>

<!-- === FLASHCARD OVERLAY === -->
<div class="flashcard-overlay" id="flashcardOverlay">
  <div class="flashcard-header">
    <span class="flashcard-counter" id="flashcardCounter">1 / 30</span>
    <button class="flashcard-close" onclick="closeFlashcards()">✕</button>
  </div>

  <div class="flashcard-scene" onclick="flipCard()">
    <div class="flashcard-card" id="flashcardCard">
      <div class="flashcard-face flashcard-front">
        <span class="flashcard-section-tag" id="fcSection">Gluteal Region</span>
        <div class="flashcard-label">Question</div>
        <div class="flashcard-text" id="fcQuestion">What is the nerve supply of Gluteus Maximus?</div>
        <div class="flashcard-hint">اضغط للقلب والاطلاع على الإجابة (أو مسافة المسافة)</div>
      </div>
      <div class="flashcard-face flashcard-back">
        <span class="flashcard-section-tag">Model Answer</span>
        <div class="flashcard-label">Answer</div>
        <div class="flashcard-text" id="fcAnswer">Inferior Gluteal Nerve (L5, S1, S2)</div>
        <div class="flashcard-hint">استخدم الأسهم ◀ ▶ للتنقل</div>
      </div>
    </div>
  </div>

  <div class="flashcard-nav">
    <button onclick="prevCard()">◀ السابق</button>
    <button onclick="shuffleCards()">🔀 عشوائي</button>
    <button onclick="nextCard()">التالي ▶</button>
  </div>
</div>

<!-- === QUICK REF SIDEBAR === -->
<div class="quickref-overlay" id="qrOverlay" onclick="toggleQuickRef()"></div>
<div class="quickref-sidebar" id="qrSidebar">
  <div class="qr-header">
    <div class="qr-title">📌 Quick Reference — Lower Limb</div>
    <button class="qr-close" onclick="toggleQuickRef()">✕</button>
  </div>

  <div class="qr-section">
    <span class="qr-section-title purple">Nerve Roots & Innervations</span>
    <ul class="qr-items">
      <li><strong>Femoral Nerve:</strong> L2, L3, L4 (Posterior divisions)</li>
      <li><strong>Obturator Nerve:</strong> L2, L3, L4 (Anterior divisions)</li>
      <li><strong>Superior Gluteal:</strong> L4, L5, S1 (Gluteus medius/minimus)</li>
      <li><strong>Inferior Gluteal:</strong> L5, S1, S2 (Gluteus maximus)</li>
      <li><strong>Sciatic Nerve:</strong> L4, L5, S1, S2, S3 (Thickest nerve)</li>
      <li><strong>Common Fibular:</strong> L4, L5, S1, S2 (Neck of fibula)</li>
      <li><strong>Tibial Nerve:</strong> L4, L5, S1, S2, S3 (Posterior compartment)</li>
    </ul>
  </div>

  <div class="qr-section">
    <span class="qr-section-title cyan">Crucial Reflexes & Tests</span>
    <ul class="qr-items">
      <li><strong>Knee Jerk (Patellar):</strong> L3, L4 (Femoral nerve)</li>
      <li><strong>Ankle Jerk (Achilles):</strong> S1, S2 (Tibial nerve)</li>
      <li><strong>Trendelenburg Test:</strong> Superior Gluteal N. (Stance side)</li>
      <li><strong>Straight Leg Raise (SLR):</strong> Sciatic nerve root traction</li>
      <li><strong>Femoral Pulse:</strong> Mid-Inguinal Point (ASIS to Pubic Symphysis)</li>
    </ul>
  </div>

  <div class="qr-section">
    <span class="qr-section-title red">Clinical Deformities</span>
    <ul class="qr-items">
      <li><strong>Foot Drop (Equinovarus):</strong> Common Fibular N. lesion</li>
      <li><strong>Calcaneovalgus:</strong> Tibial N. lesion (loss of plantarflexion)</li>
      <li><strong>Waddling Gait:</strong> Bilateral Trendelenburg deficiency</li>
      <li><strong>Meralgia Paresthetica:</strong> Lateral Cutaneous of Thigh (L2, L3)</li>
      <li><strong>Tarsal Tunnel Syndrome:</strong> Tibial N. behind medial malleolus</li>
      <li><strong>Baker's Cyst:</strong> Semimembranosus bursa enlargement</li>
    </ul>
  </div>

  <div class="qr-section">
    <span class="qr-section-title yellow">High-Yield Mnemonics</span>
    <ul class="qr-items">
      <li><strong>NAVL (Femoral Base):</strong> Nerve, Artery, Vein, Lymphatics (lat to med)</li>
      <li><strong>SGS (Pes Anserinus):</strong> Sartorius (Femoral), Gracilis (Obturator), Semitendinosus (Sciatic)</li>
      <li><strong>PIN (GSF to LSF):</strong> Pudendal N., Int. Pudendal vessels, N. to Obturator Internus</li>
    </ul>
  </div>
</div>

<!-- === KEYBOARD SHORTCUTS MODAL === -->
<div class="shortcuts-modal" id="shortcutsModal" onclick="if(event.target===this) toggleShortcuts()">
  <div class="shortcuts-box">
    <h3>⌨️ اختصارات لوحة المفاتيح</h3>
    <div class="shortcut-row"><span class="shortcut-key">S</span><span class="shortcut-desc">البحث السريع</span></div>
    <div class="shortcut-row"><span class="shortcut-key">F</span><span class="shortcut-desc">فتح الفلاش كاردز (اختبر نفسك)</span></div>
    <div class="shortcut-row"><span class="shortcut-key">Q</span><span class="shortcut-desc">المرجع السريع جانبي</span></div>
    <div class="shortcut-row"><span class="shortcut-key">P</span><span class="shortcut-desc">طباعة أو تصدير PDF</span></div>
    <div class="shortcut-row"><span class="shortcut-key">◀ / ▶</span><span class="shortcut-desc">التنقل بين الأقسام / البطاقات</span></div>
    <div class="shortcut-row"><span class="shortcut-key">Space</span><span class="shortcut-desc">قلب البطاقة (Flip Card)</span></div>
    <div class="shortcut-row"><span class="shortcut-key">Esc</span><span class="shortcut-desc">إغلاق النوافذ المنبثقة</span></div>
  </div>
</div>

<script>
  // === SECTION NAVIGATION ===
  const sectionIds = [
    'gluteal',
    'femoral-triangle',
    'ant-thigh',
    'med-thigh',
    'post-thigh',
    'fem-obt-nerves',
    'sciatic-nerves',
    'comparisons',
    'viva-spotting'
  ];
  let currentSectionIndex = 0;

  function showSection(id, btn) {
    document.querySelectorAll('.section').forEach(s => s.classList.remove('active'));
    document.querySelectorAll('.nav-btn:not(.special)').forEach(b => b.classList.remove('active'));
    
    const targetSection = document.getElementById(id);
    if (targetSection) {
      targetSection.classList.add('active');
      currentSectionIndex = sectionIds.indexOf(id);
    }
    
    if (btn) {
      btn.classList.add('active');
    } else {
      const matchingBtn = document.querySelector(`.nav-btn[onclick*="'${id}'"]`);
      if (matchingBtn) matchingBtn.classList.add('active');
    }
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
    updateProgress();
  }

  function nextSection() {
    currentSectionIndex = (currentSectionIndex + 1) % sectionIds.length;
    showSection(sectionIds[currentSectionIndex]);
  }

  function prevSection() {
    currentSectionIndex = (currentSectionIndex - 1 + sectionIds.length) % sectionIds.length;
    showSection(sectionIds[currentSectionIndex]);
  }

  // === ESSAY QUESTION ACCORDION ===
  function toggleEssay(header) {
    const card = header.parentElement;
    card.classList.toggle('open');
  }

  // Open all essay cards by default for smooth reading or keep first open
  document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.essay-card').forEach((c, idx) => {
      if (idx < 2) c.classList.add('open');
    });
  });

  // === COMPLETION TRACKING ===
  const completedSections = JSON.parse(localStorage.getItem('anatomy2_completed') || '{}');

  function toggleComplete(sectionId, btn) {
    completedSections[sectionId] = !completedSections[sectionId];
    localStorage.setItem('anatomy2_completed', JSON.stringify(completedSections));
    updateCompletionUI(sectionId, btn);
    updateProgress();

    if (completedSections[sectionId]) {
      triggerConfetti(btn);
    }
  }

  function updateCompletionUI(sectionId, btn) {
    const isDone = !!completedSections[sectionId];
    if (btn) {
      btn.textContent = isDone ? '✓ تم المذاكرة' : '☐ تم المذاكرة';
      btn.classList.toggle('completed', isDone);
    }
  }

  function updateProgress() {
    const total = sectionIds.length;
    let completedCount = 0;
    sectionIds.forEach(id => {
      if (completedSections[id]) completedCount++;
      const btn = document.querySelector(`.sec-complete-btn[data-section="${id}"]`);
      if (btn) updateCompletionUI(id, btn);
    });

    const percent = Math.round((completedCount / total) * 100);
    document.getElementById('progressFill').style.width = percent + '%';
    document.getElementById('progressBadge').textContent = `${completedCount}/${total}`;
  }

  // === CONFETTI ANIMATION ===
  function triggerConfetti(el) {
    const container = document.createElement('div');
    container.className = 'confetti-container';
    document.body.appendChild(container);

    const colors = ['#3b82f6', '#06b6d4', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899'];
    const rect = el.getBoundingClientRect();
    for (let i = 0; i < 35; i++) {
      const piece = document.createElement('div');
      piece.className = 'confetti-piece';
      piece.style.background = colors[Math.floor(Math.random() * colors.length)];
      piece.style.left = (rect.left + rect.width/2 + (Math.random()-0.5)*120) + 'px';
      piece.style.top = (rect.top) + 'px';
      piece.style.animationDuration = (1 + Math.random()) + 's';
      piece.style.animationDelay = (Math.random() * 0.3) + 's';
      container.appendChild(piece);
    }
    setTimeout(() => container.remove(), 2000);
  }

  // === SEARCH FUNCTIONALITY ===
  function searchAll(query) {
    document.querySelectorAll('mark.search-hl').forEach(m => {
      const parent = m.parentNode;
      parent.replaceChild(document.createTextNode(m.textContent), m);
      parent.normalize();
    });

    const info = document.getElementById('searchInfo');
    if (!query || query.length < 2) {
      info.style.display = 'none';
      return;
    }

    let totalMatches = 0;
    let firstMatchSection = null;

    sectionIds.forEach(id => {
      const section = document.getElementById(id);
      const walker = document.createTreeWalker(section, NodeFilter.SHOW_TEXT, null, false);
      const nodes = [];
      while (walker.nextNode()) nodes.push(walker.currentNode);

      nodes.forEach(node => {
        const text = node.textContent;
        const lowerText = text.toLowerCase();
        const lowerQuery = query.toLowerCase();
        const idx = lowerText.indexOf(lowerQuery);
        if (idx >= 0) {
          totalMatches++;
          if (!firstMatchSection) firstMatchSection = id;
          const before = text.substring(0, idx);
          const match = text.substring(idx, idx + query.length);
          const after = text.substring(idx + query.length);
          const mark = document.createElement('mark');
          mark.className = 'search-hl';
          mark.textContent = match;
          const parent = node.parentNode;
          parent.insertBefore(document.createTextNode(before), node);
          parent.insertBefore(mark, node);
          parent.insertBefore(document.createTextNode(after), node);
          parent.removeChild(node);
        }
      });
    });

    document.getElementById('searchCount').textContent = totalMatches;
    info.style.display = totalMatches > 0 ? 'block' : 'none';

    if (firstMatchSection && firstMatchSection !== sectionIds[currentSectionIndex]) {
      showSection(firstMatchSection);
    }

    // Open any essay card containing search hit
    document.querySelectorAll('.section.active mark.search-hl').forEach(m => {
      const essayCard = m.closest('.essay-card');
      if (essayCard) essayCard.classList.add('open');
    });

    const firstMark = document.querySelector('.section.active mark.search-hl');
    if (firstMark) {
      setTimeout(() => firstMark.scrollIntoView({ behavior: 'smooth', block: 'center' }), 200);
    }
  }

  // === FLASHCARDS DECK (30 CARDS) ===
  const flashcards = [
    { q: "What is the nerve supply of Gluteus Maximus?", a: "Inferior Gluteal Nerve (L5, S1, S2)", s: "Gluteal Region" },
    { q: "What is the nerve supply of Gluteus Medius & Minimus?", a: "Superior Gluteal Nerve (L4, L5, S1)", s: "Gluteal Region" },
    { q: "What causes a Positive Trendelenburg Sign?", a: "Superior Gluteal Nerve injury or Gluteus Medius paralysis on the STANCE side (pelvis drops on unsupported swing side)", s: "Gluteal Region" },
    { q: "Where is the ONLY safe quadrant for IM injection in the buttock?", a: "Upper Outer (Anterosuperior) Quadrant — avoids the Sciatic Nerve!", s: "Gluteal Region" },
    { q: "Name the structures passing ABOVE the Piriformis muscle", a: "Superior Gluteal Nerve, Superior Gluteal Artery, Superior Gluteal Vein", s: "Gluteal Region" },
    { q: "Name the structures passing through BOTH Greater and Lesser Sciatic Foramina (PIN)", a: "Pudendal nerve, Internal pudendal vessels, Nerve to obturator internus", s: "Gluteal Region" },
    { q: "What forms the boundaries of the Femoral Ring?", a: "Anterior: Inguinal ligament; Posterior: Pectineus & Pectineal ligament; Medial: Lacunar ligament; Lateral: Femoral vein", s: "Femoral Triangle" },
    { q: "What are the contents of the Femoral Canal?", a: "Fat, lymphatic vessels, and Deep Inguinal Lymph Node of Cloquet (Rosenmüller)", s: "Femoral Triangle" },
    { q: "Why is Femoral Hernia more prone to strangulation than Inguinal Hernia?", a: "Rigid unyielding boundaries (especially sharp edge of Lacunar Ligament) and narrow neck (1.25 cm)", s: "Femoral Triangle" },
    { q: "Is the Femoral Nerve INSIDE or OUTSIDE the Femoral Sheath?", a: "OUTSIDE (lies laterally in the groove between Psoas and Iliacus)", s: "Femoral Triangle" },
    { q: "What are the boundaries of the Femoral Triangle?", a: "Superior: Inguinal ligament; Lateral: Medial border of Sartorius; Medial: Medial border of Adductor longus", s: "Femoral Triangle" },
    { q: "What is the chief powerful extensor of the knee joint?", a: "Quadriceps Femoris (supplied by Femoral Nerve L2, L3, L4)", s: "Anterior Thigh" },
    { q: "What are the 3 muscles of Pes Anserinus and their nerves?", a: "Sartorius (Femoral), Gracilis (Obturator), Semitendinosus (Sciatic/Tibial) — SGS", s: "Medial Thigh" },
    { q: "Why is Adductor Magnus a composite / hybrid muscle?", a: "Dual nerve supply: Adductor part by Obturator Nerve (L2-L4); Hamstring part by Tibial part of Sciatic Nerve (L4)", s: "Medial Thigh" },
    { q: "What passes through the Adductor Hiatus?", a: "Femoral Artery and Vein (changing into Popliteal Artery and Vein in popliteal fossa)", s: "Medial Thigh" },
    { q: "What are the 4 criteria for a true hamstring muscle?", a: "1. Origin from ischial tuberosity, 2. Insertion into leg bones, 3. Crosses 2 joints, 4. Innervated by Tibial nerve", s: "Posterior Thigh" },
    { q: "Why is the Short Head of Biceps Femoris NOT a true hamstring?", a: "Arises from linea aspera, crosses only knee, innervated by Common Fibular (Peroneal) nerve", s: "Posterior Thigh" },
    { q: "Which muscle unlocks the locked knee joint?", a: "Popliteus muscle (laterally rotates femur on fixed tibia at initiation of flexion)", s: "Popliteal Fossa" },
    { q: "List the contents of Popliteal Fossa from superficial to deep", a: "Tibial Nerve → Common Fibular Nerve → Popliteal Vein → Popliteal Artery", s: "Popliteal Fossa" },
    { q: "What is the nerve root value of the Femoral Nerve?", a: "L2, L3, L4 (Posterior divisions of anterior rami of lumbar plexus)", s: "Nerves" },
    { q: "What is the longest cutaneous nerve in the human body?", a: "Saphenous Nerve (branch of posterior division of Femoral Nerve)", s: "Nerves" },
    { q: "What sensory deficit occurs in Deep Fibular Nerve injury?", a: "Loss of sensation in the 1st Interdigital Web Space ONLY (between great toe and 2nd toe)", s: "Nerves" },
    { q: "What is the deformity and gait caused by Common Fibular Nerve injury?", a: "Foot Drop (Equinovarus deformity) with High-Stepping (Cock-Walk) Gait", s: "Nerves" },
    { q: "Why is the Common Fibular Nerve easily injured?", a: "Directly winds around the subcutaneous hard neck of the fibula", s: "Nerves" },
    { q: "What is the deformity caused by Tibial Nerve injury?", a: "Calcaneovalgus deformity (loss of plantarflexion, inability to stand on tiptoes)", s: "Nerves" },
    { q: "What is Tarsal Tunnel Syndrome?", a: "Compression of the Tibial Nerve beneath the flexor retinaculum behind the medial malleolus", s: "Nerves" },
    { q: "What is Meralgia Paresthetica?", a: "Entrapment of the Lateral Cutaneous Nerve of Thigh (L2, L3) under the lateral inguinal ligament (burning outer thigh pain)", s: "Nerves" },
    { q: "What is Hilton's Law?", a: "The nerve supplying a joint also supplies the muscles moving that joint and the skin over their insertions", s: "Nerves" },
    { q: "What is the spinal segment tested by Knee Jerk vs Ankle Jerk?", a: "Knee Jerk = L3, L4 (Femoral N.); Ankle Jerk = S1, S2 (Tibial N.)", s: "Nerves" },
    { q: "Where is the Femoral Pulse palpated?", a: "At the Mid-Inguinal Point (midway between ASIS and Pubic Symphysis)", s: "Practical" }
  ];

  let currentCard = 0;
  let cardOrder = [...Array(flashcards.length).keys()];

  function openFlashcards() {
    document.getElementById('flashcardOverlay').classList.add('active');
    currentCard = 0;
    updateFlashcard();
  }

  function closeFlashcards() {
    document.getElementById('flashcardOverlay').classList.remove('active');
    document.getElementById('flashcardCard').classList.remove('flipped');
  }

  function flipCard() {
    document.getElementById('flashcardCard').classList.toggle('flipped');
  }

  function nextCard() {
    document.getElementById('flashcardCard').classList.remove('flipped');
    setTimeout(() => {
      currentCard = (currentCard + 1) % cardOrder.length;
      updateFlashcard();
    }, 150);
  }

  function prevCard() {
    document.getElementById('flashcardCard').classList.remove('flipped');
    setTimeout(() => {
      currentCard = (currentCard - 1 + cardOrder.length) % cardOrder.length;
      updateFlashcard();
    }, 150);
  }

  function shuffleCards() {
    for (let i = cardOrder.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [cardOrder[i], cardOrder[j]] = [cardOrder[j], cardOrder[i]];
    }
    currentCard = 0;
    document.getElementById('flashcardCard').classList.remove('flipped');
    setTimeout(updateFlashcard, 150);
  }

  function updateFlashcard() {
    const fc = flashcards[cardOrder[currentCard]];
    document.getElementById('fcQuestion').textContent = fc.q;
    document.getElementById('fcAnswer').textContent = fc.a;
    document.getElementById('fcSection').textContent = fc.s;
    document.getElementById('flashcardCounter').textContent = (currentCard + 1) + ' / ' + cardOrder.length;
  }

  // === QUICK REF & SHORTCUTS ===
  function toggleQuickRef() {
    document.getElementById('qrOverlay').classList.toggle('active');
    document.getElementById('qrSidebar').classList.toggle('active');
  }

  function toggleShortcuts() {
    document.getElementById('shortcutsModal').classList.toggle('active');
  }

  // === ARABIC TRANSLATION TOGGLE ===
  function toggleTranslation(sectionId, btn) {
    const panel = document.getElementById('arabic-' + sectionId);
    if (!panel) return;
    const isActive = panel.classList.contains('active');
    
    document.querySelectorAll('.arabic-panel.active').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.translate-btn.active').forEach(b => b.classList.remove('active'));
    
    if (!isActive) {
      panel.classList.add('active');
      btn.classList.add('active');
      setTimeout(() => panel.scrollIntoView({ behavior: 'smooth', block: 'nearest' }), 100);
    }
  }

  // === KEYBOARD SHORTCUTS ===
  document.addEventListener('keydown', function(e) {
    if (e.target.tagName === 'INPUT') return;

    const flashcardOpen = document.getElementById('flashcardOverlay').classList.contains('active');

    if (e.key === 'Escape') {
      closeFlashcards();
      document.getElementById('qrOverlay').classList.remove('active');
      document.getElementById('qrSidebar').classList.remove('active');
      document.getElementById('shortcutsModal').classList.remove('active');
      return;
    }

    if (flashcardOpen) {
      if (e.key === 'ArrowLeft' || e.key === 'ArrowDown') nextCard();
      else if (e.key === 'ArrowRight' || e.key === 'ArrowUp') prevCard();
      else if (e.key === ' ') { e.preventDefault(); flipCard(); }
      return;
    }

    if (e.key === 'ArrowLeft') nextSection();
    else if (e.key === 'ArrowRight') prevSection();
    else if (e.key.toLowerCase() === 's') { e.preventDefault(); document.getElementById('searchInput').focus(); }
    else if (e.key.toLowerCase() === 'f') { e.preventDefault(); openFlashcards(); }
    else if (e.key.toLowerCase() === 'q') { e.preventDefault(); toggleQuickRef(); }
    else if (e.key.toLowerCase() === 'k') { e.preventDefault(); toggleShortcuts(); }
    else if (e.key.toLowerCase() === 'p') { e.preventDefault(); window.print(); }
  });

  // Init Progress
  updateProgress();

  window.addEventListener('pageshow', function(event) {
    if (event.persisted) window.location.reload();
  });
</script>

</body>
</html>
"""

# Assemble full file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(header_html)
    f.write(get_section_1())
    f.write(get_section_2())
    f.write(get_section_3())
    f.write(get_section_4())
    f.write(get_section_5())
    f.write(get_section_6())
    f.write(get_section_7())
    f.write(get_section_8())
    f.write(get_section_9())
    f.write(modals_and_scripts)

print(f"Successfully generated: {output_file} (Size: {os.path.getsize(output_file)} bytes)")
