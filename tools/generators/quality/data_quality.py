# Quality Principles — PT12 midterm (answers as provided by the batch). (text, options, correct_index, explanation)
PT12 = [
 ("Which of the following best describes the primary purpose of ISO standards?", ["To enforce strict legal penalties on non-compliant corporations worldwide", "To ensure consistency and reliability, facilitate international trade, and protect consumers and end-users", "To replace local government laws with mandatory global legislation", "To completely eliminate all operational risks in manufacturing sectors"], 1, "الـ ISO standards هدفها consistency و reliability، وتسهيل التجارة الدولية، وحماية المستهلك. ومش قوانين ولا عقوبات."),
 ("Healthcare quality in simple terms means:", ["Treating as many patients as possible", "Using the most expensive equipment", "Doing the right thing, at the right time, for the right patient, in the best possible way", "Avoiding all complaints"], 2, ""),
 ("How is a 'process' defined under Quality Management Principle 4 (Process Approach)?", ["A series of activities that transform inputs into outputs, adding value along the way", "An unchangeable legal constraint imposed by external regulators", "A temporary project with a strict beginning and end date", "A series of isolated departmental tasks performed independently"], 0, "Inputs → activities → outputs مع إضافة value."),
 ("'Avoiding waste of equipment, supplies, ideas and energy' describes:", ["Effectiveness", "Equity", "Patient-centeredness", "Efficiency"], 3, "Efficiency = تجنب الهدر."),
 ("What are the key responsibilities of a 'Process Owner' in healthcare quality management?", ["Personally executing every single task within the process workflow", "Responsibility for the process's design, performance, and improvement", "Conducting legal defense during medical malpractice lawsuits", "Funding the hospital's annual marketing campaigns"], 1, ""),
 ("Which is part of the Technical Component of healthcare delivery?", ["Evidence-based care", "Respect & empathy", "Clear communication", "Shared decision-making"], 0, "الباقيين تبع الـ interpersonal component."),
 ("Which stage in the ISO standard development process is the first opportunity for broad stakeholder input and comment/voting by all member bodies?", ["Approval Stage", "Enquiry Stage", "Preparatory Stage", "Proposal Stage"], 1, ""),
 ("How many domains of quality does the IOM define?", ["5", "7", "4", "6"], 3, "الستة: Safe، Effective، Patient-centered، Timely، Efficient، Equitable (STEEEP)."),
 ("In TeamSTEPPS, SBAR stands for:", ["Situation, Background, Assessment, Recommendation", "Situation, Behavior, Analysis, Review", "Support, Briefing, Alert, Report", "Safety, Behavior, Action, Result"], 0, ""),
 ("'Avoiding injuries to patients from the care that is intended to help them' describes which IOM domain?", ["Efficiency", "Equity", "Timeliness", "Safety"], 3, ""),
]

TABS = []
def T(*a): TABS.append(a)

