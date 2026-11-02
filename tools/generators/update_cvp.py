# -*- coding: utf-8 -*-
import os

target_file = r'd:\Coding\PT12\Midterm\cvp_midterm.html'

with open(target_file, 'r', encoding='utf-8') as f:
    text = f.read()

hospital_addon = '''
  <!-- BEDSIDE CLINICAL MASTERCLASS -->
  <div class="guide-section">
    <div class="guide-title">
      <div class="guide-emoji">💬</div>
      <div class="guide-heading">سيناريو الحوار العملي مع المريض في العنبر (Word-by-Word Bedside Script)</div>
      <div class="guide-badge">Clinical Script</div>
    </div>

    <div class="info-card success">
      <div class="card-tag">1️⃣ كسر الجليد والتعريف بالنفس (Opening Rapport)</div>
      <div class="card-body">
        <strong>أنت:</strong> <em>"السلام عليكم يا حاج، ألف سلامة عليك. أنا دكتور علاج طبيعي، جاي أطمن على حضرتك وأفحص الصدر والتنفس عشان نساعد حضرتك ترتاح ونتعافى بسرعة بإذن الله. تسمحلي بدقايق؟"</em><br>
        <strong>المريض:</strong> <em>"اتفضل يا دكتور الله يسلمك."</em><br>
        <strong>📌 تنبيه ذهبي:</strong> بص فوراً على إسورة اليد (ID Band) أو تذكرة السرير، واطلب من المريض يؤكد اسمه وسنه بهدوء للتأكد من هويته ومطابقة الملف.
      </div>
    </div>

    <div class="info-card info">
      <div class="card-tag">2️⃣ الشكوى الرئيسية (Chief Complaint Script)</div>
      <div class="card-body">
        <strong>أنت:</strong> <em>"خير يا والدي، إيه أكتر حاجة تعباك ومضايقاك وجابتك المستشفى هنا؟"</em><br>
        <strong>المريض:</strong> <em>"صدري كابس عليا ومش قادر أتنفس من 4 أيام، وبكح بلغم أصفر كتير."</em><br>
        <strong>✔️ كيف تدونها بالشيت:</strong> <code style="color:#34d399">"Shortness of breath and productive cough for 4 days"</code><br>
        <span style="color:#f87171">❌ أوعى تكتب تشخيص</span> مثل: "COPD Exacerbation" في خانة الشكوى الرئيسية! الشكوى بكلمات المريض نفسه + المدة فقط.
      </div>
    </div>

    <div class="info-card purple">
      <div class="card-tag">3️⃣ تفكيك أعراض النهجان والكحة والألم (Detailed Probing)</div>
      <div class="card-body">
        <ul class="step-list">
          <li><div class="step-num">A</div><div><strong>فحص النهجان والـ Orthopnea:</strong> <em>"النهجان ده بيجيلك وأنت نايم مستريح ولا لما تقوم تمشي وتروح الحمام؟ بتنام على كام مخدة؟ لو شيلنا المخدات ونمت مسطح تحس إنك هتتخنق؟ بتصحى بالليل مفزوع تجري تفتح الشباك تاخد هوا؟"</em> (PND & Orthopnea = Heart Failure).</div></li>
          <li><div class="step-num">B</div><div><strong>فحص البلغم (Sputum):</strong> <em>"البلغم لونه إيه؟ أبيض شفاف ولا أصفر ولا مخضر؟ كميته قد فنجان قهوة ولا ملعقة؟ نزل معاه أي خيوط دم أو نقط حمرة؟"</em></div></li>
          <li><div class="step-num">C</div><div><strong>فحص ألم الصدر (Chest Pain):</strong> <em>"الوجع اللي حاسس بيه في صدرك طبيعته إيه؟ تقل وحجر على صدرك بيسمع في كتفك الشمال ورقبتك؟ ولا نغزة زي الدبوس بتزيد لما تاخد نفس عميق أو تكح؟"</em> (Pleuritic vs Ischemic).</div></li>
          <li><div class="step-num">D</div><div><strong>فحص التدخين (Smoking History):</strong> <em>"بتدخن يا حاج؟ بتشرب سجاير ولا معسل وشيشة؟ كام سيجارة أو علبة في اليوم تقريباً؟ وبقالك كام سنة بتدخن؟"</em> → احسب الـ <code>Pack-Years</code> والـ <code>Smoking Index</code> فوراً.</div></li>
        </ul>
      </div>
    </div>
  </div>

  <!-- RAPID PHYSICAL SIGNS & BEDSIDE DIFFERENTIATION -->
  <div class="guide-section">
    <div class="guide-title">
      <div class="guide-emoji">🩺</div>
      <div class="guide-heading">فحص الأطراف والرقبة السريع (Bedside Physical Signs)</div>
      <div class="guide-badge">Must-Know Signs</div>
    </div>

    <div class="info-card warn">
      <div class="card-tag">تعجر الأصابع — Digital Clubbing (شامروث وفخ الشفوي)</div>
      <div class="card-body">
        <strong>1. اختبار شامروث (Schamroth's Window Test):</strong> خلّي العيان يقرّب ضفرين السبابتين لبعض بظهرهم. في الوضع الطبيعي فيه فراغ معين صغير بين الضوافر (Diamond-shaped window). في الـ Clubbing <strong>يختفي هذا الفراغ تماماً</strong>.<br>
        <strong>2. زاوية لوفيبوند (Lovibond angle):</strong> زاوية اتصال الظفر بجلد الإصبع تتخطى <strong>&gt; 180°</strong>.<br>
        <strong>3. أشهر الأسباب:</strong>
        <div class="pills" style="margin-top:6px">
          <span class="pill pill-red">Suppurative lung (Bronchiectasis / Lung Abscess / Empyema)</span>
          <span class="pill pill-red">Bronchogenic Carcinoma (ورم الرئة الخبيث)</span>
          <span class="pill pill-orange">Idiopathic Pulmonary Fibrosis</span>
          <span class="pill pill-blue">Cyanotic Congenital Heart Disease / Infective Endocarditis</span>
        </div>
        <br>
        <div style="background:rgba(239,68,68,0.1);border-right:3px solid #ef4444;padding:8px 12px;border-radius:4px;margin-top:8px;">
          <strong>⚠️ فخ الشفوي القاتل:</strong> <em>"هل مريض الـ COPD بيجيله Clubbing؟"</em><br>
          <strong>الإجابة النموذجية:</strong> <span style="color:#fca5a5"><strong>لا! الـ COPD البسيط لا يسبب Clubbing مطلقاً.</strong> لو شفت مريض COPD وعنده Clubbing لازم تبحث فوراً عن <strong>Bronchogenic Carcinoma</strong> (سرطان رئة مضاعف للتدخين) أو <strong>Bronchiectasis</strong>!</span>
        </div>
      </div>
    </div>

    <div class="info-card info">
      <div class="card-tag">الزرقة — Central vs. Peripheral Cyanosis</div>
      <div class="card-body">
        <table class="data-table">
          <thead><tr><th>وجه المقارنة</th><th>Central Cyanosis (زرقة مركزية)</th><th>Peripheral Cyanosis (زرقة طرفية)</th></tr></thead>
          <tbody>
            <tr><td><strong>الأماكن</strong></td><td>الشفتين، اللسان، الغشاء المخاطي الداخلي للفم</td><td>الأصابع، الأظافر، شحمة الأذن، الأنف</td></tr>
            <tr><td><strong>حرارة الأطراف</strong></td><td class="ok">الأطراف دافئة (Warm)</td><td class="bad">الأطراف باردة ومثلجة (Cold)</td></tr>
            <tr><td><strong>التأثر بالتدفئة/المساج</strong></td><td>لا تتحسن بالتدفئة</td><td>تتحسن وتختفي بالتدفئة والمساج</td></tr>
            <tr><td><strong>السبب الرئيسي</strong></td><td>نقص أكسجين الدم الشرياني الشديد (PaO₂ &lt; 85%) نتيجة أمراض رئة متقدمة أو Right-to-Left Shunt</td><td>بطء سريان الدم وركوده في الأطراف، انخفاض حرارة الجو، Shock، Heart Failure</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="info-card purple">
      <div class="card-tag">مقارنة كحة الدم (Hemoptysis) وترجيع الدم (Hematemesis)</div>
      <div class="card-body">
        <table class="data-table">
          <thead><tr><th>المعيار</th><th>Hemoptysis (كحة دم)</th><th>Hematemesis (ترجيع دم)</th></tr></thead>
          <tbody>
            <tr><td><strong>المصدر</strong></td><td>الجهاز التنفسي (Respiratory tract)</td><td>الجهاز الهضمي (GI tract)</td></tr>
            <tr><td><strong>الشكل واللون</strong></td><td class="hl">أحمر فاتح (Bright red)، رغوي (Frothy) وفيه فقاعات هواء</td><td class="bad">أحمر داكن / بني زي تفل القهوة (Coffee-ground) ممزوج بطعام</td></tr>
            <tr><td><strong>الحموضة (pH)</strong></td><td class="ok">قلوي (Alkaline pH)</td><td>حمضي (Acidic pH بفعل حمض المعدة)</td></tr>
            <tr><td><strong>الأعراض السابقة</strong></td><td>دغدغة في الحلق، كحة شديدة، ضيق تنفس</td><td>غثيان، ألم بالمعدة، قيء</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="info-card success">
      <div class="card-tag">مقارنة ألم القلب (Cardiac) وألم الغشاء البلوري (Pleuritic)</div>
      <div class="card-body">
        <table class="data-table">
          <thead><tr><th>المعيار</th><th>Cardiac Pain (Angina / MI)</th><th>Pleuritic Chest Pain</th></tr></thead>
          <tbody>
            <tr><td><strong>الموقع</strong></td><td>خلف عظمة القص في المنتصف (Retrosternal) غير محدد بإصبع</td><td>جانبي محدد وموضعي (Localized) العيان يشير عليه بصباعه</td></tr>
            <tr><td><strong>طبيعة الألم</strong></td><td>ثقل ضاغط كالحجر، عصر، حرقان (Crushing / Heaviness)</td><td>نغزات حادة زي السكاكين أو الدبابيس (Sharp / Stabbing)</td></tr>
            <tr><td><strong>التسميع (Radiation)</strong></td><td>يسمع للكتف والذراع الأيسر، الفك السفلي، والرقبة</td><td>لا يسمع، أو يسمع لقمة الكتف فقط لو الحجاب الحاجز ملتهب</td></tr>
            <tr><td><strong>ما يزيده وما يريحه</strong></td><td>يزيد بالمجهود والضغط العصبي؛ يقل بالراحة وأقراص تحت اللسان Nitroglycerin</td><td><strong>يزيد جداً مع الكحة والشهيق العميق</strong>؛ يقل بالنوم على الجنب المصاب أو كتم النفس</td></tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
'''

