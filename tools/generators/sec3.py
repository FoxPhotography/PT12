# -*- coding: utf-8 -*-
"""
Module to generate Section 3 (Anterior Compartment of Thigh & Adductor / Hunter's Canal)
"""

def get_section_3():
    return """
<!-- ============================================================ -->
<!-- SECTION 3: ANTERIOR COMPARTMENT & ADDUCTOR CANAL               -->
<!-- ============================================================ -->
<div class="section" id="ant-thigh">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-green">🦵</div>
      <div class="sec-title">3. Anterior Thigh Compartment & Adductor (Hunter's) Canal</div>
      <button class="translate-btn" onclick="toggleTranslation('ant-thigh', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="ant-thigh" onclick="toggleComplete('ant-thigh', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-ant-thigh">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">🦵</span>
        <span class="arabic-panel-title">شرح بالعربي — المسكن الأمامي وقناة الصياد (Hunter's Canal)</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>المسكن الأمامي للفخذ (Anterior Compartment):</strong> هو مسكن البسط (Extensor Compartment) وكل عضلاته تقريباً بتتغذى بـ <span class="nerve-tag">Femoral Nerve (L2, L3, L4)</span> وشريانه الرئيسي هو <span class="artery-tag">Femoral Artery</span>.</p>
      <div class="ar-highlight">
        ⚡ <strong>العضلات الرئيسية:</strong><br>
        1. <strong>Sartorius (عضلة الخياطين):</strong> أطول عضلة شريطية في الجسم، بتعدي على مفصلين (الحوض والركبة) وبتعمل وضعية تربع الخياط (Flexion, Abduction, Lateral rotation of hip + Flexion of knee).<br>
        2. <strong>Quadriceps Femoris (رباعية الرؤوس):</strong> أهم عضلة باسطة للركبة وتتكون من ٤ رؤوس (Rectus femoris, Vastus lateralis, Vastus medialis, Vastus intermedius).<br>
        3. <strong>Iliopsoas (العضلة الحرقفية القطنية):</strong> أقوى عاطف لمفصل الحوض (Chief Flexor of Hip).
      </div>
      <p><strong>قناة الصياد (Hunter's / Adductor Canal):</strong> نفق ليفي عضلي في الثلث الأوسط من الفخذ، بيمتد من قمة مثلث الفخذ لغاية فتحة العضلة المقربة الكبيرة (Adductor Hiatus). بيمر فيها الشريان الفخذي، الوريد الفخذي، والعصب الصافن (Saphenous Nerve).</p>
    </div>

    <!-- ESSAY QUESTION 12 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q12</span>
        <div class="essay-title">Describe the Quadriceps Femoris muscle complex in detail (The 4 heads: Origin, Common Insertion, Nerve Supply, Actions, and Patellar Tracking).</div>
        <div class="essay-badges">
          <span class="badge badge-green">Core 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. The Four Heads of Quadriceps Femoris</div>
        <table class="muscle-table">
          <thead>
            <tr>
              <th>Head</th>
              <th>Origin Details</th>
              <th>Special Anatomical Feature</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Rectus Femoris</td>
              <td><strong>Straight head:</strong> Anterior Inferior Iliac Spine (AIIS).<br><strong>Reflected head:</strong> Groove above acetabulum & hip joint capsule.</td>
              <td>Only head that crosses BOTH hip and knee joints (two-joint muscle). Bipennate fiber arrangement ("kicking muscle").</td>
            </tr>
            <tr>
              <td>Vastus Lateralis</td>
              <td>Upper intertrochanteric line, greater trochanter, gluteal tuberosity, and lateral lip of linea aspera.</td>
              <td>Largest and most powerful vastus component; covers anterolateral femur.</td>
            </tr>
            <tr>
              <td>Vastus Medialis</td>
              <td>Lower intertrochanteric line, spiral line, medial lip of linea aspera, and medial supracondylar line.</td>
              <td>Lowermost horizontal fibers (<strong>Vastus Medialis Oblique - VMO</strong>) prevent lateral subluxation/dislocation of the patella.</td>
            </tr>
            <tr>
              <td>Vastus Intermedius</td>
              <td>Upper two-thirds of anterior and lateral surfaces of the femoral shaft.</td>
              <td>Deepest head; gives off deep fibers below forming <strong>Articularis Genu</strong> (retracts suprapatellar bursa).</td>
            </tr>
          </tbody>
        </table>

        <div class="subsection-title" style="margin-top:14px">2. Common Insertion & Quadriceps Tendon</div>
        <ul class="info-list">
          <li>The 4 heads converge to form the powerful <strong>Quadriceps Tendon</strong> which inserts into the superior, lateral, and medial borders of the <strong>Patella</strong> (the largest sesamoid bone in the body).</li>
          <li>Fibers continue across the anterior surface of the patella to become the <strong>Patellar Ligament (Ligamentum Patellae)</strong>, which inserts firmly into the <strong>Tibial Tuberosity</strong>.</li>
          <li>Expansion fibers form the <strong>Medial & Lateral Patellar Retinacula</strong> reinforcing the anterior knee capsule.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">3. Nerve Supply & Actions</div>
        <ul class="info-list">
          <li><strong>Nerve Supply:</strong> <span class="nerve-tag">Femoral Nerve (L2, L3, L4 - Posterior Division)</span>.</li>
          <li><strong>Main Action:</strong> <strong>Primary and only powerful Extensor of the Knee Joint</strong> (essential for standing, walking, running, kicking, jumping).</li>
          <li><strong>Rectus Femoris:</strong> Also acts as a <strong>Flexor of the Hip Joint</strong> (especially when knee is flexed).</li>
          <li><strong>Vastus Medialis Oblique (VMO):</strong> Actively pulls patella medially during terminal extension to counter the natural lateral pull (Q-angle) of the quadriceps.</li>
        </ul>

        <div class="highlight-box green" style="margin-top:12px">
          <div class="hb-title">Clinical Testing & Reflex</div>
          <strong>Knee Jerk Reflex (Patellar Reflex - L3, L4):</strong> Tapping the patellar tendon stretches quadriceps muscle spindles → afferent signal via femoral nerve to L3-L4 spinal cord segments → efferent contraction of quadriceps extending the knee.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 13 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q13</span>
        <div class="essay-title">Describe the Sartorius muscle (Tailor's muscle: Origin, Course, Insertion, Nerve Supply, Actions, and Clinical Note).</div>
        <div class="essay-badges">
          <span class="badge badge-yellow">Classic Viva</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Origin & Course</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> <strong>Anterior Superior Iliac Spine (ASIS)</strong> and upper half of notch below it.</li>
              <li><strong>Course:</strong> Longest muscle in the human body (strap-like). Passes obliquely downwards and medially across the anterior surface of the thigh.</li>
              <li>Forms the lateral boundary of the <strong>Femoral Triangle</strong> and the roof of the <strong>Adductor Canal</strong>.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title">2. Insertion & Nerve</div>
            <ul class="info-list">
              <li><strong>Insertion:</strong> Upper part of the medial surface of the shaft of the <strong>Tibia</strong> as part of the <strong>Pes Anserinus</strong> (anterior to gracilis and semitendinosus).</li>
              <li><strong>Nerve Supply:</strong> <span class="nerve-tag">Femoral Nerve (Anterior Division) (L2, L3)</span>.</li>
            </ul>
          </div>
        </div>

        <div class="content-card" style="margin-top:8px">
          <div class="subsection-title">3. Actions ("Tailor's Position")</div>
          <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
            The Sartorius crosses two joints and produces <strong>combined movements</strong> that place the lower limb in the traditional cross-legged sitting posture of a tailor:
          </p>
          <ul class="info-list numbered" style="margin-top:8px">
            <li><strong>At the Hip Joint:</strong> Flexion, Abduction, and Lateral (External) Rotation.</li>
            <li><strong>At the Knee Joint:</strong> Flexion and Medial (Internal) Rotation of the flexed leg.</li>
          </ul>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 14 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q14</span>
        <div class="essay-title">Describe the Adductor Canal (Hunter's Canal / Subsartorial Canal) in detail (Extent, Boundaries, Contents, and Adductor Hiatus).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">High Yield 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Definition & Extent</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          The <strong>Adductor Canal (Hunter's Canal / Subsartorial Canal)</strong> is an intermuscular fascial tunnel located in the middle third of the medial aspect of the thigh.
          <br>• <strong>Starts above:</strong> At the apex of the Femoral Triangle.
          <br>• <strong>Ends below:</strong> At the <strong>Adductor Hiatus</strong> (tendinous opening in Adductor Magnus) where it opens into the Popliteal Fossa.
        </p>

        <div class="subsection-title" style="margin-top:14px">2. Boundaries (Triangular on Cross-Section)</div>
        <table class="data-table">
          <thead>
            <tr>
              <th>Wall</th>
              <th>Formed By</th>
              <th>Anatomical Details</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Anteromedial (Roof)</td>
              <td><strong>Sartorius Muscle</strong></td>
              <td>Supported by the subsartorial fascial plexus (bridge between vastus medialis and adductors).</td>
            </tr>
            <tr>
              <td>Anterolateral Wall</td>
              <td><strong>Vastus Medialis</strong></td>
              <td>Muscle belly forming lateral boundary.</td>
            </tr>
            <tr>
              <td>Posterior (Floor)</td>
              <td><strong>Adductor Longus</strong> (above) & <strong>Adductor Magnus</strong> (below)</td>
              <td>Muscular floor upon which the vessels rest.</td>
            </tr>
          </tbody>
        </table>

        <div class="subsection-title" style="margin-top:14px">3. Contents of the Adductor Canal</div>
        <div class="vein-grid" style="margin-bottom:12px">
          <span class="artery-tag">Femoral Artery</span>
          <span class="vein-tag">Femoral Vein (lies posterior/posterolateral to artery)</span>
          <span class="nerve-tag">Saphenous Nerve (crosses in front of artery from lateral to medial)</span>
          <span class="nerve-tag">Nerve to Vastus Medialis</span>
          <span class="nerve-tag">Terminal branch of Obturator Nerve (sometimes)</span>
        </div>

        <div class="highlight-box purple" style="margin-top:10px">
          <div class="hb-title">Clinical & Surgical Relevance: Adductor Canal Block</div>
          <strong>Adductor Canal Block:</strong> Local anesthetic injection into the adductor canal blocks the <strong>Saphenous Nerve</strong> and <strong>Nerve to Vastus Medialis</strong> to provide excellent sensory analgesia for total knee arthroplasty (TKA) without causing profound quadriceps motor weakness (allowing early postoperative mobilization!).
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 15 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q15</span>
        <div class="essay-title">Describe the Iliopsoas Muscle Complex (Psoas Major & Iliacus: OINA, Chief Hip Flexion, and Psoas Sign).</div>
        <div class="essay-badges">
          <span class="badge badge-cyan">Core Muscle</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <table class="muscle-table">
          <thead>
            <tr>
              <th>Component</th>
              <th>Origin</th>
              <th>Insertion</th>
              <th>Nerve Supply</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Psoas Major</td>
              <td>Sides of T12-L5 vertebral bodies, intervertebral discs, and transverse processes of L1-L5.</td>
              <td><strong>Lesser Trochanter</strong> of Femur (fuses with iliacus tendon).</td>
              <td><span class="nerve-tag">Anterior rami of L1, L2, L3</span></td>
            </tr>
            <tr>
              <td>Iliacus</td>
              <td>Upper two-thirds of Iliac Fossa, iliac crest, and ala of sacrum.</td>
              <td><strong>Lesser Trochanter</strong> of Femur (common iliopsoas tendon).</td>
              <td><span class="nerve-tag">Femoral Nerve (L2, L3)</span></td>
            </tr>
          </tbody>
        </table>

        <div class="subsection-title" style="margin-top:14px">Action & Clinical Pathology</div>
        <ul class="info-list">
          <li><strong>Chief Powerful Flexor of the Hip Joint:</strong> Essential for advancing the limb during walking, sitting up from supine position, and maintaining posture.</li>
          <li><strong>Psoas Abscess:</strong> Tuberculosis of lumbar spine (Pott's disease) tracking down within the psoas sheath into the femoral triangle below the inguinal ligament.</li>
          <li><strong>Psoas Sign (Cope's Psoas Test):</strong> Pain on passive hyperextension of right hip indicative of retrocecal acute appendicitis irritating the psoas muscle.</li>
        </ul>
      </div>
    </div>

  </div>
</div><!-- end ant-thigh -->
"""

print("Section 3 generated successfully.")
