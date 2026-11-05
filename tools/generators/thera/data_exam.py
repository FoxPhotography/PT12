# Therapeutic Exercises II — doctor's quiz questions (written, with model answers), cases, T/F drill.

# ---- Written questions: (question, source_label, model_answer_html)
QUIZ_WRITTEN = [
 ("Define posture and explain upper and lower cross syndromes in a diagram.", "كويز المحاضرة 1",
  """<p class="ltr"><b>Posture:</b> position or attitude of the body either with support during muscular inactivity, or by the coordinated action of many muscles working to maintain stability or to form an essential basis which is being adapted constantly to the movement superimposed upon it.</p>
<div class="xgrid">
<div class="xbox"><div class="xt">Upper Crossed Syndrome</div>
<div class="xd"><svg viewBox="0 0 100 60" preserveAspectRatio="none"><line class="lt" x1="6" y1="8" x2="94" y2="52"/><line class="lw" x1="94" y1="8" x2="6" y2="52"/></svg>
<span class="xl tl t">TIGHT<br>Upper trapezius<br>Levator scapulae</span><span class="xl tr w">WEAK<br>Deep neck flexors</span>
<span class="xl bl w">WEAK<br>Rhomboids<br>Serratus ant.<br>Mid / Low trap</span><span class="xl br t">TIGHT<br>Pectoralis<br>major &amp; minor</span></div>
<p class="ltr xr">Result: forward head, round shoulders, ↑ thoracic kyphosis</p></div>
<div class="xbox"><div class="xt">Lower Crossed Syndrome</div>
<div class="xd"><svg viewBox="0 0 100 60" preserveAspectRatio="none"><line class="lt" x1="6" y1="8" x2="94" y2="52"/><line class="lw" x1="94" y1="8" x2="6" y2="52"/></svg>
<span class="xl tl t">TIGHT<br>Thoracolumbar<br>erector spinae</span><span class="xl tr w">WEAK<br>Abdominals</span>
<span class="xl bl w">WEAK<br>Gluteals</span><span class="xl br t">TIGHT<br>Iliopsoas<br>Rectus femoris</span></div>
<p class="ltr xr">Result: anterior pelvic tilt, lumbar hyperlordosis</p></div></div>
<p>القطر الأحمر = العضلات الـ <b>tight</b>، والقطر التاني = العضلات الـ <b>weak</b>. ارسمها كده في الورقة بالظبط.</p>"""),
 ("Explain chest deformities.", "كويز المحاضرة 2",
  """<ul class="ltr"><li><b>Pectus excavatum</b> (funnel / sunken chest): congenital chest wall deformity in which several ribs and the sternum grow abnormally, producing a concave (caved-in) anterior chest.</li>
<li><b>Pectus carinatum</b> (pigeon / keel chest): rare deformity in which the sternum pushes outward instead of lying flush with the chest (abnormal growth of costal cartilage).</li>
<li><b>Barrel chest</b>: increase in the anterior-posterior diameter of the chest resembling a barrel, most often associated with <b>emphysema</b>; arthritis can also stiffen the chest with ribs fixed in their most expanded position.</li></ul>
<p>وممكن تضيف إن الـ barrel chest = <b>inhalation lesion</b>، والـ ribs هي السبب الأساسي، فالـ first line هو exhalation rib mobilization.</p>"""),
 ("Define Maitland and explain its concept of mobilization.", "كويز المحاضرة 2",
  """<p class="ltr">The Maitland Concept of Manipulative Physiotherapy emphasizes a <b>specific way of thinking</b>, <b>continuous evaluation and assessment</b> and the <b>art of manipulative physiotherapy</b> ("know when, how and which techniques to perform, and adapt these to the individual patient") and a <b>total commitment to the patient</b>.</p>
<ul><li>بيستخدم نفس فكرة Kaltenborn (الـ accessory movement بيحسن الـ physiological movement)، بس على الـ <b>spine</b> (flexion، extension، side bending، rotation).</li>
<li><b>Static mobilization</b>: المريض passive و relaxed ومش بيشارك.</li>
<li><b>Assessment</b>: AROM (اتجاه الـ limitation)، PROM end feel (السبب والـ primary line)، segmental PAIVM (المستوى: PACVM، PAUM، APUM، TVP، longitudinal).</li>
<li><b>Treatment</b>: graded oscillations. Grades I–II للألم والـ spasm، III–IV للـ stiffness، و V manipulation.</li>
<li>Principles: direction، desired effect، starting position، method of application، expected response، progression.</li></ul>"""),
 ("Explain methods of Maitland assessment for mid thoracic flexion lesion, name of this deformity and method for treatment.", "كويز المحاضرة 4",
  """<p><b>الـ Deformity:</b> <b>Thoracic (hyper)kyphosis</b>، وهي flexion lesion + expiration lesion، والفقرات في <b>posterior displacement</b>.</p>
<p><b>Assessment (Maitland):</b></p><ol>
<li><b>Active ROM</b>: هتلاقي extension limitation (اتجاه الـ limitation).</li>
<li><b>Passive ROM / end feel</b>: عشان تعرف السبب (stiffness / spasm) والـ primary line.</li>
<li><b>Segmental assessment (PAIVM)</b> والمريض prone: <b>PACVM</b> (posteroanterior central على الـ spinous process) على كل فقرة لوحدها. الفقرة اللي فيها الـ lesion هتبقى stiff أو مؤلمة في الـ anterior glide، وده بيحدد المستوى. ممكن كمان PAUM على الـ TPs.</li>
<li><b>Rib assessment</b> (supine، global ثم segmental): expiration lesion. الـ upper 6 ribs caudal، والـ lower 6 antero-medial، والـ diaphragm ascending.</li></ol>
<p><b>Treatment:</b></p><ul>
<li>First line: <b>extension mobilization</b> = anterior (PA) mobilization على الفقرة (PACVM)، grades I–II للألم و III–IV للـ stiffness، والضلوع بتتبع.</li>
<li>Ribs: upper ribs <b>cranial</b> mobilization و lower ribs <b>postero-lateral</b> mobilization أثناء الشهيق (inhalation mobilization)، و diaphragmatic release، و release + distraction للـ costochondral.</li>
<li>Stretch للـ pectorals، تقوية الـ middle/lower trapezius والـ rhomboids والـ spinal extensors، breathing exercises، و postural training.</li></ul>"""),
]

