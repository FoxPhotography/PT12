# Therapeutic Exercises II — Lecture data, part 1 (Posture, Maitland/cervical)
# Question tuple: (text, [correct, wrong...], tag, explanation)
# tag: "" | "imp" (doctor stressed / repeated in notes) | "qz" (topic of the doctor's quiz)

LECTURES = []

def L(id, title, short, icon, source, summary, groups):
    LECTURES.append(dict(id=id, title=title, short=short, icon=icon, source=source, summary=summary, groups=groups))

# ================================================================ Posture
L("l1", "Posture — Assessment, Faults & Crossed Syndromes", "Posture", "🧍",
  "سلايدات Posture (د. ياسمين) + تفريغ المحاضرة 1 و 2 + ملخص Hla",
"""
<div class="card"><h4>التعريف والأنواع</h4>
<p class="ltr"><b>Posture</b> is a "position or attitude of the body either with support during muscular inactivity, or by the means of the coordinated action of many muscles working to maintain stability or to form an essential basis which is being adapted constantly to the movement which is superimposed upon it."</p>
<ul class="ltr"><li>Position or attitude of the body.</li><li>Relative arrangement of body parts for a specific activity.</li><li>Characteristic manner of bearing one's body.</li></ul>
<table><tr><th>النوع</th><th>التفاصيل</th></tr>
<tr><td>Inactive posture</td><td>وضع الراحة أو النوم (slouching أو supported). بيُستخدم في تدريب الـ general relaxation، والنشاط العضلي فيه في أقل حاجة.</td></tr>
<tr><td>Active posture</td><td>محتاج integrated activity لعضلات كتير. نوعين: <b>Static</b> (standing, sitting) و <b>Dynamic</b> (walking, running، وحتى القعدة وانت بتكتب).</td></tr></table></div>

<div class="card"><h4>POSTURE acronym</h4>
<table class="ltr"><tr><th>حرف</th><th>المعنى</th></tr>
<tr><td>P</td><td>Pelvis is neutral, with weight distributed (عظمتين الحوض على نفس المستوى)</td></tr>
<tr><td>O</td><td>On the whole foot (no inversion / eversion)</td></tr>
<tr><td>S</td><td>Stable joints (neutral extended joints)</td></tr>
<tr><td>T</td><td>Tight abdominals (flat stomach)</td></tr>
<tr><td>U</td><td>Upright ribs (chest cavity not collapsed)</td></tr>
<tr><td>R</td><td>Retracted midway shoulders (scapula)</td></tr>
<tr><td>E</td><td>Ear same level over shoulder (LOG through external auditory meatus, head neutral)</td></tr></table></div>

<div class="card"><h4>Posture assessment و الـ Plumb line</h4>
<ul><li>مفتاح الـ posture الكويس هو وضع الـ <b>spine</b>: 3 انحناءات طبيعية (رقبة، ضهر من فوق، أسفل الضهر). الصح إنها تفضل موجودة من غير ما تزيد. الراس فوق الكتف، والكتف فوق الحوض.</li>
<li>الـ spine والـ pelvis هما الـ central base: الـ spine بيدي vertical support، والـ pelvis هو الـ foundation اللي بينقل وزن الجسم للرجلين. لو واحد فيهم مش مظبوط هيحصل compensation في الأطراف أو الراس.</li>
<li><b>Plumb line (lateral view)</b>، الـ LOG بيعدي على:
<span class="ltr">lobe of the ear → shoulder joint → hip joint / greater trochanter → <b>slightly anterior</b> to midline of knee → <b>anterior</b> to lateral malleolus.</span></li>
<li>من قدام أو من ورا: الخط بيقسم الجسم نصين متساويين والوزن متوزع بالتساوي على الرجلين.</li>
<li>بنقيّم في 3 views (anterior, lateral, posterior): head alignment، الـ curvatures، مستوى الكتفين، الحوض، hip و knee و ankle.</li>
<li>في الـ correct posture الـ gravity line بيعدي على axes كل المفاصل. كل ما الـ alignment يقرب من محاور المفاصل كل ما الـ gravitational stress على الـ soft tissue يقل.</li></ul></div>

<div class="card"><h4>Curvatures of the spine</h4>
<ul><li><b>Frontal view</b>: مستقيم و symmetrical. الـ <b>Scoliosis</b> بيتشاف من الـ posterior view.</li>
<li><b>Sagittal view</b>: 4 انحناءات. <b>Primary</b> (dorsal و sacral) convex posteriorly، و<b>Secondary</b> (cervical و lumbar) convex anteriorly. الـ Kyphosis والـ lordosis بيتشافوا من الـ lateral view.</li>
<li>الطبيعي: cervical slight lordosis (حوالي 40°)، thoracic slight flexion (minimal kyphosis)، lumbar slight lordosis، sacrum slight posterior.</li></ul></div>

<div class="card"><h4>Good posture</h4>
<p class="ltr"><b>Definition:</b> the attitude assumed by body parts to maintain stability and balance with <b>minimum effort and least strain</b> during supportive and non-supportive positions.</p>
<p><b>Effects (5):</b> بيريّح العضلات (unloaded &amp; relaxed)، بيحسن كفاءة التنفس والدورة الدموية، بيمنع الـ strain والـ fatigue، بيقلل الأمراض الناتجة عن الـ bad posture، وبيحسن الحالة النفسية.</p></div>

<div class="card"><h4>Risk factors و Causes</h4>
<table><tr><th>Risk factors of bad posture</th><th>Common causes of poor posture</th></tr>
<tr><td class="ltr">Misalign MSK system (muscle imbalance → deformity)<br>↑ pressure on spine → injury &amp; degeneration (spondylosis)<br>Neck, shoulder &amp; back pain<br>↓ Flexibility<br>Affect joint movement (proprioceptors)<br>Affect balance &amp; ↑ risk of falling<br>Harder to digest food (sympathetic relation till L2)<br>Harder to breathe (kyphosis = expiration lesion)<br>Women: core imbalance → incontinence / pelvic organ prolapse</td>
<td class="ltr">Muscle tension or weakness<br>Over weight / Extra weight<br>Occupation (غيّر وضعك كل نص ساعة)<br>Pain or past injuries<br>Low nutritional state<br>Hereditary<br>Bad habits<br>Lifestyle &amp; fashion (sedentary، الكعب العالي، الجينز الضيق)</td></tr></table>
<p><b>Aetiology of postural faults (6):</b> gravity، environment (occupation, weather)، architecture of vertebral column والأطراف والأعضاء، pathology، emotional states، pain.</p>
<p><b>Posture &amp; pain:</b> نظريات كتير بتقول إن الـ bad posture عامل مساعد في الـ low back pain، وتحسين الـ posture والـ postural control ليه أثر إيجابي على الألم. والسبب الأساسي للألم هو الـ muscle imbalance.</p></div>

<div class="card"><h4>Postural mechanism و Muscle imbalance</h4>
<ul><li>الـ postural mechanism = تفاعل بين <b>العضلات</b> و <b>الـ nervous control</b>.</li>
<li><b>Anti-gravity muscles</b> بتحافظ على الوقفة. فيها <b>red fibers</b> أكتر، slowly contracting ومش بتتعب بسرعة.</li>
<li><b>Principle of assessment:</b> لو الـ force couple في الـ 3 cardinal planes مش متوازن، الـ segment بيتحرك بعيد عن محوره فيحصل faulty joint motion. الـ head والـ trunk والـ shoulders والـ pelvic girdle هما الأساس اللي القوى بتطلع منه للأطراف.</li>
<li>الـ bad posture بيحصل لما عضلة تبقى <b>tight</b> والـ antagonist بتاعتها <b>elongated</b>.</li>
<li><b>Chronically elongated</b> muscle: بتزود sarcomeres، والـ length-tension curve بيتحرك <b>لليمين</b>. <b>Chronically shortened</b>: بتفقد sarcomeres، والـ curve بيتحرك <b>للشمال</b>.</li>
<li><b>Stretch weakness</b> (Kendall): العضلة الـ elongated بتطلع أقصى قوة وهي متمطوطة، وبتبقى ضعيفة في الوضع الطبيعي. وعشان كده لازم نختبر العضلة في وضعها الوظيفي أو على مدى حركتها.</li></ul></div>

<div class="card"><h4>Upper &amp; Lower Crossed Syndromes ★ كويز</h4>
<table><tr><th></th><th>Tight (short)</th><th>Weak (inhibited)</th></tr>
<tr><td>Upper crossed</td><td class="ltr">Upper trapezius &amp; levator scapulae<br>Pectoralis major &amp; minor (+ SCM)</td><td class="ltr">Deep neck flexors<br>Rhomboids, serratus anterior, middle &amp; lower trapezius</td></tr>
<tr><td>Lower crossed</td><td class="ltr">Thoracolumbar erector spinae<br>Iliopsoas &amp; rectus femoris</td><td class="ltr">Abdominals<br>Gluteals</td></tr></table>
<p>كل syndrome على شكل <b>X</b>: الـ tight بيقابلوا بعض على قطر والـ weak على القطر التاني.</p>
<ul><li>Upper crossed: forward head، round shoulders، increased thoracic kyphosis.</li>
<li>Lower crossed: anterior pelvic tilt و lumbar hyperlordosis. الناس اللي عضلات بطنهم ضعيفة (الحوامل والكرش) بيجيلهم lumbar hyperlordosis.</li></ul>
<p class="key">كويز الدكتورة: <b>Define posture and explain upper and lower cross syndromes in a diagram</b>. ارسم X لكل واحدة واكتب الـ tight على قطر والـ weak على القطر التاني.</p></div>

<div class="card"><h4>Forward head, round shoulder, kyphosis (ملخص Hla)</h4>
<ul><li><b>Forward head</b>: الـ head بيعمل anterior translation، فالـ upper cervical بيدخل في <b>extension lesion</b> (hyperlordosis). Tight: upper trapezius و suboccipitals. Weak: الـ deep neck flexors.
<br>Treatment: chin-in exercises و stretch للـ extensors، وبعدين flexion mobilization.</li>
<li><b>Flattening of cervical spine</b> (flexion lesion): First line extension mobilization، وفي المراحل المتأخرة core stabilization و postural training.</li>
<li><b>Round shoulder</b>: internal rotation و protraction. Pectorals tight. العلاج: stretch للـ internal rotators، تقوية الـ external rotators، والـ retraction (rhomboids و middle/lower trapezius).</li>
<li><b>Kyphosis</b>: flexion lesion. Middle و lower trapezius والـ rhomboids over-stretched (weak)، والعلاج extension mobilization للـ thoracic + inhalation mobilization + sternal release.</li></ul></div>

<div class="card"><h4>Sitting, Gait و Body balance</h4>
<ul><li><b>Active vs passive equilibrium</b>: الأوضاع اللي محتاجة قوة عضلية عشان التوازن = active equilibrium. الـ passive: كل مراكز الثقل جوه الـ gravity line اللي جوه الـ base of support.</li>
<li><b>Faulty sitting</b>: الـ COG بيروح ورا الـ ischium، فيزيد الـ lumbar kyphosis، ويزيد الـ IVD pressure، ومع الوقت minor stress يعمل disc prolapse. كمان strain على الـ posterior ligament و muscle fatigue.
<br>ضغط الـ disc في القعدة أعلى من الوقوف. بيقل بـ arm rests و back support يحافظ على الـ lumbar lordosis، وإن ضهر الكرسي يميل 90°–100°.</li>
<li><b>Relaxed sitting</b>: الـ head erect و الـ COG بتاعها slightly anterior للـ atlanto-occipital joint، والوزن على الـ ischial tuberosities.</li>
<li><b>Gait clues</b>: لو القدم مش قادرة تعمل heel strike يبقى heel spur أو bursitis أو blister. لو الركبة مش بتفرد في الـ heel strike يبقى weak quadriceps أو flexion fusion. Heel strike مؤلم مع knee hyperextension يبقى weak hamstrings.</li>
<li><b>Unilateral spinal pain</b>: في الـ mild/moderate الجذع بيميل <b>ناحية</b> الجنب المصاب (muscle splinting). في الـ disc أو SI lesions الشديدة بيميل <b>بعيد</b> عنه. Mid/bilateral pain: مشية guarded و symmetrical وبطيئة، بخطوة قصيرة وrotation قليل.</li></ul></div>

<div class="card"><h4>Malposture in sports</h4>
<ul><li>Quadriceps أقوى من الـ hamstrings بتشد الحوض لقدام، فيحصل <b>anterior pelvic tilt</b> ثم <b>hyperlordosis</b>، والـ hip flexors بتقفل.</li>
<li>Cyclists بيجيلهم <b>kyphotic thoracic spine</b>، والـ swimmer كمان kyphosis. الـ Power athlete بيجيله lordosis.</li>
<li>Volleyball: حركات asymmetrical (serve و attack) بتعمل asymmetry في الـ spine.</li>
<li>Soccer: أغلب الإصابات في الـ LL (خصوصًا الـ ACL). الـ pelvic asymmetry ممكن يكون سببها إصابات الرجلين.</li></ul></div>

<div class="card"><h4>Visceral implications</h4>
<ul><li>مينفعش نتعامل مع أجزاء الجسم كأنها منفصلة، وأي خلل في جزء بيعمل تغيير وظيفي في الباقي.</li>
<li>لو الـ mechanics كويسة، الـ abdominal cavity بتبقى زي <b>inverted pear</b> وفيه مساحة كافية <b>فوق L4</b>.</li>
<li>الـ Kidneys عند مستوى <b>L4</b>، وشايلها الـ psoas والـ quadratus lumborum والـ retroperitoneal fat.</li>
<li>حوالي <b>87%</b> من وزن أعضاء البطن شايله الـ psoas shelf وعضلات جدار البطن.</li>
<li>الـ Digestive disturbances سببها visceroptosis، وغالبًا من stretching للـ sympathetic nerves. لما الـ cavity تقصر طوليًا ممكن يحصل orthostatic albuminuria و dysmenorrhea و constipation.</li>
<li><b>Diaphragm</b>: لما الـ mechanics وحشة التنسيق بين عضلات التنفس بيضيع، والـ VC ممكن يقل لأكتر من النص. الـ diaphragm الواطي الـ excursion بتاعه أقل، فبيساعد الـ venous و lymphatic return أقل.</li></ul></div>

<div class="card"><h4>Chest deformities ★ كويز</h4>
<table><tr><th>Deformity</th><th>الوصف</th></tr>
<tr><td>Pectus excavatum</td><td><b>Funnel / sunken chest</b>: congenital، كذا ضلع والـ sternum بيكبروا غلط فالصدر من قدام يبقى concave (caved-in).</td></tr>
<tr><td>Pectus carinatum</td><td><b>Pigeon / keel chest</b>: rare، الـ sternum بيطلع لبرة بدل ما يبقى flush مع الصدر.</td></tr>
<tr><td>Barrel chest</td><td>زيادة الـ <b>AP diameter</b> زي البرميل، غالبًا مع الـ <b>emphysema</b>. كمان الـ arthritis ممكن يخشّب الصدر ويثبت الضلوع في أقصى وضع expanded.</td></tr></table></div>
""",
[
 ("Definition & Types", [
  ("Posture is best defined as:", ["Position or attitude of the body, maintained either with support during muscular inactivity or by coordinated action of many muscles", "Only the standing position of the body", "The alignment of the spine in sitting only", "The movement superimposed on the body during gait only"], "qz", "ده تعريف السلايد اللي جه في الكويز."),
  ("Inactive posture is:", ["Attitude adopted for resting or sleeping, with minimal muscular activity", "Integrated action of many muscles", "Walking and running", "Standing erect"], "", "وبتُستخدم في تدريب الـ general relaxation."),
  ("Inactive posture is used for:", ["Training general relaxation", "Strength training", "Gait training", "Balance training"], "", ""),
  ("Walking, running and even sitting while writing are examples of:", ["Dynamic (active) posture", "Static posture", "Inactive posture", "Passive equilibrium"], "", "الـ Active posture نوعين: static (standing و sitting) و dynamic."),
  ("Active posture requires:", ["Integrated activity of many muscles", "Complete muscle relaxation", "External support only", "No nervous control"], "", ""),
  ("Good posture is the attitude assumed by body parts to maintain stability and balance with:", ["Minimum effort and least strain", "Maximum muscle contraction", "Maximum joint compression", "Minimum base of support"], "imp", ""),
  ("Effects of good posture include all EXCEPT:", ["Increases muscle load during standing", "Improves respiratory and circulatory efficiency", "Prevents unnecessary strain and fatigue", "Improves the mental and psychological state"], "", "الـ good posture بيخلي العضلات unloaded و relaxed."),
 ]),
 ("POSTURE acronym & Plumb line", [
  ("In the POSTURE acronym, 'P' stands for:", ["Pelvis is neutral, with weight distributed", "Pelvis tilted anteriorly", "Posterior shoulders", "Proper breathing"], "imp", ""),
  ("In the POSTURE acronym, 'O' stands for:", ["On the whole foot", "Open chest", "Occiput over the sacrum", "Over-pronated feet"], "", "يعني القدم كلها على الأرض من غير inversion أو eversion."),
  ("In the POSTURE acronym, 'T' stands for:", ["Tight abdominals", "Tight hamstrings", "Thoracic kyphosis", "Toes pointed"], "", ""),
  ("In the POSTURE acronym, 'R' stands for:", ["Retracted midway shoulders", "Rotated pelvis", "Relaxed abdominals", "Rounded shoulders"], "", ""),
  ("In the POSTURE acronym, 'E' stands for:", ["Ear same level over shoulder", "Elbow extended", "Erector spinae contracted", "Even weight on heels"], "", "يعني الـ LOG بيعدي على الـ external auditory meatus والراس neutral."),
  ("In ideal posture (lateral view), the line of gravity passes through all EXCEPT:", ["Posterior to the knee joint", "Lobe of the ear", "Shoulder joint", "Greater trochanter of the femur"], "imp", "بيعدي slightly anterior لمنتصف الركبة."),
  ("In ideal posture, the line of gravity passes relative to the knee:", ["Slightly anterior to the midline of the knee", "Posterior to the knee", "Through the patella's lateral border", "Through the popliteal fossa"], "", ""),
  ("At the ankle, the ideal line of gravity passes:", ["Anterior to the lateral malleolus", "Through the calcaneus", "Posterior to the lateral malleolus", "Through the medial malleolus"], "", ""),
  ("The tool used to observe the midline of the body in posture assessment is the:", ["Plumb line", "Goniometer", "Kyphometer", "Dynamometer"], "", ""),
  ("Viewed from the front or the back, the vertical line through the center of gravity should:", ["Bisect the body into two equal halves", "Pass through the right leg only", "Pass anterior to the sternum", "Pass lateral to the pelvis"], "", "والوزن يبقى متوزع بالتساوي بين القدمين."),
  ("The key to good posture is the position of the:", ["Spine", "Feet", "Head only", "Shoulders only"], "", "الـ spine والـ pelvis هما الـ central base."),
  ("The closer the postural alignment lies to the center of all joint axes:", ["The less gravitational stress on the soft tissues", "The more muscle activity is needed", "The greater the disc pressure", "The higher the risk of falling"], "", ""),
 ]),
 ("Curvatures of the spine", [
  ("The primary curves of the spine are:", ["Thoracic (dorsal) and sacral, convex posteriorly", "Cervical and lumbar, convex anteriorly", "Cervical and thoracic", "Lumbar and sacral"], "imp", ""),
  ("Secondary curves of the spine are:", ["Cervical and lumbar, convex anteriorly", "Thoracic and sacral, convex posteriorly", "Thoracic and lumbar", "Only the sacral curve"], "", ""),
  ("Viewed from the front or back, the normal spine appears:", ["Straight and symmetrical", "S-shaped", "C-shaped", "Kyphotic"], "", ""),
  ("Scoliosis is best seen from the:", ["Posterior view", "Lateral view", "Superior view", "Sagittal view"], "", "أما الـ kyphosis والـ lordosis فبيتشافوا من الـ lateral view."),
 ]),
 ("Risk factors & causes", [
  ("Risk factors of bad posture include all EXCEPT:", ["Improves digestion", "Increases pressure on the spine", "Decreases flexibility", "Increases risk of falling"], "", "الـ bad posture بيصعّب الهضم بسبب العلاقة مع الـ sympathetic."),
  ("In women, bad posture may lead to:", ["Incontinence and/or pelvic organ prolapse", "Pectus carinatum", "Down's syndrome", "Hypermobility of OAA"], "", "بسبب imbalance في الـ core والـ pelvic floor."),
  ("Weak pelvic floor muscles may lead to:", ["Stress incontinence", "Pectus excavatum", "Hyperkyphosis", "Cervical radiculopathy"], "", ""),
  ("Aetiology of postural faults includes all EXCEPT:", ["Grade V manipulation", "Gravity", "Emotional states", "Pain"], "", "الستة: gravity، environment، architecture، pathology، emotional states، pain."),
  ("Over weight leads to poor posture because it:", ["Adds resistance to gravitational force leading to early degeneration and fatigue", "Strengthens the spinal extensors", "Increases red muscle fibers", "Corrects lumbar lordosis"], "", ""),
 ]),
 ("Muscle imbalance & Crossed syndromes", [
  ("In upper crossed syndrome, the TIGHT muscles are:", ["Upper trapezius, levator scapulae and pectorals", "Deep neck flexors and rhomboids", "Abdominals and gluteals", "Middle and lower trapezius"], "qz", ""),
  ("In upper crossed syndrome, the WEAK (inhibited) muscles are:", ["Deep neck flexors, rhomboids, serratus anterior and middle/lower trapezius", "Upper trapezius and levator scapulae", "Pectoralis major and minor", "Iliopsoas and rectus femoris"], "qz", ""),
  ("In lower crossed syndrome, the TIGHT muscles are:", ["Thoracolumbar erector spinae, iliopsoas and rectus femoris", "Abdominals and gluteals", "Hamstrings and abdominals", "Gluteus maximus and rectus abdominis"], "qz", ""),
  ("In lower crossed syndrome, the WEAK muscles are:", ["Abdominals and gluteals", "Erector spinae and iliopsoas", "Rectus femoris and erector spinae", "Quadratus lumborum and psoas"], "qz", ""),
  ("Lower crossed syndrome typically results in:", ["Anterior pelvic tilt and lumbar hyperlordosis", "Posterior pelvic tilt and flat back", "Forward head only", "Pectus carinatum"], "", ""),
  ("Upper crossed syndrome is commonly associated with:", ["Forward head, round shoulders and increased thoracic kyphosis", "Lumbar flat back", "Genu recurvatum", "Pes cavus"], "", ""),
  ("People with weak abdominal muscles (e.g. pregnant women) tend to develop:", ["Lumbar hyperlordosis", "Lumbar flattening", "Cervical flattening", "Pectus excavatum"], "", ""),
  ("A muscle that is chronically elongated:", ["Adds sarcomeres and its length-tension curve shifts to the right", "Loses sarcomeres and its curve shifts to the left", "Becomes stronger in its normal position", "Has no change in length-tension relation"], "imp", ""),
  ("A muscle that is chronically shortened:", ["Loses sarcomeres and its length-tension curve shifts to the left", "Adds sarcomeres and shifts to the right", "Produces maximal force in the stretched position", "Becomes hypermobile"], "", ""),
  ("'Stretch weakness' (Kendall) means the elongated muscle:", ["Develops maximal force in the stretched position and is weak in the normal physiological position", "Is strong in all positions", "Is weak only in the stretched position", "Is always painful"], "imp", ""),
  ("Posture-maintaining (anti-gravity) muscles contain more:", ["Red fibers that are slowly contracting and not easily fatigued", "White fast-twitch fibers", "Fibers that fatigue rapidly", "Smooth muscle fibers"], "", ""),
  ("The postural mechanism depends on interaction between:", ["The muscles and the nervous control", "The bones and the ligaments only", "The viscera and the diaphragm only", "The skin and the fascia"], "", ""),
  ("Bad posture may occur when one muscle group becomes tight and:", ["Its antagonist becomes elongated", "Its antagonist becomes tight too", "Its agonist becomes hypertrophied", "Joint axes are aligned"], "", ""),
 ]),
 ("Sitting, gait & sports", [
  ("Lumbar disc pressure during sitting compared to standing is:", ["Increased", "Decreased", "Equal", "Zero"], "", "لأن القعدة بتميل لـ lumbar kyphosis."),
  ("Disc pressure while sitting can be decreased by all EXCEPT:", ["Sitting with COG posterior to the ischium", "Arm rests", "Back support maintaining lumbar lordosis", "Reclining the back of the chair 90°–100°"], "", "ده هو الـ faulty sitting نفسه."),
  ("In faulty sitting, the COG moves posterior to the ischium leading to:", ["Increased lumbar kyphosis and IVD pressure", "Increased lumbar lordosis", "Decreased disc pressure", "Anterior pelvic tilt"], "", ""),
  ("In relaxed sitting, body weight should be supported upon:", ["The ischial tuberosities and adjacent soft tissues", "The sacrum", "The coccyx", "The thighs only"], "", ""),
  ("Failure of the knee to fully extend during heel strike is a sign of:", ["Weak quadriceps or flexion fusion of the knee", "Weak hamstrings", "Heel spur", "Weak gluteus medius"], "", ""),
  ("A painful heel strike with knee hyperextension is a sign of:", ["Weak hamstrings", "Weak quadriceps", "Tight calf", "Hip flexion contracture"], "", ""),
  ("In mild unilateral spinal pain, the trunk usually leans:", ["Toward the affected side (muscle splinting)", "Away from the affected side", "Forward only", "Backward only"], "", "في الـ disc أو SI lesions الشديدة بيميل بعيد عن الجنب المصاب."),
  ("Quadriceps over-strengthening relative to hamstrings leads to:", ["Anterior pelvic tilt and hyperlordosis", "Posterior pelvic tilt", "Thoracic kyphosis", "Scoliosis"], "", ""),
  ("Thoracic kyphosis is common in:", ["Cyclists and swimmers", "Volleyball players only", "Power athletes", "Soccer players"], "", "الـ Power athlete بيجيله lordosis."),
 ]),
 ("Visceral implications & chest deformities", [
  ("With good mechanics, the abdominal cavity is shaped like an inverted pear with adequate space above:", ["L4", "T12", "S2", "L1"], "", ""),
  ("The kidneys normally rest at the level of:", ["L4", "T6", "S1", "C7"], "", "وشايلها الـ psoas والـ quadratus lumborum والـ retroperitoneal fat."),
  ("About …… of the weight of the abdominal organs is borne by the psoas shelf and abdominal wall muscles:", ["87%", "50%", "25%", "10%"], "", ""),
  ("Pectus excavatum is also known as:", ["Funnel (sunken) chest", "Pigeon chest", "Keel chest", "Barrel chest"], "qz", "Congenital، الصدر من قدام بيبقى concave."),
  ("Pectus carinatum is characterized by:", ["Sternum pushed outward (pigeon / keel chest)", "Sternum caved inward", "Increased AP diameter due to emphysema", "Lateral spinal curvature"], "qz", ""),
  ("Barrel chest is MOST associated with:", ["Emphysema", "Asthma in children", "Scheuermann's disease", "Spondylolisthesis"], "qz", "زيادة في الـ AP diameter."),
  ("Arthritis may produce barrel chest by:", ["Stiffening the chest with ribs fixed in their most expanded position", "Depressing the sternum", "Causing lateral curvature", "Weakening the diaphragm"], "", ""),
  ("Poor body mechanics may decrease vital capacity by:", ["More than half", "5%", "Nothing", "Exactly 10%"], "", ""),
 ]),
])

