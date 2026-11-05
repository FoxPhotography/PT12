# CVP PT — lecture summaries (HTML) + expected questions.
# Question tuple: (text, [correct, wrong...], tag, explanation)   tag: "" | "imp" (topic list / doctor stressed) | "dr" (doctor's own exam question)

LECTURES = []

def L(id, title, short, icon, source, summary, groups):
    LECTURES.append(dict(id=id, title=title, short=short, icon=icon, source=source, summary=summary, groups=groups))

# ---------------------------------------------------------------- Lecture 1
L("l1", "Lecture 1 — Airway, Ventilation & Respiratory Muscles", "Lec 1", "🫁",
  "تفريغ المحاضرة الأولى (عربي + English)",
"""
<div class="card"><h4>مسار الهوا والتقسيم الوظيفي</h4>
<p class="ltr">Nose → Trachea → Main bronchi (Rt &amp; Lt) → Bronchioles → Alveolar ducts → Alveoli</p>
<table><tr><th>Zone</th><th>بيضم</th><th>وظيفته</th></tr>
<tr><td>Conducting zone (upper RT)</td><td>Nose, trachea, main bronchi</td><td>ممر للهوا + <b>Filtration</b> + <b>Warming</b> لـ 37° + <b>Humidification</b></td></tr>
<tr><td>Gas exchange zone (lower RT)</td><td>Bronchioles, alveolar ducts, alveoli</td><td>تبادل الغازات، وهي المنطقة الأخطر في العدوى</td></tr></table></div>

<div class="card"><h4>ميكانيزمات الـ Filtration (3)</h4><ol>
<li><b>Nasal hair</b>: بيمسك التراب الكبير، ومينفعش مع الدخان والجزيئات الصغيرة.</li>
<li><b>Mucociliary action</b> في الـ trachea والـ main bronchi: الـ cilia بتتحرك من <b>تحت لفوق</b> وهي <b>أهم ميكانيزم</b> للتنضيف.</li>
<li><b>Cough receptors</b> في الـ conducting zone بس، وبتعمل cough reflex.</li></ol>
<p><b>اللي بيشل الـ cilia:</b> الـ <b>Heavy smoking</b> (علبة يوميًا لمدة سنتين على الأقل) بيعمل شلل مؤقت، و<b>Anesthesia</b> بيعمل شلل كامل مؤقت. عشان كده مضاعفات الصدر بعد العمليات الكبيرة اسمها <b>expected complications</b>.</p></div>

<div class="card"><h4>Retained secretions وبعد العمليات</h4>
<ul><li>حوالي <b>75%</b> من الوفيات بعد العمليات الكبيرة، و75–80% بعد القلب المفتوح، سببها respiratory infection.</li>
<li>المريض بيبقى high risk لو: كبير في السن، أو عنده سكر، أو بيدخن تقيل، أو عنده مرض رئة أو قلب، أو سمنة مفرطة (130–140 كجم، وهنا بيضيع حوالي ثلثين الرئة).</li>
<li>المضاد الحيوي بيقتل البكتيريا بس <b>مش بيطلع البلغم</b>.</li>
<li>الـ Bronchi عليها <b>C-shaped cartilage</b> فمش بتقفل. أما الـ Bronchioles فمفيهاش cartilage، فبتقفل بسهولة لو اتملت إفرازات.</li></ul>
<p class="key">ترتيب الـ Chest PT إجباري: <b>Mobilization → Transportation → Evacuation</b>. لو غيرت الترتيب مفيش فايدة، لأن أول خطوة في الكحة deep inspiration ومريض الـ ICU مش بيقدر يعملها.</p></div>

<div class="card"><h4>Ventilation و Perfusion</h4><ul>
<li><b>Ventilation</b> = دخول الهوا من الأنف للـ alveoli، ومرتبطة بالـ <b>lung</b>.</li>
<li><b>Alveolar ventilation</b> هي الأهم: من 500 ml في النفس، حوالي 150 بيفضلوا في الـ conducting zone و350 بس بيوصلوا الـ alveoli. عشان كده الـ shallow rapid breathing بيعمل تبادل غازات ضعيف جدًا.</li>
<li><b>Perfusion</b> = الدم اللي واصل للرئة بكميته وجودته (Hb)، ومرتبطة بالـ <b>heart</b>. مريض القلب ومريض الأنيميا بيعانوا من dyspnea حتى لو الرئة سليمة.</li>
<li><b>Diffusion</b> = تبادل O₂ و CO₂.</li>
<li><b>V/Q matching</b>: في الـ supine الهوا بيروح للأجزاء الأمامية والدم للخلفية، فيحصل <b>mismatch</b>. في الـ sitting الاتنين بيروحوا للأجزاء السفلية فيحصل <b>matching</b>، وعشان كده تمارين التنفس بتتعمل sitting أو crook lying.</li></ul></div>

<div class="card"><h4>الرئتين</h4>
<table><tr><th></th><th>Right lung</th><th>Left lung</th></tr>
<tr><td>الشكل</td><td>أقصر وأعرض (الكبد تحتها)</td><td>أطول وأرفع (القلب جنبها)</td></tr>
<tr><td>Lobes</td><td>3: upper، middle، lower</td><td>2: upper و lower + <b>Lingula</b> بدل الـ middle</td></tr>
<tr><td>Segments</td><td>10</td><td>8</td></tr></table>
<p class="key">سؤال مشهور: إزاي تعمل drainage للـ middle lobe في الرئة الشمال؟ ← مفيش middle lobe في الشمال، فيه <b>lingula</b> تبع الـ upper lobe.</p></div>

<div class="card"><h4>عضلات التنفس</h4><ul>
<li><b>Diaphragm</b>: skeletal muscle على شكل قبتين، عليه phrenic nerve (C3,4,5). بيعمل حوالي 75–80% من الشهيق، وبينزل لتحت فيزود الـ <b>vertical diameter</b>، وده الأهم.
<br>• بعد <b>72 ساعة</b> على الـ mechanical ventilator بيفقد أكتر من <b>70%</b> من قوته (disuse atrophy)، وعشان كده لازم weaning.
<br>• في السمنة الشديدة والحمل البطن بتقاوم نزوله، فالمريض بيفقد حوالي ثلث الـ VC.</li>
<li><b>External intercostals</b> (10–20%): حركتها up &amp; out، والـ sternum بيتحرك لقدام فيزود الـ AP والـ transverse.</li>
<li><b>Accessory muscles</b> (SCM، scalene، upper trapezius، serratus anterior، pectoralis): بتشتغل بـ reversed action، فبتشد الضلع الأول لفوق عشان تساعد الـ diaphragm. تضخم عضلات الرقبة معناه إن الـ diaphragm ضعيف. أول أمر في تمارين التنفس: <b>"Relax your shoulders"</b>، والهدف تثبيطها مش تقويتها.</li>
<li><b>Expiration</b>: الهادي <b>passive</b> بالـ elastic recoil، والـ forced (زي الكحة) active بالـ abdominal muscles والـ internal intercostals.</li></ul></div>

<div class="card"><h4>Lung volumes &amp; capacities</h4>
<table><tr><th>Volume</th><th>التعريف</th></tr>
<tr><td>TV (~500 ml)</td><td>الهوا اللي بيدخل ويخرج في التنفس الهادي</td></tr>
<tr><td>IRV</td><td>أقصى هوا إضافي تقدر تشهقه فوق الـ TV</td></tr>
<tr><td>ERV</td><td>أقصى هوا إضافي تقدر تزفره بعد زفير عادي</td></tr>
<tr><td>RV (~1.2 L)</td><td>الهوا اللي بيفضل بعد أقصى زفير، ومبيخرجش أبدًا</td></tr></table>
<p class="ltr"><b>VC = TV + IRV + ERV</b> (من غير RV) &nbsp;|&nbsp; <b>TLC = TV + IRV + ERV + RV</b> &nbsp;|&nbsp; IC = TV + IRV &nbsp;|&nbsp; FRC = ERV + RV</p>
<p><b>Aging:</b> الـ VC بتقل والـ RV بيزيد.</p></div>
""",
[
 ("Conducting zone & Filtration", [
  ("The conducting zone includes:", ["Nose, trachea and main bronchi", "Bronchioles, alveolar ducts and alveoli", "Alveoli only", "Trachea and alveoli"], "", "الـ conducting zone ممر وبيجهز الهوا. الـ bronchioles وما بعدها gas exchange zone."),
  ("The main mechanism of airway filtration is:", ["Mucociliary action", "Nasal hair", "Sneezing", "Alveolar macrophages"], "", "الـ nasal hair بيمسك التراب الكبير بس، والـ cilia هي الأساس."),
  ("Cough receptors are found in:", ["Conducting zone (trachea & main bronchi)", "Alveoli", "Alveolar ducts", "Pleura"], "", "الـ cough reflex موجود في الـ conducting zone بس."),
  ("Functions of the conducting zone include all EXCEPT:", ["Gas exchange", "Filtration", "Warming", "Humidification"], "imp", "تبادل الغازات وظيفة الـ gas exchange zone."),
  ("Complete temporary paralysis of cilia occurs with:", ["Anesthesia", "Sleeping", "Exercise", "Mouth breathing"], "imp", "التخدير بيعمل شلل كامل مؤقت، والتدخين التقيل بيعمل شلل مؤقت."),
  ("Heavy smoking is defined as:", ["One pack (20 cigarettes) daily for at least 2 years", "5 cigarettes daily for 1 year", "One pack weekly for 10 years", "Any smoking"], "", "حسب تعريف المحاضرة."),
  ("Respiratory complications after major surgeries are called expected complications because:", ["Anesthesia paralyzes cilia and abolishes cough reflex", "Patients are always smokers", "Antibiotics are not given", "The diaphragm becomes stronger"], "", "الـ defense mechanisms بتقف أثناء التخدير."),
 ]),
 ("Secretions & Chest physiotherapy", [
  ("The correct sequence of chest physical therapy for secretions is:", ["Mobilization → Transportation → Evacuation", "Evacuation → Mobilization → Transportation", "Transportation → Evacuation → Mobilization", "Coughing first then percussion"], "imp", "لو طلبت منه يكح الأول البلغم هيفضل تحت ومش هيطلع."),
  ("About …… of deaths after major operations are due to respiratory infection:", ["75%", "10%", "25%", "5%"], "", "وبعد القلب المفتوح من 75 لـ 80%."),
  ("Antibiotics alone in retained secretions:", ["Kill bacteria but do not clear sputum", "Clear sputum completely", "Open the bronchioles", "Strengthen the diaphragm"], "", "لازم البلغم يطلع بالـ chest PT."),
  ("Bronchioles collapse easily because they:", ["Have no cartilage", "Have C-shaped cartilage", "Are lined by cilia", "Are part of the conducting zone"], "", "الـ main bronchi عليها C-shaped hyaline cartilage."),
 ]),
 ("Ventilation & Perfusion", [
  ("Of 500 ml inspired air, the amount that reaches the alveoli is about:", ["350 ml", "150 ml", "500 ml", "50 ml"], "", "150 ml بيفضلوا في الـ conducting zone (dead space)."),
  ("Shallow rapid breathing leads to:", ["↓ alveolar ventilation", "↑ alveolar ventilation", "↑ gas exchange", "↑ vital capacity"], "", "معظم الهوا بيفضل في الـ conducting zone."),
  ("Ventilation is related to …… while perfusion is related to ……", ["Lung — heart", "Heart — lung", "Lung — kidney", "Brain — lung"], "", "Perfusion = كمية وجودة الدم اللي بيضخه القلب."),
  ("Best ventilation–perfusion matching occurs in:", ["Sitting position", "Supine position", "Prone position", "Head down position"], "", "في الـ supine بيحصل V/Q mismatch، أما في الـ sitting الهوا والدم بيروحوا للأجزاء السفلية مع بعض."),
  ("Anemic patient with healthy lungs complains of dyspnea because of:", ["Poor quality of perfusion (↓ Hb)", "Poor ventilation", "Airway obstruction", "Weak diaphragm"], "", "الـ Perfusion = quantity + quality."),
 ]),
 ("Lungs & Respiratory muscles", [
  ("The left lung has:", ["2 lobes + lingula", "3 lobes", "2 lobes + middle lobe", "4 lobes"], "imp", "الـ Lingula تبع الـ upper lobe ومكان القلب."),
  ("Number of bronchopulmonary segments in the right lung:", ["10", "8", "12", "6"], "imp", "اليمين 10 والشمال 8."),
  ("The main muscle of inspiration is:", ["Diaphragm", "External intercostals", "Sternocleidomastoid", "Abdominal muscles"], "imp", "بيعمل حوالي 75–80% من الشهيق."),
  ("The diaphragm is supplied by:", ["Phrenic nerve (C3,4,5)", "Vagus nerve", "Intercostal nerves T1–T12", "Accessory nerve"], "imp", "اتنين phrenic nerves، واحد لكل dome."),
  ("After 72 hours on mechanical ventilation the diaphragm loses more than:", ["70% of its strength", "10% of its strength", "30% of its strength", "Nothing"], "", "Disuse atrophy، فلازم weaning تدريجي."),
  ("Hypertrophy of neck muscles in a chest patient indicates:", ["Weak diaphragm", "Strong diaphragm", "Normal breathing", "Pleural effusion"], "", "الـ accessory muscles بتعوض ضعف الـ diaphragm."),
  ("The first instruction in breathing exercises is:", ["Relax your shoulders", "Cough strongly", "Contract your abdomen", "Hold your breath for 10 s"], "", "الهدف تثبيط الـ accessory muscles."),
  ("External intercostal muscles mainly increase the …… diameter:", ["Transverse (and AP)", "Vertical", "None", "Vertical only"], "", "حركتها up & out."),
  ("Forced expiration is performed mainly by:", ["Abdominal & internal intercostal muscles", "Diaphragm", "External intercostals", "Scalene"], "imp", "الزفير الهادي passive."),
 ]),
 ("Lung volumes", [
  ("Vital capacity equals:", ["TV + IRV + ERV", "TV + IRV + ERV + RV", "TV + RV", "IRV + ERV"], "imp", "الـ VC مفيهاش الـ RV."),
  ("Total lung capacity equals:", ["VC + RV", "VC − RV", "TV + IRV", "ERV + RV"], "imp", "TLC = TV + IRV + ERV + RV."),
  ("The air left in the lungs after maximum expiration is:", ["Residual volume", "Tidal volume", "Expiratory reserve volume", "Vital capacity"], "imp", "مبيخرجش أبدًا، ولو خرج الرئة هتقفل على نفسها."),
  ("Normal tidal volume is about:", ["500 ml", "1200 ml", "3000 ml", "150 ml"], "", "الـ RV حوالي 1.2 L والـ TLC حوالي 6 L."),
  ("With aging:", ["VC decreases and RV increases", "VC increases and RV decreases", "Both increase", "Both decrease"], "imp", "Effect of aging on lung volume من مواضيع الميدتيرم."),
  ("Functional residual capacity (FRC) equals:", ["ERV + RV", "TV + IRV", "IRV + ERV", "TV + RV"], "", "الهوا اللي بيفضل بعد زفير عادي."),
 ]),
])

