# tools/generators/hydrotherapy/data_hydro.py
# Course: Hydrotherapy (Code: 130120) — Faculty of Physical Therapy, Kafr El-Sheikh University
# 2nd Year, 1st Semester Midterm & Question Bank
# Generated according to PT Course Builder Skill (PT Hub Standard)

META = {
    'title': 'Hydrotherapy — مراجعة وبنك أسئلة الميدتيرم',
    'badge': '🌊 Hydrotherapy · Faculty of Physical Therapy',
    'h1': 'مراجعة وبنك أسئلة الهيدرو',
    'subtitle': 'Physical Properties · Immersion Physiology · Modalities · Mud Therapy · Cryotherapy · Past Exams & Platform',
    'statnum': 7,
    'statlabel': 'أقسام شاملة'
}

TABS = []
def T(*a): TABS.append(a)

# ==============================================================================
# TAB 1: Physical & Mechanical Properties of Water
# ==============================================================================
SUM_L1 = """
<div class="card"><h4>🌊 1. مقدمة وتعريف الهيدروثيرابي (Introduction)</h4>
<ul>
<li>كلمة <b>Hydrotherapy</b> يونانية الأصل: <b>Hydro</b> تعني مياه (water)، و <b>Therapeia</b> تعني شفاء أو علاج (healing).</li>
<li><b>التعريف العلمي:</b> Therapeutic modality بتستخدم الميه بأي صورة أو درجة حرارة (سخنة، باردة، بخار، سائل، تلج) لعلاج المشاكل الجسدية (physical) أو النفسية (psychological).</li>
<li><b>التركيب الكيميائي:</b> جزيء قطبي (polar) بيتكون من <b>ذرتين هيدروجين وذرة أكسجين</b> (<span dir="ltr">H₂O</span>). الميه ليها قدرة إذابة عالية جداً، وده بيسمح بإضافة مواد علاجية أو أعشاب في العناية بالجروح.</li>
</ul></div>

<div class="card"><h4>⚖️ 2. الكثافة النوعية والطفو (Specific Gravity & Buoyancy)</h4>
<ul>
<li><b>Specific Gravity (Relative Density):</b> النسبة بين كثافة المادة لكثافة الميه النقية عند <span dir="ltr">4°C</span>. الكثافة النوعية <b>dimensionless</b> (ملهاش وحدة قياس)، بينما الكثافة العادية ليها وحدة (<span dir="ltr">g/cm³</span> أو <span dir="ltr">kg/m³</span>).</li>
<li><b>كثافة الميه النقية</b> = <span dir="ltr">1.0</span> عند <span dir="ltr">4°C</span>.</li>
<li><b>كثافة جسم الإنسان (Human Body)</b> = <span dir="ltr">0.974</span> في المتوسط.</li>
<li><b>قاعدة الطفو والغوص:</b>
  <ul>
    <li>أي جسم كثافته النوعية <b>أقل من 1.0 بيطفو (floats)</b> على السطح — عشان كده جسم الإنسان بيطفو في الميه!</li>
    <li>أي جسم كثافته النوعية <b>أكبر من 1.0 بيغوص (sinks)</b> (زي العضلات المشدودة أو الأجسام المعدنية).</li>
    <li>ميه البحر (<span dir="ltr">Sea water</span>) ممتلئة أملاح فكثافتها أعلى، فالطفو فيها أسهل من ميه النهر (<span dir="ltr">River water</span>).</li>
  </ul>
</li>
<li><b>Archimedes' Principle (Buoyancy):</b> أي جسم مغمور كلياً أو جزئياً في سائل يتعرض لقوة دفع لأعلى (upward thrust) تساوي تماماً وزن السائل المزاح بواسطة الجسم.</li>
<li><b>Center of Buoyancy (COB):</b> مركز ثقل حجم السائل المزاح (في الصدر تقريباً)، بينما <b>Center of Gravity (COG)</b> بيكون عند الفقرة العجزية التانية (<span dir="ltr">S2</span>). لما بيكونوا على خط رأسي واحد، الجسم بيفضل متزن في الميه.</li>
</ul>
<p class="key">💡 <b>تريكة امتحان:</b> كل ما درجة الحرارة تزيد، كثافة الميه بتقل وحجمها بيزيد. الاستثناء الوحيد هو إن الميه بتوصل لأقصى كثافة عند <span dir="ltr">3.98°C</span> (أو <span dir="ltr">4°C</span> تقريباً).</p>
</div>

<div class="card"><h4>🌊 3. الضغط الهيدروستاتيكي وقانون باسكال (Hydrostatic Pressure)</h4>
<ul>
<li><b>Pascal's Law:</b> الضغط الواقع على أي سائل ساكن بيتوزع بالتساوي في جميع الاتجاهات وعلى جميع أسطح الجسم المغمور عند عمق معين، ويزداد الضغط طردياً مع زيادة العمق.</li>
<li><b>معدل الضغط:</b> الميه بتولد ضغط مقداره <span dir="ltr">22.4 mm Hg</span> لكل قدم عمق (<span dir="ltr">1.36 cm / 0.54 inch</span>).</li>
<li>عند عمق <span dir="ltr">48 inches</span> (يعني 4 أقدام)، الضغط بيوصل لحوالي <span dir="ltr">88.9 – 89.6 mm Hg</span>!</li>
<li><b>تأثير معجون السنان (Toothpaste Effect):</b> لأن الضغط عند الرجلين في القاع أعلى بكتير من الضغط عند الكتفين والرقبة، الميه بتعصر السوائل والدم من الأطراف السفلية لفوق باتجاه الصدر والقلب!</li>
</ul></div>

<div class="card"><h4>🌪️ 4. اللزوجة والمقاومة والديناميكا الحرارية (Viscosity & Thermodynamics)</h4>
<table>
<tr><th>الخاصية</th><th>المعنى والتطبيق الإكلينيكي في العلاج الطبيعي</th></tr>
<tr><td><b>Viscosity (اللزوجة)</b></td><td>الاحتكاك الداخلي بين جزيئات السائل. كل ما المريض يتحرك أسرع في الميه، المقاومة بتزيد. <b>بتقل اللزوجة مع ارتفاع حرارة الميه</b> (يعني الميه الدافية مقاومتها أقل سنة من الباردة).</td></tr>
<tr><td><b>Turbulence & Eddy Currents</b></td><td>التيارات الدوامية المتولدة من الحركة السريعة. حركة غير منتظمة بتزود المقاومة وتساعد في المساج والاسترخاء وتخفيف التقلص العضلي.</td></tr>
<tr><td><b>Surface Tension & Cohesion</b></td><td>قوة التجاذب بين جزيئات السائل نفسه اسمها <b>Cohesion</b>. على السطح بتعمل غشاء مرن مقاوم لاختراق السطح اسمه <b>Surface Tension</b>.</td></tr>
<tr><td><b>Specific Heat (السعة الحرارية)</b></td><td>السعة الحرارية للماء = <span dir="ltr">1.0</span>، بينما الهواء = <span dir="ltr">0.001</span>. ده معناه إن <b>الميه بتحتفظ وتنقل الحرارة بمقدار 1000 ضعف حجم مماثل من الهواء</b>!</td></tr>
</table>
</div>
"""

QS_L1 = [
    ("Hydrotherapy is derived from Greek words, where 'hydro' means water and 'therapeia' means:",
     ["Healing", "Exercise", "Cold", "Warming"], "imp", "أصل الكلمة يوناني: hydro تعني مياه و therapeia تعني شفاء أو علاج."),
    ("Pure water is chemically a polar molecule composed of:",
     ["2 hydrogen molecules and 1 oxygen molecule", "1 hydrogen molecule and 2 oxygen molecules", "2 nitrogen and 1 hydrogen", "Carbon and oxygen"], "imp", "تركيب الماء H2O (ذرتين هيدروجين وذرة أكسجين)."),
    ("Specific gravity (relative density) is scientifically defined as:",
     ["The ratio of the density of a substance to the density of pure water at 4°C", "The total weight of an object in kilograms", "The volume of fluid displaced divided by air pressure", "The friction between molecules of a fluid"], "imp", "الكثافة النوعية هي نسبة كثافة المادة لكثافة الماء عند 4 درجات مئوية."),
    ("The specific gravity of pure water at 4°C is 1.0, while the average specific gravity of the human body is:",
     ["0.974", "1.050", "0.794", "1.200"], "imp", "كثافة جسم الإنسان في المتوسط 0.974، ولأنها أقل من 1.0 فإن جسم الإنسان يطفو في الماء."),
    ("An object placed in water will generally FLOAT on the surface if its specific gravity is:",
     ["Less than 1.0", "Greater than 1.0", "Exactly equal to 2.0", "Above 1.5"], "imp", "القاعدة الفيزيائية: أقل من 1 يطفو، أكبر من 1 يغوص."),
    ("An object with a specific gravity of 1.20 placed in fresh water will:",
     ["Sink", "Float high above the surface", "Remain suspended at the very top", "Become completely weightless"], "qz", "سؤال المنصة: بما أن 1.2 أكبر من 1.0 فإن الجسم سيغوص (Sink)."),
    ("Which statement correctly distinguishes specific gravity from density?",
     ["Specific gravity is dimensionless (has no units)", "Density has no units", "Specific gravity is measured in kg/m3", "Density does not depend on volume"], "qz", "سؤال المنصة: الكثافة النوعية نسبة بين كثافتين لذلك ليس لها وحدة قياس (dimensionless)."),
    ("Why is swimming or floating in seawater easier than in river (fresh) water?",
     ["Seawater contains dissolved salts giving it higher density and greater buoyancy", "River water has higher specific gravity than seawater", "Seawater has lower viscosity than fresh water", "River water contains zero buoyant force"], "qz", "امتحان 2021: مياه البحر فيها أملاح فكثافتها أعلى وبالتالي قوة الدفع والطفو فيها أكبر من مياه النهر العذبة."),
    ("According to Archimedes' principle, an immersed body experiences an upward buoyant force equal to:",
     ["The weight of the fluid displaced by the body", "Twice the patient's dry body weight", "The atmospheric pressure above the water surface", "The surface tension of the fluid"], "imp", "قاعدة أرشميدس: قوة الدفع لأعلى = وزن السائل المزاح."),
    ("Where is the Center of Buoyancy (COB) located in the human body compared to the Center of Gravity (COG)?",
     ["COB is located in the chest area, while COG is near S2", "Both are located at the navel", "COB is in the pelvis and COG is in the head", "COB is at the feet and COG is at the shoulders"], "imp", "مركز الطفو في منطقة الصدر (حيث الرئتين الممتلئتين بالهواء)، بينما مركز الثقل عند الفقرة العجزية الثانية S2."),
    ("According to Pascal's Law, hydrostatic pressure on an immersed body at rest:",
     ["Is exerted equally on all surfaces at a given depth and increases with depth", "Acts only in a downward vertical direction", "Decreases proportionally as depth increases", "Acts only on body parts in motion"], "imp", "قانون باسكال: الضغط يتوزع بالتساوي في كل الاتجاهات ويزداد طردياً مع العمق."),
    ("Water exerts hydrostatic pressure at a rate of 22.4 mm Hg per:",
     ["Foot of depth (approx. 1.36 cm or 0.54 inch)", "Meter of depth", "Millimeter of depth", "Yard of depth"], "imp", "معدل زيادة الضغط الهيدروستاتيكي هو 22.4 مم زئبق لكل قدم عمق."),
    ("A human body immersed in water to a depth of 48 inches (4 feet) is subject to hydrostatic force equal to approximately:",
     ["88.9 to 89.6 mm Hg", "24.5 mm Hg", "150.2 mm Hg", "12.4 mm Hg"], "qz", "امتحان 2021 و 2018: العمق 48 بوصة = 4 أقدام × 22.4 = حوالي 88.9 إلى 89.6 مم زئبق."),
    ("The 'toothpaste tube effect' during vertical immersion refers to:",
     ["Greater pressure at greater depths squeezing venous blood and fluids upward toward the chest", "Water entering body orifices under pressure", "Rapid loss of body electrolytes through the skin", "The uniform cooling of extremities"], "imp", "لأن الضغط عند القدمين في القاع أكبر بكثير من السطح، يتم دفع وعصر السوائل والدم لأعلى باتجاه الصدر والقلب."),
    ("Viscosity of a fluid is defined as its:",
     ["Internal friction between fluid molecules", "Ability to conduct electrical currents", "Surface resistance to evaporation", "Rate of thermal expansion"], "imp", "اللزوجة هي الاحتكاك الداخلي بين جزيئات السائل."),
    ("As water temperature rises from cool to hot, water viscosity:",
     ["Decreases", "Increases significantly", "Remains absolutely unchanged", "Doubles every 5°C"], "qz", "سؤال المنصة: بارتفاع درجة حرارة الماء تقل لزوجته (Decreases)."),
    ("Which adjustment generally increases movement resistance when exercising a limb in water?",
     ["Increasing the speed of movement and increasing the surface area", "Moving very slowly with streamlined limb position", "Decreasing limb frontal surface area", "Heating the pool to high temperatures"], "qz", "سؤال المنصة: زيادة سرعة الحركة وزيادة المساحة المواجهة للماء تزيد المقاومة بشكل كبير."),
    ("The attractive force between molecules of the same substance is called:",
     ["Cohesion", "Adhesion", "Surface tension", "Specific heat"], "qz", "سؤال المنصة: التجاذب بين جزيئات نفس المادة هو Cohesion (بينما بين مادتين مختلفتين هو Adhesion)."),
    ("The force at a liquid surface that behaves like an elastic skin is called:",
     ["Surface tension", "Hydrostatic pressure", "Buoyancy", "Turbulence"], "qz", "سؤال المنصة: التوتر السطحي Surface tension هو الغشاء المرن على سطح السائل."),
    ("How many times more heat does water hold compared to an equivalent volume of air?",
     ["Approximately 1,000 times more", "10 times more", "50 times more", "100 times more"], "qz", "امتحان 2022 و 2018: السعة الحرارية للماء 1.0 مقابل 0.001 للهواء، فالماء يحتفظ بالحرارة 1000 ضعف الهواء."),
    ("At what temperature does liquid water reach its maximum density?",
     ["3.98°C (approx. 4°C)", "0°C", "10°C", "100°C"], "imp", "تصل المياه لأقصى كثافة عند 3.98 درجة مئوية (فوقها أو تحتها يقل تركيز الكثافة ويتمدد الحجم)."),
    ("A patient with weak lower-limb muscles performs hip flexion in water. Which property assists the upward movement?",
     ["Buoyancy", "Viscosity", "Turbulence", "Hydrostatic pressure"], "qz", "سؤال المنصة: قوة الطفو Buoyancy تدفع الطرف لأعلى مع اتجاه السطح فتساعد العضلات الضعيفة."),
    ("Turbulence in water is characterized by:",
     ["Irregular rotary movements called eddy currents", "Perfect parallel laminar flow", "Zero fluid resistance", "Complete absence of friction"], "imp", "الاضطراب Turbulence يتميز بتيارات دوامية Eddy currents غير منتظمة."),
    ("In hydrotherapy, desensitization of hypersensitive scars can be achieved mechanically by:",
     ["Water turbulence and agitation", "Stationary cold water", "Complete bed rest", "Deep water spinal traction"], "imp", "التيارات المائية والفقاعات توفر تحفيزاً لمسياً حسياً يساعد في إزالة التحسس المفرط."),
    ("A therapist wants to use water pressure to assist in lower limb edema management. Which physical property is most relevant?",
     ["Hydrostatic pressure", "Surface tension", "Cohesion", "Thermal capacity"], "qz", "سؤال المنصة: الضغط الهيدروستاتيكي هو المسؤول عن عصر السوائل وتصريف الوذمة (Edema)."),
]
T("l1", "Lec 1 — الخصائص الفيزيائية والميكانيكية للماء", "Lec 1 الخصائص الفيزيائية", "🌊", "سلايدات أ.د. محمود عويضة + بنك المنصة", SUM_L1, [("الخصائص الفيزيائية والميكانيكية والطفو", QS_L1)])


