# Book-based additions ("Foundations of Healthcare Quality" — Dr. Eman, kfs-book 2026). Patches TABS from data_quality.
from data_quality import PT12, TABS as _T, TF_DRILL as _TF
BOOK = "كتاب المادة (Foundations of Healthcare Quality)"

CH1_SUM = """
<div class="card"><h4>Learning objectives</h4>
<ol class="ltr"><li>Define healthcare quality</li><li>Explain the six IOM quality domains</li><li>Distinguish between QA and QI</li><li>Understand the systems approach to healthcare quality</li></ol></div>

<div class="card"><h4>1. Definition of quality</h4>
<ul><li><b>Quality</b> (عمومًا): the degree to which a product, service or process <b>meets or exceeds customer expectations</b> and is <b>free from deficiencies</b>.</li>
<li><b>IOM definition</b>: The degree to which health care services for individuals and populations <b>increase the likelihood of desired health outcomes</b> and are <b>consistent with current professional knowledge</b>.<br>فيه فكرتين: الوصول للـ desired outcomes، والرعاية مبنية على الـ current evidence.</li>
<li><b>Simple definition</b>: Doing the right thing, at the right time, for the right patient, in the best possible way.</li></ul></div>

<div class="card"><h4>2. Quality in manufacturing vs healthcare</h4>
<p>جودة الـ healthcare أعقد من جودة المصانع لـ 3 أسباب:</p>
<table><tr><th>السبب</th><th>الشرح</th></tr>
<tr><td>Simultaneous production &amp; consumption</td><td>الخدمة بتتقدم وبتتعاش في نفس اللحظة، فمينفعش تتصنع وتتفحص وتتخزن زي المنتج</td></tr>
<tr><td>High stakes</td><td>الغلطة ممكن تعمل harm خطير أو permanent disability أو death</td></tr>
<tr><td>Co-production</td><td>النتيجة بتعتمد على مقدم الخدمة <b>والمريض</b>: communication، adherence، patient participation، psychological factors</td></tr></table></div>

<div class="card"><h4>3. Historical development</h4>
<table><tr><th>الشخص</th><th>إسهامه</th></tr>
<tr><td>Florence Nightingale (1850s)</td><td>استخدمت <b>statistical data</b> لتحسين الرعاية، ووضحت أهمية الـ sanitation والـ infection control في تقليل الوفيات في <b>Crimean War</b></td></tr>
<tr><td>Ernest Codman (early 1900s)</td><td>عمل الـ <b>End Result System</b>: تتبع نتايج المرضى بعد الجراحة لتحديد أسباب فشل العلاج</td></tr></table>
<p class="key">الجودة اتطورت من <b>inspection and error detection</b> لـ <b>continuous system improvement</b>.</p></div>

<div class="card"><h4>4. The six IOM domains</h4>
<table><tr><th>Domain</th><th>المعنى والأمثلة</th></tr>
<tr><td>1. Safety</td><td>Avoiding harm to patients during healthcare: منع الـ medication errors والـ falls والـ healthcare-associated infections</td></tr>
<tr><td>2. Effectiveness</td><td>رعاية مبنية على scientific evidence للي هيستفيد، وتجنب الرعاية الغير لازمة. <b>Avoid both underuse and overuse</b></td></tr>
<tr><td>3. Patient-centeredness</td><td>احترام preferences و needs و values و individual circumstances للمريض</td></tr>
<tr><td>4. Timeliness</td><td>تقليل الانتظار الغير لازم والـ harmful delays في التشخيص أو العلاج</td></tr>
<tr><td>5. Efficiency</td><td>Avoiding waste of equipment, supplies, time, energy, resources</td></tr>
<tr><td>6. Equity</td><td>مفيش فروق غير مناسبة بسبب gender أو ethnicity أو geographic location أو socioeconomic status</td></tr></table>
<p class="key">Memory trick في الكتاب: <b>S–E–P–T–E–E</b> = Safety → Effectiveness → Patient-centeredness → Timeliness → Efficiency → Equity.</p></div>

<div class="card"><h4>5. Quality is context-dependent</h4>
<p>الجودة <b>مش</b> إنك تمتلك أحدث أجهزة. المهم تقدّم أفضل evidence-based care في حدود الـ resources والـ population والـ scope بتاعك. مثال: <b>rural clinic</b> و tertiary university hospital ممكن الاتنين يقدموا quality care لو بيلبوا احتياجات مرضاهم.</p></div>

<div class="card"><h4>6. Two components of healthcare delivery</h4>
<table><tr><th>Component</th><th>بيركز على</th><th>أمثلة</th></tr>
<tr><td>Technical</td><td>الجانب الـ clinical/scientific: <b>What</b> care is provided</td><td>Accurate diagnosis، <b>evidence-based care</b>، clinical expertise</td></tr>
<tr><td>Interpersonal</td><td>العلاقة بين مقدم الخدمة والمريض: <b>How</b> care is provided</td><td>Respect، empathy، clear communication، shared decision-making</td></tr></table></div>

<div class="card"><h4>7. Main aims of healthcare quality</h4>
<ol><li><b>Save lives and prevent harm</b>: تقليل الأخطاء والعدوى والـ medication errors، وsafety checks في الروتين</li>
<li><b>Improve patient outcomes</b>: evidence-based care، recovery أحسن، readmissions أقل</li>
<li><b>Build trust and patient satisfaction</b></li>
<li><b>Reduce costs and waste</b>: منع المضاعفات والتحاليل الغير لازمة</li>
<li><b>Improve staff well-being</b>: أنظمة واضحة بتقلل الـ stress والـ confusion والـ burnout</li>
<li><b>Maintain standards and accreditation</b></li></ol></div>

<div class="card"><h4>8. WHO definition</h4>
<p>الرعاية الجيدة لازم تحسّن الـ desired health outcomes وتكون: <b>Safe, Effective, Timely, Efficient, Equitable, People-centered</b>. مفاهيم الـ WHO والـ IOM <b>متشابهة جدًا</b> (الـ WHO بيقول <b>people</b>-centered والـ IOM بيقول <b>patient</b>-centered).</p></div>

<div class="card"><h4>9. Importance of quality</h4>
<table><tr><th>For patients</th><th>For organizations</th></tr>
<tr><td>Harm reduction (errors، adverse drug events، HAIs)<br>Better clinical outcomes<br>Dignity &amp; respect (privacy, values, culture)<br>Clear communication (diagnosis, prognosis, treatment options)</td>
<td>Cost reduction<br>Operational efficiency<br>Reputation &amp; accreditation<br>Risk reduction (errors و legal risk)<br>Staff engagement (satisfaction و retention)</td></tr></table></div>

<div class="card"><h4>10. Quality Assurance vs Quality Improvement (High-yield)</h4>
<table><tr><th>Quality Assurance (QA)</th><th>Quality Improvement (QI)</th></tr>
<tr><td>Mainly <b>retrospective</b></td><td>Mainly <b>proactive</b></td></tr>
<tr><td>Checks whether standards are met</td><td>Improves processes and outcomes</td></tr>
<tr><td>Focuses on identifying deviations</td><td>Focuses on finding and fixing system problems</td></tr>
<tr><td>Often compliance-oriented</td><td>Continuous improvement-oriented</td></tr>
<tr><td>Examples: <b>chart audits, peer review</b></td><td>Examples: <b>PDSA/QI projects</b></td></tr>
<tr><td>"Did we meet the required standard?"</td><td>"How can we make the system better?"</td></tr></table>
<p><b>مثال medication error</b>: QA تسأل: اتبعنا الـ policy؟ فيه violation؟ / QI تسأل: ليه الـ system سمح بالغلطة؟ نعيد تصميم الـ process إزاي؟</p>
<p class="key">الـ QA والـ QI <b>complementary</b>: الـ QA بيضمن الـ standards، والـ QI بيحسّن باستمرار.</p></div>

<div class="card"><h4>11. From inspection to modern QI</h4>
<table><tr><th>Old: Inspection / QA</th><th>Modern: Continuous QI</th></tr>
<tr><td>Retrospective، بيدور على الأخطاء بعد ما تحصل، وعلى <b>مين</b> غلط، فبيعمل <b>punitive culture</b> والستاف بيخبّي الأخطاء</td>
<td>Proactive، بيحسّن الـ systems والـ processes، بيستخدم الـ data، بيتعلم من الأخطاء، وبيشجع <b>Just Culture</b> و psychological safety</td></tr>
<tr><td>Find the error → find the person responsible</td><td>Find the system problem → redesign the process → prevent recurrence</td></tr></table></div>

<div class="card"><h4>12–14. Systems approach &amp; human factors</h4>
<ul><li><b>Systems approach</b>: الأخطاء بتطلع من التفاعل بين <b>people, processes, technology, environment, organizational systems</b>. فالتحسين ميركزش على الفرد بس.<br>مثال: بدل ما تعيد تدريب الممرضة بعد medication error: standardize labeling، <b>barcode medication administration</b>، تحسين التخزين، redesign workflow.<br><b>Key concept</b>: Design safer systems rather than relying only on human vigilance.</li>
<li><b>Human factors engineering</b>: تصميم الأنظمة والأدوات حسب ما الناس بتشتغل فعلًا، خصوصًا تحت stress و fatigue و interruptions و time pressure. البشر بيغلطوا، فالنظام لازم يقلل فرصة الغلط.</li>
<li><b>Case: CLABSI</b> (central line-associated bloodstream infections) قلّت بـ standardized insertion checklist و maintenance protocols و consistent monitoring. الدرس: التحسين جه من standardizing و redesigning الـ system مش من لوم الأفراد.</li></ul></div>
"""

