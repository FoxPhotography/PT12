# Radiology & Imaging (Dr. Rania Youssef Mehanna) — midterm data
# Tab: (id, title, short, icon, source, summary_html, groups); question: (text, [correct, ...], tag, expl)

# ---- PT12 midterm (Google form, 15 Qs) — answers as provided by the batch. (text, options, correct_idx, expl)
TF = ["True ✓", "False ✗"]
PT12 = [
 ("The most common type of bronchiectasis is", ["Cylindrical", "Varicosed", "Cystic", "Centrilobular"], 0, "الـ Cylindrical هو الأشهر والأخف. والـ centrilobular ده نوع emphysema مش bronchiectasis."),
 ("The echo-free lesion on ultrasound denoting that ultrasound waves are transmitted", TF, 0, "الموجات اللي بتعدي (transmitted) بتعمل echo-free area زي السوائل (ascites، bile، cysts)."),
 ("Sternal bowing in chest x-ray lateral view is a sign of", ["Pleural effusion", "Pneumonia", "Emphysema", "Bronchiectasis"], 2, "من علامات الـ hyperinflation في الـ emphysema، ومعاها increased retrosternal airspace."),
 ("The mineral density on x-ray is black", TF, 1, "الـ mineral (bone/calcium) أبيض radio-opaque. الأسود هو الهوا (gas)."),
 ("The right lung formed of", ["Upper lobe and lower lobe", "Upper lobe, lingula and lower lobe", "Upper lobe only", "Upper lobe, middle lobe and lower lobe"], 3, "الشمال: upper و lingula و lower."),
 ("Ghon's focus is a sign for post-primary TB", TF, 1, "الـ Ghon's focus ده الـ initial focus في الـ primary TB."),
 ("The air bronchogram in CT chest is a sign for", ["Bronchiectasis", "Lung abscess", "Pneumonia", "Pleural effusion"], 2, "Bronchus مليان هوا جوه lobe متكثف (consolidation)."),
 ("The chronic bronchiectasis associated with emphysema diagnosed as", ["T.B", "COPD", "COVID-19", "Heart failure"], 1, "الـ COPD = chronic bronchitis (small airways disease) + emphysema."),
 ("The double density sign in x-ray chest denoting right atrium enlargement", TF, 1, "ده sign للـ left atrial enlargement."),
 ("The postero-anterior view in x-ray chest the x-ray tube is posterior to the patient", TF, 0, "في الـ PA الأشعة بتدخل من ورا وتطلع من قدام، والـ film قدام الصدر."),
 ("The bronchiectasis defined as abnormal reversible dilation of the bronchial tree", TF, 1, "Irreversible."),
 ("MRI depend on ionizing radiation", TF, 1, "الـ MRI بيستخدم magnet و radio waves، ومفيهوش ionizing radiation."),
 ("Presence of gas density in pleural space in x-ray chest denoting", ["Hydrothorax", "Pneumothorax", "Hemothorax", "Pleural effusion"], 1, ""),
 ("The most anterior cardiac chamber is", ["Right atrium", "Left atrium", "Right ventricle", "Left ventricle"], 2, "الـ RV retrosternal وبيبان في الـ lateral view. والـ left atrium/ventricle posterior."),
 ("The white object in MRI is described as hyperechoic lesion", TF, 1, "في الـ MRI اسمه high signal intensity (hyperintense). الـ hyperechoic مصطلح الـ ultrasound."),
]

TABS = []
def T(*a): TABS.append(a)

# ================================================================= Lec 1
T("l1", "Lec 1 — Basics of Radiology I: X-ray & CT", "Basics 1", "☢️",
  "داتا المحاضرة الأولى مش موجودة في الملفات، فالملخص ده مبني على أسئلة الميد والأساسيات المعروفة",
"""
<div class="card"><h4>X-ray</h4>
<ul><li>بيعتمد على <b>ionizing radiation</b> (X-rays). الصورة بتطلع حسب امتصاص كل نسيج للأشعة (attenuation).</li>
<li>اللي بيمتص أشعة كتير يطلع <b>أبيض (radio-opaque)</b>، واللي بيعدّي الأشعة يطلع <b>أسود (radiolucent)</b>.</li>
<li>المصطلح المستخدم في الـ X-ray هو <b>density / opacity</b>.</li></ul>
<table><tr><th>Density</th><th>اللون</th></tr>
<tr><td>Air / gas</td><td>أسود (أكتر حاجة radiolucent)</td></tr>
<tr><td>Fat</td><td>رمادي غامق</td></tr>
<tr><td>Soft tissue / fluid (water)</td><td>رمادي</td></tr>
<tr><td>Mineral (bone, calcium)</td><td>أبيض (radio-opaque)</td></tr>
<tr><td>Metal</td><td>أبيض ناصع</td></tr></table></div>

<div class="card"><h4>Chest X-ray views</h4>
<table><tr><th>View</th><th>الوصف</th></tr>
<tr><td>PA (postero-anterior)</td><td>الـ standard. الـ <b>X-ray tube ورا المريض</b> والـ film/detector قدام صدره. المريض واقف وواخد نفس عميق. القلب مش بيتكبر (magnified)</td></tr>
<tr><td>AP (antero-posterior)</td><td>الـ tube قدام المريض. للمرضى في السرير أو الـ portable (زي "AP sitting mobile")، والقلب بيبان أكبر من حجمه</td></tr>
<tr><td>Lateral</td><td>بيبين الحاجات اللي ورا القلب والـ fissures، وفيه بيبان الـ retrosternal space والـ right ventricle</td></tr></table></div>

<div class="card"><h4>CT</h4>
<ul><li>بيستخدم X-rays (ionizing) وبيعمل صور <b>cross-sectional</b> (axial) وممكن reconstruction في كل الـ planes.</li>
<li>المصطلح: <b>density / attenuation</b> (hyperdense و hypodense)، وبتتقاس بالـ Hounsfield units: الهوا −1000، المية 0، العظم حوالي +1000.</li>
<li>فيه <b>windows</b>: lung window و mediastinal window. والـ <b>HRCT</b> أدق حاجة للـ bronchiectasis والـ lung parenchyma. والـ <b>CTPA</b> للـ pulmonary embolism.</li></ul></div>

<div class="card"><h4>مصطلحات كل modality (مهم جدًا للـ T/F)</h4>
<table><tr><th>Modality</th><th>المصطلح</th><th>أبيض / أسود</th></tr>
<tr><td>X-ray</td><td>Density / opacity</td><td>Radio-opaque / radiolucent</td></tr>
<tr><td>CT</td><td>Density (attenuation)</td><td>Hyperdense / hypodense</td></tr>
<tr><td>Ultrasound</td><td><b>Echogenicity</b></td><td>Hyperechoic / hypoechoic / anechoic (echo-free)</td></tr>
<tr><td>MRI</td><td><b>Signal intensity (SI)</b></td><td>High SI (hyperintense) / low SI (hypointense)</td></tr></table></div>
""",
[
 ("X-ray & densities", [
  ("X-ray and CT depend on:", ["Ionizing radiation", "Sound waves", "Magnetic field and radio waves", "Doppler effect"], "imp", ""),
  ("The structure that appears black (most radiolucent) on X-ray is:", ["Air (gas)", "Bone", "Metal", "Soft tissue"], "imp", ""),
  ("Mineral (bone/calcium) density on X-ray appears:", ["White (radio-opaque)", "Black", "Dark grey", "Invisible"], "imp", ""),
  ("Fat density on X-ray appears:", ["Dark grey (between air and soft tissue)", "White", "Brighter than bone", "Same as metal"], "", ""),
  ("A structure that allows X-rays to pass easily is described as:", ["Radiolucent", "Radio-opaque", "Hyperechoic", "Hyperintense"], "", ""),
  ("In the PA view, the X-ray tube is:", ["Posterior to the patient", "Anterior to the patient", "Lateral to the patient", "Above the patient"], "imp", ""),
  ("The AP chest view is commonly used for:", ["Bedridden / portable patients", "Standard outpatient chest X-ray", "MRI patients", "Ultrasound guidance"], "", ""),
  ("The heart appears magnified in the:", ["AP view", "PA view", "Lateral view only", "MRI"], "", ""),
 ]),
 ("CT & terminology", [
  ("CT images are:", ["Cross-sectional images produced by X-rays", "Images produced by sound waves", "Images produced by magnetic field", "Plain 2D projection only"], "", ""),
  ("On CT, the density of water is about:", ["0 HU", "−1000 HU", "+1000 HU", "+500 HU"], "", "الهوا −1000 والعظم حوالي +1000."),
  ("The term used to describe brightness in ultrasound is:", ["Echogenicity", "Signal intensity", "Density", "Opacity"], "imp", ""),
  ("The term used to describe brightness in MRI is:", ["Signal intensity", "Echogenicity", "Hounsfield density", "Radiolucency"], "imp", ""),
  ("A white object in MRI is described as:", ["High signal intensity (hyperintense)", "Hyperechoic", "Radio-opaque", "Hyperdense"], "imp", ""),
  ("A white object on CT is described as:", ["Hyperdense", "Hyperechoic", "Hyperintense", "Anechoic"], "", ""),
 ]),
])