# ================================================================= Intro / IOM
T("intro", "Healthcare Quality — Definition & IOM Domains", "مقدمة الجودة", "🏥",
  "سلايدات المحاضرة مش موجودة، فالملخص مكمّل من المراجع الأساسية للجودة (IOM و Donabedian و WHO) وأسئلة الميد",
"""
<div class="card"><h4>يعني إيه Healthcare Quality؟</h4>
<ul><li>ببساطة: <b>Doing the right thing, at the right time, for the right patient, in the best possible way</b>.</li>
<li>يعني مش عدد المرضى ولا أغلى أجهزة ولا إنك تتجنب الشكاوى وخلاص. المهم إن الرعاية تبقى صح ومناسبة وفي وقتها.</li></ul></div>

<div class="card"><h4>الـ 6 IOM domains of quality (STEEEP)</h4>
<p>الـ <b>Institute of Medicine (IOM)</b> حدد <b>6 domains</b>:</p>
<table><tr><th>Domain</th><th>المعنى</th></tr>
<tr><td>Safe</td><td>Avoiding injuries to patients from the care that is intended to help them</td></tr>
<tr><td>Effective</td><td>تقديم الخدمة المبنية على الـ scientific evidence لكل اللي هيستفيد منها، ومنعها عن اللي مش هيستفيد (avoid underuse & overuse)</td></tr>
<tr><td>Patient-centered</td><td>Care that respects and responds to patient preferences, needs and values</td></tr>
<tr><td>Timely</td><td>تقليل الانتظار والـ harmful delays للي بيستقبل الخدمة واللي بيقدمها</td></tr>
<tr><td>Efficient</td><td>Avoiding waste of equipment, supplies, ideas and energy</td></tr>
<tr><td>Equitable</td><td>الجودة متختلفش حسب الـ gender أو الـ ethnicity أو المكان أو الوضع المادي</td></tr></table>
<p class="key">احفظ الكلمة: <b>STEEEP</b> = Safe · Timely · Effective · Efficient · Equitable · Patient-centered. وجه في الميد: "How many domains?" = <b>6</b>.</p></div>

<div class="card"><h4>تعريفات مهمة</h4>
<ul><li><b>Quality (IOM)</b>: The degree to which health services for individuals and populations <b>increase the likelihood of desired health outcomes</b> and are consistent with <b>current professional knowledge</b>.</li>
<li><b>WHO</b>: Quality of care = the extent to which health care services improve health outcomes. والـ WHO بيضيف إن الرعاية تبقى <b>integrated</b> و effective و safe و people-centred و timely و equitable و efficient.</li></ul>
<table><tr><th>المصطلح</th><th>المعنى</th></tr>
<tr><td>Quality Control (QC)</td><td>فحص المنتج/الخدمة بعد ما تتعمل عشان تكتشف الأخطاء (inspection)</td></tr>
<tr><td>Quality Assurance (QA)</td><td>التأكد إن الخدمة مطابقة للـ standards، وتركيزه على <b>منع</b> الأخطاء (يعني retrospective audit + standards)</td></tr>
<tr><td>Quality Improvement (QI)</td><td>تحسين <b>مستمر</b> ومنظم للـ processes بالـ data (continuous)</td></tr>
<tr><td>Quality Management (QM)</td><td>المظلة الكبيرة: planning + control + assurance + improvement</td></tr>
<tr><td>Total Quality Management (TQM)</td><td>فلسفة إن <b>كل الناس في المؤسسة</b> مسؤولين عن الجودة، والتركيز على الـ customer والـ continuous improvement</td></tr></table></div>

<div class="card"><h4>Donabedian model (Structure – Process – Outcome)</h4>
<table><tr><th>العنصر</th><th>يعني إيه</th><th>أمثلة</th></tr>
<tr><td>Structure</td><td>الإمكانيات والبيئة اللي الرعاية بتتقدم فيها</td><td>المباني، الأجهزة، عدد الستاف ومؤهلاتهم، الـ policies</td></tr>
<tr><td>Process</td><td>اللي بيتعمل فعلًا للمريض (الـ care نفسها)</td><td>التشخيص، العلاج، الـ communication، الالتزام بالـ guidelines</td></tr>
<tr><td>Outcome</td><td>النتيجة على صحة المريض</td><td>Mortality، recovery، complications، readmission، patient satisfaction</td></tr></table>
<p class="key">الترتيب: Structure ← يأثر على Process ← يأثر على Outcome.</p></div>

<div class="card"><h4>PDCA cycle (Deming cycle)</h4>
<ol class="ltr"><li><b>Plan</b>: حدد المشكلة والهدف وخطة التغيير</li><li><b>Do</b>: نفّذ التغيير على نطاق صغير (pilot)</li><li><b>Check (Study)</b>: قيس النتايج وقارنها بالهدف</li><li><b>Act</b>: عمّم التغيير لو نجح، أو عدّل وابدأ دورة جديدة</li></ol>
<p>دي أداة الـ <b>continuous improvement</b> الأساسية، واتنسبت لـ <b>Deming</b> (ومعروفة كمان بـ Shewhart cycle).</p></div>

<div class="card"><h4>Components of healthcare delivery</h4>
<table><tr><th>Component</th><th>أمثلة</th></tr>
<tr><td>Technical</td><td><b>Evidence-based care</b>، التشخيص والعلاج الصح، الـ clinical skills</td></tr>
<tr><td>Interpersonal</td><td>Respect &amp; empathy، clear communication، shared decision-making</td></tr>
<tr><td>Amenities</td><td>الراحة والنضافة والخصوصية وأماكن الانتظار</td></tr></table></div>

<div class="card"><h4>ليه الجودة مهمة؟</h4>
<ul><li>تقليل الـ medical errors والـ adverse events وحماية المريض.</li>
<li>تحسين الـ outcomes ورضا المريض.</li>
<li>تقليل الهدر والتكلفة (ما تعملش تحاليل مكررة أو علاج مش لازم).</li>
<li>الـ accreditation (زي JCI و GAHAR في مصر) والسمعة والتنافسية.</li></ul></div>
""",
[
 ("Definition & domains", [
  ("Healthcare quality in simple terms means:", ["Doing the right thing, at the right time, for the right patient, in the best possible way", "Treating as many patients as possible", "Using the most expensive equipment", "Avoiding all complaints"], "imp", ""),
  ("The number of quality domains defined by the IOM is:", ["6", "4", "5", "7"], "imp", "STEEEP."),
  ("The acronym used to remember the IOM domains is:", ["STEEEP", "SBAR", "PDCA", "SMART"], "", ""),
  ("'Avoiding injuries to patients from the care that is intended to help them' describes:", ["Safety", "Efficiency", "Equity", "Timeliness"], "imp", ""),
  ("'Avoiding waste of equipment, supplies, ideas and energy' describes:", ["Efficiency", "Effectiveness", "Equity", "Patient-centeredness"], "imp", ""),
  ("Providing care that does not vary in quality because of gender, ethnicity, location or socioeconomic status is:", ["Equity", "Efficiency", "Safety", "Timeliness"], "", ""),
  ("Reducing waits and sometimes harmful delays is the domain of:", ["Timeliness", "Effectiveness", "Equity", "Safety"], "", ""),
  ("Care that respects and responds to patient preferences, needs and values is:", ["Patient-centered", "Efficient", "Timely", "Equitable"], "", ""),
  ("Providing services based on scientific knowledge to all who could benefit, avoiding underuse and overuse, is:", ["Effectiveness", "Efficiency", "Equity", "Timeliness"], "", ""),
  ("Which is NOT one of the IOM domains of quality?", ["Profitable", "Safe", "Timely", "Equitable"], "", ""),
 ]),
 ("Definitions & models", [
  ("The IOM defines quality as the degree to which health services:", ["Increase the likelihood of desired health outcomes consistent with current professional knowledge", "Generate maximum profit", "Treat the largest number of patients", "Use the newest technology"], "imp", ""),
  ("The Donabedian model evaluates quality through:", ["Structure, process and outcome", "Plan, do, check, act", "Situation, background, assessment, recommendation", "Input, output, feedback"], "imp", ""),
  ("Number of qualified staff and available equipment are measures of:", ["Structure", "Process", "Outcome", "Equity"], "imp", ""),
  ("Adherence to clinical guidelines is a measure of:", ["Process", "Structure", "Outcome", "Amenities"], "", ""),
  ("Mortality and readmission rates are measures of:", ["Outcome", "Process", "Structure", "Input"], "imp", ""),
  ("In the Donabedian model, structure affects:", ["Process, which affects outcome", "Outcome directly only", "Nothing", "Only cost"], "", ""),
  ("PDCA stands for:", ["Plan, Do, Check, Act", "Prepare, Deliver, Control, Assess", "Plan, Design, Correct, Approve", "Process, Data, Check, Audit"], "imp", ""),
  ("The PDCA cycle is also known as the:", ["Deming cycle", "Donabedian cycle", "SBAR cycle", "ISO cycle"], "", ""),
  ("In PDCA, testing a change on a small scale happens in the:", ["Do step", "Plan step", "Check step", "Act step"], "", ""),
  ("Inspecting a product or service after it is produced to detect defects is:", ["Quality control", "Quality improvement", "Total quality management", "Accreditation"], "", ""),
  ("Continuous, data-driven improvement of processes is:", ["Quality improvement", "Quality control", "Inspection", "Licensing"], "", ""),
  ("The philosophy that everyone in the organization is responsible for quality is:", ["Total Quality Management (TQM)", "Quality control", "Audit", "Inspection"], "imp", ""),
 ]),
 ("Technical vs interpersonal", [
  ("Which is part of the Technical component of healthcare delivery?", ["Evidence-based care", "Respect & empathy", "Clear communication", "Shared decision-making"], "imp", ""),
  ("Respect and empathy belong to the:", ["Interpersonal component", "Technical component", "Financial component", "Structural component"], "", ""),
  ("Shared decision-making is part of the:", ["Interpersonal component", "Technical component", "Equipment component", "Legal component"], "", ""),
  ("Clear communication with the patient is part of the:", ["Interpersonal component", "Technical component", "Efficiency domain only", "ISO 15189 standard"], "", ""),
 ]),
])

