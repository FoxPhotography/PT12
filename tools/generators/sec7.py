# -*- coding: utf-8 -*-
"""
Module to generate Section 7 (Sciatic, Tibial, Common Fibular, Deep & Superficial Fibular Nerves, Foot Drop & Dermatomes)
"""

def get_section_7():
    return """
<!-- ============================================================ -->
<!-- SECTION 7: SCIATIC, TIBIAL & FIBULAR NERVES                    -->
<!-- ============================================================ -->
<div class="section" id="sciatic-nerves">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-purple">⚡</div>
      <div class="sec-title">7. Nerves of Lower Limb: Sciatic, Tibial & Fibular Nerves</div>
      <button class="translate-btn" onclick="toggleTranslation('sciatic-nerves', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="sciatic-nerves" onclick="toggleComplete('sciatic-nerves', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-sciatic-nerves">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">⚡</span>
        <span class="arabic-panel-title">شرح بالعربي — العصب الوركي وفروعه (القصبي والشظوي وسقوط القدم)</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>العصب الوركي (Sciatic Nerve - L4, L5, S1, S2, S3):</strong> أضخم وأتخن عصب في جسم الإنسان كله (عرضه ٢ سم). بيتكون من عصبين في غلاف واحد: <strong>Tibial</strong> و <strong>Common Fibular</strong>.</p>
      <div class="ar-highlight">
        ⚡ <strong>أهم مقارنة امتحان في الطب (Foot Drop vs Calcaneovalgus):</strong><br>
        • <strong>العصب الشظوي المشترك (Common Fibular / Peroneal Nerve):</strong> بيلف حولين <strong>عنق الشظية (Neck of Fibula)</strong> وده مكان سطحي جداً ومعرض للكسر أو الضغط بالجبس. إصابته بتعمل <strong>سقوط القدم (Foot Drop)</strong> وميقدرش يرفع رجله لفوق (Loss of Dorsiflexion & Eversion) وبيمشي بمشية رفع الركبة العالية (High-Stepping Gait)!<br>
        • <strong>العصب القصبي (Tibial Nerve):</strong> بينزل ورا الركبة والساق وبيدخل باطن القدم تحت الـ Flexor Retinaculum (Tarsal Tunnel). إصابته بتلغي الثني لأسفل (Loss of Plantarflexion) وميقدرش يقف على أطراف أصابعه وبتعمل <strong>Calcaneovalgus Deformity</strong> مع فقدان الإحساس في باطن القدم كله!
      </div>
    </div>

    <!-- ESSAY QUESTION 29 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q29</span>
        <div class="essay-title">Describe the Sciatic Nerve (L4-S3) in complete detail (Origin, Components, Course in Gluteal Region and Thigh, Branches, and Termination).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">Thickest Nerve 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Origin & Components</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> <strong>Sacral Plexus</strong> (Anterior rami of L4, L5, S1, S2, S3).</li>
              <li><strong>Dimensions:</strong> Thickest nerve in the human body (approx. 2 cm width at origin).</li>
              <li><strong>Composed of two separate nerves</strong> enclosed within a single connective tissue sheath:
                <br>• <strong>Tibial Nerve Component:</strong> Formed by <em>anterior divisions</em> of L4, L5, S1, S2, S3.
                <br>• <strong>Common Fibular (Peroneal) Component:</strong> Formed by <em>posterior divisions</em> of L4, L5, S1, S2.
              </li>
            </ul>

            <div class="subsection-title" style="margin-top:12px">2. Course in Gluteal Region</div>
            <ul class="info-list">
              <li>Exits the pelvis through the <strong>Greater Sciatic Foramen BELOW the Piriformis</strong> muscle (85% normal).</li>
              <li>Curves downward and laterally, resting from above down on:
                <br>1. Ischium (posterior surface).
                <br>2. Superior Gemellus.
                <br>3. Obturator Internus tendon.
                <br>4. Inferior Gemellus.
                <br>5. Quadratus Femoris.
              </li>
              <li>Lies midway between the <strong>Greater Trochanter</strong> and <strong>Ischial Tuberosity</strong>, deep to Gluteus Maximus.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--cyan)">3. Course in Posterior Thigh & Termination</div>
            <ul class="info-list">
              <li>Enters posterior thigh at the lower border of Gluteus Maximus.</li>
              <li>Descends vertically in the midline on the posterior surface of <strong>Adductor Magnus</strong>.</li>
              <li>Crossed obliquely from medial to lateral on its superficial surface by the <strong>Long Head of Biceps Femoris</strong>.</li>
              <li><strong>Termination:</strong> Terminates at the <strong>superior angle (apex) of the Popliteal Fossa</strong> (or mid-thigh) by dividing into:
                <br>1. <span class="nerve-tag">Tibial Nerve</span> (larger medial branch).
                <br>2. <span class="nerve-tag">Common Fibular (Peroneal) Nerve</span> (smaller lateral branch).
              </li>
            </ul>

            <div class="subsection-title" style="margin-top:12px;color:var(--yellow)">4. Branches in the Thigh</div>
            <ul class="info-list">
              <li><strong>From Tibial Part (Medial side):</strong> Semitendinosus, Semimembranosus, Long head of Biceps Femoris, Ischial part of Adductor Magnus.</li>
              <li><strong>From Common Fibular Part (Lateral side):</strong> Short head of Biceps Femoris.</li>
              <li><strong>Articular:</strong> Hip joint.</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 30 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q30</span>
        <div class="essay-title">Describe the Clinical Effects of Sciatic Nerve Injury and explain Sciatica & Straight Leg Raise (SLR) Test.</div>
        <div class="essay-badges">
          <span class="badge badge-red">Clinical 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--red)">1. Complete Sciatic Nerve Lesion (Flail Foot)</div>
            <ul class="info-list">
              <li><strong>Causes:</strong> Posterior dislocation of the hip joint, fracture-dislocation of acetabulum, misplaced intramuscular gluteal injections, deep stab wounds.</li>
              <li><strong>Motor Deficits:</strong>
                <br>• Marked weakness of <strong>Knee Flexion</strong> (paralysis of hamstrings; weak flexion remains via Sartorius & Gracilis).
                <br>• <strong>Complete paralysis of ALL muscles below the knee</strong> (both anterior, lateral, and posterior compartments of leg + all intrinsic foot muscles).
              </li>
              <li><strong>Sensory Deficits:</strong>
                <br>• Complete loss of sensation of the entire leg and foot <strong>EXCEPT the medial strip of the leg and medial border of foot</strong> (which is supplied by the <strong>Saphenous Nerve</strong> from Femoral Nerve!).
              </li>
              <li><strong>Deformity:</strong> <strong>Flail / Drop Foot (Flaccid paralysis)</strong>; inability to dorsiflex or plantarflex; trophic ulcers on anesthetic sole.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">2. Sciatica (عرق النسا) & SLR Test</div>
            <p style="font-size:13px;line-height:1.6;color:var(--text)">
              <strong>Sciatica:</strong> Severe, sharp shooting pain radiating along the course of the sciatic nerve (buttock → posterior thigh → posterolateral leg → lateral foot) caused by compression of L4, L5, S1 nerve roots by:
              <br>• <strong>Herniated Lumbar Disc (L4-L5 or L5-S1)</strong>.
              <br>• <strong>Piriformis Syndrome:</strong> Spasm or hypertrophy of piriformis compressing the nerve in greater sciatic foramen.
            </p>
            <div class="highlight-box yellow" style="margin-top:10px">
              <div class="hb-title">Straight Leg Raise Test (SLR / Lasègue's Sign)</div>
              With patient supine, examiner raises the extended leg. Traction stretches the sciatic nerve roots over the herniated disc. Pain elicited between <strong>30° and 70°</strong> radiating down the leg confirms nerve root irritation!
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 31 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q31</span>
        <div class="essay-title">Describe the Common Fibular (Peroneal) Nerve (L4-S2) and explain why it is the most frequently injured nerve in the lower limb (Foot Drop & High-Stepping Gait).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Top Exam Favorite</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Course & Vulnerable Anatomical Site</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          The <strong>Common Fibular (Peroneal) Nerve (L4, L5, S1, S2)</strong> descends along the medial side of the Biceps Femoris tendon across the lateral head of Gastrocnemius, crosses the popliteus, and <strong>winds directly around the subcutaneous NECK OF THE FIBULA</strong> beneath Peroneus Longus, where it divides into the <strong>Deep Fibular</strong> and <strong>Superficial Fibular</strong> nerves.
        </p>

        <div class="highlight-box red" style="margin-top:10px">
          <div class="hb-title">Why is the Common Fibular Nerve the Most Frequently Injured Nerve in Lower Limb?</div>
          At the <strong>Neck of the Fibula</strong>, the nerve is:
          <br>1. <strong>Extremely superficial:</strong> Covered only by skin and subcutaneous fascia.
          <br>2. <strong>Directly against bone:</strong> Compresses easily against the unyielding hard fibular neck.
          <br>3. <strong>Vulnerable mechanisms:</strong> Fracture of the neck of fibula, tight plaster casts/bandages, knee dislocation, prolonged crossing of legs in bedridden/malnourished patients, lateral blow to knee.
        </div>

        <div class="subsection-title" style="margin-top:14px">2. Clinical Features of Common Fibular Nerve Lesion (Foot Drop)</div>
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">Motor Deficits & Deformity</div>
            <ul class="info-list">
              <li><strong>Paralysis of Anterior Leg Compartment:</strong> Loss of <strong>Dorsiflexion</strong> of foot and extension of toes (Deep Fibular N.).</li>
              <li><strong>Paralysis of Lateral Leg Compartment:</strong> Loss of <strong>Eversion</strong> of foot (Superficial Fibular N.).</li>
              <li><strong>Equinovarus Deformity (Foot Drop):</strong> The foot drops in <strong>Plantarflexion and Inversion</strong> due to unopposed action of calf plantarflexors (gastrocnemius/soleus) and Tibialis Posterior (supplied by intact Tibial Nerve!).</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--cyan)">Sensory Loss & Gait</div>
            <ul class="info-list">
              <li><strong>Sensory Loss:</strong> Anterolateral aspect of lower leg and <strong>entire dorsum of foot</strong> and dorsal surfaces of all toes (except 1st interdigital cleft and lateral foot border).</li>
              <li><strong>High-Stepping Gait (Cock-Walk / مشية الديك):</strong> To prevent the dropped, dragging toes from scraping on the ground during the swing phase, the patient flexes the hip and knee excessively high, slapping the foot down on the floor (slap gait).</li>
            </ul>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 32 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q32</span>
        <div class="essay-title">Compare in a detailed table between the Deep Fibular Nerve and Superficial Fibular Nerve (Course, Compartments, Motor Supply, Sensory Territory, and Isolated Testing).</div>
        <div class="essay-badges">
          <span class="badge badge-green">Comparison Table</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <table class="compare-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Deep Fibular (Anterior Tibial) Nerve</th>
              <th>Superficial Fibular (Musculocutaneous) Nerve</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Leg Compartment</td>
              <td><strong>Anterior Compartment of Leg</strong> (Extensor compartment)</td>
              <td><strong>Lateral Compartment of Leg</strong> (Peroneal compartment)</td>
            </tr>
            <tr>
              <td>Accompanied Artery</td>
              <td>Accompanies <strong>Anterior Tibial Artery</strong> and Dorsalis Pedis Artery</td>
              <td>No major artery (accompanied by small muscular branches)</td>
            </tr>
            <tr>
              <td>Muscles Innervated in Leg</td>
              <td>
                • <strong>Tibialis Anterior</strong> (chief dorsiflexor & inverter)<br>
                • <strong>Extensor Digitorum Longus (EDL)</strong><br>
                • <strong>Extensor Hallucis Longus (EHL)</strong><br>
                • <strong>Peroneus (Fibularis) Tertius</strong>
              </td>
              <td>
                • <strong>Peroneus (Fibularis) Longus</strong><br>
                • <strong>Peroneus (Fibularis) Brevis</strong>
              </td>
            </tr>
            <tr>
              <td>Muscles on Dorsum of Foot</td>
              <td><strong>Extensor Digitorum Brevis (EDB)</strong> & <strong>Extensor Hallucis Brevis</strong></td>
              <td>NONE (purely sensory on dorsum of foot)</td>
            </tr>
            <tr>
              <td>Principal Motor Action</td>
              <td><strong>Dorsiflexion of Foot</strong> and Extension of Toes</td>
              <td><strong>Eversion of Foot</strong> (stabilizes lateral longitudinal arch)</td>
            </tr>
            <tr>
              <td>Sensory Distribution (Crucial Exam Point!)</td>
              <td><strong>1st Interdigital Web Space ONLY</strong> (skin of cleft between Great Toe and 2nd Toe)</td>
              <td><strong>Lower anterior 1/3 of leg and entire Dorsum of Foot</strong> (except 1st cleft and lateral border)</td>
            </tr>
            <tr>
              <td>Specific Clinical Syndrome</td>
              <td><strong>Anterior Compartment Syndrome</strong> (Ski Boot Syndrome / deep fibular entrapment)</td>
              <td>Entrapment as it pierces deep fascia in lower third of leg</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ESSAY QUESTION 33 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q33</span>
        <div class="essay-title">Describe the Tibial Nerve (L4-S3) in complete detail (Course, Branches in Popliteal Fossa & Leg, Tarsal Tunnel, Plantar Branches, and Lesion Effects).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">Major Nerve 10M</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title">1. Course from Fossa to Sole</div>
            <ul class="info-list">
              <li><strong>Origin:</strong> Larger medial terminal branch of Sciatic Nerve (L4, L5, S1, S2, S3).</li>
              <li><strong>Popliteal Fossa:</strong> Descends vertically through the middle of the fossa (superficial to popliteal vein and artery).</li>
              <li><strong>Posterior Leg:</strong> Passes deep to the tendinous arch of <strong>Soleus</strong> to enter the posterior compartment of the leg, descending with the <strong>Posterior Tibial Artery</strong> on Tibialis Posterior.</li>
              <li><strong>Tarsal Tunnel:</strong> Passes behind the <strong>Medial Malleolus</strong> deep to the <strong>Flexor Retinaculum</strong>.</li>
              <li><strong>Termination:</strong> Divides deep to Abductor Hallucis into the <strong>Medial Plantar Nerve</strong> and <strong>Lateral Plantar Nerve</strong>.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--orange)">2. Muscular Branches</div>
            <ul class="info-list">
              <li><strong>In Popliteal Fossa:</strong> Gastrocnemius (medial & lateral heads), Plantaris, Soleus, Popliteus.</li>
              <li><strong>In Posterior Leg (Deep Flexors):</strong> Tibialis Posterior, Flexor Digitorum Longus (FDL), Flexor Hallucis Longus (FHL), and Soleus.</li>
              <li><strong>In the Sole:</strong>
                <br>• <strong>Medial Plantar Nerve:</strong> Equivalent to Median nerve of hand (supplies Abductor hallucis, FHB, FDB, 1st lumbrical + medial 3.5 digits skin).
                <br>• <strong>Lateral Plantar Nerve:</strong> Equivalent to Ulnar nerve of hand (supplies all other intrinsic sole muscles + lateral 1.5 digits skin).
              </li>
            </ul>
          </div>
        </div>

        <div class="two-col" style="margin-top:10px">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--red)">3. Clinical Effects of Tibial Nerve Lesion</div>
            <ul class="info-list">
              <li><strong>Motor Loss:</strong> Loss of <strong>Plantarflexion</strong> (cannot stand on tiptoes), loss of foot inversion (Tibialis Posterior), clawing of toes.</li>
              <li><strong>Deformity:</strong> <strong>Calcaneovalgus Deformity</strong> (foot is fixed in dorsiflexion and eversion by unopposed anterior and lateral muscles).</li>
              <li><strong>Sensory Loss:</strong> Complete anesthesia of the <strong>Sole of the Foot</strong> (predisposing to trophic pressure ulcers and neuropathic arthropathy).</li>
              <li><strong>Reflex Loss:</strong> Loss of <strong>Ankle Jerk (Achilles Reflex - S1, S2)</strong>.</li>
            </ul>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">4. Tarsal Tunnel Syndrome</div>
            <p style="font-size:13px;line-height:1.6;color:var(--text)">
              Entrapment neuropathy of the <strong>Tibial Nerve</strong> beneath the Flexor Retinaculum behind the medial malleolus.
              <br>• <strong>Symptoms:</strong> Burning pain, numbness, and tingling across the <strong>sole of the foot and toes</strong>, aggravated by prolonged walking or standing.
              <br>• <strong>Sign:</strong> Positive Tinel's sign behind the medial malleolus.
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 34 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q34</span>
        <div class="essay-title">Describe the Cutaneous Innervation and Dermatomes of the Lower Limb (Key Landmarks from L1 to S3).</div>
        <div class="essay-badges">
          <span class="badge badge-cyan">Dermatome Map</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <table class="data-table">
          <thead>
            <tr>
              <th>Spinal Root</th>
              <th>Anatomical Dermatome Landmark</th>
              <th>Clinical Sensory Testing Site</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>L1</strong></td>
              <td>Inguinal region, groin, and uppermost anterior thigh</td>
              <td>Just below inguinal ligament midway</td>
            </tr>
            <tr>
              <td><strong>L2</strong></td>
              <td>Upper anterior and lateral thigh</td>
              <td>Mid-anterior thigh</td>
            </tr>
            <tr>
              <td><strong>L3</strong></td>
              <td>Lower anterior thigh, passes across anterior knee to medial knee</td>
              <td>Medial femoral condyle / over the Patella</td>
            </tr>
            <tr>
              <td><strong>L4</strong></td>
              <td>Medial aspect of leg, <strong>Medial Malleolus</strong>, and medial side of great toe</td>
              <td>Over the <strong>Medial Malleolus</strong></td>
            </tr>
            <tr>
              <td><strong>L5</strong></td>
              <td>Anterolateral leg, <strong>Dorsum of Foot</strong>, and middle 3 toes (digits 2, 3, 4)</td>
              <td>Dorsum of foot at <strong>3rd Metatarsophalangeal joint</strong></td>
            </tr>
            <tr>
              <td><strong>S1</strong></td>
              <td><strong>Lateral border of foot</strong>, <strong>Lateral Malleolus</strong>, little toe, and posterior calf</td>
              <td>Over the <strong>Lateral Malleolus</strong> / lateral heel</td>
            </tr>
            <tr>
              <td><strong>S2</strong></td>
              <td>Posterior midline strip of thigh and popliteal fossa</td>
              <td>Center of the <strong>Popliteal Fossa</strong></td>
            </tr>
            <tr>
              <td><strong>S3, S4, S5</strong></td>
              <td>Perineum and perianal region ("saddle anesthesia")</td>
              <td>Perianal skin (Saddle area)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</div><!-- end sciatic-nerves -->
"""

print("Section 7 generated successfully.")