# ================================================================ Maitland
L("l2", "Maitland Approach — Concept, Assessment & Cervical Spine", "Maitland", "🖐️",
  "سلايدات Maitland (د. ياسمين) + ملخص Hla (Lecture 1 و 2)",
"""
<div class="card"><h4>The Maitland Concept ★ كويز</h4>
<p class="ltr">"The Maitland Concept of Manipulative Physiotherapy emphasizes <b>a specific way of thinking, continuous evaluation and assessment</b> and <b>the art of manipulative physiotherapy</b> ('know when, how and which techniques to perform, and adapt these to the individual patient') and a <b>total commitment to the patient</b>."</p>
<ul><li>نفس فكرة <b>Kaltenborn</b>: الـ Kaltenborn = mobilization للـ <b>periphery</b> ومعتمد على الـ accessory movement عشان يحسن الـ physiological movement. أما الـ <b>Maitland</b> فبيطبق ده على الـ <b>spine</b> (flexion، extension، side bending، rotation).</li>
<li>الاتنين <b>static mobilization</b>، يعني المريض مش بيشارك بأي حركة active وبيبقى relaxed تمامًا.</li>
<li>الـ Maitland بيتعامل مع الـ spine كـ group of joints، فالمشكلة ممكن تبقى في أي فقرة، وعشان كده لازم <b>segmental assessment</b>.</li></ul></div>

<div class="card"><h4>Key terms</h4>
<table><tr><th>Term</th><th>المعنى</th></tr>
<tr><td>Accessory movement</td><td>Joint play: حركات مينفعش الشخص يعملها بنفسه (roll، spin، slide) ومصاحبة للـ physiological movement. بنفحصها <b>passively</b> في الـ <b>open pack position</b>.</td></tr>
<tr><td>Physiological movement</td><td>الحركات اللي الشخص بيعملها active، وبنحللها من حيث الجودة والأعراض.</td></tr>
<tr><td>Injuring movement</td><td>الحركة اللي بتطلع الألم أو الأعراض أثناء الكشف.</td></tr>
<tr><td>Overpressure</td><td>كل مفصل ليه passive range أكبر من الـ active. بنوصله بـ stretch في آخر الـ passive movement، وغالبًا بيبقى معاه discomfort.</td></tr></table></div>

<div class="card"><h4>Principles of techniques</h4>
<ol class="ltr"><li><b>The Direction</b>: clinically reasoned ومناسب للتشخيص. مش كل الاتجاهات بتنفع مع كل dysfunction.</li>
<li><b>The Desired Effect</b>: relieve pain ولا stretch stiffness؟</li>
<li><b>The Starting Position</b>: للمريض والمعالج، ومكان الإيد عشان التأثير يبقى localized.</li>
<li><b>The Method of Application</b>: position, range, amplitude, rhythm, duration.</li>
<li><b>The Expected Response</b>: pain-free؟ زيادة الـ range؟ soreness أقل؟</li>
<li><b>How might the technique be progressed</b>: duration, frequency or rhythm.</li></ol></div>

<div class="card"><h4>Assessment (بالترتيب)</h4>
<ol><li><b>Active ROM</b>: بيحدد <b>اتجاه</b> الـ limitation ويديك توقع للـ pathology.</li>
<li><b>Passive ROM (end feel)</b>: أشهرها spasm و empty و bony. بيحدد <b>سبب</b> الـ limitation والـ primary line of treatment. (لو PROM أكبر من AROM فده inflammation، والـ empty end feel فده كمان)</li>
<li><b>Segmental assessment</b> (Maitland PAIVM: anterior، posterior، lateral glide): <b>الأهم</b> لأنه بيحدد <b>مستوى</b> الـ lesion.</li></ol>
<p>وبعدها subjective examination و palpation (temperature، soft tissue، bony positions).</p></div>

<div class="card"><h4>PAIVM assessment</h4>
<table><tr><th>Technique</th><th>التطبيق</th><th>الهدف</th></tr>
<tr><td>PACVM (CVP)</td><td>Postero-anterior central على الـ <b>spinous process</b>، والمريض prone</td><td>Flexion و extension. الـ apex بتاع الـ cervical lordosis عند C3–4</td></tr>
<tr><td>PAUM</td><td>Postero-anterior unilateral على الـ <b>transverse process</b> أو الـ <b>facet joint</b> من جنب واحد</td><td>Rotation (الـ facet حوالي ½ inch من الـ SP، والـ TP حوالي 1 inch)</td></tr>
<tr><td>APUM</td><td>Antero-posterior unilateral على الـ transverse process من قدام، والمريض <b>supine</b> (cervical بس)</td><td>بيُستخدم لما المريض <b>مش قادر ينام prone</b> (عملية، مشاكل تنفس، حروق، أمراض جلدية…)</td></tr>
<tr><td>TVP</td><td>Transverse vertebral pressure على <b>جنب الـ spinous process</b> (من الـ lateral)</td><td><b>Side bending</b></td></tr>
<tr><td>Longitudinal</td><td>Distraction (upper cervical من الـ occiput، و lower cervical)</td><td>Traction</td></tr></table>
<ul><li>عشان تقيّم الـ <b>extension</b> بنعمل anterior glide (PA). لو فيه extension limitation يبقى فيه <b>flexion lesion</b>.</li>
<li>عشان تقيّم الـ <b>rotation</b> بنعمل الـ Maitland (PAUM) على الـ transverse process والـ facet في <b>الجنب العكسي</b>. مثال: عشان تقيّم الـ right rotation بتشتغل على الـ <b>left</b> TP.</li>
<li><b>Right rotation lesion</b> = left rotation limitation، وهتلاقي الـ right TP بارز (prominent).</li>
<li>في الـ <b>Side bending</b>: الـ vertebral body بيتحرك في نفس اتجاه الحركة والـ <b>spinous process عكسها</b>. عشان كده بنحرك الـ SP في الاتجاه العكسي (TVP).</li>
<li>في الـ cervical بنستخدم الـ TP والـ facet للـ rotation mobilization. في الـ thoracic والـ lumbar بنستخدم الـ <b>TP بس</b>.</li></ul></div>

<div class="card"><h4>Grades of mobilization (Maitland)</h4>
<table class="ltr"><tr><th>Grade</th><th>Description</th><th>Use</th></tr>
<tr><td>I</td><td>Small amplitude rhythmic oscillation at the <b>beginning</b> of range (taking the slack)</td><td>Pain &amp; spasm</td></tr>
<tr><td>II</td><td>Large amplitude rhythmic oscillation within the <b>mid-range</b></td><td>Pain &amp; spasm</td></tr>
<tr><td>III</td><td>Large amplitude up to the <b>limit</b> (into resistance)</td><td>Stiffness</td></tr>
<tr><td>IV</td><td>Small amplitude <b>into the barrier</b> (end range)</td><td>Stiffness</td></tr>
<tr><td>V</td><td>Thrust = manipulation: small amplitude, high velocity</td><td>Joint lock / end-range limitation</td></tr></table>
<ul><li>Grades I &amp; II بيتعملوا غالبًا قبل وبعد الـ III &amp; IV.</li>
<li><b>Oscillations:</b> Grades I &amp; IV rapid oscillation. Grades II &amp; III بمعدل 2–3/sec لمدة 1–2 min.</li>
<li>Low amplitude و high speed عشان الألم. Slow speed عشان الـ muscle guarding.</li>
<li><b>Staccato mobilization</b> (3–5 oscillations) عشان الـ pain relief في الـ grade IV.</li>
<li>عشان تريّح المريض في النص بترجع للـ grade اللي قبله مباشرة (من III لـ II)، مش لـ I.</li>
<li><b>Sustained joint play</b>: الـ painful joint play بيتعمل intermittent distraction لمدة 7–10 sec. الـ restricted: 6 sec stretch (grade III)، بعدها partial release لـ I/II لمدة 3 sec، وكرر 3–4 مرات.</li></ul></div>

<div class="card"><h4>Cervical spine</h4>
<ul><li>بيتقسم biomechanically لـ <b>OAA complex</b> (occiput-atlas-axis) و <b>C2–C7</b>.</li>
<li>الـ Cervical lordosis في المتوسط <b>40°</b>. لو قليلة (flattening) يبقى disc compression، ولو كتيرة (hyperlordosis) يبقى facet compression.</li>
<li><b>Hyperlordosis</b> = extension lesion: زاوية أكبر من 40°، والـ vertebrae في anterior glide، وممكن تعمل facet arthritis.
<br><b>Flattening</b> = flexion lesion: زاوية أقل من 40°، والـ vertebrae في posterior glide، وممكن تعمل disc bulge.</li>
<li>الـ <b>Facets</b> في الـ cervical: <b>45°</b> مع الـ transverse plane و parallel للـ frontal plane، وكل الحركات ممكنة. الـ superior articular process بيبص posterior و up.</li>
<li><b>ROM:</b> Flexion 50°، Extension 60°، Side bending 45°، Rotation 80°.</li>
<li>حوالي <b>50%</b> من الـ flexion-extension عند <b>occiput–C1</b>، وحوالي <b>50%</b> من الـ rotation عند <b>C1–C2</b> (atlanto-axial).</li>
<li>كل الـ cervical spinous processes <b>bifid</b> ما عدا <b>C7</b>. الـ Atlas مالوش spinous process (فيه anterior و posterior tubercles). الـ Joints of Luschka بتزود الثبات.</li>
<li>الـ OAA متثبت بالـ ligaments، ومع ذلك هو <b>أكتر مكان بيحصل فيه instability</b>، لأن الـ occiput والـ atlas بيتحركوا بـ translation. الأعراض: dizziness و headache و neck pain و visual disturbance و numbness.</li>
<li>Palpation landmark للـ cervical: الـ <b>sternocleidomastoid</b>. والـ C7 هو أبرز spinous process.</li></ul></div>

<div class="card"><h4>طبيعة الألم في الـ case history</h4>
<table><tr><th>نوع الألم</th><th>المصدر المحتمل</th></tr>
<tr><td>Aching + morning stiffness، أو بعد قعدة أو وقفة طويلة</td><td>Ligament</td></tr>
<tr><td>Sharp pain on specific movements</td><td>Muscle strain أو inflammation</td></tr>
<tr><td>Fatigue</td><td>Bad posture و cervical muscular imbalance</td></tr>
<tr><td>Sharp pain when coughing</td><td>Inflammation</td></tr>
<tr><td>Radiating pain</td><td>Neurogenic (radicular أو pseudo-radicular)</td></tr>
<tr><td>Numbness أو muscle weakness</td><td>Severe radicular inflammation، غالبًا hernia ضاغط على الـ root</td></tr>
<tr><td>ألم غامض بينتشر في الدراع مع المجهود</td><td>Ischemic neuralgia</td></tr>
<tr><td>Nocturnal pain</td><td>Cancer</td></tr></table></div>

<div class="card"><h4>Safety tests (قبل أي handling للـ cervical)</h4>
<table><tr><th>Test</th><th>الطريقة</th><th>الإيجابي</th></tr>
<tr><td>Vascular: <b>De Kleyn</b></td><td>Supine، hyperextension + rotation + ipsilateral side bending، العين مفتوحة، لمدة <b>45 sec</b> على الأقل (بيضغط vertebral artery)</td><td>Dizziness، headache + neck pain، fainting، nystagmus. ده VBI، فيبقى contraindicated للـ mobilization والـ manipulation</td></tr>
<tr><td><b>Hypermobility</b> test</td><td>المعالج ورا المريض، يثبت الـ axis بصباع ويحرك الـ atlas للناحية التانية (في الاتجاهين)</td><td>حركة أكتر من <b>3 mm</b> يبقى hypermobile segment (RA، <b>Down's syndrome</b> بسبب الـ laxity)</td></tr>
<tr><td>Neural: <b>Spurling</b> (cervical compression)</td><td>Sitting، compression في الـ <b>extension</b> فالـ facets تتضغط أقصى ضغط. ممكن unilateral بـ extension + ipsilateral rotation و side bending</td><td>الألم معناه intra-articular problem. لو اتعمل في الـ flexion بيختبر الـ discs. كمان بيكشف vertebro-basilar pathology</td></tr></table>
<p class="key">الـ acute disc bulge contraindicated للـ mobilization والـ manipulation. الـ Severe pain والـ severe inflammation كمان contraindicated للـ mobilization.</p></div>
""",
[
 ("Concept & key terms", [
  ("The Maitland concept emphasizes all of the following EXCEPT:", ["A fixed protocol applied identically to every patient", "A specific way of thinking", "Continuous evaluation and assessment", "Total commitment to the patient"], "qz", "الفكرة إنك تعرف when و how و which technique وتعدلها حسب كل مريض."),
  ("'Know when, how and which techniques to perform, and adapt these to the individual patient' describes:", ["The art of manipulative physiotherapy (Maitland)", "Mulligan's PILL principle", "Fryette's third law", "Kaltenborn's convex-concave rule"], "qz", ""),
  ("Kaltenborn mobilization is applied mainly to:", ["The periphery (peripheral joints)", "The spine only", "The ribs only", "The viscera"], "imp", "والـ Maitland بيطبق نفس الفكرة على الـ spine."),
  ("Maitland and Kaltenborn are techniques of:", ["Static mobilization without active participation of the patient", "Mobilization with movement", "Dynamic weight-bearing mobilization", "Thrust manipulation"], "imp", "المريض لازم يبقى relaxed تمامًا."),
  ("Accessory movements are:", ["Joint play movements that cannot be performed by the individual", "Movements performed actively by the patient", "Movements that produce pain only", "Movements beyond the anatomical limit"], "", "Roll و spin و slide."),
  ("Accessory movements are examined passively in the:", ["Open pack position", "Close pack position", "End of anatomical range", "Weight-bearing position only"], "", ""),
  ("Making the pain 'come on' by moving the joint in a particular direction during assessment is called:", ["Injuring movement", "Overpressure", "Accessory movement", "Comparable sign"], "", ""),
  ("Overpressure is:", ["A stretch applied at the end of normal passive movement to reach the passive range exceeding the active range", "A thrust beyond the anatomical limit", "An active movement by the patient", "A grade I oscillation"], "", ""),
  ("Which is NOT one of Maitland's principles of techniques?", ["The patient's active resisted movement", "The direction", "The desired effect", "The expected response"], "", "الستة: direction، desired effect، starting position، method of application، expected response، progression."),
  ("The method of application in Maitland includes:", ["Position, range, amplitude, rhythm and duration", "Only the force direction", "Only the number of sessions", "Weight-bearing and active movement"], "", ""),
 ]),
 ("Assessment & PAIVM", [
  ("The correct order of Maitland assessment is:", ["Active ROM → Passive ROM (end feel) → Segmental assessment", "Segmental → Passive → Active", "Passive → Active → Palpation only", "Manipulation → Active ROM → Passive"], "imp", ""),
  ("Active ROM in assessment determines:", ["The direction of limitation", "The level of the lesion", "The end feel", "The grade of mobilization"], "imp", ""),
  ("Passive ROM (end feel) determines:", ["The cause of limitation and the primary line of treatment", "The direction of limitation only", "The exact vertebral level", "The patient's posture"], "imp", ""),
  ("The MOST important part of assessment because it determines the level of the lesion is:", ["Segmental assessment", "Active ROM", "Passive ROM", "Observation"], "imp", ""),
  ("PACVM is applied on the:", ["Spinous process (central)", "Transverse process unilaterally", "Facet joint from the front", "Occiput"], "", "Postero-anterior central vertebral mobilization، واسمه كمان CVP."),
  ("PACVM is used to assess and enhance:", ["Flexion and extension", "Rotation", "Side bending only", "Traction"], "", ""),
  ("PAUM is applied on the transverse process or facet joint to assess and enhance:", ["Rotation", "Flexion only", "Extension only", "Longitudinal movement"], "imp", ""),
  ("APUM is used when:", ["The patient cannot lie in the prone position", "The patient has thoracic kyphosis", "The lesion is in the lumbar spine", "The patient is in weight bearing"], "imp", "بيتعمل والمريض supine على الـ cervical."),
  ("TVP (transverse vertebral pressure) is applied on the side of the spinous process to enhance:", ["Side bending", "Flexion", "Extension", "Traction"], "imp", ""),
  ("To assess right rotation using Maitland (PAUM), pressure is applied on the:", ["Left transverse process / facet", "Right transverse process", "Spinous process centrally", "Occiput"], "imp", "الـ Maitland على الجنب العكسي، والـ Mulligan على نفس الجنب."),
  ("A right rotation lesion means:", ["Left rotation limitation with a prominent right transverse process", "Right rotation limitation", "Right side bending limitation only", "Flexion limitation"], "", ""),
  ("During side bending, the spinous process moves:", ["Opposite to the direction of the physiological movement", "In the same direction as the vertebral body", "Anteriorly", "It does not move"], "imp", "الـ body مع الحركة والـ SP عكسها."),
  ("In the thoracic and lumbar spine, rotation mobilization uses:", ["The transverse process only", "The transverse process and facet joint", "The spinous process only", "The rib angle only"], "", "في الـ cervical بنستخدم الـ TP والـ facet."),
  ("Extension limitation found on assessment indicates a:", ["Flexion lesion", "Extension lesion", "Rotation lesion", "Neutral lesion"], "imp", ""),
  ("End feels commonly assessed in passive ROM include:", ["Spasm, empty and bony", "Soft, firm and springy only", "Capsular and elastic only", "None — end feel is not assessed"], "", ""),
  ("Palpation in Maitland assessment includes all EXCEPT:", ["Spirometry", "Temperature", "Soft tissue", "Bony positions"], "", ""),
 ]),
 ("Grades of mobilization", [
  ("Grade I Maitland mobilization is:", ["Small amplitude rhythmic oscillation at the beginning of the range", "Large amplitude up to the limit", "Small amplitude into the barrier", "High velocity thrust"], "imp", ""),
  ("Grade II is:", ["Large amplitude rhythmic oscillation within the mid-range", "Small amplitude at end range", "A thrust at the anatomical barrier", "Sustained stretch for 30 seconds"], "imp", ""),
  ("Grade III is:", ["Large amplitude up to the limit of the range", "Small amplitude at the beginning of range", "Small amplitude into the barrier", "Taking up the slack only"], "imp", ""),
  ("Grade IV is:", ["Small amplitude into the barrier (end of range)", "Large amplitude mid-range", "Small amplitude beginning of range", "High velocity thrust"], "imp", ""),
  ("Grades I and II are mainly used to:", ["Manage pain and spasm", "Stretch chronic stiffness", "Break adhesions", "Unlock a joint with a thrust"], "", ""),
  ("Grades III and IV are mainly used for:", ["Stiffness", "Acute severe pain", "Muscle guarding only", "Hypermobility"], "", ""),
  ("Grade V refers to:", ["Manipulation (thrust technique)", "Sustained traction", "Mulligan SNAGs", "Grade IV with overpressure"], "", ""),
  ("Staccato mobilization (3–5 oscillations) is used for:", ["Pain relief", "Breaking adhesions", "Increasing hypermobility", "Assessment of level"], "", ""),
  ("Grades II & III oscillations are applied at a rate of:", ["2–3 per second for 1–2 minutes", "10 per second for 10 minutes", "1 every minute", "Single thrust"], "", ""),
  ("To relax the patient during grade III mobilization, the therapist returns to:", ["Grade II (the grade directly before)", "Grade I", "Grade V", "Stops the session"], "", ""),
  ("Low amplitude and high speed oscillations are used to:", ["Decrease pain", "Stretch the capsule", "Break adhesions", "Increase muscle guarding"], "", "والـ slow speed عشان الـ muscle guarding."),
 ]),
 ("Cervical spine", [
  ("The average cervical lordosis is:", ["40°", "20°", "60°", "90°"], "imp", ""),
  ("Too little cervical lordosis (flattening) leads to:", ["Disc compression", "Facet compression", "Vertebral artery stretch", "Atlas hypermobility"], "imp", ""),
  ("Too much cervical lordosis (hyperlordosis) leads to:", ["Facet compression (may cause facet arthritis)", "Disc compression", "Spinal canal widening", "Rib fanning"], "imp", ""),
  ("Cervical hyperlordosis is considered a(n):", ["Extension lesion with vertebral anterior glide", "Flexion lesion with posterior glide", "Neutral group lesion", "Rotation lesion"], "", ""),
  ("Cervical facet joints are oriented at:", ["45° to the transverse plane, parallel to the frontal plane", "60° to the transverse plane and 20° to the frontal plane", "90° in the sagittal plane", "0° horizontal"], "imp", ""),
  ("Normal cervical rotation range is:", ["80°", "45°", "50°", "60°"], "", "Flexion 50°، Extension 60°، SB 45°."),
  ("Normal cervical extension range is:", ["60°", "50°", "45°", "80°"], "", ""),
  ("About 50% of cervical flexion-extension occurs at:", ["Occiput–C1", "C1–C2", "C5–C6", "C7–T1"], "imp", ""),
  ("About 50% of cervical rotation occurs at:", ["C1–C2 (atlanto-axial)", "Occiput–C1", "C3–C4", "C6–C7"], "imp", ""),
  ("All cervical spinous processes are bifid EXCEPT:", ["C7", "C2", "C3", "C5"], "", ""),
  ("The atlas (C1):", ["Has no spinous process but has anterior and posterior tubercles", "Has the most prominent spinous process", "Has a bifid spinous process", "Has no transverse processes"], "", ""),
  ("The most common site for cervical instability (hypermobility) is the:", ["OAA complex", "C5–C6", "C7–T1", "C3–C4"], "", "لأن الـ occiput والـ atlas بيتحركوا بـ translation."),
  ("Symptoms of cervical spine hypermobility include all EXCEPT:", ["Bony end feel", "Dizziness", "Headache", "Visual disturbance"], "", ""),
  ("The cervical spine is divided biomechanically into:", ["OAA complex and C2–C7", "C1–C4 and C5–T1", "Upper thoracic and lower cervical", "Atlas and axis only"], "", ""),
 ]),
 ("Pain nature & safety tests", [
  ("Aching pain in the morning with morning stiffness most likely originates from:", ["Ligament", "Nerve root", "Cancer", "Ischemic neuralgia"], "", ""),
  ("Nocturnal neck pain often indicates:", ["Cancer", "Ligament sprain", "Bad posture", "Muscle fatigue"], "imp", ""),
  ("Numbness or muscle weakness in a neck patient indicates:", ["Severe radicular inflammation (often hernia compressing the root)", "Ligament strain", "Postural fatigue", "Facet arthritis only"], "", ""),
  ("Vague radiating arm pain during exercise can indicate:", ["Ischemic neuralgia", "Disc herniation", "Ligament sprain", "Muscle strain"], "", ""),
  ("Sharp pain when coughing often directs towards:", ["Inflammation", "Ligament laxity", "Postural fatigue", "Cancer"], "", ""),
  ("De Kleyn test is a:", ["Vascular safety test for vertebrobasilar insufficiency", "Neural compression test", "Hypermobility test of OAA", "Rib spring test"], "imp", ""),
  ("De Kleyn test position is:", ["Supine with hyperextension, rotation and ipsilateral side bending held ≥45 seconds", "Sitting with axial compression in extension", "Prone with PA pressure", "Standing with forward flexion"], "imp", ""),
  ("A positive De Kleyn test includes all EXCEPT:", ["Increased cervical rotation range", "Dizziness", "Nystagmus", "Feeling of fainting"], "", ""),
  ("In the hypermobility test, a motion of more than …… indicates a hypermobile segment:", ["3 mm", "1 cm", "10 mm", "0.5 mm"], "imp", ""),
  ("The hypermobility test is positive in:", ["Down's syndrome (general laxity) and rheumatoid arthritis", "Ankylosing spondylitis", "Cervical spondylosis", "Scheuermann's disease"], "", ""),
  ("Spurling (cervical compression) test applies compression in extension so that:", ["The facets are under maximum compression", "The discs are unloaded", "The vertebral artery is stretched", "The atlas translates"], "imp", "الألم معناه intra-articular problem، ولو في flexion بيختبر الـ discs."),
  ("Cervical compression with the head in flexion tests the:", ["Intervertebral discs", "Facet joints", "Vertebral artery", "Alar ligament"], "", ""),
  ("A positive vascular safety test (VBI) means:", ["Mobilization and manipulation are contraindicated", "Grade IV mobilization is indicated", "Manipulation is the first line", "Mulligan SNAGs are indicated"], "", ""),
 ]),
])