# ---------------------------------------------------------------- Lecture 2
L("l2", "Lecture 2 — Breathing Mechanics, PFT & Chest Symptoms", "Lec 2", "🌬️",
  "نوتس المحاضرة التانية + ملخص مواضيع الميدتيرم",
"""
<div class="card"><h4>ميكانيكا التنفس</h4><ul>
<li><b>Inspiration:</b> الـ sternum بيتحرك لقدام فيزيد الـ AP، والـ diaphragm بيطوّل الصدر (vertical)، والـ external intercostals بتعرّضه.</li>
<li><b>Expiration:</b> passive بالـ elastic recoil، والـ forced بيبقى بالـ abdominal muscles.</li></ul></div>

<div class="card"><h4>Pulmonary function tests</h4><ul>
<li><b>Spirometry</b>: بيقيس الـ lung volumes والـ capacities ومعاهم الـ FEV1. الـ FEV1 قياس <b>dynamic</b>.</li>
<li><b>ABG</b> (Arterial Blood Gases):</li></ul>
<table class="ltr"><tr><th>pH</th><th>PaCO₂</th><th>HCO₃⁻</th><th>PaO₂</th></tr>
<tr><td>7.35 – 7.45</td><td>35 – 45 mmHg</td><td>22 – 26 mEq/L</td><td>80 – 100 mmHg</td></tr></table>
<p>لو المشكلة في الـ CO₂ تبقى respiratory، ولو في الـ HCO₃ تبقى metabolic. والـ HCO₃ بيزيد عشان يعوض زيادة الـ CO₂.</p></div>

<div class="card"><h4>Airway resistance</h4><ul>
<li><b>أسبابها:</b> تفرعات الشعب (bifurcation &amp; branching) وقطر الـ lumen.</li>
<li><b>أسباب ضيق الـ lumen:</b> mucus أو edema جوه الـ airway، أو contraction of smooth muscle.</li>
<li>الـ airways بتوسع في الشهيق وبتضيق في الزفير، فالـ resistance بتبقى أعلى في الزفير في الـ asthma والـ chronic bronchitis.</li></ul></div>

<div class="card"><h4>Dyspnea</h4><ul>
<li>Dyspnea = difficulty / awareness of breathing، وأسبابها chest أو heart أو أسباب تانية (metabolic، كبد، كلى، psychological، ألم الصدر اللي بيمنع full expansion).</li>
<li><b>Exertional:</b> mild مع مجهود شديد، أو severe مع مجهود بسيط. والأسوأ <b>dyspnea at rest</b>.</li>
<li><b>Orthopnea:</b> بتحصل وهو نايم flat وبتتحسن بالقعدة، لأن الـ venous return بيزيد في الـ flat. بتحصل في الـ LSHF، والأنسب للمريض squatting أو sitting.</li>
<li><b>PND:</b> بتصحّيه من النوم بعد ساعة أو ساعتين، ومعاها عرق وزرقان وبرودة. سببها LSHF.</li>
<li>BMI = weight / height²: من 25 لـ 30 overweight، وأكتر من 30 obesity، وأكتر من 40 خطر.</li></ul></div>

<div class="card"><h4>Cough</h4>
<p>Forced expiration بيطلّع البلغم. لو المريض عنده شلل في عضلات البطن (paraplegia) مش بيقدر يكح، والبلغم بيتحبس فيعمل pneumonia.</p>
<p class="key">Steps of cough: <b>1) Deep inspiration</b> → 2) Close epiglottis → 3) ↑ Abdominal pressure → 4) Open epiglottis → 5) Forced expiration</p></div>

<div class="card"><h4>Hemoptysis vs Hematemesis</h4>
<table><tr><th>Hemoptysis</th><th>Hematemesis</th></tr>
<tr><td>كحة بدم، من الجهاز التنفسي</td><td>ترجيع دم، من الـ GIT</td></tr></table>
<p><b>Causes of hemoptysis:</b><br>• <b>Cardiovascular:</b> left heart congestion بتعمل pulmonary edema.<br>• <b>Respiratory:</b> acute infection، violent coughing، TB، pneumonia، bronchial carcinoma، bronchiectasis، pulmonary edema &amp; infarction.<br>والـ Epistaxis = نزيف من الأنف.</p></div>

<div class="card"><h4>Expectoration: اللون والريحة والـ aspect</h4>
<table><tr><th>اللون</th><th>معناه</th></tr>
<tr><td>Colorless</td><td>Normal</td></tr><tr><td>Yellow / Green</td><td>Infection</td></tr><tr><td>White</td><td>Asthma, allergy</td></tr>
<tr><td>Rusty (brown-red)</td><td>Pneumonia</td></tr><tr><td>Pink / frothy blood-tinged</td><td>Pulmonary edema، TB</td></tr>
<tr><td>Red</td><td>Bronchogenic carcinoma</td></tr><tr><td>Brown</td><td>Lung abscess</td></tr><tr><td>Black</td><td>Smoker</td></tr></table>
<p><b>Aspect:</b> watery salty = alveolar carcinoma، frothy blood-tinged = pulmonary edema، mucoid = bronchitis و asthma، purulent = suppurative diseases. <b>Bad odour</b> = infection.</p></div>
""",
[
 ("Mechanics & PFT", [
  ("During inspiration the sternum moves:", ["Forward → ↑ AP diameter", "Backward", "Downward only", "Does not move"], "dr", "سؤال امتحان PT7."),
  ("FEV1 is a …… measurement:", ["Dynamic", "Static", "Blood gas", "Radiological"], "dr", "بيتقاس في زمن محدد هو أول ثانية."),
  ("Normal arterial pH is:", ["7.35 – 7.45", "7.0 – 7.2", "7.5 – 7.6", "6.8 – 7.0"], "", "ABG."),
  ("Normal PaCO₂ is:", ["35 – 45 mmHg", "22 – 26 mmHg", "80 – 100 mmHg", "10 – 20 mmHg"], "", "الـ HCO₃ من 22 لـ 26."),
  ("Causes of airway resistance:", ["Branching of airways and size of lumen", "Heart rate", "Body weight only", "Number of alveoli"], "imp", "من الـ 18 موضوع."),
  ("Causes of decreased diameter of airway lumen include:", ["Mucus/edema and smooth muscle contraction", "Deep breathing", "Cartilage rings", "Surfactant"], "imp", "من الـ 18 موضوع."),
  ("Airway resistance is normally greatest during:", ["Expiration", "Inspiration", "Breath holding", "Sleep"], "", "الـ airways بتضيق في الزفير."),
 ]),
 ("Dyspnea & Cough", [
  ("Orthopnea is dyspnea that:", ["Occurs lying flat and is relieved by sitting", "Occurs sitting and relieved by lying", "Occurs with exercise only", "Occurs on one side only"], "imp", "Definition of orthopnea من الـ 18 موضوع."),
  ("Paroxysmal nocturnal dyspnea is mainly due to:", ["Left side heart failure", "Right side heart failure", "Asthma", "Pleural effusion"], "imp", "بيصحّيه من النوم ومعاه عرق وزرقان."),
  ("The worst grade of dyspnea is:", ["Dyspnea at rest", "Mild exertional dyspnea", "Dyspnea with severe effort", "Dyspnea after running"], "", "الأسوأ وقت الراحة."),
  ("The first step of cough is:", ["Deep inspiration", "Closure of epiglottis", "Forced expiration", "Opening of epiglottis"], "imp", "ومريض الـ ICU مش بيقدر يعمله."),
  ("A paraplegic patient with paralyzed abdominal muscles is at risk of:", ["Retained secretions and pneumonia", "Hyperventilation", "Barrel chest", "Pulmonary embolism only"], "", "مش بيقدر يعمل forced expiration."),
 ]),
 ("Hemoptysis & Sputum", [
  ("Coughing of blood is called:", ["Hemoptysis", "Hematemesis", "Epistaxis", "Melena"], "", "الـ Hematemesis ترجيع دم والـ Epistaxis من الأنف."),
  ("The cardiovascular cause of hemoptysis is:", ["Left heart congestion (pulmonary edema)", "Right heart failure", "Varicose veins", "Hypertension only"], "imp", "Cardiovascular causes of hemoptysis."),
  ("All are respiratory causes of hemoptysis EXCEPT:", ["Cirrhosis of liver", "TB", "Bronchiectasis", "Bronchial carcinoma"], "imp", "التليف الكبدي سبب hematemesis."),
  ("Rusty sputum indicates:", ["Pneumonia", "Asthma", "Smoking", "Normal"], "imp", "صدئي = brown-red."),
  ("Pink frothy blood-tinged sputum indicates:", ["Pulmonary edema", "Lung abscess", "Asthma", "Chronic bronchitis"], "imp", "دم بيتسرب من الشعيرات للـ alveoli."),
  ("Mucoid sputum is typical of:", ["Bronchitis and asthma", "Lung abscess", "Alveolar carcinoma", "Pulmonary edema"], "imp", "Aspect of expectoration."),
  ("Watery salty sputum is seen in:", ["Alveolar carcinoma", "Pneumonia", "Asthma", "TB"], "", "Aspect."),
  ("Bad odour of sputum indicates:", ["Infection", "Allergy", "Heart failure", "Smoking only"], "", "Odour."),
  ("White sputum indicates:", ["Asthma / allergy", "Infection", "Abscess", "Carcinoma"], "", "Colour."),
 ]),
])