sec1_addon = '''
    <div class="info-card info">
      <div class="card-tag">💓 Pulse & Heart Rate — تقييم النبض الإكلينيكي</div>
      <div class="card-body">
        <strong>Normal Range:</strong> <code>60 – 100 bpm</code> عند البالغين في وضع الراحة.<br>
        <strong>Tachycardia (&gt; 100 bpm):</strong> سخونية (كل 1°C ترفع ~10 bpm)، قلق، نقص أكسجين، هبوط قلب، نشاط غدة درقية.<br>
        <strong>Bradycardia (&lt; 60 bpm):</strong> رياضيين، أدوية Beta-blockers، إثارة العصب الحائر Vagus stimulation، انخفاض حرارة الجسم.<br><br>
        <strong>⚠️ علامة الـ Pulse Deficit (سؤال امتحان):</strong><br>
        هو الفرق بين ضربات القلب المسموعة بالسماعة (Apical rate) والنبض المحسوس باليد (Radial pulse).<br>
        إذا كان <code>Apical Rate > Radial Pulse Rate</code> → يدل قطعياً على وجود عدم انتظام في ضربات القلب أشهرها <strong>Atrial Fibrillation (AF)</strong>.
      </div>
    </div>

    <div class="info-card purple">
      <div class="card-tag">🩸 Blood Pressure (BP) — ضغط الدم وطريقة القياس الصحيحة</div>
      <div class="card-body">
        <strong>المستويات المعتمدة (AHA Guidelines):</strong>
        <table class="data-table" style="margin-top:8px">
          <thead><tr><th>التصنيف</th><th>الانقباضي (Systolic)</th><th>الانبساطي (Diastolic)</th></tr></thead>
          <tbody>
            <tr><td><strong>طبيعي (Normal)</strong></td><td class="hl">&lt; 120 mmHg</td><td class="hl">و &lt; 80 mmHg</td></tr>
            <tr><td>مرتفع (Elevated)</td><td class="hl">120 – 129 mmHg</td><td class="hl">و &lt; 80 mmHg</td></tr>
            <tr><td>ضغط دم مرحلة 1 (HTN Stage 1)</td><td class="hl">130 – 139 mmHg</td><td class="hl">أو 80 – 89 mmHg</td></tr>
            <tr><td>ضغط دم مرحلة 2 (HTN Stage 2)</td><td class="hl">≥ 140 mmHg</td><td class="hl">أو ≥ 90 mmHg</td></tr>
            <tr><td>أزمة ضغط (Hypertensive Crisis)</td><td class="bad">&gt; 180 mmHg</td><td class="bad">أو &gt; 120 mmHg (طوارئ!)</td></tr>
          </tbody>
        </table>
        <strong>شروط القياس الدقيق:</strong>
        <ul style="margin-right:16px;margin-top:6px;line-height:2;font-size:13px">
          <li>المريض جالس مستريح 5 دقائق، الذراع مسنود في مستوى القلب.</li>
          <li>حجم الكفة (Cuff Size): العرض يغطي 40% من محيط الذراع، والطول يغطي 80%. (الكفة الضيقة تعطي قراءة عالية كاذبة!).</li>
          <li>حافة الكفة السفلية توضع على بعد <strong>2.5 سم (1 inch)</strong> فوق ثنية الكوع.</li>
          <li>أصوات كورتكوف: <strong>Phase 1</strong> (أول صوت نبض واضح) = Systolic BP | <strong>Phase 5</strong> (اختفاء الصوت تماماً) = Diastolic BP.</li>
        </ul>
      </div>
    </div>
'''

