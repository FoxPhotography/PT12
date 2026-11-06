# CVP PT — practical sections (rebuilt from the section data: Dr. Fatma, Dr. Dina, Dr. Alaa transcripts,
# "Cardiovascular PT Practical" 2/3/4 files, and PT11 notes).
# Tab: (id, title, short, icon, source, summary_html, groups)
# Question tuple: (text, [correct, wrong...], tag, explanation)   tag: "" | "imp"

TABS = []
def T(*a): TABS.append(a)

# ===================================================================== 1. Temperature & Pulse
T("vs1", "Vital Signs I — Temperature & Pulse", "Temp & Pulse", "🌡️",
  "سكشن 1 (د. فاطمة + داتا د. آلاء + نوت PT11)",
"""
<div class="card"><h4>Vital signs</h4>
<p>Signs of life بتعكس الحالة الجسدية العامة للمريض ووظيفة الأعضاء الداخلية، وبنسجلها كـ <b>baseline</b> أول ما المريض يدخل المستشفى.</p>
<p class="ltr">The 5 vital signs: <b>Temperature · Heart rate (pulse) · Blood pressure · O₂ saturation · Respiratory rate</b></p></div>

<div class="card"><h4>Body temperature</h4>
<ul><li><b>التعريف:</b> balance between <b>heat production</b> و <b>heat loss</b>، والتنظيم بيحصل في الـ <b>hypothalamus</b> (thermoregulatory center).</li>
<li><b>Receptors:</b> central في الـ hypothalamus (بتحس بحرارة الدم اللي داخل المخ)، و peripheral في الجلد (بتحس بحرارة الجو). <b>Effectors:</b> blood vessels الجلد (vasodilation)، و sweat glands، والـ endocrine.</li>
<li><b>Heat production:</b> muscle contraction/activity، conversion of food to energy (digestion)، environmental temp.</li>
<li><b>Heat loss:</b> urination، defecation، sweating، respiration، environmental temp.</li></ul>
<table><tr><th>Mechanism</th><th>التعريف</th></tr>
<tr><td>Radiation</td><td>انتقال الحرارة من جسم لجسم <b>من غير</b> actual contact</td></tr>
<tr><td>Conduction</td><td>انتقال الحرارة <b>بالتلامس</b> المباشر</td></tr>
<tr><td>Convection</td><td>انتقال الحرارة عن طريق <b>حركة الهوا أو السوائل</b></td></tr>
<tr><td>Evaporation</td><td>تبخر المية من الجلد (sweating)</td></tr></table>
<table><tr><th>القيمة</th><th>المعنى</th></tr>
<tr><td>36.5 – 37.5 °C</td><td>Normal (core)</td></tr>
<tr><td>&gt; 37.5</td><td>Fever / pyrexia</td></tr>
<tr><td>&lt; 36</td><td>Hypothermia: cold skin، cyanosis، HR و RR بيقلوا، cutaneous sensation و mental response بيقلوا</td></tr>
<tr><td>&gt; 40 – 41</td><td>Hyperpyrexia / hyperthermia: confusion و ممكن coma</td></tr></table>
<ul><li><b>Fever</b> بيزود الـ metabolic rate، فيزيد الـ CO₂، فيزيد الـ HR والـ RR (compensatory). كمان headache و blushing و chills. وكل <b>1°C</b> زيادة بيزود الـ pulse حوالي <b>10 beats/min</b>.</li>
<li><b>Hyperpyrexia</b> سببها infection (الجهاز المناعي بيقاوم). <b>Hyperthermia</b> سببها الجو الخارجي (زي ضربة الشمس).</li></ul></div>

<div class="card"><h4>أنواع الترمومتر وأماكن القياس</h4>
<ul><li><b>Mercury-in-glass (clinical)</b>: بالزئبق اللي بيتمدد. <b>Chemical</b>: مادة كيميائية حساسة. <b>Electronic/digital</b>: سريع (1–2 sec)، ومنه الـ tympanic اللي بيتعمل في الأطفال وفاقدين الوعي. <b>Temperature-sensitive tape</b>: على الجبهة، للأطفال، ومش دقيق.</li></ul>
<table><tr><th>المكان</th><th>المدة</th><th>القراءة</th><th>ملاحظات</th></tr>
<tr><td>Oral (تحت اللسان)</td><td>2–5 min</td><td>زي الـ core</td><td>الأشهر. <b>CI:</b> oral infection/ulcer، unconscious/comatosed، mental illness، persistent cough، mouth breathers، irritable، الرضع</td></tr>
<tr><td>Axillary</td><td>5–10 min</td><td>أقل بـ <b>0.5</b> (فبنزود 0.5)</td><td><b>Least accurate</b> لأنه بعيد عن الـ major vessels. الدراع على الكتف التاني. للرضع والأطفال</td></tr>
<tr><td>Tympanic</td><td>1–2 sec</td><td>زي الـ core</td><td>في الـ outer ear canal</td></tr>
<tr><td>Rectal</td><td>3 min</td><td>أعلى بـ <b>0.5</b> (فبنطرح 0.5)</td><td><b>Most accurate</b> (قريب من major vessels). المريض side lying. <b>CI:</b> rectal infection/surgery/disease/inflammation، diarrhea</td></tr></table>
<p><b>Factors affecting BT:</b> time of day (أقل حاجة الصبح بدري وأعلى حاجة بعد الضهر)، age (الأطفال أعلى)، sex (الستات أعلى بسبب الهرمونات)، exercise، stress/emotions، environmental temp، smoking و alcohol بيزودوا، drugs و diseases (infection، hyperthyroidism بيزودوا).</p></div>

<div class="card"><h4>Pulse / Heart rate</h4>
<ul><li><b>Pulse</b> = palpable wave of blood flow في أماكن مختلفة في الجسم، نتيجة <b>left ventricular contraction</b>.</li>
<li>الطبيعي الـ PR = HR. لو الـ pulse rate أقل من الـ heart rate يبقى فيه <b>peripheral arterial occlusion</b>. الـ HR بيتقاس من القلب نفسه (apical pulse): <b>left 5th intercostal space, mid-clavicular line</b> (تحت الـ nipple في الراجل، وتحت الـ breast في الست).</li>
<li><b>Normal:</b> 60–100 beats/min، والـ newborn من 120 لـ 160. <b>Bradycardia</b> أقل من 60 (sleeping، beta-blockers، athletes، parasympathetic). <b>Tachycardia</b> أكتر من 100 (fever، stress، anemia).</li>
<li><b>القياس:</b> palpation بالـ <b>index و middle و ring</b>، ومش بالإبهام عشان ليه pulse لوحده. لو منتظم تعد 30 ثانية × 2 أو 15 × 4، ولو مش منتظم تعد دقيقة كاملة.</li></ul>
<table><tr><th>Artery</th><th>مكانه</th></tr>
<tr><td>Temporal</td><td>superior و lateral لنهاية الحاجب</td></tr>
<tr><td>Carotid</td><td>بين الـ SCM والـ trachea (متقيسش الناحيتين مع بعض)</td></tr>
<tr><td>Axillary</td><td>deep في الـ axilla والمريض عامل abduction</td></tr>
<tr><td>Brachial</td><td>medial للـ biceps tendon / الـ antecubital fossa</td></tr>
<tr><td>Radial</td><td>عند قاعدة الإبهام (radial styloid)</td></tr>
<tr><td>Ulnar</td><td>عند قاعدة الصباع الصغير (ulnar styloid)</td></tr>
<tr><td>Femoral</td><td>المريض supine في open book position، وبيتحس في نص المسافة بين الـ ASIS والـ symphysis pubis تحت الـ inguinal ligament</td></tr>
<tr><td>Popliteal</td><td>الركبة semi-flexed والإيدين حوالين الركبة</td></tr>
<tr><td>Posterior tibial</td><td>ورا وتحت الـ medial malleolus</td></tr>
<tr><td>Dorsalis pedis / anterior tibial</td><td>lateral لـ tendon الـ extensor hallucis longus (بين الـ 1st و 2nd metatarsal)</td></tr></table>
<p><b>تقييم الـ pulse:</b> rate، rhythm (regular / irregular)، volume (strength)، elasticity.</p>
<table><tr><th>Grade</th><th>Volume</th></tr>
<tr><td>0</td><td>Absent</td></tr><tr><td>1</td><td>Weak (بيتحس بصعوبة)</td></tr><tr><td>2</td><td>Normal</td></tr><tr><td>3</td><td>Full / strong</td></tr><tr><td>4</td><td>Bounding</td></tr></table>
<p><b>Elasticity:</b> الشريان الطبيعي soft و flexible و straight. لو cord-like و hard (sclerotic) يبقى old age أو atherosclerosis.</p>
<p><b>Factors affecting HR:</b> age (الأطفال أعلى)، sex (الستات أعلى)، exercise، stress و smoking بيزودوا، beta-blockers بتقلل، temp (+10 لكل 1°C)، قلة النوم أو الأكل بتزود، dehydration بتزود (CO = HR × SV)، و body position (أقل حاجة supine، وبتزيد في sitting ثم standing ثم الطلوع). الرياضيين عندهم bradycardia.</p>
<p><b>Regulation:</b> autonomic. الـ <b>Sympathetic</b> بيزود الـ HR (SAN أسرع وانقباض أقوى)، والـ <b>parasympathetic</b> بيقلله. وكمان الـ chemoreceptors والـ endocrine.</p></div>
""",
[
 ("Vital signs & temperature", [
  ("The five vital signs include all EXCEPT:", ["Blood glucose", "Temperature", "O₂ saturation", "Respiratory rate"], "", "الخمسة: T و HR و BP و SpO₂ و RR."),
  ("Body temperature is regulated by the:", ["Hypothalamus", "Medulla", "Pons", "Cerebellum"], "imp", ""),
  ("Normal core body temperature is:", ["36.5–37.5 °C", "35–36 °C", "37.5–38.5 °C", "38–39 °C"], "imp", ""),
  ("Body temperature above 37.5 °C is called:", ["Fever (pyrexia)", "Hypothermia", "Normothermia", "Hypopnea"], "", ""),
  ("Transfer of heat WITHOUT actual contact is:", ["Radiation", "Conduction", "Convection", "Evaporation"], "imp", ""),
  ("Transfer of heat WITH actual contact is:", ["Conduction", "Radiation", "Convection", "Evaporation"], "imp", ""),
  ("Transfer of heat through air (or fluid) movement is:", ["Convection", "Conduction", "Radiation", "Evaporation"], "imp", ""),
  ("Sweating causes heat loss by:", ["Evaporation", "Radiation", "Conduction", "Convection"], "", ""),
  ("Fever increases HR and RR because it:", ["Increases metabolic rate and CO₂ production", "Decreases metabolic rate", "Stimulates the parasympathetic", "Decreases O₂ demand"], "", ""),
  ("Each 1 °C rise in temperature increases the pulse by about:", ["10 beats/min", "2 beats/min", "30 beats/min", "50 beats/min"], "imp", ""),
  ("Hyperthermia (as opposed to hyperpyrexia) results from:", ["External environment (e.g. sun stroke)", "Infection", "Immune reaction", "Hypothyroidism"], "", ""),
  ("Hypothermia is associated with:", ["Cold skin, cyanosis and decreased HR & RR", "Increased HR and RR", "Sweating and flushing", "Hyperventilation"], "", ""),
 ]),
 ("Thermometers & sites", [
  ("The most accurate site of temperature measurement is:", ["Rectal", "Axillary", "Oral", "Forehead tape"], "imp", ""),
  ("The least accurate site of temperature measurement is:", ["Axillary", "Rectal", "Oral", "Tympanic"], "imp", "لأنه بعيد عن الـ major vessels."),
  ("Axillary temperature is measured for:", ["5–10 minutes", "1–2 seconds", "3 minutes", "30 seconds"], "", ""),
  ("Oral temperature is measured for:", ["2–5 minutes", "10–15 minutes", "1–2 seconds", "20 minutes"], "", ""),
  ("Rectal temperature is measured for about:", ["3 minutes", "10 minutes", "1 second", "15 minutes"], "", ""),
  ("Tympanic (electronic) thermometer takes about:", ["1–2 seconds", "5–10 minutes", "3 minutes", "15 minutes"], "", ""),
  ("Axillary reading compared to core temperature is:", ["0.5 °C less (so add 0.5)", "0.5 °C more", "The same", "2 °C less"], "imp", ""),
  ("Rectal reading compared to core temperature is:", ["0.5 °C higher (so subtract 0.5)", "0.5 °C lower", "The same", "2 °C higher"], "", ""),
  ("Contraindications of oral temperature include all EXCEPT:", ["Diarrhea", "Unconscious patient", "Mouth breather", "Persistent cough"], "imp", "الـ diarrhea contraindication للـ rectal."),
  ("Contraindications of rectal temperature include:", ["Rectal surgery, rectal infection and diarrhea", "Mouth breathing", "Persistent cough", "Mental illness"], "", ""),
  ("Patient position for rectal temperature is:", ["Side lying", "Prone", "Sitting", "Standing"], "", ""),
  ("The temperature-sensitive tape is placed on the:", ["Forehead", "Axilla", "Rectum", "Tongue"], "", "بيُستخدم مع الأطفال ومش دقيق."),
  ("Body temperature is lowest:", ["Early morning", "Afternoon", "Evening after meals", "It does not change"], "", ""),
 ]),
 ("Pulse", [
  ("The pulse is a palpable wave of blood resulting from contraction of the:", ["Left ventricle", "Right ventricle", "Left atrium", "Right atrium"], "imp", ""),
  ("Normal adult pulse rate is:", ["60–100 beats/min", "40–60 beats/min", "100–140 beats/min", "120–160 beats/min"], "imp", ""),
  ("Normal pulse rate of a newborn is:", ["120–160 beats/min", "60–100 beats/min", "40–60 beats/min", "200–240 beats/min"], "", ""),
  ("A pulse rate less than the heart rate indicates:", ["Peripheral arterial occlusion", "Fever", "Normal finding", "Athlete's heart"], "imp", ""),
  ("The apical pulse is felt at:", ["Left 5th intercostal space, mid-clavicular line", "Right 2nd intercostal space", "Left 2nd intercostal space parasternal", "Xiphoid process"], "imp", ""),
  ("The pulse is palpated using:", ["Index, middle and ring fingers (not the thumb)", "The thumb", "The palm", "The ulnar border of the hand"], "imp", "الإبهام ليه pulse لوحده."),
  ("If the pulse is irregular, it should be counted for:", ["A full minute", "15 seconds × 4", "30 seconds × 2", "10 seconds × 6"], "", ""),
  ("The carotid pulse is felt:", ["Between the SCM and the trachea (never both sides together)", "Lateral to the SCM", "Behind the ear", "At the suprasternal notch"], "", ""),
  ("The brachial pulse is felt:", ["Medial to the biceps tendon at the antecubital fossa", "Lateral to the biceps tendon", "In the axilla", "At the wrist"], "", ""),
  ("The radial pulse is felt at:", ["The base of the thumb (radial styloid)", "The base of the little finger", "The antecubital fossa", "The axilla"], "", ""),
  ("The posterior tibial pulse is felt:", ["Behind and below the medial malleolus", "Lateral to EHL tendon", "Behind the knee", "Lateral malleolus"], "", ""),
  ("The dorsalis pedis pulse is felt:", ["Lateral to the extensor hallucis longus tendon", "Behind the medial malleolus", "Behind the knee", "At the heel"], "", ""),
  ("The femoral pulse is felt with the patient:", ["Supine in open book position, midway between ASIS and symphysis pubis", "Prone", "Sitting", "Side lying"], "", ""),
  ("Pulse volume grade 4 is:", ["Bounding", "Absent", "Weak", "Normal"], "imp", ""),
  ("Pulse volume grade 1 is:", ["Weak", "Normal", "Bounding", "Full"], "", ""),
  ("A cord-like hard artery (sclerotic) is seen in:", ["Old age and atherosclerosis", "Athletes", "Children", "Fever"], "", ""),
  ("Bradycardia (< 60) occurs in all EXCEPT:", ["Fever", "Sleeping", "Beta-blockers", "Athletes"], "", "الـ fever بيعمل tachycardia."),
  ("Heart rate is lowest in which position?", ["Supine", "Standing", "Sitting", "Climbing"], "", ""),
  ("The sympathetic nervous system:", ["Increases HR", "Decreases HR", "Has no effect on HR", "Stops the SAN"], "", ""),
 ]),
])