# ================================================================= Teamwork
T("team", "The Power of Teamwork in Healthcare Delivery", "Teamwork", "🤝",
  "ملف الـ Teamwork in Healthcare (38 slide)",
"""
<div class="card"><h4>What is teamwork?</h4>
<ul><li>مجموعة ناس بـ <b>skills مختلفة</b> شغالين على <b>هدف واحد مشترك (shared goal)</b>.</li>
<li>بيتكلموا بصراحة، وبيثقوا في بعض، وبيشيلوا مسؤولية النتيجة سوا.</li>
<li>في الـ healthcare: <b>المريض وأهله جزء من التيم</b>.</li></ul>
<p>عناصر التيم: <b>Shared goal · Clear roles · Open talk · Mutual trust · Shared ownership</b>.</p>
<p>المحاضرة 3 نقط: (1) The case for teamwork (2) Building effective teams (3) Impact &amp; sustainability.</p></div>

<div class="card"><h4>Point 1 — The case for teamwork (ليه مينفعش نشتغل في silos)</h4>
<ul><li><b>One patient, many hands</b>: إقامة واحدة في المستشفى ممكن يشارك فيها دستة professionals أو أكتر، ومحدش شايف الصورة كاملة لوحده. (الرسم: clinic visit 3، ward stay 8، surgery 12، ICU 15 professionals)</li>
<li><b>Care team</b>: مش دكاترة وتمريض بس. فيه pharmacist و therapist و social worker و technician، و<b>المريض في النص</b>.</li></ul>
<table><tr><th>Silos</th><th>Collaboration</th></tr>
<tr><td>Information stays local<br>Tests get repeated<br>Patient carries the load</td><td>Information flows freely<br>One coordinated plan<br>Team carries the load</td></tr></table>
<ul><li><b>Where things go wrong</b>: أغلب الـ adverse events سببها <b>طريقة الكلام (communication)</b> مش قلة المهارة. الـ handoffs بين الشيفتات <b>weak spot</b>، والـ unclear roles بتخلي مهام تقع.
<br>الأرقام (illustrative): <b>Communication gaps 40%</b>، poor handoffs 25%، role confusion 20%، other 15%.</li>
<li><b>The price of working apart</b>: الـ fragmented care = تحاليل بتتعاد و follow-ups بتضيع. التيم المنسق بيقفل الفجوات، والتوفير بيبان <b>خلال سنة</b> (avoidable readmissions index 100 → 82).</li>
<li><b>Shared picture of the patient — 4 habits</b>: Agree on the goal → Share what each knows → Make one plan → Update it together <b>daily</b> (مش عند الـ admission بس).</li>
<li><b>4 principles</b>: <b>Respect</b> لكل المهن · <b>Clear roles</b> · <b>Open talk</b> حتى لو مش مريح · <b>Shared accountability</b>.</li>
<li><b>Patient at the centre</b>: الرعاية <b>with patients, not to them</b>. أسئلتهم بتكشف اللي التيم فوّته. اللوب: Listen → Involve → Explain → Decide together → Follow up.</li>
<li><b>Time lost chasing information</b>: شيفت التمريض: direct care 55%، <b>chasing information 25%</b>، paperwork 20%. الحل: shared notes و quick huddles.</li></ul>
<p class="key">Point 1 باختصار: Care is complex → Silos cause harm → Shared goals fix it.</p></div>

<div class="card"><h4>Point 2 — Building effective teams</h4>
<ul><li><b>Everyone knows their role</b>: مين بيقود، مين بينفذ، مين بيراقب. <b>Skills can overlap, accountability should not</b>. راجع الأدوار مع كل shift change.</li></ul>
<table><tr><th>Unclear roles</th><th>Clear roles</th></tr>
<tr><td>Tasks done twice · Tasks missed · Blame afterwards</td><td>Right person first time · Nothing falls through · Quick calm fixes</td></tr></table>
<ul><li><b>Right mix of skills</b>: مجهود التيم: clinical care 45%، coordination 25%، patient education 20%، admin 10%. الـ coordination والـ education بياخدوا وقت حقيقي فلازم تخطط لهم.</li>
<li><b>SBAR — a common language</b>: script من 4 أجزاء للمحادثات العاجلة، بيخلي المكالمة قصيرة وكاملة وكله يسمع نفس الحاجة بنفس الترتيب:
<ol class="ltr"><li><b>S</b>ituation: what is happening now</li><li><b>B</b>ackground: relevant history</li><li><b>A</b>ssessment: what I think is wrong</li><li><b>R</b>ecommendation: what I need</li></ol></li>
<li><b>Better handoffs</b>: fixed structure لكل handoff. الـ handoff errors نزلت من 12 → 5 لكل 100 مريض في 12 شهر. Small routine, big safety gain.</li>
<li><b>Huddles &amp; rounds</b>: <b>Short and regular beats long and rare</b>. Morning huddle (<b>5 min</b>) → Bedside rounds → Midday check-in → Evening handoff. الـ bedside rounds بتدخل المريض في الكلام.</li></ul>
<table><tr><th>Low psychological safety</th><th>High safety</th></tr>
<tr><td>Mistakes hidden · Questions unasked · <b>Blame culture</b></td><td>Mistakes reported early · Anyone can speak up · <b>Learning culture</b></td></tr></table>
<ul><li><b>Feeling safe to speak up</b>: الـ junior nurse غالبًا أول واحد يشوف المشكلة. القائد بيحدد الجو لما يشكر اللي بيرفع concerns.</li>
<li><b>Leadership</b>: الـ command-and-control بيبطّأ التيم. Team effectiveness: Autocratic 45 &lt; Directive 60 &lt; Coaching 78 &lt; <b>Shared 88</b>. <b>Good leaders ask before they tell</b>.</li>
<li><b>Training together</b>: <b>Simulation drills</b> قبل الأزمة الحقيقية، كورسات <b>TeamSTEPPS</b> لأدوات الـ communication، و<b>debrief</b> قصير بعد الأحداث (teamwork score 52 → 78).</li></ul>
<table><tr><th>Barrier</th><th>Fix</th></tr>
<tr><td>Hierarchy</td><td>Checklists give all a voice</td></tr>
<tr><td>Time pressure</td><td>Protected huddle time</td></tr>
<tr><td>Too many tools</td><td>One shared care plan</td></tr></table>
<p class="key">Point 2 باختصار: Define roles → Use a shared language → Build a safe culture.</p></div>

<div class="card"><h4>Point 3 — Impact &amp; sustainability</h4>
<ul><li><b>What teamwork delivers</b>: Safety · Patient experience · Staff wellbeing · Lower cost = Better care.</li>
<li><b>Fewer adverse events</b> (9 → 4 لكل 1000 patient-days في 4 سنين). و<b>الـ near-miss reporting بيزيد وده signal كويس</b>.</li>
<li><b>Patient satisfaction</b>: siloed 68% · partial 79% · team-based <b>91%</b>. المريض بيعيد حكايته أقل.</li>
<li><b>Staff who stay</b>: engaged 55%، neutral 25%، burned out 20%. Turnover أقل = تكلفة أقل ورعاية أثبت.</li>
<li><b>Shorter stays</b>: average LOS من 6.2 → 5.0 يوم.</li>
<li><b>Savings</b>: readmits 30%، delays 22%، errors 18%، turnover 12%.</li></ul>
<p><b>Example — Sepsis response:</b></p>
<ol class="ltr"><li>Nurse flags early warning signs</li><li>Physician confirms and orders</li><li>Pharmacy prepares antibiotics</li><li>Lab fast-tracks results</li><li>Team reviews the response</li></ol>
<p><b>Rolling it out</b> (start small, learn fast):</p>
<ol class="ltr"><li>Assess current culture</li><li>Set shared goals</li><li>Train together</li><li>Pilot on one unit</li><li>Scale up</li></ol>
<table><tr><th>Measure</th><th>Examples</th></tr>
<tr><td>Safety</td><td>Adverse events, near-misses</td></tr>
<tr><td>Experience</td><td>Patient and staff surveys</td></tr>
<tr><td>Flow</td><td>Length of stay, readmissions</td></tr>
<tr><td>Teamwork</td><td>Huddles held, handoff quality</td></tr></table>
<p>Track <b>a few measures, not fifty</b>، وراجعهم سوا <b>كل شهر</b>.</p>
<p><b>Keeping it going</b>: Culture fades if nobody tends it. الدايرة: <b>Lead → Train → Measure → Celebrate → Improve</b>.</p>
<p class="key">References: IHI (PS 104 Teamwork &amp; Communication)، WHO Safe Surgery Saves Lives، The Joint Commission (Sentinel event root causes)، PubMed (team training).</p></div>
""",
[
 ("Basics & the case for teamwork", [
  ("Teamwork is best defined as:", ["A group of people with different skills working toward one shared goal", "A group of people with identical skills working independently", "A hierarchy where one person decides everything", "Staff working in separate departments"], "imp", ""),
  ("In healthcare, the care team includes:", ["The patient and family as well", "Doctors only", "Doctors and nurses only", "Administrative staff only"], "imp", ""),
  ("All of the following are elements of teamwork EXCEPT:", ["Individual blame", "Shared goal", "Mutual trust", "Shared ownership"], "", ""),
  ("Most adverse events trace back to:", ["How people communicate, not lack of skill", "Lack of clinical skill", "Old equipment", "Patient non-compliance"], "imp", ""),
  ("The largest contributing factor to adverse events in the lecture was:", ["Communication gaps", "Poor handoffs", "Role confusion", "Equipment failure"], "imp", "40% communication gaps."),
  ("A known weak spot in patient care is:", ["Handoffs between shifts", "Morning huddles", "Bedside rounds", "Debriefs"], "", ""),
  ("In 'silos':", ["Information stays local and tests get repeated", "Information flows freely", "One coordinated plan exists", "The team carries the load"], "imp", ""),
  ("In collaboration:", ["One coordinated plan is put in front of everyone", "The patient carries the load", "Each person knows only their piece", "Tests are repeated"], "", ""),
  ("Fragmented care leads to:", ["Repeat tests and missed follow-ups", "Shorter stays", "Fewer readmissions", "Higher staff engagement"], "", ""),
  ("The four habits of a shared picture of the patient should be repeated:", ["Every day", "At admission only", "At discharge only", "Monthly"], "", ""),
  ("The first habit for a shared picture of the patient is:", ["Agree on the goal", "Make one plan", "Update it together", "Discharge the patient"], "", ""),
  ("The four principles that hold teams together are respect, clear roles, open talk and:", ["Shared accountability", "Strict hierarchy", "Individual credit", "Competition"], "imp", ""),
  ("Patient-centred care means care is done:", ["With patients, not to them", "To patients, not with them", "Without informing the family", "By the physician alone"], "imp", ""),
  ("In a typical nursing shift, chasing information takes about:", ["25%", "55%", "5%", "75%"], "", "Direct care 55%، paperwork 20%."),
  ("Time lost chasing information can be won back by:", ["Shared notes and quick huddles", "Longer meetings", "More paperwork", "Working in silos"], "", ""),
 ]),
 ("Building effective teams", [
  ("Regarding roles in a team:", ["Skills can overlap, accountability should not", "Accountability should overlap", "Roles should never be revisited", "Only the leader needs to know the roles"], "imp", ""),
  ("Roles should be revisited:", ["At every shift change", "Once a year", "Only after an error", "Never"], "", ""),
  ("Unclear roles lead to:", ["Tasks done twice, tasks missed and blame", "Right person first time", "Quick, calm fixes", "Nothing falls through"], "", ""),
  ("SBAR stands for:", ["Situation, Background, Assessment, Recommendation", "Situation, Behavior, Analysis, Review", "Support, Briefing, Alert, Report", "Safety, Behavior, Action, Result"], "imp", ""),
  ("In SBAR, 'what I think is wrong' is the:", ["Assessment", "Situation", "Background", "Recommendation"], "imp", ""),
  ("In SBAR, 'what I need' is the:", ["Recommendation", "Assessment", "Background", "Situation"], "", ""),
  ("In SBAR, 'relevant history' is the:", ["Background", "Situation", "Assessment", "Recommendation"], "", ""),
  ("SBAR is mainly used for:", ["Urgent conversations, keeping calls short and complete", "Billing", "Writing research", "Scheduling shifts"], "", ""),
  ("Using a fixed structure for every handoff leads to:", ["Fewer handoff errors", "More errors", "Longer stays", "No change"], "", ""),
  ("Regarding huddles and rounds:", ["Short and regular beats long and rare", "Long and rare beats short and regular", "Huddles should last one hour", "Rounds exclude the patient"], "imp", ""),
  ("The morning huddle lasts about:", ["5 minutes", "30 minutes", "1 hour", "2 hours"], "", ""),
  ("Bedside rounds:", ["Bring the patient into the conversation", "Exclude the patient", "Replace handoffs", "Are done monthly"], "", ""),
  ("In a high psychological safety culture:", ["Mistakes are reported early and anyone can speak up", "Mistakes are hidden", "Questions go unasked", "Blame culture dominates"], "imp", ""),
  ("Leaders set the tone for speaking up by:", ["Thanking people who raise concerns", "Punishing errors", "Ignoring juniors", "Avoiding huddles"], "", ""),
  ("The leadership style with the highest team effectiveness is:", ["Shared", "Autocratic", "Directive", "Command-and-control"], "imp", ""),
  ("'Good leaders …… before they tell':", ["Ask", "Order", "Punish", "Decide"], "", ""),
  ("Simulation drills allow teams to:", ["Practise before a real crisis", "Avoid training", "Replace real care", "Skip debriefs"], "", ""),
  ("TeamSTEPPS-style courses teach:", ["Communication tools", "Surgical techniques", "Billing systems", "Drug doses"], "imp", ""),
  ("A short session after an event that turns experience into learning is a:", ["Debrief", "Huddle", "Handoff", "Round"], "", ""),
  ("The fix for the barrier of hierarchy is:", ["Checklists that give everyone a voice", "Protected huddle time", "One shared care plan", "More tools"], "imp", ""),
  ("The fix for time pressure is:", ["Protected huddle time", "Checklists", "More tools", "Longer shifts"], "", ""),
  ("The fix for too many tools is:", ["One shared care plan", "Checklists", "Protected huddle time", "Hierarchy"], "", ""),
 ]),
 ("Impact & sustainability", [
  ("Teamwork delivers all of the following EXCEPT:", ["Higher avoidable cost", "Safer care", "Better patient experience", "Staff wellbeing"], "imp", ""),
  ("In units with strong teamwork, near-miss reporting:", ["Goes up, which is a good sign", "Goes down", "Stops completely", "Is a bad sign"], "imp", ""),
  ("Patient satisfaction is highest with:", ["Team-based care", "Siloed care", "Partial coordination", "No coordination"], "", "91%."),
  ("Engaged staff are:", ["Less likely to burn out or leave", "More likely to leave", "More expensive", "Less productive"], "", ""),
  ("Smoother handoffs lead to:", ["Shorter length of stay", "Longer stays", "More readmissions", "More errors"], "", ""),
  ("The largest potential saving area in the lecture was:", ["Readmissions", "Turnover", "Errors", "Delays"], "", "Readmits 30%."),
  ("In the sepsis response example, the first step is:", ["Nurse flags early warning signs", "Physician confirms and orders", "Pharmacy prepares antibiotics", "Lab fast-tracks results"], "imp", ""),
  ("In the sepsis response, the last step is:", ["Team reviews the response", "Nurse flags signs", "Lab fast-tracks results", "Patient discharge"], "", ""),
  ("The first step in rolling out teamwork is:", ["Assess current culture", "Scale up", "Pilot on one unit", "Train together"], "imp", ""),
  ("The correct rollout approach is:", ["Start small: pilot on one unit, prove it, then grow", "Apply to the whole hospital at once", "Exclude frontline staff", "Skip assessment"], "", ""),
  ("When measuring teamwork, you should:", ["Track a few measures, not fifty, and review them monthly", "Track as many measures as possible", "Measure only cost", "Never review measures"], "", ""),
  ("'Huddles held and handoff quality' are measures of:", ["Teamwork", "Flow", "Experience", "Safety"], "", ""),
  ("'Length of stay and readmissions' are measures of:", ["Flow", "Safety", "Teamwork", "Experience"], "", ""),
  ("The cycle for keeping team culture going is:", ["Lead, Train, Measure, Celebrate, Improve", "Plan, Do, Check, Act", "Situation, Background, Assessment, Recommendation", "Listen, Involve, Explain"], "", ""),
 ]),
])

