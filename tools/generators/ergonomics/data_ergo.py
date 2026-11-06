# Ergonomics (Dr. Anees Ghiet) — simple summaries in slide order.
TF2 = ["True ✓", "False ✗"]
PT12 = [
 ("Which of the following is an example of contact stress?", ["Standing up and stretching", "Prolonged typing", "Heavy lifting", "Resting the wrist on the edge of a desk"], 3, "Contact stress = تلامس نسيج حساس مع حرف حاد. الـ prolonged typing ده repetition."),
 ("Which of the following is considered a risk factor for CTDs?", ["Adequate rest", "Neutral posture", "Repetition", "Proper workstation adjustment"], 2, ""),
 ("Which of the following is considered an engineering control?", ["Training workers annually", "Rotating personnel between jobs", "Redesigning the workstation or tools", "Establishing work/rest schedules"], 2, "الباقيين administrative controls."),
 ("Holding a fixed position for a prolonged period is known as:", ["Repetition", "Static posture", "Force", "Contact stress"], 1, ""),
 ("A worker performs the same hand movement continuously for several hours with little variation. This is an example of:", ["Contact stress", "Repetition", "Static posture", "Force"], 1, ""),
 ("Which of the following best describes Ergonomics?", ["The applied science of equipment design to reduce fatigue and discomfort", "The study of diseases affecting muscles", "The treatment of workplace injuries", "The study of human anatomy only"], 0, ""),
 ("Which of the following is an administrative control used to reduce ergonomic risks?", ["Rotating personnel to different jobs", "Redesigning the workstation", "Redesigning work tools", "Changing the shape of equipment"], 0, ""),
 ("Cumulative Trauma Disorders (CTDs) mainly arise from:", ["Exposure to cold temperatures", "Sudden trauma to the body", "Repeated biomechanical stress", "Lack of physical activity"], 2, ""),
 ("Which situation is the best example of an awkward posture?", ["Working with the hands over the head", "Taking regular rest breaks", "Changing posture frequently", "Sitting in a neutral position"], 0, ""),
 ("Which technique is recommended when lifting a load?", ["Lift quickly with a jerking movement", "Bend from the waist and keep the load far from the body", "Bend the knees and keep the load close to the body", "Keep the back rounded while lifting"], 2, ""),
]
PT12_TF = [
 ("Ergonomics is theoretical science of equipment design aiming to maximize productivity by reducing operator fatigue.", TF2, 1, "Applied مش theoretical."),
 ("CTDs are arising from repeated mechanical stress to hands, wrist, elbows, shoulders, neck, back.", TF2, 0, ""),
 ("MSDs affect hard tissue of body in areas like neck, back, shoulder, elbow, hand, wrist, and fingers.", TF2, 1, "Soft tissue."),
 ("Approximate 42% of workplace injuries are back injuries.", TF2, 1, "24%."),
 ("Back injuries cost UK Business $36 Billion per year.", TF2, 1, "US مش UK."),
 ("MSDs represent over third of military disabilities.", TF2, 1, "نص (half) الـ military disabilities."),
 ("MSDs represent over one third of civilian injuries and illnesses within Marine.", TF2, 0, "حسب إجابة الدفعة: صح (السلايد: one third)."),
 ("Refresher training should be provided annually and also when personnel are assigned to new job with different risks.", TF2, 0, ""),
 ("Prop two feet up on stool to reduce stress in lower back.", TF2, 1, "رجل واحدة (one foot)."),
 ("Supervisors not necessary receive sufficient training on ergo issues to effectively carry out their responsibilities.", TF2, 1, "لازم ياخدوا training كفاية."),
]

TABS = []
def T(*a): TABS.append(a)