# ==============================================================================
# TAB 2: Physiological Effects of Immersion
# ==============================================================================
SUM_L2 = """
<div class="card"><h4>❤️ 1. الجهاز الدوري والقلب (Cardiovascular Effects)</h4>
<ul>
<li><b>Central Blood Shift:</b> لما المريض ينزل في الميه لحد الرقبة (<span dir="ltr">C7</span>)، الضغط الهيدروستاتيكي بيعصر الأوردة وينقل حوالي <span dir="ltr">700 ml</span> من الدم من الأطراف للأوعية الدموية المركزية والقلب.</li>
<li><b>ارتفاع الضغط الوريدي المركزي (CVP):</b> الـ <span dir="ltr">CVP</span> بيرتفع بشكل ملحوظ مع امتلاء الأذين الأيمن.</li>
<li><b>Stroke Volume & Cardiac Output:</b>
  <ul>
    <li>حجم الضربة (<span dir="ltr">Stroke Volume</span>) بيزيد بنسبة <span dir="ltr">35%</span> تقريباً.</li>
    <li>النتاج القلبي (<span dir="ltr">Cardiac Output</span>) بيزيد بنسبة <span dir="ltr">30% إلى 60%</span> (بيزيد من <span dir="ltr">5 L/min</span> في الراحة ليوصل لحوالي <span dir="ltr">8.6 L/min</span> أثناء الغمر)!</li>
  </ul>
</li>
<li><b>معدل ضربات القلب (Heart Rate):</b> في الميه المتعادلة أو الدافية (<span dir="ltr">Thermoneutral</span>) ضربات القلب بتفضل ثابتة أو تقل سنة بسيطة، بينما في الميه السخنة جداً بتزيد لتعويض التمدد الوعائي.</li>
<li><b>تدفق الدم للعضلات:</b> الغمر لحد الرقبة بيزود تدفق الدم للعضلات في وضع الراحة بنسبة <span dir="ltr">100% إلى 225%</span>، وده بيسرّع التخلص من الفضلات الأيضية وتغذية الأنسجة.</li>
</ul></div>

<div class="card"><h4>🫁 2. الجهاز التنفسي (Pulmonary System)</h4>
<ul>
<li><b>زيادة المجهود التنفسي (Work of Breathing):</b> ضغط الميه الخارجي على جدار الصدر والبطن بيعاكس تمدد القفص الصدري، وده بيزود الشغل المطلوب للتنفس بنسبة <span dir="ltr">60%</span>!</li>
<li><b>السعة الحيوية (Vital Capacity):</b> <b>بتقل بنسبة 6% إلى 9%</b> بسبب ضغط الميه وزيادة حجم الدم في الأوعية الرئوية.</li>
<li><b>استخدام عضلات التنفس المساعدة:</b> المريض بيحتاج يشغل الـ accessory muscles of respiration، وده تمرين ممتاز لتقوية عضلات التنفس لمرضى التأهيل التنفسي، بس محتاج حذر مع مرضى الـ COPD الشديد أو فشل القلب الاحتقاني.</li>
</ul></div>

<div class="card"><h4>🚽 3. الجهاز البولي وإدرار البول (Renal System & Diuresis)</h4>
<ul>
<li><b>Suppression of ADH:</b> لما الدم يتجمع في الصدر والأذين، مستقبلات الضغط في القلب (<span dir="ltr">atrial stretch receptors</span>) بتحس إن الجسم عنده سوائل زايدة، فتبعت إشارات للمخ توقف إفراز هرمون منع إدرار البول (<b>ADH suppression</b>) وتقلل الـ aldosterone، وتفرز الـ ANP.</li>
<li><b>زيادة إدرار البول (Diuresis):</b> معدل البول الطبيعي حوالي <span dir="ltr">0.034 oz (1 ml/min)</span>. أثناء الغمر الرأسي بيزيد إلى <span dir="ltr">0.21 – 0.26 oz (6.2 – 7.6 ml/min)</span> — يعني <b>زيادة 7 أضعاف (7-fold increase)</b>!</li>
<li><b>زيادة إخراج الصوديوم والبوتاسيوم:</b> بيزيد التخلص من الصوديوم (<span dir="ltr">natriuresis</span>) والبوتاسيوم وتنقية الكرياتينين.</li>
</ul>
<p class="key">⚠️ <b>قاعدة السلامة في الجلسات:</b> مدة جلسة التمارين المائية لا تتعدى <span dir="ltr">45 دقيقة</span> (<span dir="ltr">≤ 45 min</span>) عشان سعة المثانة وإجهاد المريض وتجنب الجفاف.</p>
</div>

<div class="card"><h4>🦴 4. الجهاز العضلي الهيكلي والتحميل (Musculoskeletal System)</h4>
<ul>
<li><b>تقليل التحميل على المفاصل (Unweighting):</b>
  <ul>
    <li>الغمر لمستوى الرقبة (<span dir="ltr">C7</span>): الجسم بيتحمل فقط <b>10%</b> من وزنه (تخفيف 90%).</li>
    <li>الغمر لمستوى الـ Xiphoid process: الجسم بيتحمل <b>30%</b> إلى <b>33%</b> من وزنه.</li>
    <li>الغمر لمستوى الحوض / السرة (<span dir="ltr">ASIS</span>): الجسم بيتحمل حوالي <b>50%</b> من وزنه.</li>
  </ul>
</li>
<li>الطفو بيقلل الإجهاد الميكانيكي على الغضاريف والمفاصل، وده بيسمح لمرضى خشونة الركبة والديسك بالمشي والحركة المبكرة بدون ألم.</li>
<li><b>تسكين الألم (Pain Relief):</b> الحرارة والمساج وضغط الميه بينبهوا مستقبلات اللمس السريعة (<span dir="ltr">A-beta fibers</span>) فتقفل بوابة الألم في الحبل الشوكي حسب نظرية <b>Gate Control Theory</b>.</li>
</ul></div>
"""