EXPECTED_WRITTEN = [
 ("Compare between Maitland and Mulligan.", "متوقع",
  """<table><tr><th>Maitland</th><th>Mulligan</th></tr>
<tr><td>Assessment + treatment</td><td>Treatment only</td></tr><tr><td>Chronic</td><td>Acute &amp; chronic</td></tr>
<tr><td>Slight discomfort (III, IV)</td><td>Pain free</td></tr><tr><td>Static, passive</td><td>Dynamic, active participation</td></tr>
<tr><td>Neutral / position of limitation, NWB</td><td>Functional position, WB &amp; NWB</td></tr>
<tr><td>Opposite side of limitation</td><td>Same side of limitation</td></tr><tr><td>Gradual effect</td><td>Immediate effect</td></tr>
<tr><td>Central pressure</td><td>Cranial glide + overpressure at end ROM</td></tr>
<tr><td>Better for severe stiffness &amp; adhesions</td><td>Better for functional improvement &amp; acute cases</td></tr></table>"""),
 ("State Fryette's laws and the first line of treatment of neutral and non-neutral lesions.", "متوقع",
  """<ol class="ltr"><li><b>1st law (neutral):</b> side bending to one side → rotation to the opposite side (group lesion).</li>
<li><b>2nd law (non-neutral, flexion/extension):</b> side bending → rotation to the same side (monolytic lesion).</li>
<li><b>3rd law:</b> increasing motion in one plane decreases motion in the other two planes.</li></ol>
<p>Neutral (group) lesion: first line <b>visceral release</b> (sympathetic chain). Non-neutral (monolytic): first line <b>manipulation</b>. تحت <b>L2</b> مفيش neutral lesion لأن الـ sympathetic chain بيخلص عند L2.</p>"""),
 ("Compare between kyphosis and barrel chest regarding ribs, diaphragm and line of treatment.", "متوقع",
  """<table><tr><th></th><th>Kyphosis</th><th>Barrel chest</th></tr>
<tr><td>Lesion</td><td>Flexion + expiration</td><td>Inhalation (+ extension)</td></tr>
<tr><td>Primary cause</td><td>Vertebrae</td><td>Ribs</td></tr>
<tr><td>Upper ribs</td><td>Caudal → cranial mob.</td><td>Cranial</td></tr>
<tr><td>Lower ribs</td><td>Antero-medial → postero-lateral mob.</td><td>Postero-lateral</td></tr>
<tr><td>Diaphragm</td><td>Ascending, short → release</td><td>Descending, weak → strengthen</td></tr>
<tr><td>Costochondral</td><td>Compressed → release/distraction</td><td>Distracted → approximation</td></tr>
<tr><td>First line</td><td>Thoracic extension mobilization</td><td>Exhalation rib mobilization</td></tr></table>"""),
 ("Mention the grades of Maitland mobilization.", "متوقع",
  """<ul class="ltr"><li><b>I</b>: small amplitude rhythmic oscillation at the beginning of range (pain/spasm).</li><li><b>II</b>: large amplitude within mid-range (pain/spasm).</li><li><b>III</b>: large amplitude up to the limit (stiffness).</li><li><b>IV</b>: small amplitude into the barrier (stiffness).</li><li><b>V</b>: manipulation (high velocity small amplitude thrust).</li></ul>"""),
 ("Mention the safety tests before cervical mobilization / manipulation.", "متوقع",
  """<ol class="ltr"><li><b>Vascular – De Kleyn:</b> supine, hyperextension + rotation + ipsilateral SB, eyes open, ≥45 s. +ve: dizziness, headache, fainting, nystagmus (VBI).</li>
<li><b>Hypermobility test (OAA):</b> fix axis, move atlas to the opposite side; &gt;3 mm = hypermobile (RA, Down's).</li>
<li><b>Neural – Spurling (cervical compression):</b> sitting, compression in extension → facets; pain = intra-articular; in flexion → discs.</li></ol>"""),
 ("Mention the principles of application of manipulation (HVLAT).", "متوقع",
  """<p class="ltr">Joint gapping · Localization (apex of two intersecting curves) · Force direction · Fulcrum · Velocity · Amplitude (≈1/8 inch) · Balance &amp; control · Maintenance (other segments with the same direction of dominance).</p>"""),
 ("Mention absolute contraindications of spinal manipulation.", "متوقع",
  """<ul class="ltr"><li><b>Bone:</b> tumour, infection (TB), metabolic (osteomalacia), congenital dysplasia, iatrogenic (long-term corticosteroids), inflammatory (severe RA), fracture.</li>
<li><b>Neurological:</b> cervical myelopathy, cord compression, cauda equina compression, nerve root compression with increasing deficit.</li>
<li><b>Vascular:</b> diagnosed VBI, aortic aneurysm, bleeding diathesis (haemophilia).</li>
<li>Lack of diagnosis, lack of consent, position cannot be achieved (pain/resistance).</li></ul>"""),
 ("Mention the types of kyphosis and the braces used for hyperkyphosis.", "متوقع",
  """<p><b>Types:</b> postural (الأكثر شيوعًا، البنات، المراهقة)، Scheuermann's (structural، المراهقة، مع scoliosis)، congenital (الأقل شيوعًا، fusion).</p>
<p><b>Braces:</b> Milwaukee (الأكثر، posterior pads، 23 ساعة في اليوم لمدة 1–2 سنة)، Lyon antikyphosis، Kyphologic، Gschwend (two 3-point pressure، ألمانيا). بنلجأ للـ bracing بس لما التمارين متنفعش، ومن غير PT مالوش تأثير.</p>"""),
]