# ============================================================ Lec 1
T("l1", "Lec 1 — Introduction to Ergonomics & Backpack Ergonomics", "Lec 1 Intro & Backpack", "🎒",
  "سلايدات Lec 1 (د. أنيس غيث) + ملخص Be IN",
"""
<div class="card"><h4>1. Definition</h4>
<ul><li><b>"Ergo" = work</b> و <b>"nomics" = study of</b>.</li>
<li>The <b>applied</b> science of equipment design, intended to <b>maximize productivity</b> by <b>reducing operator fatigue and discomfort</b>.</li></ul>
<table><tr><th>التعريف</th><th>المعنى</th></tr>
<tr><td>1. Old definition</td><td>أوائل الـ <b>1700s</b>: دراسة الأضرار من الـ poor posture والأدوات السيئة على صحة العمال. من اليوناني: <b>Ergon = work</b>، <b>Nomikos = law</b>، يعني "study of work laws"</td></tr>
<tr><td>2. Modern definition</td><td>Science of <b>fitting workplace conditions and job demands to the capabilities</b> of the working population</td></tr>
<tr><td>3. Another definition</td><td>Science of improving employee <b>performance and well-being</b> in relation to the <b>job tasks، equipment، environment</b></td></tr></table></div>

<div class="card"><h4>2. Ergonomics of backpack</h4>
<ul><li><b>Dr. Karen Jacobs (1998)</b>: الشنط بتكبر وتتقل ومش متناسبة مع حجم الأطفال، وده بسبب المدارس الزحمة وقلة الـ lockers.</li>
<li>بتوجع الضهر والرقبة والكتف، وكمان بتعمل <b>headaches</b> ومشاكل تركيز.</li>
<li>University of California (<b>2010</b>): الشنطة مسؤولة عن الـ back pain، و<b>تلت</b> الأطفال من 11–14 سنة عندهم LBP. وأبحاث <b>2011</b> وصلت لنفس النتيجة.</li>
<li><b>Dr. Rob Danoff</b>: العمود الفقري زي هيكل البيت، والحمل الزيادة وهو لسه بيكبر بيغير الـ posture ويضغط الـ spine ويأثر على النمو.</li></ul></div>

<div class="card"><h4>3. Biomechanical hazards</h4>
<ul><li>الشنطة = <b>addition of weight</b> ورا الجذع، فالـ <b>COG بيروح لورا</b>، والجسم بيعوّض و<b>يميل لقدام</b> عشان ميقعش لورا.</li></ul>
<p><b>النتيجة:</b> 1. round shoulders · 2. <b>kyphosis</b> · 3. postural deformity · 4. cervical و dorsal و lumbosacral pain (LBP) · 5. <b>disc prolapse</b> · 6. spondylosis · 7. spondylolisthesis · 8. <b>scoliosis لو شنطة بشيال واحد</b> · 9. asymmetry of both shoulders.</p></div>

<div class="card"><h4>4. How heavy is too heavy?</h4>
<ul><li>Jacobs: الشنطة <b>من 10 لـ 20%</b> من وزن الطفل بالكتير، والحاجات التقيلة (كتب، لانش بوكس) في النص وقريبة من الضهر.</li>
<li>توصية تانية: <b>10–15%</b> من وزن الجسم، و<b>أبدًا مش أكتر من 25 pounds</b>.</li></ul>
<table><tr><th>وزن الشخص (lb)</th><th>أقصى وزن للشنطة (lb)</th></tr>
<tr><td>60</td><td>5</td></tr><tr><td>100</td><td>15</td></tr><tr><td>125</td><td>18</td></tr><tr><td>150</td><td>20</td></tr><tr><td>200 أو أكتر</td><td>25</td></tr></table></div>

<div class="card"><h4>5. Choosing the right backpack</h4>
<ol><li><b>Wide, padded shoulder straps</b>: الشيالات الرفيعة بتعمل ألم في الكتف، ومع الوقت تنميل وضعف في الإيد بسبب ضغط الأعصاب والدورة الدموية.</li>
<li><b>Two shoulder straps</b>: شيال واحد بيعمل alignment problems زي الـ <b>scoliosis</b>.</li>
<li><b>Padded back</b>: يحمي من الحاجات اللي ليها حروف جوه الشنطة.</li>
<li><b>Waist strap</b>: يوزع الحمل على الـ spine والـ <b>pelvis</b>.</li>
<li><b>Multiple compartments</b>: يوزع الوزن بالتساوي.</li></ol>
<p>وكمان: <b>light weight backpack</b> و <b>rolling backpack</b>.</p></div>

<div class="card"><h4>6. Safe backpack summary &amp; injury prevention</h4>
<ol><li><b>البس الشيالين</b> (شيال واحد بيعمل muscle spasm و LBP)، و<b>شدّهم</b> عشان الحمل يبقى قريب من الجسم.</li>
<li>الحاجات التقيلة <b>تحت وعلى الضهر</b>، والشنطة في <b>نص الضهر</b>.</li>
<li><b>Take a load off</b>: اقلعها لو هتقف كتير، لأن الشيل الطويل بيزود الضغط على الـ spine.</li>
<li>Pack light: خد بس اللي محتاجه النهارده.</li>
<li>ارفعها صح بـ <b>ثني الركب</b>.</li>
<li>الـ <b>cross body bag</b> بديل كويس.</li></ol></div>

<div class="card"><h4>7. Tips for parents</h4>
<ol><li>شجع ابنك يقولك على أي <b>numbness أو tingling</b> أو discomfort في الإيد أو الرجل (معناه fit غلط أو وزن زيادة).</li>
<li>اتفرج عليه وهو بيلبسها ويقلعها، ولو تقيلة يشيل كتب في إيده.</li>
<li>متتجاهلش أي back pain.</li>
<li>كلم المدرسة عن تخفيف الحمل، واتعاون مع أولياء الأمور.</li>
<li>يستخدم الـ locker لما يقدر.</li>
<li>لو الألم مش بيتحسن، نسخة تانية من الكتب في البيت.</li></ol></div>
""",
[
 ("Definitions", [
  ("'Ergo' means:", ["Work", "Law", "Study", "Body"], "imp", ""),
  ("Ergonomics is the …… science of equipment design to maximize productivity by reducing fatigue:", ["Applied", "Theoretical", "Historical", "Surgical"], "imp", ""),
  ("The old definition of ergonomics appeared in the:", ["Early 1700s", "1950s", "1998", "2010"], "", ""),
  ("In the old definition, 'Nomikos' means:", ["Law", "Work", "Body", "Tool"], "imp", ""),
  ("The modern definition of ergonomics is:", ["Fitting workplace conditions and job demands to the capabilities of workers", "Study of work laws", "Treatment of injuries", "Design of hospitals"], "imp", ""),
  ("Another definition: ergonomics improves performance in relation to all EXCEPT:", ["Salary", "Job tasks", "Equipment", "Environment"], "", ""),
 ]),
 ("Backpack", [
  ("Dr. Karen Jacobs (1998) said backpacks are:", ["Getting bigger and heavier, not in proportion to kids' sizes", "Getting lighter", "Safe for all children", "Only harmful to adults"], "imp", ""),
  ("A heavy backpack can also contribute to:", ["Headaches and problems concentrating", "Better posture", "Higher grades", "Weight loss"], "", ""),
  ("The University of California study (2010) found that low back pain is reported by …… of kids aged 11–14:", ["One third", "One half", "10%", "All"], "imp", ""),
  ("Carrying a backpack moves the COG:", ["Backward, and the person compensates by leaning the trunk forward", "Forward", "Laterally", "It does not change"], "imp", ""),
  ("Using a backpack with one strap (unilateral) may cause:", ["Scoliosis", "Kyphosis only", "Flat foot", "Genu varum"], "imp", ""),
  ("Poor backpack use leads to all EXCEPT:", ["Increased height", "Round shoulders", "Kyphosis", "Disc prolapse"], "", ""),
  ("According to Jacobs, a backpack should be no more than …… of body weight:", ["10–20%", "30–40%", "50%", "5%"], "imp", ""),
  ("It is recommended that backpacks never weigh more than:", ["25 pounds", "50 pounds", "10 pounds", "40 pounds"], "imp", ""),
  ("For a 100 lb person, the maximum backpack weight is:", ["15 lb", "5 lb", "25 lb", "20 lb"], "", ""),
  ("Heavy items should be placed:", ["In the middle/bottom and close to the back", "In the front pocket", "At the top away from the back", "On one side"], "imp", ""),
  ("Non-padded straps can eventually cause tingling and weakness in arms due to:", ["Nerve compression and compromised circulation", "Muscle hypertrophy", "Bone fracture", "Infection"], "", ""),
  ("The waist strap distributes the weight on the:", ["Spine and pelvis", "Neck", "Shoulders only", "Knees"], "", ""),
  ("To pick up a backpack properly you should:", ["Bend at the knees", "Bend at the waist", "Twist the trunk", "Use one hand"], "", ""),
  ("A good alternative for carrying books is a:", ["Cross body bag", "One-strap bag", "Heavier backpack", "Hand bag on one shoulder"], "", ""),
  ("A child complaining of numbness or tingling in the arms may indicate:", ["Poor backpack fit or too much weight", "Normal growth", "Good posture", "Vitamin excess"], "", ""),
 ]),
])