sec2_addon = '''
    <div class="info-card purple">
      <div class="card-tag">🌊 أنماط التنفس غير الطبيعية الشهيرة (Abnormal Breathing Patterns)</div>
      <div class="card-body">
        <table class="data-table">
          <thead><tr><th>النمط</th><th>الوصف والشكل</th><th>الأسباب والارتباط</th></tr></thead>
          <tbody>
            <tr>
              <td class="hl">Cheyne-Stokes Breathing</td>
              <td>دورات متكررة: تنفس يبدأ سطحي ثم يعمق تدريجياً (Crescendo) ثم يقل تدريجياً (Decrescendo) يليه انقطاع تنفس (Apnea) لعدة ثوانٍ</td>
              <td>هبوط القلب الاحتقاني الشديد (Severe CHF)، جلطات جذع المخ، اليوريميا (Uremia)</td>
            </tr>
            <tr>
              <td class="hl">Kussmaul Breathing</td>
              <td>تنفس عميق جداً وسريع ومجهد ومنتظم بدون أي انقطاع (Air Hunger)</td>
              <td>الحماض الكيتوني السكري <strong>Diabetic Ketoacidosis (DKA)</strong>، الفشل الكلوي الحاد (Metabolic Acidosis لغسيل CO₂)</td>
            </tr>
            <tr>
              <td class="hl">Biot's (Ataxic) Breathing</td>
              <td>أنفاس سريعة وعميقة غير منتظمة عشوائياً تتخللها فترات Apnea مفاجئة</td>
              <td>التهاب السحايا (Meningitis)، تلف المخ وارتفاع ضغط الجمجمة الشديد (ICP)</td>
            </tr>
            <tr>
              <td class="hl">Paradoxical Breathing</td>
              <td>حركة متناقضة: جدار الصدر يدخل للداخل مع الشهيق ويبرز للخارج مع الزفير (عكس الطبيعي)</td>
              <td>الصدر السائب <strong>Flail Chest</strong> (كسور متعددة بالضلوع)، شلل الحجاب الحاجز أو إجهاده الشديد</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
'''