# ===================================================================== 2. RR, SpO2, BP
T("vs2", "Vital Signs II — Respiratory Rate, O₂ Saturation & Blood Pressure", "RR · SpO₂ · BP", "🩸",
  "سكشن 2 (د. دينا + د. آلاء + نوت PT11)",
"""
<div class="card"><h4>Respiratory rate</h4>
<ul><li><b>Respiration</b> = gas exchange (O₂ / CO₂). <b>RR</b> = number of breaths per minute (one cycle = inspiration + expiration).</li>
<li><b>Assessment by inspection / observation</b>: المريض في وضع مريح ومتقولوش إنك بتعد نفسه، عشان ميغيرش طريقة تنفسه. حط إيدك كأنك بتقيس الـ pulse وعد.</li>
<li>مستويات الملاحظة: apical (عند الـ clavicle)، sternal (sternal notch)، diaphragmatic (xiphoid)، costal (الـ 4th ICS والـ costal margin)، posterior basal (inferior angle of scapula).</li></ul>
<table><tr><th>العمر</th><th>Normal RR</th></tr>
<tr><td>Adult</td><td>12–20</td></tr><tr><td>Pre-school</td><td>20–25</td></tr><tr><td>4 years</td><td>25–30</td></tr><tr><td>Infants</td><td>30–60</td></tr></table>
<table><tr><th>المصطلح</th><th>المعنى</th></tr>
<tr><td>Bradypnea</td><td>RR أقل من 12 (CNS depression، مخدرات)</td></tr>
<tr><td>Tachypnea</td><td>RR أكتر من 20 (anemia، fever، stress)، وغالبًا shallow و rapid</td></tr>
<tr><td>Hyperpnea</td><td>↑ depth (deep breathing)، زي الـ acidosis</td></tr>
<tr><td>Oligopnea</td><td>↓ depth (shallow)، زي الـ CNS depression</td></tr>
<tr><td>Hyperventilation</td><td>↑ rate و depth مع بعض</td></tr>
<tr><td>Hypoventilation</td><td>↓ rate و depth مع بعض</td></tr>
<tr><td>Apnea</td><td>temporary stop of breathing (غالبًا upper airway obstruction)</td></tr>
<tr><td>Dyspnea</td><td>difficult breathing / awareness of breathing (الطبيعي effortless)</td></tr></table>
<ul><li><b>Pattern:</b> الراجل <b>abdomino-thoracic</b> (الـ diaphragm قوي)، والست <b>thoraco-abdominal</b> (عشان فترة الحمل).</li>
<li><b>Factors:</b> age (الأطفال والكبار أعلى)، sex (الستات أعلى، والرجالة عندهم vital capacity أكبر)، exercise و stress و drugs/smoking و metabolism بيزودوا، altitude (العالي بيزود)، و body position (الـ supine بيزود لأن الأحشاء بتضغط على الـ diaphragm، وأحسن وضع half supine أو long sitting).</li>
<li><b>Regulation:</b> respiratory center في الـ <b>medulla</b> (أساسًا) والـ pons. <b>Central chemoreceptors</b> (جنب الـ medulla) حساسة لزيادة الـ CO₂ (hypercapnia). <b>Peripheral chemoreceptors</b> (carotid و aortic) حساسة لنقص الـ O₂. والـ <b>stretch receptors</b> في الـ alveoli بتمنع الـ over-inflation.</li></ul></div>

<div class="card"><h4>O₂ saturation</h4>
<ul><li>= concentration of O₂ in the <b>blood</b> (مش الـ tissue oxygenation)، وبتتقاس بالـ <b>pulse oximeter</b> على الصباع.</li>
<li>Normal <b>95–99%</b>. Mild hypoxemia 91–94، moderate 86–90، severe ≤ 85.</li>
<li><b>Hypoxemia</b> = O₂ قليل في الدم. <b>Hypoxia</b> = O₂ قليل في الـ tissue. أنواع الـ hypoxia: <b>hypoxemic</b> (الدم نفسه فيه O₂ قليل)، <b>ischemic</b> (الدم كويس بس الـ flow قليل)، <b>anemic</b> (الـ Hb قليل)، <b>histotoxic</b> (الـ tissue مش قادرة تستخدم الـ O₂).</li></ul></div>

<div class="card"><h4>Blood pressure</h4>
<ul><li><b>BP</b> = force exerted by blood against the vessel wall (بعد الـ left ventricular contraction). <b>Systolic</b> أقصى ضغط، و<b>diastolic</b> أقل ضغط (الـ ventricle في relaxation).</li>
<li><b>Normal</b> 120/80 (± 20/15)، يعني systolic من <b>100 لـ 140</b> و diastolic من <b>60 لـ 90</b>. أكتر من 140/90 يبقى <b>hypertension</b>، وأقل من 100/60 يبقى <b>hypotension</b>. الـ <b>diastolic</b> الواطي أخطر.</li>
<li><b>Pulse pressure</b> = systolic − diastolic (مثلًا 120 − 80 = 40 mmHg).</li></ul>
<table><tr><th>مصطلح</th><th>المعنى</th></tr>
<tr><td>White coat hypertension</td><td>الضغط عالي في العيادة أو المستشفى بس، وطبيعي في البيت</td></tr>
<tr><td>Postural hypotension</td><td>sudden drop في الضغط لما يقوم من sitting أو lying (الدم بيتجمع في الرجلين فيقل الـ venous return)</td></tr>
<tr><td>Pulsus paradoxus</td><td>abnormal drop في الـ systolic أكتر من <b>10 mmHg</b> أثناء الـ <b>inspiration</b> (أمراض قلب أو رئة)</td></tr>
<tr><td>Auscultatory (silent) gap</td><td>الصوت بيختفي بين الـ systolic وضغط أقل وبعدين يرجع (old age، hypertension، atherosclerosis، arterial stiffness)، فممكن تقرا الـ systolic غلط</td></tr></table>
<p><b>Factors affecting BP:</b></p>
<ul><li>Age بيزوده (↓ elasticity)، و athletes ضغطهم stable أو أقل (vagal tone).</li>
<li>Dominant arm أعلى بـ <b>15–20 mmHg</b>، والـ lower limb أعلى بحوالي <b>20 mmHg</b> من الـ upper limb.</li>
<li>Blood volume: الـ haemorrhage بيقلله، والـ transfusion بيزوده. الـ cardiac output بيزوده.</li>
<li>Vasoconstriction بيزود، والـ vasodilatation (أو زيادة الـ diameter) بيقلل. لو الـ elasticity قلت الضغط بيزيد.</li>
<li>Exercise و stress و smoking و caffeine بيزودوا.</li>
<li><b>Valsalva</b>: زيادة الضغط في البطن والصدر بتقلل الـ venous return فيقل الضغط، وبعدها يحصل protective vasoconstriction فيرجع يزيد.</li></ul></div>

<div class="card"><h4>قياس الضغط</h4>
<ul><li><b>Device:</b> mercury sphygmomanometer (cuff، bulb، valve، mercury) + stethoscope (ear tips، ear tubes، tube، <b>diaphragm</b> لأصوات الرئة، <b>bell</b> لأصوات القلب).</li>
<li><b>Site:</b> الأشهر <b>brachial artery</b>. ممكن sitting أو standing أو supine، بس الـ cuff لازم على مستوى القلب.</li>
<li><b>Instructions:</b> المريض مشربش caffeine ومعملش exercise ومدخنش من نص ساعة على الأقل، مش لسه صاحي من النوم، مش لابس حاجة ضيقة (bare skin)، وفي وضع مريح.</li>
<li>الـ cuff فوق الـ antecubital space بـ <b>2.5–5 cm</b>، ومش tight ولا loose (يدخل صباع أو اتنين).</li></ul>
<table><tr><th>Method</th><th>الطريقة</th></tr>
<tr><td>Palpatory</td><td>تحس الـ <b>radial</b> pulse، تنفخ لحد ما الـ pulse يختفي، وبعدين تفرغ. أول pulse يرجع هو الـ <b>systolic</b>. عيبه إنه بيدي الـ systolic بس. بنستخدمه قبل الـ auscultatory عشان نعرف الـ systolic ونتجنب الـ auscultatory gap</td></tr>
<tr><td>Auscultatory</td><td>تنفخ فوق الـ systolic بحوالي 20–30، وتحط الـ stethoscope على الـ brachial (medial)، وتفرغ ببطء (حوالي 2 mmHg في الثانية). أول صوت = systolic، واختفاء الصوت = diastolic</td></tr></table>
<table><tr><th>Korotkoff phase</th><th>الصوت</th></tr>
<tr><td>1</td><td>Clear tapping = <b>systolic</b></td></tr><tr><td>2</td><td>Murmur</td></tr><tr><td>3</td><td>Softer tapping</td></tr><tr><td>4</td><td>Muffled</td></tr><tr><td>5</td><td>Disappear = <b>diastolic</b></td></tr></table>
<p>أهم صوتين: الـ 1st والـ 5th.</p></div>
""",
[
 ("Respiratory rate", [
  ("Respiratory rate is assessed by:", ["Inspection/observation without telling the patient", "Asking the patient to breathe deeply", "Spirometry", "Auscultation only"], "imp", "لو عرف إنك بتعد هيغير طريقة تنفسه."),
  ("Normal adult respiratory rate is:", ["12–20 breaths/min", "20–30 breaths/min", "30–60 breaths/min", "8–10 breaths/min"], "imp", ""),
  ("Normal respiratory rate in infants is:", ["30–60 breaths/min", "12–20 breaths/min", "20–25 breaths/min", "60–80 breaths/min"], "", ""),
  ("One respiratory cycle consists of:", ["One inspiration + one expiration", "Two inspirations", "Inspiration only", "Expiration only"], "", ""),
  ("RR less than 12 is called:", ["Bradypnea", "Tachypnea", "Apnea", "Hyperpnea"], "", ""),
  ("Increase in depth of respiration (deep breathing) is:", ["Hyperpnea", "Oligopnea", "Tachypnea", "Apnea"], "imp", ""),
  ("Decrease in depth of respiration (shallow) is:", ["Oligopnea", "Hyperpnea", "Hyperventilation", "Bradypnea"], "imp", ""),
  ("Increase in both rate and depth is:", ["Hyperventilation", "Hypoventilation", "Hyperpnea", "Tachypnea"], "", ""),
  ("Temporary stop of breathing is:", ["Apnea", "Dyspnea", "Orthopnea", "Bradypnea"], "", ""),
  ("Breathing pattern in males is:", ["Abdomino-thoracic", "Thoraco-abdominal", "Apical", "Paradoxical"], "imp", "لأن الـ diaphragm عندهم well established."),
  ("Breathing pattern in females is:", ["Thoraco-abdominal", "Abdomino-thoracic", "Purely diaphragmatic", "Paradoxical"], "", ""),
  ("The respiratory center is mainly in the:", ["Medulla", "Hypothalamus", "Cerebellum", "Cortex"], "", ""),
  ("Central chemoreceptors are mainly sensitive to:", ["Increased CO₂ (hypercapnia)", "Decreased O₂", "Blood pressure", "Temperature"], "", ""),
  ("Peripheral chemoreceptors (carotid & aortic) are sensitive to:", ["Decreased O₂ (hypoxia)", "Increased temperature", "Stretch of alveoli", "Blood glucose"], "", ""),
  ("Supine position increases RR because:", ["Viscera press on the diaphragm", "Lung capacity increases", "Metabolism decreases", "The diaphragm becomes stronger"], "", ""),
 ]),
 ("O₂ saturation", [
  ("O₂ saturation measures the concentration of O₂ in the:", ["Blood", "Tissues", "Alveoli", "Inspired air"], "imp", ""),
  ("O₂ saturation is measured by:", ["Pulse oximeter", "Sphygmomanometer", "Spirometer", "Thermometer"], "", ""),
  ("Normal O₂ saturation is:", ["95–99%", "85–90%", "90–94%", "75–85%"], "imp", ""),
  ("SpO₂ of 88% indicates:", ["Moderate hypoxemia", "Mild hypoxemia", "Severe hypoxemia", "Normal"], "imp", "Mild 91–94، moderate 86–90، severe ≤ 85."),
  ("SpO₂ ≤ 85% indicates:", ["Severe hypoxemia", "Mild hypoxemia", "Normal", "Moderate hypoxemia"], "", ""),
  ("Hypoxia with normal blood O₂ but decreased blood flow to the tissue is:", ["Ischemic hypoxia", "Hypoxemic hypoxia", "Anemic hypoxia", "Histotoxic hypoxia"], "", ""),
  ("When the tissue cannot use the O₂ delivered to it, this is:", ["Histotoxic hypoxia", "Anemic hypoxia", "Ischemic hypoxia", "Hypoxemic hypoxia"], "", ""),
 ]),
 ("Blood pressure", [
  ("Normal blood pressure range for systolic is:", ["100–140 mmHg", "60–90 mmHg", "140–180 mmHg", "80–100 mmHg"], "imp", ""),
  ("Normal blood pressure range for diastolic is:", ["60–90 mmHg", "100–140 mmHg", "40–50 mmHg", "90–120 mmHg"], "imp", ""),
  ("Pulse pressure is:", ["Systolic − diastolic", "Systolic + diastolic", "Diastolic − systolic", "Mean arterial pressure"], "imp", ""),
  ("BP rising only in the clinic and normal at home is:", ["White coat hypertension", "Postural hypotension", "Pulsus paradoxus", "Essential hypertension"], "imp", ""),
  ("Sudden drop of BP on standing from sitting or lying is:", ["Postural (orthostatic) hypotension", "White coat hypertension", "Pulsus paradoxus", "Auscultatory gap"], "imp", ""),
  ("Pulsus paradoxus is an abnormal drop in systolic BP of more than …… during inspiration:", ["10 mmHg", "2 mmHg", "40 mmHg", "100 mmHg"], "imp", ""),
  ("BP in the dominant arm compared to the non-dominant arm is:", ["Higher by 15–20 mmHg", "Lower by 15–20 mmHg", "Equal", "Higher by 50 mmHg"], "", ""),
  ("BP in the lower limb compared to the upper limb is:", ["Higher by about 20 mmHg", "Lower by 20 mmHg", "Equal", "Unmeasurable"], "", ""),
  ("Which DECREASES blood pressure?", ["Haemorrhage", "Vasoconstriction", "Blood transfusion", "Smoking"], "", ""),
  ("Decreased elasticity of blood vessels (old age) leads to:", ["Increased BP", "Decreased BP", "No change", "Postural hypotension only"], "", ""),
  ("The most common site for BP measurement is the:", ["Brachial artery", "Radial artery", "Femoral artery", "Carotid artery"], "", ""),
  ("The diaphragm of the stethoscope is used mainly for:", ["Lung sounds", "Heart sounds", "Bowel sounds only", "Measuring temperature"], "", "والـ bell لأصوات القلب."),
  ("The BP cuff is wrapped above the antecubital space by:", ["2.5–5 cm", "10–15 cm", "0 cm", "20 cm"], "", ""),
  ("Before measuring BP, the patient should avoid caffeine, exercise and smoking for at least:", ["30 minutes", "5 minutes", "24 hours", "1 week"], "", ""),
  ("The palpatory method measures:", ["Systolic pressure only", "Diastolic pressure only", "Both systolic and diastolic", "Pulse pressure only"], "imp", ""),
  ("In the palpatory method, the pulse palpated is the:", ["Radial", "Carotid", "Femoral", "Dorsalis pedis"], "", ""),
  ("The first Korotkoff sound (clear tapping) represents the:", ["Systolic pressure", "Diastolic pressure", "Pulse pressure", "Mean pressure"], "imp", ""),
  ("Disappearance of Korotkoff sounds (phase 5) represents the:", ["Diastolic pressure", "Systolic pressure", "Pulse pressure", "Auscultatory gap"], "imp", ""),
  ("The auscultatory (silent) gap is common in:", ["Old age, hypertension and atherosclerosis", "Children", "Athletes", "Fever"], "", "وعشان نتجنبه بنعمل الـ palpatory method الأول."),
 ]),
])