# ============================================================ Lec 2
T("l2", "Lec 2 — Scope of Ergonomic Injuries", "Lec 2 Scope of injuries", "⚠️",
  "سلايدات Scope of ergonomic injuries + نوتس Lec 2",
"""
<div class="card"><h4>1. Scope of ergonomic injuries</h4>
<table><tr><th>النوع</th><th>التعريف</th></tr>
<tr><td>1. CTDs (Cumulative trauma disorders)</td><td>Health disorders من <b>repeated biomechanical stress</b> على الكتف والكوع والرسغ والإيد والرقبة والضهر</td></tr>
<tr><td>2. MSDs (Musculoskeletal disorders)</td><td>بتصيب الـ <b>soft tissue</b>: nerves و tendons و cartilage و ligaments و muscles</td></tr></table>
<p><b>Goals of ergonomics in workplace:</b> 1. reduce risk of CTD · 2. increase safety · 3. increase productivity · 4. improve quality of work · 5. decrease fatigue and errors.</p></div>

<div class="card"><h4>2. CTD statistics</h4>
<ul><li>حوالي <b>24%</b> من إصابات الشغل <b>back injuries</b>.</li>
<li>بتكلف شركات <b>أمريكا (US) 36 Billion $</b> في السنة.</li>
<li>التدرج مع الوقت: <b>Discomfort → Fatigue → Pain → Injury</b>.</li>
<li><b>Most common CTD</b>: <b>Carpal tunnel syndrome</b> و <b>Low back pain</b>.</li></ul></div>

<div class="card"><h4>3. Risk factors for CTD (5)</h4>
<table><tr><th>Risk factor</th><th>المعنى</th><th>مثال</th></tr>
<tr><td>Force</td><td>المجهود الجسدي للتحكم في الأدوات أو الشغل</td><td>Heavy lifting، pushing، pulling، carrying</td></tr>
<tr><td>Repetition</td><td>نفس الحركة باستمرار لفترة طويلة ومن غير تنويع</td><td><b>Prolonged typing</b>، أدوات إيد متكررة</td></tr>
<tr><td>Awkward postures</td><td>أوضاع بعيدة جدًا عن الـ neutral</td><td><b>Working over-head</b>، extended reaching، twisting، squatting، kneeling</td></tr>
<tr><td>Static postures</td><td>ثبات على وضع واحد</td><td>مسك أداة مينفعش تتساب، الوقوف في مكان واحد كتير</td></tr>
<tr><td>Contact stress</td><td>تلامس متكرر بين نسيج حساس وحاجة حادة</td><td><b>Resting wrist on edge of desk</b>، يد الأداة بتضغط في الكف</td></tr></table>
<p><b>Age-related changes:</b> reaction time بيطول · workload capacity بيقل · discomfort من الحرارة بيزيد · النظر بيضعف.</p>
<p><b>Risky postures:</b> frequent أو awkward أو heavy lifting · repetitive motion · awkward positions · <b>back bent أكتر من 30°</b> · <b>neck bent أكتر من 30°</b> (العضلات القصيرة بتضغط على العصب) · الإيد فوق الراس أو الكوع فوق الكتف.</p></div>

<div class="card"><h4>4. MSDs recent history (USA)</h4>
<ul><li>الـ MSDs = <b>نص (½) الـ military disabilities</b>، و<b>تلت (⅓)</b> كل الإصابات والأمراض الـ civilian في الـ <b>Marine Corps</b>.</li>
<li>زيادة التسجيل سببها: تغير طرق الشغل والـ risks، والتكنولوجيا والتدريب زودوا الوعي.</li></ul></div>

<div class="card"><h4>5. Hazard prevention &amp; control</h4>
<p>إنك تلغي أو تقلل أو تتحكم في الـ risk factors بـ:</p>
<table><tr><th>Control</th><th>إيه هو</th></tr>
<tr><td><b>Engineering controls</b> (الـ <b>preferred</b>)</td><td><b>Redesigning</b> الـ workstation وطرق الشغل والأدوات عشان يقلل الـ exertion والـ repetition والـ awkward positions</td></tr>
<tr><td><b>Administrative controls</b></td><td>1. <b>Rotating personnel</b> بين الأشغال · 2. <b>Work/rest schedules</b> · 3. <b>Training</b> على طرق شغل مناسبة لما الـ engineering controls متبقاش feasible</td></tr></table>
<ul><li><b>Workstation design</b>: لازم يبقى <b>easily adjustable</b> حسب العامل.</li>
<li><b>Training</b>: يخلي كل واحد يعرف الـ risk factors. بيتعمل <b>annually</b>، وفيه <b>retraining</b> لما ينتقل لشغل بـ risks مختلفة أو يظهر risk جديد.</li>
<li><b>Back injury training</b>: anatomy و physiology للضهر، biomechanics of lifting، <b>weight control</b>، إزاي تتجنب الإصابة، physical fitness.</li></ul></div>

<div class="card"><h4>6. Other methods to reduce back injury</h4>
<ol><li><b>Standing posture</b>: العمود على انحناءاته الطبيعية، و<b>ارفع رجل واحدة</b> على stool.</li>
<li><b>Shift and stretch</b>: غيّر وضعك واعمل stretch طول اليوم، خليك flexible، ومتجبرش جسمك على مكان الشغل.</li>
<li><b>Push not pull</b>: ممكن تزقها بدل ما تشيلها؟</li>
<li><b>Use lifting devices</b>: hand trucks، forklifts، dollies، وجوانتي لو محتاج.</li>
<li><b>Stretch and be ready</b>: warm up، جزمة <b>slip resistant</b>، وفضّي الطريق قبل ما تشيل.</li>
<li><b>Lift with your legs</b>: رجلك ثابتة (stable base)، <b>اثني الركب مش الوسط</b>، شد البطن، ومسكة كويسة بالإيدين.</li>
<li>الحمل <b>قريب من الجسم</b>.</li>
<li>استخدم عضلات الرجل.</li>
<li>الضهر upright على وضعه الطبيعي.</li>
<li>ارفع <b>بهدوء من غير jerking</b>.</li></ol>
<p><b>Supervisors:</b> لازم ياخدوا training كفاية في الـ ergonomics، ويتأكدوا إن الناس اتدربت، ويطلبوا مساعدة لإدارة الـ risk factors.</p></div>
""",
[
 ("Scope & statistics", [
  ("CTDs arise from:", ["Repeated biomechanical stress", "Sudden single trauma", "Cold exposure", "Infection"], "imp", ""),
  ("MSDs affect the …… tissue of the body:", ["Soft", "Hard", "Bony only", "Nervous only"], "imp", ""),
  ("Goals of ergonomics in the workplace include all EXCEPT:", ["Increase fatigue and errors", "Reduce risk of CTD", "Increase safety", "Increase productivity"], "", ""),
  ("Approximately …… of all workplace injuries are back injuries:", ["24%", "42%", "50%", "10%"], "imp", ""),
  ("Back injuries cost US business per year about:", ["$36 billion", "$3.6 billion", "$360 billion", "$36 million"], "imp", ""),
  ("The progression of CTDs over time is:", ["Discomfort → Fatigue → Pain → Injury", "Injury → Pain → Fatigue", "Pain → Discomfort → Injury", "Fatigue → Injury → Pain"], "", ""),
  ("The most common CTDs are:", ["Carpal tunnel syndrome and low back pain", "Fractures and sprains", "Tennis elbow and ganglion", "Raynaud's and TOS"], "imp", ""),
  ("MSDs represent …… of military disabilities:", ["Half", "One third", "One quarter", "10%"], "imp", ""),
 ]),
 ("Risk factors", [
  ("The number of risk factors for CTD is:", ["5", "3", "7", "10"], "", ""),
  ("Heavy lifting, pushing and pulling are examples of:", ["Force", "Repetition", "Contact stress", "Static posture"], "imp", ""),
  ("Prolonged typing is an example of:", ["Repetition", "Force", "Contact stress", "Awkward posture"], "imp", ""),
  ("Working overhead, twisting and kneeling are examples of:", ["Awkward postures", "Static postures", "Repetition", "Force"], "imp", ""),
  ("Standing in one place for prolonged periods is:", ["Static posture", "Repetition", "Contact stress", "Force"], "imp", ""),
  ("Tool handles pressing into the palms is:", ["Contact stress", "Force", "Repetition", "Static posture"], "imp", ""),
  ("Age-related changes include all EXCEPT:", ["Increased workload capacity", "Longer reaction time", "Decreased visual capabilities", "More temperature-related discomfort"], "", ""),
  ("A risky posture is bending the back more than:", ["30 degrees", "5 degrees", "90 degrees", "60 degrees only"], "", ""),
 ]),
 ("Prevention & control", [
  ("The preferred mechanism for controlling ergonomic hazards is:", ["Engineering controls", "Administrative controls", "Medications", "Personal protective equipment only"], "imp", ""),
  ("Redesigning the workstation, work methods and tools is:", ["Engineering control", "Administrative control", "Training", "Rest schedule"], "imp", ""),
  ("Rotating personnel to jobs is:", ["Administrative control", "Engineering control", "Lifting device", "Contact stress"], "imp", ""),
  ("Administrative controls include all EXCEPT:", ["Redesigning tools", "Job rotation", "Work/rest schedules", "Training"], "imp", ""),
  ("Workstations must be:", ["Easily adjustable", "Fixed", "Very high", "Without chairs"], "", ""),
  ("Training should be provided:", ["Annually, with retraining when assigned to a new job with different risks", "Once in a lifetime", "Every 10 years", "Only after injury"], "imp", ""),
  ("Back injury training includes all EXCEPT:", ["Salary negotiation", "Biomechanics of lifting", "Weight control", "Physical fitness"], "", ""),
  ("To reduce stress on the lower back while standing:", ["Prop one foot up on a stool", "Prop both feet up", "Lock the knees", "Lean backward"], "imp", ""),
  ("'Push not pull' means:", ["Slide the object instead of lifting it if possible", "Always pull heavy loads", "Lift everything", "Never move objects"], "", ""),
  ("When lifting with your legs you should:", ["Bend knees not waist and tighten abdominal muscles", "Bend at the waist", "Lock the knees", "Use one hand"], "imp", ""),
  ("Lifting should be done:", ["Steadily and smoothly without jerking", "Quickly with jerks", "With twisting", "Far from the body"], "", ""),
  ("Supervisors should:", ["Receive sufficient training on ergonomic issues", "Not be trained", "Only punish workers", "Avoid managing risk factors"], "", ""),
 ]),
])

