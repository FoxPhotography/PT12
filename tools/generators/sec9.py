# -*- coding: utf-8 -*-
"""
Module to generate Section 9 (Practical OSPE Spotting & Rapid-Fire Oral Viva Simulator)
"""

def get_section_9():
    return """
<!-- ============================================================ -->
<!-- SECTION 9: PRACTICAL & SPOTTING OSPE & ORAL SIMULATOR          -->
<!-- ============================================================ -->
<div class="section" id="viva-spotting">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-pink">🔬</div>
      <div class="sec-title">9. Practical OSPE Spotting & Rapid-Fire Oral Viva Simulator</div>
      <button class="translate-btn" onclick="toggleTranslation('viva-spotting', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="viva-spotting" onclick="toggleComplete('viva-spotting', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-viva-spotting">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">🔬</span>
        <span class="arabic-panel-title">شرح بالعربي — محطات العملي (OSPE) وأسئلة الشفوي السريعة والمصائد</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p>في امتحانات العملي (Spotting) وامتحانات الشفوي (Oral Viva)، الدكتور بيمسك دبوس في الجثة أو الموديل وبيسألك سؤالين ثابتين:</p>
      <div class="ar-highlight">
        📌 <strong>السؤالين الثابتين في كل محطة عملي:</strong><br>
        1. <strong>Identify the tagged structure:</strong> (اسم العضلة أو العصب أو الشريان).<br>
        2. <strong>Mention its Nerve Supply OR Action:</strong> (عصبها أو وظيفتها أو علاقتها الإكلينيكية).
      </div>
    </div>

    <!-- PRACTICAL STATION 1 -->
    <div class="content-card">
      <div class="subsection-title" style="color:var(--yellow)">🔬 Station 1: Muscle Identification Guide on Cadaver / Model</div>
      <table class="data-table">
        <thead>
          <tr>
            <th>Pinned Muscle</th>
            <th>How to Spot / Recognize on Cadaver</th>
            <th>Standard OSPE Viva Questions & Model Answers</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Sartorius</td>
            <td>Longest strap muscle running obliquely across anterior thigh from ASIS to medial tibia.</td>
            <td><strong>Q: Nerve Supply & Actions?</strong><br>A: Femoral nerve (L2, L3). Flexes, abducts, and laterally rotates hip; flexes knee ("tailor's position").</td>
          </tr>
          <tr>
            <td>Rectus Femoris</td>
            <td>Central bipennate muscle on anterior thigh running straight down between vastus medialis & lateralis.</td>
            <td><strong>Q: What makes it unique among quadriceps?</strong><br>A: It is the only head crossing TWO joints (originates from AIIS and groove above acetabulum). Flexes hip and extends knee.</td>
          </tr>
          <tr>
            <td>Gracilis</td>
            <td>Most superficial, thin strap muscle on the medial aspect of thigh.</td>
            <td><strong>Q: Where does it insert and what is Pes Anserinus?</strong><br>A: Inserts on upper medial shaft of tibia with Sartorius and Semitendinosus (SGS). Nerve: Obturator nerve.</td>
          </tr>
          <tr>
            <td>Adductor Longus</td>
            <td>Triangular muscle forming medial boundary of femoral triangle, originating from pubic body.</td>
            <td><strong>Q: What forms the floor of femoral triangle?</strong><br>A: Iliopsoas, Pectineus, and Adductor Longus (from lateral to medial). Nerve: Obturator (ant. division).</td>
          </tr>
          <tr>
            <td>Piriformis</td>
            <td>Pear-shaped muscle emerging from greater sciatic foramen into gluteal region.</td>
            <td><strong>Q: What structures pass above and below it?</strong><br>A: Above: Superior gluteal nerve & vessels. Below: Sciatic nerve, Inferior gluteal nerve & vessels, Pudendal nerve.</td>
          </tr>
          <tr>
            <td>Gluteus Medius</td>
            <td>Fan-shaped muscle deep to gluteus maximus, inserting into lateral greater trochanter.</td>
            <td><strong>Q: What happens if its nerve is injured?</strong><br>A: Superior gluteal nerve lesion causes <strong>Positive Trendelenburg Sign</strong> (pelvis drops on opposite swing side).</td>
          </tr>
          <tr>
            <td>Biceps Femoris</td>
            <td>Lateral hamstring muscle inserting into head of fibula.</td>
            <td><strong>Q: Nerve supply of both heads?</strong><br>A: Long head: Tibial part of Sciatic N. Short head: Common Fibular (Peroneal) part of Sciatic N.</td>
          </tr>
          <tr>
            <td>Semitendinosus</td>
            <td>Medial hamstring with long round cord-like tendon in lower half of thigh.</td>
            <td><strong>Q: Action on flexed knee?</strong><br>A: Flexes and <strong>medially rotates</strong> the flexed knee; extends hip. Nerve: Tibial division of Sciatic N.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- PRACTICAL STATION 2 -->
    <div class="content-card" style="margin-top:16px">
      <div class="subsection-title" style="color:var(--cyan)">⚡ Station 2: Pinned Neurovascular Structures</div>
      <table class="data-table">
        <thead>
          <tr>
            <th>Pinned Structure</th>
            <th>Anatomical Clue / Relation</th>
            <th>Must-Know Exam Fact</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Femoral Nerve</td>
            <td>Lies in groove between Psoas and Iliacus, lateral to femoral artery, <strong>OUTSIDE femoral sheath</strong>.</td>
            <td>Divides into anterior & posterior divisions; posterior gives <strong>Saphenous Nerve</strong> and supplies Quadriceps.</td>
          </tr>
          <tr>
            <td>Femoral Artery</td>
            <td>Enters thigh at <strong>Mid-Inguinal Point</strong> (midway between ASIS and Pubic Symphysis).</td>
            <td>Lies inside lateral compartment of femoral sheath; gives <strong>Profunda Femoris</strong> 4 cm below ligament.</td>
          </tr>
          <tr>
            <td>Femoral Vein</td>
            <td>Medial to femoral artery at base; passes posterior to artery in adductor canal.</td>
            <td>Receives <strong>Great Saphenous Vein</strong> through the Saphenous Opening (Fossa Ovalis).</td>
          </tr>
          <tr>
            <td>Sciatic Nerve</td>
            <td>Thickest nerve (2 cm), emerges below Piriformis midway between Greater Trochanter and Ischial Tuberosity.</td>
            <td>Supplies all hamstrings; divides into <strong>Tibial</strong> and <strong>Common Fibular</strong> nerves at popliteal apex.</td>
          </tr>
          <tr>
            <td>Common Fibular Nerve</td>
            <td>Runs along biceps femoris tendon, winds directly around <strong>Neck of Fibula</strong>.</td>
            <td>Most vulnerable nerve in lower limb; injury causes <strong>Foot Drop (loss of dorsiflexion & eversion)</strong>.</td>
          </tr>
          <tr>
            <td>Saphenous Nerve</td>
            <td>Accompanies femoral artery in adductor canal, then emerges with Great Saphenous Vein down medial leg.</td>
            <td>Purely sensory branch of femoral nerve; supplies medial leg and medial border of foot to ball of great toe.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- RAPID-FIRE ORAL VIVA TRAPS -->
    <div class="content-card" style="margin-top:16px">
      <div class="subsection-title" style="color:var(--purple)">🎤 Top 20 Rapid-Fire Oral Viva Traps & Professor Favorite Questions</div>
      
      <div class="two-col">
        <div>
          <div class="highlight-box blue">
            <div class="hb-title">Q1: Where do you feel the Femoral Pulse?</div>
            <strong>A:</strong> At the <strong>Mid-Inguinal Point</strong> (midway between Anterior Superior Iliac Spine and Pubic Symphysis), NOT the midpoint of the inguinal ligament!
          </div>

          <div class="highlight-box green">
            <div class="hb-title">Q2: Which nerve lies inside the Femoral Sheath?</div>
            <strong>A:</strong> <strong>Femoral branch of the Genitofemoral Nerve</strong> (in lateral compartment). The <em>Femoral Nerve</em> lies OUTSIDE the sheath!
          </div>

          <div class="highlight-box yellow">
            <div class="hb-title">Q3: Why is Femoral Hernia more common in females?</div>
            <strong>A:</strong> Due to the wider female bony pelvis, resulting in a larger femoral ring and wider femoral canal.
          </div>

          <div class="highlight-box purple">
            <div class="hb-title">Q4: What are the three muscles of Pes Anserinus?</div>
            <strong>A:</strong> <strong>SGS</strong>: <strong>S</strong>artorius (Femoral), <strong>G</strong>racilis (Obturator), <strong>S</strong>emitendinosus (Sciatic/Tibial).
          </div>

          <div class="highlight-box red">
            <div class="hb-title">Q5: Which muscle unlocks the knee joint?</div>
            <strong>A:</strong> <strong>Popliteus muscle</strong> (laterally rotates femur on fixed tibia, or medially rotates tibia on fixed femur).
          </div>
        </div>

        <div>
          <div class="highlight-box cyan">
            <div class="hb-title">Q6: What causes Trendelenburg Sign?</div>
            <strong>A:</strong> Injury to the <span class="nerve-tag">Superior Gluteal Nerve (L4, L5, S1)</span> paralyzing Gluteus Medius & Minimus on the stance side.
          </div>

          <div class="highlight-box orange">
            <div class="hb-title">Q7: What is the sensory zone of the Deep Fibular Nerve?</div>
            <strong>A:</strong> The <strong>1st Interdigital Web Space ONLY</strong> (skin of cleft between great toe and 2nd toe).
          </div>

          <div class="highlight-box purple">
            <div class="hb-title">Q8: What is the safe quadrant for gluteal IM injection?</div>
            <strong>A:</strong> The <strong>Upper Outer Quadrant</strong> (to avoid damaging the Sciatic Nerve in lower quadrants).
          </div>

          <div class="highlight-box blue">
            <div class="hb-title">Q9: What causes Foot Drop?</div>
            <strong>A:</strong> Injury to the <strong>Common Fibular (Peroneal) Nerve</strong> at the neck of the fibula, paralyzing dorsiflexors and everters.
          </div>

          <div class="highlight-box green">
            <div class="hb-title">Q10: What is Hilton's Law?</div>
            <strong>A:</strong> A nerve supplying a joint also supplies the muscles moving that joint and the skin covering their insertions. Explains knee pain from hip disease!
          </div>
        </div>
      </div>
    </div>

  </div>
</div><!-- end viva-spotting -->
"""

print("Section 9 generated successfully.")