CH1_Q = [
 ("Definition & manufacturing vs healthcare", [
  ("The IOM defines healthcare quality as the degree to which health services:", ["Increase the likelihood of desired health outcomes and are consistent with current professional knowledge", "Generate maximum profit for the hospital", "Treat the largest number of patients", "Use the most advanced technology"], "imp", ""),
  ("Healthcare quality in simple terms means:", ["Doing the right thing, at the right time, for the right patient, in the best possible way", "Treating as many patients as possible", "Using the most expensive equipment", "Avoiding all complaints"], "imp", "جه في الميد."),
  ("Quality in general is the degree to which a product or service:", ["Meets or exceeds customer expectations and is free from deficiencies", "Is the cheapest available", "Is produced the fastest", "Uses imported materials"], "", ""),
  ("Healthcare services cannot be produced, inspected and stored like products because of:", ["Simultaneous production and consumption", "Co-production", "Equity", "Accreditation"], "imp", ""),
  ("Healthcare outcomes depending on both the provider and the patient (adherence, participation) is called:", ["Co-production", "High stakes", "Simultaneous consumption", "Efficiency"], "imp", ""),
  ("Which is NOT a reason healthcare quality is more complex than manufacturing quality?", ["Products can be stored before use", "Simultaneous production and consumption", "High stakes", "Co-production"], "", ""),
 ]),
 ("History & IOM domains", [
  ("Florence Nightingale improved healthcare in the 1850s by:", ["Using statistical data and emphasizing sanitation and infection control", "Developing the End Result System", "Creating ISO 9001", "Developing the PDCA cycle"], "imp", ""),
  ("Ernest Codman (early 1900s) developed the:", ["End Result System", "PDCA cycle", "Donabedian model", "SBAR tool"], "imp", ""),
  ("Codman's End Result System focused on:", ["Tracking patient outcomes after surgery", "Hospital sanitation", "Staff salaries", "Drug pricing"], "", ""),
  ("Healthcare quality evolved from:", ["Inspection and error detection toward continuous system improvement", "Continuous improvement toward inspection", "Patient-centered care toward blame", "Accreditation toward inspection"], "", ""),
  ("How many domains of quality does the IOM define?", ["6", "4", "5", "7"], "imp", "جه في الميد."),
  ("The book's memory trick for the IOM domains is:", ["S-E-P-T-E-E", "S-B-A-R", "P-D-C-A", "F-S-N-P-A"], "", ""),
  ("'Avoiding injuries to patients from the care that is intended to help them' describes:", ["Safety", "Efficiency", "Equity", "Timeliness"], "imp", "جه في الميد."),
  ("'Avoiding waste of equipment, supplies, ideas and energy' describes:", ["Efficiency", "Effectiveness", "Equity", "Patient-centeredness"], "imp", "جه في الميد."),
  ("Avoiding both underuse and overuse of healthcare is the key concept of:", ["Effectiveness", "Efficiency", "Equity", "Safety"], "imp", ""),
  ("Providing care without differences based on gender, ethnicity, location or socioeconomic status is:", ["Equity", "Efficiency", "Timeliness", "Safety"], "", ""),
  ("Reducing unnecessary waiting and harmful delays is:", ["Timeliness", "Effectiveness", "Equity", "Efficiency"], "", ""),
  ("Care that respects patient preferences, needs and values is:", ["Patient-centered", "Efficient", "Timely", "Equitable"], "", ""),
  ("Preventing falls and healthcare-associated infections are examples of:", ["Safety", "Equity", "Timeliness", "Efficiency"], "", ""),
  ("Which is NOT an IOM domain?", ["Profitability", "Safety", "Timeliness", "Equity"], "", ""),
 ]),
 ("Context, components & aims", [
  ("Quality is context-dependent, meaning:", ["Appropriate evidence-based care within the clinical context, not simply having the most technology", "Only tertiary hospitals can provide quality care", "Rural clinics cannot provide quality care", "Quality equals advanced equipment"], "imp", ""),
  ("Which is part of the Technical component of healthcare delivery?", ["Evidence-based care", "Respect & empathy", "Clear communication", "Shared decision-making"], "imp", "جه في الميد."),
  ("The technical component describes:", ["What care is provided", "How care is provided", "Where care is provided", "Who pays for care"], "imp", ""),
  ("The interpersonal component describes:", ["How care is provided", "What care is provided", "The cost of care", "The equipment used"], "imp", ""),
  ("Shared decision-making belongs to the:", ["Interpersonal component", "Technical component", "Financial component", "Structural component"], "", ""),
  ("Clear systems and procedures reducing stress, confusion and burnout reflect the aim of:", ["Improving staff well-being", "Reducing costs", "Building patient trust", "Maintaining accreditation"], "", ""),
  ("The WHO describes quality care as safe, effective, timely, efficient, equitable and:", ["People-centered", "Profitable", "Technology-driven", "Physician-centered"], "", ""),
  ("Regarding the WHO and IOM concepts of quality:", ["They are highly similar", "They are completely different", "WHO ignores safety", "IOM ignores equity"], "", ""),
  ("For healthcare organizations, quality helps achieve all EXCEPT:", ["Increased repeat testing", "Cost reduction", "Risk reduction", "Staff engagement"], "", ""),
 ]),
 ("QA vs QI & systems approach", [
  ("Quality Assurance is mainly:", ["Retrospective and compliance-oriented", "Proactive and improvement-oriented", "Focused on redesigning systems", "Based on PDSA projects"], "imp", ""),
  ("Quality Improvement is mainly:", ["Proactive and focused on fixing system problems", "Retrospective", "Focused on identifying deviations only", "Punitive"], "imp", ""),
  ("Chart audits and peer review are examples of:", ["Quality Assurance", "Quality Improvement", "Human factors engineering", "Accreditation"], "imp", ""),
  ("PDSA projects are examples of:", ["Quality Improvement", "Quality Assurance", "Inspection", "Peer review"], "", ""),
  ("'Did we meet the required standard?' is the question of:", ["QA", "QI", "PDCA", "Human factors"], "imp", ""),
  ("'How can we make the system better?' is the question of:", ["QI", "QA", "Inspection", "Audit"], "imp", ""),
  ("'Why did the system allow the medication error to occur?' is a:", ["QI approach", "QA approach", "Punitive approach", "Legal approach"], "", ""),
  ("The relationship between QA and QI is:", ["Complementary", "Contradictory", "Identical", "Unrelated"], "", ""),
  ("The old inspection approach is characterized by:", ["Finding the person responsible, creating a punitive culture", "Promoting Just Culture", "Redesigning processes", "Learning from errors"], "imp", ""),
  ("Modern continuous quality improvement promotes:", ["Just Culture and psychological safety", "Blame and punishment", "Hiding errors", "Retrospective inspection only"], "", ""),
  ("A systems approach recognizes that errors arise from interactions between:", ["People, processes, technology, environment and organizational systems", "Patients only", "Individual nurses only", "Equipment only"], "imp", ""),
  ("After a medication error, a systems approach would prefer:", ["Barcode medication administration and standardized labeling", "Only retraining the nurse", "Firing the nurse", "Ignoring the error"], "", ""),
  ("'Design safer systems rather than relying only on human vigilance' is the key concept of:", ["Systems approach", "Quality assurance", "Inspection", "Peer review"], "", ""),
  ("Designing systems according to how people actually work under stress and fatigue is:", ["Human factors engineering", "Quality control", "Accreditation", "Benchmarking"], "imp", ""),
  ("In the CLABSI case example, improvement came mainly from:", ["Standardizing and redesigning the system", "Blaming individual staff", "Buying new equipment only", "Reducing staff"], "", ""),
 ]),
]