# ============================================================ Lec 3
T("l3", "Lec 3 — Work-Related Musculoskeletal Disorders", "Lec 3 WRMSDs", "✋",
  "نوتس Lec 3 + نوتس الدفعة المكتوبة بخط الإيد",
"""
<div class="card"><h4>1. Upper extremity disorders (10)</h4>
<table><tr><th>النوع</th><th>الأمراض</th></tr>
<tr><td>Neurovascular</td><td>Carpal tunnel · Cubital tunnel · Thoracic outlet · Raynaud's (white finger)</td></tr>
<tr><td>Tendon</td><td>Rotator cuff · De Quervain's · Tendinitis · Tenosynovitis · Trigger finger · Ganglion cyst</td></tr></table></div>

<div class="card"><h4>2. Neurovascular disorders</h4>
<table><tr><th>المرض</th><th>السبب</th><th>الأعراض</th></tr>
<tr><td><b>Carpal tunnel syndrome</b></td><td>Impingement of <b>median nerve</b> بسبب swelling مزمن في الـ <b>flexor tendons</b> في الـ carpal tunnel</td><td>Pain و numbness و tingling في <b>أول 3 صوابع والإبهام</b></td></tr>
<tr><td><b>Raynaud's</b> (vibration white finger)</td><td>الأوعية الدموية في الإيد بتضيق من <b>vibration</b> طويل (hair clippers، jack hammers)</td><td>تنميل أثناء الـ vibration، و<b>blanching</b> (بياض) لطرف صباع وبعدين الباقي، والألم والنوبات بتزيد مع الوقت</td></tr>
<tr><td><b>Cubital tunnel syndrome</b></td><td>ضغط على الـ <b>ulnar nerve</b> من سند الكوع على أسطح ناشفة</td><td>Pain و tingling و numbness في <b>البنصر والخنصر</b></td></tr>
<tr><td><b>Thoracic outlet syndrome</b></td><td>Reaching فوق الكتف، شيل حاجات تقيلة، أو forward head. الـ <b>brachial plexus</b> بيتضغط بين الـ <b>clavicle وأول ضلع</b></td><td><b>Weakened pulse</b>، numbness في الصوابع</td></tr></table>
<p class="key">من النوتس عن الـ TOS: بيصيب حوالي <b>1%</b> من الناس، <b>أكتر في الستات</b>، غالبًا من <b>20–50 سنة</b>. اتوصف أول مرة <b>1818</b>، واسم "thoracic outlet syndrome" اتستخدم أول مرة <b>1956</b>.</p></div>

<div class="card"><h4>3. Tendon disorders</h4>
<table><tr><th>المرض</th><th>الشرح</th><th>الأعراض</th></tr>
<tr><td><b>Rotator cuff syndrome</b></td><td>Swelling وألم في tendons الـ rotator cuff: <b>subscapularis، supraspinatus، infraspinatus، teres minor</b></td><td>ألم مع ثني الدراع ولفه لبرا ضد مقاومة، ألم برا الكتف ممكن ينزل للدراع، <b>أسوأ بالليل</b>، stiffness</td></tr>
<tr><td><b>Tendinitis</b></td><td>Irritation of the tendon من الضغط المستمر. شائع في الرسغ والكوع والكتف</td><td>Point tenderness، swelling. <b>Lateral epicondylitis = tennis elbow</b> (extension و pronation). <b>Medial epicondylitis = golfer's elbow</b> (flexion و supination)</td></tr>
<tr><td><b>Tenosynovitis</b></td><td>Irritation/swelling of the <b>synovial sheath</b> من الاحتكاك</td><td>Swelling، pain، فقد حركة وقوة</td></tr>
<tr><td><b>Ganglion cyst</b></td><td><b>Bump</b> تحت الجلد من <b>تجمع سوائل جوه الـ tendon sheath</b>، شائع في الإيد والرسغ</td><td>—</td></tr>
<tr><td><b>De Quervain's</b></td><td>التهاب الـ sheath بتاع وترين الإبهام من الاحتكاك = <b>tendinitis + tenosynovitis</b>. من الـ twisting والمسك القوي</td><td>Swelling وألم <b>عند قاعدة الإبهام</b></td></tr></table>
<p>من النوتس عن الـ rotator cuff: شائع في اللي بيشيلوا أوزان تقيلة، وفيه differential diagnosis مع cervical disc و frozen shoulder (adhesive capsulitis) و glenohumeral OA.</p>
<p><b>دراسة Gerr et al. (2002)</b> على <b>632</b> شخص اشتغلوا في شغل فيه 15 ساعة أو أكتر في الأسبوع على الكمبيوتر، واتتابعوا <b>3 سنين</b>: أكتر من <b>50%</b> اشتكوا من muscle soreness في أول سنة. أشهر hand/arm disorder كان <b>De Quervain's tendonitis</b>، وأشهر neck/shoulder disorder كان <b>somatic pain syndrome</b>.</p></div>

<div class="card"><h4>4. Common occupational injuries of the back</h4>
<table><tr><th>الإصابة</th><th>الشرح</th></tr>
<tr><td>1. Strains &amp; sprains</td><td>إصابة tendons و ligaments من مجهود <b>مرة واحدة</b> (شيل تقيل). الألم واضح بس <b>بيهدى في كام يوم</b></td></tr>
<tr><td>2. Facet joint pain</td><td>Irritation في مكان مقابلة الضلوع للعمود. swelling، صعوبة القعدة أو الوقوف مفرود، وأحيانًا صعوبة التنفس العميق</td></tr>
<tr><td>3. Disk erosion</td><td>ضغط طويل على الـ discs فبتنضغط <b>بشكل دائم</b>، والمسافة بين الفقرات تقل، والـ nerve roots تتضغط. <b>القعدة بتضغط على الـ disc أكتر من الوقوف</b>، خصوصًا من غير سند</td></tr>
<tr><td>4. Sciatic nerve impingement</td><td>(Sciatica) شائع في اللي بيقعدوا كتير. swelling في عضلات الـ buttock بيضغط على العصب، فبيحصل ألم نازل في الرجل</td></tr>
<tr><td>5. Herniated (bulging) discs</td><td>الجزء الداخلي (<b>nucleus pulposus</b>) بيطلع ويضغط على الـ nerve roots، فبيحصل ألم أو تنميل في الرجلين</td></tr></table></div>
""",
[
 ("Neurovascular", [
  ("Carpal tunnel syndrome is impingement of the:", ["Median nerve", "Ulnar nerve", "Radial nerve", "Brachial artery"], "imp", ""),
  ("CTS symptoms affect the:", ["First three fingers and the thumb", "Ring and little fingers", "Whole arm", "Shoulder only"], "imp", ""),
  ("Raynaud's syndrome is also known as:", ["Vibration white finger", "Trigger finger", "Tennis elbow", "Golfer's elbow"], "imp", ""),
  ("Raynaud's syndrome is caused by:", ["Repeated exposure to vibration for long periods", "Resting elbows on hard surfaces", "Reaching overhead", "Twisting"], "imp", ""),
  ("Blanching of finger tips is a symptom of:", ["Raynaud's syndrome", "Cubital tunnel", "Ganglion cyst", "Rotator cuff syndrome"], "", ""),
  ("Cubital tunnel syndrome is pressure on the:", ["Ulnar nerve", "Median nerve", "Radial nerve", "Sciatic nerve"], "imp", ""),
  ("Cubital tunnel syndrome is caused by:", ["Resting elbows on hard surfaces", "Vibrating tools", "Heavy lifting", "Typing"], "", ""),
  ("Cubital tunnel symptoms affect the:", ["Ring and little fingers", "Thumb and index", "Middle finger only", "Wrist only"], "imp", ""),
  ("In thoracic outlet syndrome, the brachial plexus is compressed between the:", ["Clavicle and first rib", "Humerus and scapula", "Radius and ulna", "C1 and C2"], "imp", ""),
  ("Thoracic outlet syndrome is caused by all EXCEPT:", ["Resting wrist on desk", "Reaching above shoulder level", "Carrying heavy objects", "Forward head posture"], "", ""),
  ("A symptom of thoracic outlet syndrome is:", ["Weakened pulse", "Bump on wrist", "Pain at thumb base", "Night blindness"], "", ""),
  ("Thoracic outlet syndrome is more common in:", ["Women aged 20–50", "Men over 70", "Children", "Infants"], "", ""),
 ]),
 ("Tendon disorders", [
  ("The rotator cuff muscles include all EXCEPT:", ["Teres major", "Subscapularis", "Supraspinatus", "Infraspinatus"], "imp", ""),
  ("Rotator cuff syndrome pain is typically:", ["Worse at night", "Absent at night", "Only in the hand", "Only on the medial elbow"], "", ""),
  ("Tennis elbow is:", ["Lateral epicondylitis", "Medial epicondylitis", "De Quervain's", "Olecranon bursitis"], "imp", ""),
  ("Golfer's elbow is:", ["Medial epicondylitis", "Lateral epicondylitis", "Tenosynovitis of thumb", "Carpal tunnel"], "imp", ""),
  ("Irritation of the synovial sheath covering the tendon is:", ["Tenosynovitis", "Tendinitis", "Ganglion", "Bursitis"], "imp", ""),
  ("A bump under the skin due to fluid accumulation within the tendon sheath is:", ["Ganglion cyst", "Trigger finger", "Raynaud's", "Tendinitis"], "imp", ""),
  ("De Quervain's disease is a combination of:", ["Tendinitis and tenosynovitis", "CTS and cubital tunnel", "Ganglion and bursitis", "Raynaud's and TOS"], "imp", ""),
  ("De Quervain's disease causes pain at the:", ["Base of the thumb", "Little finger", "Medial elbow", "Shoulder"], "imp", ""),
  ("De Quervain's may be caused by:", ["Twisting and forceful gripping", "Vibration", "Resting elbows", "Overhead reaching"], "", ""),
  ("In Gerr et al. (2002), the most common hand/arm disorder among computer users was:", ["De Quervain's tendonitis", "Carpal tunnel syndrome", "Ganglion cyst", "Raynaud's"], "imp", ""),
  ("In Gerr et al. (2002), more than …… of users reported muscle soreness in the first year:", ["50%", "10%", "90%", "25%"], "", ""),
 ]),
 ("Back injuries", [
  ("Damage to tendons and ligaments from one-time exertion such as heavy lifting is:", ["Strain and sprain", "Disk erosion", "Herniated disc", "Facet joint pain"], "imp", ""),
  ("Strain and sprain pain usually:", ["Subsides within a few days", "Is permanent", "Never hurts", "Needs surgery"], "", ""),
  ("Disk erosion results from:", ["Prolonged pressure on spinal disks", "Single lift", "Vibration", "Infection"], "imp", ""),
  ("Which posture puts more pressure on spinal disks?", ["Sitting (especially unsupported)", "Standing", "Lying supine", "Walking"], "imp", ""),
  ("Sciatica is common in people who:", ["Sit for prolonged periods", "Run daily", "Swim", "Sleep long"], "", ""),
  ("Herniated disc occurs when …… protrudes:", ["The inner portion (nucleus pulposus)", "The annulus only", "The vertebral body", "The facet joint"], "imp", ""),
  ("Facet joint pain may make it difficult to:", ["Breathe deeply", "See", "Hear", "Swallow"], "", ""),
 ]),
])