# ================================================================= ISO
T("iso", "Lec 2 — ISO Standards", "ISO", "📜",
  "صور سلايدات المحاضرة التانية (Lec2 quality)",
"""
<div class="card"><h4>Learning objectives</h4>
<ol class="ltr"><li>Define ISO and its role in global standardization</li><li>Explain the key requirements of ISO 9001:2015</li><li>Identify the benefits of ISO certification in healthcare settings</li></ol></div>

<div class="card"><h4>What is ISO?</h4>
<ul><li><b>International Organization for Standardization</b>: منظمة <b>independent, non-governmental</b> دولية، أعضاؤها <b>165 national standards bodies</b>.</li>
<li>بتطوّر وتنشر standards <b>voluntary, consensus-based, market-relevant</b> (يعني اختيارية ومش قوانين).</li>
<li>الاسم من الكلمة اليونانية <b>"isos" = equal</b>، وده بيعكس مهمتها: standards متساوية تسهل التجارة والتعاون العالمي.</li>
<li><b>Mission</b>: promote development of standardization in the world، وتسهيل التبادل الدولي للـ goods &amp; services، وتطوير التعاون في الـ intellectual, scientific, technological &amp; economic activity.</li></ul>
<p><b>ISO standards are designed to:</b></p>
<ul class="ltr"><li>Ensure <b>consistency and reliability</b> in products and services</li><li>Facilitate <b>international trade</b> by removing technical barriers</li><li>Promote <b>innovation</b> through shared frameworks</li><li><b>Protect consumers</b> and end-users through quality and safety requirements</li><li>Support <b>sustainable development</b> and environmental protection</li></ul>
<p><b>ISO in healthcare</b>: framework شامل للـ quality management و environmental management و risk management و patient safety، والمؤسسات بتتبناها عشان تثبت التزامها بالجودة والـ continuous improvement.</p></div>

<div class="card"><h4>ISO standard development process — 7 stages</h4>
<table><tr><th>Stage</th><th>اللي بيحصل</th></tr>
<tr><td>1. Proposal</td><td>New work item بيتقترح من national standards body أو industry association أو technical committee</td></tr>
<tr><td>2. Preparatory</td><td><b>Working group of experts</b> (industry, government, academia, consumer organizations) بيجهز الـ working draft</td></tr>
<tr><td>3. Committee</td><td>الـ draft بيلف على الـ technical committee للـ comments و voting، وممكن revisions كتير</td></tr>
<tr><td>4. Enquiry</td><td>الـ draft بيلف على <b>كل الـ ISO member bodies</b>، وده <b>أول فرصة لـ broad stakeholder input</b></td></tr>
<tr><td>5. Approval</td><td>Formal approval: <b>two-thirds majority of participating members</b> + <b>majority of all member votes</b></td></tr>
<tr><td>6. Publication</td><td>الـ standard بيتنشر ويبقى متاح للشراء والتطبيق</td></tr>
<tr><td>7. Review</td><td>مراجعة كل فترة (<b>typically every 5 years</b>) عشان يفضل relevant و up-to-date</td></tr></table>
<p class="key">ترتيب المراحل: <b>P</b>roposal → <b>P</b>reparatory → <b>C</b>ommittee → <b>E</b>nquiry → <b>A</b>pproval → <b>P</b>ublication → <b>R</b>eview.</p></div>

<div class="card"><h4>Origins of ISO 9001</h4>
<ul><li>سنة <b>1987</b> ISO نشرت أول نسخة من ISO 9001، ومعتمدة بشكل كبير على الـ <b>British standard</b>.</li>
<li>اتعملها revisions كتير، وآخرها <b>ISO 9001:2015</b> اللي جابت تغييرات مهمة زي <b>risk-based thinking</b> وتركيز أكبر على <b>leadership engagement</b>.</li></ul></div>

<div class="card"><h4>Healthcare-specific ISO standards</h4>
<table><tr><th>Standard</th><th>بيغطي إيه</th></tr>
<tr><td>ISO 15189</td><td><b>Medical laboratories</b>: quality و competence (pathology, microbiology, clinical chemistry). الـ accreditation بتثبت technical competence ونتايج reliable</td></tr>
<tr><td>ISO 13485</td><td><b>Medical devices</b>: QMS لتصميم وتصنيع وتوزيع الأجهزة. <b>More prescriptive than ISO 9001</b> وفيه risk management و regulatory compliance و traceability</td></tr>
<tr><td>ISO 14971</td><td><b>Medical device risk management</b>: identifying, evaluating, controlling risks طول الـ lifecycle</td></tr>
<tr><td>ISO 22870</td><td><b>Point-of-care testing</b> (زي glucose monitoring و rapid tests جنب المريض)</td></tr>
<tr><td>ISO 22367</td><td><b>Laboratory medicine – risk management</b>، بيكمّل ISO 15189</td></tr>
<tr><td>ISO 7101</td><td><b>Healthcare organization management</b>: أول standard مخصوص لإدارة مؤسسات الصحة، مبني على ISO 9001 ومركز على patient safety و clinical governance و care coordination</td></tr></table></div>

<div class="card"><h4>ISO 9001:2015 — The Quality Management Standard</h4>
<p>Key changes in the 2015 version:</p>
<table><tr><th>Change</th><th>المعنى</th></tr>
<tr><td>Risk-based thinking</td><td>تحديد ومعالجة الـ risks والـ opportunities اللي ممكن تأثر على الـ QMS ونتايجه</td></tr>
<tr><td>Increased emphasis on leadership</td><td>الـ <b>top management</b> مطلوب منها صراحةً تثبت leadership و commitment للـ QMS</td></tr>
<tr><td>Process approach</td><td>إدارة الأنشطة كـ <b>interconnected processes</b> مش tasks منفصلة</td></tr>
<tr><td>Context of the organization</td><td>مراعاة الـ <b>external and internal factors</b> اللي بتأثر على تحقيق الأهداف</td></tr>
<tr><td>Removal of mandatory documentation</td><td>الـ documentation لسه مطلوبة، بس مبقاش لازم "quality manual" أو "documented procedures" بعينها، فبقى فيه <b>flexibility</b></td></tr>
<tr><td>Consolidated structure</td><td>بيستخدم <b>High-Level Structure (HLS)</b> المشترك مع باقي الـ management system standards، فالـ integration أسهل</td></tr></table></div>

<div class="card"><h4>The Seven Quality Management Principles</h4>
<table><tr><th>Principle</th><th>المعنى</th></tr>
<tr><td>1. Customer focus</td><td>فهم وتلبية احتياجات وتوقعات المريض. الـ "customers" في الصحة: <b>patients, families, referrers, payers, regulatory bodies</b></td></tr>
<tr><td>2. Leadership</td><td>Vision و direction للجودة على كل المستويات. أكتر من إصدار أوامر: <b>visible commitment, personal accountability, active engagement</b></td></tr>
<tr><td>3. Engagement of people</td><td>إشراك الستاف على كل المستويات. لما يبقوا engaged و empowered بياخدوا ownership، وأكتر productivity و innovation وبيفضلوا في المؤسسة</td></tr>
<tr><td>4. Process approach</td><td>إدارة الأنشطة كـ interconnected processes. <b>Process = series of activities that transform inputs into outputs, adding value along the way</b></td></tr>
<tr><td>5. Improvement</td><td>تحسين مستمر من خلال structured cycles مش one-off fixes. <b>مش project ليه بداية ونهاية</b>، ده ongoing priority</td></tr>
<tr><td>6. Evidence-based decision making</td><td>استخدام الـ data لتوجيه التدخلات حيث الـ impact أكبر، في القرارات الـ clinical والـ operational</td></tr>
<tr><td>7. Relationship management</td><td>(من الـ ISO 9001 standard، مش ظاهر في الصور) إدارة العلاقة مع الـ interested parties زي الموردين والشركاء والجهات الرقابية عشان نجاح مستدام</td></tr></table></div>

<div class="card"><h4>Process approach in healthcare — key elements</h4>
<ul><li><b>Inputs &amp; outputs</b>: Inputs = information, materials, staff, equipment, time. Outputs = نتيجة الـ process زي diagnosis أو treatment أو medication أو discharge summary.</li>
<li><b>Interconnected processes</b>: الـ output بتاع process بيبقى input لغيره. مثال: prescribing → medication order → dispensing → medication → administration.</li>
<li><b>Process owners</b>: لكل process owner مسؤول عن الـ <b>design, performance, and improvement</b> (ممكن clinicians أو administrators أو multidisciplinary teams).</li>
<li><b>Process metrics</b>: indicators قابلة للقياس: timeliness, accuracy, patient satisfaction, cost, quality.</li>
<li><b>Process documentation</b>: للـ consistency والـ training والتحسين: flowcharts, procedures, policies, work instructions.</li></ul></div>

<div class="card"><h4>Benefits of ISO certification in healthcare</h4>
<ul><li><b>Patient safety</b>: الـ standardized procedures بتقلل الـ variability والـ errors. ISO 9001 بيطلب document procedures و train staff و monitor compliance، فبيبقى فيه approach ثابت وموثوق.</li>
<li><b>Operational efficiency</b>: شيل الـ redundancies و الـ non-value-added activities = cost savings وموارد أكتر لرعاية المريض.</li></ul></div>
""",
[
 ("What is ISO", [
  ("ISO stands for:", ["International Organization for Standardization", "International Standards Office", "Institute of Safety Organizations", "International System of Operations"], "imp", ""),
  ("ISO is:", ["An independent, non-governmental international organization", "A governmental regulatory agency", "A WHO department", "A private hospital network"], "imp", ""),
  ("ISO has a membership of about …… national standards bodies:", ["165", "50", "100", "250"], "", ""),
  ("ISO standards are:", ["Voluntary, consensus-based and market-relevant", "Mandatory laws with penalties", "Applicable to one country only", "Secret documents"], "imp", ""),
  ("The word 'ISO' is derived from the Greek 'isos' meaning:", ["Equal", "Quality", "Standard", "Safe"], "imp", ""),
  ("The primary purpose of ISO standards is:", ["To ensure consistency and reliability, facilitate trade and protect consumers", "To enforce legal penalties on companies", "To replace local government laws", "To eliminate all risks completely"], "imp", ""),
  ("ISO standards facilitate international trade by:", ["Removing technical barriers", "Raising taxes", "Limiting exports", "Replacing currencies"], "", ""),
  ("Which is NOT a design goal of ISO standards?", ["Creating trade barriers between countries", "Promoting innovation", "Protecting consumers", "Supporting sustainable development"], "", ""),
  ("In healthcare, ISO standards provide a framework for all EXCEPT:", ["Marketing campaigns", "Quality management", "Risk management", "Patient safety"], "", ""),
 ]),
 ("Development process", [
  ("The number of stages in ISO standard development is:", ["7", "5", "4", "6"], "", ""),
  ("The first stage of ISO standard development is:", ["Proposal stage", "Preparatory stage", "Enquiry stage", "Approval stage"], "imp", ""),
  ("A working group of experts prepares a working draft in the:", ["Preparatory stage", "Proposal stage", "Committee stage", "Publication stage"], "imp", ""),
  ("The working draft is circulated to the technical committee for comments and voting in the:", ["Committee stage", "Enquiry stage", "Review stage", "Proposal stage"], "", ""),
  ("The first opportunity for broad stakeholder input (all ISO member bodies) is the:", ["Enquiry stage", "Approval stage", "Preparatory stage", "Proposal stage"], "imp", "جه في الميد."),
  ("Approval of an ISO standard requires:", ["Two-thirds majority of participating members and a majority of all member votes", "A simple majority of participating members only", "Unanimous agreement", "Approval by the ISO president"], "imp", ""),
  ("In the publication stage, the standard is:", ["Published and made available for purchase and implementation", "Circulated for comment", "Drafted by experts", "Withdrawn"], "", ""),
  ("ISO standards are typically reviewed every:", ["5 years", "1 year", "10 years", "20 years"], "imp", ""),
  ("Experts in the working group come from all EXCEPT:", ["Only one private company", "Industry", "Academia", "Consumer organizations"], "", ""),
  ("A new work item may be proposed by all EXCEPT:", ["An individual patient", "A national standards body", "An industry association", "A technical committee"], "", ""),
 ]),
 ("ISO 9001 & healthcare standards", [
  ("The first version of ISO 9001 was published in:", ["1987", "2015", "1947", "2000"], "imp", ""),
  ("ISO 9001 drew heavily from the:", ["British standard", "American standard", "German standard", "WHO guidelines"], "", ""),
  ("The most recent version of ISO 9001 is:", ["ISO 9001:2015", "ISO 9001:1987", "ISO 9001:2008", "ISO 9001:2000"], "", ""),
  ("ISO 9001:2015 introduced:", ["Risk-based thinking and stronger leadership engagement", "Mandatory quality manual", "Removal of leadership role", "Isolated task management"], "imp", ""),
  ("ISO 15189 concerns:", ["Medical laboratories", "Medical devices", "Point-of-care testing", "Healthcare organization management"], "imp", ""),
  ("ISO 13485 concerns:", ["Quality management systems for medical devices", "Medical laboratories", "Environmental management", "Point-of-care testing"], "imp", ""),
  ("Compared to ISO 9001, ISO 13485 is:", ["More prescriptive", "Less prescriptive", "Identical", "Voluntary only for labs"], "", ""),
  ("ISO 14971 concerns:", ["Medical device risk management", "Medical laboratories", "Healthcare organization management", "Point-of-care testing"], "imp", ""),
  ("ISO 22870 concerns:", ["Point-of-care testing", "Medical devices", "Laboratory risk management", "Environmental management"], "", ""),
  ("Glucose monitoring at the patient's bedside is covered by:", ["ISO 22870", "ISO 15189", "ISO 13485", "ISO 7101"], "", ""),
  ("ISO 22367 (laboratory medicine – risk management) complements:", ["ISO 15189", "ISO 13485", "ISO 7101", "ISO 22870"], "", ""),
  ("The standard specifically for healthcare organization management is:", ["ISO 7101", "ISO 9001", "ISO 15189", "ISO 14971"], "imp", ""),
 ]),
 ("ISO 9001:2015 changes & principles", [
  ("'Organizations must identify and address risks and opportunities' describes:", ["Risk-based thinking", "Process approach", "Context of the organization", "Customer focus"], "imp", ""),
  ("'Top management is explicitly required to demonstrate leadership and commitment' describes:", ["Increased emphasis on leadership", "Engagement of people", "Removal of documentation", "Risk-based thinking"], "", ""),
  ("'Considering external and internal factors affecting quality objectives' describes:", ["Context of the organization", "Process approach", "Improvement", "Leadership"], "imp", ""),
  ("Regarding documentation in ISO 9001:2015:", ["Still required, but no longer mandates a specific quality manual", "Completely abolished", "A quality manual is mandatory", "Only verbal procedures are allowed"], "imp", ""),
  ("ISO 9001:2015 uses a structure shared with other standards called:", ["High-Level Structure (HLS)", "Low-Level Structure", "PDCA structure", "SBAR structure"], "imp", ""),
  ("The number of quality management principles is:", ["7", "6", "5", "8"], "imp", ""),
  ("The first quality management principle is:", ["Customer focus", "Leadership", "Improvement", "Process approach"], "", ""),
  ("In healthcare, 'customers' include all EXCEPT:", ["Competitor hospitals", "Patients and families", "Payers", "Regulatory bodies"], "", ""),
  ("Leadership as a principle requires:", ["Visible commitment, personal accountability and active engagement", "Simply issuing directives", "Avoiding staff contact", "Delegating all quality work"], "", ""),
  ("Engaged and empowered employees:", ["Take ownership and are more likely to stay", "Leave the organization faster", "Are less productive", "Resist improvement"], "", ""),
  ("A 'process' under the Process Approach principle is:", ["A series of activities that transform inputs into outputs, adding value", "An isolated departmental task", "A legal constraint", "A temporary project"], "imp", "جه في الميد."),
  ("Improvement as a principle is:", ["An ongoing priority through structured cycles, not one-off fixes", "A project with a beginning and an end", "Only needed after accidents", "Optional"], "imp", ""),
  ("The seventh quality management principle is:", ["Relationship management", "Customer focus", "Risk-based thinking", "Documentation"], "", ""),
  ("Using data to target interventions where they have greatest impact is:", ["Evidence-based decision making", "Customer focus", "Leadership", "Engagement of people"], "", ""),
 ]),
 ("Process approach & benefits", [
  ("The person responsible for a process's design, performance and improvement is the:", ["Process owner", "Patient", "Auditor", "Supplier"], "imp", "جه في الميد."),
  ("Process outputs in healthcare may include all EXCEPT:", ["Staff and equipment", "A diagnosis", "A treatment", "A discharge summary"], "", "دي inputs."),
  ("The output of the prescribing process (a medication order) serves as input to the dispensing process. This illustrates:", ["Interconnected processes", "Process metrics", "Process documentation", "Customer focus"], "imp", ""),
  ("Timeliness, accuracy, patient satisfaction and cost are examples of:", ["Process metrics", "Process inputs", "Process owners", "ISO stages"], "", ""),
  ("Flowcharts, procedures, policies and work instructions are forms of:", ["Process documentation", "Process metrics", "Process outputs", "Risk-based thinking"], "", ""),
  ("ISO certification improves patient safety mainly by:", ["Standardized procedures that reduce variability and errors", "Reducing staff training", "Removing documentation", "Increasing tests"], "imp", ""),
  ("Operational efficiency from ISO comes from:", ["Eliminating redundancies and non-value-added activities", "Hiring more staff", "Buying more equipment", "Longer hospital stays"], "", ""),
 ]),
])