sec4_addon = '''
    <div class="info-card warn">
      <div class="card-tag">📌 وضع القصبة الهوائية (Tracheal Position & Shift)</div>
      <div class="card-body">
        في الوضع الطبيعي: القصبة الهوائية <strong>Central</strong> في المنتصف تماماً في الـ Suprasternal notch.<br><br>
        <table class="data-table">
          <thead><tr><th>اتجاه الانحراف (Shift)</th><th>الميكانيزم</th><th>الأسباب الإكلينيكية</th></tr></thead>
          <tbody>
            <tr>
              <td class="bad"><strong>منحرفة لنفس الناحية المصابة (Pulled toward)</strong></td>
              <td>سحب نتيجة انكماش ونقص حجم الرئة وشد الأنسجة</td>
              <td><strong>Lung Fibrosis (تليف الرئة)</strong> أو <strong>Atelectasis (انهيار الرئة / Collapse)</strong></td>
            </tr>
            <tr>
              <td class="bad"><strong>مندفعة للناحية السليمة العكسية (Pushed away)</strong></td>
              <td>دفع نتيجة تراكم ضغط أو سوائل أو هواء هائل</td>
              <td><strong>Tension Pneumothorax</strong>، <strong>Massive Pleural Effusion</strong>، أورام ضخمة</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="info-card info">
      <div class="card-tag">👐 علامة هوفر (Hoover's Sign)</div>
      <div class="card-body">
        <strong>التعريف:</strong> حركة الحواف السفلية للقفص الصدري (Lower costal margins) إلى <strong>الداخل</strong> بدلاً من التوسع للخارج أثناء الشهيق.<br>
        <strong>السبب:</strong> تسطح عضلة الحجاب الحاجز (Flattened Diaphragm) نتيجة احتباس الهواء المزمن (Hyperinflation) في مرضى <strong>COPD الشديد</strong>، فتسحب الحواف للداخل عند انقباضها بدلاً من النزول لأسفل.
      </div>
    </div>
'''