# ============================================================ Lec 4
T("l4", "Lec 4 — Library Ergonomics", "Lec 4 Library", "📚",
  "نوتس Lec 4 + ملخص Be IN",
"""
<div class="card"><h4>1. Introduction</h4>
<p>شغل المكتبات فيه manual handling كتير (رص الكتب على الرفوف و book carts)، وده بيضغط على الضهر والكتف والدراع والإيد والرسغ، وبيزود الـ <b>repetitive stress injuries</b>.</p></div>

<div class="card"><h4>2. Shelving</h4>
<p><b>Risk factors:</b> weight of books · reaching و bending · high repetition rate.</p>
<table><tr><th>المشكلة</th><th>الحل</th></tr>
<tr><td>Reaching overhead بيضغط على الكتف والدراع والضهر</td><td>استخدم <b>foot stool</b> للرفوف العالية</td></tr>
<tr><td>شيل كتب كتير مرة واحدة</td><td>شيل <b>بس الكتاب اللي هترصه</b></td></tr>
<tr><td>Bending من الوسط بيضغط على الضهر</td><td><b>Squat</b> للرفوف الواطية، والضهر مفرود</td></tr>
<tr><td>الكتب التقيلة بتضغط على الرسغ والدراع</td><td>ارفعها <b>بالإيدين</b> (زي الـ bound volumes)</td></tr>
<tr><td>الـ <b>Pinch grip</b> قوته حوالي <b>25%</b> بس من قوة الإيد كلها، فبيزود risk الرسغ</td><td>استخدم <b>two-handed power grip</b>، وتجنب الـ pinch grip</td></tr>
<tr><td>الإيد المسيطرة بتتعب</td><td><b>بدّل</b> بين الإيد اليمين والشمال</td></tr></table>
<p>ولو ينفع: الكتب التقيلة تتحط في مستوى <b>الوسط (waist height)</b>.</p></div>

<div class="card"><h4>3. Book carts</h4>
<p><b>Risk factors:</b> awkward wrist و hand و arm postures · strain على عضلات الكتف والضهر · <b>collisions</b>.</p>
<ul><li>امشي بسرعة عادية أو بطيئة، والـ cart يسيب مكان لرجلك وتكون قريبة منك.</li>
<li><b>متستخدمش</b> cart بايظ (خصوصًا العجل)، أو cart بيحجب رؤيتك.</li>
<li><b>Push rather than pull</b>، ما عدا: <b>pull</b> وانت خارج من الأسانسير، و<b>pull</b> في الأبواب الـ swinging.</li>
<li>زق من <b>الطرف مش الجناب</b>، واطلب مساعدة للـ cart الكبير أو المليان، واستخدم carts بـ handles.</li>
<li><b>Inspection</b> قبل الاستخدام: العجل loose أو worn، الـ stability، سهولة الحركة والمناورة. والعجل أهم حاجة في الصيانة.</li></ul></div>

<div class="card"><h4>4. Lifting &amp; carrying</h4>
<ul><li>اثني الركب والضهر مفرود، وقرّب الحمل وارفع برجلك.</li>
<li>اطلب مساعدة للحمل الكبير أو التقيل أو الغريب، وشيله قريب من جسمك.</li>
<li>الحمل التقيل في مستوى الوسط.</li>
<li><b>Take a step and turn</b> بدل ما تلف الجذع (twisting).</li></ul></div>

<div class="card"><h4>5. Work organization</h4>
<p><b>Stretch breaks</b> · نوّع المهام · بدّل الإيدين والدراعات · اشتغل بسرعة مريحة، لأن السرعة الزيادة مش بتدي الجسم وقت يرتاح من الحركات المتكررة أو القوية.</p></div>
""",
[
 ("Library ergonomics", [
  ("Library tasks increase the risk of:", ["Repetitive stress injuries", "Infections", "Fractures only", "Hearing loss"], "", ""),
  ("Risk factors for shelving include all EXCEPT:", ["Using a foot stool", "Weight of books", "Reaching and bending", "High repetition"], "", ""),
  ("When shelving books on high shelves you should:", ["Use a foot stool", "Reach overhead", "Jump", "Use one hand"], "imp", ""),
  ("When shelving on low shelves you should:", ["Squat with the back straight", "Bend at the waist", "Kneel on one knee only", "Twist"], "imp", ""),
  ("While shelving you should carry:", ["Only the book being shelved", "As many books as possible", "A full cart", "Books in one hand"], "", ""),
  ("Pinch grip strength is approximately …… of whole-hand strength:", ["25%", "75%", "50%", "100%"], "imp", ""),
  ("The recommended grip while shelving is:", ["Two-handed power grip", "Pinch grip", "One finger grip", "Hook grip"], "imp", ""),
  ("Heavy books should be located, if practical, at:", ["Waist height", "Top shelf", "Floor level", "Overhead"], "", ""),
  ("Risk factors for book carts include all EXCEPT:", ["Walking at a slow pace", "Awkward wrist postures", "Strain on shoulder and back", "Collisions"], "", ""),
  ("In general, book carts should be:", ["Pushed rather than pulled", "Pulled always", "Lifted", "Dragged by one hand"], "imp", ""),
  ("Book carts should be pulled when:", ["Exiting elevators and through swinging doors", "On flat floors", "Going straight", "Never"], "imp", ""),
  ("Book carts should be pushed from:", ["The end, not the sides", "The sides", "The top", "The wheels"], "", ""),
  ("The most important part to maintain in a book cart is the:", ["Wheels", "Color", "Handles only", "Shelves"], "", ""),
  ("Instead of twisting while carrying, you should:", ["Take a step and turn", "Twist faster", "Rotate the trunk", "Lean backward"], "imp", ""),
  ("Working at too fast a speed is harmful because:", ["It doesn't allow the body to recover", "It increases rest", "It reduces repetition", "It improves posture"], "", ""),
 ]),
])