TF_DRILL = [
 ("ISO is a governmental organization.", 1, "Independent, non-governmental."),
 ("ISO standards are voluntary and consensus-based.", 0, ""),
 ("'Isos' is a Greek word meaning equal.", 0, ""),
 ("The enquiry stage is the first opportunity for broad stakeholder input.", 0, ""),
 ("Approval of an ISO standard requires a simple majority of participating members.", 1, "Two-thirds of participating + majority of all votes."),
 ("ISO standards are typically reviewed every 10 years.", 1, "كل 5 سنين."),
 ("The first version of ISO 9001 was published in 1987.", 0, ""),
 ("ISO 9001:2015 requires a specific quality manual.", 1, "شال الـ mandatory documentation."),
 ("ISO 13485 is less prescriptive than ISO 9001.", 1, "More prescriptive."),
 ("ISO 15189 is for medical laboratories.", 0, ""),
 ("ISO 7101 is a standard for healthcare organization management.", 0, ""),
 ("ISO 22870 addresses point-of-care testing.", 0, ""),
 ("Improvement is a project with a beginning and an end.", 1, "Ongoing priority."),
 ("A process transforms inputs into outputs, adding value along the way.", 0, ""),
 ("There are 7 quality management principles.", 0, ""),
 ("The IOM defines 4 domains of quality.", 1, "6 (STEEEP)."),
 ("Evidence-based care is part of the interpersonal component.", 1, "Technical."),
 ("Most adverse events are due to lack of clinical skill.", 1, "بسبب الـ communication."),
 ("Skills can overlap, but accountability should not.", 0, ""),
 ("Long and rare meetings are better than short and regular huddles.", 1, "Short and regular beats long and rare."),
 ("In SBAR, B stands for Behavior.", 1, "Background."),
 ("An increase in near-miss reporting is a bad sign.", 1, "Good sign."),
 ("Shared leadership gives the highest team effectiveness.", 0, ""),
 ("The patient and family are part of the healthcare team.", 0, ""),
 ("In the Donabedian model, mortality rate is a structure measure.", 1, "Outcome."),
 ("PDCA stands for Plan, Do, Check, Act.", 0, ""),
 ("Number of staff and equipment are structure measures.", 0, ""),
 ("Rolling out teamwork should start on the whole hospital at once.", 1, "Pilot on one unit then scale up."),
 ("Care should be done to patients, not with them.", 1, "With patients, not to them."),
]