QS_L2 = [
    ("Upon vertical neck-level immersion, what specific cardiac hormone is released in response to atrial stretching?",
     ["Atrial Natriuretic Peptide (ANP)", "Renin", "Epinephrine", "Thyroxine"], "imp", "تمدد جدار الأذين ينبه إفراز هرمون ANP الذي يزيد إخراج الصوديوم والماء في البول."),
    ("How does vertical water immersion affect systemic vascular resistance (SVR)?",
     ["Decreases slightly or remains stable in warm water due to peripheral vasodilation", "Increases by 500%", "Causes immediate vascular collapse", "Stops venous blood flow"], "imp", "في الماء الدافئ المعتدل يتوازن الضغط ويقل المقاومة الوعائية الكلية SVR."),
    ("Creatinine clearance during neck-level water immersion is clinically observed to:",
     ["Increase significantly as renal perfusion rises", "Decrease by half", "Drop to absolute zero", "Remain completely unmeasurable"], "imp", "زيادة تروية الكليتين ترفع معدل فلترة وتصفية الكرياتينين Creatinine clearance."),
    ("At what water depth is weight-bearing on the lower extremities reduced to exactly 50%?",
     ["Immersion to the level of the ASIS / waist", "Immersion to the ankle", "Immersion to the chin", "Immersion to the knees"], "imp", "عند مستوى عظام الحوض ASIS أو الوسط يتحمل المريض 50% من وزن جسمه فقط."),
    ("The reduction of joint compression force during water immersion is directly caused by:",
     ["Buoyancy counteracting gravitational downward force", "Water viscosity resisting movement", "Hydrostatic pressure pushing sideways only", "Water salinity"], "imp", "قوة الطفو Buoyancy تدفع الجسم لأعلى فتعاكس الجاذبية وتخفف الضغط عن الغضاريف والمفاصل."),

    ("During vertical water immersion up to the neck (C7 level), central venous pressure (CVP):",
     ["Increases significantly as blood is displaced toward the chest", "Decreases to zero", "Remains completely unchanged", "Fluctuates erratically"], "imp", "الضغط الهيدروستاتيكي يضغط الأوردة وينقل الدم نحو الصدر فيرتفع الضغط الوريدي المركزي CVP."),
    ("During neck-depth immersion, cardiac output increases by approximately:",
     ["30% to 60% (from ~5 L/min to ~8.6 L/min)", "5% only", "200% to 300%", "It decreases by half"], "qz", "امتحان 2022: يزيد النتاج القلبي من 5 لتر/دقيقة إلى حوالي 8.6 لتر/دقيقة (زيادة 30-60%)."),
    ("How does neck-depth water immersion affect the pulmonary system?",
     ["Decreases vital capacity by 6–9% and increases total work of breathing by ~60%", "Increases vital capacity by 25%", "Decreases the work of breathing by half", "Expands lung total compliance dramatically"], "imp", "امتحان 2022 و 2018: يضغط الماء على جدار الصدر والبطن فتقل السعة الحيوية 6-9% ويزداد جهد التنفس 60%."),
    ("Normal urine production is about 1 ml/min. During vertical water immersion, it increases up to:",
     ["6.2 to 7.6 ml/min (a 7-fold increase)", "20 to 30 ml/min", "1.5 ml/min", "Zero (anuria)"], "qz", "امتحان 2022 و 2018 و 2021: يزداد إدرار البول حوالي 7 أضعاف من 1 مل/دقيقة إلى 6.2 - 7.6 مل/دقيقة."),
    ("The primary endocrine mechanism behind immersion-induced diuresis is:",
     ["Suppression of antidiuretic hormone (ADH) and aldosterone", "Stimulation of ADH and renin", "Massive release of epinephrine", "Inhibition of atrial natriuretic peptide (ANP)"], "imp", "تجمع الدم في الأذين ينبه مستقبلات الضغط فيثبط هرمون ADH والـ Aldosterone فيحدث إدرار البول."),
    ("To accommodate patient bladder tolerance and prevent fatigue, aquatic therapy pool sessions should NOT exceed:",
     ["45 minutes", "15 minutes", "90 minutes", "120 minutes"], "qz", "امتحان 2021 و 2018: يجب ألا تزيد جلسة التمارين المائية عن 45 دقيقة."),
    ("When an individual is immersed in water up to the neck (C7), weight-bearing on lower extremity joints is reduced to approximately:",
     ["10% of total body weight", "50% of total body weight", "75% of total body weight", "0% (pure vacuum)"], "imp", "الغمر لمستوى الرقبة C7 يقلل وزن الجسم المحمول إلى 10% فقط (الطفو يحمل 90%)."),
    ("At the level of the xiphoid process, weight-bearing on the lower extremities is approximately:",
     ["30% to 33% of body weight", "10% of body weight", "70% of body weight", "90% of body weight"], "imp", "عند مستوى عظمة القص Xiphoid process يتحمل الجسم ثلث وزنه فقط (30-33%)."),
    ("At the level of the ASIS (waist/pelvis), weight-bearing is reduced to approximately:",
     ["50% of total body weight", "10% of total body weight", "25% of total body weight", "80% of total body weight"], "imp", "عند مستوى الحوض أو السرة يتحمل الجسم نصف وزنه (50%)."),
    ("Neck-level water immersion increases resting muscle blood flow by approximately:",
     ["100% to 225%", "10% to 15%", "300% to 400%", "Zero change"], "imp", "امتحان 2022: يزيد تدفق الدم للعضلات في وضع الراحة بنسبة 100% إلى 225% بفعل الحرارة والضغط."),
    ("During relaxation states in water, heart rate variability demonstrates an autonomic shift toward:",
     ["Vagal or parasympathetic nervous system control", "Extreme sympathetic adrenergic dominance", "Complete sinus arrest", "Thyroid storm"], "qz", "امتحان 2022 و 2018: الاسترخاء في الماء يوجه الجهاز العصبي نحو النشاط الباراسمبثاوي (Vagal/Parasympathetic)."),
    ("Water immersion is beneficial for chronic edema management primarily because:",
     ["Hydrostatic pressure compresses superficial veins and lymphatics to move interstitial fluid centrally", "Water dissolves interstitial fluid directly through the epidermis", "Buoyancy eliminates all fluid gravity completely", "Cold water stops arterial circulation entirely"], "imp", "الضغط الهيدروستاتيكي يضغط الأوعية اللمفاوية والوريدية السطحية ليعيد السوائل المترسبة للدورة الدموية."),
    ("According to the Gate Control Theory, hydrotherapy relieves pain because:",
     ["Agitation and water pressure stimulate large A-beta sensory fibers, blocking pain signals at the spinal cord", "Water destroys sensory nerve endings", "Heat paralyzes motor units permanently", "Cold eliminates brain pain perception entirely"], "imp", "التحفيز اللمسي من الميه وحركتها ينبه ألياف A-beta التي تغلق بوابة الألم في النخاع الشوكي."),
    ("Which of the following patients is at RISK during full neck-level water immersion due to increased cardiac preload?",
     ["Severe decompensated Congestive Heart Failure (CHF)", "Mild quadriceps spasm", "Old ankle sprain", "Controlled healed humerus fracture"], "imp", "مرضى فشل القلب الاحتقاني غير المستقر CHF لأن عودة 700 مل دم فجأة للقلب قد تسبب أزمة قلبية."),
    ("In patients with severe lung disease (e.g. low vital capacity), hydrotherapy immersion requires caution because:",
     ["Hydrostatic pressure on the chest increases work of breathing and reduces lung compliance", "Water causes immediate pleural effusion", "Buoyancy collapses the trachea", "Viscosity stops diaphragm contraction"], "imp", "ضغط الماء على الصدر يقلل السعة الحيوية ويزيد جهد التنفس بنسبة 60%."),
]
T("l2", "Lec 2 — التأثيرات الفسيولوجية للغمر المائي", "Lec 2 فسيولوجيا الغمر", "🫀", "سلايدات الكلية + بنك الأسئلة المعتمد", SUM_L2, [("تأثيرات الغمر على القلب والتنفس والكلى", QS_L2)])


# ==============================================================================
# TAB 3: Thermal Modalities (Hydrocollator, Paraffin, Whirlpool & Contrast)
# ==============================================================================
SUM_L3 = """
<div class="card"><h4>♨️ 1. الكمادات الساخنة (Hydrocollator Packs)</h4>
<ul>
<li><b>التركيب:</b> وحدات تسخين أوتوماتيكية بتحتوي على كمادات قطنية محشوة بحبيبات جل السيليكا (<b>silica gel</b>) القادرة على امتصاص كميات هائلة من الميه والاحتفاظ بالحرارة لفترة طويلة.</li>
<li><b>درجة حرارة الخزان:</b> الميه جوه الخزان بتكون عند حرارة <span dir="ltr">160–170°F</span> (<span dir="ltr">71–79°C</span>).</li>
<li><b>ارتفاع درجات الحرارة في الأنسجة (موضع امتحان دقيق!):</b>
  <ul>
    <li>الجلد (<span dir="ltr">Skin</span>): بيرتفع حتى <b>20°F</b>.</li>
    <li>الأنسجة تحت الجلد (<span dir="ltr">Subcutaneous tissue</span>): بترتفع حتى <b>15°F</b>.</li>
    <li>العضلات العميقة اللي تحتها (<span dir="ltr">Muscle tissue underneath</span>): بترتفع حتى <b>6°F فقط</b>!</li>
  </ul>
</li>
<li><b>النوع:</b> حرارة رطبة (<b>Moist heat</b>) — مش جافة (Dry heat)!</li>
<li><b>التأثيرات:</b> مسكن آمن (sedative & analgesic)، باسط للعضلات، بيزود مطاطية الكولاجين، وبيعمل counter-irritant effect.</li>
<li><b>موانع الاستخدام:</b> فقدان الإحساس، الجلطة الوريدية العميقة (<span dir="ltr">DVT</span>)، القرح المفتوحة، الأورام، الالتهاب الحاد، والحساسية الشديدة.</li>
</ul></div>

<div class="card"><h4>🕯️ 2. شمع البرافين (Paraffin Wax Therapy)</h4>
<ul>
<li><b>النسبة الذهبية للخلط:</b> <b>4 أجزاء شمع برافين : 1 جزء زيت معدني (4:1)</b>.</li>
<li><b>ليه بنضيف زيت البرافين؟</b>
  <ol>
    <li>بيقلل درجة انصهار الشمع من <span dir="ltr">54°C (129°F)</span> لـ <span dir="ltr">45–50°C (113–122°F)</span> فيخليه سائل ومريح وميحرقش المريض.</li>
    <li>بيخلي الشمع يفضل سائل وطري عند حرارات منخفضة، وبيسهل تقشيره وينعم الجلد.</li>
  </ol>
</li>
<li><b>ارتفاع الحرارة:</b> بعد 30 دقيقة لف، حرارة الجلد بتزيد <span dir="ltr">8–13°C</span>، واللفافة تحت الجلد <span dir="ltr">5°C</span>، والعضلات السطحية <span dir="ltr">2–3°C</span>.</li>
<li><b>طرق التطبيق:</b>
  <ul>
    <li><b>Dip-and-wrap:</b> غمس الطرف (الإيد أو القدم) من <span dir="ltr">8 إلى 12 مرة</span> لتكوين طبقة قفاز سميكة، ثم لفه بكيس وفوطة لمدة <span dir="ltr">20 دقيقة</span>.</li>
    <li><b>Dip-and-immerse:</b> غمس الطرف ثم تركه مغموراً في الحمام.</li>
    <li><b>Painting:</b> دهان الشمع بالفرشاة للمناطق اللي مبيعرفش يغمسها (زي الركبة أو الكتف).</li>
  </ul>
</li>
<li><b>الاستخدام الأساسي:</b> تيبس مفاصل الإيدين والقدمين، الروماتويد في المراحل غير الحادة، الالتصاقات وندبات الحروق لتليينها قبل التمارين.</li>
</ul></div>

<div class="card"><h4>🌀 3. حمامات الدوامات المائية (Whirlpool Tanks)</h4>
<ul>
<li><b>التعريف:</b> خزانات مصنوعة من الستانلس ستيل (<span dir="ltr">stainless-steel</span>) مزودة بتوربينات (<span dir="ltr">turbines</span>) تخلط الهواء مع الماء لتوليد تيار مائي دوار.</li>
<li><b>أنواع الخزانات:</b>
  <ol>
    <li><b>Extremity Tank:</b> مخصص لعلاج طرف واحد (إيد أو رجل) أو الطرفين السفليين من تحت الركبة.</li>
    <li><b>Lowboy Tank:</b> خزان منخفض وطويل، المريض بيقعد فيه بوضع <span dir="ltr">long-sitting</span> والميه بتوصل لمستوى الصدر السفلي، ويقدر يعمل تمارين ثني وفرد للركبتين.</li>
    <li><b>Highboy Tank:</b> خزان عميق، المريض بيقعد فيه وركبه وفخذيه مثنيين (<span dir="ltr">flexed hips and knees</span>) والميه بتوصل للصدر.</li>
    <li><b>Hubbard Tank:</b> خزان كبير على شكل فراشة (<span dir="ltr">figure-8</span>) لغمر الجسم بالكامل ونقل المريض بالرافعة.</li>
  </ol>
</li>
<li><b>الاستخدامات:</b> تنظيف الجروح وإزالة الأنسجة الميتة والصديد (mechanical debridement)، تليين الالتصاقات بعد الجبس، تسكين التقلصات، وتسهيل الحركة المائية.</li>
<li><b>موانع الاستخدام:</b> أمراض الأوعية الدموية الطرفية المتقدمة (<span dir="ltr">PVD</span>)، الدوالي الشديدة، تصلب الشرايين المتقدم.</li>
</ul></div>

<div class="card"><h4>🔄 4. حمامات التباين (Contrast Baths)</h4>
<ul>
<li><b>الفكرة:</b> غمر الطرف بالتناوب بين الماء الساخن والماء البارد لإحداث تمدد وانقباض وعائي متعاقب.</li>
<li><b>درجات الحرارة الرسمية:</b>
  <ul>
    <li>الماء الساخن: <span dir="ltr">100–105°F</span> (<span dir="ltr">40–45°C</span>).</li>
    <li>الماء البارد: <span dir="ltr">59–68°F</span> (<span dir="ltr">15–20°C</span>).</li>
  </ul>
</li>
<li><b>النسبة والزمن (3:1 أو 4:1):</b>
  <ul>
    <li>البداية بالماء الدافئ لمدة <span dir="ltr">4 إلى 6 دقائق</span>.</li>
    <li>ثم الماء البارد لمدة <span dir="ltr">1 إلى 4 دقائق</span>.</li>
    <li>تكرار الدورة 4 مرات، بإجمالي زمن علاج <span dir="ltr">15 إلى 30 دقيقة</span>.</li>
    <li><b>القاعدة الذهبية للإنهاء:</b> بننهي بالماء الدافئ لزيادة المرونة وتخفيف الألم، أو بننهي بالبارد لو الهدف تقليل الارتشاح والوذمة.</li>
  </ul>
</li>
<li><b>Vascular Flush / Circulatory Whip:</b> التعاقب السريع بين التمدد والانقباض يضخ الدم ويزيد التدفق الموضعي بنسبة تصل إلى <b>100%</b>!</li>
<li><b>الاستخدامات:</b> تورم ما بعد الإصابات والكسور (<span dir="ltr">post-traumatic edema</span>)، الآلام العصبية، متلازمة الألم الناحي المركب (<span dir="ltr">CRPS / Reflex Sympathetic Dystrophy</span>)، والتهاب الأوتار المزمن.</li>
</ul></div>
"""