# ============================================================ Lec 5
T("l5", "Lec 5 — Lifting Process", "Lec 5 Lifting", "🏋️",
  "نوتس Lec 5 + ملخص Be IN",
"""
<div class="card"><h4>1. Factors affecting load on the spine during lifting</h4>
<p><b>1) Position of the object</b> بالنسبة لـ center of motion الـ spine: لازم الحاجة <b>قريبة من الجسم</b>. لو بعيدة، المسافة بين الـ COG بتاعها والـ spine بتزيد، فالـ <b>bending moment</b> والحمل على عضلات الضهر بيزيدوا.</p>
<p><b>2) Degree of flexion &amp; rotation</b>: الـ spine أكتر flexibility في الـ flexion من الـ extension. وكل ما الـ flexion يزيد، الـ bending moment يزيد، فعضلات الضهر تشتغل أكتر والحمل على الـ discs يزيد.</p>
<table><tr><th>الـ Flexion</th><th>اللي بيشيل الحمل</th></tr>
<tr><td>لحد <b>60°</b></td><td><b>عضلات الضهر</b> نشاطها بيزيد عشان توازن وزن الجزء العلوي</td></tr>
<tr><td>أكتر من <b>60°</b></td><td>عضلات الضهر <b>inactive</b> والحمل على الـ <b>ligaments</b>. والـ ligaments مرونتها أقل فبتتصاب أسهل</td></tr></table>
<p class="key">Flexion أكتر من 60° + شيل تقيل بشكل <b>مفاجئ أو jerky</b> = <b>lumbar disc prolapse</b>.</p>
<p><b>3) Characteristics of the object</b> (size، weight، density، shape): لو الحاجة <b>كبيرة</b> أو <b>تقيلة</b>، الـ bending moment بيزيد، فعضلات الضهر تشتغل أكتر، والحمل والـ <b>intradiscal pressure</b> يزيدوا.</p></div>

<div class="card"><h4>2. Role of abdominal muscles &amp; intra-abdominal pressure</h4>
<table><tr><th>Strong abdominals</th><th>Weak abdominals</th></tr>
<tr><td>بتعمل intra-abdominal و intra-thoracic pressure عالي، فالحمل على الـ discs والـ lumbar spine بيقل، والقدرة على الشيل بتزيد. في الرياضيين الحمل بيقل <b>40%</b>.<br>والـ IAP بيزيد مع زيادة الوزن وسرعة الرفع</td>
<td>مش بتعمل IAP كفاية، فالحمل على الـ discs بيزيد. ولو حاول يعمل IAP عالي ممكن يحصل <b>hernia</b>.<br><b>Belly abdomen</b> يعني forward moment أكبر، فالـ erector spinae تشتغل أكتر، والحمل على الـ disc والـ joint reaction force يزيدوا</td></tr></table>
<p class="key">N.B: المريض اللي عضلات بطنه ضعيفة الأحسن <b>يقوّيها</b> بدل ما يلبس <b>abdominal corset</b>، لأن الكورسيه بيضعّفها أكتر.</p></div>

<div class="card"><h4>3. Steps of proper lifting (5)</h4>
<ol><li><b>Facing correctly</b></li><li><b>Assume natural lifting position</b></li><li><b>Lifting the load</b></li><li><b>Turning properly</b></li><li><b>Putting load down</b></li></ol>
<p><b>Lifting from a shelf:</b> stride standing بـ base واسعة (رجل قدام ورجل ورا)، والوزن على الرجل <b>القدامية</b>. ولما تنزّل الحاجة، الوزن ينتقل للرجل <b>الورانية</b> عشان: تمنع extension زيادة في الـ lumbar، تمنع strain على الضهر، وتزود الـ stability.</p></div>

<div class="card"><h4>4. Carrying a load</h4>
<ol><li><b>قريب من الجسم</b>: يقلل الـ strain ويوفّر طاقة.</li>
<li><b>على أو عند مستوى الكتف</b>: الـ COG قريب من الـ midline.</li>
<li><b>فوق الراس</b>: الـ line of gravity في الـ midline، فالطاقة ونشاط العضلات <b>في أقل حاجة</b>، بس ده مش شائع.</li></ol></div>

<div class="card"><h4>5. Improper lifting</h4>
<ol><li>الرجلين <b>لازقين في بعض</b>، فالـ base of support صغيرة والـ stability أقل.</li>
<li>Friction قليل بين الرجل والأرض.</li>
<li>الإيد مش بتساعد (مسك بأطراف الصوابع).</li>
<li>Extension للجذع، أو رفع jerky، أو twisting.</li>
<li>لف سريع، أو لف بالجذع والرجلين ثابتين.</li>
<li><b>ركب مفرودة + flexion للجذع</b>، ودي بتعمل:
<br>a. Bending moment أكبر، فالضغط والـ strain على الضهر يزيدوا.
<br>b. Torque على الـ lumbar بيزيد مع زيادة الـ flexion.
<br>c. زاوية شد عضلات الضهر <b>بتقل</b>، فالـ effective component صغير، ومع الـ length-tension relationship الـ tension والـ compressive force بيزيدوا.</li></ol></div>
""",
[
 ("Factors affecting spinal load", [
  ("To reduce the load on the spine, the object should be:", ["As close to the body as possible", "Far from the body", "Above the head always", "Held with straight arms"], "imp", ""),
  ("Holding the object away from the spine increases the:", ["Bending moment and load on back muscles", "Stability", "Intra-abdominal pressure only", "Base of support"], "imp", ""),
  ("The spine is more flexible in:", ["Flexion than extension", "Extension than flexion", "Rotation only", "Lateral flexion only"], "", ""),
  ("When the spine is flexed up to 60°, the load is carried mainly by:", ["Back muscles", "Ligaments", "Bones", "Abdominal muscles"], "imp", ""),
  ("When spinal flexion exceeds 60°, the load is carried by:", ["Spinal ligaments (muscles inactive)", "Back muscles", "Abdominal muscles", "Hip flexors"], "imp", ""),
  ("Ligaments are more susceptible to injury than muscles because:", ["Their elastic property is less", "They are stronger", "They contract actively", "They have more blood supply"], "", ""),
  ("Lifting a heavy load suddenly with spinal flexion > 60° may lead to:", ["Lumbar disc prolapse", "Carpal tunnel", "Raynaud's", "Ganglion"], "imp", ""),
  ("A big or heavy object increases all EXCEPT:", ["Base of support", "Bending moment", "Back muscle moment", "Intradiscal pressure"], "", ""),
 ]),
 ("Abdominals & IAP", [
  ("Strong abdominal muscles during lifting:", ["Create high intra-abdominal pressure and decrease disc load", "Increase disc load", "Cause hernia", "Have no role"], "imp", ""),
  ("In athletes, intra-abdominal pressure decreases the load on the lumbar spine by:", ["40%", "4%", "90%", "10%"], "imp", ""),
  ("Intra-abdominal pressure increases with:", ["Heavier weight and faster lifting", "Lighter weight", "Slower lifting only", "Lying down"], "", ""),
  ("Trying to create high IAP with weak abdominal muscles may lead to:", ["Hernia", "Kyphosis", "Raynaud's", "Ganglion"], "imp", ""),
  ("Weak abdominal muscles cause belly abdomen which increases:", ["Erector spinae activity and disc load", "Base of support", "Stability", "Flexibility"], "", ""),
  ("A patient with weak abdominal muscles is advised to:", ["Strengthen the abdominal muscles rather than wear a corset", "Wear an abdominal corset", "Avoid exercise", "Lift heavier loads"], "imp", ""),
 ]),
 ("Proper lifting & carrying", [
  ("The number of steps of proper lifting is:", ["5", "3", "7", "10"], "", ""),
  ("The first step of proper lifting is:", ["Facing correctly", "Lifting the load", "Turning properly", "Putting the load down"], "imp", ""),
  ("When lifting from a shelf, body weight is initially on the:", ["Forward leg", "Backward leg", "Both equally", "Toes only"], "imp", ""),
  ("As the object is lifted down from a shelf, weight shifts to the backward leg to:", ["Prevent undue lumbar extension and increase stability", "Increase lumbar extension", "Decrease base of support", "Speed up"], "", ""),
  ("Carrying the load overhead:", ["Minimizes energy expenditure and muscle activity", "Maximizes back strain", "Is the most common method", "Moves COG away from midline"], "imp", ""),
  ("Improper lifting includes all EXCEPT:", ["Wide base of support", "Feet close together", "Twisting while lifting", "Jerky lifting"], "imp", ""),
  ("Lifting with straight knees and trunk flexion:", ["Increases bending moment and lumbar torque", "Is the safest method", "Decreases disc pressure", "Uses leg muscles"], "imp", ""),
  ("As back flexion increases, the angle of pull of back muscles:", ["Decreases, increasing compressive force", "Increases", "Does not change", "Becomes 90°"], "", ""),
 ]),
])