# ================================================================= Lec 2
T("l2", "Lec 2 — Basics of Radiology II: Ultrasound & MRI", "Basics 2", "🔊",
  "Basics for radiology part 2 (د. رانيا)",
"""
<div class="card"><h4>Ultrasound (US)</h4>
<ul><li>Imaging technology بتستخدم <b>high-frequency sound waves</b> عشان توصف الـ tissue. الـ transducer بيبعت ultrasound pulse وبيستقبل الـ <b>echoes</b> اللي راجعة، وفيها spatial و contrast information. الفكرة شبه الـ <b>sonar</b>.</li>
<li>بيطلع صورة 2D grayscale بتتحرك (real time). المصطلح هو <b>echogenicity</b>.</li></ul>
<table><tr><th>الموجة</th><th>النتيجة</th></tr>
<tr><td>Scattered</td><td>مش بتساعد في الصورة</td></tr>
<tr><td>Transmitted</td><td><b>Echo-free (anechoic)</b> area: سوايل زي ascites و bile و serous fluid في الـ cysts، وبتطلع سودا</td></tr>
<tr><td>Reflected</td><td>بتعمل density من رمادي لأبيض. مثلًا الـ pancreas بيعكس أكتر (أبيض أكتر) من الـ liver</td></tr></table>
<ul><li><b>Safety</b>: آمن (لا radiation ولا electromagnetic field)، وآمن في الحمل والـ neonates.</li>
<li><b>Advantages</b>: من أكتر الـ modalities المتاحة، رخيص، no radiation hazards، real time.</li>
<li><b>Disadvantages</b>: <b>operator dependent</b>، ومحتاج تعاون المريض.</li>
<li><b>Color Doppler</b>: بيكشف ويقيس الـ blood flow، ومعتمد على الـ <b>Doppler effect</b> (تغيّر الـ frequency بسبب حركة الـ reflector، وهو الدم).</li>
<li>في الـ pleural effusion الـ US بيكشف كميات صغيرة جدًا (3–5 mL) وبيوجّه الـ thoracocentesis.</li></ul></div>

<div class="card"><h4>MRI</h4>
<ul><li>الـ <b>Hydrogen (H⁺)</b> حوالي 9.5% من جسم الإنسان، وهو أبسط عنصر (atomic number و weight = 1). وهو في الـ ionic state يبقى proton بس، والـ proton positively charged وليه <b>magnetic spin</b>، والـ MRI بيستغل الـ spin ده.</li>
<li>الجهاز: <b>magnet</b> كبير وقوي المريض بينام جواه، و<b>radio wave antenna</b> بتبعت signals للجسم وتستقبلها، والكمبيوتر يحولها لصور. فيه closed و open.</li>
<li>بيصور أي جزء في <b>أي plane</b>. المصطلح: <b>signal intensity (SI)</b>.</li>
<li>ممتاز في كشف الـ <b>water</b> (أغلب الـ pathology فيها edema أو مية).</li>
<li>الـ sequences الأساسية: <b>T1</b> و <b>T2</b>.</li></ul>
<table><tr><th></th><th>Black</th><th>High SI (white)</th></tr>
<tr><td>T1</td><td>air، calcium، cortical bone، rapidly flowing blood. والـ fluid low SI</td><td><b>fat</b>، blood، gadolinium (contrast)، melanin، protein</td></tr>
<tr><td>T2</td><td>air، calcium، cortical bone، rapidly flowing blood</td><td><b>fluid</b>، CSF، bladder، bile/gallbladder، kidneys</td></tr></table>
<p class="key">باختصار: الـ <b>fluid/CSF أسود في T1 وأبيض في T2</b>، والـ fat أبيض في T1.</p>
<table><tr><th>Advantages of MRI</th><th>Disadvantages of MRI</th></tr>
<tr><td>No ionizing X-rays<br>Multiple planes (axial، sagittal، coronal، oblique)<br>Superior soft tissue contrast<br>Angiography من غير contrast أحيانًا<br>Diffusion، spectroscopy، perfusion<br>Functional MRI للمخ</td>
<td>أغلى من الـ CT<br>أبطأ بكتير، فراحة المريض مشكلة<br>صوته عالي (noisy)<br>Claustrophobia<br>Artifacts خاصة بيه<br><b>مش آمن</b> مع الـ pacemakers وبعض الـ metal implants والـ foreign bodies</td></tr></table></div>
""",
[
 ("Ultrasound", [
  ("Ultrasound imaging uses:", ["High-frequency sound waves", "Ionizing radiation", "Magnetic field", "Gamma rays"], "imp", ""),
  ("The term used in ultrasound is:", ["Echogenicity", "Signal intensity", "Density", "Attenuation"], "imp", ""),
  ("The principle of ultrasound is analogous to:", ["Sonar", "Radar", "Laser", "Magnetism"], "", ""),
  ("Ultrasound waves that are transmitted produce:", ["Echo-free (anechoic) areas", "White areas", "Scattered artifacts", "Hyperechoic lesions"], "imp", ""),
  ("Echo-free areas on ultrasound are seen with:", ["Fluids such as ascites, bile and cyst fluid", "Bone", "Air in lungs", "Calcified stones"], "", ""),
  ("Reflected ultrasound waves create:", ["Density from grey to white", "Echo-free black areas", "No image", "Artifacts only"], "", ""),
  ("Scattered ultrasound waves:", ["Do not help to create the image", "Create white areas", "Create black areas", "Measure blood flow"], "", ""),
  ("The pancreas compared to the liver on ultrasound appears:", ["Whiter (reflects more)", "Darker", "Echo-free", "Identical"], "", ""),
  ("Ultrasound is safe in pregnancy because it has:", ["No radiation and no electromagnetic field", "Low dose radiation", "Strong magnetic field", "Contrast media"], "imp", ""),
  ("The main disadvantage of ultrasound is that it is:", ["Operator dependent and needs patient cooperation", "Expensive", "Uses ionizing radiation", "Not real time"], "imp", ""),
  ("Advantages of ultrasound include all EXCEPT:", ["Operator independent", "Cheap", "Real time", "No radiation hazards"], "", ""),
  ("Color Doppler ultrasound is used to:", ["Detect and measure blood flow", "Measure bone density", "Image the brain", "Detect air in pleura"], "imp", ""),
  ("The Doppler effect is:", ["Change in wave frequency due to motion of the reflector (blood)", "Absorption of X-rays by bone", "Magnetic spin of protons", "Reflection from air"], "", ""),
 ]),
 ("MRI", [
  ("MRI depends on:", ["Magnetic field and radio waves (proton spin)", "Ionizing radiation", "Sound waves", "Gamma rays"], "imp", ""),
  ("Hydrogen forms about …… of the human body:", ["9.5%", "50%", "1%", "25%"], "", ""),
  ("MRI utilizes the …… of the proton:", ["Magnetic spin", "Negative charge", "Atomic weight of 16", "Radioactivity"], "", ""),
  ("The term used in MRI is:", ["Signal intensity", "Echogenicity", "Hounsfield unit", "Radiolucency"], "imp", ""),
  ("The main MRI sequences are:", ["T1 and T2", "PA and AP", "Axial and lateral", "B-mode and M-mode"], "", ""),
  ("On T2-weighted images, fluid and CSF appear:", ["White (high SI)", "Black", "Intermediate", "Invisible"], "imp", ""),
  ("On T1-weighted images, fat appears:", ["White (high SI)", "Black", "Low SI", "Invisible"], "imp", ""),
  ("On T1-weighted images, fluid appears:", ["Low signal (dark)", "High signal", "Same as fat", "Brightest"], "", ""),
  ("In both T1 and T2, air, calcium and cortical bone appear:", ["Black", "White", "Intermediate", "Bright"], "", ""),
  ("MRI is excellent in detecting:", ["Water (edema) in pathological conditions", "Bone fractures only", "Air in lungs", "Calcification"], "", ""),
  ("Advantages of MRI include all EXCEPT:", ["Faster and cheaper than CT", "No ionizing X-rays", "Multiple planes", "Superior soft tissue contrast"], "imp", "الـ MRI أغلى وأبطأ من الـ CT."),
  ("MRI is NOT safe for patients with:", ["Artificial pacemakers and some metal implants", "Pregnancy in all cases", "Fractures", "Asthma"], "imp", ""),
  ("Disadvantages of MRI include:", ["Noise, claustrophobia, long time and high cost", "Ionizing radiation", "Single plane imaging", "Poor soft tissue contrast"], "", ""),
  ("Gadolinium (contrast) on T1 appears:", ["High signal (white)", "Black", "Low signal", "Not visible"], "", ""),
 ]),
])