QS_L3 = [
    ("What is the recommended water temperature for a whirlpool bath when treating OPEN WOUNDS or burns?",
     ["Neutral warm: 92°F to 96°F (33.5°C to 35.5°C)", "Very hot: 110°F to 115°F", "Ice cold: 40°F to 50°F", "Boiling: 212°F"], "imp", "لعلاج الجروح المفتوحة والحروق تستخدم حرارة معتدلة Neutral warm (33.5 - 35.5 مئوية) لتجنب تلف الأنسجة الهشة."),
    ("When should a Contrast Bath cycle terminate with COLD water immersion rather than warm water?",
     ["When the primary clinical goal is edema reduction and inflammation control", "When the goal is maximum joint flexibility and pain relaxation", "Before performing strenuous heavy weight training", "In patients with severe Raynaud's phenomenon"], "imp", "إذا كان الهدف الأساسي هو تقليل التورم والوذمة Edema ننهي بالماء البارد لإحداث انقباض وعائي."),
    ("In the dip-immersion paraffin wax technique, after forming the initial wax glove, the body part is:",
     ["Kept immersed in the paraffin bath for the remainder of the 20-minute session", "Immediately washed with soap and hot water", "Scraped with a metal knife", "Wrapped in ice cubes"], "imp", "في طريقة Dip-immersion يظل الطرف مغموراً داخل حوض الشمع طوال مدة الجلسة (20 دقيقة)."),
    ("How often should a therapeutic paraffin wax bath unit be completely emptied, cleaned, and refilled?",
     ["At least twice a year (every 6 months) or whenever contaminated", "Every 5 years", "Never (the wax is self-cleaning)", "Every single morning"], "imp", "يجب تفريغ وتنظيف حوض الشمع مرتين سنوياً على الأقل أو عند تراكم الرواسب والأتربة."),

    ("Hydrocollator hot packs contain silica gel granules designed primarily to:",
     ["Absorb large quantities of water and retain moist heat effectively", "Produce electrical current in tissues", "Provide dry radiant heat", "Freeze instantly at room temperature"], "imp", "الكمادات تحتوي على جل سيليكا يمتص كميات كبيرة من الماء ويحتفظ بالحرارة الرطبة."),
    ("Properly applied Hydrocollator hot packs elevate underlying muscle tissue temperature by up to:",
     ["6°F", "20°F", "15°F", "35°F"], "qz", "امتحان 2021: ترتفع حرارة الجلد حتى 20°F، وتحت الجلد 15°F، والعضلات تحتها حتى 6°F فقط."),
    ("The operating water temperature inside a Hydrocollator heating unit is maintained between:",
     ["160°F and 170°F (71°C to 79°C)", "100°F and 110°F", "200°F and 220°F", "90°F and 100°F"], "imp", "درجة حرارة خزان الهيدروكوليتور بين 160 و 170 فهرنهايت."),
    ("In Paraffin Wax therapy, what is the standard recommended ratio of paraffin wax to mineral oil?",
     ["4 parts wax to 1 part mineral oil", "1 part wax to 4 parts oil", "10 parts wax to 1 part oil", "Equal parts (1:1)"], "imp", "النسبة القياسية لشمع البرافين هي 4 أجزاء شمع إلى جزء واحد زيت برافين (4:1)."),
    ("Why is mineral oil added to paraffin wax in therapeutic units?",
     ["To lower the melting temperature from 54°C to 45–50°C and prevent tissue burns", "To make the wax harden immediately like stone", "To raise the melting temperature above 80°C", "To sterilize the patient's skin with chemicals"], "qz", "امتحان 2021 و 2018: إضافة الزيت تقلل نقطة الانصهار من 54° إلى 45-50° مئوية مما يمنع الحروق."),
    ("After 30 minutes of paraffin wax wrapping, skin temperature elevates by approximately:",
     ["8°C to 13°C", "1°C to 2°C", "25°C to 30°C", "0°C"], "qz", "امتحان 2022: ترتفع حرارة الجلد بين 8 إلى 13 درجة مئوية."),
    ("In the dip-wrap paraffin technique, how many times is the patient's distal limb typically dipped?",
     ["8 to 12 times", "1 to 2 times only", "30 to 40 times", "50 times"], "imp", "يتم غمس الطرف من 8 إلى 12 مرة لتكوين طبقة عازلة سميكة قبل اللف بالفوطة."),
    ("Which whirlpool tank allows the patient to sit in a long-sitting position and perform knee ROM exercises?",
     ["Lowboy tank", "Highboy tank", "Extremity tank", "Contrast bath tub"], "qz", "امتحان 2018 و 2021: خزان Lowboy مخصص للجلوس الطويل long-sitting وتمارين الركبة."),
    ("In a Highboy tank, the patient is seated in water with:",
     ["Chest-high water with flexed hips and knees", "Legs fully extended horizontally", "Only hands submersed", "Head completely underwater"], "qz", "امتحان 2018: في خزان Highboy يجلس المريض وركبتيه وفخذيه في وضع انثناء flexed."),
    ("Which of the following is considered a CONTRAINDICATION for whirlpool tank therapy?",
     ["Advanced peripheral vascular disease (PVD) and severe arteriosclerosis", "Open contaminated burns", "Subacute ankle contracture", "Post-immobilization joint stiffness"], "imp", "أمراض الأوعية الدموية الطرفية المتقدمة PVD وتصلب الشرايين موانع لاستخدام الدوامات."),
    ("Contrast baths alternate between hot and cold water. What are the recommended temperature ranges?",
     ["Hot: 100–105°F (40–45°C), Cold: 59–68°F (15–20°C)", "Hot: 130–140°F, Cold: 32–40°F", "Hot: 80–85°F, Cold: 70–75°F", "Hot: 115–120°F, Cold: 50–55°F"], "imp", "درجات حمام التباين الرسمية: الساخن 100-105 فهرنهايت (40-45 مئوية)، والبارد 59-68 فهرنهايت (15-20 مئوية)."),
    ("The alternating vasoconstriction and vasodilation induced by contrast baths is termed:",
     ["Vascular flush or circulatory whip", "Lewis hunting paralysis", "Secondary hypoxic stasis", "Raynaud spasm"], "imp", "التأثير الفسيولوجي لحمامات التباين يسمى Vascular flush أو Circulatory whip ويزيد تدفق الدم حتى 100%."),
    ("Contrast bath application can increase localized blood flow by up to:",
     ["100%", "10%", "20%", "500%"], "imp", "يزيد التدفق الدموي الموضعي بنسبة تصل إلى 100%."),
    ("What is the typical ratio and duration for warm versus cold immersion in a contrast bath cycle?",
     ["3:1 or 4:1 ratio (4–6 min warm : 1–4 min cold), repeating for 15–30 min", "1:1 ratio (30 sec warm : 30 sec cold)", "10:1 ratio (20 min warm : 2 min cold)", "Pure cold for 30 minutes"], "imp", "النسبة القياسية 3:1 أو 4:1 (4-6 دقائق دافئ ثم 1-4 دقائق بارد) بإجمالي 15-30 دقيقة."),
    ("Contrast baths are especially indicated for which challenging condition?",
     ["Reflex Sympathetic Dystrophy (CRPS) and post-traumatic swelling", "Acute active hemorrhage", "Advanced gangrene", "Acute high fever"], "imp", "امتحان 2021: ممتازة لعلاج الـ CRPS / RSD والتورم المزمن بعد الإصابات."),
    ("Why should a Hydrocollator pack NEVER be placed under a patient who is lying supine on top of it?",
     ["Body weight compresses pack layers, squeezes out water, and accelerates heat transfer causing severe burns", "It cools down the pack too rapidly", "It prevents sweating completely", "It breaks the silica gel granules into dust"], "imp", "وزن المريض يعصر الفوط ويضغط الكمادة مما يسبب حروقاً خطيرة لعدم إمكانية الهروب من الحرارة."),
    ("Which modality is preferred for breaking down old adhesions and softening burn scars before stretching?",
     ["Paraffin wax or hot whirlpool", "Cryotherapy ice massage", "Vapocoolant spray", "Dry ice pack"], "imp", "الشمع والدوامات الساخنة تزيد ليونة الكولاجين قبل تمارين الإطالة."),
]
T("l3", "Lec 3 — الكمادات، الشمع، الدوامات، وحمامات التباين", "Lec 3 الوسائل الحرارية", "♨️", "سلايدات الكلية + بنك الأسئلة المعتمد", SUM_L3, [("الوسائل الحرارية وحمامات الدوامات والتباين", QS_L3)])


# ==============================================================================
# TAB 4: Peloids (Mud Therapy & Baths) & Fluidotherapy
# ==============================================================================
SUM_L4 = """
<div class="card"><h4>🌿 1. الطمي العلاجي والبيسلات (Peloids & Mud Therapy)</h4>
<ul>
<li><b>التعريف:</b> الطمي العلاجي مادة طبيعية بتستخدم من آلاف السنين، وبتتميز بـ <b>سعة حرارية عالية (high heat capacity) وتوصيل حراري منخفض جداً (low thermal conductivity)</b>، فبتحتفظ بالحرارة وتنقلها ببطء شديد للأنسجة العميقة.</li>
<li><b>أنواع الطمي العلاجي (Types of Therapeutic Muds):</b>
  <ol>
    <li><b>Moor Mud (Peat):</b> بيتكون على مدار آلاف السنين من تحلل النباتات والطحالب في المستنقعات، وغني جداً بـ <b>humic & fulvic acids</b>، وده بيديه خواص مضادة للالتهاب ومقاومة للشيخوخة.</li>
    <li><b>Black Sulfurous Mud:</b> طمي كبريتي أسود بيوجد في قاع الخلجان البحرية والبحيرات المالحة، وغني بالكبريت والأملاح، ممتاز للأمراض الجلدية والمفاصل.</li>
    <li><b>Mineral Clay (Fuller's Earth / Multani Mitti):</b> طمي معدني عالي الامتصاص، بيستخدم ككمادات لتبريد الجلد وسحب السموم.</li>
    <li><b>Dead Sea Mud (طمي البحر الميت):</b> طمي فائق الملوحة غني جداً بالماغنسيوم، الكالسيوم، والسيليكا، مشهور عالمياً بصحة الجلد وتنشيط الخلايا.</li>
  </ol>
</li>
<li><b>الخواص الكيميائية وانتقال الأيونات (Ion Transfer Properties — حفظ تام!):</b>
  <table>
    <tr><th>الأيون / المادة في الطمي</th><th>التأثير العلاجي واستخدامها في الامتحان</th></tr>
    <tr><td><b>Zinc (زنك)</b></td><td>مضاد للفطريات (<span dir="ltr">Fungi</span>) وصحة الجلد.</td></tr>
    <tr><td><b>Copper (نحاس)</b></td><td>لحالات الحساسية (<span dir="ltr">Allergic conditions</span>).</td></tr>
    <tr><td><b>Iodine (يود)</b></td><td>لتليين الالتصاقات وزيادة المدى الحركي (<span dir="ltr">Adhesions & ROM</span>).</td></tr>
    <tr><td><b>Magnesium (ماغنسيوم)</b></td><td>لعلاج التورم والارتشاح (<span dir="ltr">Edema treatment</span>).</td></tr>
    <tr><td><b>Salicylates (ساليسيلات)</b></td><td>لتسكين الآلام وتخفيف الالتهاب (<span dir="ltr">Pain relief</span>).</td></tr>
  </table>
</li>
<li><b>الاستخدام الداخلي للطمي حسب اللون (Traditional Internal Use):</b>
  <ul>
    <li><b>الطمي الأصفر (Yellow mud):</b> لأمراض الجهاز الهضمي، الكبد، الطحال، والسكر (<span dir="ltr">digestive, diabetes, hepatomegaly</span>).</li>
    <li><b>الطمي الأبيض (White mud):</b> لاضطرابات المخ والكبد (<span dir="ltr">brain & liver</span>).</li>
    <li><b>الطمي الأسود (Black mud):</b> لحالات التسمم والأمراض الجلدية (<span dir="ltr">poisoning & skin</span>).</li>
    <li><b>الطمي الأحمر (Red mud):</b> لآلام البطن، الروماتويد، والشلل (<span dir="ltr">abdominal pain, RA, paralysis</span>).</li>
  </ul>
</li>
<li><b>شروط تحضير الطمي:</b> يجب جمعه من عمق لا يقل عن <b>قدمين (at least 2 feet depth)</b> لضمان خلوه من التلوث السطحي والشوائب.</li>
</ul></div>

<div class="card"><h4>🌾 2. العلاج بالفلويدوثيرابي (Fluidotherapy)</h4>
<ul>
<li><b>فكرة العمل:</b> جهاز تسخين جاف بيعتمد على <b>الحمل القسري (Forced Convection)</b>. الكابينة بتحتوي على جزيئات سليلوز ناعمة جداً مطحونة من كيزان الذرة (<span dir="ltr">finely ground cellulose from corn cobs</span>). لما الهواء الساخن يندفع من تحت، الجزيئات بتتعلق وتتصرف زي السائل بالظبط!</li>
<li><b>درجة الحرارة التشغيلية:</b> من <span dir="ltr">100°F إلى 125°F</span> (<span dir="ltr">38°C إلى 51.7°C</span>).</li>
<li><b>الميزة الكبرى عن الشمع والكمادات:</b> المريض يقدر <b>يحرك مفاصله ويعمل تمارين نشطة (Active exercises)</b> جوه الجهاز أثناء جلسة التسخين!</li>
<li><b>إزالة التحسس (Desensitization):</b> اصطدام الجزيئات الناعمة بالجلد بيعمل تحفيز حسي ميكانيكي ممتاز لإزالة التحسس المفرط من الندبات وبقايا الأطراف المبتورة (<span dir="ltr">amputation stumps</span>).</li>
<li><b>تنبيه الوذمة:</b> للمرضى المعرضين لتكوين وذمة (<span dir="ltr">edema predisposition</span>)، بنستخدم درجات حرارة منخفضة مع تشغيل خفيف للهواء لتجنب زيادة التورم.</li>
</ul></div>
"""