# ============================================================ Lec 6
T("l6", "Lec 6 — Human-Machine System (Ergosystem)", "Lec 6 Human-machine", "🤖",
  "صور نوتس Lec 6",
"""
<div class="card"><h4>1. Components of the human-machine system (3)</h4>
<table><tr><th>Component</th><th>بيشمل</th></tr>
<tr><td>1. <b>Human</b></td><td>كل خصائص الإنسان: anatomical و physiological و psychological</td></tr>
<tr><td>2. <b>Machine</b></td><td>الكراسي والأدوات والمعدات اللي الإنسان بيتعامل معاها</td></tr>
<tr><td>3. <b>Environment</b></td><td>المكان والظروف. <b>Physical</b>: noise، vibration، light، climate، chemicals. <b>Social</b>: الأسرة والناس اللي حواليه زي الزملا</td></tr></table>
<ul><li><b>Work space</b> = الـ <b>three dimension space</b> اللي الشغل بيتعمل فيه. محتاج دراسة أبعاد الماكينة وأبعاد الإنسان (<b>anthropometry</b>)، والأنشطة ومعدل الشغل.</li></ul></div>

<div class="card"><h4>2. Simple vs complex ergosystem</h4>
<table><tr><th>Simple</th><th>Complex</th></tr>
<tr><td><b>إنسان واحد + ماكينة واحدة</b></td><td>إنسان واحد مع <b>ماكينات مختلفة</b>، أو <b>ناس كتير</b> على ماكينة واحدة</td></tr></table>
<ul><li><b>Output</b>: ممكن يطلع من الماكينة تحت تحكم الإنسان، أو من الإنسان لما ياخد قرار. وممكن يكون <b>إنسان</b> زي المستشفى، فالـ output بتاعها <b>مرضى اتعالجوا</b>.</li>
<li>كل الـ ergosystems متصلة ببعض بالـ inputs والـ outputs، فالـ output بتاع system ممكن يبقى input لغيره.</li>
<li>الرسمة: Input → <b>sense</b> → <b>CNS</b> → MS → <b>controls</b> → central processing (machine) → <b>display</b> → Output.</li></ul></div>

<div class="card"><h4>3. The human component</h4>
<ul><li><b>Senses</b> = وسيلة الـ <b>input</b>: الـ 5 (sight، smell، taste، hearing، touch)، وغيرهم زي balance، body position in space، sense of speed.</li>
<li><b>Brain</b> = مركز معالجة المعلومات. فيه <b>low level programs</b> للـ sensorimotor activities الأساسية، و<b>higher cognitive processes</b> للـ planning و decision making و problem solving.</li>
<li>الشغل الجسدي والذهني محتاج <b>education، training، energy، motivation</b>، والـ psychological aspects والـ motivation بيدعموا سلوك الشغل.</li>
<li>الـ <b>human errors</b> غالبًا سببها تصميم الـ work space اللي مش واخد في اعتباره خصائص الإنسان وحدوده.</li></ul></div>

<div class="card"><h4>4. Four strategies for an ideal HMS</h4>
<table><tr><th>Strategy</th><th>الفكرة</th></tr>
<tr><td>1. <b>Reducing stress</b></td><td>Physical أو mental. الأجهزة السيئة بتعمل bad posture وضغط غير طبيعي، ولو الـ stress عدّى الـ tolerance فالـ performance والـ productivity بيقلوا والـ safety والصحة بيسوءوا</td></tr>
<tr><td>2. <b>Designing the machines</b></td><td>الأجهزة تتصمم وخصائص الإنسان في الاعتبار، والـ matching الكويس بيخلي الشغل easy و safe و efficient</td></tr>
<tr><td>3. <b>Matching job demands with people's abilities</b></td><td>Demands = abilities يبقى optimal. <b>Abilities أكبر من demands يبقى safer</b>. <b>Demands أكبر من abilities يبقى injuries</b> ومشاكل صحية</td></tr>
<tr><td>4. <b>Educating &amp; training people</b></td><td>تحسين معرفتهم ووعيهم بالبيئة بالـ <b>motor learning</b> (تعلم بالممارسة والخبرة)، وده بيعمل <b>relatively permanent changes</b> في المهارة</td></tr></table>
<p class="key">مفهومين: <b>Fit man to job</b>: زي الطيار، محتاج حد qualified جدًا. <b>Fit job to man</b>: زي شيل الحاجات، مش محتاج تدريب كتير.</p></div>
""",
[
 ("Human-machine system", [
  ("The components of the human-machine system are:", ["Human, machine and environment", "Brain, muscles and bones", "Input, output and feedback only", "Chair, desk and computer"], "imp", ""),
  ("Noise, vibration, light and climate are …… aspects of the environment:", ["Physical", "Social", "Psychological", "Anatomical"], "imp", ""),
  ("Family and colleagues are …… aspects of the environment:", ["Social", "Physical", "Mechanical", "Chemical"], "", ""),
  ("The work space is:", ["The three-dimensional space in which work is carried out", "The office only", "A 2D drawing", "The machine only"], "imp", ""),
  ("The study of human body dimensions is:", ["Anthropometry", "Kinesiology", "Ergometry", "Biomechanics only"], "imp", ""),
  ("A simple ergosystem means:", ["One human and one machine", "Several humans and several machines", "One human with different machines", "No machine"], "imp", ""),
  ("One human interacting with different machines is a:", ["Complex ergosystem", "Simple ergosystem", "Closed system", "Open system"], "", ""),
  ("The output of a hospital ergosystem is:", ["Cured patients", "Machines", "Noise", "Money only"], "imp", ""),
  ("The means of input in the human component are the:", ["Senses", "Muscles", "Controls", "Displays"], "imp", ""),
  ("Planning, decision making and problem solving are …… processes of the brain:", ["Higher level cognitive", "Low level sensorimotor", "Reflex", "Spinal"], "", ""),
  ("Human errors are often attributed to:", ["Design of the work space ignoring human limitations", "Laziness only", "Weather", "Genetics"], "imp", ""),
 ]),
 ("Strategies", [
  ("The number of main strategies for an ideal HMS is:", ["4", "3", "5", "2"], "", ""),
  ("The first strategy is concerned with:", ["Reducing stress", "Designing machines", "Matching demands", "Training"], "imp", ""),
  ("If human abilities exceed task demands, the result is:", ["A safer human-machine system", "Injuries", "Health problems", "Lower productivity"], "imp", ""),
  ("If task demands exceed human abilities, the result is:", ["Injuries and health problems", "Safer system", "Optimal environment", "Better productivity"], "imp", ""),
  ("Motor learning leads to:", ["Relatively permanent changes in skilled performance", "Temporary fatigue", "Loss of skills", "No change"], "", ""),
  ("'Fit man to job' is exemplified by:", ["A pilot flying a fighter airplane", "Carrying objects", "Sitting at a desk", "Walking"], "imp", ""),
  ("'Fit job to man' is exemplified by:", ["Carrying objects (little training needed)", "Pilot", "Surgeon", "Astronaut"], "", ""),
 ]),
])