# ---- Case sets (MCQ). Each: (case_text, [ (q, [correct, wrong...], expl) ])
CASES = [
 ("A 45-year-old office worker complains of mid-back pain and fatigue. On lateral view he has a rounded upper back, forward head and protracted shoulders. Active extension of the thoracic spine is limited. On PACVM, T6 is stiff and painful. Rib assessment shows the upper ribs depressed (caudal) and the lower ribs antero-medial.", [
   ("The deformity is:", ["Thoracic hyperkyphosis", "Barrel chest", "Lumbar hyperlordosis", "Scoliosis"], ""),
   ("T6 is in a:", ["Flexion lesion (posterior displacement)", "Extension lesion (anterior displacement)", "Neutral group lesion", "Rotation lesion only"], ""),
   ("The rib lesion is:", ["Expiration lesion", "Inhalation lesion", "Neutral lesion", "No lesion"], ""),
   ("The first line of treatment is:", ["Extension (anterior PA) mobilization of the thoracic spine", "Exhalation rib mobilization", "Flexion mobilization", "Diaphragm strengthening"], "الفقرات هي السبب الأساسي والضلوع بتتبعها."),
   ("The upper ribs should be mobilized:", ["Cranially during inspiration", "Caudally during expiration", "Antero-medially", "Not mobilized"], ""),
   ("The diaphragm in this patient is likely:", ["Ascending and shortened → needs release", "Descending and weak → needs strengthening", "Normal", "Paralyzed"], ""),
   ("Muscles that need stretching in this patient are:", ["Pectorals", "Rhomboids", "Middle trapezius", "Deep neck flexors"], "دي upper crossed، والـ pectorals tight."),
 ]),
 ("A 65-year-old smoker with emphysema has an increased AP chest diameter. Rib assessment shows upper ribs cranial and lower ribs postero-lateral, with the diaphragm low and flat.", [
   ("The chest deformity is:", ["Barrel chest", "Pectus excavatum", "Pectus carinatum", "Kyphosis"], ""),
   ("This is considered a(n):", ["Inhalation lesion", "Expiration lesion", "Flexion lesion", "Group lesion"], ""),
   ("The primary cause here is:", ["The ribs (then the vertebrae follow)", "The vertebrae (then the ribs follow)", "The pelvis", "The cervical spine"], ""),
   ("First line of treatment:", ["Exhalation rib mobilization", "Thoracic extension mobilization", "Inhalation rib mobilization", "Manipulation of L4"], ""),
   ("The diaphragm should be:", ["Strengthened (it is chronically stretched and weak)", "Released (it is shortened)", "Stretched further", "Ignored"], ""),
   ("The costochondral joints need:", ["Approximation to increase stability", "Distraction", "Manipulation", "Release of fascia"], ""),
 ]),
 ("A 30-year-old female presents with neck pain after a car accident. Before starting manual therapy, the therapist performs a test: patient supine, head in hyperextension, rotation and ipsilateral side bending for 45 seconds. The patient develops dizziness and nystagmus.", [
   ("The test performed is:", ["De Kleyn test", "Spurling test", "Hypermobility test", "Slump test"], ""),
   ("The test assesses:", ["Vertebrobasilar insufficiency", "Nerve root compression", "Atlas hypermobility", "Disc herniation"], ""),
   ("The result means:", ["Mobilization and manipulation are contraindicated", "Grade IV mobilization is safe", "Manipulation is the first line", "Mulligan NAGs are indicated with thrust"], ""),
 ]),
 ("A patient with neck pain is tested sitting: the therapist applies axial compression with the neck in extension and ipsilateral rotation and side bending. Pain is reproduced locally.", [
   ("This is the:", ["Spurling (cervical compression) test", "De Kleyn test", "Hypermobility test", "Distraction test"], ""),
   ("Local pain on compression in extension indicates:", ["Intra-articular (facet) problem", "Vertebral artery insufficiency", "Ligament laxity", "Disc problem only"], ""),
   ("To test the intervertebral discs, compression is applied with the head in:", ["Flexion", "Extension", "Rotation", "Side bending"], ""),
 ]),
 ("A child with Down's syndrome is referred for neck exercises. The therapist fixes the axis and moves the atlas laterally; the motion exceeds 3 mm.", [
   ("The test is the:", ["Hypermobility (instability) test", "De Kleyn test", "Spurling test", "Rule of threes"], ""),
   ("The finding indicates:", ["Hypermobile OAA segment due to ligamentous laxity", "Normal motion", "Facet arthritis", "Disc bulge"], ""),
   ("Mobilization and manipulation in this case are:", ["Contraindicated", "Indicated as first line", "Indicated with grade V", "Indicated with self manipulation"], ""),
 ]),
 ("On assessment of a patient with neck pain, the therapist finds limited left rotation, a prominent right transverse process at C4, and pain on PAUM.", [
   ("The lesion is a:", ["Right rotation lesion", "Left rotation lesion", "Flexion lesion", "Left side bending lesion"], "Right rotation lesion = left rotation limitation."),
   ("To mobilize using Maitland, pressure is applied on the:", ["Right transverse process (opposite to the limitation)", "Left transverse process", "Spinous process centrally", "Occiput"], "Maitland على الجنب العكسي للـ limitation."),
   ("Using Mulligan, the glide would be applied on the:", ["Left side (same side of the limitation) in a cranial direction", "Right side in a caudal direction", "Spinous process caudally", "Occiput with thrust"], ""),
 ]),
 ("A 25-year-old athlete has an acute painful limitation of cervical rotation after a minor strain. The therapist applies a sustained cranial glide on the facet while the patient actively rotates to end range, then adds pain-free overpressure. Rotation improves immediately.", [
   ("This technique is:", ["SNAGs (Mulligan)", "Maitland grade IV", "HVLAT manipulation", "NAGs"], "فيه active movement فده SNAGs، والـ NAGs مفيهاش active."),
   ("The immediate improvement satisfies which part of the PILL response?", ["Instant result", "Long lasting", "Pain free", "None"], ""),
   ("If the patient felt pain during the technique, the therapist should:", ["Change the plane / grade / segment — the technique must be pain free", "Increase the force", "Add a thrust", "Continue for 10 sets"], ""),
   ("To continue at home, the patient can be taught:", ["Self SNAGs using a towel", "Self manipulation", "Grade IV oscillations", "Bracing"], ""),
 ]),
 ("A 35-year-old with chronic low back stiffness at L4 shows F-SB-R to the same side on assessment. Mobilization did not improve the limitation; there is a bony block end feel. There are no contraindications.", [
   ("The lesion at L4 must be:", ["Non-neutral (monolytic) lesion", "Neutral group lesion", "Visceral lesion", "Inhalation lesion"], "تحت L2 مفيش neutral lesion."),
   ("The first line of treatment is:", ["Manipulation", "Visceral release", "Grade I mobilization", "Bracing"], ""),
   ("In this flexion lesion, the thrust should be directed towards:", ["Rotation", "Side bending", "Flexion", "Traction"], ""),
   ("Before applying the thrust, the therapist must first:", ["Exclude contraindications and obtain informed consent", "Apply the thrust quickly", "Make the patient anxious", "Perform self manipulation"], ""),
 ]),
 ("A 28-year-old female with low back pain stands with anterior pelvic tilt and increased lumbar lordosis. She has weak abdominals and gluteals with tight hip flexors.", [
   ("This posture fits:", ["Lower crossed syndrome", "Upper crossed syndrome", "Thoracic kyphosis", "Flat back"], ""),
   ("Tight muscles to be stretched include:", ["Iliopsoas, rectus femoris and thoracolumbar erector spinae", "Abdominals and gluteals", "Hamstrings only", "Deep neck flexors"], ""),
   ("Muscles to be strengthened include:", ["Abdominals and gluteals", "Erector spinae", "Iliopsoas", "Rectus femoris"], ""),
 ]),
 ("A 15-year-old girl has a rounded back that corrects when she stands straight. She complains of back fatigue and pain. X-ray shows a thoracic curve of 50° with normal vertebrae.", [
   ("The most likely type is:", ["Postural kyphosis", "Scheuermann's kyphosis", "Congenital kyphosis", "Scoliosis"], "Postural: الأكثر شيوعًا، في البنات المراهقات، والفقرات طبيعية."),
   ("The curve is considered:", ["Hyperkyphosis (> 40°)", "Normal kyphosis", "Hypokyphosis", "Lordosis"], ""),
   ("A tool to measure her kyphosis clinically is:", ["Debrunner kyphometer on C7 and T12", "Plumb line", "Goniometer on the hip", "Spirometer"], ""),
   ("Bracing for her is indicated only if:", ["The kyphosis is no longer reversible through exercises", "Her curve is 50° regardless of exercise response", "She refuses exercises", "Always as a first line"], ""),
 ]),
 ("A 60-year-old woman with osteoporosis and long-term corticosteroid use has thoracic stiffness. The student suggests a thoracic HVLA thrust.", [
   ("Manipulation in this patient is:", ["Contraindicated (bone weakness)", "The first line", "Indicated with high force", "Indicated only with self manipulation"], ""),
   ("For Mulligan, osteoporosis is a:", ["Red flag (absolute contraindication)", "Green flag", "Yellow flag", "Not relevant"], ""),
   ("The safer option to improve her thoracic mobility is:", ["Gentle mobilization and exercises within safe limits", "Rotation manipulation", "Self manipulation", "Grade V thrust"], ""),
 ]),
]