# ===================================================================== 3. History & general examination
T("hist", "Chest History Taking & General Examination", "History & General", "📋",
  "سكشن 3 (تفريغ السكشن التالت + Cardiovascular PT Practical 2)",
"""
<div class="card"><h4>Chest examination sheet</h4>
<p>الشيت بيتقسم لـ <b>History</b> و <b>Assessment</b>، والـ Assessment بيتقسم لـ <b>general</b> و <b>local</b> examination.</p></div>

<div class="card"><h4>Personal history</h4>
<table><tr><th>البند</th><th>ليه بنسأل</th></tr>
<tr><td>Name</td><td>to be familiar with the patient</td></tr>
<tr><td>Age</td><td>أمراض ليها سن: <b>cystic fibrosis</b> (أطفال، genetic)، <b>TB</b> (young)، <b>senile emphysema</b> و <b>COPD</b> (كبار، old smokers)</td></tr>
<tr><td>Sex</td><td>Male: bronchogenic carcinoma (smokers) و COPD. Female: asthma</td></tr>
<tr><td>Occupation</td><td>occupational lung diseases: <b>silicosis</b> (silica)، <b>pneumoconiosis</b> (coal)، <b>asbestosis</b> (asbestos fibers)</td></tr>
<tr><td>Address</td><td>زي اللي ساكن جنب مصانع الفحم: <b>black lung disease</b> (coal dust)</td></tr>
<tr><td>Habits</td><td>smoking، alcohol، narcotics (بتعمل inhibition للـ respiratory center)</td></tr>
<tr><td>Telephone، marital status، date of admission</td><td>بيانات</td></tr></table>
<p class="key"><b>Smoking index</b> = number of cigarettes/day × years of smoking. <b>Mild</b> لحد 200، <b>moderate</b> 200–400، <b>heavy</b> أكتر من 400.</p></div>

<div class="card"><h4>Past, present و family history</h4>
<ul><li><b>Past:</b> previous diseases (DM، HTN)، هل المشكلة حصلت قبل كده، الأدوية، الحوادث، العمليات، و physical therapy sessions.</li>
<li><b>Present (chief complaint):</b> بكلام المريض نفسه من غير medical terms (يعني "بيكح دم" مش "hemoptysis"). وبعدين التحليل:
<br>• <b>Onset:</b> sudden ولا gradual.
<br>• <b>Course:</b> progressive، regressive، stationary، relapse، intermittent.
<br>• <b>Duration.</b>
<br>• <b>Aggravating &amp; relieving (mitigating) factors.</b>
<br>• date of admission و operation و discharge.</li>
<li><b>Family history:</b> هل حد في العيلة عنده نفس المشكلة؟ (+ve أو −ve)</li></ul></div>

<div class="card"><h4>Symptoms: chest pain, cough, sputum</h4>
<table><tr><th>Chest pain</th><th>الوصف</th></tr>
<tr><td>Pleural</td><td>sharp و superficial وبيزيد مع الكحة والنفس</td></tr>
<tr><td>Tracheal</td><td>بيحصل مع الكحة بس</td></tr>
<tr><td>Myocardial infarction</td><td>compression pain</td></tr>
<tr><td>GERD</td><td>ممكن يتلخبط مع الـ cardiac pain</td></tr></table>
<p>أسباب تانية: ribs و spine (fracture، inflammation، neoplasm)، muscles (myalgia، myositis)، nerves (neuritis)، cardiac (angina، pericarditis)، pleural (effusion، embolism)، diaphragmatic (hernia).</p>
<p><b>Cough:</b> <b>dry</b> (acute laryngitis، COVID-19) أو <b>wet/productive</b> (pneumonia). الـ <b>obstructive</b> lung disease نشجعه على الكحة عشان يطلع البلغم، والـ <b>restrictive</b> نثبطها عشان متزودش الوجع.</p>
<table><tr><th>Sputum</th><th>المعنى</th></tr>
<tr><td>Yellow</td><td>bacterial (pyogenic) infection</td></tr>
<tr><td>Pink / frothy blood-tinged</td><td>pulmonary edema (والـ pink كمان TB)</td></tr>
<tr><td>Red</td><td>bronchogenic carcinoma</td></tr>
<tr><td>Purple</td><td>neoplasm</td></tr>
<tr><td>Brown / with pus</td><td>lung abscess (suppurative lung disease)</td></tr>
<tr><td>Black</td><td>smoking، occupational lung disease، industrial city</td></tr>
<tr><td>Watery salty</td><td>alveolar carcinoma</td></tr>
<tr><td>Mucoid (tenacious)</td><td>bronchitis و asthma</td></tr>
<tr><td>Bad odor</td><td>infection</td></tr></table></div>

<div class="card"><h4>Shortness of breath و مصطلحات</h4>
<table><tr><th>المصطلح</th><th>المعنى</th></tr>
<tr><td>Dyspnea</td><td>difficult breathing (أسوأها at rest)</td></tr>
<tr><td>Exertional dyspnea</td><td>مع المجهود بس</td></tr>
<tr><td>Orthopnea</td><td>dyspnea في الـ <b>flat position</b> وبيرتاح لما يقعد أو يقف (بيزود الـ venous drainage من الراس ويقلل الـ venous return من الرجلين)</td></tr>
<tr><td>PND</td><td>paroxysmal nocturnal dyspnea</td></tr>
<tr><td>Platypnea</td><td>dyspnea في الـ <b>upright</b> position (مرتاح وهو نايم)</td></tr>
<tr><td>Trepopnea</td><td>dyspnea في lateral decubitus على جنب واحد (asymmetrical lung disease)</td></tr>
<tr><td>Hemoptysis / hematemesis / epistaxis</td><td>دم مع الكحة / ترجيع دم / دم من الأنف</td></tr>
<tr><td>Cachexia</td><td>general physical wasting (فقد العضلات)</td></tr>
<tr><td>Hoarseness</td><td>abnormal voice</td></tr>
<tr><td>Wheezing</td><td>تزييق مع النفس بسبب ضيق الصدر</td></tr></table></div>

<div class="card"><h4>General examination</h4>
<p><b>Consciousness: Glasgow Coma Scale</b> (من 3 لـ 15). Mild 13–15، moderate 9–12، severe 3–8.</p>
<table><tr><th>Eye (4)</th><th>Verbal (5)</th><th>Motor (6)</th></tr>
<tr><td class="ltr">4 Spontaneous<br>3 To speech<br>2 To pain<br>1 None</td><td class="ltr">5 Orientated<br>4 Confused<br>3 Words<br>2 Incomprehensible sounds<br>1 None</td><td class="ltr">6 Obeys commands<br>5 Localizes pain<br>4 Withdrawal<br>3 Normal (abnormal) flexion<br>2 Extension<br>1 None</td></tr></table>
<table><tr><th>البند</th><th>إيه اللي بنشوفه</th></tr>
<tr><td>Decubitus (body position)</td><td>Orthopnea: long sitting أو half supine 45° (semi-Fowler). COPD/asthma: <b>leaning forward</b>. Pericarditis: <b>prayer position</b>. Fallot's: <b>squatting</b>. Trepopnea: ينام على الجنب السليم</td></tr>
<tr><td>Body built</td><td>Obese: CAD و chronic bronchitis (<b>blue bloater</b>). Underweight/cachexia: TB و carcinoma و emphysema (<b>pink puffer</b>). Belly: splenomegaly، hepatomegaly، ascites</td></tr>
<tr><td>Face</td><td>Moon face: Cushing's. Pale: anemia. Yellow: jaundice. Blue: cyanosis. Depressed expression: nasal flare و sweating و dilated pupils (hypoxia)</td></tr>
<tr><td>Eye</td><td>Sclera صفرا: jaundice. حمرا: chronic cough أو hypertension. Puffy eyelids: edema (chronic HTN أو RHF)</td></tr>
<tr><td>Neck</td><td>Congested neck veins: right side heart failure. Accessory muscles spasm: dyspnea</td></tr></table></div>

<div class="card"><h4>Cyanosis</h4>
<p>Bluish discoloration of skin و mucous membrane بسبب زيادة الـ <b>reduced (deoxygenated) Hb</b> عن <b>5 g/100 ml</b>.</p>
<table><tr><th></th><th>Central</th><th>Peripheral</th></tr>
<tr><td>السبب</td><td>مشكلة في القلب (VSD) أو الرئة (gas exchange)، يعني <b>hypoxemia</b></td><td><b>Hypoxia</b> مش hypoxemia: vasoconstriction، Raynaud's، برد، low cardiac output، obstruction of small arteries</td></tr>
<tr><td>المكان</td><td><b>Tongue</b>، inner lips، mucous membranes</td><td>Fingers، toes، outer lips، ear lobe، tip of nose</td></tr>
<tr><td>الجلد</td><td>Warm</td><td>Cold</td></tr>
<tr><td>Heat / massage / exercise</td><td>مش بتتحسن، والـ exercise بيسوّءها</td><td>بتتحسن</td></tr>
<tr><td>O₂ mask</td><td>بتتحسن</td><td>مالوش تأثير</td></tr></table>
<p>أهم فرق: الـ <b>tongue</b>. وفيه كمان <b>chemical cyanosis</b> (عيب في الـ Hb) و <b>differential cyanosis</b> (الرجلين بس) في الـ <b>patent ductus arteriosus</b>.</p></div>

<div class="card"><h4>Clubbing و Edema</h4>
<ul><li><b>Clubbing</b>: hypertrophy/hyperplasia of connective tissue of the nail bed بسبب chronic hypoxia أو toxemia. الأسباب: lung cancer، interstitial lung disease، cystic fibrosis، bronchiectasis، cyanotic congenital heart disease، endocarditis.</li>
<li><b>Schamroth's (diamond) test</b>: المريض يحط ضوافر صوابع الـ index ضهر لضهر. الطبيعي فيه diamond-shaped window، وفي الـ clubbing بيختفي.</li></ul>
<table><tr><th>Grade</th><th>الوصف</th></tr>
<tr><td>1</td><td>Window/angle lost</td></tr><tr><td>2</td><td>Parrot beak appearance</td></tr><tr><td>3</td><td>Drum stick (زيادة سمك الـ nail bed والـ distal phalanx)</td></tr><tr><td>4</td><td>Pulmonary (hypertrophic) osteoarthropathy: الالتهاب وصل للـ wrist والـ ankle</td></tr></table>
<p><b>Edema</b>: بنقيسه بالـ tape measurement، أو water displacement، أو مقارنة unilateral و bilateral، أو <b>pressure test</b> بالإبهام لمدة ثانيتين على الأقل على bony landmark (من distal لـ proximal: dorsum of foot، malleoli، tibia).</p>
<table><tr><th>Grade</th><th>Pitting</th></tr>
<tr><td>0</td><td>Non-pitting</td></tr><tr><td>+1</td><td>2 mm، بيختفي بسرعة</td></tr><tr><td>+2</td><td>4 mm، 10–15 sec</td></tr><tr><td>+3</td><td>6 mm، أكتر من دقيقة</td></tr><tr><td>+4</td><td>8 mm، أكتر من دقيقتين</td></tr></table>
<p><b>Treatment</b>: elevation (بحذر مع مريض القلب لأنها بتزود الـ venous return)، compression (elastic bandage)، ice، deep flexion massage، و active/passive exercises.</p></div>

<div class="card"><h4>Accessory muscles</h4>
<table><tr><th>Inspiration</th><th>Expiration</th></tr>
<tr><td class="ltr">Sternocleidomastoid<br>Upper trapezius<br>Subclavius<br>External intercostals<br>Serratus anterior<br>Pectoralis major &amp; minor (+ scalenes)</td><td class="ltr">Internal intercostals<br>Abdominal muscles<br>Latissimus dorsi<br>Pelvic floor</td></tr></table></div>
""",
[
 ("History", [
  ("The chief complaint should be written:", ["In the patient's own words without medical terms", "As a medical diagnosis", "As the lab result", "In Latin terms"], "imp", ""),
  ("Analysis of the chief complaint includes all EXCEPT:", ["Smoking index", "Onset", "Course", "Duration"], "", ""),
  ("Course of the complaint may be:", ["Progressive, regressive, stationary or relapsing", "Sudden or gradual", "Acute only", "Positive or negative"], "", "الـ sudden أو gradual ده الـ onset."),
  ("Cystic fibrosis is a disease that occurs mainly in:", ["Children (genetic)", "Old smokers", "Coal workers", "Pregnant women"], "", ""),
  ("Senile emphysema and COPD occur mainly in:", ["Old people / old smokers", "Infants", "Young athletes", "Children"], "", ""),
  ("Silicosis is caused by inhalation of:", ["Silica", "Coal dust", "Asbestos fibers", "Cotton dust"], "imp", ""),
  ("Pneumoconiosis (black lung) is caused by inhalation of:", ["Coal dust", "Silica", "Asbestos", "Smoke only"], "imp", ""),
  ("Smoking index is calculated as:", ["Cigarettes per day × years of smoking", "Packs per day ÷ years", "Cigarettes per day ÷ 20", "Years of smoking only"], "imp", ""),
  ("A smoking index of more than 400 indicates:", ["Heavy smoker", "Mild smoker", "Moderate smoker", "Non-smoker"], "imp", ""),
  ("A patient smoking 20 cigarettes/day for 15 years has a smoking index of:", ["300 (moderate smoker)", "150 (mild)", "450 (heavy)", "35"], "", "20 × 15 = 300."),
  ("Narcotics are dangerous for chest patients because they:", ["Inhibit the respiratory center", "Stimulate cough", "Increase vital capacity", "Dilate bronchi"], "", ""),
 ]),
 ("Symptoms", [
  ("Sharp superficial chest pain increasing with breathing and cough is:", ["Pleural pain", "Myocardial infarction pain", "Tracheal pain", "GERD pain"], "imp", ""),
  ("Chest pain occurring only with cough is:", ["Tracheal pain", "Pleural pain", "Cardiac pain", "Muscular pain"], "", ""),
  ("Compression chest pain is typical of:", ["Myocardial infarction", "Pleurisy", "Tracheitis", "Rib fracture"], "", ""),
  ("Patients with obstructive lung disease should be:", ["Encouraged to cough to clear sputum", "Prevented from coughing", "Given cough suppressants always", "Kept supine"], "", "والـ restrictive نثبط الكحة عندهم."),
  ("Frothy blood-tinged sputum indicates:", ["Pulmonary edema", "Asthma", "Bronchitis", "Silicosis"], "imp", ""),
  ("Yellow sputum indicates:", ["Bacterial (pyogenic) infection", "Normal", "Pulmonary edema", "Smoking"], "", ""),
  ("Watery salty sputum is seen in:", ["Alveolar carcinoma", "Asthma", "Lung abscess", "Pneumonia"], "", ""),
  ("Mucoid (tenacious) sputum is seen in:", ["Bronchitis and asthma", "Lung abscess", "Pulmonary edema", "Bronchogenic carcinoma"], "", ""),
  ("Sputum with pus is seen in:", ["Lung abscess (suppurative lung disease)", "Asthma", "Pulmonary edema", "COVID-19"], "", ""),
  ("Orthopnea is dyspnea:", ["In the flat position, relieved by sitting or standing", "In the upright position", "On one lateral side", "Only on exertion"], "imp", ""),
  ("Platypnea is dyspnea:", ["In the upright position", "In the flat position", "At night only", "On exertion"], "imp", ""),
  ("Trepopnea is dyspnea:", ["In one lateral decubitus position (asymmetrical lung disease)", "In the flat position", "In the upright position", "On exertion"], "imp", ""),
  ("Epistaxis means:", ["Bleeding from the nose", "Coughing blood", "Vomiting blood", "Blood in urine"], "", ""),
  ("Cachexia means:", ["General physical wasting (loss of muscle mass)", "Abnormal voice", "Blood in sputum", "Swelling of the ankles"], "", ""),
 ]),
 ("General examination", [
  ("The Glasgow Coma Scale assesses:", ["Eye opening, verbal response and motor response", "Pulse, BP and RR", "Muscle power", "Pain intensity"], "imp", ""),
  ("The maximum score of the eye opening response in GCS is:", ["4", "5", "6", "3"], "", ""),
  ("The maximum score of the verbal response in GCS is:", ["5", "4", "6", "3"], "", ""),
  ("The maximum score of the motor response in GCS is:", ["6", "5", "4", "3"], "", ""),
  ("A confused patient scores …… in the verbal response:", ["4", "5", "3", "2"], "", ""),
  ("Severe impairment of consciousness on GCS is:", ["3–8", "13–15", "9–12", "15 only"], "", ""),
  ("COPD and asthma patients usually adopt:", ["Leaning forward position", "Prayer position", "Squatting", "Flat supine"], "imp", ""),
  ("Pericarditis patients adopt the:", ["Prayer position", "Squatting position", "Flat position", "Leaning backward"], "", ""),
  ("Children with Fallot's tetralogy adopt:", ["Squatting", "Prayer position", "Leaning forward", "Orthopnea position"], "", ""),
  ("'Blue bloater' refers to:", ["Obese patient with chronic bronchitis", "Thin patient with emphysema", "Patient with TB", "Patient with asthma"], "", ""),
  ("'Pink puffer' refers to:", ["Thin patient with emphysema", "Obese patient with chronic bronchitis", "Patient with pulmonary edema", "Child with cystic fibrosis"], "", ""),
  ("Moon face is seen in:", ["Cushing's syndrome", "Emphysema", "Anemia", "Jaundice"], "", ""),
  ("Congested neck veins indicate:", ["Right side heart failure", "Asthma", "Left side heart failure only", "Pneumonia"], "", ""),
 ]),
 ("Cyanosis, clubbing & edema", [
  ("Cyanosis appears when reduced hemoglobin exceeds:", ["5 g/100 ml", "1 g/100 ml", "15 g/100 ml", "0.5 g/100 ml"], "imp", ""),
  ("The best site to differentiate central from peripheral cyanosis is the:", ["Tongue", "Fingers", "Ear lobe", "Toes"], "imp", ""),
  ("Central cyanosis is characterized by:", ["Warm skin and improvement with O₂ mask", "Cold skin and improvement with heat", "Appearing only in the toes", "Disappearing with massage"], "imp", ""),
  ("Peripheral cyanosis improves with:", ["Heat, massage and exercise", "O₂ mask only", "Nothing", "Increasing exercise intensity only"], "imp", ""),
  ("Differential cyanosis (lower limbs only) is seen in:", ["Patent ductus arteriosus", "VSD", "Emphysema", "Raynaud's disease"], "", ""),
  ("Peripheral cyanosis may be caused by:", ["Cold, vasoconstriction, Raynaud's and low cardiac output", "VSD", "Severe lung disease only", "High altitude only"], "", ""),
  ("Schamroth's test is used to assess:", ["Finger clubbing", "Cyanosis", "Edema", "Tracheal shift"], "imp", ""),
  ("In Schamroth's test, clubbing is detected by:", ["Loss of the diamond-shaped window between the index nails", "Appearance of a window", "Cyanosis of the nails", "Pain on pressure"], "", ""),
  ("Clubbing grade 2 is:", ["Parrot beak appearance", "Drum stick appearance", "Loss of nail angle only", "Osteoarthropathy"], "imp", ""),
  ("Clubbing grade 3 is:", ["Drum stick appearance", "Parrot beak", "Window lost only", "Osteoarthropathy of wrist and ankle"], "", ""),
  ("Clubbing grade 4 is:", ["Pulmonary (hypertrophic) osteoarthropathy", "Drum stick", "Parrot beak", "Normal nail"], "", ""),
  ("In the edema pressure test, the thumb is pressed for at least:", ["2 seconds over a bony landmark", "1 minute over muscle", "10 minutes", "0.5 second"], "", ""),
  ("Pitting edema +2 is:", ["4 mm depression disappearing after 10–15 seconds", "2 mm disappearing rapidly", "6 mm lasting more than a minute", "8 mm lasting more than 2 minutes"], "imp", ""),
  ("Pitting edema +4 is:", ["8 mm depression lasting more than 2 minutes", "2 mm disappearing rapidly", "4 mm for 10–15 sec", "Non-pitting"], "", ""),
  ("Accessory muscles of inspiration include all EXCEPT:", ["Internal intercostals", "Sternocleidomastoid", "Upper trapezius", "Pectoralis minor"], "imp", "الـ internal intercostals accessory للـ expiration."),
  ("Accessory muscles of expiration include:", ["Internal intercostals, abdominals, latissimus dorsi and pelvic floor", "SCM and scalenes", "Upper trapezius", "External intercostals"], "", ""),
 ]),
])