QS_L4 = [
    ("In therapeutic mud application, what is the standard recommended thickness of the mud pack layer applied to the skin?",
     ["1 to 2 cm (approx. 0.5 to 1 inch)", "10 cm (4 inches)", "1 millimeter (transparent film)", "50 cm"], "imp", "سماكة طبقة كمادة الطمي القياسية على الجلد تتراوح بين 1 إلى 2 سم لتأمين عزل حراري وبطء انتقال الحرارة."),
    ("What is the typical duration of a single therapeutic mud bath or pack session?",
     ["20 to 30 minutes", "5 minutes only", "2 to 3 hours", "Overnight (8 hours)"], "imp", "مدة جلسة كمادات أو حمامات الطمي القياسية بين 20 إلى 30 دقيقة."),
    ("Dead Sea mud therapy is particularly famous worldwide for providing long-term clinical remission in which dermatological disease?",
     ["Psoriasis and atopic eczema", "Skin melanoma cancer", "Acute viral herpes", "Third-degree thermal burns"], "imp", "طمي البحر الميت مشهور عالمياً في تحسين وتخفيف أعراض الصدفية Psoriasis والإكزيما المزمنة."),
    ("In addition to thermal and chemical benefits, what mechanical effect does a full-body mud bath provide?",
     ["Gentle uniform pressure and osmotic skin softening due to mud density and plastic viscosity", "Electrocution of skin bacteria", "Permanent weight loss", "Bone fracture realigning"], "imp", "كثافة الطمي ولزوجته البلاستيكية توفر ضغطاً متجانساً ليناً يلين الجلد وينشط الامتصاص الأسموزي."),

    ("Therapeutic muds (peloids) are characterized physically by having:",
     ["High heat capacity and low thermal conductivity", "Low heat capacity and high thermal conductivity", "Instant cooling capacity only", "High electrical resistance only"], "imp", "الطمي يتميز بسعة حرارية عالية وتوصيل حراري منخفض فيحتفظ بالحرارة طويلاً."),
    ("Moor Mud (Peat) is exceptionally rich in which organic substances providing anti-inflammatory benefits?",
     ["Humic and fulvic acids", "Hydrochloric acid and sulfuric acid", "Pure sodium chloride crystals", "Acetic acid"], "imp", "طمي المستنقعات Peat غني بأحماض الهيوميك والفولفيك المضادة للالتهابات."),
    ("According to the ion-transfer properties of mud therapy, MAGNESIUM is specifically indicated for:",
     ["Edema treatment", "Fungal infections", "Breaking adhesions", "Allergic conditions"], "qz", "امتحان 2021: الماغنسيوم لعلاج التورم والارتشاح Edema."),
    ("In therapeutic mud application, IODINE is primarily utilized for:",
     ["Softening adhesions and contractures to improve ROM", "Treating active bleeding", "Cooling acute burns", "Destroying fungal spores"], "qz", "امتحان 2021: اليود يستخدم لتليين الالتصاقات وزيادة المدى الحركي."),
    ("In mud ion-transfer, SALICYLATES are used for:",
     ["Pain relief and analgesia", "Treating fungal infection", "Reducing sweating", "Increasing skin pigmentation"], "qz", "امتحان 2021: الساليسيلات لتسكين الألم وتخفيف الالتهاب."),
    ("In traditional internal clay usage, which color of mud is indicated for digestive disorders and diabetes?",
     ["Yellow mud", "Black mud", "Red mud", "White mud"], "imp", "امتحان 2018: الطمي الأصفر Yellow mud لأمراض الهضم والسكر والكبد."),
    ("When harvesting natural therapeutic mud, it must be collected from a clean site at a minimum depth of:",
     ["2 feet", "6 inches", "10 feet", "50 feet"], "imp", "يجب جمع الطمي من عمق قدمين على الأقل 2 feet لضمان نقائه وخلوه من الملوثات السطحية."),
    ("Which of the following is an absolute CONTRAINDICATION for mud pack therapy?",
     ["Acute inflammation and active tuberculosis", "Chronic osteoarthritis", "Chronic low back pain", "Old healed sprain"], "imp", "الالتهاب الحاد والسل النشط من أهم موانع العلاج بالطمي."),
    ("Fluidotherapy transfers heat to the treated body part primarily through:",
     ["Forced convection", "Direct conduction", "Radiation", "Evaporation"], "imp", "الفلويدوثيرابي ينقل الحرارة بالحمل القسري Forced convection عبر تيار الهواء الساخن."),
    ("The suspended medium inside a modern Fluidotherapy cabinet consists of:",
     ["Finely ground cellulose particles from corn cobs", "Glass beads", "Crushed silica sand", "Plastic micro-pellets"], "imp", "امتحان 2022 و 2018: حبيبات سليلوز ناعمة مصنوعة من كيزان الذرة Corn cobs."),
    ("The standard operating temperature range for a Fluidotherapy unit is:",
     ["100°F to 125°F (38°C to 51.7°C)", "160°F to 180°F", "70°F to 85°F", "200°F to 212°F"], "imp", "درجة حرارة تشغيل الفلويدوثيرابي بين 100 و 125 فهرنهايت."),
    ("A primary therapeutic advantage of Fluidotherapy over paraffin wax or hot packs is that:",
     ["The patient can perform active joint movements and exercise inside the cabinet during heating", "It completely immerses the whole torso", "It requires no electrical power", "It applies heavy hydrostatic pressure"], "qz", "امتحان 2022: المريض يستطيع أداء تمارين حركية نشطة أثناء خضوعه للتسخين داخل الكابينة."),
    ("The tactile bombardment of circulating cellulose particles in Fluidotherapy serves as an effective tool for:",
     ["Desensitization of hypersensitive scars and amputation stumps", "Exfoliating bone tissue", "Eliminating motor nerve conduction", "Decreasing arterial blood flow"], "qz", "امتحان 2022: قصف الجزيئات الناعمة يوفر تحفيزاً لمسياً ممتازاً لإزالة التحسس المفرط Desensitization."),
    ("For patients with a predisposition to edema, Fluidotherapy settings should be adjusted to:",
     ["The lower range of temperatures (approx. 100–105°F) with controlled agitation", "The maximum possible temperature (125°F)", "Zero air movement", "Ice water immersion"], "qz", "امتحان 2022 و 2018: لمرضى القابلية للوذمة نستخدم درجات حرارة منخفضة."),
    ("Fluidotherapy is clinically limited to the treatment of:",
     ["Distal extremities (hands, wrists, feet, ankles)", "The thoracic and lumbar spine", "The hip joint and pelvis", "The abdomen"], "qz", "امتحان 2021: أجهزة الفلويدوثيرابي مخصصة للأطراف الطرفية (اليدين والقدمين)."),
]
T("l4", "Lec 4 — الطمي العلاجي والفلويدوثيرابي", "Lec 4 الطمي والفلويدوثيرابي", "🌿", "سلايدات الكلية + بنك الأسئلة المعتمد", SUM_L4, [("الطمي العلاجي Peloids والفلويدوثيرابي", QS_L4)])


# ==============================================================================
# TAB 5: Cryotherapy & Aquatic Rehabilitation
# ==============================================================================
SUM_L5 = """
<div class="card"><h4>❄️ 1. العلاج بالتبريد (Cryotherapy Fundamentals)</h4>
<ul>
<li><b>التعريف:</b> الاستخدام العلاجي للبرودة الموضعية أو العامة لعلاج المشاكل المرضية. التبريد هو ببساطة <b>سحب الطاقة الحرارية بعيداً عن الأنسجة (transfer of energy away from tissue)</b>.</li>
<li><b>طرق انتقال التبريد (Mechanisms of Cooling):</b>
  <ol>
    <li><b>Conductive Cooling (التوصيل المباشر):</b> تلامس مباشر مع وسيط بارد زي كمادات التلج (<span dir="ltr">ice packs</span>) أو الثلج المجروش.</li>
    <li><b>Convective Cooling (الحمل الحراري):</b> حركة سائل أو هواء بارد حول الجسم، زي دوامة الماء البارد (<span dir="ltr">cold whirlpool</span>) أو مروحة هواء.</li>
    <li><b>Evaporative Cooling (التبريد بالتبخير):</b> استخدام سوائل متطايرة تتبخر بسرعة وتسحب الحرارة، زي الـ <span dir="ltr">ethyl chloride</span> والـ <span dir="ltr">fluoromethane</span>. درجة حرارة الجلد ممكن تنزل لـ <span dir="ltr">-4°C</span>!</li>
  </ol>
</li>
<li><b>تأثير البرودة على الدورة الدموية (Vasoconstriction):</b>
  <ul>
    <li>انقباض فوري للأوعية الجلدية بفعل تنبيه العضلات الملساء ورد فعل سمبثاوي انعكاسي.</li>
    <li><b>زيادة لزوجة الدم (Increased Blood Viscosity)</b> وزيادة مقاومة التدفق، وده بيقلل النزيف وتكوين التجمع الدموي (<span dir="ltr">hematoma</span>) مباشرة بعد الإصابة.</li>
  </ul>
</li>
<li><b>قانون فانتهوف والأيض (Van 't Hoff's Law):</b> معدل التفاعلات الكيميائية الحيوية يقل مع البرودة. <b>الأيض يقل بنسبة 13% تقريباً لكل انخفاض 1°C</b>. وده بيحمي الأنسجة من الإصابة بنقص الأكسجين الثانوي (<b>secondary hypoxic injury</b>)!</li>
<li><b>تأثير التبريد على التقلص والسباستيستي (Spasticity & Spasm):</b>
  <ul>
    <li>الكمادات الباردة بتقلل نشاط المغازل العضلية (<span dir="ltr">muscle spindle activity</span>).</li>
    <li>بتقلل نشاط الـ gamma motor neurons وتبطئ سرعة التوصيل العصبي في الأعصاب الحسية والحركية.</li>
    <li><b>Brief cold application</b> (ثواني معدودة) بيحفز الـ motor control، بينما <b>Prolonged cooling</b> (15-20 دقيقة) بيبسط العضلات ويقلل الـ spasticity.</li>
  </ul>
</li>
<li><b>Hunting Response / CIVD (Cold-Induced Vasodilation):</b>
  <ul>
    <li>عند تطبيق تبريد شديد لفترة طويلة (> 10–15 دقيقة)، بيحصل تعاقب بين انقباض وتمدد الأوعية الدموية لحماية الأنسجة من التجمد ونقص التروية.</li>
    <li>السبب هو إفراز مواد شبيهة بالهيستامين (<span dir="ltr">histamine-like substances</span>).</li>
    <li><b>تفسير اللون الوردي (Erythema / Pinkness):</b> الجلد بيبان لونه وردي محمر لأن الهيموجلوبين مش عارف يسيب الأكسجين للأنسجة في البرد، فبيحتوي على <b>كمية أعلى من الـ oxyhemoglobin</b>!</li>
  </ul>
</li>
<li><b>Cryokinetics & Cryostretch:</b>
  <ul>
    <li><b>Cryokinetics:</b> استخدام البرودة لتخدير الألم ثم عمل تمارين حركية نشطة (<span dir="ltr">cold + active movement</span>).</li>
    <li><b>Cryostretch:</b> استخدام البرودة لتسكين التقلص العضلي ثم عمل استطالة (<span dir="ltr">cold + stretching</span>).</li>
  </ul>
</li>
<li><b>موانع التبريد:</b> متلازمة رينود (<span dir="ltr">Raynaud's disease/phenomenon</span>)، حساسية البرد (<span dir="ltr">cold urticaria</span>)، الأعصاب الطرفية في مرحلة إعادة التجدد (<span dir="ltr">regenerating nerves</span>)، والقصور الشرياني الشديد.</li>
</ul></div>

<div class="card"><h4>🏊 2. التمارين المائية وإعادة التأهيل (Aquatic Therapy Techniques)</h4>
<ul>
<li><b>الحركات المساعدة والمقاومة (Assisted vs Resisted):</b>
  <ul>
    <li>الحركة لأعلى باتجاه السطح: مدعومة بقوة الطفو (<b>Buoyancy-assisted</b>)، ممتازة لتقوية العضلات الضعيفة (درجة 1 أو 2).</li>
    <li>الحركة لأسفل بعكس اتجاه السطح: مقاومة بقوة الطفو (<b>Buoyancy-resisted</b>)، زي دفع لوح الطفو لأسفل لتقوية عضلات الكوادريسبس أو الترايسبس!</li>
    <li>الحركة الأفقية الموازية للسطح: مدعومة بالطفو وتلغي الجاذبية (<b>Buoyancy-supported</b>).</li>
  </ul>
</li>
<li><b>مرضى التصلب المتعدد (Multiple Sclerosis - Uhthoff's Phenomenon):</b>
  <ul>
    <li>مرضى الـ MS عندهم حساسية مفرطة للحرارة. الميه السخنة بتسبب تعب وإرهاق شديد وتوقف التوصيل العصبي.</li>
    <li><b>درجة الحرارة المناسبة لمرضى الـ MS:</b> ماء معتدل أو بارد نسبياً (<span dir="ltr">Neutral to cool pool: 80–84°F / 26–29°C</span>). ممنوع تماماً الميه السخنة أكتر من <span dir="ltr">88°F</span>!</li>
  </ul>
</li>
<li><b>تمارين التوازن (Balance Training):</b> بيتم التدريب بتقليل قاعدة الارتكاز (<span dir="ltr">reducing base of support</span>) واستخدام التيارات المائية الدوامية لتحدي اتزان الجذع بأمان تام ضد السقوط.</li>
</ul></div>
"""