CH3_SUM = """
<div class="card"><h4>ليه محتاجين quality frameworks؟</h4>
<ul><li>التحسين لازم يبقى <b>systematic</b> مش بالـ intuition. الـ frameworks بتقدم طريقة لـ assessing → identifying → implementing → evaluating → sustaining.</li>
<li>من غيرها التحسين بيبقى haphazard و unsustainable و صعب يتقاس.</li>
<li>بتدي <b>common language</b>، وتحسن الـ communication بين التخصصات، وتساعد في القياس والـ accountability والـ organizational learning.</li></ul>
<table><tr><th>الفترة</th><th>الـ focus</th></tr>
<tr><td>Early 20th century</td><td>Inspection &amp; error detection (والأخطاء مسؤولية الفرد)</td></tr>
<tr><td>1940s–1960s</td><td>Management responsibility &amp; prevention: <b>Deming</b> و <b>Juran</b> (prevention بدل inspection، statistics). Deming في <b>اليابان</b> بعد الحرب العالمية التانية</td></tr>
<tr><td>1960s–1970s</td><td><b>Donabedian</b>: Structure → Process → Outcome</td></tr>
<tr><td>1980s–1990s</td><td>TQM و continuous improvement و <b>PDCA</b>، والـ ISO 9000 اتطبق في الـ healthcare</td></tr>
<tr><td>2000s–present</td><td>Holistic: patient-centered، culture، leadership، technology، <b>EFQM Excellence Model</b></td></tr></table>
<p><b>ليه فيه frameworks كتير؟</b> كل واحد بيجاوب سؤال: EFQM للـ strategic organizational assessment، Donabedian للـ quality assessment، PDCA للـ implementation والـ testing. وهم <b>complementary</b> مش متنافسين.</p>
<p><b>Core concepts</b> مشتركة: systems thinking، data-driven decisions، continuous improvement، patient-centeredness، leadership engagement، staff involvement.</p></div>

<div class="card"><h4>The Donabedian Model</h4>
<p>اتعمل على إيد <b>Avedis Donabedian</b> في الـ <b>1960s</b>. قبله الـ assessment كان بالـ professional judgment والـ peer review (subjective و inconsistent)، وهو عمل طريقة <b>systematic and reproducible</b>.</p>
<table><tr><th>العنصر</th><th>التعريف</th><th>أمثلة</th></tr>
<tr><td>Structure</td><td>خصائص المكان اللي الرعاية بتتقدم فيه: <b>What does the organization have?</b></td><td>Physical facilities، equipment &amp; technology (CT، EHR)، human resources (staff-to-patient ratio، qualifications)، organizational characteristics (governance، policies، accreditation status، culture)، financial resources</td></tr>
<tr><td>Process</td><td>الأنشطة اللي بتكوّن تقديم الرعاية: <b>What do providers actually do?</b></td><td>Clinical (diagnosis، medication administration)، Coordination (transitions، discharge planning)، Management (documentation، incident reporting)</td></tr>
<tr><td>Outcome</td><td>تأثير الرعاية على صحة المرضى والمجتمع: <b>What happened to the patient?</b></td><td>Clinical (mortality، complications، functional status)، patient experience (satisfaction)، population (disparities)، resource-use (LOS، readmission، cost)</td></tr></table>
<p><b>أمثلة structure measures</b>: ICU فيه 1:1 nurse-to-patient؟ 24-hour physician coverage؟ stroke unit؟ simulation center؟<br>
<b>أمثلة process measures</b>: antibiotic خلال ساعة من تشخيص الـ sepsis؟ VTE risk assessment؟ WHO Surgical Safety Checklist قبل الـ incision؟ medication reconciliation؟<br>
<b>أمثلة outcome measures</b>: 30-day readmission للـ heart failure، SSI rate، pressure-ulcer rate، functional status بعد stroke.</p>
<p class="key"><b>Causal relationship</b>: Structure → Process → Outcome. ومفيد في الـ <b>root-cause analysis</b>: تبدأ من الـ outcome وترجع لورا.<br>مثال: structure (1 nurse : 8 patients) → process (vital signs متقاستش وعلامات الإنذار فاتت) → outcome (preventable cardiac arrest).<br>مثال تاني: مفيش barcode system → ممرضة إدت جرعة غلط بسبب look-alike packaging → adverse drug event.</p>
<table><tr><th>Strengths</th><th>Limitations</th></tr>
<tr><td>Simple، intuitive، systematic &amp; reproducible، بيربط S-P-O، مفيد في الـ root-cause analysis، بيتطبق على مستويات كتير</td>
<td>ممكن يبسّط الأنظمة المعقدة (linear causality)<br><b>Good structure ≠ good process</b><br>الـ outcomes بتتأثر بعوامل برا (social determinants، genetics)<br>مش بيغطي الـ patient-centeredness كلها<br>هو <b>assessment framework</b> بس، مش بيقول تعمل التدخل إزاي<br>الـ culture والـ leadership ممكن يبقوا underrepresented</td></tr></table>
<p><b>Application formula</b>: Identify the problem → Assess Structure → Assess Process → Assess Outcome → Analyze the relationships → Design improvement. (مثال AMI: ECG خلال 10 دقايق، aspirin خلال 30 دقيقة، door-to-balloon أقل من 90 دقيقة.)</p></div>

<div class="card"><h4>The PDCA Cycle</h4>
<p>نموذج <b>iterative</b> من 4 خطوات للـ continuous improvement، مرتبط بـ <b>W. Edwards Deming</b> ومبني على شغل <b>Walter Shewhart</b>. أسماؤه: <b>Deming Cycle، Shewhart Cycle، Deming Wheel</b>. بيعكس منطق الـ scientific method.</p>
<table><tr><th>الخطوة</th><th>اللي بيحصل</th></tr>
<tr><td>Plan</td><td>حدد المشكلة والهدف والـ root causes والتغيير اللي هتجربه وإزاي هتقيس النجاح. أدوات: fishbone، Five Whys، Pareto chart، process mapping، <b>FMEA</b>، brainstorming، affinity diagrams</td></tr>
<tr><td>Do</td><td>نفّذ التغيير <b>على نطاق صغير (pilot)</b> عشان تقلل الـ risk وتتعلم وتكتشف المشاكل قبل التعميم، واجمع data</td></tr>
<tr><td>Check</td><td>حلل الـ data وقارن الـ baseline بالـ post-intervention، وشوف الأهداف اتحققت؟ وفيه unintended consequences؟ أدوات: run charts، control charts، SPC</td></tr>
<tr><td>Act</td><td>لو نجح: standardize و scale up. لو نجح جزئيًا: modify و repeat. لو فشل: reconsider وابدأ cycle جديدة</td></tr></table>
<p><b>مثال falls</b>: أغلب الوقعات في unassisted nighttime toilet trips → bundle (risk assessment، purple non-slip socks، bed alarms، hourly rounding) → pilot على جناحين 6 أسابيع → الوقعات قلت 45% → standardized hospital-wide.<br>
<b>مثال SSI</b>: من 6% والهدف 2% في 6 شهور → bundle (chlorhexidine bathing، antibiotic timing، normothermia، glucose control) → وصلت 2.5% → اتعممت.</p>
<table><tr><th>PDCA</th><th>PDSA</th></tr>
<tr><td><b>Check</b>: هل التغيير نجح؟ (more evaluation-oriented)</td><td><b>Study</b>: نجح ليه وفي أنهي ظروف؟ (deeper learning)</td></tr></table>
<p><b>Rapid-cycle improvement</b>: كذا cycle قصيرة ورا بعض: <b>Test → Learn → Modify → Retest → Scale</b> (مثال: أوقات انتظار الطوارئ أسبوع ورا أسبوع).</p>
<table><tr><th>Strengths</th><th>Limitations</th></tr>
<tr><td>Simple، accessible لكل المستويات، clinical و administrative، rapid-cycle، risk-reducing (pilot)، data-driven، بيتعلم من الفشل</td><td>ممكن يبقى simple زيادة على المشاكل المعقدة، محتاج data كتير، ممكن ميعالجش الـ systemic problems، ممكن يبقى bureaucratic، محتاج engagement مستمر</td></tr></table></div>

<div class="card"><h4>Donabedian vs PDCA</h4>
<table><tr><th></th><th>Donabedian</th><th>PDCA</th></tr>
<tr><td>Purpose</td><td><b>Assess</b> quality</td><td><b>Improve</b> processes</td></tr>
<tr><td>Type</td><td>Assessment framework</td><td>Improvement framework</td></tr>
<tr><td>Main question</td><td>"Where is the quality problem?"</td><td>"How can we test and improve a change?"</td></tr>
<tr><td>Time</td><td>Assessment at a point in time</td><td>Continuous and iterative</td></tr>
<tr><td>Typical use</td><td>Measurement و root-cause analysis</td><td>QI projects</td></tr>
<tr><td>Output</td><td>Identification of quality gaps</td><td>Tested and refined interventions</td></tr></table>
<p class="key">Donabedian بيقولك <b>فين وإزاي</b> المشكلة بتحصل، والـ PDCA بيساعدك <b>تجرب وتطبق</b> الحل. الاتنين complementary.</p></div>
"""

