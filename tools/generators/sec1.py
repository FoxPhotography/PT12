# -*- coding: utf-8 -*-
"""
Module to generate Sections 1, 2, and 3 for Anatomy 2 Lower Limb.
"""

def get_section_1():
    return """
<!-- ============================================================ -->
<!-- SECTION 1: GLUTEAL REGION                                     -->
<!-- ============================================================ -->
<div class="section active" id="gluteal">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-purple">🍑</div>
      <div class="sec-title">1. Gluteal Region (Muscles, Foramina, Trendelenburg & Nerves)</div>
      <button class="translate-btn" onclick="toggleTranslation('gluteal', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="gluteal" onclick="toggleComplete('gluteal', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-gluteal">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">🍑</span>
        <span class="arabic-panel-title">شرح بالعربي — منطقة الإلية (Gluteal Region)</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p><strong>منطقة الإلية (Gluteal Region):</strong> من أهم مناطق الامتحان لأنها مليانة أسئلة مقالي وشفوي وعملي. العضلات فيها بتتقسم لطبقتين: <strong>طبقة سطحية كبيرة</strong> (Gluteus maximus, medius, minimus + Tensor fasciae latae) و<strong>طبقة عميقة بتعمل دوران للخارج</strong> (Deep lateral rotators: Piriformis, Obturator internus, Gemelli, Quadratus femoris).</p>
      <div class="ar-highlight">
        ⚡ <strong>أهم نقطة امتحان في التاريخ:</strong> عضلة <strong>Gluteus Maximus</strong> بتغذيها <span class="nerve-tag">Inferior Gluteal Nerve (L5, S1, S2)</span> وهي أقوى باسط لمفصل الحوض (Extensor) خصوصاً في طلوع السلم والقيام من وضع الجلوس. بينما <strong>Gluteus Medius & Minimus</strong> بيتغذوا بـ <span class="nerve-tag">Superior Gluteal Nerve (L4, L5, S1)</span> ودول أهم مثبتات للحوض أثناء المشي (Abductors) وعطلهم بيعمل <strong>Trendelenburg Sign</strong>!
      </div>
      <p><strong>عضلة الـ Piriformis:</strong> هي مفتاح منطقة الإلية لأنها بتقسم الثقب الوركي الكبير (Greater Sciatic Foramen) لمنطقتين: حاجات فوقها (Superior gluteal nerve & vessels) وحاجات تحتها وأهمهم <strong>Sciatic Nerve</strong> و <strong>Inferior Gluteal Nerve</strong> و <strong>Pudendal Nerve</strong>.</p>
      <p><strong>حقن العضل (IM Injection):</strong> بنقسم الإلية ٤ أرباع؛ الربع الآمن الوحيد هو <strong>العلوي الخارجي (Upper Outer Quadrant)</strong> لتجنب إصابة العصب الوركي (Sciatic Nerve) تحت، أو الأوعية العلوية جوة.</p>
    </div>

    <!-- Overview Highlights -->
    <div class="two-col">
      <div class="highlight-box purple">
        <div class="hb-title">High-Yield Muscle Rules</div>
        • <strong>Gluteus Maximus:</strong> Chief hip extensor (rising from chair, stairs) → <span class="nerve-tag">Inferior Gluteal N.</span><br>
        • <strong>Gluteus Medius & Minimus:</strong> Pelvic stabilizers / Abductors → <span class="nerve-tag">Superior Gluteal N.</span><br>
        • <strong>Key Landmark Muscle:</strong> Piriformis (key to gluteal foramina).
      </div>
      <div class="highlight-box red">
        <div class="hb-title">Clinical Red Flags</div>
        • <strong>Trendelenburg Sign:</strong> Pelvis drops on opposite unsupported side.<br>
        • <strong>IM Injection:</strong> MUST be given in <strong>Upper Outer Quadrant</strong> to avoid Sciatic Nerve injury.<br>
        • <strong>Piriformis Syndrome:</strong> Hypertrophy/spasm compresses Sciatic Nerve.
      </div>
    </div>

    <!-- ESSAY QUESTION 1 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q1</span>
        <div class="essay-title">Describe the Gluteus Maximus muscle in detail (Origin, Insertion, Nerve Supply, Actions, Bursae, and Clinical Testing).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">10 Marks</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Origin</div>
        <ul class="info-list">
          <li><strong>Outer surface of Ilium:</strong> Behind the posterior gluteal line.</li>
          <li><strong>Posterior surface of Sacrum and Coccyx.</strong></li>
          <li><strong>Sacrotuberous ligament</strong> and the overlying thoracolumbar fascia.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">2. Insertion</div>
        <ul class="info-list">
          <li><strong>Superficial 3/4 (three quarters):</strong> Inserts into the <strong>Iliotibial Tract (ITT)</strong> of the fascia lata (acting across the knee joint).</li>
          <li><strong>Deep 1/4 (one quarter):</strong> Inserts directly into the <strong>Gluteal Tuberosity</strong> of the femur (between lateral lip of linea aspera and greater trochanter).</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">3. Nerve Supply</div>
        <ul class="info-list">
          <li><span class="nerve-tag">Inferior Gluteal Nerve (L5, S1, S2)</span> — enters the muscle on its deep surface.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">4. Actions & Biomechanics</div>
        <ul class="info-list numbered">
          <li><strong>Chief Powerful Extensor of the Hip Joint:</strong> It is not used much in ordinary walking on flat ground, but is essential in <em>forceful extension</em> — rising from a sitting position, climbing stairs, running, jumping, and standing from a stoop.</li>
          <li><strong>Lateral Rotator of the Thigh</strong> at the hip joint.</li>
          <li><strong>Steadies the Pelvis on the Femoral Head:</strong> via its insertion into the iliotibial tract, it helps stabilize the extended knee joint.</li>
          <li><strong>Abduction / Adduction:</strong> Upper fibers assist abduction; lower fibers assist adduction.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">5. Related Bursae</div>
        <ul class="info-list">
          <li><strong>Trochanteric Bursa:</strong> Separates deep surface of gluteus maximus from greater trochanter (Trochanteric bursitis causes lateral hip pain).</li>
          <li><strong>Ischial Bursa:</strong> Separates gluteus maximus from ischial tuberosity (Weaver's bottom / Ischial bursitis).</li>
          <li><strong>Gluteofemoral Bursa:</strong> Separates iliotibial tract from vastus lateralis.</li>
        </ul>

        <div class="highlight-box blue" style="margin-top:14px">
          <div class="hb-title">Clinical & Practical Examination Note</div>
          <strong>To test Gluteus Maximus:</strong> Patient lies prone and raises the lower limb with the knee flexed (to eliminate hamstrings). Examiner applies resistance to posterior thigh while palpating contraction of Gluteus Maximus. In paralysis, the patient cannot rise from a chair without pushing with their arms.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 2 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q2</span>
        <div class="essay-title">Describe the Gluteus Medius and Minimus muscles (OINA) and explain their crucial role as pelvic stabilizers during the gait cycle.</div>
        <div class="essay-badges">
          <span class="badge badge-blue">High Yield</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <table class="muscle-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Gluteus Medius</th>
              <th>Gluteus Minimus</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Origin</td>
              <td>Outer surface of Ilium between anterior and posterior gluteal lines</td>
              <td>Outer surface of Ilium between anterior and inferior gluteal lines</td>
            </tr>
            <tr>
              <td>Insertion</td>
              <td>Lateral surface of the <strong>Greater Trochanter</strong> (oblique ridge)</td>
              <td>Anterior surface of the <strong>Greater Trochanter</strong></td>
            </tr>
            <tr>
              <td>Nerve Supply</td>
              <td><span class="nerve-tag">Superior Gluteal Nerve (L4, L5, S1)</span></td>
              <td><span class="nerve-tag">Superior Gluteal Nerve (L4, L5, S1)</span></td>
            </tr>
            <tr>
              <td>Main Action</td>
              <td>Primary <strong>Abductor</strong> of the hip joint; anterior fibers medially rotate</td>
              <td>Primary <strong>Abductor</strong> & <strong>Medial Rotator</strong> of the hip joint</td>
            </tr>
          </tbody>
        </table>

        <div class="highlight-box green" style="margin-top:14px">
          <div class="hb-title">Crucial Biomechanical Function During Gait (Pelvic Abductor Mechanism)</div>
          During normal walking, when one foot is lifted off the ground (<strong>Swing Phase</strong>), the body weight tends to tilt the pelvis down on the unsupported side.
          The <strong>Gluteus Medius and Minimus of the SUPPORTED limb (Stance Phase)</strong> strongly contract, pulling the ilium toward the greater trochanter, thereby preventing pelvic sag and keeping the pelvis horizontal or slightly elevated on the swing side so the foot clears the ground.
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 3 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q3</span>
        <div class="essay-title">Explain the Trendelenburg Sign and Trendelenburg Gait in detail (Definition, Mechanism, Causes, and Clinical Findings).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Viva Favorite</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Definition & Normal Mechanics</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          The <strong>Trendelenburg Test</strong> evaluates the integrity of the hip abductor mechanism (Gluteus Medius, Gluteus Minimus, and Superior Gluteal Nerve).
        </p>
        <ul class="info-list" style="margin-top:8px">
          <li><strong>Normal (Negative Sign):</strong> When standing on one leg (e.g., right leg), the abductors of that right hip contract and elevate/maintain the left (unsupported) side of the pelvis.</li>
          <li><strong>Abnormal (Positive Sign):</strong> When standing on the affected leg, the abductors FAIL to stabilize the pelvis, causing the <strong>pelvis to DROP on the opposite (normal/healthy) unsupported side</strong>.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">2. Causes of Positive Trendelenburg Sign</div>
        <ul class="info-list numbered">
          <li><strong>Neurological:</strong> Injury to the <span class="nerve-tag">Superior Gluteal Nerve (L4, L5, S1)</span> or L5 radiculopathy (polio, pelvic surgery, deep gluteal trauma).</li>
          <li><strong>Muscular:</strong> Paralysis, severe atrophy, or tear of Gluteus Medius / Minimus tendons.</li>
          <li><strong>Skeletal / Biomechanical Disruption:</strong>
            <br>• Fracture of the neck of the femur (loss of lever arm).
            <br>• Unreduced congenital/developmental dislocation of the hip (DDH).
            <br>• Coxa vara (angle of femoral neck & shaft &lt; 120° reducing abductor mechanical advantage).
            <br>• Non-union of femoral neck fracture.</li>
        </ul>

        <div class="subsection-title" style="margin-top:14px">3. Trendelenburg Gait & Duchenne Lurch</div>
        <ul class="info-list">
          <li><strong>Unilateral Trendelenburg Gait (Abductor Lurch / Duchenne Limp):</strong> The patient leans their trunk laterally toward the <em>affected</em> stance side during the stance phase to shift the center of gravity over the hip joint and balance without relying on abductors.</li>
          <li><strong>Bilateral Trendelenburg Gait (Waddling Gait / مشية البطة):</strong> Caused by bilateral abductor deficiency (e.g., bilateral DDH or muscular dystrophy). The patient rocks/waddles from side to side with every step.</li>
        </ul>
      </div>
    </div>

    <!-- ESSAY QUESTION 4 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q4</span>
        <div class="essay-title">Enumerate the structures passing through the Greater Sciatic Foramen (Above and Below Piriformis) and Lesser Sciatic Foramen.</div>
        <div class="essay-badges">
          <span class="badge badge-yellow">Top Exam Trap</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card" style="margin-bottom:0">
            <div class="subsection-title" style="color:var(--orange)">A. Greater Sciatic Foramen (GSF)</div>
            <p style="font-size:12.5px;color:var(--muted);margin-bottom:8px">Divided into two zones by the <strong>Piriformis Muscle</strong>:</p>
            
            <div style="font-size:12px;font-weight:700;color:var(--yellow);margin-bottom:6px;text-transform:uppercase">1. Structures ABOVE Piriformis:</div>
            <div class="vein-grid" style="margin-bottom:12px">
              <span class="nerve-tag">Superior Gluteal Nerve</span>
              <span class="artery-tag">Superior Gluteal Artery</span>
              <span class="vein-tag">Superior Gluteal Vein</span>
            </div>

            <div style="font-size:12px;font-weight:700;color:var(--cyan);margin-bottom:6px;text-transform:uppercase">2. Structures BELOW Piriformis:</div>
            <div class="vein-grid">
              <span class="nerve-tag">Sciatic Nerve (thickest)</span>
              <span class="nerve-tag">Inferior Gluteal Nerve</span>
              <span class="artery-tag">Inferior Gluteal Artery</span>
              <span class="vein-tag">Inferior Gluteal Vein</span>
              <span class="nerve-tag">Post. Cutaneous Nerve of Thigh</span>
              <span class="nerve-tag">Nerve to Quadratus Femoris</span>
              <span class="nerve-tag">Nerve to Obturator Internus</span>
              <span class="nerve-tag">Pudendal Nerve</span>
              <span class="artery-tag">Internal Pudendal Artery</span>
              <span class="vein-tag">Internal Pudendal Vein</span>
            </div>
          </div>

          <div class="content-card" style="margin-bottom:0">
            <div class="subsection-title" style="color:var(--green)">B. Lesser Sciatic Foramen (LSF)</div>
            <p style="font-size:12.5px;color:var(--muted);margin-bottom:8px">Acts as the gateway to the perineum / ischioanal fossa:</p>
            <ul class="info-list">
              <li><strong>Tendon of Obturator Internus muscle</strong> (emerging from pelvis).</li>
              <li><span class="nerve-tag">Nerve to Obturator Internus</span> (re-entering).</li>
              <li><span class="nerve-tag">Pudendal Nerve</span> (re-entering).</li>
              <li><span class="artery-tag">Internal Pudendal Artery</span> (re-entering).</li>
              <li><span class="vein-tag">Internal Pudendal Vein</span> (re-entering).</li>
            </ul>

            <div class="highlight-box yellow" style="margin-top:14px">
              <div class="hb-title">PIN Mnemonic Rule (Leave GSF → Enter LSF)</div>
              Structures that exit Greater Sciatic Foramen below piriformis, cross the <strong>Ischial Spine / Sacrospinous ligament</strong>, and enter Lesser Sciatic Foramen to reach the perineum:
              <br><strong>P</strong> = <strong>P</strong>udendal Nerve
              <br><strong>I</strong> = <strong>I</strong>nternal Pudendal Vessels
              <br><strong>N</strong> = <strong>N</strong>erve to Obturator Internus
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 5 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q5</span>
        <div class="essay-title">Describe the Safe Technique for Intramuscular (IM) Injections in the Gluteal Region (Quadrants, Danger Zones, and Nerve Protection).</div>
        <div class="essay-badges">
          <span class="badge badge-red">Safety / Clinical</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="subsection-title">1. Anatomical Quadrants of the Buttock</div>
        <p style="font-size:13.5px;line-height:1.7;color:var(--text)">
          The buttock is divided into <strong>four quadrants</strong> by two imaginary intersecting lines:
          <br>1. A <strong>Vertical line</strong> passing midway between the Greater Trochanter and the Ischial Tuberosity.
          <br>2. A <strong>Horizontal line</strong> passing midway between the highest point of the Iliac Crest and the lower border of the Gluteus Maximus (gluteal fold).
        </p>

        <div class="two-col" style="margin-top:12px">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--green)">The ONLY Safe Quadrant</div>
            <div class="highlight-box green">
              <div class="hb-title">Upper Outer (Anterosuperior) Quadrant</div>
              <strong>Why Safe?</strong>
              <br>• The thick muscular mass here is formed by <strong>Gluteus Medius</strong> and <strong>Gluteus Maximus</strong>.
              <br>• It is completely devoid of major neurovascular trunks.
              <br>• Needle points forward and slightly medially toward iliac bone (Ventrogluteal site between ASIS and iliac crest is also preferred).
            </div>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--red)">Danger Quadrants (Never Inject!)</div>
            <ul class="info-list">
              <li><strong>Lower Inner Quadrant:</strong> Contains the <strong>Sciatic Nerve</strong> and <strong>Pudendal Neurovascular bundle</strong> over the ischial tuberosity.</li>
              <li><strong>Lower Outer Quadrant:</strong> Contains the descending <strong>Sciatic Nerve</strong> and branches of profunda femoris.</li>
              <li><strong>Upper Inner Quadrant:</strong> Contains <strong>Superior Gluteal Nerve and Artery</strong> as they exit above piriformis.</li>
            </ul>
          </div>
        </div>

        <div class="highlight-box red">
          <div class="hb-title">Catastrophic Complications of Misplaced Injections</div>
          Injecting into lower quadrants can directly pierce or inject neurotoxic medication into the <strong>Sciatic Nerve</strong>, producing agonizing pain, complete <strong>Foot Drop</strong>, trophic ulcers on sole, and irreversible motor paralysis of all calf and foot muscles!
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 6 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q6</span>
        <div class="essay-title">Describe the Arterial Anastomoses around the Hip Joint (Cruciate Anastomosis & Trochanteric Anastomosis: vessels, locations, and surgical importance).</div>
        <div class="essay-badges">
          <span class="badge badge-purple">Arterial Supply</span>
          <div class="essay-toggle-icon">▼</div>
        </div>
      </div>
      <div class="essay-body">
        <div class="two-col">
          <div class="content-card">
            <div class="subsection-title" style="color:var(--orange)">1. Cruciate Anastomosis (Cross-shaped)</div>
            <p style="font-size:13px;color:var(--muted);margin-bottom:8px">Located at the level of the <strong>lesser trochanter</strong> in the upper posterior thigh between adductor magnus and quadratus femoris.</p>
            <ul class="info-list numbered">
              <li><strong>Superior:</strong> Descending branch of <span class="artery-tag">Inferior Gluteal Artery</span> (Internal Iliac system).</li>
              <li><strong>Inferior:</strong> Ascending branch of <span class="artery-tag">1st Perforating Artery</span> (from Profunda Femoris).</li>
              <li><strong>Lateral:</strong> Transverse branch of <span class="artery-tag">Lateral Circumflex Femoral Artery</span>.</li>
              <li><strong>Medial:</strong> Transverse branch of <span class="artery-tag">Medial Circumflex Femoral Artery</span>.</li>
            </ul>
            <div class="highlight-box blue" style="margin-top:10px">
              <strong>Clinical Importance:</strong> Establishes a vital collateral connection between <strong>Internal Iliac</strong> and <strong>External Iliac / Femoral</strong> systems if the Femoral or External Iliac artery is ligated or occluded.
            </div>
          </div>

          <div class="content-card">
            <div class="subsection-title" style="color:var(--yellow)">2. Trochanteric Anastomosis</div>
            <p style="font-size:13px;color:var(--muted);margin-bottom:8px">Located in the <strong>trochanteric fossa</strong> of the greater trochanter.</p>
            <ul class="info-list numbered">
              <li><span class="artery-tag">Superior Gluteal Artery</span> (descending branch).</li>
              <li><span class="artery-tag">Inferior Gluteal Artery</span>.</li>
              <li><span class="artery-tag">Medial Circumflex Femoral Artery</span> (ascending branch).</li>
              <li><span class="artery-tag">Lateral Circumflex Femoral Artery</span> (ascending branch).</li>
            </ul>
            <div class="highlight-box yellow" style="margin-top:10px">
              <strong>Clinical Importance:</strong> Gives off retinacular arteries that pass along the femoral neck to provide the <strong>main arterial supply to the Head and Neck of the Femur</strong>. In intracapsular femoral neck fractures, these vessels are torn, causing <strong>Avascular Necrosis (AVN)</strong> of the femoral head!
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ESSAY QUESTION 7 -->
    <div class="essay-card">
      <div class="essay-header" onclick="toggleEssay(this)">
        <span class="essay-q-tag">ESSAY Q7</span>
        <div class="essay-title">Enumerate the Deep Lateral Rotators of the Hip Joint (Origin, Insertion, Nerve Supply, and Common Function).</div>
        <div class="essay-badges">
          <span class="badge badge-cyan">Muscles</span>
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
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Piriformis</td>
              <td>Anterior surface of 2nd, 3rd, 4th sacral vertebrae</td>
              <td>Upper border of Greater Trochanter</td>
              <td><span class="nerve-tag">Anterior rami of S1, S2</span></td>
            </tr>
            <tr>
              <td>Obturator Internus</td>
              <td>Inner surface of obturator membrane & pelvic bone</td>
              <td>Medial surface of Greater Trochanter</td>
              <td><span class="nerve-tag">Nerve to Obturator Internus (L5, S1, S2)</span></td>
            </tr>
            <tr>
              <td>Superior Gemellus</td>
              <td>Ischial spine</td>
              <td>Blends with Obturator Internus tendon</td>
              <td><span class="nerve-tag">Nerve to Obturator Internus (L5, S1)</span></td>
            </tr>
            <tr>
              <td>Inferior Gemellus</td>
              <td>Upper part of Ischial tuberosity</td>
              <td>Blends with Obturator Internus tendon</td>
              <td><span class="nerve-tag">Nerve to Quadratus Femoris (L4, L5, S1)</span></td>
            </tr>
            <tr>
              <td>Quadratus Femoris</td>
              <td>Lateral border of Ischial tuberosity</td>
              <td>Quadrate tubercle on Intertrochanteric crest</td>
              <td><span class="nerve-tag">Nerve to Quadratus Femoris (L4, L5, S1)</span></td>
            </tr>
            <tr>
              <td>Obturator Externus</td>
              <td>Outer surface of obturator membrane & rami</td>
              <td>Trochanteric fossa of femur</td>
              <td><span class="nerve-tag">Obturator Nerve (Post. Division) (L3, L4)</span></td>
            </tr>
          </tbody>
        </table>
        <div class="highlight-box cyan" style="margin-top:12px">
          <strong>Common Action:</strong> Powerful <strong>Lateral (External) Rotation</strong> of the extended femur; act as "rotator cuff of the hip joint" by stabilizing the femoral head within the acetabulum during movements.
        </div>
      </div>
    </div>

  </div>
</div><!-- end gluteal -->
"""

print("Section 1 generated successfully.")