# ---------------------------------------------------------------- Lecture 3
L("l3", "Lecture 3 — Cardiac Basics & Heart Failure", "Lec 3", "🫀",
  "نوتس المحاضرة التالتة",
"""
<div class="card"><h4>خطوات فحص المريض</h4>
<p class="ltr">History (personal, present, past, family) → General examination → Local examination → Investigations</p>
<p>تحليل الشكوى بيكون بالـ Onset والـ Cause والـ Duration.</p></div>

<div class="card"><h4>Cardiac circulation</h4>
<p class="ltr">SVC/IVC → RA → <b>Tricuspid</b> → RV → <b>Pulmonary</b> valve → Pulmonary artery → Lungs → Pulmonary veins → LA → <b>Mitral</b> → LV → <b>Aortic</b> valve → Aorta → body</p>
<ul><li>الدورة الكاملة حوالي <b>0.8 sec</b>. الـ venous return بيدخل الـ <b>right side</b>.</li>
<li>الصمامات <b>one way</b>. لو حصل Stenosis يبقى ضيق، ولو Regurge يبقى ارتجاع. والـ Echo بيبين المشكلة.</li>
<li>الـ <b>Coronary arteries</b> طالعة من الـ arch of aorta وبتغذي عضلة القلب.</li>
<li><b>Arrhythmia</b> = عدم انتظام ضربات القلب.</li></ul></div>

<div class="card"><h4>Heart failure symptoms</h4>
<table><tr><th>Left side HF ← Pulmonary congestion</th><th>Right side HF ← Systemic venous congestion</th></tr>
<tr><td>Dyspnea (on exertion، orthopnea، PND)، Cough، Hemoptysis، Pulmonary edema</td><td><b>Cardiac edema</b>: bilateral، pitting، dependent/gravitational. ومعاها Ascites، Jaundice، تقل في الرجلين، puffy eyelids</td></tr></table>
<p>مريض الـ LSHF بيرتاح أكتر في الـ sitting أو الـ squatting، لأن الـ venous return بيقل.</p></div>

<div class="card"><h4>Low cardiac output</h4>
<p>الجسم بيوزع الدم القليل بالأولوية: القلب ثم المخ ثم العضلات ثم الأعضاء الداخلية. أول حاجة بتتأثر <b>الجلد والأغشية المخاطية</b> (pallor و cyanosis)، وبعدها العضلات (fatigue).</p></div>
""",
[
 ("Cardiac circulation", [
  ("Venous return enters the heart at the:", ["Right atrium", "Left atrium", "Left ventricle", "Aorta"], "dr", "سؤال امتحان PT10."),
  ("The tricuspid valve lies between:", ["RA and RV", "LA and LV", "LV and aorta", "RV and pulmonary artery"], "dr", "الـ Mitral بين الـ LA والـ LV."),
  ("Pulmonary veins carry:", ["Oxygenated blood to the LA", "Deoxygenated blood to the RA", "Deoxygenated blood to the lungs", "Oxygenated blood to the RV"], "", "الأوردة الوحيدة اللي بتشيل دم مؤكسج."),
  ("Heart valves act in:", ["One way direction", "Two way direction", "Three way direction", "No direction"], "dr", "سؤال امتحان PT10."),
  ("Cardiac muscle is supplied by:", ["Coronary arteries", "Carotid arteries", "Pulmonary arteries", "Basilar artery"], "dr", "سؤال امتحان PT10."),
  ("Narrowing of a heart valve is called:", ["Stenosis", "Regurgitation", "Arrhythmia", "Infarction"], "", "والارتجاع اسمه Regurgitation."),
  ("Arrhythmia means:", ["Irregular heart rhythm", "Valve narrowing", "Low blood pressure", "Heart muscle death"], "", "عدم انتظام."),
 ]),
 ("Heart failure", [
  ("Pulmonary congestion is a feature of:", ["Left side heart failure", "Right side heart failure", "Varicose veins", "DVT"], "imp", "Congestion of Lt side heart failure من الـ 18 موضوع."),
  ("Symptoms of left side heart failure include all EXCEPT:", ["Ascites", "Dyspnea on exertion", "Orthopnea", "Hemoptysis"], "imp", "الـ Ascites من الـ RSHF."),
  ("Symptoms of right side heart failure include:", ["Ascites, edema and jaundice", "Orthopnea and PND", "Hemoptysis", "Wheezes"], "imp", "Systemic venous congestion."),
  ("Cardiac edema is:", ["Bilateral, pitting, dependent (gravitational)", "Unilateral, non pitting", "Bilateral, non pitting, not gravitational", "Unilateral, pitting"], "dr", "سؤال امتحان PT10 ومهم جدًا."),
  ("The most comfortable position for a left side heart failure patient is:", ["Sitting / squatting", "Flat supine", "Head down", "Prone"], "", "عشان الـ venous return يقل."),
  ("The first tissues affected by low cardiac output are:", ["Skin and mucous membranes", "Heart", "Brain", "Kidney"], "", "Pallor و cyanosis، وبعدها العضلات."),
 ]),
])

