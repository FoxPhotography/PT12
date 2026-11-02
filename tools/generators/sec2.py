# -*- coding: utf-8 -*-
"""
Module to generate Section 2 (Femoral Triangle, Sheath, Canal & Hernia)
"""

def get_section_2():
    return """
<!-- ============================================================ -->
<!-- SECTION 2: FEMORAL TRIANGLE & CANAL                            -->
<!-- ============================================================ -->
<div class="section" id="femoral-triangle">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-blue">📐</div>
      <div class="sec-title">2. Femoral Triangle, Sheath, Canal & Femoral Hernia</div>
      <button class="translate-btn" onclick="toggleTranslation('femoral-triangle', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="femoral-triangle" onclick="toggleComplete('femoral-triangle', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-femoral-triangle">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">📐</span>
        <span class="arabic-panel-title">شرح بالعربي — مثلث الفخذ والقناة الفخذية والفتق</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>مثلث الفخذ (Femoral Triangle):</strong> هو منطقة مثلثة الشكل في أعلى الفخذ من قدام، قاعدته لفوق والقمة لتحت.</p>
      <div class="ar-highlight">
        📌 <strong>الحدود (Boundaries):</strong><br>
        • <strong>فوق (القاعدة Base):</strong> الرباط الأربي (Inguinal Ligament).<br>
        • <strong>برة (Lateral):</strong> الحافة الإنسية لعضلة الخياطين (Medial border of Sartorius).<br>
        • <strong>جوة (Medial):</strong> الحافة الإنسية لعضلة المقربة الطويلة (Medial border of Adductor Longus).<br>
        • <strong>الأرضية (Floor):</strong> من برة لجوة: Iliopsoas ثم Pectineus ثم Adductor Longus.
      </div>
      <p><strong>ترتيب المحتويات من برة لجوة (Lateral to Medial):</strong> تذكر كلمة <strong>NAVL</strong>:</p>
      <p>1. <span class="nerve-tag">Nerve</span> (العصب الفخذي - برة الغمد).<br>
      2. <span class="artery-tag">Artery</span> (الشريان الفخذي داخل الغمد).<br>
      3. <span class="vein-tag">Vein</span> (الوريد الفخذي داخل الغمد).<br>
      4. <span class="lymph-tag">Lymphatics / Canal</span> (القناة الفخذية وبداخلها عقدة كلوكيت الليمفاوية).</p>
      <p><strong>الفتق الفخذي (Femoral Hernia):</strong> خروج جزء من الأمعاء عبر القناة الفخذية. بيحصل أكتر في <strong>الستات</strong> عشان الحوض أوسع وحلقة الفخذ أكبر، وخطورته عالية جداً إنه يحصله اختناق (Strangulation) لأن حدود الحلقة عظمية وأربطة صلبة غير قابلة للتمدد (خصوصاً الـ Lacunar ligament).</p>
    </div>

    <!-- ESSAY QUESTION 8 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q8</span>
        <div class="essay-title">Describe the Femoral Triangle in complete detail (Boundaries, Roof, Floor, Contents, and Clinical Relations).</div>
        <div class="essay-badges">
          <span class="badge badge-blue">Top Priority 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Boundaries</div>
            <ul class="info-list">
              <li><strong>Superior (Base):</strong> Inguinal Ligament (lower border folded backward from ASIS to Pubic Tubercle).</li>
              <li><strong>Lateral Boundary:</strong> Medial border of the <strong>Sartorius</strong> muscle.</li>
              <li><strong>Medial Boundary:</strong> Medial border of the <strong>Adductor Longus</strong> muscle.</li>
              <li><strong>Apex (Inferior):</strong> Point where the Sartorius crosses the Adductor Longus (continuous below with Adductor/Hunter's canal).</li>
            </ul>

            <div class="subsection-title" style="margin-top:14px">2. Roof</div>
            <ul class="info-list">
              <li>Skin and superficial fascia (containing superficial inguinal lymph nodes, great saphenous vein, superficial branches of femoral artery).</li>
              <li><strong>Cribriform Fascia</strong> (fascia pierced by Great Saphenous Vein).</li>
              <li><strong>Fascia Lata</strong> with the <strong>Saphenous Opening (Fossa Ovalis)</strong>.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title">3. Floor (Gutter-Shaped)</div>
            <p style="font-size:12.5px;color:var(--muted);margin-bottom:8px">Formed by 4 muscles (from lateral to medial):</p>
            <ul class="info-list numbered">
              <li><strong>Iliacus</strong> muscle (lateral).</li>
              <li><strong>Psoas Major</strong> tendon (lateral).</li>
              <li><strong>Pectineus</strong> muscle (intermediate).</li>
              <li><strong>Adductor Longus</strong> muscle (medial).</li>
            </ul>

            <div class="highlight-box blue" style="margin-top:12px">
              <div class="hb-title">Floor Sloping</div>
              The floor forms a deep muscular gutter where the femoral vessels lie securely supported between the pelvis and the thigh.
            </div>
          </div>
        </div>

        <div class="content-card" style="margin-top:10px">
          <div class="subsection-title">4. Contents of Femoral Triangle</div>
          <div class="vein-grid" style="margin-bottom:12px">
            <span class="artery-tag">Femoral Artery & its 3 superficial + deep branches</span>
            <span class="vein-tag">Femoral Vein & termination of Great Saphenous Vein</span>
            <span class="nerve-tag">Femoral Nerve (outside sheath)</span>
            <span class="nerve-tag">Lateral Cutaneous Nerve of Thigh (lateral angle)</span>
            <span class="nerve-tag">Femoral branch of Genitofemoral Nerve</span>
            <span class="tube-tag">Femoral Sheath</span>
            <span class="lymph-tag">Deep Inguinal Lymph Nodes (Node of Cloquet)</span>
          </div>

          <div class="highlight-box yellow">
            <div class="hb-title">NAVL Mnemonic (Arrangement at Base from Lateral to Medial)</div>
            <strong>N</strong> = <strong>N</strong>erve (Femoral Nerve - lateral, OUTSIDE the femoral sheath in groove between psoas & iliacus)<br>
            <strong>A</strong> = <strong>A</strong>rtery (Femoral Artery - inside lateral compartment of sheath)<br>
            <strong>V</strong> = <strong>V</strong>ein (Femoral Vein - inside intermediate compartment of sheath)<br>
            <strong>L</strong> = <strong>L</strong>ymphatics (Femoral Canal / Node of Cloquet - inside medial compartment)
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 9 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q9</span>
        <div class="essay-title">Describe the Femoral Sheath (Formation, Extent, and the 3 Compartments with their contents).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">Core Anatomy</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Formation & Structure</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          The <strong>Femoral Sheath</strong> is a funnel-shaped fascial prolongation of extraperitoneal abdominal fascia into the upper thigh, surrounding the femoral vessels for about <strong>2.5 cm (1 inch)</strong> below the inguinal ligament.
        </p>
        <ul class="info-list" style="margin-top:8px">
          <li><strong>Anterior Wall:</strong> Formed by downward prolongation of the <strong>Fascia Transversalis</strong>.</li>
          <li><strong>Posterior Wall:</strong> Formed by downward prolongation of the <strong>Fascia Iliaca</strong>.</li>
          <li><strong>Inferior Termination:</strong> Blends with the adventitia (tunica externa) of the femoral vessels at the lower end of the femoral triangle.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">2. The Three Compartments of the Femoral Sheath</div>
        <table class="data-table">
          <thead>
            <tr>
              <th>Compartment</th>
              <th>Position</th>
              <th>Contents</th>
              <th>Function / Clinical Note</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Lateral Compartment</td>
              <td>Most lateral</td>
              <td><span class="artery-tag">Femoral Artery</span> + <span class="nerve-tag">Femoral branch of Genitofemoral nerve</span></td>
              <td>Transmits main arterial trunk into thigh</td>
            </tr>
            <tr>
              <td>Intermediate Compartment</td>
              <td>Middle</td>
              <td><span class="vein-tag">Femoral Vein</span></td>
              <td>Transmits venous return to external iliac vein</td>
            </tr>
            <tr>
              <td>Medial Compartment (Femoral Canal)</td>
              <td>Most medial</td>
              <td>Fat, efferent lymph vessels, and <span class="lymph-tag">Deep Inguinal Lymph Node of Cloquet / Rosenmüller</span></td>
              <td>Dead space allowing femoral vein expansion during increased venous return; site of <strong>Femoral Hernia</strong></td>
            </tr>
          </tbody>
        </table>

        <div class="highlight-box red" style="margin-top:12px">
          <div class="hb-title">Crucial Exam Point: What lies OUTSIDE the Femoral Sheath?</div>
          The <strong>Femoral Nerve</strong> lies <strong>OUTSIDE (Lateral to) the Femoral Sheath</strong>, separated from the artery by the iliopsoas fascia. This is because the femoral nerve descends in the groove between Psoas and Iliacus deep to the fascia iliaca and does not enter the vascular sheath.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 10 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q10</span>
        <div class="essay-title">Describe the Femoral Canal and Femoral Ring in detail (Dimensions, Boundaries, Contents, and Mechanism of Femoral Herniation).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Surgical / Viva</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Femoral Canal Dimensions & Shape</div>
            <ul class="info-list">
              <li><strong>Shape:</strong> Small, conical medial compartment of femoral sheath.</li>
              <li><strong>Length:</strong> 1.25 cm (0.5 inch) long.</li>
              <li><strong>Base (Upper End):</strong> Open, directed toward the abdominal cavity, called the <strong>Femoral Ring</strong>.</li>
              <li><strong>Apex (Lower End):</strong> Closed, pointed downwards, ends at the saphenous opening.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">2. Boundaries of the Femoral Ring</div>
            <ul class="info-list numbered">
              <li><strong>Anterior:</strong> <span class="artery-tag">Inguinal Ligament</span>.</li>
              <li><strong>Posterior:</strong> <strong>Pectineus muscle</strong>, its covering fascia, and the <strong>Pectineal Ligament (Ligament of Cooper)</strong> on the superior pubic ramus.</li>
              <li><strong>Medial:</strong> Sharp, crescentic free margin of the <strong>Lacunar Ligament (Gimbernat's Ligament)</strong>.</li>
              <li><strong>Lateral:</strong> <strong>Femoral Vein</strong> (separated by a thin fascial septum).</li>
            </ul>
          </div>
        </div>

        <div class="content-card" style="margin-top:8px">
          <div class="subsection-title" style="color:var(--red)">3. Femoral Hernia & Strangulation Pathology</div>
          <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
            A <strong>Femoral Hernia</strong> occurs when intra-abdominal contents (loop of small bowel, omentum) protrude through the femoral ring into the femoral canal, emerging through the saphenous opening into the subcutaneous tissue of the upper anterior thigh.
          </p>
          <div class="highlight-box red" style="margin-top:10px">
            <div class="hb-title">Why is Femoral Hernia Prone to Strangulation?</div>
            <strong>3 Rigid Anatomical Reasons:</strong>
            <br>1. The boundaries of the Femoral Ring are <strong>rigid, fibrous, and unyielding</strong> (especially the sharp edge of the <strong>Lacunar Ligament</strong> medially and Inguinal ligament anteriorly).
            <br>2. The neck of the hernial sac is extremely narrow (1.25 cm).
            <br>3. When a loop of bowel enters, its venous drainage is immediately compressed against the sharp lacunar ligament, leading to rapid arterial compromise, ischemia, necrosis, and bowel gangrene (<strong>Surgical Emergency!</strong>).
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 11 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q11</span>
        <div class="essay-title">Compare in a table between Inguinal Hernia and Femoral Hernia (Anatomical position, Relation to pubic tubercle, Risk of strangulation, and Demographics).</div>
        <div class="essay-badges">
          <span class="badge badge-green">Comparison 100%</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <table class="compare-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Inguinal Hernia</th>
              <th>Femoral Hernia</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Defect / Canal</td>
              <td>Passes through <strong>Inguinal Canal</strong> (superficial / deep inguinal rings)</td>
              <td>Passes through <strong>Femoral Canal</strong> (femoral ring)</td>
            </tr>
            <tr>
              <td>Relation to Inguinal Ligament</td>
              <td>Emerges <strong>ABOVE</strong> and medial to Inguinal Ligament</td>
              <td>Emerges <strong>BELOW</strong> and lateral to Inguinal Ligament</td>
            </tr>
            <tr>
              <td>Relation to Pubic Tubercle (Gold Standard Test)</td>
              <td>Hernial neck lies <strong>ABOVE and MEDIAL</strong> to Pubic Tubercle</td>
              <td>Hernial neck lies <strong>BELOW and LATERAL</strong> to Pubic Tubercle</td>
            </tr>
            <tr>
              <td>Gender Incidence</td>
              <td>Much more common in <strong>Males</strong> (due to spermatic cord descent)</td>
              <td>Much more common in <strong>Females</strong> (wider pelvis & larger femoral canal after pregnancy)</td>
            </tr>
            <tr>
              <td>Risk of Strangulation</td>
              <td>Lower risk (inguinal ring is more yielding)</td>
              <td><strong>Extremely High Risk (up to 40%)</strong> due to sharp, rigid lacunar ligament</td>
            </tr>
            <tr>
              <td>Direction of Sac Passage</td>
              <td>Downwards and medially into scrotum / labium majus</td>
              <td>Downwards into femoral canal, forwards through saphenous opening, then turns upwards toward inguinal ligament</td>
            </tr>
            <tr>
              <td>Surgical Treatment</td>
              <td>Elective repair recommended</td>
              <td><strong>Always Urgent / Emergency surgical repair</strong> to avoid gangrene</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</div><!-- end femoral-triangle -->
"""

print("Section 2 generated successfully.")