# ================================================================= Lec 3
T("l3", "Lec 3 — Chest Imaging I: Normal Anatomy & Pleural Diseases", "Chest 1", "🫁",
  "Chest imaging part 1 (د. رانيا)",
"""
<div class="card"><h4>Normal anatomy</h4>
<ul><li>الـ <b>pleural cavity</b>: visceral pleura (على الرئة) و parietal pleura (على اللي حواليها). الـ pleurae <b>مش بتبان</b> في الـ chest X-ray الطبيعي.</li>
<li>الـ lobes بتفصلها الـ <b>interlobar fissures</b> (مكان ما الـ visceral pleurae بتلمس بعض). الـ visceral pleura رفيعة جدًا (أقل من 1 mm) وبتبان بس لو thickened أو الأشعة جت عليها tangentially.</li>
<li><b>Major fissure</b>: بتفصل الـ upper عن الـ lower lobe في الناحيتين. في الـ lateral بتنزل من T4/T5 قدام وتحت لحد الـ diaphragm. و<b>مش بتبان في الـ AP</b>.</li>
<li><b>Minor fissure</b> (يمين بس): horizontal، وبتعمل الـ middle lobe، و<b>بتبان في الـ AP والـ lateral</b>.</li>
<li>عشان تفرق الـ major fissure الشمال من اليمين في الـ lateral: الشمال بتنتهي على الـ left hemidiaphragm اللي غالبًا أوطى، والـ <b>air bubble في المعدة</b> علامة للـ left hemidiaphragm.</li>
<li><b>Right lung</b>: upper و middle و lower. <b>Left lung</b>: upper و <b>lingula</b> و lower.</li></ul></div>

<div class="card"><h4>القلب والـ hila</h4>
<ul><li>القلب <b>retrosternal</b> ومايل للشمال، والـ tip للشمال، وبيبقى rotated شوية. الـ left ventricle والـ left atrium <b>posterior</b>.</li>
<li>في الـ <b>PA</b>: بيبان contour الـ <b>right atrium</b> (يمين) والـ <b>left ventricle</b> (شمال).</li>
<li>الـ <b>right ventricle</b> بيبان في الـ <b>lateral</b> لأنه central و anterior retrosternal، وهو أكتر chamber قدام.</li>
<li>Contours الـ hila معظمها من الـ <b>pulmonary arteries</b>.</li>
<li>في أكتر من <b>90%</b> من الناس الـ <b>left hilum أعلى</b> من اليمين: الـ left pulmonary artery بتعدي فوق الـ left main bronchus، والـ right pulmonary artery تحت الـ right main bronchus. ساعات بيبقوا على نفس المستوى، لكن لو اليمين أعلى غالبًا pathological (أو بعد عملية).</li>
<li>في الـ lateral: الـ right anterior pulmonary artery قدام الـ trachea، والـ left pulmonary artery ورا الـ trachea.</li></ul></div>

<div class="card"><h4>Pleural effusion</h4>
<p>Abnormal accumulation of fluid في الـ pleural space، لأن أي pathology غلبت قدرة الـ pleura على امتصاص السوائل.</p>
<ul><li><b>X-ray</b>: <b>blunting of the costophrenic angle</b>، و blunting of the cardiophrenic angle، و fluid في الـ fissures. مع الكميات الكبيرة الـ mediastinum بيعمل shift <b>بعيد</b> عن الـ effusion، ولو معاه collapse غالب ممكن يعمل shift ناحيته. الـ X-ray بيكشف أكتر من <b>50 mL</b>.</li>
<li><b>CT</b>: ممتاز في الكميات الصغيرة، وبيحدد السبب (malignant deposits، lung neoplasm) وكمان المشاكل تحت الـ diaphragm (subdiaphragmatic abscess).</li>
<li><b>Ultrasound</b>: بيكشف loculated fluid لحد <b>3–5 mL</b>، ويفرق بين loculated fluid و thickened pleura، وبيوجّه الـ <b>thoracocentesis</b>.</li></ul></div>

<div class="card"><h4>Pneumothorax</h4>
<p>Presence of <b>gas (air)</b> في الـ pleural space. لو بيكبر باستمرار بيضغط على الـ mediastinum وممكن يبقى life threatening.</p>
<ul><li><b>X-ray</b>: الـ visceral pleural edge بيبان <b>خط أبيض رفيع وحاد</b>، ومفيش <b>lung markings</b> برة الخط ده، والمسافة دي radiolucent (أسود) مقارنة بالرئة. الرئة ممكن تعمل complete collapse. الـ mediastinum <b>مش بيعمل shift</b> بعيد عن الـ pneumothorax إلا لو <b>tension pneumothorax</b>. وممكن يبقى معاه subcutaneous emphysema و pneumomediastinum.</li>
<li><b>CT (lung window)</b>: بيبان بسهولة جدًا. ولو فيه bullous disease ممكن loculated pneumothorax يتلخبط معاه.</li></ul></div>
""",
[
 ("Normal anatomy", [
  ("On a normal chest X-ray, the pleurae are:", ["Invisible", "Clearly seen as thick white lines", "Seen only on the left", "Black lines"], "imp", ""),
  ("The visceral pleura is visible only when:", ["Thickened or hit tangentially by the X-ray beam", "The patient is standing", "On every PA film", "Contrast is used"], "", ""),
  ("The major fissure separates:", ["Upper lobe from lower lobe", "Upper lobe from middle lobe only", "Right lung from left lung", "Lingula from lower lobe"], "", ""),
  ("The major fissures on the AP image are:", ["Invisible", "Clearly visible", "Seen only on the right", "Seen as air"], "imp", ""),
  ("The minor fissure:", ["Is on the right, creates the middle lobe and is seen on AP and lateral images", "Is on the left and creates the lingula", "Is invisible on all images", "Separates both lungs"], "imp", ""),
  ("The right lung is formed of:", ["Upper, middle and lower lobes", "Upper lobe, lingula and lower lobe", "Upper and lower lobes only", "Middle lobe only"], "imp", ""),
  ("The left lung is formed of:", ["Upper lobe, lingula and lower lobe", "Upper, middle and lower lobes", "Upper lobe only", "Middle and lower lobes"], "", ""),
  ("A reference point for the left hemidiaphragm on the lateral image is:", ["The air bubble in the stomach", "The liver", "The trachea", "The sternum"], "", ""),
  ("On the PA view, the cardiac contours visible are:", ["Right atrium and left ventricle", "Right ventricle and left atrium", "Right ventricle only", "Left atrium only"], "imp", ""),
  ("The right ventricle contour is visible on the:", ["Lateral image (anterior retrosternal)", "PA image right border", "PA image left border", "It is never visible"], "imp", ""),
  ("The most anterior cardiac chamber is the:", ["Right ventricle", "Left ventricle", "Left atrium", "Right atrium"], "imp", ""),
  ("The contours of the hila are mostly created by the:", ["Pulmonary arteries", "Main bronchi", "Lymph nodes", "Pulmonary veins only"], "", ""),
  ("In more than 90% of people:", ["The left hilum is higher than the right", "The right hilum is higher", "Both hila are absent", "The hila are at the level of the diaphragm"], "imp", ""),
  ("A higher right hilum than left is usually:", ["Pathological or postoperative", "Normal in most people", "Seen in children only", "Due to breathing"], "", ""),
 ]),
 ("Pleural diseases", [
  ("Blunting of the costophrenic angle on X-ray indicates:", ["Pleural effusion", "Pneumothorax", "Pneumonia", "Emphysema"], "imp", ""),
  ("With a large pleural effusion, the mediastinum shifts:", ["Away from the effusion", "Towards the effusion always", "It never shifts", "Upwards"], "imp", ""),
  ("Plain X-ray can detect pleural fluid volumes above:", ["50 mL", "3–5 mL", "500 mL", "1 mL"], "imp", ""),
  ("Ultrasound can detect pleural fluid as small as:", ["3–5 mL", "50 mL", "200 mL", "1 liter"], "imp", ""),
  ("The best modality to guide thoracocentesis and differentiate loculated fluid from thickened pleura is:", ["Ultrasound", "Plain X-ray", "MRI", "Nuclear scan"], "", ""),
  ("The modality that also identifies subdiaphragmatic causes of pleural effusion is:", ["CT", "Plain X-ray", "Doppler", "Fluoroscopy"], "", ""),
  ("Pneumothorax is the presence of …… in the pleural space:", ["Gas (air)", "Fluid", "Blood", "Pus"], "imp", ""),
  ("On X-ray, pneumothorax shows:", ["Thin sharp white visceral pleural line with no lung markings peripheral to it", "Blunted costophrenic angle", "Air bronchogram", "Double density sign"], "imp", ""),
  ("The mediastinum shifts away from a pneumothorax only in:", ["Tension pneumothorax", "Every pneumothorax", "Small pneumothorax", "Bilateral effusion"], "imp", ""),
  ("A loculated pneumothorax on CT may be confused with:", ["Bullous disease", "Pleural effusion", "Pneumonia", "Pericardial effusion"], "", ""),
 ]),
])