QS_L5 = [
    ("In the Cryostretch protocol, what is the exact sequence of therapeutic steps?",
     ["Cold application until numb → Static stretch → Isometric contraction → Repeat", "Heavy lifting → Ice pack → Running", "Hot pack → Ice massage → Surgery", "Vigorous stretching until tearing → Cold spray"], "imp", "بروتوكول Cryostretch: تبريد حتى التخدير -> إطالة ثابتة -> انقباض أيزومتري -> تكرار."),
    ("During vapocoolant spray application for myofascial trigger points, how should the spray nozzle be oriented?",
     ["Swept in unidirectional parallel strokes from the trigger point toward its referred pain area at a 30° angle, 12 inches away", "Held stationary at 1 inch distance until frost forms", "Circular random spraying for 10 minutes", "Directed straight into the patient's eyes"], "imp", "الرش في خطوط متوازية في اتجاه واحد من نقطة الزناد نحو منطقة الألم على بعد 12 بوصة وبزاوية 30 درجة."),
    ("In the Lewis Hunting reaction, each vasodilatory phase typically lasts approximately:",
     ["4 to 6 minutes before vasoconstriction resumes", "1 second only", "60 to 90 minutes", "24 hours"], "imp", "في رد فعل هنتنج، تدوم موجة التمدد الوعائي من 4 إلى 6 دقائق ثم يعود الانقباض الوعائي للعمل."),
    ("Why should prolonged ice application be avoided directly over superficial superficial peripheral nerves (such as the peroneal nerve at the fibular head)?",
     ["Risk of cold-induced neuropraxia or temporary nerve palsy", "It causes permanent bone fusion", "It leads to muscle hypertrophy", "It increases tendon reflexes permanently"], "imp", "التبريد المطول فوق عصب سطحي كالعصب الشظوي Peroneal nerve قد يسبب شللاً أو خدراً مؤقتاً Neuropraxia."),

    ("Cryotherapy cools the body surface primarily by:",
     ["Transferring thermal energy away from body tissues", "Pumping cold molecules into the bloodstream", "Eliminating all metabolic enzymes permanently", "Increasing core body radiation"], "imp", "التبريد هو سحب الطاقة الحرارية بعيداً عن أنسجة الجسم."),
    ("The direct transfer of heat from warm body tissue to a melting ice pack is an example of:",
     ["Conductive cooling", "Convective cooling", "Evaporative cooling", "Radiative cooling"], "qz", "سؤال المنصة: التلامس المباشر مع كمادة الثلج هو تبريد بالتوصيل Conductive cooling."),
    ("Vapocoolant sprays (such as ethyl chloride and fluoromethane) achieve rapid cooling through:",
     ["Evaporative cooling as volatile liquid changes to vapor", "Direct convective heating", "Electrochemical conduction", "Deep tissue ultrasound"], "qz", "امتحان 2021 وسؤال المنصة: تبخير السوائل المتطايرة يمثل تبريداً بالتبخير Evaporative cooling."),
    ("Immediately following acute tissue injury, cold application reduces bleeding and hematoma by:",
     ["Vasoconstriction and increased blood viscosity", "Vasodilation and decreased blood viscosity", "Accelerating capillary filtration", "Increasing cellular metabolism"], "qz", "سؤال المنصة وامتحان 2021: انقباض الأوعية مع زيادة لزوجة الدم يقلل النزيف والورم الدموي."),
    ("According to Van 't Hoff's Law, tissue metabolic rate decreases by approximately …… for each 1°C drop in temperature:",
     ["13% (approx. one-eighth)", "2% to 3%", "50%", "80%"], "imp", "قانون فانتهوف: يقل معدل الأيض بنسبة 13% (حوالي التمن) لكل درجة مئوية واحدة."),
    ("How does cryotherapy reduce the extent of SECONDARY HYPOXIC INJURY after trauma?",
     ["By lowering tissue metabolic rate and reducing cellular oxygen demand", "By increasing local blood flow massively", "By releasing inflammatory prostaglandins", "By increasing cellular temperature"], "qz", "سؤال المنصة: خفض الأيض يقلل استهلاك الخلايا للأكسجين فيحميها من الموت بنقص الأكسجين."),
    ("What physiological phenomenon is characterized by alternating cycles of vasoconstriction and vasodilation during prolonged cold exposure?",
     ["Hunting Response / Cold-Induced Vasodilation (CIVD)", "Lewis white reaction", "Spastic contracture", "Raynaud's attack"], "qz", "امتحان 2021 وسؤال المنصة: ظاهرة هنتنج Hunting response أو الـ CIVD."),
    ("The Hunting Response (CIVD) is triggered primarily by the local release of:",
     ["Histamine-like substances", "Adrenaline and noradrenaline only", "Acetylcholine only", "Insulin"], "qz", "امتحان 2021: إفراز مواد شبيهة بالهيستامين يسبب تمدداً وعائياً وقائياً من التجمد."),
    ("Why does skin appear bright pink (erythema) during cold-induced vasodilation?",
     ["Cold inhibits oxygen dissociation from hemoglobin, leaving blood rich in oxyhemoglobin", "Blood loses all oxygen completely", "Capillaries fill with carbon dioxide", "Melanocytes migrate to the surface"], "qz", "امتحان 2021 و 2018: البرودة تمنع انفصال الأكسجين فيظل الدم ممتلئاً بالأوكسي هيموجلوبين الوردي."),
    ("Cryokinetics is defined as the therapeutic combination of:",
     ["Cold application followed by pain-free active movement", "Cold application followed by heavy weight lifting", "Passive stretching during electrical shock", "Contrast immersion during sleep"], "qz", "امتحان 2021 وسؤال المنصة: التبريد لتسكين الألم متبوعاً بحركة نشطة Cryokinetics."),
    ("Cold application reduces muscle spasticity primarily by:",
     ["Decreasing gamma motor neuron activity and reducing muscle spindle sensitivity", "Increasing nerve conduction velocity", "Stimulating alpha motor neurons directly", "Eliminating muscle blood supply permanently"], "imp", "امتحان 2021: البرودة تقلل نشاط عصبون جاما وتقلل حساسية مغازل العضلات وسرعة التوصيل."),
    ("Which of the following is considered an ABSOLUTE CONTRAINDICATION for cryotherapy?",
     ["Raynaud's phenomenon and cold hypersensitivity", "Acute ankle sprain within 12 hours", "Acute hamstring muscle strain", "Post-surgical joint effusion"], "qz", "سؤال المنصة: ظاهرة رينود وحساسية البرودة من أهم موانع التبريد."),
    ("Why must hot water pools (>88°F / 31°C) be AVOIDED for patients with Multiple Sclerosis (MS)?",
     ["Heat worsens fatigue, causes nerve conduction block (Uhthoff's phenomenon), and exacerbates symptoms", "Hot water breaks bones in MS patients", "Buoyancy is completely lost in hot water", "MS patients cannot float in warm water"], "qz", "امتحان 2022 و 2018: مرضى التصلب المتعدد MS لديهم ظاهرة Uhthoff حيث تفشل الأعصاب عند التسخين."),
    ("In aquatic exercises, pushing a float DOWNWARD into the water to strengthen the triceps/quadriceps is an example of:",
     ["Buoyancy-resisted movement", "Buoyancy-assisted movement", "Buoyancy-supported movement", "Gravity-assisted movement"], "imp", "الحركة لأسفل عكس قوة الطفو تواجه مقاومة وتعتبر Buoyancy-resisted."),
    ("A patient with weak knee extensors (quadriceps) moving the leg UPWARD toward the water surface is performing:",
     ["Buoyancy-assisted movement", "Buoyancy-resisted movement", "High-drag movement", "Pure isometric contraction"], "imp", "الحركة لأعلى مع قوة الطفو تعتبر حركة مساعدة Buoyancy-assisted."),
]
T("l5", "Lec 5 — العلاج بالتبريد والتمارين المائية", "Lec 5 التبريد والتمارين", "❄️", "سلايدات الكلية + بنك الأسئلة المعتمد", SUM_L5, [("العلاج بالتبريد Cryotherapy والتمارين المائية", QS_L5)])


# ==============================================================================
# TAB 6: Past Exams (2021, 2022, 2018) & Platform Bank
# ==============================================================================
SUM_EXAMS = """
<div class="card"><h4>🏛️ تجميعة امتحانات السنوات السابقة والمنصة الرسمية</h4>
<ul>
<li><b>مصدر الأسئلة:</b> امتحانات كلية العلاج الطبيعي جامعة كفر الشيخ الرسمية (سنوات 2021، 2022، 2018) بالإضافة إلى <b>أسئلة المنصة الإلكترونية (2026/2027)</b>.</li>
<li><b>طبيعة الامتحان:</b> أسئلة حالات إكلينيكية (Clinical Case Studies) يتبعها أسئلة صح وغلط، واختيار من متعدد، وأسئلة الاختيار المزدوج المشهورة في كفر الشيخ.</li>
<li><b>راجع الحالات التلاتة دول كويس جداً لأن الامتحانات بتكررهم بالنص:</b>
  <ol>
    <li><b>حالة 2021 (Hemiplegia + Disc L4-L5 + Knee OA):</b> مريضة 57 سنة، بتتعالج بالـ Contrast bath لتسكين الألم والتورم، وتمارين الديب ووتر لتخفيف وزن الديسك، وممنوع التبريد للتقلص لو سببه نقص تروية (Ischemia).</li>
    <li><b>حالة 2021 (Athlete with fractured humerus & septic wound):</b> لاعب مصاب بكسر ملتئم بنسبة 80% مع جرح متقيح تحت الإبط؛ <b>الجرح المتقيح مانع مطلق لنزول البول</b> لمنع نقل العدوى! الفلويدوثيرابي للإيد مش للكتف. طمي اليود لتليين الالتصاقات.</li>
    <li><b>حالة 2022 (Diabetic 62 yo with lower back ulcer):</b> مريضة سكر وشلل نصفي وقرحة في الظهر؛ <b>القرحة مانع لكمادات الظهر</b>؛ وتمرين الظهر في Deep water أفضل من Shallow water.</li>
  </ol>
</li>
</ul></div>
"""