CH3_Q = [
 ("Frameworks & history", [
  ("Quality frameworks are needed because quality improvement requires:", ["Systematic approaches rather than intuition", "Intuition and anecdotes", "Punishment of individuals", "Only new equipment"], "", ""),
  ("Quality pioneers who emphasized prevention rather than inspection in the mid-20th century were:", ["Deming and Juran", "Nightingale and Codman", "Donabedian and Tuckman", "Haynes and Berwick"], "imp", ""),
  ("Deming demonstrated systematic quality improvement after World War II in:", ["Japan", "USA", "Germany", "Britain"], "", ""),
  ("The EFQM Excellence Model is mainly used for:", ["Strategic organizational assessment", "Testing small changes", "Bedside handoffs", "Medication reconciliation"], "", ""),
  ("Different quality frameworks are:", ["Complementary rather than competing", "Competing and must not be combined", "Identical", "Obsolete"], "imp", ""),
 ]),
 ("Donabedian model", [
  ("The Donabedian model was developed by Avedis Donabedian in the:", ["1960s", "1850s", "1987", "2000s"], "", ""),
  ("The three components of the Donabedian model are:", ["Structure, Process, Outcome", "Plan, Do, Check", "Input, Process, Output", "Forming, Storming, Norming"], "imp", ""),
  ("Structure refers to:", ["The resources and characteristics of the healthcare setting", "The activities of care delivery", "The effects of care on patients", "Patient satisfaction"], "imp", ""),
  ("Process refers to:", ["The activities involved in delivering healthcare", "The hospital building", "Mortality rates", "The budget"], "imp", ""),
  ("Outcome refers to:", ["The effects of healthcare on patients and populations", "Staff qualifications", "Medication administration", "Policies"], "imp", ""),
  ("Staff-to-patient ratio is a measure of:", ["Structure", "Process", "Outcome", "Equity"], "imp", ""),
  ("Accreditation status of a hospital is a:", ["Structure measure", "Process measure", "Outcome measure", "Balancing measure"], "", ""),
  ("'Was the WHO Surgical Safety Checklist completed before incision?' is a:", ["Process measure", "Structure measure", "Outcome measure", "Population measure"], "imp", ""),
  ("Discharge planning and referral management are:", ["Coordination processes", "Structure measures", "Outcomes", "Financial resources"], "", ""),
  ("30-day readmission rate and length of stay are:", ["Outcome (resource-use) measures", "Structure measures", "Process measures", "Inputs"], "imp", ""),
  ("The causal relationship in the Donabedian model is:", ["Structure → Process → Outcome", "Outcome → Structure → Process", "Process → Structure → Outcome", "There is no relationship"], "imp", ""),
  ("In root-cause analysis using Donabedian, investigators:", ["Work backward from the outcome to process and structure", "Start with the budget", "Ignore structure", "Only look at outcomes"], "", ""),
  ("Inadequate nurse staffing (1:8) leading to missed vital signs and a cardiac arrest illustrates:", ["Structure → Process → Outcome chain", "PDCA cycle", "Tuckman stages", "CUS framework"], "", ""),
  ("A limitation of the Donabedian model is that:", ["Good structure does not guarantee good process", "It is too complex to use", "It cannot be used for root-cause analysis", "It ignores outcomes"], "imp", ""),
  ("The Donabedian model is primarily a/an:", ["Assessment framework", "Improvement framework", "Communication tool", "Accreditation body"], "imp", ""),
  ("Outcomes may be affected by factors outside the healthcare system such as:", ["Social determinants of health and genetics", "Staff ratios", "Policies", "Equipment"], "", ""),
 ]),
 ("PDCA", [
  ("PDCA stands for:", ["Plan, Do, Check, Act", "Plan, Design, Correct, Approve", "Prepare, Deliver, Control, Assess", "Process, Data, Check, Audit"], "imp", ""),
  ("PDCA is also known as all EXCEPT:", ["Donabedian Cycle", "Deming Cycle", "Shewhart Cycle", "Deming Wheel"], "imp", ""),
  ("The underlying concepts of PDCA were developed from the earlier work of:", ["Walter Shewhart", "Florence Nightingale", "Bruce Tuckman", "Ernest Codman"], "", ""),
  ("Fishbone diagram, Five Whys and FMEA are tools mainly used in the:", ["Plan phase", "Do phase", "Check phase", "Act phase"], "imp", ""),
  ("Implementing the change on a small scale (pilot) happens in the:", ["Do phase", "Plan phase", "Check phase", "Act phase"], "imp", ""),
  ("Starting with a pilot is preferred because it:", ["Reduces risk and allows learning before scaling up", "Is more expensive", "Avoids data collection", "Guarantees success"], "", ""),
  ("Comparing baseline and post-intervention results happens in the:", ["Check phase", "Do phase", "Plan phase", "Act phase"], "", ""),
  ("Run charts and control charts are tools of the:", ["Check phase", "Plan phase", "Act phase", "Do phase"], "", ""),
  ("Standardizing and scaling up a successful intervention happens in the:", ["Act phase", "Check phase", "Do phase", "Plan phase"], "imp", ""),
  ("PDSA differs from PDCA because 'Study' emphasizes:", ["Understanding why and under what conditions a change works", "Skipping evaluation", "Punishing staff", "Buying equipment"], "imp", ""),
  ("Rapid-cycle improvement follows:", ["Test → Learn → Modify → Retest → Scale", "Plan → Wait → Inspect", "Structure → Process → Outcome", "Forming → Storming → Norming"], "", ""),
  ("A limitation of PDCA is that it may:", ["Be too simple for highly complex problems", "Be impossible to understand", "Not use data", "Not allow pilot testing"], "", ""),
  ("The main distinction: Donabedian is for …… while PDCA is for ……", ["Assessment of quality; improvement of quality", "Improvement; assessment", "Accreditation; certification", "Teamwork; leadership"], "imp", ""),
  ("'Where is the quality problem?' is the main question of:", ["Donabedian model", "PDCA cycle", "SBAR", "CUS"], "", ""),
 ]),
]