# 1. Hospital insert
split_marker = '  <div class="info-card danger">\n    <div class="card-tag">🚨 Red Flags'
if split_marker in text and 'Bedside Script' not in text:
    text = text.replace(split_marker, hospital_addon + '\n' + split_marker)

# 2. Sec 1 insert (before the closing </div> of sec1)
sec1_end = '<!-- ===================== SECTION 2 ===================== -->'
if sec1_end in text and 'Pulse & Heart Rate' not in text:
    idx = text.find(sec1_end)
    # Find the last </div> before sec1_end
    last_div = text.rfind('</div>', 0, idx)
    last_div2 = text.rfind('</div>', 0, last_div)
    text = text[:last_div2] + sec1_addon + '\n  </div>\n</div>\n\n' + text[idx:]

# 3. Sec 2 insert (before sec3)
sec2_end = '<!-- ===================== SECTION 3 ===================== -->'
if sec2_end in text and 'Abnormal Breathing Patterns' not in text:
    idx = text.find(sec2_end)
    last_div = text.rfind('</div>', 0, idx)
    last_div2 = text.rfind('</div>', 0, last_div)
    text = text[:last_div2] + sec2_addon + '\n  </div>\n</div>\n\n' + text[idx:]

# 4. Sec 4 insert (before quiz)
sec4_end = '<!-- ===================== QUIZ ===================== -->'
if sec4_end in text and 'Tracheal Position' not in text:
    idx = text.find(sec4_end)
    last_div = text.rfind('</div>', 0, idx)
    last_div2 = text.rfind('</div>', 0, last_div)
    text = text[:last_div2] + sec4_addon + '\n  </div>\n</div>\n\n' + text[idx:]

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(text)

print(f'Enhanced cvp_midterm.html! New length: {len(text)}')