QS_EXAMS = [
    ("Case 2 (2021): Hydrostatic pressure equation is P = ρ·g·h. For a patient submerged at 3 meters depth (density = 1000 kg/m³, g = 9.8 m/s²), the hydrostatic pressure equals:",
     ["29.4 kPa (approx. 0.294 bar)", "24.9 bar", "100 bar", "1.2 bar"], "qz", "امتحان 2021: الضغط = الكثافة × عجلة الجاذبية × العمق = 1000 × 9.8 × 3 = 29,400 باسكال = 29.4 كيلو باسكال."),
    ("Case 2 (2021): When this athlete moves his shoulder underwater into flexion and extension at moderate speed, the water provides:",
     ["Resistance to movement due to viscosity and drag", "Zero resistance", "A downward pulling gravitational weight", "Electrical stimulation"], "qz", "امتحان 2021: حركة الكتف داخل الماء بسرعة تولد مقاومة بفعل لزوجة السائل والاضطراب Drag force."),
    ("Case 2 (2021): For cervical muscle spasm in this patient, which thermal application is most clinically suitable?",
     ["Hydrocollator moist pack contoured around neck and shoulders", "Paraffin wax dipping", "Ice bath for 40 minutes", "Dry sauna"], "qz", "امتحان 2021: كمادة الهيدروكوليتور الرطبة تلتف حول عضلات الرقبة والكتف بسهولة وتفك التقلص."),
    ("Case 2 (2021): Brief ice application (a few seconds) to a spastic or inhibited muscle acts to:",
     ["Facilitate alpha motor neuron activation and stimulate muscle contraction", "Paralyze the limb permanently", "Cause immediate necrosis", "Decrease blood pressure to zero"], "qz", "امتحان 2021: التطبيق الخاطف للثلج لبضع ثوانٍ ينبه المستقبلات الجلدية ويحفز عصبون ألفا الحركي."),
    ("Case 2 (2021): In this patient, stiff elbow after 3 months of cast immobilization is BEST mobilized following:",
     ["Paraffin wax application or hot whirlpool", "Cold compression wraps", "Liquid nitrogen spray", "Immediate heavy weight resistance"], "qz", "امتحان 2021: تيبس المرفق بعد الجبس يعالج بالشمع الساخن لتليين الأنسجة وتسهيل التمارين."),
    ("Case 2 (2021): Retrostasis during superficial cold application is defined as:",
     ["Vasoconstriction in the skin and subcutaneous tissues mobilizing blood from the surface into deeper tissues and internal organs", "Dilation of skin vessels pushing blood out through the pores", "Stagnation of blood in the feet", "Immediate arterial thrombosis"], "qz", "امتحان 2021 و 2022: الـ Retrostasis هو انقباض أوعية الجلد السطحية وهروب الدم للأنسجة العميقة والأحشاء."),
    ("Case 3 (2022): An aquatic physical therapy assessment for an elderly diabetic hemiplegic patient MUST include:",
     ["Transfers assessment, balance safety, and skin/ulcer inspection", "Only checking eye color", "A mandatory 500-meter swimming test", "A heavy dumbbell press"], "qz", "امتحان 2022: التقييم المائي يشمل فحص الانتقال Transfers، والاتزان، وفحص سلامة الجلد والقرح."),
    ("Case 3 (2022): Hydrocollator moist heat relieves pain and muscle spasm effectively in:",
     ["Superficial postural muscles like upper trapezius (penetrating 1–2 cm)", "Deep multifidus muscles of the lumbar spine (penetrating 10 cm)", "The femoral head bone marrow", "Deep abdominal visceral organs"], "qz", "امتحان 2022: كمادات الهيدروكوليتور حرارة سطحية تخترق 1 إلى 2 سم فقط فتناسب الترابيزيوس السطحية."),
    ("Case 3 (2022): Mineral mud (Fango) is characterized by containing:",
     ["Sulfur, iron, silicates, and natural radioactive materials", "Pure synthetic plastics", "Zero minerals", "Petroleum gasoline"], "qz", "امتحان 2022: طمي الفانجو Fango غني بالكبريت، الحديد، والسيليكات وله تأثير مهدئ للمفاصل."),
    ("Case 3 (2022): What two primary mechanisms cause dependent edema in a hemiplegic lower extremity?",
     ["Loss of active calf muscle pump and venous congestion", "Excessive sweating and dehydration", "Low protein diet only", "Hyperactive knee reflexes"], "qz", "امتحان 2022: تورم طرف مريض الشلل النصفي ناتج عن فقدان مضخة العضلات Muscle pump وركود الأوردة Venous congestion."),

    # Case 1 & Exam 2021 Questions
    ("Case 1 (2021): A 57-year-old female patient with L4-L5 disc prolapse and left knee OA. For her lumbar disc prolapse, traction and unloading are best achieved in:",
     ["Deep water immersion with buoyancy floats", "Shallow water wading", "Dry sauna", "Supine bed traction only"], "qz", "امتحان 2021: حالات انزلاق غضاريف الظهر L4-L5 يفضل علاجها في المياه العميقة Deep water لتخفيف وزن العمود الفقري."),
    ("Case 1 (2021): In this patient, mild bilateral feet edema is treated by water immersion primarily because of:",
     ["Hydrostatic pressure gradient facilitating venous and lymphatic return", "Water absorbing edema fluid through the skin", "Buoyancy eliminating patient blood volume", "Water temperature evaporating sweat"], "qz", "امتحان 2021: الضغط الهيدروستاتيكي يضغط الأطراف من أسفل لأعلى فيعيد السوائل للدورة الدموية."),
    ("Case 1 (2021): Intermittent claudication in this patient's calf muscle is primarily caused by:",
     ["Arterial vascular insufficiency / ischemia", "Muscle weakness only", "Excess calcium in bones", "Tendon rupture"], "qz", "امتحان 2021: العرج المتقطع Intermittent claudication سببه نقص التروية الشريانية Ischemia وليس ضعف العضلات."),
    ("Case 1 (2021): If muscle spasm is primarily caused by tissue ischemia, it is BETTER treated with:",
     ["Warm water application", "Cold water application", "Ice massage for 30 minutes", "Vapocoolant spray"], "qz", "امتحان 2021: التقلص الناتج عن نقص التروية يعالج بالماء الدافئ لزيادة تدفق الدم (البرودة تزيد نقص التروية سوءاً)."),
    ("Case 1 (2021): If this patient develops Deep Vein Thrombosis (DVT), hydrotherapy immersion is:",
     ["Strictly contraindicated due to the risk of dislodging an embolus", "Recommended twice daily", "Safe if performed in very hot water", "Safe if the patient swims vigorously"], "qz", "امتحان 2021: الجلطة الوريدية العميقة DVT مانع مطلق للهيدروثيرابي والتدليك خوفاً من تحرك الجلطة."),
    ("Case 1 (2021): Water temperature of 30°C is equal on the Kelvin scale to:",
     ["303 K", "273 K", "330 K", "243 K"], "qz", "امتحان 2021: التحويل لكلفن = C + 273 = 30 + 273 = 303 K."),
    ("Case 1 (2021): Hydrocollator hot packs apply which type of thermal energy to tissues?",
     ["Moist heat", "Dry radiant heat", "Microwave radiation", "Evaporative cold"], "qz", "امتحان 2021: الهيدروكوليتور يطبق حرارة رطبة Moist heat (بينما الفلويدوثيرابي حرارة جافة)."),

    # Case 2 & Exam 2021
    ("Case 2 (2021): An 18-year-old athlete after 3 months of humerus immobilization presents with a septic open wound under the axilla. His pool immersion is:",
     ["Contraindicated because an open septic wound risks serious cross-contamination and pool infection", "Indicated to clean the wound with pool chlorine", "Indicated if herbal medicine is dissolved in the pool", "Allowed for 2 hours"], "qz", "امتحان 2021: الجروح الملوثة والصديدية مانع لنزول حمامات السباحة لتجنب تلويث الحمام ونقل العدوى."),
    ("Case 2 (2021): To treat his stiff right elbow and soften adhesions to improve ROM, therapeutic mud rich in which element is preferred?",
     ["Iodine", "Zinc", "Copper", "Magnesium"], "qz", "امتحان 2021: طمي غني باليود Iodine لتليين الالتصاقات وتحسين المدى الحركي للمرفق."),
    ("Case 2 (2021): To accelerate bone fracture union in this athlete, which therapeutic modality is clinically effective?",
     ["Mud therapy (peloids)", "Ice packs", "Cold whirlpool", "Vapocoolant spray"], "qz", "امتحان 2021: كمادات الطمي تزيد الدورة الدموية وتنشيط التئام العظام."),
    ("Case 2 (2021): For his right hand post-immobilization edema, which modality provides alternating vascular flushing?",
     ["Contrast bath", "Fluidotherapy at 140°F", "Continuous ice packing for 1 hour", "Immobilization in a sling"], "qz", "امتحان 2021: حمام التباين Contrast bath هو الخيار الأمثل للوذمة بعد إزالة الجبس."),
    ("Case 2 (2021): Fluidotherapy is designed to treat conditions in the:",
     ["Hand and distal extremities", "Shoulder joint only", "Hip and pelvic girdle", "Lumbar spine"], "qz", "امتحان 2021: الفلويدوثيرابي مخصص للأطراف الطرفية (اليدين والقدمين)."),

    # Case 3 & Exam 2022
    ("Case 3 (2022): A 62-year-old diabetic hemiplegic female with a lower back decubitus ulcer. Hydrocollator pack application on her lower back is:",
     ["Contraindicated over the open ulcer and area of impaired sensation", "Indicated for 45 minutes directly over the ulcer", "Safe if applied at 180°F", "Recommended twice daily directly on the wound"], "qz", "امتحان 2022: القرحة المفتوحة وفقدان الإحساس مانعان لتطبيق كمادات الحرارة الرطبة."),
    ("Case 3 (2022): In this patient, exercise in water for back pain relief is best performed in:",
     ["Deep water with a flotation vest", "Shallow water without equipment", "Cold water below 15°C", "Hot water above 45°C"], "qz", "امتحان 2022: التمارين في المياه العميقة Deep water بسترة طفو تخفف الضغط عن العمود الفقري وتريح عضلات الظهر."),
    ("Case 3 (2022): For a diabetic patient with glove-and-stocking sensory loss, Paraffin wax therapy is:",
     ["Contraindicated or strictly precautioned due to the high risk of burns from impaired thermal sensation", "The safest modality available", "Applied at boiling temperatures", "Recommended without towels"], "qz", "امتحان 2022: اعتلال الأعصاب وفقدان الإحساس لمرضى السكر يمنع الشمع خوفاً من الاحتراق."),
    ("Case 3 (2022): The recommended pool water temperature for patients with minimal-to-mild physical disability performing conditioning exercise is:",
     ["30°C to 35°C", "15°C to 20°C", "42°C to 45°C", "20°C to 25°C"], "qz", "امتحان 2022: درجة حرارة حمام السباحة الموصى بها هي 30 إلى 35 درجة مئوية."),
    ("Case 3 (2022): Fatigue in physical therapy rehabilitation is defined as:",
     ["A physical and/or mental weariness resulting from exertion, or a subjective lack of energy", "Permanent destruction of muscle fibers", "Decreased urine production", "Inability to float in water"], "qz", "امتحان 2022: الإجهاد Fatigue هو تعب جسدي أو ذهني ناتج عن المجهود أو نقص ذاتي في الطاقة."),

    # Platform & General High-Yield Bank Questions
    ("Platform 2026: The use of cold together with movement to improve pain-limited function is called:",
     ["Cryokinetics", "Cryostretch", "Contrast therapy", "Hydro-traction"], "qz", "سؤال المنصة: الجمع بين التبريد والحركة النشطة يسمى Cryokinetics."),
    ("Platform 2026: An object with a specific gravity of 0.85 placed in water will:",
     ["Float with a portion above the water surface", "Sink straight to the bottom", "Dissolve instantaneously", "Generate heat"], "qz", "بما أن الكثافة النوعية 0.85 أقل من 1.0 فإن الجسم يطفو (Float)."),
    ("Platform 2026: Reduced muscle spasm after cold application is associated with reduced:",
     ["Muscle spindle activity", "Cellular mitochondria", "Blood viscosity", "Endorphin release"], "qz", "سؤال المنصة: تقليل التقلص بالتبريد يرتبط بإنقاص نشاط مغازل العضلات Muscle spindle activity."),
    ("Platform 2026: What effect does cold have on nerve conduction velocity (NCV)?",
     ["Cold slows (decreases) nerve conduction velocity in both sensory and motor nerves", "Cold speeds up nerve conduction by 50%", "Cold has zero effect on nerves", "Cold converts motor nerves to sensory nerves"], "qz", "سؤال المنصة وامتحان 2021: البرودة تبطئ سرعة التوصيل العصبي NCV مما يسكن الألم."),
    ("Platform 2026: Water turbulence consists of circular motions in fluid known as:",
     ["Eddy currents", "Laminar rays", "Capillary waves", "Static zones"], "qz", "التيارات الدوامية تسمى Eddy currents وتنتج عن حركة الماء المضطرب."),
    ("Exam 2018: In patients with Multiple Sclerosis, which pool temperature is recommended?",
     ["Neutral to cool water (80–84°F / 26–29°C)", "Hot water (105°F)", "Boiling water", "Ice slurry"], "qz", "امتحان 2018: مرضى الـ MS يحتاجون ماء معتدل يميل للبرودة تجنباً لانتكاسة الأعصاب."),
    ("Exam 2018: Lowboy whirlpool tanks are primarily designed for:",
     ["Lower extremity and lumbar immersion in a long-sitting posture", "Full body standing exercise", "Head and neck soaking only", "Treating only one finger"], "qz", "امتحان 2018: خزان Lowboy مخصص للأطراف السفلية والجلوس الطويل long-sitting."),
    ("Exam 2021: Human body specific gravity is 0.794 — True or False?",
     ["False — human body specific gravity is 0.974", "True — it is 0.794"], "tf", "امتحان 2021 صح وغلط: خطأ، كثافة جسم الإنسان 0.974 وليس 0.794."),
    ("Exam 2021: Hydrocollator moist heat raises muscle tissue underneath by up to 8°F — True or False?",
     ["False — it raises underlying muscle by up to 6°F (skin up to 20°F, subQ 15°F)", "True — it raises muscle by 8°F"], "tf", "امتحان 2021 صح وغلط: خطأ، العضلة ترتفع حتى 6 درجات فهرنهايت فقط."),
    ("Exam 2021: Water immersion at the waist level increases urine production 7-fold — True or False?",
     ["False — the 7-fold increase occurs with vertical immersion up to the neck (C7)", "True — waist level immersion causes 7-fold diuresis"], "tf", "امتحان 2021 صح وغلط: خطأ، الزيادة 7 أضعاف تحدث عند الغمر حتى الرقبة وليس الوسط فقط."),
    ("Exam 2022: Full body water immersion decreases vital capacity by 6–9% — True or False?",
     ["True — hydrostatic pressure compresses the chest and reduces vital capacity by 6–9%", "False — it increases vital capacity by 20%"], "tf", "امتحان 2022 صح وغلط: صح، يقلل السعة الحيوية 6-9% بفعل ضغط الماء."),
    ("Exam 2022: Total work of breathing increases by ~60% during neck-level water immersion — True or False?",
     ["True — overcoming hydrostatic chest compression increases work of breathing by ~60%", "False — work of breathing decreases to zero"], "tf", "امتحان 2022 صح وغلط: صح، يزداد جهد التنفس بنسبة 60%."),
]
T("exams", "⭐ امتحانات السنين السابقة والمنصة الرسمية", "⭐ امتحانات السنين والمنصة", "🏛️", "امتحانات 2021، 2022، 2018 + أسئلة المنصة", SUM_EXAMS, [("امتحانات كفر الشيخ والمنصة الإلكترونية", QS_EXAMS)])