CH4_SUM = """
<div class="card"><h4>من الكتاب: Chapter 4 — The Power of Teamwork</h4>
<p class="hint">الملخص اللي فوق من سلايدات المحاضرة، والجزء ده من الكتاب ومكمّل ليه.</p>
<ul><li>محدش لوحده عنده كل المعرفة. التيم بيدي رعاية comprehensive و coordinated و safe. والـ <b>communication failures</b> سبب مهم للـ adverse events: المعلومة بتتنسي أو تتفهم غلط أو تتأخر أو تروح للشخص الغلط.</li>
<li><b>Haynes et al. (2009)</b>: الـ <b>WHO Surgical Safety Checklist</b> في <b>8 مستشفيات</b> قلل المضاعفات والوفيات. الـ checklist <b>مجابتش clinical knowledge جديدة</b>، قوتها إنها نظّمت الـ communication.</li></ul></div>

<div class="card"><h4>The five characteristics of effective teams (TeamSTEPPS)</h4>
<table><tr><th>Characteristic</th><th>المعنى والمثال</th></tr>
<tr><td>1. Team leadership</td><td>Leader واضح بيوزع المهام ويقرر ويراقب. مثال: <b>Code Blue</b>: واحد compressions، واحد airway، واحد medications، واحد documentation</td></tr>
<tr><td>2. Mutual support</td><td>تتوقع احتياج زميلك وتساعده: <b>safety net</b>. مثال: الـ scrub nurse بتدي الجراح الأداة قبل ما يطلبها</td></tr>
<tr><td>3. Situation monitoring</td><td>مراقبة مستمرة للمريض والبيئة وأداء التيم، وده بيعمل <b>shared mental model</b> (فهم مشترك: إيه اللي بيحصل، إيه الخطوة الجاية، مين مسؤول، إيه الـ risks)</td></tr>
<tr><td>4. Communication</td><td>Clear، concise، accurate، timely، structured. أشهر أداة <b>SBAR</b></td></tr>
<tr><td>5. Closed-loop communication</td><td>المستقبل بيعيد الرسالة يأكد فهمها. "Give 4 mg morphine IV" ← "Confirming, 4 mg morphine IV"<br><b>Sender → Message → Receiver → Repeat/Confirm → Action</b></td></tr></table>
<p><b>مثال SBAR (الساعة 2 بالليل)</b>: S: Mr. Ahmed bed 4 HR 130 · B: post-op day 1 hip replacement · A: I'm concerned about bleeding · R: please come and assess him now. أحسن بكتير من "Doctor, he doesn't look good".</p></div>

<div class="card"><h4>Tuckman model — stages of team development</h4>
<table><tr><th>Stage</th><th>Main characteristic</th><th>Leader's role</th></tr>
<tr><td>1. Forming</td><td>Uncertainty، dependence on leader، polite، أسئلة كتير</td><td><b>Provide structure</b>: roles، ground rules، objectives</td></tr>
<tr><td>2. Storming</td><td>Conflict و disagreement و competition for influence</td><td><b>Manage conflict</b> بشكل constructive ويفكّر بالهدف المشترك</td></tr>
<tr><td>3. Norming</td><td>Trust، shared norms، team identity</td><td><b>Build cohesion</b>: consensus، celebrate small wins</td></tr>
<tr><td>4. Performing</td><td>High performance، autonomy، shared decision-making</td><td><b>Delegate and support</b>، remove barriers</td></tr>
<tr><td>5. Adjourning</td><td>Completion، accomplishment أو sense of loss</td><td><b>Debrief</b> و transfer knowledge</td></tr></table>
<p class="key">F → S → N → P → A. مثال الكتاب: <b>COVID-19 ICU teams</b> (redeployed staff): الـ daily huddles والـ written protocols والـ bedside mentoring ساعدوهم يوصلوا Performing أسرع.</p></div>

<div class="card"><h4>Barriers to effective teamwork</h4>
<table><tr><th>Barrier</th><th>Consequence</th></tr>
<tr><td>Hierarchical culture</td><td>الـ junior بيتردد يتكلم، فالـ concerns متتقالش والأخطاء تكمل</td></tr>
<tr><td>Poor handovers</td><td>Medication errors، missed diagnoses، repeated tests</td></tr>
<tr><td>Lack of shared mental models</td><td>Fragmented care، contradictory instructions</td></tr>
<tr><td>Physical environment</td><td>Separate workstations، noisy corridors، فالتواصل بيتأخر</td></tr>
<tr><td>High workload &amp; fatigue</td><td>Shortcuts، irritability، poor monitoring</td></tr>
<tr><td>Professional silos</td><td>كل مهنة بمصطلحاتها وثقافتها، فبيحصل conflict و duplication</td></tr></table>
<p><b>CUS framework</b> لكسر الـ hierarchy (طريقة متدرجة لرفع الـ concern):</p>
<ul class="ltr"><li><b>C</b> — "I am <b>Concerned</b>"</li><li><b>U</b> — "I am <b>Uncomfortable</b>"</li><li><b>S</b> — "This is a <b>Safety issue</b>" (لازم reassessment فوري)</li></ul>
<p class="key">Patient safety should take priority over professional hierarchy.</p></div>

<div class="card"><h4>Structured communication tools</h4>
<table><tr><th>Tool</th><th>الاستخدام</th></tr>
<tr><td>SBAR</td><td>Urgent calls، physician communication، handovers، transfer reports</td></tr>
<tr><td>Call-out</td><td>إعلان معلومة حرجة بصوت عالي للتيم كله (cardiac arrest، trauma)</td></tr>
<tr><td>Check-back</td><td>نوع من الـ closed-loop: المستقبل يعيد الأمر (medication orders، critical results)</td></tr>
<tr><td>I-PASS (handoff)</td><td><b>I</b>llness severity · <b>P</b>atient summary · <b>A</b>ction list · <b>S</b>ituational awareness &amp; contingency planning · <b>S</b>ynthesis by receiver</td></tr>
<tr><td>Huddle</td><td>اجتماع قصير لعمل أو إعادة الـ shared mental model (تغير مفاجئ، procedure معقد)</td></tr>
<tr><td>Debrief</td><td>نقاش منظم بعد الحدث: إيه اللي مشي كويس، وإيه اللي لأ، ونغير إيه</td></tr></table>
<p><b>Case: Rapid Response Team</b> (مستشفى 300 سرير): كل الـ RRT calls بقت بالـ SBAR + <b>30-second huddle</b> عند الوصول. في 12 شهر: cardiac arrests برا الـ ICU قلت <b>30%</b> والـ unplanned ICU transfers قلت، وبتكلفة قليلة لأنه تغيير في الـ communication مش أجهزة.</p></div>

<div class="card"><h4>Culture, leadership, measurement &amp; technology</h4>
<ul><li><b>Culture</b>: psychological safety، <b>interprofessional education</b> (التدريب سوا)، protected time للـ huddles والـ debriefs، data &amp; feedback (dashboards)، recognition لنجاح التيم مش الفرد بس.</li>
<li><b>Leaders</b>: يحضروا الـ huddles، يسألوا الـ juniors، يعترفوا بالـ uncertainty والأخطاء. Leadership behavior establishes the culture.</li>
<li><b>Measuring teamwork</b>: <b>T-TAQ</b> (TeamSTEPPS Teamwork Attitudes Questionnaire)، observational checklists في الـ simulation و mock codes، clinical outcome indicators (time to antibiotic، door-to-balloon، handover errors)، staff outcomes (turnover، burnout، absenteeism).</li>
<li><b>Technology</b>: secure messaging، EHR فيها SBAR templates، tele-ICU، simulation &amp; VR. بس technology لوحدها مش بتعمل teamwork، وممكن تبقى distraction. <b>Technology should support teamwork, not replace it</b>.</li></ul></div>
"""