# ================================================================= Lec 4
T("l4", "Lec 4 — Chest Imaging II: Pneumonia, Abscess, TB & COVID-19", "Chest 2", "🦠",
  "Chest imaging part 2 (د. رانيا)",
"""
<div class="card"><h4>Lobar pneumonia</h4>
<p>(Non-segmental / focal non-segmental pneumonia) = homogeneous و fibrinosuppurative <b>consolidation</b> في lobe أو أكتر نتيجة bacterial pneumonia.</p>
<ul><li><b>X-ray</b>: homogeneous opacification في lobar pattern، وممكن تبقى sharply defined عند الـ fissures (والأكتر segmental consolidation). الـ bronchus اللي مش متكثف جوه الـ lobe بيعمل <b>air bronchogram</b>. والـ consolidation <b>مش معاه volume loss</b> (لكن ممكن atelectasis مع small airway obstruction).</li>
<li><b>CT</b>: focal dense opacification لمعظم الـ lobe مع sparing للـ large airways، وممكن ground-glass opacity جنبها.</li></ul></div>

<div class="card"><h4>Lung abscess</h4>
<ul><li><b>Cavitating infective consolidation</b>، single أو multiple. البكتيريا (Staph aureus، Klebsiella، Proteus، Pseudomonas، TB، anaerobes) أو fungi.</li>
<li>أكتر مكان: <b>apicoposterior</b> segment في الـ upper lobes، أو الـ apical segment في الـ lower lobe.</li>
<li><b>X-ray</b>: cavitating spherical consolidation غالبًا أكبر من <b>2 cm</b> (لحد 12 cm)، فيها <b>air-fluid level</b>، وأبعادها تقريبًا متساوية في الـ frontal والـ lateral. الـ wall <b>thick و irregular</b>، ولو لامس الـ pleura بيعمل <b>acute angles</b>.</li>
<li><b>DD</b>: broncho-pleural fistula، empyema، lung neoplasms (squamous cell carcinoma)، TB (reactivation).</li></ul></div>

<div class="card"><h4>Tuberculosis</h4>
<table><tr><th>Primary TB</th><th>Post-primary (secondary) TB</th></tr>
<tr><td>Initial focus = <b>Ghon's focus</b> (consolidation of tubercles في الـ upper zones) + lymphadenitis + lymphangitis</td>
<td>بييجي بعد سنين مع ضعف المناعة. في الـ <b>posterior segments of upper lobes</b> أو الـ <b>superior segments of lower lobes</b>. Patchy consolidation أو nodular/linear opacities، و<b>بيعمل cavitation أكتر</b>، وممكن miliary (nodules 2–4 mm)</td></tr></table>
<ul><li><b>Complications</b>: fungal colonization للـ cavity (<b>aspergilloma</b>)، bronchiectasis، tuberculous empyema، fibrothorax.</li>
<li><b>X-ray</b>: infiltration مع pleural effusion (كبار السن)، <b>miliary pattern</b> (small dense nodules منتشرة في الـ immunocompromised)، calcifications (بعد الشفا)، Ghon's focus calcified، و <b>Ranke's complex</b> (calcified focus + calcified hilar LN).</li></ul></div>

<div class="card"><h4>COVID-19</h4>
<ul><li>سببه SARS-CoV-2. التشخيص الأكيد بالـ <b>RT-PCR</b>، والـ CT <b>مش</b> بيُستخدم للتشخيص، لكنه مفيد في الـ complications.</li>
<li><b>X-ray</b>: طبيعي في الأول أو الحالات البسيطة. Airspace opacities (consolidation أو GGO)، <b>bilateral، peripheral، lower zone</b>.</li>
<li><b>CT</b>: <b>GGO</b> (bilateral، subpleural، peripheral)، <b>crazy paving</b> (GGO + septal thickening)، consolidation، bronchovascular thickening، traction bronchiectasis.</li>
<li><b>CO-RADS</b> (درجة الاشتباه): 1 no، 2 low، 3 indeterminate، 4 high، 5 very high (typical)، 6 PCR +ve.</li></ul></div>
""",
[
 ("Pneumonia & abscess", [
  ("Lobar pneumonia appears on X-ray as:", ["Homogeneous opacification in a lobar pattern", "Black area without lung markings", "Ring shadows", "Water bottle heart"], "imp", ""),
  ("Air bronchogram is a sign of:", ["Consolidation (pneumonia)", "Pneumothorax", "Pleural effusion", "Emphysema"], "imp", ""),
  ("Air bronchogram results from:", ["A non-opacified (air-filled) bronchus within a consolidated lobe", "Air in the pleural space", "Air in the pericardium", "Dilated bronchi in bronchiectasis"], "", ""),
  ("Consolidation is usually:", ["Not associated with volume loss", "Always associated with volume loss", "Associated with mediastinal shift away", "Black on X-ray"], "", ""),
  ("Lung abscess is:", ["A cavitating infective consolidation", "Air in pleural space", "Irreversible bronchial dilatation", "Fluid in pericardium"], "imp", ""),
  ("A characteristic X-ray finding of lung abscess is:", ["Air-fluid level in a thick irregular-walled cavity", "Blunted costophrenic angle", "Tram-track sign", "Double density sign"], "imp", ""),
  ("Lung abscess is most common in the:", ["Apicoposterior segment of the upper lobes", "Middle lobe", "Lingula", "Costophrenic angle"], "", ""),
  ("The usual diameter of a lung abscess is more than:", ["2 cm", "2 mm", "20 cm", "50 cm"], "", ""),
  ("A lung abscess abutting the pleura forms:", ["Acute angles", "Obtuse angles", "No angles", "Right angles only"], "", ""),
  ("The differential diagnosis of lung abscess includes all EXCEPT:", ["Pneumothorax", "Empyema", "Squamous cell carcinoma", "TB"], "", ""),
 ]),
 ("TB & COVID-19", [
  ("Ghon's focus is a sign of:", ["Primary TB", "Post-primary TB", "COVID-19", "Lung abscess"], "imp", ""),
  ("Post-primary TB develops in:", ["Posterior segments of upper lobes and superior segments of lower lobes", "Middle lobe only", "Lingula only", "Costophrenic angles"], "imp", ""),
  ("Post-primary TB is more likely to:", ["Cavitate", "Be completely invisible", "Cause water bottle heart", "Cause double density sign"], "", ""),
  ("Miliary TB appears as:", ["Diffuse small (2–4 mm) dense nodules", "A single large cavity", "Blunted costophrenic angle", "Black area without lung markings"], "imp", ""),
  ("Fungal colonization of a TB cavity is called:", ["Aspergilloma", "Ghon's focus", "Ranke's complex", "Empyema"], "", ""),
  ("Ranke's complex is:", ["Calcified focus + calcified hilar lymph node", "Air-fluid level", "Crazy paving", "Tram-track sign"], "", ""),
  ("The definitive diagnosis of COVID-19 requires:", ["Positive RT-PCR", "CT chest", "Chest X-ray", "MRI"], "imp", ""),
  ("COVID-19 opacities on X-ray are typically:", ["Bilateral, peripheral and lower zone", "Unilateral upper zone", "Central perihilar only", "Apical cavities"], "imp", ""),
  ("Crazy paving appearance on CT is:", ["GGO with inter/intra-lobular septal thickening", "Air-fluid level", "Thin white pleural line", "Ring shadows"], "imp", ""),
  ("CO-RADS 5 means:", ["Very high suspicion (typical COVID-19)", "No suspicion", "PCR positive", "Indeterminate"], "", ""),
  ("CO-RADS 6 means:", ["PCR positive", "Very high suspicion", "Low suspicion", "Normal"], "", ""),
  ("The main CT finding in COVID-19 is:", ["Bilateral subpleural peripheral ground-glass opacities", "Unilateral lobar collapse", "Pleural effusion only", "Tram-track sign"], "", ""),
 ]),
])