# ---------------------------------------------------------------- Lecture 4
L("l4", "Lecture 4 — Chest Pain: Differential Diagnosis", "Lec 4", "💢",
  "تفريغ محاضرة ألم الصدر (المحاضرة الرابعة)",
"""
<div class="card"><h4>أنواع ألم الصدر</h4><p>مش كل ألم صدر يبقى قلب. الأنواع:</p><ol>
<li><b>Musculoskeletal</b> زي الـ Myositis: شكة حادة بتزيد مع الشهيق العميق.</li>
<li><b>Pleural / Pulmonary</b>: الـ <b>Lung نفسها مفيهاش pain receptors</b>، والألم جاي من الـ <b>pleura</b>. بيبقى sharp stitching وبيزيد مع الشهيق. والـ Pneumonia بتعمل pleuritic pain في ناحية واحدة.</li>
<li><b>Vascular</b> زي الـ Pulmonary embolism.</li>
<li><b>Cardiac / Ischemic</b> زي الـ Angina والـ CAD.</li>
<li><b>Psychological</b> من الـ stress والـ anxiety.</li></ol></div>

<div class="card"><h4>Pleural collections (كلها restrictive)</h4>
<table><tr><td>Fluid</td><td>Pleural effusion</td></tr><tr><td>Air</td><td>Pneumothorax (زي الطعن والحوادث)</td></tr>
<tr><td>Blood</td><td>Hemothorax</td></tr><tr><td>Pus</td><td>Empyema / Pyothorax</td></tr></table>
<p>لو التجمع في الناحيتين ممكن يحصل Respiratory failure.</p></div>

<div class="card"><h4>DVT → Pulmonary embolism</h4><ul>
<li><b>Risk factors:</b> fractures و casting، obesity، الجلوس الطويل والطيران، المرضى اللي نايمين في السرير، ومرضى القلب والكبد والكلى. وفيه حالة طفل جاله DVT من القعدة على الموبايل.</li>
<li>الـ Thrombus لما يتفصل يبقى Embolus، ويمشي في الـ IVC للـ RA ثم الـ RV ثم الـ <b>pulmonary artery</b> ويسدها.</li>
<li>العرض: <b>massive chest pain</b> مفاجئ، و<b>90%</b> من الحالات مش بتتشخص في الوقت المناسب.</li></ul>
<p class="key">🚨 لو فيه شك في DVT: ممنوع dorsiflexion أو plantarflexion أو أي تمرين أو deep breathing قوي قبل الـ <b>Doppler</b>.</p></div>

<div class="card"><h4>Ischemia → Infarction</h4><ul>
<li><b>Ischemia</b> = نقص الدم والأكسجين لعضلة القلب. والقاعدة: <b>"Every ischemia must be followed by pain"</b>، زي الـ intermittent claudication في الرجل.</li>
<li>انسداد أكتر من <b>50%</b> لمدة <b>20–30 دقيقة</b> بيوصل لـ <b>MI</b> يعني necrosis، وده محتاج ICU وقسطرة ودعامة.</li>
<li><b>High risk:</b> كبار السن (الشرايين بتبقى stiff)، والسكر وحتى الـ pre-diabetic، والـ post-CABG.</li>
<li><b>Coronary vasospasm</b>: شرايين سليمة بس بتنقبض فجأة من الصدمات النفسية.</li>
<li><b>Silent ischemia</b>: ischemia من غير أي ألم، ودي عند مرضى <b>السكر</b> بسبب الـ autonomic neuropathy، وعند الـ post-CABG.</li>
<li>الكبار ومرضى السكر والقلب المفتوح محتاجين exercise prescription محسوبة بالـ intensity والـ duration والـ frequency والـ type. ولو المريض اشتكى من chest pain أثناء التمرين: <b>STOP فورًا</b> وقيس الـ vital signs.</li></ul></div>

<div class="card"><h4>Anginal vs Psychological pain</h4>
<table><tr><th></th><th>Anginal</th><th>Psychological</th></tr>
<tr><td>Site</td><td>Retrosternal، diffuse، <b>hand sign</b></td><td>نقطة محددة، <b>finger sign</b></td></tr>
<tr><td>Character</td><td>Compression / squeezing / heavy (dull aching)</td><td>Sharp needle stitching</td></tr>
<tr><td>Duration</td><td><b>3–15 دقيقة</b> (الكتاب بيقول 5–15)، ولو 30 دقيقة يبقى MI</td><td>ثواني</td></tr>
<tr><td>Increased by</td><td>Exercise، stress، heavy meal، cold weather، smoking</td><td>التفكير الزايد</td></tr>
<tr><td>Relieved by</td><td>Rest + <b>Sublingual nitrates</b></td><td>الطمأنة والـ relaxation</td></tr>
<tr><td>Referred</td><td>كتف ودراع شمال، الفك، الرقبة، الصباع الصغير</td><td>مفيش</td></tr>
<tr><td>Associated</td><td>Cold sweating، pallor، مش قادر يتكلم</td><td>Vital signs طبيعية</td></tr></table>
<p><b>Atypical angina</b>: غثيان، epigastric discomfort، dyspnea وتعب، وبتبقى شائعة في الكبار والستات ومرضى السكر.</p>
<p><b>ليه دول بيزودوا الألم:</b> البرد والتدخين والـ stress بيعملوا vasoconstriction، والمجهود والوجبة التقيلة بيزودوا الـ O₂ demand. والـ nitrates بتعمل vasodilatation، وممكن تعمل صداع.</p></div>
""",
[
 ("Types of chest pain", [
  ("Lung tissue itself:", ["Has no pain receptors; pain arises from the pleura", "Is very rich in pain receptors", "Gives anginal pain", "Gives referred pain to the jaw"], "", "قاعدة مهمة."),
  ("Pleuritic chest pain characteristically:", ["Increases with inspiration", "Is relieved by nitrates", "Lasts 3–15 minutes", "Is retrosternal compression"], "", "حركة الـ pleura الملتهبة."),
  ("Collection of pus in the pleural space is called:", ["Empyema", "Hemothorax", "Pneumothorax", "Chylothorax"], "", "الهوا = pneumothorax، والدم = hemothorax."),
  ("Pleural collections are classified as:", ["Restrictive lung disease", "Obstructive lung disease", "Suppurative only", "Cardiac disease"], "", "بيضغطوا على الرئة ويمنعوها تتمدد."),
  ("Stab wound to the chest wall leading to air in the pleural space is:", ["Pneumothorax", "Pleural effusion", "Emphysema", "Bronchiectasis"], "", "مثال المحاضرة."),
 ]),
 ("DVT & Pulmonary embolism", [
  ("Pulmonary embolism usually originates from:", ["DVT of lower limb veins", "Left ventricle", "Coronary arteries", "Carotid artery"], "imp", "Embolus ← IVC ← RA ← RV ← pulmonary artery."),
  ("In a patient suspected of DVT, the physiotherapist must:", ["Avoid ankle movements/exercise until Doppler confirms", "Start active ankle pumps immediately", "Apply deep massage to the calf", "Apply resisted exercise"], "dr", "زي سؤال PT10: In acute DVT ← None of the above."),
  ("Risk factors of DVT include all EXCEPT:", ["Regular walking", "Fractures and casting", "Obesity and long sitting", "Bed-ridden patients"], "", "الحركة بتمنع الـ DVT."),
  ("The main presentation of pulmonary embolism is:", ["Sudden massive chest pain", "Chronic productive cough", "Wheezes", "Clubbing"], "", "و90% مش بيتشخصوا في الوقت المناسب."),
 ]),
 ("Ischemic pain & Angina", [
  ("Myocardial infarction occurs when severe ischemia lasts:", ["20–30 minutes", "1–2 seconds", "3–5 seconds", "24 hours only"], "imp", "مع انسداد أكتر من 50%."),
  ("Anginal pain lasts:", ["3–15 minutes", "Few seconds", "Hours", "Days"], "imp", "Duration of anginal pain."),
  ("Anginal pain is relieved by:", ["Rest and sublingual nitrates", "Exercise", "Heavy meals", "Cold weather"], "imp", "Factors decrease."),
  ("Factors increasing anginal pain include all EXCEPT:", ["Rest", "Exercise", "Heavy meal", "Cold weather"], "imp", "Factors increase."),
  ("Anginal pain is referred to:", ["Left shoulder, arm, jaw, neck and fingers", "Right leg", "Lower back only", "Not referred"], "imp", "Site & referred pain."),
  ("Hand syndrome (hand sign) is typical of:", ["Anginal pain", "Psychological pain", "Pleuritic pain", "Myositis"], "dr", "زي سؤال PT10 (17)."),
  ("Finger sign with few-seconds stitching pain suggests:", ["Psychological chest pain", "Angina", "MI", "Pulmonary embolism"], "dr", "زي سؤال PT10 (6)."),
  ("Silent myocardial ischemia is common in:", ["Diabetic patients", "Young athletes", "Asthmatic children", "Pregnant women"], "", "بسبب الـ autonomic neuropathy."),
  ("If the patient complains of chest pain during exercise session you must:", ["Stop exercise immediately and check vital signs", "Increase intensity", "Continue and observe", "Give him water and continue"], "", "Stop exercise rule."),
  ("Cold weather and smoking increase anginal pain because they cause:", ["Vasoconstriction of coronary arteries", "Vasodilatation", "Decreased O₂ demand", "Bradycardia"], "", "والمجهود والأكل التقيل بيزودوا الـ demand."),
  ("Coronary vasospasm is mostly triggered by:", ["Severe psychological stress", "Rest", "Sleep", "Nitrates"], "", "شرايين سليمة بتنقبض فجأة."),
 ]),
])