CH4_Q = [
 ("Book: characteristics & communication", [
  ("The landmark study by Haynes et al. (2009) evaluated:", ["The WHO Surgical Safety Checklist", "The PDCA cycle", "ISO 9001", "The Tuckman model"], "imp", ""),
  ("The main strength of the WHO Surgical Safety Checklist was that it:", ["Structured communication among the team", "Introduced new clinical knowledge", "Replaced surgeons", "Reduced staff numbers"], "imp", ""),
  ("The five characteristics of effective teams include all EXCEPT:", ["Strict hierarchy", "Team leadership", "Mutual support", "Situation monitoring"], "imp", ""),
  ("A scrub nurse handing the surgeon an instrument before being asked is an example of:", ["Mutual support", "Call-out", "Storming", "CUS"], "imp", ""),
  ("Assigning roles immediately during a Code Blue reflects:", ["Team leadership", "Adjourning", "Debrief", "Equity"], "", ""),
  ("Situation monitoring contributes to a:", ["Shared mental model", "Professional silo", "Punitive culture", "Hierarchical culture"], "imp", ""),
  ("A common understanding among team members of what is happening and who is responsible is a:", ["Shared mental model", "Closed loop", "Call-out", "Process owner"], "", ""),
  ("'Give 4 mg morphine IV' — 'Confirming, 4 mg morphine IV' is an example of:", ["Closed-loop communication", "Call-out", "SBAR", "CUS"], "imp", ""),
  ("In SBAR, 'I am concerned about possible bleeding' is the:", ["Assessment", "Situation", "Background", "Recommendation"], "imp", ""),
  ("In SBAR, 'He is postoperative day one following hip replacement' is the:", ["Background", "Situation", "Assessment", "Recommendation"], "", ""),
  ("Effective healthcare communication should be all EXCEPT:", ["Ambiguous", "Clear", "Timely", "Structured"], "", ""),
 ]),
 ("Book: Tuckman model", [
  ("The correct order of Tuckman's stages is:", ["Forming, Storming, Norming, Performing, Adjourning", "Storming, Forming, Norming, Performing, Adjourning", "Forming, Norming, Storming, Performing, Adjourning", "Norming, Forming, Storming, Adjourning, Performing"], "imp", ""),
  ("High uncertainty and dependence on the leader characterize:", ["Forming", "Storming", "Norming", "Performing"], "imp", ""),
  ("Conflict and competition for influence characterize:", ["Storming", "Forming", "Norming", "Adjourning"], "imp", ""),
  ("Establishing trust, shared rules and team identity occurs in:", ["Norming", "Storming", "Forming", "Adjourning"], "", ""),
  ("The leader's role in the Performing stage is to:", ["Delegate and support", "Provide structure", "Manage conflict", "Debrief and close"], "imp", ""),
  ("The leader's role in the Forming stage is to:", ["Provide structure, define roles and reduce uncertainty", "Delegate authority", "Conduct a final debrief", "Remove external barriers only"], "", ""),
  ("Conducting a final debrief and preserving knowledge is the leader's role in:", ["Adjourning", "Forming", "Norming", "Storming"], "", ""),
  ("The Tuckman model contains …… stages:", ["5", "4", "3", "6"], "", ""),
 ]),
 ("Book: barriers & tools", [
  ("Junior staff hesitating to raise safety concerns to seniors is the barrier of:", ["Hierarchical culture", "Physical environment", "Professional silos", "High workload"], "imp", ""),
  ("Different disciplines training separately with different terminology and cultures is:", ["Professional silos", "Shared mental model", "Mutual support", "Situation monitoring"], "", ""),
  ("CUS stands for:", ["Concerned, Uncomfortable, Safety issue", "Call, Update, Summarize", "Check, Understand, Support", "Communicate, Unite, Serve"], "imp", ""),
  ("The purpose of the CUS framework is to:", ["Allow any team member to raise safety concerns regardless of rank", "Assign tasks during a code", "Document handoffs", "Measure staff burnout"], "imp", ""),
  ("Announcing critical information aloud to the whole team during a resuscitation is a:", ["Call-out", "Check-back", "Debrief", "Huddle"], "imp", ""),
  ("I-PASS is a structured tool used for:", ["Handoffs", "Billing", "Surgery", "Accreditation"], "imp", ""),
  ("In I-PASS, the last 'S' stands for:", ["Synthesis by receiver", "Situation", "Safety", "Summary of history"], "", ""),
  ("A brief team meeting to establish or re-establish a shared mental model is a:", ["Huddle", "Debrief", "Call-out", "Audit"], "", ""),
  ("A structured discussion after a cardiac arrest about what went well and what to change is a:", ["Debrief", "Huddle", "Check-back", "Call-out"], "", ""),
  ("In the Rapid Response Team case, cardiac arrests outside the ICU decreased by:", ["30%", "5%", "60%", "90%"], "", ""),
  ("The Rapid Response Team case required little investment because it focused on:", ["Changing communication behavior (SBAR + huddle)", "Buying new monitors", "Hiring new doctors", "Building a new ICU"], "", ""),
 ]),
 ("Book: culture, measurement & technology", [
  ("Doctors, nurses, pharmacists and physical therapists training together is:", ["Interprofessional education", "Professional silos", "Peer review", "Adjourning"], "", ""),
  ("The T-TAQ is a tool used to:", ["Measure teamwork attitudes", "Measure blood pressure", "Certify ISO", "Calculate cost"], "imp", ""),
  ("Staff turnover, burnout and absenteeism are used to measure teamwork as:", ["Staff outcomes", "Clinical outcomes", "Structure", "Inputs"], "", ""),
  ("Regarding technology and teamwork:", ["Technology should support teamwork, not replace it", "Technology automatically creates teamwork", "Technology should replace direct communication", "Technology has no limitations"], "imp", ""),
  ("Tele-ICU systems allow:", ["Off-site intensivists to collaborate with bedside teams", "Patients to discharge themselves", "Removal of nurses", "Avoiding EHR use"], "", ""),
 ]),
]