# ===================================================================== 4. Inspection
T("insp", "Local Examination — Inspection", "Inspection", "👁️",
  "سكشن 4 (د. فاطمة + Cardiovascular PT Practical 2)",
"""
<div class="card"><h4>ترتيب الـ local examination</h4>
<p class="ltr"><b>Inspection → Palpation → Percussion → Auscultation</b></p>
<p>الـ Inspection بالعين بس. بنبص على: neck (congested veins، neck muscle spasm أو atrophy)، chest wall deformities، surgical أو traumatic scars، skin (scars، hematoma، لون)، axillary و neck lymph nodes، شكل الصدر، وحركته.</p></div>

<div class="card"><h4>Normal chest</h4>
<ul><li>Elliptical و symmetrical.</li>
<li>3 diameters: <b>transverse</b>، <b>AP</b>، و <b>vertical</b> (من الـ diaphragm لأعلى نقطة في الصدر).</li>
<li><b>AP ≈ نص الـ transverse</b> (1 : 2، وفي كتب 5 : 7). الـ transverse أكبر من الـ AP.</li>
<li>الضلوع نازلة <b>downward و lateral</b> (حوالي 45° من الـ spine)، والـ intercostal spaces صغيرة.</li>
<li>الـ <b>subcostal (infrasternal) angle</b> حوالي 90° أو أقل.</li>
<li>الـ thoracic spine فيه slight kyphosis.</li></ul></div>

<div class="card"><h4>Abnormalities of chest shape</h4>
<table><tr><th>Symmetrical</th><th>الوصف</th></tr>
<tr><td>Barrel chest</td><td>الـ AP = الـ transverse، والضلوع horizontal، والـ intercostal spaces واسعة. سببه chronic lung disease زي COPD و emphysema</td></tr>
<tr><td>Flat chest</td><td>الـ AP قل، وممكن winging of scapula. في الـ bilateral fibrosis أو collapse (TB)</td></tr>
<tr><td>Funnel chest (pectus excavatum)</td><td>retraction of lower end of sternum، والـ AP بيقل. Congenital أو acquired (زي الـ shoemaker)</td></tr>
<tr><td>Pigeon chest (pectus carinatum)</td><td>protrusion of sternum، والـ AP بيزيد. Rickets، و acquired في الـ COPD و emphysema</td></tr>
<tr><td>Rachitic rosary</td><td>hypertrophy عند الـ costochondral junctions زي السبحة (rickets)</td></tr>
<tr><td>Harrison's sulcus</td><td>depression في الـ lateral lower ribs عند insertion الـ diaphragm (rickets، chronic respiratory distress)</td></tr>
<tr><td>Kyphosis / scoliosis / kyphoscoliosis</td><td>الـ kyphoscoliosis بيعمل <b>restrictive lung defect</b> ولو شديد يوصل لـ respiratory failure</td></tr></table>
<table><tr><th>Asymmetrical</th><th>الأسباب</th></tr>
<tr><td>Unilateral bulge</td><td>pleural effusion، pneumothorax، hemothorax، empyema، tumor، pericardial effusion</td></tr>
<tr><td>Unilateral retraction</td><td>collapse، atelectasis، fibrosis، adhesion، thoracoplasty</td></tr></table></div>

<div class="card"><h4>Movement of the chest</h4>
<ul><li>Rate (12–16 لحد 20)، rhythm (منتظم)، depth، pattern، و accessory muscles.</li>
<li>نسبة <b>I : E = 1 : 2</b>. في الـ COPD بتوصل 1 : 3 أو 1 : 4 (الزفير طويل).</li>
<li><b>Pursed-lip breathing</b> في الـ emphysema/COPD: بيعمل back pressure يفتح الـ airway ويمنع الـ collapse.</li>
<li>الـ thoracic surgery بتقلل الـ expansion في جنب واحد، والـ pulmonary fibrosis بتخلي الـ chest wall rigid.</li>
<li><b>Litten sign</b>: shadow of diaphragmatic descent على الـ chest wall (inward movement في الضلوع السفلية) مع الشهيق. بيختفي في diaphragmatic paralysis، pleural effusion، emphysema/COPD، والسمنة.</li></ul></div>

<div class="card"><h4>Scars، trachea و lymph nodes</h4>
<table><tr><th>Scar</th><th>العملية</th></tr>
<tr><td>Median sternotomy</td><td>open heart surgery</td></tr>
<tr><td>Postero-lateral thoracotomy</td><td>lung surgery</td></tr>
<tr><td>Left infraclavicular</td><td>pacemaker</td></tr></table>
<ul><li>الـ <b>Trachea</b> central بين الـ 2 tendons بتوع الـ SCM. <b>Trail's sign</b>: tendon الـ SCM بارز في ناحية، وده معناه إن الـ trachea عملت shift لنفس الناحية.</li>
<li><b>Neck lymph nodes</b>: submental، submandibular، occipital، pre- و post-auricular. <b>Axillary</b>: anterior، posterior، lateral، central.</li>
<li>الـ <b>Jugular vein</b> lateral للـ SCM. الطبيعي مفيهوش pulse، ولو congested ومتمدد يبقى right heart failure.</li></ul></div>

<div class="card"><h4>Anatomical lines و regions</h4>
<ul><li><b>Anterior</b>: mid-sternal، mid-clavicular، parasternal (في النص بينهم).</li>
<li><b>Lateral</b>: anterior، mid، و posterior axillary lines.</li>
<li><b>Posterior</b>: scapular line، paravertebral (بين الـ scapula والـ spine)، vertebral.</li>
<li><b>Regions</b>: anterior (supramammary، mammary، inframammary)، posterior (suprascapular، scapular، interscapular، infrascapular)، lateral (upper و lower lateral).</li></ul></div>
""",
[
 ("Normal chest & order", [
  ("The correct order of local chest examination is:", ["Inspection → Palpation → Percussion → Auscultation", "Palpation → Inspection → Auscultation → Percussion", "Auscultation → Percussion → Palpation → Inspection", "Percussion → Palpation → Inspection → Auscultation"], "imp", ""),
  ("In the normal chest, the AP diameter is about …… the transverse diameter:", ["Half", "Equal to", "Double", "Three times"], "imp", ""),
  ("In the normal adult chest, the ribs:", ["Descend downward and laterally (about 45°)", "Are horizontal", "Ascend upward", "Are vertical"], "", ""),
  ("The three diameters of the chest are:", ["Transverse, AP and vertical", "Apical, middle and basal", "Anterior, lateral and posterior", "Upper, middle and lower"], "", ""),
  ("The normal thoracic spine has:", ["Slight kyphosis", "Lordosis", "Scoliosis", "No curve"], "", ""),
 ]),
 ("Chest deformities", [
  ("In barrel chest:", ["AP diameter equals transverse diameter with horizontal ribs", "AP is half the transverse", "Sternum is depressed", "Unilateral retraction"], "imp", ""),
  ("Barrel chest is associated with:", ["COPD / emphysema", "Rickets", "Pleural effusion", "Fibrosis"], "imp", ""),
  ("Funnel chest (pectus excavatum) is:", ["Retraction of the lower end of the sternum", "Protrusion of the sternum", "Increased AP diameter", "Unilateral bulge"], "imp", ""),
  ("Pigeon chest (pectus carinatum) is:", ["Protrusion of the sternum with increased AP diameter", "Depression of the sternum", "Flat chest", "Lateral spinal curvature"], "", ""),
  ("Rachitic rosary is hypertrophy at the:", ["Costochondral junctions (rickets)", "Sternoclavicular joint", "Spinous processes", "Nail bed"], "", ""),
  ("Harrison's sulcus is a depression of the:", ["Lateral lower ribs at the diaphragm insertion", "Sternum", "Clavicle", "Upper ribs"], "", ""),
  ("Kyphoscoliosis may cause:", ["Restrictive lung defect and respiratory failure", "Obstructive lung disease", "Barrel chest", "Clubbing"], "", ""),
  ("Flat chest is seen in:", ["Bilateral fibrosis or collapse (e.g. TB)", "Emphysema", "Rickets only", "Pleural effusion"], "", ""),
  ("Unilateral bulge of the chest is caused by:", ["Pleural effusion or pneumothorax", "Fibrosis", "Collapse", "Thoracoplasty"], "imp", ""),
  ("Unilateral retraction of the chest is caused by:", ["Collapse, fibrosis or thoracoplasty", "Pneumothorax", "Pleural effusion", "Empyema"], "imp", ""),
 ]),
 ("Movement, scars & signs", [
  ("The normal ratio of inspiration to expiration is:", ["1 : 2", "1 : 1", "2 : 1", "1 : 4"], "imp", "في الـ COPD بتوصل 1 : 3 أو 1 : 4."),
  ("Pursed-lip breathing is seen in:", ["Emphysema / COPD", "Pneumonia", "Pleural effusion", "Fibrosis"], "", ""),
  ("Litten sign is the shadow of:", ["Diaphragmatic descent on the lower chest wall", "Tracheal shift", "Heart pulsation", "Rib fracture"], "imp", ""),
  ("Litten sign is absent in all EXCEPT:", ["Normal healthy thin person", "Diaphragmatic paralysis", "Pleural effusion", "Emphysema"], "", ""),
  ("A median sternotomy scar indicates:", ["Open heart surgery", "Pacemaker insertion", "Lung lobectomy", "Chest tube"], "imp", ""),
  ("A left infraclavicular scar indicates:", ["Pacemaker insertion", "Open heart surgery", "Lobectomy", "Thoracoplasty"], "", ""),
  ("A postero-lateral thoracotomy scar indicates:", ["Lung surgery", "Pacemaker", "CABG", "Mastectomy"], "", ""),
  ("Trail's sign (prominent SCM tendon on one side) indicates:", ["Tracheal shift to the same side", "Tracheal shift to the opposite side", "Neck muscle spasm only", "Thyroid enlargement"], "imp", ""),
  ("The parasternal line lies:", ["Midway between the mid-sternal and mid-clavicular lines", "Lateral to the mid-clavicular line", "In the axilla", "Over the scapula"], "", ""),
 ]),
])