# ---------------------------------------------------------------- Lecture 5
L("l5", "Lecture 5 — Chronic Obstructive Diseases: COPD & Asthma", "Lec 5", "🚬",
  "تفريغ محاضرة أمراض الجهاز التنفسي المزمنة (المحاضرة الخامسة)",
"""
<div class="card"><h4>تصنيف أمراض الصدر (4)</h4>
<table><tr><th>المجموعة</th><th>المشكلة</th><th>مثال</th></tr>
<tr><td>Obstructive</td><td>صعوبة الزفير</td><td>COPD، Asthma</td></tr>
<tr><td>Restrictive</td><td>صعوبة الشهيق والتمدد</td><td>Scoliosis، kyphosis، post-surgery، fibrosis</td></tr>
<tr><td>Pleural (تبع الـ restrictive)</td><td>تجمع في الـ pleura والرئة نفسها سليمة</td><td>Effusion، pneumothorax، hemothorax، empyema</td></tr>
<tr><td>Suppurative</td><td>عدوى بصديد كتير</td><td>Bronchiectasis، lung abscess</td></tr></table></div>

<div class="card"><h4>COPD: 3 مراحل</h4><ol>
<li><b>Chronic bronchitis</b>: كحة ببلغم على الأقل <b>3 شهور متتالية في السنة ولمدة سنتين متتاليتين</b>. بتبدأ في الـ main bronchi والـ cartilage بيحافظ عليها مفتوحة.</li>
<li><b>Chronic bronchiolitis</b>: الالتهاب بينزل للـ bronchioles، ودي مفيهاش cartilage، فيحصل انسداد حقيقي.</li>
<li><b>Emphysema</b>: destruction / loss of elasticity of alveolar walls. سببه نقص <b>Alpha-1 antitrypsin</b>، الإنزيم اللي بيحمي الرئة.</li></ol>
<p><b>Risk factors:</b> heavy smoking وهو السبب الأول، والاستعداد الوراثي (α1-AT)، والمستوى المعيشي، والتعرض المهني لمصانع الزجاج والسجاد والغزل.</p></div>

<div class="card"><h4>Air trapping ونتايجه</h4><ul>
<li>الهوا بيدخل بسهولة لكن مش بيخرج، فيحصل <b>Hyperinflation</b>.</li>
<li><b>Barrel chest</b>: الطبيعي AP:Transverse حوالي 5:7، وفي الـ COPD بيبقى <b>AP = Transverse</b>، والضلوع horizontal، والـ subcostal angle بيزيد.</li>
<li>الـ <b>Diaphragm بيبقى low flattened</b> فيفقد الـ mechanical advantage.</li>
<li>Hypoxemia، و<b>Central cyanosis</b> تحت اللسان، و<b>Clubbing</b> بـ 3 درجات: loss of angle ← parrot beak ← drumstick.</li>
<li>Productive cough، و dyspnea، و ↓ exercise tolerance.</li></ul></div>

<div class="card"><h4>Cor pulmonale</h4>
<p class="ltr">Chronic hypoxemia → reflex pulmonary vasoconstriction → <b>pulmonary hypertension</b> → RV overload → <b>RV hypertrophy = Cor pulmonale</b> → <b>Right side HF</b> (edema، ascites، ↑ cyanosis)</p></div>

<div class="card"><h4>PFT في الـ COPD</h4>
<table><tr><th>Parameter</th><th>Normal</th><th>COPD</th></tr>
<tr><td>TV، IRV، ERV، VC</td><td>TV ~500 ml</td><td>↓</td></tr>
<tr><td>RV</td><td>~1.2 L</td><td>↑↑↑ (air trapping)</td></tr>
<tr><td>TLC</td><td>~6 L</td><td>↑ (بسبب الـ RV)</td></tr>
<tr><td>FEV1</td><td>80% في الثانية الأولى (و15% في التانية و5% في التالتة)</td><td>&lt;80%. لو &lt;50% يبقى severe، ولو &lt;30% يبقى very severe</td></tr>
<tr><td>Bronchodilator</td><td>—</td><td><b>Irreversible</b></td></tr></table>
<p><b>X-ray:</b> hyperlucency (أسود)، والضلوع متباعدة، و barrel، و flat diaphragm. <b>Percussion:</b> hyper-resonance. <b>TVF:</b> ↓.</p></div>

<div class="card"><h4>Bronchial asthma</h4><ul>
<li>Antigen–antibody reaction (<b>IgE</b>) على الـ main bronchi.</li>
<li><b>Triad:</b> bronchoconstriction، mucosal edema، tenacious sticky mucus.</li>
<li><b>Reversible</b>: المريض بيبقى طبيعي بين النوبات، ومفيش clubbing.</li>
<li><b>Status asthmaticus</b>: نوبة شديدة مش بتستجيب للموسعات، ومحتاجة ICU.</li>
<li><b>Exercise-induced asthma</b>: سببها الـ mouth breathing، لأن الهوا بيدخل بارد وناشف ومليان تراب.</li>
<li>الصوت المميز: <b>Wheeze</b>.</li></ul>
<p class="key">📌 سؤال الدكتور: FEV1 = 60% وبعد الـ bronchodilator والـ PT بقت 80% ← التشخيص <b>Asthma</b> لأنه reversible. ولو مااتحسنتش يبقى COPD.</p>
<p><b>الوضع أثناء النوبة:</b> <b>Forward leaning / tripod</b> مع pursed-lip breathing. و🚫 ممنوع الـ supine.</p></div>

<div class="card"><h4>COPD vs Asthma</h4>
<table><tr><th></th><th>COPD</th><th>Asthma</th></tr>
<tr><td>Pathology</td><td>تدمير الـ alveoli والتهاب الـ bronchioles</td><td>IgE allergic</td></tr>
<tr><td>Reversibility</td><td>Irreversible</td><td>Reversible</td></tr><tr><td>Age</td><td>أكبر من 40–50</td><td>أطفال وشباب</td></tr>
<tr><td>Smoking</td><td>السبب الأساسي</td><td>مش شرط</td></tr><tr><td>Clubbing</td><td>موجود</td><td>مش موجود</td></tr>
<tr><td>Barrel chest</td><td>دائم</td><td>مؤقت أثناء النوبة</td></tr></table></div>

<div class="card"><h4>PT management</h4><ol>
<li><b>Dyspnea control:</b> الـ <b>Pursed-lip breathing</b> بيعمل back pressure يمنع collapse الـ bronchioles وبيطلع الهوا المحبوس.</li>
<li><b>Secretions:</b> Hydration ← Mobilization (percussion و vibration و tapping) ← Clearance (controlled cough و huffing و suction).</li>
<li><b>Exercise training</b> تدريجي.</li></ol>
<p><b>COPD problems → goals:</b> ↑ secretions ← قللها وطلّعها. ضعف عضلات التنفس ← قويها. ↓ exercise tolerance ← زودها. Barrel chest ← صحح الـ posture. Abnormal breathing pattern ← controlled breathing و relaxed expiration.</p>
<p><b>Asthma:</b> ↓ bronchospasm، والتحكم في النفس، وطلّع البلغم <b>بعد</b> النوبة. الـ postural drainage مش أثناء النوبة لأنه بيزود الـ bronchospasm. وكمان تصحيح الـ posture (rounded shoulders و forward head)، ونشاط خفيف لفترات قصيرة.</p></div>
""",
[
 ("COPD", [
  ("Chronic bronchitis is defined as productive cough for at least:", ["3 consecutive months/year for 2 consecutive years", "1 month for 1 year", "2 weeks", "6 months for 5 years"], "imp", "تعريف المحاضرة."),
  ("Emphysema means:", ["Destruction / loss of elasticity of alveolar walls", "Inflammation of main bronchi", "Fluid in pleura", "Dilatation of bronchi"], "dr", "سؤال امتحان PT7."),
  ("The protective enzyme whose deficiency causes emphysema is:", ["Alpha-1 antitrypsin", "Lipase", "Amylase", "Pepsin"], "", "الوراثة بتفسر ليه مش كل المدخنين بيجيلهم COPD."),
  ("The number one risk factor of COPD is:", ["Heavy smoking", "Exercise", "Pregnancy", "Mouth breathing"], "", "وكمان التعرض المهني."),
  ("In barrel chest:", ["AP diameter = transverse diameter", "AP > transverse", "AP < transverse (5:7)", "Sternum is depressed"], "imp", "Types of chest deformity."),
  ("The diaphragm in COPD becomes:", ["Low and flattened", "High and domed", "Paralyzed", "Hypertrophied and domed"], "", "بسبب الـ hyperinflation."),
  ("Residual volume in COPD is:", ["Tremendously increased", "Decreased", "Normal", "Zero"], "dr", "سؤال امتحان PT7."),
  ("Total lung capacity in COPD:", ["Increases", "Decreases", "Unchanged", "Becomes zero"], "dr", "سؤال امتحانات سابقة."),
  ("FEV1 < 30% indicates:", ["Very severe COPD", "Mild COPD", "Normal", "Restrictive disease"], "", "أقل من 50% يبقى severe."),
  ("Normally a person exhales …… of the vital capacity in the first second:", ["80%", "50%", "100%", "15%"], "", "و15% في التانية و5% في التالتة."),
  ("COPD airflow limitation is:", ["Irreversible", "Reversible", "Always normal", "Restrictive"], "dr", "سؤال الامتحان السابق (T/F 10)."),
  ("Chest X-ray in COPD shows:", ["Hyperlucency with flat diaphragm", "Ground-glass opacity", "Cavity", "White lung"], "", "الهوا بيظهر أسود."),
  ("Percussion note in COPD is:", ["Hyper-resonance", "Dullness", "Stony dullness", "Normal resonance"], "dr", "سؤال امتحان PT10."),
  ("Cor pulmonale means:", ["RV hypertrophy due to lung disease (pulmonary hypertension)", "LV hypertrophy due to hypertension", "Valve disease", "Coronary disease"], "", "Lung problem بيأثر على القلب."),
  ("Cor pulmonale ends in:", ["Right side heart failure", "Left side heart failure", "Pulmonary embolism", "Asthma"], "", "Edema و ascites."),
  ("The first stage of finger clubbing is:", ["Loss of the nail-bed angle", "Parrot beak", "Drumstick", "Osteoarthropathy"], "", "وبعده parrot beak وبعده drumstick."),
 ]),
 ("Asthma", [
  ("Asthma is caused by antigen–antibody reaction involving:", ["IgE", "IgG", "IgM", "IgA"], "", "على الـ main bronchi."),
  ("The asthmatic triad includes all EXCEPT:", ["Alveolar destruction", "Bronchoconstriction", "Mucosal edema", "Tenacious mucus"], "", "تدمير الـ alveoli ده emphysema."),
  ("FEV1 was 60% and rose to 80% after bronchodilator. The diagnosis is:", ["Bronchial asthma", "COPD", "Emphysema", "Restrictive lung disease"], "dr", "سؤال الدكتور في المحاضرة: reversible يبقى asthma."),
  ("Asthma is classified as:", ["Reversible obstructive disease", "Irreversible obstructive", "Restrictive", "Suppurative"], "dr", "سؤال امتحان PT7 (case)."),
  ("The characteristic abnormal breath sound in asthma is:", ["Wheeze", "Pleural rub", "Bronchial breathing", "Crepitations only"], "dr", "سؤال امتحان PT10."),
  ("Exercise-induced asthma is mainly due to:", ["Mouth breathing", "Nasal breathing", "Low heart rate", "Overhydration"], "", "الهوا بيدخل بارد وناشف."),
  ("Best position during an asthmatic attack:", ["Forward leaning (tripod) with pursed lips", "Supine", "Head down", "Prone lying"], "", "والـ supine ممنوع."),
  ("Status asthmaticus is:", ["Severe prolonged attack not responding to bronchodilators", "Mild attack", "Asthma between attacks", "Exercise-induced attack"], "", "محتاج ICU."),
  ("Postural drainage in asthma is applied:", ["After the attack, not during it", "During the attack", "Never", "Only in supine"], "imp", "Management of asthma من الـ 18 موضوع."),
  ("Clubbing in a pure asthmatic is:", ["Absent (free between attacks)", "Always present", "Grade 3", "Present only in children"], "", "الـ clubbing علامة chronic hypoxemia."),
 ]),
 ("PT management", [
  ("Pursed-lip breathing helps by:", ["Creating back pressure preventing bronchiolar collapse", "Increasing bronchospasm", "Strengthening accessory muscles", "Increasing residual volume"], "imp", "Clinical problems & management of COPD."),
  ("The first step of secretion management in COPD is:", ["Hydration", "Suction", "Huffing", "Percussion"], "", "Hydration ← Mobilization ← Clearance."),
  ("Huffing and controlled coughing are methods of:", ["Clearance (evacuation) of secretions", "Mobilization", "Hydration", "Postural correction"], "", "و suction للي مش بيقدر يكح."),
  ("A goal of COPD rehabilitation is:", ["Increase exercise tolerance", "Strengthen accessory muscles", "Increase residual volume", "Encourage upper chest breathing"], "imp", "ومعاها correct posture و decrease secretions."),
 ]),
])