CH2_EXTRA = """
<div class="card"><h4>إضافات من الكتاب (Chapter 2)</h4>
<ul><li><b>ISO facts</b>: Founded <b>1947</b>، headquarters <b>Geneva, Switzerland</b>، official languages <b>English, French, Russian</b>. و<b>ISO is not an acronym</b> (من isos = equal).</li>
<li>الـ ISO <b>voluntary</b> عكس القوانين، بس الـ certification مهمة للـ contracts والـ market opportunities والـ international recognition.</li></ul>
<p><b>Evolution of ISO 9001</b> (اتطور من الـ military والـ industrial standards):</p>
<table><tr><th>السنة</th><th>الـ milestone</th></tr>
<tr><td>1959</td><td>MIL-Q-9858: U.S. military quality program</td></tr>
<tr><td>1960s</td><td>NATO AQAP series</td></tr>
<tr><td>1979</td><td><b>BS 5750</b>: British standard و <b>direct predecessor of ISO 9001</b></td></tr>
<tr><td>1987</td><td>First ISO 9001 edition</td></tr>
<tr><td>2015</td><td>ISO 9001:2015 (current)</td></tr></table>
<p><b>الـ 7 principles بالتفصيل</b>: Customer focus (patient feedback، shared decision-making) · Leadership (commitment، allocate resources) · Engagement of people (reporting near misses، suggestions، recognition) · Process approach (Prescribing → Dispensing → Administration → Monitoring) · Improvement (PDCA/PDSA) · Evidence-based decisions (infection rates، satisfaction data) · <b>Relationship management</b> (suppliers، labs، device &amp; pharma companies، community providers).</p>
<p><b>Silo approach</b> بيعمل communication problems و duplication و inefficiency، والـ process approach بيركز على <b>رحلة المريض كاملة</b>.</p>
<p><b>Benefits of ISO certification (8)</b>: Safety · Efficiency (duplication، waste، <b>bottlenecks</b>) · Credibility &amp; reputation · Documentation &amp; legal support (بس <b>مش ضمان</b> للحماية القانونية ولا إن الأخطاء متحصلش) · Staff satisfaction · Continuous improvement culture · Competitive advantage · Integration with other standards (<b>ISO 14001</b> environmental، <b>ISO 45001</b> occupational health &amp; safety).</p>
<table><tr><th>Challenge</th><th>الشرح / الحل</th></tr>
<tr><td>Cost</td><td>Fees، training، consultants، audits</td></tr>
<tr><td>Compliance culture</td><td>التركيز على الورق بدل التحسين. <b>Certification is a means, not the final goal</b></td></tr>
<tr><td>Complexity &amp; bureaucracy</td><td>الحل: training، expert guidance، <b>phased implementation</b></td></tr>
<tr><td>Staff resistance</td><td>الحل: involve staff early، explain benefits، training، support</td></tr>
<tr><td>Sustainability</td><td>لازم الجودة تبقى جزء من الشغل اليومي</td></tr></table>
<p class="key">Benefits: Safety – Efficiency – Credibility – Documentation – Staff – Improvement – Advantage – Integration<br>Challenges: Cost – Compliance – Complexity – Resistance – Sustainability</p></div>
"""

