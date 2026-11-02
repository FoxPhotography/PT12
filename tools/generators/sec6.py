# -*- coding: utf-8 -*-
"""
Module to generate Section 6 (Femoral & Obturator Nerves, Lumbar Plexus, Saphenous, Meralgia)
"""

def get_section_6():
    return """
<!-- ============================================================ -->
<!-- SECTION 6: FEMORAL & OBTURATOR NERVES                          -->
<!-- ============================================================ -->
<div class="section" id="fem-obt-nerves">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-purple">⚡</div>
      <div class="sec-title">6. Nerves of Lower Limb: Femoral & Obturator Nerves</div>
      <button class="translate-btn" onclick="toggleTranslation('fem-obt-nerves', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="fem-obt-nerves" onclick="toggleComplete('fem-obt-nerves', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-fem-obt-nerves">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">⚡</span>
        <span class="arabic-panel-title">شرح بالعربي — العصب الفخذي (Femoral) والعصب السدادي (Obturator)</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>العصب الفخذي (Femoral Nerve - L2, L3, L4):</strong> أكبر عصب في الضفيرة القطنية (Lumbar Plexus). طالع من <em>الفروع الخلفية (Posterior divisions)</em> للجذور القطنية ٢، ٣، ٤.</p>
      <div class="ar-highlight">
        ⚡ <strong>مساره وفروعه:</strong> بينزل على الجانب الخارجي لعضلة الـ Psoas major ويدخل الفخذ تحت الرباط الأربي <strong>برة الغمد الفخذي</strong>، وبعد ٢ سم بينقسم لـ:<br>
        • <strong>Anterior Division:</strong> بيغذي Sartorius وعضلات Pectineus، وبيدي فروع حسية للجلد (Intermediate & Medial cutaneous of thigh).<br>
        • <strong>Posterior Division:</strong> بيغذي عضلات <strong>Quadriceps كاملة</strong>، وبيدي العصب الصافن <strong>Saphenous Nerve</strong> (أطول عصب حسي في الجسم بيغذي الجانب الإنسي للركبة والساق وباطن القدم لغاية الصباع الكبير).<br>
        ⚠️ <strong>قطع العصب الفخذي:</strong> شلل في Quadriceps → فقدان بسط الركبة (Loss of Knee Extension) ورجله بتخونه وهو ماشي، مع فقدان رد فعل الركبة (Lost Knee Jerk).
      </div>
      <p><strong>العصب السدادي (Obturator Nerve - L2, L3, L4):</strong> طالع من <em>الفروع الأمامية (Anterior divisions)</em> لـ L2, L3, L4. بيمشي في جدار الحوض ويدخل الفخذ عبر القناة السدادية (Obturator Canal) وبيتقسم لفرع أمامي وخلفي حولين عضلة <strong>Adductor Brevis</strong> ليغذي كل عضلات المقربة.</p>
      <p><strong>قانون هيلتون (Hilton's Law):</strong> العصب اللي بيغذي مفصل بيغذي العضلات المحركة له والجلد المغطي له. عشان كده أمراض مفصل الحوض (زي التهاب أو تآكل مفصل الفخذ) بتسمع بوجع في <strong>الركبة من جوة</strong> عن طريق العصب السدادي والعصب الفخذي!</p>
    </div>

    <!-- ESSAY QUESTION 25 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q25</span>
        <div class="essay-title">Describe the Femoral Nerve (L2, L3, L4) in complete detail (Origin, Course, Anterior and Posterior Divisions, and Full Distribution).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">Core 10M Nerve</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Origin & Root Value</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> Largest branch of the <strong>Lumbar Plexus</strong>.</li>
              <li><strong>Roots:</strong> <strong>Posterior divisions</strong> of anterior rami of <strong>L2, L3, L4</strong> spinal nerves within the substance of Psoas Major.</li>
            </ul>

            <div class="subsection-title" style="margin-top:12px">2. Course</div>
            <ul class="info-list">
              <li>Emerges from the <strong>lateral border of Psoas Major</strong>.</li>
              <li>Descends in the groove between Psoas Major and Iliacus, deep to the iliac fascia.</li>
              <li>Enters the thigh by passing behind the <strong>Inguinal Ligament</strong> (lateral to the femoral artery and <strong>OUTSIDE the femoral sheath</strong>).</li>
              <li>Approximately <strong>2.5 cm (1 inch) below the inguinal ligament</strong>, it terminates by dividing into <strong>Anterior and Posterior divisions</strong> (separated by the lateral circumflex femoral artery).</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--cyan)">3. Branches of Anterior Division</div>
            <ul class="info-list">
              <li><strong>Muscular Branches:</strong>
                <br>• Nerve to <strong>Sartorius</strong> muscle.
                <br>• Nerve to <strong>Pectineus</strong> (passes behind femoral sheath).
              </li>
              <li><strong>Cutaneous Branches:</strong>
                <br>• <strong>Intermediate Cutaneous Nerve of Thigh:</strong> Pierces fascia lata to supply skin of anterior thigh down to the knee.
                <br>• <strong>Medial Cutaneous Nerve of Thigh:</strong> Supplies skin of medial aspect of lower thigh and joins subsartorial plexus.
              </li>
            </ul>
          </div>
        </div>

        <div class="content-card" style="margin-top:10px">
          <div class="subsection-title" style="color:var(--green)">4. Branches of Posterior Division</div>
          <div class="two-col">
            <div>
              <div style="font-size:12px;font-weight:700;color:var(--yellow);margin-bottom:6px;text-transform:uppercase">Muscular (Quadriceps):</div>
              <ul class="info-list">
                <li>Nerve to <strong>Rectus Femoris</strong> (also supplies hip joint).</li>
                <li>Nerve to <strong>Vastus Lateralis</strong> (accompanies descending branch of LCFA to knee joint).</li>
                <li>Nerve to <strong>Vastus Medialis</strong> (longest muscular branch; travels in adductor canal and gives rich supply to knee joint).</li>
                <li>Nerve to <strong>Vastus Intermedius</strong> & <strong>Articularis Genu</strong>.</li>
              </ul>
            </div>

            <div>
              <div style="font-size:12px;font-weight:700;color:var(--cyan);margin-bottom:6px;text-transform:uppercase">Cutaneous & Articular:</div>
              <ul class="info-list">
                <li><span class="nerve-tag">Saphenous Nerve:</span> Largest cutaneous branch; accompanies femoral artery in adductor canal, emerges at knee between sartorius & gracilis, descends with Great Saphenous Vein down medial leg to medial side of ball of great toe.</li>
                <li><strong>Articular branches:</strong> Hip joint (from nerve to rectus femoris) and Knee joint (from nerves to vasti).</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 26 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q26</span>
        <div class="essay-title">Describe the Clinical Effects of Femoral Nerve Injury / Lesion (Motor Deficits, Sensory Loss, Reflex Loss, and Gait Abnormalities).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Clinical 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">1. Motor Deficits</div>
            <ul class="info-list">
              <li><strong>Paralysis of Quadriceps Femoris:</strong> Complete loss of active <strong>Knee Extension</strong>.</li>
              <li><strong>Weakness of Hip Flexion:</strong> Due to paralysis of Rectus Femoris, Sartorius, and Pectineus (Iliopsoas remains functional if lesion is below inguinal ligament).</li>
              <li><strong>Unstable Knee ("Giving Way" / Buckling):</strong> The patient cannot lock the knee into extension during the stance phase of walking and is unable to climb stairs, jump, or run.</li>
            </ul>

            <div class="subsection-title" style="margin-top:12px;color:var(--red)">2. Reflex Loss</div>
            <ul class="info-list">
              <li><strong>Loss of Patellar Reflex (Knee Jerk Reflex - L3, L4):</strong> Absence of reflex knee extension on tapping patellar tendon.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--cyan)">3. Sensory Deficits</div>
            <ul class="info-list">
              <li>Loss of sensation over the <strong>anterior and medial surfaces of the thigh</strong> (Intermediate and Medial cutaneous nerves).</li>
              <li>Loss of sensation over the <strong>medial side of the knee, medial side of the leg, and medial border of the foot</strong> up to the base of the great toe (Saphenous Nerve territory).</li>
            </ul>

            <div class="subsection-title" style="margin-top:12px;color:var(--green)">4. Characteristic Compensatory Gait</div>
            <p style="font-size:13px;line-height:1.6;color:var(--text)">
              To walk without falling, the patient walks with the knee kept passively in <strong>hyperextension (genu recurvatum)</strong> by pushing the thigh backward with their hand or leaning forward, avoiding any knee flexion during stance.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 27 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q27</span>
        <div class="essay-title">Describe the Obturator Nerve (L2, L3, L4) in detail (Origin, Pelvic Course, Anterior and Posterior Divisions, Distribution, and Clinical Lesion).</div>
        <div class="essay-badges">
          <span class="badge badge-yellow">Core Nerve</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Origin & Course</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> <strong>Anterior divisions</strong> of anterior rami of <strong>L2, L3, L4</strong> spinal nerves (Lumbar Plexus).</li>
              <li><strong>Pelvic Course:</strong> Emerges from the <em>medial border</em> of Psoas Major, crosses pelvic brim into pelvis minor, runs along lateral pelvic wall above obturator vessels.</li>
              <li><strong>Exit:</strong> Enters thigh through the <strong>Obturator Canal</strong> in the obturator membrane, where it immediately divides into Anterior and Posterior divisions around <strong>Adductor Brevis</strong>.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--orange)">2. The Two Divisions & Distribution</div>
            <ul class="info-list">
              <li><strong>Anterior Division (in front of Adductor Brevis):</strong>
                <br>• <em>Muscular:</em> Adductor Longus, Adductor Brevis, Gracilis, and sometimes Pectineus.
                <br>• <em>Cutaneous:</em> Small sensory patch on <strong>medial aspect of middle thigh</strong>.
                <br>• <em>Articular:</em> Supplies <strong>Hip Joint</strong>.
              </li>
              <li><strong>Posterior Division (behind Adductor Brevis):</strong>
                <br>• Pierces Obturator Externus.
                <br>• <em>Muscular:</em> <strong>Obturator Externus</strong> and <strong>Adductor part of Adductor Magnus</strong>.
                <br>• <em>Articular:</em> Descends through adductor hiatus to supply <strong>Knee Joint</strong>.
              </li>
            </ul>
          </div>
        </div>

        <div class="highlight-box red" style="margin-top:10px">
          <div class="hb-title">Clinical: Obturator Nerve Lesion & Scissor Gait</div>
          <strong>Injury:</strong> During pelvic surgery, anterior hip dislocation, or obturator hernia.
          <br>• <strong>Motor Loss:</strong> Severe weakness of <strong>Thigh Adduction</strong>.
          <br>• <strong>Gait:</strong> In bilateral involvement, spastic adduction (e.g. cerebral palsy) produces a <strong>Scissor Gait (مشية المقص)</strong> where knees rub together.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 28 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q28</span>
        <div class="essay-title">Explain Hilton's Law and describe Meralgia Paresthetica (Lateral Cutaneous Nerve of Thigh entrapment).</div>
        <div class="essay-badges">
          <span class="badge badge-cyan">Viva Concepts</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">1. Hilton's Law (Referred Pain Mechanism)</div>
            <div class="highlight-box yellow">
              <strong>Statement of Hilton's Law:</strong>
              "The nerve supplying a joint also supplies the muscles that move that joint and the skin over the insertions of those muscles."
            </div>
            <p style="font-size:13px;line-height:1.6;color:var(--text);margin-top:8px">
              <strong>Application in Lower Limb:</strong>
              Both the <strong>Femoral Nerve</strong> and <strong>Obturator Nerve</strong> send articular branches to BOTH the <strong>Hip Joint</strong> and the <strong>Knee Joint</strong>.
              <br>• Therefore, disease of the hip joint (e.g., pediatric Perthes disease, septic arthritis, slipped capital femoral epiphysis, osteoarthritis) frequently presents clinically as <strong>isolated pain in the medial knee</strong>!
            </p>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--red)">2. Meralgia Paresthetica (Bernhardt-Roth Syndrome)</div>
            <ul class="info-list">
              <li><strong>Nerve Involved:</strong> <span class="nerve-tag">Lateral Cutaneous Nerve of Thigh (L2, L3)</span> (purely sensory nerve).</li>
              <li><strong>Site of Entrapment:</strong> As it passes under or through the <strong>lateral attachment of the Inguinal Ligament</strong> near the ASIS.</li>
              <li><strong>Causes:</strong> Tight belts, tool belts, obesity, pregnancy, prolonged standing.</li>
              <li><strong>Symptoms:</strong> Burning pain, numbness, tingling, and paresthesia over the <strong>anterolateral aspect of the thigh</strong> (NO motor deficit).</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

  </div>
</div><!-- end fem-obt-nerves -->
"""

print("Section 6 generated successfully.")