# ---------------------------------------------------------------- Lecture 6
L("l6", "Lecture 6 — TVF, Restrictive & Suppurative Lung Diseases", "Lec 6", "🩺",
  "تفريغ المحاضرة السادسة",
"""
<div class="card"><h4>Tactile Vocal Fremitus (TVF)</h4><ul>
<li>اهتزاز الأحبال الصوتية لما المريض يقول <b>99</b> أو <b>44</b>، والاهتزاز بيوصل لجدار الصدر.</li>
<li>بتحط الـ <b>ulnar border of the hand</b> على الـ apex والـ middle والـ lower lobes من قدام ومن ورا، وبتقارن <b>الناحيتين ببعض</b>.</li>
<li>الـ TVF بيقل في <b>أغلب</b> أمراض الصدر، زي الـ COPD والـ effusion والـ pneumothorax.</li></ul>
<p class="key">TVF بيزيد في الـ <b>3 Cs</b> بس: <b>Consolidation</b> (زي الـ pneumonia)، و<b>Cavity</b> أو abscess بجدار صلب، و<b>Solid mass</b>. السبب إن المادة الصلبة بتنقل الصوت أحسن من الهوا.</p></div>

<div class="card"><h4>Restrictive lung disease</h4><ul>
<li>الرئة مش بتقدر تتمدد في الشهيق، فالـ volume بيقل.</li>
<li><b>Causes:</b><br>• <b>Pleural</b>: effusion، pneumothorax، empyema، chylothorax.<br>• <b>Fibrosis</b> وده بيقلل الـ compliance.<br>• <b>Occupational</b>: silicosis في الزجاج والسيراميك، و asbestosis، و coal worker's.<br>• <b>Autoimmune</b>: SLE، RA، polymyositis.<br>• <b>Drugs و radiation</b> زي الـ methotrexate.<br>• <b>Neuromuscular</b>: GBS و MG.<br>• <b>Chest wall</b>: scoliosis و kyphosis، والألم الشديد.</li>
<li><b>PFT:</b> FVC و TLC بيقلوا، و<b>FEV1/FVC بتبقى طبيعية أو عالية</b> (70–80%) لأن مفيش obstruction. عشان كده النسبة دي مبتشخصش الـ restrictive.</li>
<li><b>X-ray:</b> opacity أو ground-glass (أبيض)، عكس الـ COPD اللي بيبان أسود.</li>
<li><b>الكحة:</b> dry non-productive.</li></ul>
<p><b>Positioning:</b><br>• <b>Acute</b> (فيه سوائل أو هوا): ينام على الناحية <b>المصابة</b> (affected side down) عشان الألم يقل والرئة السليمة تتمدد، ومعاها UWSD.<br>• <b>Chronic</b> (عشان التمدد): الناحية المصابة <b>لفوق</b> + segmental breathing.</p></div>

<div class="card"><h4>Suppurative lung diseases</h4><ul>
<li>دول <b>أكتر</b> المرضى في كمية البلغم، والـ asthma والـ COPD والـ restrictive أقل.</li>
<li><b>Bronchiectasis:</b> التهاب بكتيري متكرر بيدمر جدار الشعب، فيحصل <b>توسع دائم irreversible</b>، والـ cilia بتقف، والبلغم بيبقى غزير.</li>
<li><b>Lung abscess:</b> تجويف فيه صديد. أسبابه pneumonia مهملة، والسكر، والـ RA، وكبار السن، ونقص المناعة، وبعد التخدير. وممكن empyema تعمل pleurobronchial fistula.</li>
<li><b>Risk factors:</b> aspiration pneumonia في فقدان الوعي أو التخدير، والـ cystic fibrosis، والـ chemotherapy، والتدخين مع إهمال نظافة الفم.</li>
<li><b>البلغم الخطير:</b> الأخضر والأصفر الغامق والصدئي، وده معناه active bacterial infection (neutrophils و myeloperoxidase).</li>
<li><b>Retained secretions</b> ممكن توصل لـ toxemia أو septicemia.</li>
<li><b>Investigations:</b> <b>HRCT</b> وده الأفضل، و sputum culture، و CRP و ESR، و bronchoscopy.</li>
<li><b>PT:</b> Postural drainage، و percussion و vibration، و ACBT (huffing)، و breathing exercises.</li></ul></div>

<div class="card"><h4>جدول المقارنة الشامل</h4>
<table><tr><th></th><th>Asthma</th><th>COPD</th><th>Restrictive</th><th>Suppurative</th></tr>
<tr><td>TLC</td><td>طبيعي أو ↑</td><td>↑</td><td>↓↓</td><td>طبيعي أو ↓</td></tr>
<tr><td>FEV1/FVC</td><td>↓ (&lt;70%)</td><td>↓↓</td><td>طبيعي أو ↑</td><td>↓ حسب البلغم</td></tr>
<tr><td>Sputum</td><td>قليل مخاطي</td><td>قليل لمتوسط</td><td>ناشف</td><td>غزير صديدي</td></tr>
<tr><td>TVF</td><td>↓</td><td>↓</td><td>↓ (إلا الـ 3 Cs)</td><td>↑ فوق الـ cavity</td></tr>
<tr><td>X-ray</td><td>طبيعي أو hyperinflation</td><td>أسود hyperlucent</td><td>أبيض opacity</td><td>Cavity</td></tr>
<tr><td>هدف الـ PT</td><td>تخفيف التقلص</td><td>Ventilation و tolerance</td><td>Expansion</td><td>Airway clearance</td></tr></table></div>
""",
[
 ("TVF", [
  ("TVF is examined by asking the patient to say:", ["99 or 44", "AAA", "Cough", "Deep breath only"], "", "وبتحط الـ ulnar border of hand."),
  ("TVF is increased in:", ["Consolidation (pneumonia)", "Pleural effusion", "COPD", "Pneumothorax"], "dr", "الـ 3 Cs. وفي سؤال PT10 الإجابة كانت None of the above."),
  ("TVF is decreased in:", ["Pleural effusion", "Consolidation", "Solid mass", "Lung abscess cavity with solid wall"], "", "معظم أمراض الصدر بتقلل الـ TVF."),
  ("The diagnostic value of TVF depends mainly on:", ["Comparison between both sides", "Absolute value", "Patient's age", "Heart rate"], "", "By comparison."),
 ]),
 ("Restrictive", [
  ("Restrictive lung disease means:", ["Inability of the lung to expand → ↓ volume", "Difficulty of expiration", "Reversible airflow limitation", "Purulent secretions"], "", "صعوبة الشهيق."),
  ("In restrictive disease, FEV1/FVC is:", ["Normal or high", "Very low", "Zero", "Below 30%"], "", "مفيش obstruction."),
  ("Vital capacity in restrictive disease:", ["Decreases", "Increases", "Unchanged", "Doubles"], "dr", "سؤال امتحان PT7."),
  ("Silicosis results from exposure to silica in:", ["Glass and ceramic industries", "Coal mines only", "Farming", "Textile only"], "", "والـ coal worker's pneumoconiosis من الفحم."),
  ("All are causes of restrictive lung disease EXCEPT:", ["Bronchial asthma", "Scoliosis", "Pleural effusion", "Guillain–Barré syndrome"], "", "الربو obstructive."),
  ("Postural deformities (kyphoscoliosis) cause:", ["Restrictive lung disease", "Obstructive lung disease", "Suppurative disease", "Asthma"], "dr", "سؤال الامتحان السابق (T/F 9)."),
  ("Cough in restrictive / pleural disease is usually:", ["Dry non-productive", "Purulent profuse", "Rusty", "Pink frothy"], "dr", "زي سؤال الامتحان السابق: Dry cough in pleural effusion."),
  ("In the acute phase of pleural effusion the patient lies on:", ["The affected side", "The healthy side", "Prone", "Head down"], "", "الألم يقل والرئة السليمة تتمدد."),
  ("For lung expansion in the chronic phase the affected lung is placed:", ["Uppermost", "Downward", "Not important", "Under pressure"], "", "مع segmental breathing."),
  ("Chest X-ray in restrictive disease shows:", ["Opacity / ground-glass", "Hyperlucency", "Flat diaphragm", "Barrel chest"], "", "الرئة فيها هوا قليل."),
 ]),
 ("Suppurative", [
  ("The patients who produce the largest amount of sputum are:", ["Suppurative lung diseases", "Asthma", "Restrictive diseases", "COPD"], "", "عدوى نشطة وتدمير نسيج."),
  ("Bronchiectasis is:", ["Permanent irreversible dilatation of bronchi", "Reversible bronchospasm", "Pleural fluid", "Alveolar destruction only"], "", "من التهاب بكتيري متكرر."),
  ("Purulent sputum with pus occurs in:", ["Lung abscess", "Pleural effusion", "Emphysema", "Asthma"], "dr", "سؤال الامتحان السابق (7)."),
  ("The best investigation for bronchiectasis and lung abscess is:", ["HRCT", "ECG", "Spirometry", "Echo"], "", "High-resolution CT."),
  ("A complication of retained secretions is:", ["Toxemia / septicemia", "Hypertension", "Barrel chest", "DVT"], "", "أسوأ حالة في الصدر."),
  ("Huffing is part of:", ["Active cycle of breathing technique (ACBT)", "Postural drainage", "Percussion", "Spirometry"], "", "عشان البلغم يطلع بأقل مجهود."),
 ]),
])