# ==============================================================================
# TAB 7: True / False Drills
# ==============================================================================
SUM_TF = """
<div class="card"><h4>✅ تدريبات الصواب والخطأ (True or False Exam Drills)</h4>
<ul>
<li>دي كل جمل الصح والغلط اللي بتيجي في امتحانات الهيدرو في كفر الشيخ، ومترتبة على أدق التريكات اللي بتتقلب في الامتحان!</li>
<li>الأسئلة دي اتجمعت من امتحانات 2018 و 2021 و 2022 وكويزات المنصة.</li>
<li>حلهم كلهم وركز في تعليق كل سؤال عشان تضمن الفول مارك بإذن الله.</li>
</ul></div>
"""

QS_TF = [
    ("In Fluidotherapy, the lower ranges of temperature are recommended for patients with a greater predisposition for edema.",
     ["True ✓", "False ✗"], "tf", "صح: امتحان 2018: المرضى المعرضون للوذمة يستخدمون حرارات منخفضة مع تقليب خفيف."),
    ("The whirlpool bath combines the effects of convective heat, gentle massage, and wound debridement.",
     ["True ✓", "False ✗"], "tf", "صح: امتحان 2018: حمامات الدوامات تجمع بين الحرارة بالحمل والتدليك اللطيف وتنظيف الجروح."),
    ("Cryotherapy in prolonged application helps in reducing edema by decreasing capillary hydrostatic pressure and permeability.",
     ["True ✓", "False ✗"], "tf", "صح: البرودة تقلل الضغط الهيدروستاتيكي في الشعيرات ونفاذية الجدران فتحاصر الوذمة."),
    ("Water immersion at neck level increases cardiac output by 30% to 60%.",
     ["True ✓", "False ✗"], "tf", "صح: امتحان 2022: يرتفع النتاج القلبي من 5 لتر إلى حوالي 8.6 لتر/دقيقة بفعل زيادة الامتلاء المركزي."),
    ("Neck-depth immersion enhances cognitive brain functions, alertness, and memory.",
     ["True ✓", "False ✗"], "tf", "صح: امتحان 2022: الغمر لمستوى الرقبة ينشط التروية الدماغية واليقظة الإدراكية عبر الجهاز الباراسمبثاوي."),
    ("Moving a limb against the direction of water buoyancy (downward) assists muscle power.",
     ["False ✗", "True ✓"], "tf", "خطأ: الدفع لأسفل ضد الطفو يقاوم الحركة ويعتبر تمريناً للمقاومة Resisted وليس مساعداً Assisted."),
    ("In Multiple Sclerosis, pool water warmer than 88°F (31°C) can induce severe fatigue and conduction failure.",
     ["True ✓", "False ✗"], "tf", "صح: ظاهرة Uhthoff تجعل أعصاب الـ MS حساسة جداً للحرارة، والماء الساخن ممنوع."),
    ("Contrast baths produce a vascular flush that increases localized blood circulation by up to 100%.",
     ["True ✓", "False ✗"], "tf", "صح: التعاقب بين التمدد والانقباض يرفع التدفق الدموي الموضعي بنسبة تصل إلى 100%."),
    ("Deep water exercise with a buoyancy vest unloads lumbar disc pressure and relieves sciatica.",
     ["True ✓", "False ✗"], "tf", "صح: المياه العميقة مع سترة الطفو توفر شد ناعم وتلغي ضغط الجاذبية عن الغضاريف."),
    ("Whirlpool therapy is indicated for patients with advanced peripheral vascular disease.",
     ["False ✗", "True ✓"], "tf", "خطأ: أمراض الأوعية الدموية الطرفية المتقدمة PVD مانع قطعي لاستخدام الدوامات المائية."),

    ("Human body has an average specific gravity of 0.794.",
     ["False ✗", "True ✓"], "tf", "خطأ: كثافة جسم الإنسان 0.974 وليس 0.794."),
    ("Hydrocollator moist heat raises muscle tissue underneath by up to 8°F.",
     ["False ✗", "True ✓"], "tf", "خطأ: الكمادة ترفع حرارة العضلة حتى 6 درجات فهرنهايت فقط (الجلد حتى 20°F، وتحت الجلد 15°F)."),
    ("By immersion in water at the level of the waist, urine production increases 7-fold.",
     ["False ✗", "True ✓"], "tf", "خطأ: الزيادة بمقدار 7 أضعاف تحدث عند الغمر الرأسي حتى الرقبة C7 وليس عند الوسط."),
    ("Full body water immersion decreases vital capacity by 6–9%.",
     ["True ✓", "False ✗"], "tf", "صح: ضغط الماء على القفص الصدري وزيادة الدم الرئوي يقللان السعة الحيوية 6-9%."),
    ("Total work of breathing increases by ~60% during neck-level water immersion.",
     ["True ✓", "False ✗"], "tf", "صح: ضغط الماء على جدار الصدر والبطن يرفع المجهود التنفسي بنسبة 60%."),
    ("Paraffin wax therapy is usually applied for knees and elbows via dipping.",
     ["False ✗", "True ✓"], "tf", "خطأ: الغمس Dipping يطبق على اليدين والقدمين؛ بينما الركبة والكتف يدهنان بالفرشاة Painting."),
    ("Fluidotherapy delivers thermal energy to tissues primarily through forced convection.",
     ["True ✓", "False ✗"], "tf", "صح: الفلويدوثيرابي يعتمد على الحمل القسري Forced convection بواسطة تيار الهواء الساخن."),
    ("Fluidotherapy uses cellulose particles to heat tissues as moist heat.",
     ["False ✗", "True ✓"], "tf", "خطأ: الفلويدوثيرابي حرارة جافة Dry heat وليست رطبة."),
    ("In patients with acute inflammation, elevation of temperature is recommended to absorb exudates.",
     ["False ✗", "True ✓"], "tf", "خطأ: الالتهاب الحاد مانع قطعي للحرارة لأنه يزيد النزيف والارتشاح."),
    ("Cold application increases conduction velocity in both sensory and motor nerves.",
     ["False ✗", "True ✓"], "tf", "خطأ: البرودة تبطئ سرعة التوصيل العصبي Decreases NCV مما يسكن الألم."),
    ("Cooling increases cellular oxygen requirements and worsens secondary hypoxic injury.",
     ["False ✗", "True ✓"], "tf", "خطأ: البرودة تقلل الأيض واستهلاك الأكسجين وتحمي الخلايا من الموت بنقص الأكسجين."),
    ("Water viscosity decreases as water temperature rises.",
     ["True ✓", "False ✗"], "tf", "صح: تسخين الماء يقلل لزوجته واحتكاكه الداخلي."),
    ("Hydrostatic pressure may make chest expansion more difficult during immersion.",
     ["True ✓", "False ✗"], "tf", "صح: الضغط الخارجي يعاكس تمدد القفص الصدري."),
    ("Buoyancy can reduce mechanical stress on immersed weight-bearing joints.",
     ["True ✓", "False ✗"], "tf", "صح: قوة الطفو ترفع الجسم وتقلل الحمل على المفاصل والغضاريف."),
    ("Retrostasis refers to the mobilization of fluid from deeper tissues into the body surface.",
     ["False ✗", "True ✓"], "tf", "خطأ: الـ Retrostasis هو انقباض الأوعية السطحية ودفع الدم من السطح إلى الأنسجة العميقة والأحشاء الداخلية."),
    ("Cryokinetics involves the use of cold in conjunction with movement.",
     ["True ✓", "False ✗"], "tf", "صح: استخدام التبريد لتسكين الألم متبوعاً بحركة نشطة."),
    ("Erythema (pinkness) due to cold contains MORE oxyhemoglobin in the blood.",
     ["True ✓", "False ✗"], "tf", "صح: البرد يمنع تفكك الأكسجين من الهيموجلوبين فيظل الدم ممتلئاً بالأوكسي هيموجلوبين الوردي."),
    ("Contrast bath could be used to directly decrease spasticity in upper motor neuron lesions.",
     ["False ✗", "True ✓"], "tf", "خطأ: حمام التباين ينشط الدورة الدموية؛ بينما تقليل التشنج Spasticity يتطلب تبريداً مستمراً أو تدفئة مطولة."),
    ("During relaxation states in water, heart rate variability demonstrates an autonomic bias toward vagal control.",
     ["True ✓", "False ✗"], "tf", "صح: الاسترخاء في الماء يوجه الجهاز العصبي نحو النشاط الباراسمبثاوي Vagal tone."),
    ("In a lowboy tank, the patient is seated in chest-high water with flexed hips and knees.",
     ["False ✗", "True ✓"], "tf", "خطأ: هذا وصف خزان Highboy؛ أما Lowboy فيجلس فيه المريض بوضع الجلوس الطويل long-sitting."),
    ("Frostbite is a good indicator of effective ice treatment.",
     ["False ✗", "True ✓"], "tf", "خطأ: عضة الصقيع Frostbite تلف نسيجي خطير ومضاعفة يجب تجنبها تماماً."),
    ("Raynaud's disease is an indication for cryotherapy.",
     ["False ✗", "True ✓"], "tf", "خطأ: مرض رينود مانع قطعي للبرودة لأنه يسبب تقلصاً شريانياً شديداً قد يؤدي إلى غرغرينا."),
    ("Spastic muscles tend to sink in water, requiring additional buoyancy support.",
     ["True ✓", "False ✗"], "tf", "صح: العضلات المتشنجة كثافتها أعلى وتميل للغوص فتحتاج لعوامات دعم."),
    ("Swimming in seawater is easier than in freshwater due to higher salinity and greater buoyancy.",
     ["True ✓", "False ✗"], "tf", "صح: ملوحة البحر تزيد كثافة الماء وقوة دفع الطفو لأعلى."),
    ("A patient with an open septic axillary wound should be immersed in a public pool to clean the wound.",
     ["False ✗", "True ✓"], "tf", "خطأ: الجروح المتقيحة مانع مطلق لنزول حمامات السباحة لمنع نقل العدوى وتلويث المياه."),
    ("Calisthenics water exercises in deep water with floats place the patient's spine under traction.",
     ["True ✓", "False ✗"], "tf", "صح: التمارين في المياه العميقة مع العوامات تضع العمود الفقري تحت شد ناعم Traction."),
    ("The sudden rise in temperature from a hot pack creates a counter-irritant effect relieving pain temporarily.",
     ["True ✓", "False ✗"], "tf", "صح: الارتفاع السريع في الحرارة يحدث تأثيراً مسكناً مضاداً للألم Counter-irritant."),
    ("Aquatic therapy exercise programs are highly beneficial in the restoration of fitness in obese patients.",
     ["True ✓", "False ✗"], "tf", "صح: الطفو يخفف وزن الجسم الزائد عن المفاصل فيساعد المرضى ذوي السمنة المفرطة على الحركة بأمان."),
    ("In Multiple Sclerosis, nerve conduction sensitivity is exacerbated by warm environmental and water temperatures.",
     ["True ✓", "False ✗"], "tf", "صح: ظاهرة Uhthoff تجعل أعصاب مرضى التصلب المتعدد حساسة للحرارة وتفقد التوصيل."),
    ("Dynamic splinting should be applied during the time of thermal hydrocollator pack intervention.",
     ["False ✗", "True ✓"], "tf", "خطأ: الجبائر المتحركة Dynamic splints لا توضع أثناء تطبيق الكمادة الساخنة."),
]
T("tf", "✅ تدريبات الصح والغلط الشاملة", "✅ صح وغلط (30)", "✔️", "امتحانات كفر الشيخ الرسمية", SUM_TF, [("جمل الصواب والخطأ وتريكات الامتحان", QS_TF)])