TF_DRILL = [
 ("'Ergo' means work and 'nomics' means study of.", 0, ""),
 ("The backpack should not exceed 10–20% of the child's body weight.", 0, ""),
 ("A backpack moves the COG forward.", 1, "لورا، والجسم بيميل لقدام."),
 ("One-strap backpacks may cause scoliosis.", 0, ""),
 ("Approximately 24% of workplace injuries are back injuries.", 0, ""),
 ("Administrative controls are the preferred mechanism for ergonomic hazards.", 1, "Engineering controls."),
 ("Prolonged typing is an example of contact stress.", 1, "Repetition."),
 ("Carpal tunnel syndrome affects the ulnar nerve.", 1, "Median."),
 ("Cubital tunnel syndrome affects the ring and little fingers.", 0, ""),
 ("Raynaud's syndrome is caused by vibration.", 0, ""),
 ("De Quervain's disease is a combination of tendinitis and tenosynovitis.", 0, ""),
 ("Tennis elbow is medial epicondylitis.", 1, "Lateral."),
 ("Standing puts more pressure on spinal disks than sitting.", 1, "القعدة أكتر."),
 ("Pinch grip is about 25% of whole-hand strength.", 0, ""),
 ("Book carts should be pulled through swinging doors.", 0, ""),
 ("Above 60° of spinal flexion, back muscles carry the load.", 1, "الـ ligaments."),
 ("Strong abdominal muscles reduce load on the lumbar spine by 40% in athletes.", 0, ""),
 ("Wearing an abdominal corset is better than strengthening weak abdominals.", 1, "التقوية أحسن."),
 ("Carrying a load overhead minimizes energy expenditure.", 0, ""),
 ("A simple ergosystem is one human and one machine.", 0, ""),
 ("If task demands exceed human abilities, the system is safer.", 1, "بيحصل injuries."),
]