# ---------------------------------------------------------------- Lecture 7 / Cardiac clinical exam
L("l7", "Cardiac Clinical Examination (Dr. Doaa)", "Cardiac Exam", "📋",
  "تفريغ محاضرة الفحص الإكلينيكي للقلب",
"""
<div class="card"><h4>History</h4><ul>
<li><b>Age:</b><br>• كبار السن ← IHD و MI.<br>• البالغين ← <b>valvular disease من الـ rheumatic fever</b> (streptococci بتبدأ في الحلق، والمريض بيبقى pale).<br>• الأطفال ← congenital: <b>Fallot's tetralogy</b> (PS + RVH + VSD + overriding aorta، والطفل بيقعد squatting و leaning forward)، و<b>PDA</b> (cyanosis).</li>
<li><b>Sex:</b> الرجالة أكتر لحد الـ menopause (حوالي 55 سنة).</li>
<li><b>Occupation:</b> الـ mental stress.</li>
<li><b>Residence:</b> البلهارسيا بتعمل <b>cor pulmonale</b>.</li>
<li><b>Chief complaint:</b> بكلام المريض نفسه من غير مصطلحات طبية، وتحللها بالـ onset والـ course والـ duration.</li>
<li><b>Risk factors of CHD:</b> HTN، DM، obesity، hyperlipidemia (LDL)، smoking، و family congenital.</li></ul></div>

<div class="card"><h4>Cardiac symptoms</h4><ul>
<li><b>Anginal pain:</b> retrosternal و diffuse، بالكف كله، بينتشر للفك والرقبة الشمال، وبيقعد دقايق. لو 30 دقيقة يبقى MI. وبيروح بالـ nitrates.</li>
<li><b>Localized pain</b> بالصباع: myositis، GERD، esophageal spasm.</li>
<li><b>Dyspnea</b>: exertional، orthopnea، PND.<br>• <b>Trepopnea</b>: ضيق نفس وهو نايم على ناحية واحدة، وده في الـ effusion أو الـ pneumothorax. بيحصل وهو نايم على <b>الناحية المصابة</b>، فيرتاح على السليمة.</li>
<li><b>Palpitations</b> = awareness of heartbeat. لو fast regular يبقى atrial، ولو heavy يبقى ventricular.</li>
<li><b>Fatigue</b> من الـ low COP من غير فقدان وعي، أما <b>Syncope</b> فهو فقدان وعي مؤقت من cerebral anoxia. مريض القلب بيقع فجأة <b>من غير عرق</b>، والشخص الطبيعي بيعرق وبتجيله مقدمات.</li>
<li><b>Intermittent claudication</b>: في الـ calf، وبيزيد في الطلوع، وبيتقاس بالـ claudication distance.</li>
<li><b>Cardiac edema</b>: bilateral، dependent (بيزيد بالليل)، pitting. بتضغط 10–15 ثانية على الـ dorsum of foot أو الـ medial malleolus أو الـ shin.</li></ul></div>

<div class="card"><h4>General examination</h4>
<table><tr><th>العلامة</th><th>معناها</th></tr>
<tr><td>Mood</td><td>مريض الصدر عنده anxiety، ومريض القلب عنده depression</td></tr>
<tr><td>Orthopneic (long sitting)</td><td>LSHF</td></tr><tr><td>Squatting و leaning forward</td><td>Fallot's tetralogy</td></tr>
<tr><td>طويل جدًا + sternal depression</td><td>Marfan، ومعاه aortic regurgitation</td></tr><tr><td>Short / dwarf</td><td>Congenital HD</td></tr>
<tr><td>Obese</td><td>RSHF</td></tr><tr><td>Thin</td><td>LSHF</td></tr><tr><td>Inverted pyramid</td><td>Coarctation of aorta</td></tr>
<tr><td>Mitral facies (butterfly، خدود ومناخير حمرا)</td><td>Mitral stenosis</td></tr><tr><td>Pallor</td><td>Rheumatic fever</td></tr>
<tr><td>Jaundice</td><td>Bilirubin أكتر من 3 mg/dL</td></tr>
<tr><td>Central cyanosis</td><td>اللسان والشفايف من جوه</td></tr><tr><td>Peripheral cyanosis</td><td>الأطراف وشحمة الودن</td></tr>
<tr><td>Differential cyanosis (lower limbs بس)</td><td>PDA</td></tr>
<tr><td>Osler's nodes: في كف الإيد، tender، 1–3 cm</td><td>Infective endocarditis</td></tr>
<tr><td>Subcutaneous nodules: على الـ extensor، non-tender</td><td>Rheumatic fever</td></tr>
<tr><td>Puffy eyelids</td><td>RSHF</td></tr><tr><td>Chorea (حركات لا إرادية)</td><td>Rheumatic fever</td></tr>
<tr><td>Clubbing (Schamroth test)</td><td>Loss of angle ← parrot beak ← drumstick</td></tr></table></div>

<div class="card"><h4>Arterial vs Venous pulsation</h4>
<table><tr><th></th><th>Arterial (carotid)</th><th>Venous (JVP)</th></tr>
<tr><td>Site</td><td>Medial</td><td>Lateral</td></tr><tr><td>بيتفحص بـ</td><td>Palpable</td><td>Visible</td></tr>
<tr><td>مع الضربة</td><td>Synchronous</td><td>قبلها أو بعدها</td></tr><tr><td>بالـ posture</td><td>مش بيتأثر</td><td>بيتأثر</td></tr></table></div>

<div class="card"><h4>Hepatojugular (abdominojugular) reflux</h4>
<p>المريض long sitting على <b>45°</b> وراسه لف للشمال، وانت واقف على يمينه. اضغط بإيديك الاتنين على الـ <b>RUQ</b> (فوق الكبد) لمدة <b>دقيقة</b>، وراقب الـ jugular vein. لو اتملت يبقى RSHF أو cirrhosis.</p>
<p class="key">مسطرة أفقية عند الـ suprasternal notch ومسطرة رأسية: لو أقل من <b>7 cm</b> تبقى المشكلة في الكبد، ولو <b>7 cm أو أكتر</b> تبقى في القلب (right side).</p></div>
""",
[
 ("History & symptoms", [
  ("The commonest cardiac problem in adults (young) is:", ["Valvular disease due to rheumatic fever", "MI", "Fallot's tetralogy", "PDA"], "", "كبار السن IHD و MI، والأطفال congenital."),
  ("Fallot's tetralogy includes all EXCEPT:", ["Atrial septal defect", "Pulmonary stenosis", "RV hypertrophy", "Overriding aorta"], "", "الرابعة VSD مش ASD."),
  ("A child adopting squatting / leaning forward position suggests:", ["Fallot's tetralogy", "Asthma", "LSHF", "Marfan"], "", "عشان يقلل الـ heart load."),
  ("The chief complaint is written:", ["In the patient's own words", "As a medical diagnosis", "In Latin terms", "By the physician's interpretation"], "", "يعني متكتبش dyspnea أو epistaxis."),
  ("Trepopnea is dyspnea that occurs:", ["Lying on one (affected) side", "Lying flat", "At night only", "On exertion only"], "", "في الـ effusion والـ pneumothorax."),
  ("Fatigue differs from syncope in that fatigue:", ["Has no loss of consciousness", "Causes transient loss of consciousness", "Is due to cerebral anoxia", "Is always sudden"], "", "الـ Syncope فيه فقدان وعي مؤقت."),
  ("During syncope a cardiac patient characteristically shows:", ["No sweating, sudden collapse", "Profuse sweating with prodromes", "Hyperventilation", "Hypertension"], "", "بسبب الـ low COP."),
  ("Residence in bilharzial areas predisposes to:", ["Cor pulmonale", "Mitral stenosis", "Marfan syndrome", "Coarctation"], "", "Lung problem بيعمل heart effect."),
  ("Males are more liable to heart disease than females until:", ["Menopause (~55 years)", "Puberty", "Age 20", "Pregnancy"], "", "الهرمونات بتحمي الستات."),
 ]),
 ("General examination", [
  ("An obese body build is more seen in:", ["Right side heart failure", "Left side heart failure", "Marfan", "Fallot's"], "", "والـ LSHF بيبقى رفيع."),
  ("Mitral facies (butterfly red cheeks) indicates:", ["Mitral stenosis", "Aortic regurgitation", "PDA", "Rheumatic chorea"], "", "Mitral facies."),
  ("Differential cyanosis (lower limbs only) is seen in:", ["Patent ductus arteriosus", "Fallot's tetralogy", "LSHF", "COPD"], "", "PDA."),
  ("Osler's nodes are:", ["Tender palmar nodules in infective endocarditis", "Non-tender nodules in rheumatic fever", "Signs of COPD", "Signs of DVT"], "", "والـ subcutaneous nodules بتبقى non-tender في الـ RF."),
  ("Inverted pyramid body build indicates:", ["Coarctation of aorta", "Marfan syndrome", "Fallot's", "RSHF"], "", "الجزء العلوي متطور والسفلي ضعيف."),
  ("Puffy eyelids are seen in:", ["Right side heart failure", "Left side heart failure", "Angina", "Asthma"], "", "Systemic venous congestion."),
  ("Jaundice appears when serum bilirubin exceeds:", ["3 mg/dL", "0.5 mg/dL", "10 mg/dL", "1 mg/dL"], "", "حسب المحاضرة."),
  ("Mood of a cardiac patient is usually:", ["Depression", "Anxiety", "Euphoria", "Normal always"], "", "ومريض الصدر عنده anxiety."),
 ]),
 ("Pulsations & HJR", [
  ("Compared with arterial pulsation, venous pulsation is:", ["Lateral, visible and affected by posture", "Medial, palpable and not affected by posture", "Synchronous with heartbeat", "Felt better than seen"], "", "زي الجدول."),
  ("In the hepatojugular reflux test, pressure is applied over:", ["Right upper quadrant (liver) for 1 minute", "Left lower quadrant for 10 s", "Sternum for 5 minutes", "Neck veins"], "", "والمريض على 45°."),
  ("If the jugular distension level is ≥ 7 cm, the problem is:", ["Cardiac (right side)", "Hepatic", "Pulmonary", "Normal"], "", "أقل من 7 cm يبقى كبد."),
 ]),
])
