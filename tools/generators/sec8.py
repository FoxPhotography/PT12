# -*- coding: utf-8 -*-
"""
Module to generate Section 8 (Master Comparison Tables & High-Yield Clinical Pearls)
"""

def get_section_8():
    return """
<!-- ============================================================ -->
<!-- SECTION 8: COMPARISONS & CLINICAL PEARLS                       -->
<!-- ============================================================ -->
<div class="section" id="comparisons">

  <div class="topic-group">
    <div class="sec-header">
      <div class="sec-icon ic-green">📊</div>
      <div class="sec-title">8. Master Comparison Tables & Clinical Syndromes</div>
      <button class="translate-btn" onclick="toggleTranslation('comparisons', this)" title="شرح بالعربي">🌐 <span class="btn-label">عربي</span></button>
      <button class="sec-complete-btn" data-section="comparisons" onclick="toggleComplete('comparisons', this)">☐ تم المذاكرة</button>
    </div>

    <div class="arabic-panel" id="arabic-comparisons">
      <div class="arabic-panel-header">
        <span class="arabic-panel-icon">📊</span>
        <span class="arabic-panel-title">شرح بالعربي — جداول المقارنات الشاملة والمتلازمات الإكلينيكية</span>
        <span class="arabic-panel-badge">Arabic</span>
      </div>
      <p>هذا القسم يجمع لك <strong>أقوى جداول المقارنات</strong> اللي بيسألها الدكاترة في امتحانات الشفوي والتحريري والفاينال في صفحة واحدة للمراجعة السريعة قبل الامتحان مباشرة.</p>
    </div>

    <!-- COMPARISON 1 -->
    <div class="content-card">
      <div class="subsection-title">Comparison 1: The Three Compartments of the Thigh</div>
      <table class="compare-table">
        <thead>
          <tr>
            <th>Feature</th>
            <th>Anterior (Extensor)</th>
            <th>Medial (Adductor)</th>
            <th>Posterior (Hamstrings)</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>Main Muscles</td>
            <td>Quadriceps femoris, Sartorius, Iliopsoas, Pectineus</td>
            <td>Adductor longus, brevis, magnus (adductor part), Gracilis, Obturator externus</td>
            <td>Biceps femoris, Semitendinosus, Semimembranosus, Adductor magnus (ischial part)</td>
          </tr>
          <tr>
            <td>Main Nerve Supply</td>
            <td><span class="nerve-tag">Femoral Nerve (L2, L3, L4)</span></td>
            <td><span class="nerve-tag">Obturator Nerve (L2, L3, L4)</span></td>
            <td><span class="nerve-tag">Sciatic Nerve (Tibial Part) (L4-S3)</span></td>
          </tr>
          <tr>
            <td>Main Arterial Supply</td>
            <td><span class="artery-tag">Femoral Artery</span></td>
            <td><span class="artery-tag">Profunda Femoris & Obturator Artery</span></td>
            <td><span class="artery-tag">Perforating branches of Profunda Femoris</span></td>
          </tr>
          <tr>
            <td>Primary Joint Action</td>
            <td><strong>Extension of Knee</strong> & Flexion of Hip</td>
            <td><strong>Adduction of Hip</strong></td>
            <td><strong>Flexion of Knee</strong> & Extension of Hip</td>
          </tr>
          <tr>
            <td>Reflex Tested</td>
            <td><strong>Patellar Reflex (Knee Jerk - L3, L4)</strong></td>
            <td>Adductor Reflex (L2, L3)</td>
            <td>Hamstring Reflex (L5, S1)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- COMPARISON 2 -->
    <div class="content-card">
      <div class="subsection-title">Comparison 2: Nerve Lesions of the Lower Limb Summary</div>
      <table class="data-table">
        <thead>
          <tr>
            <th>Nerve & Roots</th>
            <th>Vulnerable Site / Cause</th>
            <th>Motor Loss</th>
            <th>Sensory Loss</th>
            <th>Characteristic Deformity & Gait</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Femoral Nerve</strong><br>(L2, L3, L4)</td>
            <td>Pelvic fracture, retroperitoneal hematoma, catheterization</td>
            <td>Loss of <strong>Knee Extension</strong> (Quadriceps); weak hip flexion</td>
            <td>Anterior & medial thigh; medial leg & foot (Saphenous)</td>
            <td><strong>Knee Buckling</strong>; loss of knee jerk; walks with knee in hyperextension</td>
          </tr>
          <tr>
            <td><strong>Obturator Nerve</strong><br>(L2, L3, L4)</td>
            <td>Pelvic surgery, anterior hip dislocation, obturator hernia</td>
            <td>Loss of <strong>Thigh Adduction</strong></td>
            <td>Small patch on medial mid-thigh</td>
            <td>Unstable lateral swing; <strong>Scissor Gait</strong> if bilateral spasticity</td>
          </tr>
          <tr>
            <td><strong>Superior Gluteal Nerve</strong><br>(L4, L5, S1)</td>
            <td>Posterior hip surgery, intramuscular injection, polio</td>
            <td>Paralysis of <strong>Gluteus Medius & Minimus</strong> (Abductors)</td>
            <td>NO sensory loss (purely motor!)</td>
            <td><strong>Positive Trendelenburg Sign</strong>; Duchenne lurch / Waddling gait</td>
          </tr>
          <tr>
            <td><strong>Inferior Gluteal Nerve</strong><br>(L5, S1, S2)</td>
            <td>Posterior hip dislocation, surgical approach to hip</td>
            <td>Paralysis of <strong>Gluteus Maximus</strong></td>
            <td>NO sensory loss (purely motor!)</td>
            <td>Inability to rise from chair or climb stairs without using hands; backward trunk lurch at heel-strike</td>
          </tr>
          <tr>
            <td><strong>Sciatic Nerve</strong><br>(L4-S3)</td>
            <td>Posterior hip dislocation, misplaced IM gluteal injection</td>
            <td>Weak knee flexion; paralysis of ALL leg and foot muscles</td>
            <td>Entire leg/foot except medial strip (Saphenous intact)</td>
            <td><strong>Flail Foot / Foot Drop</strong>; High-stepping gait; trophic ulcers on sole</td>
          </tr>
          <tr>
            <td><strong>Common Fibular Nerve</strong><br>(L4-S2)</td>
            <td>Fracture <strong>neck of fibula</strong>, tight casts, leg crossing</td>
            <td>Loss of <strong>Dorsiflexion</strong> & <strong>Eversion</strong> of foot</td>
            <td>Anterolateral leg & entire dorsum of foot</td>
            <td><strong>Foot Drop (Equinovarus)</strong>; <strong>High-Stepping Gait</strong> (slap gait)</td>
          </tr>
          <tr>
            <td><strong>Tibial Nerve</strong><br>(L4-S3)</td>
            <td>Popliteal fossa trauma, <strong>Tarsal Tunnel</strong> compression</td>
            <td>Loss of <strong>Plantarflexion</strong> & Inversion; intrinsic sole muscles</td>
            <td>Entire <strong>Sole of the Foot</strong> (anesthesia)</td>
            <td><strong>Calcaneovalgus Deformity</strong>; inability to stand on tiptoes; loss of ankle jerk</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- COMPARISON 3 -->
    <div class="two-col">
      <div class="content-card">
        <div class="subsection-title">Comparison 3: Greater vs Lesser Sciatic Foramen</div>
        <table class="compare-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Greater Sciatic Foramen</th>
              <th>Lesser Sciatic Foramen</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Role</td>
              <td>Gateway from <strong>Pelvis to Gluteal Region</strong></td>
              <td>Gateway from <strong>Gluteal Region to Perineum</strong></td>
            </tr>
            <tr>
              <td>Key Muscle</td>
              <td>Transmits <strong>Piriformis</strong> muscle</td>
              <td>Transmits <strong>Obturator Internus</strong> tendon</td>
            </tr>
            <tr>
              <td>Major Nerve</td>
              <td><strong>Sciatic Nerve</strong> (exits below piriformis)</td>
              <td><strong>Pudendal Nerve</strong> (re-enters pelvis to perineum)</td>
            </tr>
            <tr>
              <td>Shared Vessels</td>
              <td>Internal Pudendal artery exits</td>
              <td>Internal Pudendal artery re-enters</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="content-card">
        <div class="subsection-title">Comparison 4: Cruciate vs Trochanteric Anastomosis</div>
        <table class="compare-table">
          <thead>
            <tr>
              <th>Feature</th>
              <th>Cruciate Anastomosis</th>
              <th>Trochanteric Anastomosis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Location</td>
              <td>Level of <strong>Lesser Trochanter</strong> (posterior thigh)</td>
              <td>In <strong>Trochanteric Fossa</strong> of Greater Trochanter</td>
            </tr>
            <tr>
              <td>Vessels Involved</td>
              <td>Inferior Gluteal + 1st Perforating + Transverse LCFA + Transverse MCFA</td>
              <td>Superior Gluteal + Inferior Gluteal + Ascending MCFA + Ascending LCFA</td>
            </tr>
            <tr>
              <td>Clinical Importance</td>
              <td>Bypass if <strong>Femoral / External Iliac</strong> artery is occluded</td>
              <td><strong>Main blood supply to Head and Neck of Femur</strong> (prevents Avascular Necrosis)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

  </div>
</div><!-- end comparisons -->
"""

print("Section 8 generated successfully.")