# ===================================================================== 5. Palpation, percussion, auscultation
T("ppa", "Palpation, Percussion & Auscultation", "Palpation · Percussion · Auscultation", "🖐️",
  "Cardiovascular PT Practical 3 + تفريغ د. فاطمة",
"""
<div class="card"><h4>Palpation: إيه اللي بنتحسه</h4>
<p>بنعمل palpation لكل الحاجات اللي شفناها في الـ inspection: chest wall tenderness، vital signs، neck muscles، neck veins، lobe motion (expansion)، symmetry of chest wall muscles، deformity، apex beat، و trachea position.</p>
<ul><li><b>Chest deformity / tenderness</b>: المريض <b>sitting</b> relaxed والمعالج <b>قدامه</b>. بالـ palms أو طرف الـ index من فوق الـ clavicles ونازل لتحت الضلع الـ 12، وبعدين lateral و anterior. بندور على asymmetry و nodules و tenderness و deformity.</li></ul>
<table><tr><th>Grade</th><th>Tenderness</th></tr>
<tr><td>0</td><td>No tenderness</td></tr><tr><td>1</td><td>Complains of pain</td></tr><tr><td>2</td><td>Pain + winces</td></tr><tr><td>3</td><td>Pain + winces + withdraws</td></tr><tr><td>4</td><td>Severe pain، مش بيسمح باللمس</td></tr></table>
<p>Tenderness في الضلوع: osteomyelitis أو fracture. في العضلة: myositis. في الـ sternum: leukemia.</p></div>

<div class="card"><h4>Trachea و Apex beat</h4>
<ul><li>الـ trachea بتبعد <b>away</b> عن: <b>tension pneumothorax</b>، tumor، و large pleural effusion.</li>
<li>والـ trachea بتتشد <b>towards</b>: lobar collapse، atelectasis، pneumonectomy (و fibrosis).</li>
<li>الـ palpation بتاعة الـ trachea ممكن تبقى مزعجة، فحذّر المريض واشتغل بلطف. الطبيعي يدخل صباعين بين الـ trachea والـ SCM في الناحيتين بنفس المسافة.</li>
<li>في الـ tension pneumothorax الهوا بيدخل الـ pleura زي one-way valve، فالرئة تعمل collapse والـ mediastinum يعمل shift للجنب السليم.</li>
<li><b>Apex beat</b>: left 5th ICS، mid-clavicular line. لو مش حاسس بيه خلي المريض side lying على الشمال.</li></ul></div>

<div class="card"><h4>Chest expansion</h4>
<p>بيتعمل segmental والمريض بيتنفس، ونقارن الناحيتين. الطبيعي عمومًا <b>1–3 cm</b> في الـ quiet breathing و <b>3–5 cm</b> في الـ deep breathing. والقياس بيبدأ من آخر الزفير وبعدين deep inspiration، وتقيس المسافة بين الإبهامين.</p>
<table><tr><th>المستوى</th><th>مكان الإيد</th><th>الطبيعي (deep)</th></tr>
<tr><td>Apical</td><td>half supine. الصوابع فوق الـ clavicle والإبهامين ناحية الـ sternal notch</td><td>حوالي 1 cm هادي و 3 cm deep (د. فاطمة: 1–2 cm)</td></tr>
<tr><td>Upper lobe</td><td>الإبهامين عند الـ angle of Louis (2nd rib)</td><td>2–3 cm</td></tr>
<tr><td>Middle lobe</td><td>الـ web space تحت الـ nipple والإبهامين ناحية الـ xiphoid</td><td>3–5 cm</td></tr>
<tr><td>Posterior basal (lower lobe)</td><td>تحت الـ inferior angle of scapula والإبهامين ناحية الـ spinous processes</td><td>5–7 cm</td></tr></table>
<ul><li><b>Symmetrical (bilateral) reduction</b>: diffuse pulmonary fibrosis، bronchial asthma، emphysema/COPD.</li>
<li><b>Asymmetrical (unilateral) reduction</b>: pneumothorax، pneumonia، pleural effusion، collapse، fibrosis في جنب واحد.</li></ul></div>

<div class="card"><h4>Tactile vocal fremitus (TVF)</h4>
<ul><li>Vibration بيطلع من الصوت وبيتنقل لجدار الصدر ونحسه بالإيد. المريض يقول <b>"99"</b> (أو "44" بالعربي)، وانت حاطط الـ hypothenar (ulnar aspect) أو الـ palms على الناحيتين (upper، middle، lower) من قدام وورا، وتقارن.</li>
<li>الصوت بيتنقل في الـ solid أحسن من الـ air.</li>
<li><b>Increased TVF</b>: زيادة الـ tissue density، زي consolidation و pneumonia و tumor و cavitation و lung abscess.</li>
<li><b>Decreased TVF</b>: fluid أو air برة الرئة، زي pleural effusion و pneumothorax و pleural fibrosis/thickening و emphysema، وكمان obstructed airway.</li></ul></div>

<div class="card"><h4>Percussion</h4>
<ul><li>Technique بيقيّم الـ <b>air/solid ratio</b>، وبيتعمل على الـ <b>intercostal spaces</b> (مش على العظم)، وبنبدأ من الجنب السليم.</li>
<li>الطريقة: الـ <b>middle finger</b> بتاع الإيد الـ non-dominant مضغوط على الصدر، والـ middle finger بتاع الإيد الـ dominant يخبط على الـ <b>middle phalanx</b> بحركة من الـ <b>wrist</b>، ويترفع بسرعة عشان الصوت ميتكتمش.</li>
<li>Heavy percussion للضهر (structure تقيلة)، و light percussion لباقي الصدر.</li></ul>
<table><tr><th>Note</th><th>المعنى</th></tr>
<tr><td>Resonant</td><td>Normal</td></tr>
<tr><td>Hyper-resonant</td><td>هوا أكتر من الطبيعي: emphysema/COPD</td></tr>
<tr><td>Tympanic</td><td>pneumothorax (هوا في الـ pleura)، وطبيعي فوق الـ Traube's area (fundus of stomach)</td></tr>
<tr><td>Impaired note / Dullness</td><td>tissue density زادت: consolidation، secretions، tumor، fibrosis، collapse</td></tr>
<tr><td>Stony dullness</td><td><b>Pleural effusion</b></td></tr></table>
<ul><li>Cardiac dullness على الشمال من الـ 4th لـ 6th ICS (bare area of heart).</li>
<li>Liver dullness عند الـ <b>right 5th ICS</b> (mid-clavicular). لو بدأت من الـ 4th يبقى hepatomegaly أو lung fibrosis شدت الكبد لفوق.</li>
<li>لو الـ Traube's area بقت dull يبقى فيه مشكلة (splenomegaly، hepatomegaly، tumor).</li></ul></div>

<div class="card"><h4>Diaphragmatic excursion</h4>
<ul><li>حركة الـ diaphragm أثناء التنفس، والطبيعي <b>5–7 cm</b>.</li>
<li>المريض ياخد نفس عميق ويكتمه، وتعمل percussion ناحية تحت (تحت الـ scapula) لحد ما الصوت يتحول من resonant لـ dull، وتعلّم: ده الـ <b>lower level</b>. بعدين يطلع نفسه للآخر ويكتمه، وتعمل percussion تاني وتعلّم: ده الـ <b>upper level</b>. المسافة بينهم هي الـ excursion، وتعيد في الناحية التانية.</li>
<li><b>High (fixed) diaphragm</b>: pregnancy، ascites، زيادة الضغط في البطن. <b>Low diaphragm</b>: emphysema.</li></ul></div>

<div class="card"><h4>Auscultation</h4>
<p>بالـ <b>diaphragm</b> بتاع السماعة، عشان: نحدد مناطق الـ congestion اللي محتاجة <b>postural drainage</b>، ونعرف هل الـ PD كان مفيد، وهل الرئة نضفت ونقدر نوقفه.</p>
<table><tr><th>Normal sound</th><th>المكان</th><th>الصفة</th><th>I : E</th></tr>
<tr><td>Tracheal</td><td>فوق الـ trachea (suprasternal notch)</td><td>loud، harsh، very high pitched</td><td>I = E</td></tr>
<tr><td>Bronchial</td><td>جنب الـ sternum</td><td>loud، hollow، tubular، high pitched، والـ expiration أطول</td><td>2 : 3</td></tr>
<tr><td>Bronchovesicular</td><td>1st و 2nd ICS (جنب الـ main bronchi) وبين الـ scapulae من ورا</td><td>أنعم، breezy</td><td>1 : 1</td></tr>
<tr><td>Vesicular</td><td>معظم الرئة، وأوضح عند الـ bases والـ periphery</td><td>soft، swishy، والـ inspiration أطول بكتير</td><td>3 : 1</td></tr></table>
<p><b>Absent</b> breath sounds: total airway obstruction. <b>Diminished</b>: bronchospasm (asthma)، atelectasis، emphysema، أو blockage بالإفرازات (pneumonia).</p>
<table><tr><th>Adventitious</th><th>الوصف</th></tr>
<tr><td>Rales (fine)</td><td>fine crackling (زي فرك الشعر جنب الودن) في الـ <b>inspiration</b>: secretions في الـ <b>distal</b> airways</td></tr>
<tr><td>Rhonchi</td><td>coarse popping في الـ inspiration أو expiration: congestion في الـ <b>proximal</b> airways، و<b>بتروح مع الكحة</b></td></tr>
<tr><td>Wheezing</td><td>high pitched في الـ <b>expiration</b> بسبب ضيق الـ lumen (bronchospasm)، و<b>مبتروحش بالكحة</b></td></tr>
<tr><td>Crackles / crepitations</td><td>هوا بيعدي على wet alveoli (pulmonary edema)، في الـ <b>basal areas</b> بسبب الجاذبية</td></tr>
<tr><td>Pleural rub</td><td>احتكاك بين طبقتين الـ pleura (pleurisy)، خصوصًا lateral</td></tr>
<tr><td>Snoring</td><td>obstruction بسبب malposition</td></tr>
<tr><td>Stridor</td><td>high pitched <b>extra-thoracic</b> sound من upper airway ضيق: foreign body (acute) أو subglottic stenosis (chronic)</td></tr></table></div>
""",
[
 ("Palpation", [
  ("Examination of chest tenderness is done with the patient:", ["Sitting, therapist in front", "Prone, therapist behind", "Supine, therapist at the head", "Standing, therapist behind"], "", ""),
  ("Tenderness grade 2 is:", ["Pain and winces", "Pain only", "Pain, winces and withdraws", "No tenderness"], "imp", ""),
  ("Tenderness grade 3 is:", ["Pain, winces and withdraws", "Pain only", "Pain and winces", "No pain"], "", ""),
  ("The trachea deviates AWAY from:", ["Tension pneumothorax, tumor and large pleural effusion", "Collapse and atelectasis", "Pneumonectomy", "Fibrosis"], "imp", ""),
  ("The trachea deviates TOWARDS:", ["Lobar collapse, atelectasis and pneumonectomy", "Tension pneumothorax", "Large pleural effusion", "Tumor"], "imp", ""),
  ("Normal chest expansion during deep breathing (general) is:", ["3–5 cm", "0.5 cm", "10 cm", "1 mm"], "", ""),
  ("Normal posterior basal (lower lobe) expansion is:", ["5–7 cm", "1 cm", "2–3 cm", "10–12 cm"], "imp", ""),
  ("For middle lobe expansion, the thumbs are directed toward the:", ["Xiphoid process", "Sternal notch", "Spinous processes", "Clavicle"], "", ""),
  ("For apical expansion, the thumbs are directed toward the:", ["Sternal notch", "Xiphoid process", "Spinous processes", "Nipples"], "", ""),
  ("For posterior basal expansion, the hands are placed:", ["Below the inferior angle of the scapula, thumbs toward the spinous processes", "Above the clavicle", "Under the nipple", "On the sternum"], "", ""),
  ("Symmetrical (bilateral) reduction of chest expansion occurs in:", ["Emphysema, asthma and diffuse fibrosis", "Pneumothorax", "Unilateral pleural effusion", "Lobar pneumonia"], "", ""),
  ("Unilateral reduction of chest expansion occurs in:", ["Pneumothorax, pleural effusion and collapse", "Emphysema", "Bronchial asthma", "Diffuse fibrosis"], "", ""),
  ("During TVF assessment the patient is asked to say:", ["'99' (or '44' in Arabic)", "'A' continuously", "Nothing (silent)", "Count from 1 to 100 quickly"], "", ""),
  ("TVF is increased in:", ["Consolidation (pneumonia) and tumor", "Pleural effusion", "Pneumothorax", "Emphysema"], "imp", ""),
  ("TVF is decreased in:", ["Pleural effusion and pneumothorax", "Consolidation", "Lung abscess", "Pneumonia"], "imp", ""),
  ("TVF is felt using the:", ["Hypothenar (ulnar aspect) or palm", "Fingertips only", "Stethoscope", "Thumb only"], "", ""),
 ]),
 ("Percussion & diaphragmatic excursion", [
  ("Percussion assesses the:", ["Air/solid ratio in the lungs", "Blood flow", "Muscle strength", "Breath sounds"], "imp", ""),
  ("Percussion is performed over the:", ["Intercostal spaces", "Ribs", "Sternum only", "Scapula"], "", ""),
  ("In percussion, the striking finger hits the:", ["Middle phalanx of the non-dominant middle finger", "Distal phalanx of the index", "Palm", "Rib directly"], "", ""),
  ("Normal lung percussion note is:", ["Resonant", "Dull", "Stony dull", "Tympanic"], "", ""),
  ("Stony dullness is typical of:", ["Pleural effusion", "Pneumothorax", "Emphysema", "Asthma"], "imp", ""),
  ("Hyper-resonance is found in:", ["Emphysema and pneumothorax", "Consolidation", "Pleural effusion", "Fibrosis"], "imp", ""),
  ("Dullness is found in:", ["Consolidation, tumor, fibrosis and collapse", "Emphysema", "Pneumothorax", "Normal lung"], "", ""),
  ("Normal liver dullness starts at the:", ["Right 5th intercostal space", "Left 5th intercostal space", "Right 2nd intercostal space", "Left 10th intercostal space"], "", "لو بدأت من الـ 4th يبقى hepatomegaly أو lung fibrosis."),
  ("Normal diaphragmatic excursion is:", ["5–7 cm", "1–2 cm", "10–15 cm", "0 cm"], "imp", ""),
  ("A high (fixed) diaphragm is seen in:", ["Pregnancy and ascites", "Emphysema", "Athletes", "Pneumothorax"], "", ""),
  ("A low diaphragm is seen in:", ["Emphysema", "Pregnancy", "Ascites", "Obesity"], "", ""),
  ("In diaphragmatic excursion, the lower level is marked after:", ["Deep inspiration and breath holding", "Forced expiration", "Normal breathing", "Coughing"], "", ""),
 ]),
 ("Auscultation", [
  ("Auscultation of breath sounds is done with the:", ["Diaphragm of the stethoscope", "Bell of the stethoscope", "Bare ear only", "Percussion hammer"], "", ""),
  ("Auscultation helps to identify areas that need:", ["Postural drainage", "Manipulation", "Bracing", "Traction"], "", ""),
  ("Vesicular breath sounds have an I:E ratio of:", ["3 : 1", "1 : 1", "2 : 3", "1 : 3"], "imp", ""),
  ("Bronchovesicular sounds have an I:E ratio of:", ["1 : 1", "3 : 1", "2 : 3", "1 : 2"], "imp", ""),
  ("Bronchial breath sounds have an I:E ratio of:", ["2 : 3 (expiration longer)", "3 : 1", "1 : 1", "1 : 4"], "imp", ""),
  ("Tracheal breath sounds are heard:", ["Over the trachea, harsh and very high pitched", "At the lung bases", "Between the scapulae only", "Over the liver"], "", ""),
  ("Vesicular sounds are best heard at the:", ["Lung bases and periphery", "Trachea", "Sides of the sternum", "Suprasternal notch"], "", ""),
  ("Bronchovesicular sounds are heard at the:", ["1st and 2nd intercostal spaces and between the scapulae", "Lung bases", "Over the trachea only", "Axilla only"], "", ""),
  ("Rhonchi indicate congestion of the …… airways and are cleared by:", ["Proximal / effective cough", "Distal / bronchodilator", "Alveoli / nothing", "Pleura / rest"], "imp", ""),
  ("Wheezing is a high pitched sound heard mainly on:", ["Expiration, due to bronchospasm and not cleared by cough", "Inspiration, cleared by cough", "Both phases, due to pleurisy", "Only during speech"], "imp", ""),
  ("Fine crackles at the lung bases due to wet alveoli are typical of:", ["Pulmonary edema", "Asthma", "Pneumothorax", "Pleurisy"], "", ""),
  ("Pleural rub is heard in:", ["Pleurisy (friction between pleural layers)", "Asthma", "Pulmonary edema", "Emphysema"], "imp", ""),
  ("Stridor is:", ["A high-pitched extra-thoracic sound from a narrowed upper airway", "A low-pitched sound from the alveoli", "A pleural sound", "A normal tracheal sound"], "imp", ""),
  ("Rales (fine crackles) on inspiration indicate:", ["Secretions in the distal airways", "Bronchospasm", "Pleural friction", "Upper airway obstruction"], "", ""),
  ("Absent breath sounds indicate:", ["Total airway obstruction", "Normal lung", "Mild asthma", "Bronchial breathing"], "", ""),
 ]),
])

