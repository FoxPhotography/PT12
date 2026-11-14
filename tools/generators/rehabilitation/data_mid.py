# Principles of Rehabilitation — midterm compilation from the official slides REHABILITATION(1)(2) … (7).
# 100 easy MCQs + a simple summary. Built with ../common/build_simple.py
META = {'title': 'Rehabilitation — تجميعة الميد', 'badge': '🏥 Principles of Rehabilitation', 'h1': 'تجميعة الميد',
        'subtitle': 'Intro & Team · Disability · Handicap · Function assessment · FIM & Berg · Gait devices',
        'statnum': 7, 'statlabel': 'محاضرات'}
TABS = []
def T(*a): TABS.append(a)

SUMMARY = """
<div class="card"><h4>📌 اقرا دي الأول</h4>
<ul><li>الملخص والأسئلة من <b>سلايدات الدكتور الرسمية</b> (المحاضرات 1 لـ 7)، ومترتبين بنفس ترتيب المحاضرات.</li>
<li>الامتحان MCQ وسهل: احفظ <b>التعريفات والأرقام</b> المتعلّم عليها، وحل الـ 100 سؤال لحد ما تجيبهم صح.</li></ul></div>

<div class="card"><h4>1. Lec 1–2 — Rehabilitation, Settings &amp; Team</h4>
<ul><li><b>Rehabilitation</b> = إنك ترجّع الشخص اللي عنده disability <b>maximally able again</b> وتحسّن الـ functional capacities بتاعته.</li>
<li><b>الأهداف (3)</b>: يتأقلم ويرجع للمجتمع بإعاقته · يبقى <b>independent</b> و productive على قد ما يقدر · يحل مشاكله بنفسه.</li>
<li><b>بتتحقق بـ</b>: Teamwork approach (<b>as early as possible</b>) · Family involvement · Community support (health agencies، social welfare، <b>Ministry of Education</b>) · modern methods · أقصى restoration عشان يرجع شغله · مهارات جديدة لشغل جديد حسب الـ <b>residual disability</b>.</li>
<li><b>Inpatient rehabilitation</b>: المريض بيقعد جوه مستشفى أو مركز. 3 أشكال: unit جوه community hospital · مستشفى مستقلة (<b>freestanding</b>) · unit جوه medical academic center.</li>
<li>الـ <b>acute rehab unit</b>: دكاترة وتمريض موجودين طول الوقت، والمريض لازم يقدر على <b>3 ساعات therapy في اليوم</b> على الأقل. والـ medical director غالبًا <b>physiatrist</b>.</li>
<li><b>Home health</b>: خدمات في بيت المريض. الـ <b>homebound</b> = عنده "normal inability to leave home".</li>
<li><b>Transdisciplinary approach</b>: بيزوّد قوة الفريق ويقلل <b>duplication of services</b>، وبيتختار عضو واحد يبقى <b>primary therapist / leader</b>.</li></ul>
<table><tr><th>Level</th><th>مين؟</th></tr>
<tr><td>First — <b>Core members</b></td><td>بيشتغلوا مع بعض في نفس الـ unit كل يوم: physicians، nurses، social workers، PT و OT. هم اللي بيحطوا النظام.</td></tr>
<tr><td>Second — <b>Extended members</b></td><td>بيشتغلوا في أكتر من مكان: dieticians، pharmacists، psychiatrists/psychologists، speech therapists، dentists.</td></tr>
<tr><td>Third — <b>Consultants</b></td><td>الـ <b>core members</b> هم اللي بيقرروا يدخلوهم لما يحتاجوا.</td></tr></table>
<p class="key">العضو الجديد في الفريق: عادي جدًا <b>يقعد يسمع ويلاحظ</b> أول كام اجتماع.</p></div>

<div class="card"><h4>2. Lec 3 — Disability: definition, types &amp; models</h4>
<ul><li><b>Disability</b> = restriction or lack (<b>resulting from an impairment</b>) of ability to perform an activity بالشكل الطبيعي.</li></ul>
<table><tr><th>التصنيف</th><th>مثال</th></tr>
<tr><td>Temporary</td><td>fracture، أو شلل مؤقت بعد stroke</td></tr>
<tr><td>Permanent</td><td><b>blindness، amputation</b></td></tr>
<tr><td>From birth / Acquired</td><td>وراثي أو إصابة في الولادة / مرض أو حادثة بعدين</td></tr>
<tr><td>Progressive (بيسوء)</td><td><b>muscular dystrophy</b></td></tr>
<tr><td>Regressive (بيتحسن)</td><td>رجوع وظيفة الطرف بعد stroke بالـ physiotherapy</td></tr></table>
<ul><li><b>الأنواع (6)</b>: Physical · Sensory · Intellectual/cognitive · Mental/Psychiatric · Developmental · Invisible.</li>
<li>أسباب الـ physical: <b>Prenatal</b> (قبل الولادة) · <b>Perinatal</b> (أثناء الولادة: نقص O₂، forceps، premature) · <b>Postnatal</b> (بعد الولادة: accidents، infection).</li>
<li><b>Sensory</b>: أساسًا <b>vision و hearing</b>. الكفيف بيستخدم cane و <b>Braille</b>. الأصم <b>sign language</b> أو lip-read.</li>
<li><b>Ageusia</b> = فقد كامل للـ taste. <b>Dysgeusia</b> = taste غلط مستمر.</li>
<li><b>Balance</b> محتاج: eyes (visual) + ears (<b>vestibular</b>) + <b>proprioception</b>.</li>
<li><b>Cognitive</b>: نوعين = <b>learning disabilities</b> و <b>mental retardation</b>.</li>
<li><b>Developmental</b>: بتحصل <b>قبل سن 18</b>. الخمسة: Mental retardation، Cerebral palsy، Epilepsy، Autism، Neurological impairments.</li>
<li><b>Invisible</b>: مش باينة، زي renal failure، diabetes، asthma، AIDS، cancer.</li></ul>
<p><b>Nagi model</b>: Pathology → Impairment → Functional limitation → Disability.</p>
<ul><li><b>Direct impairment</b> (في الـ stroke): sensory loss، paresis، hemianopia. <b>Secondary (indirect)</b> = complications: decubitus ulcer، DVT، UTI، pneumonia، depression.</li>
<li><b>BADL</b>: dressing، feeding، bathing. <b>IADL</b>: house cleaning، preparing meals، shopping، managing finance.</li>
<li>الـ <b>Disability</b> عند Nagi = <b>societal</b> مش individual (الأدوار الاجتماعية).</li></ul>
<p><b>ICF</b>: 3 مكونات = Body functions &amp; structures · Activities &amp; participation · Personal &amp; environmental factors.</p>
<ul><li><b>Capacity</b> = اللي يقدر يعمله في <b>standard environment</b>. <b>Performance</b> = اللي بيعمله في <b>usual environment</b>.</li>
<li><b>Activity</b> = execution of a task. <b>Participation</b> = involvement in a life situation.</li>
<li>الـ <b>Personal factors</b> مش متصنفة جوه الـ ICF.</li></ul></div>

<div class="card"><h4>3. Lec 4 — Causes, management &amp; handicap</h4>
<table><tr><th>السبب</th><th>أمثلة</th></tr>
<tr><td>Genetic</td><td>mental retardation، hearing / speech / visual impairment، congenital heart disease</td></tr>
<tr><td>Non-genetic</td><td>birth trauma، malnutrition، drug use in pregnancy</td></tr>
<tr><td>Communicable</td><td><b>Herpes، HIV، AIDS</b></td></tr>
<tr><td>Non-communicable</td><td>scoliosis، cervical spondylosis، rheumatic arthritis، diabetes، cancer</td></tr>
<tr><td>Psychiatric</td><td>schizophrenia، mental depression</td></tr>
<tr><td>Trauma / Drug abuse / Malnutrition</td><td>accidents / alcoholism / anemia</td></tr></table>
<ul><li><b>Management (3)</b>: Different therapy (medications، PT، OT، speech) · <b>Assistive technology</b> (umbrella term: wheelchairs، prostheses، hearing &amp; visual aids) · <b>Adapted sports</b> (3 مجموعات: the deaf، physical، intellectual. مثال: wheelchair basketball).</li>
<li><b>Handicap</b> = <b>disadvantage</b> ناتج من impairment أو disability بيمنع الشخص يعمل <b>role</b> طبيعي ليه.</li>
<li><b>Categories (4)</b>: Physically · Sensorily (visual، hearing) · Mentally (retarded، ill، <b>epilepsy</b>) · Multiply handicapped.</li>
<li>الـ <b>Blind</b>: completely blind (مفيش أي رد فعل للضوء) · <b>light perception</b> (بيفرّق نور وضلمة بس) · residual vision.</li>
<li>الـ <b>Partially sighted</b>: نظره أحسن من <b>3/60</b> ومش أحسن من <b>1/4</b>.</li>
<li>الـ <b>Epilepsy</b>: فقد وعي مفاجئ. Major fit = <b>grand mal</b>، Minor fit = <b>petit mal</b>.</li>
<li>الـ <b>Multi-handicapped</b>: بيشتغلوا بس في <b>sheltered conditions</b>.</li></ul>
<table><tr><th>IQ</th><th>الدرجة</th></tr>
<tr><td>125+</td><td>Superior</td></tr><tr><td>111–124</td><td>Above average</td></tr><tr><td><b>90–110</b></td><td><b>Average</b></td></tr>
<tr><td>70–89</td><td>Borderline</td></tr><tr><td><b>52–69</b></td><td>Mild MR</td></tr><tr><td>36–51</td><td>Moderate MR</td></tr>
<tr><td>20–35</td><td>Severe MR</td></tr><tr><td><b>أقل من 20</b></td><td>Profound MR</td></tr></table></div>

<div class="card"><h4>4. Lec 5 — Function assessment (Part 1)</h4>
<ul><li><b>Function assessment</b> = تقييم الـ function abilities وتحديد الـ <b>function limitation (disabilities)</b>.</li>
<li><b>Evaluation</b> = <b>collecting information</b> عشان نعمل <b>baseline</b> ونخطط العلاج ونوثّق التقدم.</li>
<li><b>General considerations</b>: المريض <b>fully supported</b> (يزود الـ base of support) · وضع مريح · توقيت مناسب (<b>sundowning behavior</b>) · حرارة الأوضة · نشرح للمريض · نبعد عن اللي يزود الـ <b>spasticity</b> (noise، excitation، coldness) · التقييم <b>بدري</b> · على <b>two sessions</b> · والأسرة ليها دور كبير.</li></ul>
<table><tr><th>Decision making step</th><th>بيعمل إيه</th></tr>
<tr><td>I. Diagnostic interview</td><td>بيطلّع الـ main problems والـ <b>chief complaint</b></td></tr>
<tr><td>II. Screening examination</td><td><b>scan quickly</b> وبيبرر الـ <b>referrals</b></td></tr>
<tr><td>III. Comprehensive testing</td><td>بيحدد الـ dysfunction وسببه · <b>broad database</b></td></tr>
<tr><td>IV. Treatment goals</td><td><b>Long term</b>: مقدار الـ independence. <b>Short term</b>: الإجراءات اللي توصّل للـ long term</td></tr>
<tr><td>V. Special tests</td><td>بتكمّل الداتا <b>الناقصة</b> وبتأكد السبب</td></tr>
<tr><td>VI. Continuous reassessment</td><td>بيتابع التقدم، ولو مفيش تقدم نغيّر العلاج</td></tr></table>
<ul><li><b>Evaluation chart</b>: History (personal، family، past، present، social) · <b>Chief complaint</b> (from the patient's <b>own words</b>) · Medical examination · Physical examination.</li>
<li><b>Inspection</b>: skin color، deformities، atrophy، edema. <b>Palpation</b>: site of pain، degree of contracture، type of edema.</li>
<li><b>Muscle testing</b>: individual muscle للـ <b>LMN</b>، و functional pattern للـ <b>UMN</b>.</li>
<li><b>Gross motor</b> (عضلات كبيرة): تحت الـ <b>extrapyramidal &amp; cerebellum</b>. <b>Fine motor</b> (عضلات صغيرة): تحت الـ <b>cortical</b> control.</li>
<li><b>Coordination</b>: Equilibrium (static و dynamic balance) · Non-equilibrium (finger to nose، heel to knee).</li>
<li><b>Functional examination</b> (5 أنشطة: transfer، eating، hygiene، dressing، gait): <b>0</b> can't · <b>1</b> great assistance · <b>2</b> minimal assistance · <b>3</b> without assistance.</li></ul></div>

<div class="card"><h4>5. Lec 6 — Screening, FIM &amp; Berg</h4>
<ul><li><b>Assess, don't assume. Watch, don't just ask.</b></li>
<li><b>Vision</b>: <b>Snellen chart</b>. كشف العين كل <b>سنتين</b> على الأقل، ومع diabetes أو glaucoma كل <b>6–12 شهر</b>.</li>
<li><b>Hearing</b>: <b>Whisper test</b> و <b>Finger rub</b>. الـ <b>cerumen</b> بيعطّل توصيل الصوت.</li>
<li><b>Lower extremities</b>: <b>Get Up and Go</b> (قوم، امشي <b>10 feet</b>، لف وارجع، اقعد). المشكلة فيه = abnormal gait و <b>risk of falling</b>.</li>
<li><b>Delirium</b>: hours to days · <b>Depression</b>: weeks to months · <b>Dementia</b>: months to years.</li>
<li><b>ADL</b>: bathing، dressing، eating، toileting، transfers. <b>IADL</b> (أعقد): cooking، shopping، managing money، telephone.</li></ul>
<table><tr><th></th><th>FIM</th><th>Berg Balance Scale</th></tr>
<tr><td>بيقيس</td><td>Disability / independence، <b>مش خاص بتشخيص معين</b></td><td>Balance أثناء tasks محددة</td></tr>
<tr><td>Items</td><td><b>18</b> item، <b>7</b> levels</td><td><b>14</b> item، كل واحد من <b>0 لـ 4</b></td></tr>
<tr><td>Subscales</td><td><b>Motor</b> (13) و <b>Cognition</b> (5)</td><td>—</td></tr>
<tr><td>التوقيت</td><td>خلال <b>72 ساعة</b> من الدخول و 72 ساعة قبل الخروج</td><td>حوالي <b>20 دقيقة</b></td></tr>
<tr><td>ملحوظة</td><td>7 = complete independence، 1 = total assistance</td><td><b>مفيش فيه gait</b> · <b>56</b> = functional balance · <b>&lt;45</b> = risk of falling</td></tr></table>
<p class="key">FIM cognition (5): Comprehension · Expression · Social interaction · Problem solving · Memory. والباقي motor.</p></div>

<div class="card"><h4>6. Lec 7 — Assistive gait devices</h4>
<ul><li><b>ليه بنستخدمها</b>: poor balance · مش قادر يحمّل على رجله (fracture) · paralysis · amputation.</li>
<li><b>فايدة الـ early ambulation</b>: aiding circulation · <b>preventing calcium loss</b> · aiding pulmonary &amp; renal systems.</li>
<li>الاختيار حسب الـ <b>disability، coordination، stability</b>.</li></ul>
<table><tr><th>Device</th><th>أهم حاجة</th><th>المقاس</th></tr>
<tr><td>Parallel bars</td><td><b>Maximal support</b>، بس بتحد الـ mobility</td><td>Elbow flexion <b>15–20°</b> · المسكة <b>6 inches</b> قدام الـ hips · أوسع من الـ hips بـ <b>2 inches</b></td></tr>
<tr><td>Walker</td><td>Maximum stability + mobile · <b>4 legs</b> · صعب على السلم وبطيء</td><td>Elbow <b>15–25°</b></td></tr>
<tr><td>Axillary crutches</td><td>أسرع وأنواع gait أكتر · ممكن تأذي الـ <b>neurovascular</b> في الـ axilla</td><td><b>2–3 fingers</b> تحت الباط · الطرف <b>6 inches</b> من الصوابع بزاوية <b>45°</b> · elbow 15–25°</td></tr>
<tr><td>Forearm (<b>Lofstrand / Canadian</b>)</td><td>للاستخدام <b>الدائم</b> أو الطويل · مفيش خطر على الـ axilla</td><td>الـ handpiece عند الـ <b>ulnar styloid</b> · الـ cuff <b>1–1.5 inch</b> تحت الـ olecranon</td></tr>
<tr><td>Cane (<b>J cane</b>)</td><td>للـ balance · ينفع على السلم · دعمه قليل (base صغير)</td><td>الـ handpiece عند الـ <b>ulnar styloid</b> · elbow 15–25°</td></tr></table>
<table><tr><th>Gait pattern</th><th>المهم</th></tr>
<tr><td>Four-point</td><td><b>Maximum assistance with balance</b> · جهازين · <b>slow but stable</b> (right cane، left foot، left cane، right foot)</td></tr>
<tr><td>Three-point</td><td>وزن كامل على <b>رجل واحدة</b> (NWB) · crutches أو walker، <b>مش بـ two canes</b> · <b>44.4–49%</b> من الوزن على الدراعين · طاقة <b>ضعف</b> المشي العادي</td></tr>
<tr><td>Two-point</td><td>أسرع من الـ four-point و<b>أقرب للمشي الطبيعي</b>، بس أقل ثباتًا</td></tr>
<tr><td>Modified four / two-point</td><td><b>جهاز واحد</b> بس · في الإيد <b>العكسية</b> للرجل المصابة · WBAT و PWB</td></tr>
<tr><td>Modified three-point</td><td><b>Touchdown / toe-touch</b> weight bearing</td></tr></table>
<p class="key">Swing-to = الرجل السليمة توصل <b>جنب</b> المصابة. Swing-through = تعدّي <b>قدامها</b>.</p></div>
"""