# ---- Written cases (case text, question, model answer html)
CASES_WRITTEN = [
 ("A 40-year-old computer programmer presents with neck and upper back pain, forward head and round shoulders.",
  "Name the syndrome, mention the tight and weak muscles, and outline the treatment.",
  """<p><b>Upper crossed syndrome.</b> Tight: upper trapezius، levator scapulae، pectorals (+ suboccipitals). Weak: deep neck flexors، rhomboids، serratus anterior، middle و lower trapezius.</p>
<p>Treatment: stretch للـ tight (pectorals، upper trap، levator، suboccipitals)، تقوية الـ weak (chin-in للـ deep neck flexors، scapular retraction للـ rhomboids و middle/lower trap)، thoracic extension mobilization، inhalation rib mobilization و sternal release، و postural training (يغير وضعه كل نص ساعة، ويظبط مكتبه).</p>"""),
 ("A patient with a neutral group lesion of the mid-thoracic spine complains of chronic constipation.",
  "What is the first line of treatment and why?",
  """<p><b>Visceral release</b>، لأن الـ group (neutral) lesion ليه علاقة بالـ sympathetic chain (viscero-somatic relation)، فالمشكلة الحشوية المزمنة ممكن تعمل الـ lesion. لو عالجت الفقرات من غير ما تعالج الأحشاء المشكلة هترجع.</p>"""),
 ("Assessment of T5 reveals extension, right side bending and right rotation (non-neutral).",
  "Name the lesion type and its first line of treatment, and where to direct the thrust.",
  """<p>Non-neutral (<b>monolytic</b>) lesion حسب Fryette's 2nd law، والـ first line هو <b>manipulation</b>. ولأنه <b>extension lesion</b> (ESbR) فالـ thrust يكون في اتجاه الـ <b>side bending</b>. (في الـ flexion lesion الـ thrust على الـ rotation)</p>"""),
 ("A patient complains of radiating arm pain. A safety test performed in sitting reproduces the radiating symptoms.",
  "Name the test, describe it, and state the interpretation.",
  """<p><b>Spurling (cervical compression) test</b>: المريض قاعد، والمعالج وراه وإيديه على راسه، وبيعمل compression في الـ extension (أو extension + ipsilateral rotation و side bending)، فالـ facets تتضغط لأقصى حد. الألم الموضعي معناه intra-articular problem، والـ radiating معناه nerve root compression. لو اتعمل في الـ flexion بيختبر الـ discs. وفي الـ acute disc bulge الـ mobilization والـ manipulation contraindicated.</p>"""),
]