# ================================================================= Lec 5
T("l5", "Lec 5 — Chest Imaging III: Bronchiectasis, Emphysema & COPD", "Chest 3", "🌬️",
  "Chest imaging part 3 (د. رانيا)",
"""
<div class="card"><h4>Bronchiectasis</h4>
<ul><li><b>Irreversible</b> abnormal dilatation of the bronchial tree، وسببه الشائع chronic inflammation.</li>
<li><b>HRCT</b> أدق modality للتشخيص.</li></ul>
<table><tr><th>Subtype</th><th>الوصف</th></tr>
<tr><td><b>Cylindrical</b> (الأشهر)</td><td>bronchi بقطر واحد ومش بتضيق، والـ walls parallel (<b>tram track</b> و <b>signet ring</b> signs)</td></tr>
<tr><td>Varicose</td><td>نادر نسبيًا. Beaded appearance (توسع مع أماكن ضيق)</td></tr>
<tr><td>Cystic</td><td>الأشد. Bronchi زي الـ cysts لحد الـ pleura، و<b>air-fluid levels</b> كتير</td></tr></table>
<ul><li><b>X-ray</b>: غالبًا abnormal بس مش كفاية للتشخيص. Tram-track في الـ cylindrical، و air-fluid levels في الـ cystic، و زيادة الـ bronchovascular markings، و ring shadows (bronchi end on)، والأوعية ill-defined.</li>
<li><b>CT</b>: bronchus ظاهر في حدود <b>1 cm من الـ pleura</b> (أهم sign للـ early cylindrical)، <b>lack of tapering</b>، و<b>bronchoarterial ratio</b> أكبر من <b>1.5</b> (الطبيعي 0.65–1).</li>
<li>Ancillary: bronchial wall thickening (الطبيعي أقل من نص عرض الـ artery)، mucoid impaction، air trapping و mosaic perfusion.</li>
<li><b>Signs</b>: tram-track، signet ring، string of pearls، cluster of grapes.</li></ul></div>

<div class="card"><h4>Emphysema</h4>
<p>Abnormal <b>permanent</b> enlargement of airspaces distal to the terminal bronchioles مع destruction of alveolar wall و<b>من غير fibrosis</b>. جزء من الـ COPD، وأحسن تقييم ليه بالـ <b>CT</b>.</p>
<table><tr><th>Subtype</th><th>المميزات</th></tr>
<tr><td><b>Centrilobular</b></td><td>الأشهر. Proximal respiratory bronchioles. <b>Upper zones</b>. مرتبط بالـ <b>smoking</b> (dose-dependent). في الـ CT: lucencies لحد 1 cm في نص الـ lobule ومعاها central dot</td></tr>
<tr><td><b>Panlobular</b></td><td>الـ secondary lobule كله. <b>Lower zones</b> (أكتر blood flow). Uniform distribution</td></tr>
<tr><td><b>Paraseptal</b></td><td>الأجزاء الـ peripheral، جنب الـ pleura والـ fissures. مرتبط بالتدخين، ويعمل <b>subpleural bullae</b> و <b>spontaneous pneumothorax</b></td></tr></table>
<p>أي lucency أكبر من 10 mm اسمها bleb/bulla. والـ emphysematous spaces <b>مالهاش wall</b> ظاهر.</p>
<table><tr><th>Hyperinflation (X-ray)</th><th>Vascular changes</th></tr>
<tr><td><b>Flattened hemidiaphragms</b> (أوثق sign)<br>Increased irregular radiolucency<br>Increased retrosternal airspace و AP diameter<br>Widely spaced ribs<br><b>Sternal bowing</b><br>Tenting of diaphragm</td>
<td>Paucity of vessels<br>Pulmonary arterial hypertension<br>Pruning of peripheral vessels<br>Increased caliber of central arteries<br>RV enlargement</td></tr></table>
<p>الـ X-ray مش بيصور الـ emphysema مباشرة (إلا لو متقدم مع bullae)، لكنه بيخلينا نشك فيه.</p></div>

<div class="card"><h4>COPD</h4>
<ul><li>Spectrum of obstructive airway diseases، فيه component اتنين: <b>chronic bronchitis</b> (small airways disease) و <b>emphysema</b>. Phenotypes: emphysema predominant، airways predominant (small أو large)، mixed.</li>
<li><b>X-ray</b> non-specific: increased bronchovascular markings، cardiomegaly، والـ emphysema بيبان hyperinflation مع flattened diaphragms و <b>small heart</b> وممكن bullae.</li>
<li><b>CT</b>: في الـ chronic bronchitis: bronchial wall thickening و enlarged vessels، والالتهاب المتكرر يعمل scarring و fibrosis.</li></ul></div>
""",
[
 ("Bronchiectasis", [
  ("Bronchiectasis is defined as:", ["Irreversible abnormal dilatation of the bronchial tree", "Reversible bronchial dilatation", "Air in pleural space", "Destruction of alveolar walls"], "imp", ""),
  ("The most accurate modality for diagnosing bronchiectasis is:", ["High resolution CT (HRCT)", "Plain X-ray", "Ultrasound", "MRI"], "imp", ""),
  ("The most common type of bronchiectasis is:", ["Cylindrical", "Varicose", "Cystic", "Centrilobular"], "imp", ""),
  ("The most severe type of bronchiectasis with air-fluid levels is:", ["Cystic", "Cylindrical", "Varicose", "Tubular"], "", ""),
  ("Beaded appearance of bronchi is seen in:", ["Varicose bronchiectasis", "Cylindrical bronchiectasis", "Cystic bronchiectasis", "Emphysema"], "", ""),
  ("Tram-track sign is seen in:", ["Cylindrical bronchiectasis", "Pneumothorax", "Lung abscess", "Pericardial effusion"], "imp", ""),
  ("The most helpful CT sign of early cylindrical bronchiectasis is:", ["Bronchus visualized within 1 cm of the pleural surface", "Air-fluid level", "Blunted costophrenic angle", "Crazy paving"], "", ""),
  ("A bronchoarterial ratio indicating bronchiectasis is greater than:", ["1.5", "0.65", "0.5", "0.1"], "imp", "الطبيعي 0.65–1."),
  ("CT signs of bronchiectasis include all EXCEPT:", ["Double density sign", "Signet ring sign", "String of pearls", "Cluster of grapes"], "", ""),
  ("Chest X-ray in bronchiectasis is:", ["Usually abnormal but inadequate for diagnosis", "Always normal", "The gold standard", "Diagnostic of the subtype always"], "", ""),
 ]),
 ("Emphysema & COPD", [
  ("Emphysema is enlargement of airspaces distal to the terminal bronchioles with alveolar wall destruction and:", ["Without obvious fibrosis", "With extensive fibrosis", "With pleural fluid", "With bronchial dilatation"], "imp", ""),
  ("Emphysema is best evaluated on:", ["CT", "Plain X-ray", "Ultrasound", "MRI"], "", ""),
  ("The most frequent type of emphysema is:", ["Centrilobular", "Panlobular", "Paraseptal", "Cylindrical"], "imp", ""),
  ("Centrilobular emphysema is:", ["Upper zone predominant and strongly associated with smoking", "Lower zone predominant", "Located only adjacent to pleura", "Not related to smoking"], "imp", ""),
  ("Panlobular emphysema is predominantly in the:", ["Lower zones", "Upper zones", "Hilum", "Mediastinum"], "imp", ""),
  ("The emphysema type that may lead to subpleural bullae and spontaneous pneumothorax is:", ["Paraseptal", "Centrilobular", "Panlobular", "Cylindrical"], "imp", ""),
  ("An emphysematous lucency greater than 10 mm is called:", ["Bleb / bulla", "Cavity", "Abscess", "Cyst of bronchiectasis"], "", ""),
  ("The most reliable X-ray sign of hyperinflation is:", ["Flattened hemidiaphragms", "Sternal bowing", "Widely spaced ribs", "Small heart"], "imp", ""),
  ("Sternal bowing and increased retrosternal airspace on lateral X-ray suggest:", ["Emphysema", "Pleural effusion", "Pneumonia", "Pericardial effusion"], "imp", ""),
  ("Vascular changes in emphysema include all EXCEPT:", ["Increased peripheral vessels", "Pruning of peripheral vessels", "Increased caliber of central arteries", "Pulmonary arterial hypertension"], "", ""),
  ("COPD includes:", ["Chronic bronchitis and emphysema", "Asthma and TB", "Pneumonia and abscess", "Pleural effusion and pneumothorax"], "imp", ""),
  ("Chronic bronchiectasis associated with emphysema is diagnosed as:", ["COPD", "TB", "COVID-19", "Heart failure"], "", ""),
  ("On X-ray, emphysema (in COPD) shows a:", ["Small heart with flattened diaphragms", "Water bottle heart", "Large left atrium", "Blunted costophrenic angle"], "", ""),
 ]),
])

