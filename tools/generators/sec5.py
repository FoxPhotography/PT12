# -*- coding: utf-8 -*-
"""
Module to generate Section 5 (Posterior Thigh, Hamstrings, Popliteal Fossa & Anastomosis)
"""

def get_section_5():
    return """
<!-- ============================================================ -->
<!-- SECTION 5: POSTERIOR COMPARTMENT & POPLITEAL FOSSA             -->
<!-- ============================================================ -->
<div class="section" id="post-thigh">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-red">🏃</div>
      <div class="sec-title">5. Posterior Thigh (Hamstrings) & Popliteal Fossa</div>
      <button class="translate-btn" onclick="toggleTranslation('post-thigh', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="post-thigh" onclick="toggleComplete('post-thigh', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-post-thigh">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">🏃</span>
        <span class="arabic-panel-title">شرح بالعربي — عضلات الهامسترينج والحفرة المأبضية (Popliteal Fossa)</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>عضلات الفخذ الخلفية (Hamstrings):</strong> بتتميز إنها عضلات بتعبر مفصلين (الحوض والركبة) وبتعمل <strong>Extension للـ Hip</strong> و <strong>Flexion للـ Knee</strong>. عشان العضلة تتسمى <em>True Hamstring</em> لازم تحقق ٤ شروط:</p>
      <div class="ar-highlight">
        📌 <strong>شروط الـ True Hamstrings:</strong><br>
        1. تطلع من <strong>Ischial Tuberosity</strong>.<br>
        2. تمسك في عظام الساق (Tibia أو Fibula).<br>
        3. تعبر مفصلين (Hip & Knee).<br>
        4. يغذيها <strong>Tibial part of Sciatic Nerve</strong>.<br>
        ⚠️ <em>ملحوظة امتحان خطيرة:</em> الرأس القصيرة لعضلة <strong>Biceps Femoris (Short Head)</strong> مش True Hamstring لأنها طالعة من الـ Linea Aspera في الفخذ وبيعصبها <span class="nerve-tag">Common Fibular (Peroneal) Nerve</span>!
      </div>
      <p><strong>الحفرة المأبضية (Popliteal Fossa):</strong> مساحة معينة الشكل خلف الركبة (Diamond-shaped). محتوياتها من السطح للعمق (ومن برة لجوة):<br>
      1. <span class="nerve-tag">Tibial Nerve</span> (السطحي وفي النص).<br>
      2. <span class="nerve-tag">Common Peroneal Nerve</span> (على الحافة الخارجية مع وتر البايسبس).<br>
      3. <span class="vein-tag">Popliteal Vein</span> (في النص في المنتصف عمقاً).<br>
      4. <span class="artery-tag">Popliteal Artery</span> (أعمق حاجة وملاصق للعظم، بنقيس منه نبض الركبة).</p>
      <p><strong>عضلة الـ Popliteus:</strong> مفتاح فك قفل مفصل الركبة (Unlocking the Knee joint) عن طريق تدوير الفخذ للخارج أو الساق للداخل في أول درجات الثني.</p>
    </div>

    <!-- ESSAY QUESTION 20 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q20</span>
        <div class="essay-title">Describe the Hamstring Muscles in detail (Definition of true hamstrings, OINA Table, and Actions on Hip and Knee).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Core 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. The 4 Criteria for a "True Hamstring Muscle"</div>
        <ul class="info-list numbered">
          <li><strong>Origin:</strong> Arises from the <strong>Ischial Tuberosity</strong> of the pelvic bone.</li>
          <li><strong>Insertion:</strong> Inserts into the <strong>Bones of the Leg</strong> (Tibia or Fibula).</li>
          <li><strong>Bi-articular Action:</strong> Crosses both the <strong>Hip Joint</strong> (extension) and <strong>Knee Joint</strong> (flexion).</li>
          <li><strong>Innervation:</strong> Supplied by the <strong>Tibial division of the Sciatic Nerve</strong>.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">2. Muscles Table</div>
        <table class="muscle-table">
          <thead>
            <tr>
              <th>Muscle</th>
              <th>Origin</th>
              <th>Insertion</th>
              <th>Nerve Supply</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Biceps Femoris (Long Head)</td>
              <td>Ischial tuberosity (common tendon with semitendinosus)</td>
              <td>Head of <strong>Fibula</strong> (lateral side, splitting around LCL)</td>
              <td><span class="nerve-tag">Tibial division of Sciatic Nerve (L5, S1, S2)</span></td>
              <td>Flexes and <strong>laterally rotates</strong> flexed knee; extends hip</td>
            </tr>
            <tr>
              <td>Biceps Femoris (Short Head)*</td>
              <td>Lateral lip of Linea Aspera & lateral supracondylar line of femur</td>
              <td>Head of <strong>Fibula</strong> (with long head tendon)</td>
              <td><span class="nerve-tag">Common Fibular (Peroneal) Nerve (L5, S1, S2)</span></td>
              <td>Flexes and laterally rotates flexed knee (acts ONLY on knee)</td>
            </tr>
            <tr>
              <td>Semitendinosus</td>
              <td>Ischial tuberosity (with long head of biceps)</td>
              <td>Upper medial shaft of <strong>Tibia</strong> (Pes Anserinus)</td>
              <td><span class="nerve-tag">Tibial division of Sciatic Nerve (L5, S1, S2)</span></td>
              <td>Flexes and <strong>medially rotates</strong> flexed knee; extends hip</td>
            </tr>
            <tr>
              <td>Semimembranosus</td>
              <td>Ischial tuberosity (upper lateral facet, membranous origin)</td>
              <td>Groove on posterior surface of <strong>Medial Condyle of Tibia</strong> (gives Oblique Popliteal Ligament)</td>
              <td><span class="nerve-tag">Tibial division of Sciatic Nerve (L5, S1, S2)</span></td>
              <td>Flexes and <strong>medially rotates</strong> flexed knee; extends hip</td>
            </tr>
            <tr>
              <td>Adductor Magnus (Ischial Part)</td>
              <td>Ischial tuberosity</td>
              <td><strong>Adductor Tubercle</strong> on medial femoral condyle</td>
              <td><span class="nerve-tag">Tibial division of Sciatic Nerve (L4)</span></td>
              <td>Modified hamstring: acts as powerful <strong>Extensor of hip</strong></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ESSAY QUESTION 21 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q21</span>
        <div class="essay-title">Explain why the Short Head of Biceps Femoris is NOT a true hamstring muscle and describe Hamstring Injuries (Pulled Hamstring).</div>
        <div class="essay-badges">
          <span class="badge badge-yellow">Clinical & Viva</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">Why Short Head of Biceps is an Exception:</div>
            <ul class="info-list">
              <li>1. <strong>Origin:</strong> Arises from the <em>femur</em> (linea aspera), NOT the ischial tuberosity.</li>
              <li>2. <strong>Joint Cross:</strong> Crosses ONLY the <em>knee joint</em>, does NOT cross the hip joint.</li>
              <li>3. <strong>Innervation:</strong> Supplied by the <span class="nerve-tag">Common Fibular (Peroneal) Nerve</span>, NOT the tibial nerve.</li>
              <li>4. Embryologically derived from the gluteal musculature.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--red)">Hamstring Strain ("Pulled Hamstring")</div>
            <p style="font-size:13px;color:var(--text);line-height:1.6">
              Extremely common in sprinters, footballers, and hurdlers during the <strong>late swing phase</strong> of sprinting (when hamstrings are decelerating the forward-moving leg with maximum eccentric tension).
              <br>• Tearing of muscle fibers (most commonly at the myotendinous junction of <strong>Biceps Femoris</strong>).
              <br>• In adolescents, forceful contraction can cause <strong>Avulsion Fracture of the Ischial Tuberosity</strong>.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 22 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q22</span>
        <div class="essay-title">Describe the Popliteal Fossa in complete detail (Boundaries, Roof, Floor, Contents arranged superficial to deep, and Clinical Examination).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">High Yield 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Diamond-Shaped Boundaries</div>
            <ul class="info-list">
              <li><strong>Superolateral:</strong> Biceps Femoris tendon.</li>
              <li><strong>Superomedial:</strong> Semimembranosus supplemented by Semitendinosus.</li>
              <li><strong>Inferolateral:</strong> Lateral head of Gastrocnemius supplemented by Plantaris.</li>
              <li><strong>Inferomedial:</strong> Medial head of Gastrocnemius.</li>
            </ul>

            <div class="subsection-title" style="margin-top:12px">2. Roof & Floor</div>
            <ul class="info-list">
              <li><strong>Roof:</strong> Deep popliteal fascia; superficial fascia contains <strong>Small Saphenous Vein</strong> and <strong>Posterior Cutaneous Nerve of Thigh</strong>.</li>
              <li><strong>Floor (From Above Downwards):</strong>
                <br>1. Popliteal surface of the femur.
                <br>2. Oblique popliteal ligament of the knee joint.
                <br>3. Popliteus muscle covered by its thick fascia.
              </li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--cyan)">3. Contents (Superficial to Deep)</div>
            <ul class="info-list numbered">
              <li><span class="nerve-tag">Tibial Nerve:</span> Most superficial, traverses vertically through center of fossa from superior to inferior angle.</li>
              <li><span class="nerve-tag">Common Fibular (Peroneal) Nerve:</span> Runs along the superolateral boundary (following biceps tendon) to wind around neck of fibula.</li>
              <li><span class="vein-tag">Popliteal Vein:</span> Lies intermediate between tibial nerve and popliteal artery; receives Small Saphenous Vein.</li>
              <li><span class="artery-tag">Popliteal Artery:</span> Deepest major structure, lying directly against the bony/ligamentous floor; gives 5 genicular branches.</li>
              <li><span class="lymph-tag">Popliteal Lymph Nodes</span> and abundant protective fat.</li>
            </ul>
          </div>
        </div>

        <div class="highlight-box blue" style="margin-top:12px">
          <div class="hb-title">Clinical Examination: Palpation of the Popliteal Pulse</div>
          Because the Popliteal Artery is the <strong>deepest structure</strong> in the fossa, palpating the popliteal pulse requires the patient to be prone (or supine with knee flexed to 45° to relax the popliteal fascia). The examiner places two hands around the knee with fingertips pressing firmly into the deep floor of the fossa against the posterior surface of the femur.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 23 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q23</span>
        <div class="essay-title">Describe the Popliteus Muscle and explain the "Locking and Unlocking Mechanism of the Knee Joint".</div>
        <div class="essay-badges">
          <span class="badge badge-green">Biomechanics / Viva</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Popliteus Muscle Anatomy</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> Deep, intracapsular groove on the lateral surface of the <strong>Lateral Condyle of the Femur</strong> and lateral meniscus.</li>
              <li><strong>Course:</strong> Passes downwards and medially, piercing the posterior knee joint capsule.</li>
              <li><strong>Insertion:</strong> Triangular area on the posterior surface of the shaft of the <strong>Tibia</strong> above the soleal line.</li>
              <li><strong>Nerve Supply:</strong> <span class="nerve-tag">Tibial Nerve (L4, L5, S1)</span>.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">2. Unlocking the Knee Joint ("Key to the Knee")</div>
            <ul class="info-list">
              <li><strong>Locking of Knee (Full Extension):</strong> At the end of full extension, the larger medial femoral condyle continues to roll backwards, causing <strong>medial rotation of the femur on the fixed tibia</strong>. This tightens all major knee ligaments, making the knee structurally stable and rigid ("screwed-home").</li>
              <li><strong>Unlocking of Knee (Initiation of Flexion):</strong> Flexion CANNOT occur until the locked joint is unlocked. The <strong>Popliteus contracts at the very start of flexion</strong>:
                <br>• <em>Weight-bearing (foot on ground):</em> Rotates the <strong>Femur Laterally</strong> on the fixed tibia.
                <br>• <em>Non-weight-bearing (foot off ground):</em> Rotates the <strong>Tibia Medially</strong> on the fixed femur.
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 24 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q24</span>
        <div class="essay-title">Describe the Anastomosis around the Knee Joint (10 contributing arteries, functional significance, and Baker's Cyst).</div>
        <div class="essay-badges">
          <span class="badge badge-orange">Arterial / Clinical</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. The 10 Arteries Forming the Genicular Anastomosis</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          A rich network of arterial arcades located around the patella, condyles of the femur, and condyles of the tibia:
        </p>
        <div class="vein-grid" style="margin-top:8px;margin-bottom:12px">
          <span class="artery-tag">1. Superior Medial Genicular (Popliteal)</span>
          <span class="artery-tag">2. Superior Lateral Genicular (Popliteal)</span>
          <span class="artery-tag">3. Inferior Medial Genicular (Popliteal)</span>
          <span class="artery-tag">4. Inferior Lateral Genicular (Popliteal)</span>
          <span class="artery-tag">5. Middle Genicular (Popliteal - pierces oblique ligament)</span>
          <span class="artery-tag">6. Descending Genicular (Femoral artery)</span>
          <span class="artery-tag">7. Descending branch of Lateral Circumflex Femoral (Profunda)</span>
          <span class="artery-tag">8. Anterior Tibial Recurrent (Anterior Tibial artery)</span>
          <span class="artery-tag">9. Posterior Tibial Recurrent (Anterior Tibial artery)</span>
          <span class="artery-tag">10. Circumflex Fibular branch (Posterior Tibial artery)</span>
        </div>

        <div class="two-col">
          <div class="highlight-box blue">
            <div class="hb-title">Functional Significance</div>
            During full knee flexion, the Popliteal Artery is compressed and kinked by the tight popliteal fascia. The genicular anastomotic network ensures continuous uninterrupted collateral blood flow to the leg and foot regardless of joint position.
          </div>

          <div class="highlight-box red">
            <div class="hb-title">Clinical: Baker's Cyst (Popliteal Cyst)</div>
            Chronic effusion in the knee joint (arthritis, meniscal tears) causes enlargement/distension of the <strong>Semimembranosus / Gastrocnemius bursa</strong> into the popliteal fossa, presenting as a fluctuant posterior swelling that can compress the popliteal vein and mimic deep vein thrombosis (DVT).
          </div>
        </div>
      </div>
    </div>

  </div>
</div><!-- end post-thigh -->
"""

print("Section 5 generated successfully.")