# ---- True / False drill: (statement, correct_index (0 True, 1 False), explanation)
TF_DRILL = [
 ("In ideal posture the line of gravity passes posterior to the knee joint.", 1, "Slightly anterior لمنتصف الركبة."),
 ("Primary curves of the spine are convex posteriorly.", 0, "Thoracic و sacral."),
 ("Scoliosis is best seen from the lateral view.", 1, "من الـ posterior view."),
 ("In upper crossed syndrome the deep neck flexors are tight.", 1, "Weak (inhibited)."),
 ("In lower crossed syndrome the gluteals are weak.", 0, ""),
 ("A chronically elongated muscle loses sarcomeres.", 1, "بيزود sarcomeres والـ curve بيتحرك لليمين."),
 ("Maitland mobilization requires active participation of the patient.", 1, "Static و passive."),
 ("Segmental assessment determines the level of the lesion.", 0, ""),
 ("PAUM is used to assess and enhance rotation.", 0, ""),
 ("APUM is applied in prone lying.", 1, "Supine، لما المريض مش قادر ينام prone."),
 ("Grade IV is a small amplitude movement into the barrier.", 0, ""),
 ("About 50% of cervical rotation occurs at the occiput–C1 level.", 1, "عند C1–C2. الـ flexion-extension هو اللي عند occiput–C1."),
 ("Cervical facets are oriented at 45° to the transverse plane.", 0, ""),
 ("De Kleyn test is a neural compression test.", 1, "Vascular (VBI)."),
 ("A motion of more than 3 mm in the hypermobility test indicates a hypermobile segment.", 0, ""),
 ("In neutral mechanics, side bending is accompanied by rotation to the same side.", 1, "للناحية العكسية (1st law)."),
 ("Below L2 there is no neutral (group) lesion.", 0, ""),
 ("The first line of treatment of a monolytic lesion is visceral release.", 1, "Manipulation. الـ visceral release للـ group lesion."),
 ("Kyphosis is a flexion lesion with expiration lesion.", 0, ""),
 ("In barrel chest the diaphragm is shortened and needs release.", 1, "Descending و weak ومحتاج تقوية."),
 ("Upper ribs move in a bucket-handle manner.", 1, "Pump-handle. الـ lower ribs هي bucket-handle."),
 ("Mulligan's glide in the spine is always cranial.", 0, ""),
 ("Mulligan techniques are applied on the opposite side of the limitation.", 1, "نفس الجنب. الـ Maitland هو اللي على العكسي."),
 ("NAGs require active movement of the patient.", 1, "SNAGs هي اللي فيها active movement."),
 ("Osteopenia is a yellow flag for Mulligan.", 0, "Relative contraindication."),
 ("The audible pop is the therapeutic goal of manipulation.", 1, ""),
 ("Manipulation takes the joint beyond its anatomical limit.", 1, "للـ paraphysiological space بس."),
 ("Rotation manipulation is contraindicated at the OA joint.", 0, ""),
 ("Pregnancy is an absolute contraindication to manipulation.", 1, "Relative."),
 ("Postural kyphosis is the least common type.", 1, "الأكثر شيوعًا. الـ congenital هو الأقل."),
 ("Hyperkyphosis is a thoracic curve over 40°.", 0, ""),
 ("Passive bracing without physical therapy has no effect on the thoracic spine.", 0, ""),
 ("The Milwaukee brace is worn 8 hours a day for 3 months.", 1, "23 ساعة في اليوم لمدة 1–2 سنة."),
]