# ================================================================= Lec 6
T("l6", "Lec 6 — Cardiac & Vascular Imaging", "Cardiac", "❤️",
  "Cardiac imaging (د. رانيا)",
"""
<div class="card"><h4>Cardiomegaly و تكبير الـ chambers</h4>
<ul><li><b>Cardiomegaly</b> = تكبير القلب (متتلخبطش مع تكبير الـ cardiomediastinal outline لأسباب تانية). غالبًا الـ X-ray كفاية، ولو مش متأكد بنقيس الـ <b>cardiothoracic ratio</b>.</li>
<li>تكبير chamber معينة بيبان بتغير الـ contour، أو interface جديد مع الرئة، أو إزاحة لحاجة في الـ mediastinum.</li></ul>
<table><tr><th>Chamber</th><th>علامات الـ X-ray</th></tr>
<tr><td>Right atrium</td><td>increased convexity في النص التحتاني من الـ right heart border. الـ convexity أكتر من 50% من الـ cardiovascular height، أو الـ margin أبعد من <b>5.5 cm</b> عن الـ midline</td></tr>
<tr><td>Right ventricle</td><td><b>Rounded left heart border</b> و <b>uplifted cardiac apex</b></td></tr>
<tr><td>Left atrium</td><td><b>Double density sign</b>. Oblique measurement أكتر من <b>7 cm</b> (من نص الـ left main bronchus للـ right border بتاع الـ LA). Convex left atrial appendage. <b>Splaying of carina</b> (أكتر من 90°). رفع الـ left main bronchus. إزاحة الـ esophagus لورا</td></tr>
<tr><td>Left ventricle</td><td>Dilatation: الـ left heart border بيتزق لشمال ولتحت ولورا. Hypertrophy: rounding of cardiac apex</td></tr></table></div>

<div class="card"><h4>Pericardial effusion</h4>
<ul><li>الـ pericardial sac الطبيعي فيه <b>30–50 mL</b>.</li>
<li><b>X-ray</b>: الكميات الصغيرة مش بتبان. لازم أكتر من <b>200 mL</b> عشان تبان. <b>Globular enlargement (water bottle configuration)</b>، و widening of subcarinal angle من غير علامات LA تانية، و differential density sign، و cardiothoracic ratio بيكبر مع الوقت.</li>
<li><b>CT/MRI</b>: سمك الـ pericardium الطبيعي <b>2 mm</b>، وأكتر من <b>3–4 mm</b> abnormal. الـ CT بيسهل التشخيص جدًا، ودوره الأساسي يوضح السبب.</li></ul></div>

<div class="card"><h4>Pulmonary embolism</h4>
<ul><li>Embolic occlusion في الـ pulmonary arterial system، وغالبًا thrombus، فاسمه pulmonary thromboembolism.</li>
<li><b>X-ray</b>: <b>not sensitive ولا specific</b>. بيُستخدم عشان يستبعد تشخيصات تانية (pneumonia، pneumothorax).</li>
<li><b>CTPA</b> (CT pulmonary angiography): الـ <b>acute</b> بيبان filling defect في النص وحواليه thin rim of contrast. الـ <b>chronic</b> غالبًا complete occlusion أو filling defects peripheral.</li></ul></div>
""",
[
 ("Cardiac chambers", [
  ("When unsure about cardiomegaly on X-ray, we measure the:", ["Cardiothoracic ratio", "Bronchoarterial ratio", "Hounsfield units", "Signal intensity"], "imp", ""),
  ("Right atrial enlargement is suggested when the right atrial margin is more than …… from the midline:", ["5.5 cm", "1 cm", "15 cm", "2 mm"], "", ""),
  ("Rounded left heart border with uplifted cardiac apex indicates:", ["Right ventricular enlargement", "Left atrial enlargement", "Right atrial enlargement", "Pericardial effusion"], "imp", ""),
  ("Double density sign indicates:", ["Left atrial enlargement", "Right atrial enlargement", "Left ventricular hypertrophy", "Pneumothorax"], "imp", ""),
  ("Splaying of the carina (angle > 90°) is a sign of:", ["Left atrial enlargement", "Right ventricular enlargement", "Pneumonia", "Emphysema"], "imp", ""),
  ("Left atrial enlargement is suggested by an oblique measurement greater than:", ["7 cm", "2 cm", "15 cm", "0.5 cm"], "", ""),
  ("Left atrial enlargement may cause …… displacement of the left main bronchus:", ["Superior", "Inferior", "No", "Anterior"], "", ""),
  ("Left ventricular dilatation displaces the left heart border:", ["Leftward, inferiorly and posteriorly", "Rightward and upward", "Anteriorly only", "It does not change"], "", ""),
  ("Left ventricular hypertrophy may show:", ["Rounding of the cardiac apex", "Double density sign", "Water bottle heart", "Uplifted apex with rounded border only"], "", ""),
 ]),
 ("Pericardial effusion & PE", [
  ("The normal pericardial sac contains:", ["30–50 mL of fluid", "200–300 mL", "1 liter", "No fluid"], "imp", ""),
  ("Pericardial fluid becomes visible on X-ray when it exceeds:", ["200 mL", "30 mL", "5 mL", "1 liter"], "imp", ""),
  ("Water bottle configuration of the heart is seen in:", ["Pericardial effusion", "Left atrial enlargement", "Emphysema", "Pneumothorax"], "imp", ""),
  ("Normal pericardial thickness on CT/MRI is about:", ["2 mm", "10 mm", "0.1 mm", "5 cm"], "", "وأكتر من 3–4 mm abnormal."),
  ("The main role of CT in pericardial effusion is to:", ["Clarify the cause rather than confirm the diagnosis", "Measure blood flow", "Replace echocardiography always", "Detect bone fractures"], "", ""),
  ("Plain chest X-ray in pulmonary embolism is:", ["Neither sensitive nor specific; used to exclude other diagnoses", "Diagnostic", "The gold standard", "Always normal"], "imp", ""),
  ("The imaging of choice for pulmonary embolism is:", ["CT pulmonary angiography (CTPA)", "Plain X-ray", "Ultrasound of chest", "MRI brain"], "imp", ""),
  ("Acute pulmonary embolism on CTPA appears as:", ["Central filling defect surrounded by a thin rim of contrast", "Air-fluid level", "Ground-glass opacity", "Blunted costophrenic angle"], "imp", ""),
  ("Chronic pulmonary emboli on CTPA are often:", ["Complete occlusions or peripheral non-occlusive filling defects", "Central defects with a rim of contrast", "Invisible", "Calcified nodules"], "", ""),
 ]),
])