# ===================================================================== 6. Cardiac history & general examination
T("card", "Cardiac History & General Cardiac Examination", "Cardiac Exam", "❤️",
  "Cardiovascular PT Practical 4 (آخر سكشن)",
"""
<div class="card"><h4>Personal history (cardiac)</h4>
<table><tr><th>البند</th><th>الأهمية</th></tr>
<tr><td>Age</td><td>Old: ischemic heart disease، MI، CAD. Adult: <b>rheumatic valve disease</b>. Young: <b>congenital</b> (Fallot's tetralogy)</td></tr>
<tr><td>Sex</td><td>الـ rheumatic heart disease أكتر في الستات</td></tr>
<tr><td>Occupation</td><td>الـ stress بيزود خطر الـ IHD</td></tr>
<tr><td>Residence</td><td>أمراض مرتبطة بالمكان (bilharzia، cor pulmonale)</td></tr>
<tr><td>Habits و smoking</td><td>الـ smoking بيزود الـ IHD</td></tr>
<tr><td>Diet، activity، socioeconomic state</td><td>—</td></tr></table>
<ul><li><b>Cor pulmonale</b>: respiratory disease أدت لـ heart disease، يعني <b>right ventricular hypertrophy</b>.</li>
<li><b>Fallot's tetralogy (4)</b>: pulmonary stenosis، RV hypertrophy، overriding of aorta، ventricular septal defect. الدم بيختلط فيحصل cyanosis، والطفل بيعمل <b>squatting</b>.</li>
<li><b>Risk factors of CHD</b>: hypertension، hyperlipidemia، diabetes، previous MI، sedentary life، male gender، elevated cholesterol، smoking.</li></ul></div>

<div class="card"><h4>Cardiac symptoms</h4>
<ul><li><b>Chest pain (angina)</b>: central، retrosternal، diffuse. بينتشر للـ left arm و shoulder و jaw و neck. إحساس ضغط "كأن حد قاعد على صدره". بيزيد مع المجهود ويروح بالراحة والـ <b>nitroglycerin</b> (sublingual)، ومدته دقايق. الـ <b>MI</b> بيستمر لحد 30 دقيقة وأكتر.</li>
<li><b>Dyspnea</b>: exertional، orthopnea (left side failure بتعمل pulmonary congestion)، و <b>PND</b> (بعد ساعة أو اتنين من النوم، left heart failure، وممكن مع frothy blood-tinged sputum). والأسوأ dyspnea at rest.</li>
<li><b>Palpitation</b>: awareness of heart beats، fluttering، "heart skipped a beat"، وغالبًا arrhythmias. ممكن تبقى طبيعية بعد الخوف أو المجهود أو القهوة.</li>
<li><b>Intermittent claudication</b>: cramp في الـ calf (ممكن للـ thigh أو الـ buttock) بعد مسافة معينة (claudication distance) بسبب نقص الـ blood supply. الـ calf هي "<b>the second heart</b>".</li>
<li><b>Syncope</b>: transient loss of consciousness بسبب cerebral anoxia. الـ <b>presyncope</b> ضعف من غير فقدان وعي. لو sudden من غير مقدمات غالبًا <b>arrhythmia</b>. لو مع المجهود: aortic stenosis أو HOCM.</li>
<li><b>Ankle swelling</b>: bilateral pitting dependent edema، بيزيد بالليل ويقل في الـ flat position، وده في الـ <b>congestive heart failure</b>. الـ unilateral ممكن lymphedema.</li>
<li><b>Fatigue</b> بسبب low cardiac output.</li></ul></div>

<div class="card"><h4>General cardiac examination</h4>
<table><tr><th>البند</th><th>إيه اللي بنشوفه</th></tr>
<tr><td>Mentality</td><td>orientation، memory، comprehension، level of consciousness (GCS)، الـ cooperation، والـ mood (الـ depression شائع في أمراض القلب، والـ anxiety أكتر في أمراض الصدر)</td></tr>
<tr><td>Decubitus</td><td>semi-Fowler، <b>squatting</b> (Fallot's)، <b>prayer / leaning forward</b> (pericarditis)</td></tr>
<tr><td>Body built</td><td><b>Thin</b>: left side HF (low CO). <b>Obese appearance</b>: right side HF (generalized edema). <b>Inverted pyramid</b>: coarctation of aorta. <b>Dwarfism</b>: congenital heart disease</td></tr>
<tr><td>Color</td><td><b>Malar flush</b> (احمرار الخدود والأنف): tight mitral stenosis. <b>Pale</b>: rheumatic fever. <b>Jaundice</b>. <b>Cyanosis</b></td></tr>
<tr><td>Nodules</td><td><b>Osler</b>: infective endocarditis، في الـ thenar و hypothenar، <b>tender</b>. <b>Subcutaneous</b>: rheumatic fever، على الـ extensor surfaces، <b>not tender</b></td></tr>
<tr><td>Rheumatic chorea</td><td>حركات involuntary jerky purposeless، أكتر في البنات</td></tr>
<tr><td>Clubbing</td><td>الـ angle الطبيعي للـ nail bed حوالي 160°</td></tr></table>
<p><b>Cyanosis types</b>: central (Fallot's، shunts)، بتزيد مع المجهود والحرارة وأي حاجة تزود الـ HR وبتقل بالراحة بس. Peripheral (atherosclerosis)، بتزيد مع البرد والراحة وبتقل مع المجهود والحرارة. Differential (الرجلين بس): <b>PDA</b>.</p></div>

<div class="card"><h4>Arterial vs venous pulsation و Hepatojugular reflux</h4>
<table><tr><th>Carotid (arterial)</th><th>Jugular (venous)</th></tr>
<tr><td><b>Medial</b> للـ SCM</td><td><b>Lateral</b> للـ SCM</td></tr>
<tr><td>Better felt than seen</td><td>Better seen than felt</td></tr>
<tr><td>Synchronous مع ضربات القلب</td><td>بيتأثر بالـ position</td></tr>
<tr><td>مش بيتأثر بوضع المريض</td><td>الطبيعي مفيهوش pulse</td></tr></table>
<p><b>Hepatojugular (abdominojugular) reflux</b>: المريض long sitting والراس لافة للناحية التانية. تضغط على الكبد (right upper quadrant) وتبص على الـ jugular vein. لو اتملت ونبضت يبقى مشكلة في الكبد أو القلب.</p>
<p class="key">للتفرقة: مسطرة أفقية على الـ sternal notch ومسطرة رأسية عليها، وتقيس لحد مكان بداية النبض في الـ jugular. <b>أقل من 7 cm</b> يبقى hepatic problem. <b>7 cm أو أكتر</b> يبقى right side cardiac problem.</p></div>
""",
[
 ("Cardiac history", [
  ("In young age, the most common cardiac diseases are:", ["Congenital anomalies (e.g. Fallot's tetralogy)", "Ischemic heart disease", "Rheumatic valve disease", "Atherosclerosis"], "imp", ""),
  ("In adults, the common cardiac disease is:", ["Valve disease due to rheumatic fever", "Congenital anomalies", "Myocardial infarction only", "Cor pulmonale only"], "", ""),
  ("Rheumatic heart disease is more common in:", ["Females", "Males", "Infants", "Athletes"], "", ""),
  ("Cor pulmonale is:", ["Right ventricular hypertrophy due to respiratory disease", "Left ventricular failure due to hypertension", "Rheumatic mitral stenosis", "Congenital VSD"], "imp", ""),
  ("Fallot's tetralogy includes all EXCEPT:", ["Left ventricular hypertrophy", "Pulmonary stenosis", "Overriding of aorta", "Ventricular septal defect"], "imp", "الـ hypertrophy في الـ right ventricle."),
  ("Typical anginal pain is relieved by:", ["Rest and sublingual nitroglycerin", "Exertion", "Deep breathing", "Lying on the affected side"], "imp", ""),
  ("Typical anginal pain radiates to the:", ["Left arm, shoulder, jaw and neck", "Right leg", "Lower back only", "Abdomen only"], "", ""),
  ("Paroxysmal nocturnal dyspnea occurs:", ["1–2 hours after sleep, due to left heart failure", "On waking in the morning", "During exercise only", "In the upright position"], "imp", ""),
  ("Orthopnea in cardiac patients is due to:", ["Left side failure causing pulmonary congestion", "Right side failure only", "Anemia", "Asthma"], "", ""),
  ("Intermittent claudication is:", ["Calf cramp after walking a certain distance due to decreased blood supply", "Chest pain at rest", "Ankle swelling at night", "Loss of consciousness"], "imp", ""),
  ("The 'second heart' refers to the:", ["Calf muscle", "Diaphragm", "Liver", "Spleen"], "", ""),
  ("Syncope of sudden onset without warning is most likely due to:", ["Arrhythmia", "Vasovagal attack", "Hypoglycemia", "Anxiety"], "imp", ""),
  ("Exertional syncope may be due to:", ["Aortic stenosis or hypertrophic obstructive cardiomyopathy", "Asthma", "Hypothyroidism", "Anemia only"], "", ""),
  ("Cardiac edema is typically:", ["Bilateral pitting dependent, increasing in the evening", "Unilateral non-pitting", "Facial only", "Hard non-pitting with protein"], "imp", ""),
  ("Risk factors for coronary heart disease include all EXCEPT:", ["Regular physical activity", "Hypertension", "Diabetes mellitus", "Sedentary life"], "", "ومنهم كمان hyperlipidemia و male gender و smoking."),
 ]),
 ("General cardiac examination", [
  ("Squatting position is common in children with:", ["Fallot's tetralogy", "Pericarditis", "Mitral stenosis", "Heart failure"], "imp", ""),
  ("A thin patient with heart disease suggests:", ["Left side heart failure (low cardiac output)", "Right side heart failure", "Coarctation of aorta", "Hypertension"], "", ""),
  ("An obese appearance in a cardiac patient may be due to:", ["Right side heart failure with generalized edema", "Left side failure", "Mitral stenosis", "Endocarditis"], "", ""),
  ("Inverted pyramid body built is seen in:", ["Coarctation of the aorta", "Fallot's tetralogy", "Mitral stenosis", "Pericarditis"], "imp", ""),
  ("Malar flush indicates:", ["Tight mitral stenosis", "Aortic stenosis", "Rheumatic chorea", "Jaundice"], "imp", ""),
  ("Osler nodules are:", ["Tender nodules in the palm (thenar/hypothenar) in infective endocarditis", "Painless nodules on extensor surfaces in rheumatic fever", "Nodules in the eyelid", "Lymph nodes"], "imp", ""),
  ("Subcutaneous nodules of rheumatic fever are:", ["Not tender, on extensor surfaces of limbs", "Tender, in the palm", "On the eyelid", "In the liver"], "", ""),
  ("Rheumatic chorea is:", ["Involuntary jerky purposeless movements, common in females", "A type of cyanosis", "A heart murmur", "A painful nodule"], "", ""),
  ("Differential cyanosis (lower limbs only) is seen in:", ["Patent ductus arteriosus", "Fallot's tetralogy", "Mitral stenosis", "Atherosclerosis"], "", ""),
  ("The carotid pulsation is:", ["Medial to the SCM, better felt than seen, not affected by position", "Lateral to the SCM, better seen than felt", "Affected by position", "Absent normally"], "imp", ""),
  ("The jugular vein lies:", ["Lateral to the SCM", "Medial to the SCM", "Behind the trachea", "Under the clavicle"], "", ""),
  ("In the hepatojugular reflux test, pressure is applied over the:", ["Right upper quadrant (liver)", "Left upper quadrant", "Epigastrium only", "Neck"], "imp", ""),
  ("In the hepatojugular test, a distance of 7 cm or more indicates:", ["Right side cardiac problem", "Hepatic problem", "Normal finding", "Left side heart failure"], "imp", "أقل من 7 cm يبقى hepatic problem."),
  ("Normal nail bed angle is about:", ["160°", "90°", "200°", "45°"], "", ""),
 ]),
])