T("mid", "تجميعة الميد — Lec 1 to 7", "تجميعة الميد", "⭐", "سلايدات الدكتور الرسمية (7 محاضرات)", SUMMARY,
[
 ("Lec 1–2 — Rehabilitation, settings & team", [
  ("Rehabilitation is the process of:", ["Making the person with a disability maximally able again", "Curing all diseases with drugs", "Keeping the patient in bed", "Performing surgery for the disabled"], "imp", ""),
  ("One of the aims of rehabilitation is to help the patient to be:", ["Independent as much as possible", "Dependent on his family", "Isolated from society", "Hospitalized for life"], "imp", ""),
  ("The teamwork approach treats the patient's problems:", ["As early as possible", "After one year", "Only after discharge", "Only when complications appear"], "", ""),
  ("Community support in rehabilitation includes cooperation of health agencies, social welfare and the:", ["Ministry of Education", "Ministry of Defense", "Ministry of Tourism", "Ministry of Finance"], "", ""),
  ("Developing new skills for a new job is done according to the patient's:", ["Residual disability", "Age only", "Family wishes", "Income"], "", ""),
  ("Inpatient rehabilitation means that the patient:", ["Stays inside a hospital or special center", "Is treated at home", "Visits a clinic once a month", "Is treated by phone"], "imp", ""),
  ("Patients in an acute rehabilitation unit must be able to join at least:", ["3 hours of therapy every day", "30 minutes of therapy weekly", "1 hour of therapy monthly", "10 hours of therapy every day"], "imp", ""),
  ("The medical director of a hospital rehabilitation unit is usually a:", ["Physiatrist", "Dentist", "Pharmacist", "Dietician"], "imp", ""),
  ("Home health rehabilitation refers to restorative services provided in:", ["The patient's home", "The intensive care unit", "A freestanding hospital", "An academic center"], "", ""),
  ("A homebound patient is one who experiences:", ["A normal inability to leave home", "A wish to stay in hospital", "Full independence", "Fear of therapists"], "", ""),
  ("The transdisciplinary approach:", ["Maximizes the strength of team members and minimizes duplication of services", "Increases duplication of services", "Excludes the patient", "Uses one profession only"], "imp", ""),
  ("In the transdisciplinary approach, one team member is chosen to be the:", ["Primary therapist or leader", "Consultant", "Extended member", "Observer"], "", ""),
  ("Core members (first level) of the team include:", ["Physicians, nurses, social workers, physical and occupational therapists", "Dieticians and pharmacists", "Dentists and psychologists", "Consultants only"], "imp", ""),
  ("Extended members (second level) of the team include:", ["Dieticians, pharmacists and dentists", "Physicians and nurses", "Physical therapists", "Social workers"], "imp", ""),
 ]),
 ("Lec 3 — Disability: definition, types & models", [
  ("Disability is defined as:", ["A restriction or lack (resulting from an impairment) of ability to perform an activity", "Any disease with fever", "A disadvantage in a social role only", "A loss of a body structure only"], "imp", ""),
  ("Which is an example of PERMANENT disability?", ["Blindness or amputation of limbs", "Limb fracture", "Temporary paralysis after stroke", "Common cold"], "imp", ""),
  ("Which is an example of a PROGRESSIVE disability?", ["Muscular dystrophy", "Healed fracture", "Recovery after stroke", "Sprained ankle"], "imp", ""),
  ("A regressive disability is one that is:", ["Improving and leading to recovery", "Deteriorating to a more severe status", "Present from birth", "Never changing"], "", ""),
  ("Disabilities acquired DURING birth (e.g., lack of oxygen, misuse of forceps) are:", ["Perinatal causes", "Prenatal causes", "Postnatal causes", "Genetic causes"], "imp", ""),
  ("Disabilities acquired before birth are called:", ["Prenatal", "Perinatal", "Postnatal", "Acquired"], "", ""),
  ("The term sensory disability is used primarily to refer to impairment of:", ["Vision and hearing", "Smell and taste", "Memory and reasoning", "Muscle power"], "imp", ""),
  ("A person with visual impairment may read using:", ["Braille", "Sign language", "Lip-reading", "A hearing aid"], "", ""),
  ("Complete loss of the sense of taste is known as:", ["Ageusia", "Dysgeusia", "Anosmia", "Aphasia"], "imp", "الـ Dysgeusia = taste غلط مستمر."),
  ("Balance requires the visual system, proprioception and the:", ["Vestibular system", "Digestive system", "Urinary system", "Endocrine system"], "", ""),
  ("Cognitive disabilities are separated into two categories:", ["Learning disabilities and mental retardation", "Blindness and deafness", "Epilepsy and autism", "Prenatal and postnatal"], "imp", ""),
  ("A developmental disability occurs prior to age:", ["18", "30", "40", "65"], "imp", ""),
  ("All are common types of developmental disability EXCEPT:", ["Diabetes", "Cerebral palsy", "Autism", "Epilepsy"], "", "الخمسة: Mental retardation، CP، Epilepsy، Autism، Neurological impairments."),
  ("Renal failure, diabetes and asthma are examples of …… disability:", ["Invisible", "Sensory", "Developmental", "Cognitive"], "imp", ""),
  ("The Nagi model uses the terms:", ["Pathology, impairment, functional limitation and disability", "Capacity and performance", "Core, extended and consultant", "Motor and cognition"], "imp", ""),
  ("Decubitus ulcer, DVT and UTI are examples of:", ["Secondary (indirect) impairments", "Direct impairments", "Pathology", "Handicap"], "imp", "المضاعفات."),
  ("Which is an INSTRUMENTAL activity of daily living (IADL)?", ["Shopping", "Dressing", "Feeding", "Bathing"], "imp", "Dressing و feeding و bathing دول BADL."),
  ("In the ICF, what a person does in his usual environment is his level of:", ["Performance", "Capacity", "Impairment", "Pathology"], "imp", "Capacity = في الـ standard environment."),
 ]),
 ("Lec 4 — Causes, management & handicap", [
  ("Which is a GENETIC cause of disability?", ["Congenital heart disease", "Birth trauma", "Accidents", "Alcoholism"], "", ""),
  ("Birth trauma, malnutrition and drug use in pregnancy are …… causes:", ["Non-genetic", "Genetic", "Psychiatric", "Communicable"], "", ""),
  ("Herpes, HIV and AIDS are examples of:", ["Communicable diseases", "Non-communicable diseases", "Genetic causes", "Trauma"], "imp", ""),
  ("Scoliosis, cervical spondylosis and diabetes are examples of:", ["Non-communicable diseases", "Communicable diseases", "Psychiatric causes", "Drug abuse"], "imp", ""),
  ("Schizophrenia is a …… cause of disability:", ["Psychiatric", "Genetic", "Communicable", "Traumatic"], "", ""),
  ("An umbrella term that includes assistive, adaptive and rehabilitative devices is:", ["Assistive technology", "Adapted sports", "Occupational therapy", "Speech therapy"], "imp", ""),
  ("Adapted sports are divided into three groups: the deaf, people with physical disabilities and people with:", ["Intellectual disabilities", "Chest diseases", "Skin diseases", "Dental problems"], "", ""),
  ("Wheelchair basketball is usually played by the:", ["Physically impaired", "Deaf", "Blind", "Mentally ill"], "", ""),
  ("Handicap is defined as:", ["A disadvantage that limits or prevents the fulfillment of a normal role", "A loss of body structure", "A pathological condition of the body", "A measure of balance"], "imp", ""),
  ("Mentally handicapped persons include mentally retarded, mentally ill and persons suffering from:", ["Epilepsy", "Amputation", "Deafness", "Scoliosis"], "", ""),
  ("Blind persons with light perception are only able to:", ["Discriminate light and darkness", "Read regular print", "Drive a car", "See colors clearly"], "", ""),
  ("Average intelligence corresponds to an IQ of:", ["90–110", "52–69", "20–35", "125 and above"], "imp", ""),
  ("Mild mental retardation corresponds to an IQ of:", ["52–69", "90–110", "Below 20", "111–124"], "imp", "Profound = أقل من 20."),
  ("A major epileptic fit is called:", ["Grand mal", "Petit mal", "Paranoia", "Paresis"], "", ""),
 ]),
 ("Lec 5 — Function assessment (Part 1)", [
  ("Function assessment is designed to assess function abilities and identify:", ["Function limitations (disabilities)", "Blood groups", "Drug doses", "Family income"], "imp", ""),
  ("All are goals of function assessment EXCEPT:", ["Increasing dependence on others", "Monitoring changes", "Enhancing independence", "Identifying disabilities"], "", ""),
  ("Evaluation is a process of:", ["Collecting information to establish a baseline level of performance", "Giving medications", "Discharging the patient", "Performing surgery"], "imp", ""),
  ("During evaluation, the patient must be fully supported to:", ["Increase the base of support and maintain security", "Increase spasticity", "Save time", "Avoid talking to him"], "", ""),
  ("Choosing the proper timing for evaluation is related to:", ["Sundowning behavior", "Room color", "Patient's height", "Therapist's age"], "", ""),
  ("Noise, excitation and coldness should be avoided because they increase:", ["Spasticity", "Muscle strength", "Range of motion", "Appetite"], "imp", ""),
  ("Assessment must be performed in:", ["Two sessions", "Ten sessions", "One minute", "Six months"], "", ""),
  ("The step that reveals the patient's main problems and chief complaint is:", ["Diagnostic interviewing", "Special tests", "Continuous reassessment", "Comprehensive testing"], "imp", ""),
  ("The screening examination allows the therapist to:", ["Scan data quickly and justify referrals", "Set long term goals", "Supply missing data", "Treat the patient"], "imp", ""),
  ("Short term goals determine:", ["The procedures needed to attain long term goals", "The amount of independence required", "The patient's past history", "The hospital budget"], "", ""),
  ("Special tests are used for:", ["Supplying data that are missing in comprehensive tests", "Replacing the interview", "Personal history", "Measuring IQ"], "", ""),
  ("The chief complaint is recorded:", ["From the patient's own words", "From the X-ray", "From the nurse only", "From the textbook"], "imp", ""),
  ("Individual muscle testing is used for:", ["Lower motor neuron diseases", "Upper motor neuron diseases", "Skin diseases", "Mental diseases"], "imp", "الـ UMN = functional muscle testing / motor pattern."),
  ("Gross motor activities are under the control of the:", ["Extrapyramidal system and cerebellum", "Cerebral cortex only", "Spinal nerves only", "Heart"], "imp", "الـ fine motor تحت الـ cortical control."),
  ("Finger to nose and heel to knee are examples of:", ["Non-equilibrium coordination tests", "Static balance tests", "Sensory tests", "Muscle tests"], "", ""),
  ("In functional examination, grade 3 means the patient:", ["Does it without assistance", "Can't do it", "Does it with great assistance", "Does it with minimal assistance"], "imp", "0 = can't، 1 = great، 2 = minimal."),
 ]),
 ("Lec 6 — Screening, FIM & Berg", [
  ("Vision is screened using the:", ["Snellen chart", "Berg scale", "Whisper test", "Get Up and Go test"], "imp", ""),
  ("The minimum frequency of eye examination is every:", ["Two years", "Ten years", "Week", "Five years"], "", "مع diabetes أو glaucoma: كل 6–12 شهر."),
  ("Hearing can be screened by the:", ["Whisper test and finger rub", "Snellen chart", "FIM", "Finger to nose test"], "imp", ""),
  ("Build up of cerumen:", ["Interferes with the conduction of sound", "Improves hearing", "Affects vision", "Causes dementia"], "", ""),
  ("In the 'Get Up and Go' test, the person walks:", ["10 feet", "100 feet", "1 mile", "2 inches"], "imp", ""),
  ("Problems with the 'Get Up and Go' test correlate with:", ["Abnormal gait and increased risk of falling", "Hearing loss", "Poor vision", "Depression"], "", ""),
  ("The onset of delirium is:", ["Hours to days", "Weeks to months", "Months to years", "Since birth"], "imp", ""),
  ("The onset of dementia is:", ["Months to years", "Hours to days", "Minutes", "Weeks to months"], "imp", "Depression = weeks to months."),
  ("Which is an activity of daily living (ADL)?", ["Bathing and grooming", "Managing money", "Using the telephone", "Doing laundry"], "", ""),
  ("The FIM is:", ["An 18-item, seven-level ordinal scale", "A 14-item, five-point scale", "A 10-item scale", "A 56-item scale"], "imp", ""),
  ("The FIM is a measure of disability that is:", ["Not specific to any diagnosis", "Used only for stroke", "Used only for children", "A test of balance only"], "", ""),
  ("FIM admission assessment is collected within:", ["72 hours of the start of rehabilitation", "One month", "One year", "5 minutes"], "imp", ""),
  ("FIM items are grouped into two subscales:", ["Motor and cognition", "Static and dynamic", "Core and extended", "Gross and fine"], "imp", ""),
  ("Which item belongs to the FIM cognition subscale?", ["Memory", "Eating", "Stairs", "Toileting"], "", "Cognition: comprehension، expression، social interaction، problem solving، memory."),
  ("The Berg Balance Scale consists of:", ["14 items, each scored from 0 to 4", "18 items, each scored from 1 to 7", "5 items scored 0 to 3", "56 items"], "imp", ""),
  ("The Berg Balance Scale takes approximately:", ["20 minutes", "2 hours", "72 hours", "1 minute"], "", ""),
  ("On the Berg Balance Scale, a score of less than 45 indicates:", ["Greater risk of falling", "Functional balance", "Total independence", "Normal gait"], "imp", "56 = functional balance. والـ Berg مفيش فيه gait."),
 ]),
 ("Lec 7 — Assistive gait devices", [
  ("All are reasons for using an assistive gait device EXCEPT:", ["Good balance", "Paralysis of the lower extremities", "Amputation of a lower extremity", "Inability to bear weight due to fracture"], "", ""),
  ("An advantage of early ambulation following an injury is:", ["Preventing calcium loss in bones", "Increasing calcium loss", "Slowing circulation", "Weakening the lungs"], "imp", ""),
  ("The selection of an assistive gait device is based on the patient's:", ["Disability, coordination and stability", "Hair color", "Job title", "Blood group"], "", ""),
  ("Parallel bars are used when:", ["Maximal patient support and stability are required", "The patient climbs stairs", "The patient runs", "No support is needed"], "imp", ""),
  ("Parallel bar height should provide elbow flexion of:", ["15–20 degrees", "45–60 degrees", "90 degrees", "0 degrees"], "imp", ""),
  ("Parallel bars should be wider than the patient's hips by about:", ["2 inches", "20 inches", "6 feet", "1 meter"], "", ""),
  ("All walkers have:", ["Four legs", "Two legs", "One leg", "Six legs"], "", ""),
  ("A disadvantage of walkers is that they are:", ["Very difficult to use on stairs", "Unstable", "Dangerous to the axilla", "Too fast"], "imp", ""),
  ("With axillary crutches, the space between the top of the crutch and the axilla should fit:", ["Two or three fingers", "One whole hand", "Nothing", "A fist"], "imp", ""),
  ("The tips of axillary crutches should be about …… from the toes at a 45-degree angle:", ["6 inches", "6 feet", "1 inch", "20 inches"], "imp", ""),
  ("Improper use of axillary crutches can injure the:", ["Neurovascular structures in the axillary region", "Knee ligaments", "Ulnar styloid", "Spinal cord"], "imp", ""),
  ("Forearm crutches are also known as:", ["Lofstrand or Canadian crutches", "J crutches", "Axillary crutches", "Platform walkers"], "imp", "بتتستخدم لما المريض محتاج crutches دايمًا أو لفترة طويلة."),
  ("The top of the forearm cuff should be located:", ["1 to 1.5 inches distal to the olecranon", "At the wrist", "At the shoulder", "10 inches above the elbow"], "", ""),
  ("The hand-piece of a cane should be level with the:", ["Ulnar styloid process", "Greater trochanter of the opposite side", "Knee joint", "Shoulder"], "imp", ""),
  ("The standard cane is known as the:", ["J cane", "Quad walker", "Canadian crutch", "Platform"], "", ""),
  ("The four-point gait pattern is:", ["Slow but stable", "Fast but unstable", "Done with one cane", "Non-weight bearing"], "imp", "للمريض اللي محتاج maximum assistance with balance."),
  ("The three-point gait pattern cannot be performed with:", ["Two canes", "A walker", "Axillary crutches", "Forearm crutches"], "imp", ""),
  ("In three-point gait with axillary crutches, the upper extremities carry about …… of body weight:", ["44.4–49%", "5–10%", "90–100%", "1%"], "", "والطاقة حوالي ضعف المشي العادي."),
  ("The gait pattern that closely approximates normal gait is the:", ["Two-point gait", "Four-point gait", "Three-point gait", "Swing-to gait"], "imp", ""),
  ("With one assistive device, it should be used in the upper extremity:", ["Opposite to the involved lower extremity", "On the same side as the involved lower extremity", "Either side, no difference", "It is never used with one hand"], "imp", ""),
  ("The modified three-point gait pattern is used for:", ["Touchdown (toe-touch) weight bearing", "Full weight bearing on both legs", "Patients with one cane", "Running"], "", ""),
 ]),
])