# ---- T/F drill (statement, correct_idx 0 True/1 False, expl)
TF_DRILL = [
 ("Air appears black (radiolucent) on X-ray.", 0, ""),
 ("Bone (mineral) density appears black on X-ray.", 1, "أبيض."),
 ("In the PA view, the X-ray tube is anterior to the patient.", 1, "Posterior."),
 ("MRI uses ionizing radiation.", 1, ""),
 ("Ultrasound is operator dependent.", 0, ""),
 ("Echo-free areas on US mean the waves are transmitted (fluid).", 0, ""),
 ("Hyperechoic is the term used to describe a white object on MRI.", 1, "Hyperintense / high SI."),
 ("On T2-weighted MRI, CSF appears white.", 0, ""),
 ("On T1-weighted MRI, fat appears black.", 1, "أبيض."),
 ("MRI is safe for patients with artificial pacemakers.", 1, ""),
 ("Pleurae are invisible on a normal chest X-ray.", 0, ""),
 ("The minor fissure is on the left lung.", 1, "على اليمين، وبتعمل الـ middle lobe."),
 ("In most people the left hilum is higher than the right.", 0, ""),
 ("The right ventricle is the most anterior cardiac chamber.", 0, ""),
 ("Ultrasound can detect as little as 3–5 mL of pleural fluid.", 0, ""),
 ("In simple pneumothorax the mediastinum shifts away from the pneumothorax.", 1, "بس في الـ tension pneumothorax."),
 ("Air bronchogram is a sign of pneumonia (consolidation).", 0, ""),
 ("Ghon's focus is a sign of post-primary TB.", 1, "Primary TB."),
 ("CT chest is used to diagnose COVID-19 definitively.", 1, "الـ RT-PCR."),
 ("Bronchiectasis is a reversible dilatation of the bronchi.", 1, "Irreversible."),
 ("Cylindrical bronchiectasis is the commonest type.", 0, ""),
 ("Centrilobular emphysema predominates in the lower zones.", 1, "Upper zones. الـ panlobular هو اللي في الـ lower."),
 ("Flattened hemidiaphragm is the most reliable sign of hyperinflation.", 0, ""),
 ("Double density sign denotes right atrial enlargement.", 1, "Left atrial."),
 ("More than 200 mL of pericardial fluid is needed to be visible on X-ray.", 0, ""),
 ("Plain X-ray is the investigation of choice for pulmonary embolism.", 1, "الـ CTPA."),
]