CH2_Q = ("Book: ISO facts, benefits & challenges", [
  ("ISO was founded in:", ["1947", "1987", "2015", "1959"], "imp", ""),
  ("ISO headquarters is located in:", ["Geneva, Switzerland", "London, UK", "New York, USA", "Paris, France"], "imp", ""),
  ("The official languages of ISO are:", ["English, French and Russian", "English only", "English, Arabic and Chinese", "French and German"], "", ""),
  ("Regarding the name 'ISO':", ["It is not an acronym; it comes from Greek 'isos'", "It is an English acronym", "It comes from Latin", "It means 'standard'"], "", ""),
  ("The direct predecessor of ISO 9001 is:", ["BS 5750 (1979)", "MIL-Q-9858", "NATO AQAP", "ISO 14001"], "imp", ""),
  ("MIL-Q-9858 (1959) was a:", ["U.S. military quality program", "British standard", "NATO publication", "Healthcare accreditation"], "", ""),
  ("ISO 14001 concerns:", ["Environmental management", "Occupational health and safety", "Medical laboratories", "Medical devices"], "", ""),
  ("ISO 45001 concerns:", ["Occupational health and safety", "Environmental management", "Point-of-care testing", "Quality management"], "", ""),
  ("Regarding ISO certification and legal protection:", ["It does not guarantee legal protection or that errors will not occur", "It guarantees full legal protection", "It guarantees zero errors", "It replaces malpractice insurance"], "imp", ""),
  ("A major risk of ISO implementation is a 'compliance culture', meaning:", ["Focusing on paperwork instead of actual quality improvement", "Focusing on patients", "Reducing documentation", "Improving teamwork"], "imp", ""),
  ("'Certification is a means to improve quality, not the final goal' addresses the challenge of:", ["Compliance culture", "Cost", "Staff resistance", "Integration"], "", ""),
  ("The solution to staff resistance to ISO is to:", ["Involve staff early, explain benefits and provide training", "Force changes without explanation", "Punish resisters", "Abandon certification"], "", ""),
  ("Relationship management (principle 7) involves relationships with:", ["Suppliers, laboratories and pharmaceutical companies", "Only patients", "Only top management", "Competitors only"], "", ""),
  ("Which is NOT a challenge of ISO certification?", ["Competitive advantage", "Cost", "Bureaucracy", "Sustainability"], "", "دي من الـ benefits."),
 ])

# ---------------- assemble
_by = {t[0]: list(t) for t in _T}
team, iso = _by['team'], _by['iso']
iso[4] = "صور سلايدات المحاضرة التانية + Chapter 2 من الكتاب"
iso[5] = iso[5] + CH2_EXTRA
iso[6] = iso[6] + [CH2_Q]
team[4] = "سلايدات الـ Teamwork (38 slide) + Chapter 4 من الكتاب"
team[5] = team[5] + CH4_SUM
team[6] = team[6] + CH4_Q
TABS = [
 ("ch1", "Chapter 1 — Understanding Healthcare Quality", "Ch1 مقدمة", "🏥", BOOK + " — Chapter 1", CH1_SUM, CH1_Q),
 tuple(iso[:1]) + ("Chapter 2 — ISO Standards",) + ("Ch2 ISO",) + tuple(iso[3:]),
 ("ch3", "Chapter 3 — Donabedian Model & PDCA Cycle", "Ch3 Frameworks", "🔁", BOOK + " — Chapter 3", CH3_SUM, CH3_Q),
 tuple(team[:1]) + ("Chapter 4 — The Power of Teamwork",) + ("Ch4 Teamwork",) + tuple(team[3:]),
]
TF_DRILL = [t for t in _TF if 'PDCA' not in t[0] and 'Donabedian' not in t[0] and 'Number of staff' not in t[0]] + [
 ("ISO was founded in 1947 and its headquarters is in Geneva.", 0, ""),
 ("BS 5750 is the direct predecessor of ISO 9001.", 0, ""),
 ("ISO certification guarantees legal protection.", 1, "مش ضمان."),
 ("Chart audits and peer review are examples of Quality Improvement.", 1, "دي QA."),
 ("QA is mainly retrospective while QI is mainly proactive.", 0, ""),
 ("Ernest Codman developed the End Result System.", 0, ""),
 ("Florence Nightingale developed the PDCA cycle.", 1, "Deming/Shewhart."),
 ("The technical component describes how care is provided.", 1, "What. والـ interpersonal = How."),
 ("Good structure guarantees good process and outcome.", 1, "Excellent structure ≠ excellent care."),
 ("The Donabedian model is mainly an assessment framework.", 0, ""),
 ("In PDCA, the change is first implemented hospital-wide in the Do phase.", 1, "Small scale pilot."),
 ("PDSA's 'Study' explores why and under what conditions a change works.", 0, ""),
 ("Storming is characterized by conflict and disagreement.", 0, ""),
 ("In the Performing stage, the leader should provide tight structure and reduce uncertainty.", 1, "ده Forming. في Performing: delegate and support."),
 ("Closed-loop communication means the receiver repeats the message to confirm it.", 0, ""),
 ("CUS stands for Concerned, Uncomfortable, Safety issue.", 0, ""),
 ("The WHO Surgical Safety Checklist worked by introducing new clinical knowledge.", 1, "بنظّم الـ communication."),
 ("Technology automatically creates good teamwork.", 1, "Should support, not replace."),
]
