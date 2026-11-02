# -*- coding: utf-8 -*-
"""
Module to generate Section 4 (Medial Thigh, Adductor Group, Pes Anserinus & Profunda Femoris)
"""

def get_section_4():
    return """
<!-- ============================================================ -->
<!-- SECTION 4: MEDIAL (ADDUCTOR) COMPARTMENT                       -->
<!-- ============================================================ -->
<div class="section" id="med-thigh">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-yellow">🧲</div>
      <div class="sec-title">4. Medial (Adductor) Compartment & Pes Anserinus</div>
      <button class="translate-btn" onclick="toggleTranslation('med-thigh', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="med-thigh" onclick="toggleComplete('med-thigh', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-med-thigh">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">🧲</span>
        <span class="arabic-panel-title">شرح بالعربي — المسكن الإنسي (المقرب) وقدم الإوزة (Pes Anserinus)</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>المسكن الإنسي للفخذ (Medial / Adductor Compartment):</strong> عضلاته كلها بتقرب الفخذ للداخل (Adduction)، وعصبها الرئيسي هو <span class="nerve-tag">Obturator Nerve (L2, L3, L4)</span> وشريانها الرئيسي هو <span class="artery-tag">Profunda Femoris Artery</span>.</p>
      <div class="ar-highlight">
        ⚡ <strong>أهم الأسئلة المقالي المضمونة في الامتحان:</strong><br>
        1. <strong>Adductor Magnus (العضلة المقربة الكبيرة):</strong> بنسميها "عضلة هجينة / مركبة (Hybrid / Composite Muscle)" لأن لها <strong>عصبين</strong> (Obturator nerve لجزء الـ Adductor + Sciatic nerve لجزء الـ Hamstring) ولها <strong>وظيفتين</strong> (تقريب وبسط للفخذ)!<br>
        2. <strong>Pes Anserinus (قدم الإوزة):</strong> ٣ أوتار لعضلات من ٣ مساكن مختلفة و٣ أعصاب مختلفة بيمسكوا في الجزء العلوي الإنسي لعظمة القصبة (Tibia):<br>
        • <strong>S</strong>artorius (<span class="nerve-tag">Femoral N.</span> - Anterior)<br>
        • <strong>G</strong>racilis (<span class="nerve-tag">Obturator N.</span> - Medial)<br>
        • <strong>S</strong>emitendinosus (<span class="nerve-tag">Sciatic N.</span> - Posterior) — اختصارهم <strong>SGS</strong>!
      </div>
    </div>

    <!-- ESSAY QUESTION 16 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q16</span>
        <div class="essay-title">Describe the Muscles of the Medial (Adductor) Compartment of the Thigh (Complete OINA Table).</div>
        <div class="essay-badges">
          <span class="badge badge-yellow">Complete Group</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <table class="muscle-table">
          <thead>
            <tr>
              <th>Muscle</th>
              <th>Origin</th>
              <th>Insertion</th>
              <th>Nerve Supply</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Adductor Longus</td>
              <td>Body of pubis (below pubic crest)</td>
              <td>Middle 1/3 of Linea Aspera of femur</td>
              <td><span class="nerve-tag">Obturator Nerve (Ant. Division) (L2, L3, L4)</span></td>
              <td>Adducts and flexes thigh at hip joint</td>
            </tr>
            <tr>
              <td>Adductor Brevis</td>
              <td>Inferior pubic ramus</td>
              <td>Pectineal line & upper part of linea aspera</td>
              <td><span class="nerve-tag">Obturator Nerve (Ant. Division) (L2, L3, L4)</span></td>
              <td>Adducts and assists flexion of hip</td>
            </tr>
            <tr>
              <td>Adductor Magnus</td>
              <td><strong>Pubic arch</strong> (ischiopubic ramus) & <strong>Ischial tuberosity</strong></td>
              <td>Gluteal tuberosity, linea aspera, supracondylar line & <strong>Adductor Tubercle</strong></td>
              <td><strong>Dual:</strong> <span class="nerve-tag">Obturator N.</span> + <span class="nerve-tag">Tibial part of Sciatic N.</span></td>
              <td>Powerful adductor & extensor of hip</td>
            </tr>
            <tr>
              <td>Gracilis</td>
              <td>Inferior pubic ramus & pubic arch</td>
              <td>Upper medial surface of shaft of <strong>Tibia</strong> (Pes Anserinus)</td>
              <td><span class="nerve-tag">Obturator Nerve (Ant. Division) (L2, L3)</span></td>
              <td>Adducts hip, flexes & medially rotates knee</td>
            </tr>
            <tr>
              <td>Pectineus</td>
              <td>Pectineal line of superior pubic ramus</td>
              <td>Pectineal line of femur (from lesser trochanter to linea aspera)</td>
              <td><span class="nerve-tag">Femoral Nerve (L2, L3)</span> + sometimes <span class="nerve-tag">Accessory Obturator / Obturator N.</span></td>
              <td>Adducts and flexes hip joint</td>
            </tr>
            <tr>
              <td>Obturator Externus</td>
              <td>Outer surface of obturator membrane & bony margins</td>
              <td><strong>Trochanteric Fossa</strong> of Femur</td>
              <td><span class="nerve-tag">Obturator Nerve (Post. Division) (L3, L4)</span></td>
              <td>Laterally rotates hip; steadies femoral head</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ESSAY QUESTION 17 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q17</span>
        <div class="essay-title">Explain why Adductor Magnus is classified as a "Composite / Hybrid" muscle (Dual Origin, Insertion, Innervation, Action, and the Adductor Hiatus).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">High Yield 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">1. Adductor (Pubic) Part</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> Inferior pubic ramus and ramus of the ischium.</li>
              <li><strong>Insertion:</strong> Medial margin of gluteal tuberosity, linea aspera, and medial supracondylar line.</li>
              <li><strong>Nerve Supply:</strong> <span class="nerve-tag">Obturator Nerve (Posterior Division) (L2, L3, L4)</span>.</li>
              <li><strong>Actions:</strong> Powerful <strong>Adduction</strong> and flexion of the hip joint.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--green)">2. Hamstring (Ischial) Part</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> <strong>Ischial Tuberosity</strong> (like true hamstrings).</li>
              <li><strong>Insertion:</strong> <strong>Adductor Tubercle</strong> of the medial condyle of femur via a rounded tendon.</li>
              <li><strong>Nerve Supply:</strong> <span class="nerve-tag">Tibial Division of Sciatic Nerve (L4)</span>.</li>
              <li><strong>Actions:</strong> Powerful <strong>Extension</strong> of the hip joint.</li>
            </ul>
          </div>
        </div>

        <div class="highlight-box purple" style="margin-top:10px">
          <div class="hb-title">The Adductor Hiatus (Hiatus Tendineus)</div>
          A large gap between the lower end of the adductor part and the insertion of the hamstring tendon into the adductor tubercle. It allows the <strong>Femoral Artery and Vein</strong> to pass from the Adductor Canal into the Popliteal Fossa, where their names change to the <strong>Popliteal Artery and Vein</strong>.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 18 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q18</span>
        <div class="essay-title">Describe the Pes Anserinus ("Goose Foot" / Guy Ropes of the Pelvis) in complete detail (Muscles, Innervation, Compartments, Functions, and Bursitis).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Viva Classic</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Definition & Anatomical Arrangement</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          The <strong>Pes Anserinus (Goose Foot)</strong> is the conjoined insertion of three long strap-like tendons onto the <strong>upper medial surface of the shaft of the Tibia</strong> (just below the medial condyle).
          <br>From anterior to posterior, the arrangement is: <strong>Sartorius → Gracilis → Semitendinosus</strong>.
        </p>

        <table class="data-table" style="margin-top:10px">
          <thead>
            <tr>
              <th>Muscle</th>
              <th>Thigh Compartment</th>
              <th>Nerve Supply</th>
              <th>Main Action</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>S</strong>artorius</td>
              <td>Anterior Compartment</td>
              <td><span class="nerve-tag">Femoral Nerve (L2, L3)</span></td>
              <td>Flexes hip & knee; abducts & rotates hip</td>
            </tr>
            <tr>
              <td><strong>G</strong>racilis</td>
              <td>Medial (Adductor) Compartment</td>
              <td><span class="nerve-tag">Obturator Nerve (L2, L3)</span></td>
              <td>Adducts hip; flexes & medially rotates knee</td>
            </tr>
            <tr>
              <td><strong>S</strong>emitendinosus</td>
              <td>Posterior (Hamstring) Compartment</td>
              <td><span class="nerve-tag">Sciatic Nerve (Tibial part) (L5, S1, S2)</span></td>
              <td>Extends hip; flexes & medially rotates knee</td>
            </tr>
          </tbody>
        </table>

        <div class="two-col" style="margin-top:12px">
          <div class="highlight-box blue">
            <div class="hb-title">Functional Role ("Guy Ropes of Pelvis")</div>
            By converging from three different pelvic origins to a single point on the tibia, these three muscles act as dynamic stabilizers ("guy ropes") to steady and balance the bony pelvis on the lower limb during locomotion.
          </div>

          <div class="highlight-box red">
            <div class="hb-title">Clinical: Pes Anserine Bursitis</div>
            The <strong>Anserine Bursa</strong> lies deep to the three tendons. Overuse (running, cycling, osteoarthritis) produces localized tenderness, swelling, and pain on the medial aspect of the knee, often misdiagnosed as a medial meniscus tear!
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 19 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q19</span>
        <div class="essay-title">Describe the Profunda Femoris Artery (Deep Artery of the Thigh: Origin, Course, Branches, and Anastomotic Contributions).</div>
        <div class="essay-badges">
          <span class="badge badge-orange">Arterial Tree</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Origin & Course</div>
        <ul class="info-list">
          <li><strong>Origin:</strong> Arises from the lateral side of the <span class="artery-tag">Femoral Artery</span> about <strong>4 cm below the Inguinal Ligament</strong> within the femoral triangle.</li>
          <li><strong>Course:</strong> Passes posteriorly and medially, descending behind the femoral vessels and Adductor Longus directly on the surface of Pectineus, Adductor Brevis, and Adductor Magnus.</li>
          <li><strong>Termination:</strong> Ends as the <strong>4th Perforating Artery</strong> piercing Adductor Magnus to reach the hamstrings.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">2. Major Branches</div>
        <ul class="info-list numbered">
          <li><span class="artery-tag">Medial Circumflex Femoral Artery (MCFA):</span> Winds around femoral neck between psoas and pectineus; gives ascending branch to <strong>Trochanteric Anastomosis</strong> and transverse branch to <strong>Cruciate Anastomosis</strong>. Principal supply to femoral head.</li>
          <li><span class="artery-tag">Lateral Circumflex Femoral Artery (LCFA):</span> Passes laterally deep to sartorius and rectus femoris; divides into:
            <br>• <strong>Ascending branch:</strong> Joins trochanteric anastomosis.
            <br>• <strong>Transverse branch:</strong> Joins cruciate anastomosis.
            <br>• <strong>Descending branch:</strong> Runs with nerve to vastus lateralis to join <strong>Genicular Anastomosis around the knee</strong>.
          </li>
          <li><span class="artery-tag">Perforating Arteries (4 Branches):</span> Pierce Adductor Magnus close to the femur to supply all the <strong>Hamstring muscles</strong> and anastomose with one another.</li>
        </ul>
      </div>
    </div>

  </div>
</div><!-- end med-thigh -->
"""

print("Section 4 generated successfully.")
