# Nutrition (Dr. Sayed Hanoura) — simple summaries in slide order. Tab: (tid, title, short, icon, source, summary, groups)
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
_L1 = json.load(open(os.path.join(HERE, 'l1_mcq.json'), encoding='utf8'))
L1_BATCH = [(q['q'], q['o'], q['c'], '') for q in _L1]

TABS = []
def T(*a): TABS.append(a)

# ============================================================ Lec 1
T("l1", "Lec 1 — Introduction & Basic Definitions", "Lec 1 مقدمة", "🍎",
  "سلايدات Lec 1 + تفريغ المحاضرة",
"""
<div class="card"><h4>1. Introduction</h4>
<ul><li>الـ Nutrition أساس الـ wellness والصحة، والأكل بيأثر على الطاقة والأمراض.</li>
<li>عادات الأكل الغلط على المدى الطويل بتعمل <b>chronic diseases</b>: cardiovascular و diabetes و cancer.</li>
<li>الـ balanced diet بيمنعها. والأساس هو الـ <b>FOOD</b>.</li></ul></div>

<div class="card"><h4>2. The science of nutrition</h4>
<ul><li><b>Nutrition science</b> = بيدرس العلاقة بين الـ <b>individual</b> والـ <b>environment</b>، والوسيط بينهم هو الـ <b>food</b>.</li>
<li>مجالاته: food production، diet composition، food intake و appetite، digestion و absorption، metabolism، nutrient requirements، وتأثير الـ deficiency والـ excess.</li>
<li>من التفريغ: الـ food production والتخزين شغل الـ agriculture، والطبخ وتخطيط الوجبات شغل الـ home economics، <b>مش في منهجنا</b>. إحنا بندرس الـ nutrients نفسها وهضمها وامتصاصها واحتياجات الجسم.</li></ul></div>

<div class="card"><h4>3. Basic definitions</h4>
<table><tr><th>المصطلح</th><th>التعريف</th></tr>
<tr><td>Nutrition</td><td>الأكل اللي الناس بتاكله وإزاي الجسم بيستخدمه</td></tr>
<tr><td>Nutrition science</td><td>المعرفة العلمية باحتياجات الأكل (للـ growth والـ activity والـ reproduction والـ lactation). دايمًا فيها <b>أرقام</b></td></tr>
<tr><td>Dietetics</td><td>المهنة اللي بتطبق علم التغذية عشان الصحة وعلاج الأمراض</td></tr>
<tr><td>Registered dietitian</td><td>المرجع في التغذية في الـ health-care team</td></tr>
<tr><td>Food</td><td>أي مادة لما تتاكل بتغذي الجسم</td></tr>
<tr><td>Nutrient</td><td><b>Chemical component</b> الجسم محتاجه عشان: energy، build &amp; repair tissues، regulate life processes</td></tr>
<tr><td>Digestion</td><td>تكسير mechanical و chemical للأكل لأجزاء أصغر (carbs → glucose، fats → fatty acids، proteins → amino acids)</td></tr>
<tr><td>Absorption</td><td>الـ nutrients بتدخل الـ bloodstream</td></tr>
<tr><td>Metabolism</td><td>تحويل الأكل لمواد تانية عشان الحياة تستمر</td></tr>
<tr><td>Nutritional status</td><td>حالة الجسم الناتجة من استخدام الـ essential nutrients</td></tr>
<tr><td>Calorie</td><td>الـ fuel potential في الأكل = كمية الحرارة اللي ترفع <b>1 لتر مية درجة واحدة Celsius</b></td></tr>
<tr><td>RDA (من التفريغ)</td><td>الكمية اللي <b>لو قلّيت عنها تظهر deficiency symptoms</b>. ولو زوّدت عنها كتير ممكن toxicity</td></tr></table>
<p class="key">Calories: <b>Carbs 4 · Protein 4 · Fat 9</b> لكل جرام.</p></div>

<div class="card"><h4>4. Balanced diet — 6 essential nutrients</h4>
<p><b>Carbohydrates · Protein · Fat · Vitamins · Minerals · Water</b>.<br>لو ناقص منهم حاجة يبقى <b>unbalanced diet</b> (زي الـ keto أو low carb high fat).</p></div>

<div class="card"><h4>5. Functions of nutrients (3)</h4>
<ol><li><b>Provide energy</b>
<ul><li><b>Carbs</b>: الـ primary fuel، وبيتخزن كـ <b>glycogen</b>. من <b>45%–65%</b> من الـ kcal.</li>
<li><b>Fats</b>: الـ secondary (storage) energy. من <b>20%–35%</b>.</li>
<li><b>Proteins</b>: وظيفتها الأساسية <b>tissue building</b>، وبتبقى energy لو الـ carbs والـ fats مش كفاية. من <b>10%–35%</b>.</li></ul></li>
<li><b>Build tissue</b>: proteins (amino acids)، Vit C، Ca و P للعظم، <b>Iron للـ hemoglobin</b>، fatty acids لجدار الخلية.</li>
<li><b>Regulation &amp; control</b>: vitamins و minerals (coenzymes)، <b>water</b> أساس كل الـ metabolism، و<b>fiber</b> بينظم مرور الأكل في الـ GIT.</li></ol>
<p><b>من التفريغ:</b></p>
<ul><li>الـ glucose <b>أكفأ</b> مصدر طاقة: 1 g محتاج حوالي <b>0.7 L O₂</b>. البروتين حوالي 0.9 L، والدهون <b>أقل كفاءة</b> (حوالي 1.2 L).</li>
<li>ترتيب استخدام الطاقة: <b>Carbs → Fats → Proteins (آخر حاجة)</b>. لما الجسم يكسر البروتين بيحصل muscle wasting، و<b>الـ exercise بيحمي البروتين</b>.</li>
<li><b>Simple carbs</b> (glucose، sucrose): امتصاص سريع، insulin سريع، فبتجوع بعد 2–3 ساعات. <b>Complex carbs</b> (starch): امتصاص بطيء (plateau)، وطاقة طويلة.</li>
<li>الـ starvation بتعمل <b>ketone bodies</b> (ريحة acetone في البُق).</li>
<li>الـ ATP بيطلع في 3 أشكال: <b>mechanical</b> (عضلات)، <b>electrical</b> (أعصاب)، <b>chemical</b> (بناء أنسجة).</li>
<li>الـ <b>Fiber (cellulose = insoluble)</b> مش بيتهضم، فبيعمل bulk يحافظ على الـ peristalsis، يمنع الـ constipation، وينظم امتصاص الـ glucose والدهون.</li></ul></div>

<div class="card"><h4>6. Health promotion</h4>
<ul><li><b>Health</b> = أكتر من غياب المرض. و<b>Wellness</b> = تطوير كامل للإمكانيات. ومن التفريغ: wellness = <b>efficiency</b> إنك تعمل أنشطتك بنفس المستوى كل يوم.</li>
<li>National health goals: <b>Healthy People 2020</b>.</li>
<li><b>Preventive approach</b>: تحدد الـ risk factors وتقللها. <b>Traditional approach</b>: تتحرك لما الأعراض تظهر.</li></ul>
<p><b>Healthy diet</b>: يكفي الطاقة (macro)، فيه essential nutrients كفاية (micro)، يقلل risk المرض، و<b>safe</b> (contaminants قليلة).</p>
<p><b>Signs of good nutrition</b>: well-developed body، ideal weight، good muscles، smooth clear skin، <b>glossy hair</b>، clear bright eyes.</p></div>

<div class="card"><h4>7. Nutritional states</h4>
<table><tr><th>State</th><th>المعنى</th></tr>
<tr><td>A) Optimal nutrition</td><td><b>Varied and balanced</b> diet فيه كل الـ 6 nutrients</td></tr>
<tr><td>B) Malnutrition</td><td>Diet غلط أو مش كفاية. بيشمل <b>under و over</b> nutrition، ويقلل الشغل والمناعة والنشاط الذهني</td></tr>
<tr><td>C) Undernutrition</td><td>الـ reserves خلصت. بيصيب الـ vulnerable (أطفال، كبار سن، مرضى bedridden)، و<b>ممكن يحصل في المستشفيات</b></td></tr>
<tr><td>D) Overnutrition</td><td>Energy و nutrients زيادة لفترة، فبيحصل وزن ضار، أو supplements زيادة</td></tr></table>
<p class="key">من التفريغ: الدهون والكوليسترول الزيادة بتعمل <b>atherosclerosis</b>. لو سدّت الـ coronary يبقى ischemic heart disease، والـ cerebral يبقى brain damage، والـ femoral يبقى مشكلة في الرجل. والـ triglycerides ممكن تسد الـ <b>insulin receptors</b> فتعمل diabetes.</p></div>
""",
[
 ("Definitions", [
  ("Nutrition science studies the interaction between the individual and the environment mediated by:", ["Food", "Water only", "Exercise", "Hormones"], "imp", ""),
  ("A chemical component needed by the body for energy, tissue building and regulation is a:", ["Nutrient", "Food", "Calorie", "Hormone"], "imp", ""),
  ("Mechanical and chemical breakdown of food into smaller components is:", ["Digestion", "Absorption", "Metabolism", "Excretion"], "imp", ""),
  ("The process where nutrients enter the bloodstream is:", ["Absorption", "Digestion", "Metabolism", "Dietetics"], "", ""),
  ("The condition of the body resulting from utilization of essential nutrients is:", ["Nutritional status", "Metabolism", "Wellness", "Dietetics"], "", ""),
  ("One calorie is the heat required to raise …… of water by 1°C:", ["1 liter", "1 ml", "10 liters", "100 ml"], "imp", ""),
  ("The health profession that applies nutrition science to promote health and treat disease is:", ["Dietetics", "Pharmacology", "Physiology", "Agriculture"], "", ""),
  ("RDA is the amount of a nutrient:", ["Below which deficiency symptoms appear", "Above which growth stops", "That causes obesity", "Not related to health"], "imp", ""),
 ]),
 ("Balanced diet & functions", [
  ("The number of essential nutrients in a balanced diet is:", ["6", "3", "4", "5"], "imp", ""),
  ("Which is NOT one of the six essential nutrients?", ["Hormones", "Water", "Vitamins", "Minerals"], "", ""),
  ("The three basic functions of food are:", ["Provide energy, build tissue, regulate metabolic processes", "Taste, smell, colour", "Digestion, absorption, excretion", "Storage, transport, excretion"], "imp", ""),
  ("The primary source of fuel for heat and energy is:", ["Carbohydrates", "Proteins", "Vitamins", "Water"], "imp", ""),
  ("Carbohydrates should provide …… of total kilocalories (Lec 1 slides):", ["45%–65%", "10%–35%", "20%–35%", "70%–80%"], "imp", ""),
  ("Fats should provide …… of total kilocalories:", ["20%–35%", "45%–65%", "5%–10%", "50%–60%"], "", ""),
  ("Proteins should provide …… of total kilocalories:", ["10%–35%", "45%–65%", "40%–50%", "1%–5%"], "", ""),
  ("The primary function of protein is:", ["Tissue building", "Main energy source", "Regulating GIT motility", "Heat insulation"], "imp", ""),
  ("Iron is an essential part of:", ["Hemoglobin", "Cell walls", "Bone", "Glycogen"], "", ""),
  ("Regulation of passage of food through the GIT is the role of:", ["Fiber", "Fat", "Protein", "Vitamin K"], "", ""),
  ("Fat provides …… calories per gram:", ["9", "4", "7", "2"], "imp", ""),
  ("The order in which the body uses energy sources is:", ["Carbohydrates → Fats → Proteins", "Proteins → Fats → Carbohydrates", "Fats → Proteins → Carbohydrates", "Proteins → Carbohydrates → Fats"], "imp", ""),
  ("The main defense against protein breakdown (muscle wasting) during dieting is:", ["Exercise", "Fasting", "High sugar intake", "Sleeping"], "", ""),
 ]),
 ("Health promotion & nutritional states", [
  ("The preventive approach to health:", ["Identifies and minimizes risk factors", "Acts only when symptoms appear", "Ignores lifestyle", "Depends on surgery"], "imp", ""),
  ("The traditional approach to health:", ["Attempts change when symptoms of disease appear", "Identifies risk factors early", "Focuses on wellness", "Prevents disease"], "", ""),
  ("Signs of good nutrition include all EXCEPT:", ["Dull, brittle hair", "Glossy hair", "Clear bright eyes", "Good muscle development"], "", ""),
  ("Optimal nutrition requires a diet that is:", ["Varied and balanced", "High in protein only", "Low in water", "Fat-free"], "imp", ""),
  ("Malnutrition includes:", ["Both undernutrition and overnutrition", "Undernutrition only", "Overnutrition only", "Optimal nutrition"], "imp", ""),
  ("Undernutrition:", ["Can occur in hospitals and affects the most vulnerable", "Never occurs in hospitals", "Means excess energy intake", "Is caused by supplements"], "", ""),
  ("Excess nutrient and energy intake over time producing harmful body weight is:", ["Overnutrition", "Undernutrition", "Optimal nutrition", "Wellness"], "", ""),
  ("A healthy diet should be safe to consume, meaning:", ["Low in contaminants and harmful added substances", "High in sugar", "Without water", "Only cooked food"], "", ""),
 ]),
 ("أسئلة الدفعة على Lec 1 (85 سؤال)", L1_BATCH, "fixed"),
])

# ============================================================ Lec 2
T("l2", "Lec 2 — Macronutrients: Carbs, Fats & Proteins", "Lec 2 Macro", "🍞",
  "سلايدات Lec 2 + شرح المحاضرة",
"""
<div class="card"><h4>1. أرقام البداية</h4>
<ul><li>الأكل فيه حوالي <b>100,000</b> مادة، منهم <b>300</b> بس nutrients، و<b>45</b> بس <b>essential</b>.</li>
<li><b>Essential nutrient</b> = الجسم <b>مش بيقدر يصنعه</b> ولازم ييجي من الأكل (بعض الفيتامينات والمعادن والـ amino acids والـ fatty acids).</li></ul></div>

<div class="card"><h4>2. Nutrients we need (3 أنواع)</h4>
<table><tr><th>النوع</th><th>الكمية</th><th>أمثلة</th></tr>
<tr><td>Macronutrients</td><td>كتير: من <b>1 g لـ ¼ kg</b> في اليوم</td><td>Carbs، proteins، fats، وبعض الـ minerals</td></tr>
<tr><td>Micronutrients</td><td>قليل: أقل من 1 g لحد 1 millionth of a gram</td><td>Vitamins وباقي الـ minerals. الـ trace: boron، chromium، copper، iodine، <b>iron</b>، <b>zinc</b>...</td></tr>
<tr><td>Protective nutrients</td><td>—</td><td>Soluble و insoluble fiber، antioxidants، phytonutrients</td></tr></table></div>

<div class="card"><h4>3. Carbohydrates</h4>
<ul><li><b>4 cal/g</b>، وبيدوا <b>50–55%</b> من الـ calories، يعني <b>250–275 g/day</b> (حوالي ¼ kg) في diet 2000 calorie.</li>
<li>بناكل carbs <b>أكتر</b> من البروتين والدهون. ومريض السكر لازم ينظم الـ carbs ويقيس السكر.</li>
<li>بيشمل: starch، dextrins، sugar، glucose، lactose، fructose. وأكلاته: عيش، رز، شوفان، ذرة، مكرونة، عسل، حلويات.</li>
<li>الزيادة بتتخزن <b>glycogen</b> (طاقة يوم واحد)، والباقي <b>يتحول fat</b>، فالوزن يزيد.</li></ul>
<p><b>Carbohydrate deficiency:</b></p>
<ul><li><b>Reduced stamina</b>: الـ endurance بيقل حوالي <b>50%</b>.</li>
<li><b>Ketosis</b>: الجسم بيحول البروتين لسكر وبتتراكم ketones، فبيحصل فقد مية وصوديوم، وتعب و lethargy.</li>
<li><b>Mood swings</b>: الـ <b>serotonin</b> بيقل، فبيحصل depression.</li>
<li><b>Fat as fuel</b>: الدهون المخزنة بتتحرق.</li></ul></div>

<div class="card"><h4>4. Fats</h4>
<ul><li><b>9 cal/g</b>، وبتتخزن في الأنسجة كطاقة لأوقات الشدة. من <b>20–35%</b> من الـ calories، يعني <b>40–70 g/day</b>.</li></ul>
<table><tr><th>النوع</th><th>الشكل</th><th>أمثلة</th></tr>
<tr><td>Liquid fats (oils)</td><td><b>Unsaturated</b>، سايلة في درجة حرارة الأوضة</td><td>Corn، canola، olive، fish oil. وبتتقسم <b>omega-3 و omega-6</b></td></tr>
<tr><td>Solid fats</td><td><b>Saturated</b>، صلبة</td><td>Lard، shortening، butter، coconut oil. Long-chain و medium-chain و <b>trans fats</b></td></tr></table>
<ul><li><b>Bad</b>: كل الـ saturated (<b>ما عدا coconut oil</b>) مرتبطة بالكوليسترول والـ atherosclerosis والـ CHD. والـ omega-6 الزيادة inflammatory وبتزود risk الكانسر.</li>
<li><b>Good</b>: omega-3 (DHA و EPA: fish oil و flaxseed)، omega-6 باعتدال (linoleic acid)، والـ MCT (lauric acid في الـ coconut oil).</li>
<li><b>أمراض مرتبطة بالدهون</b>: atherosclerosis (الشريان بيتخن بالكوليسترول)، CHD (plaque في الـ coronary)، cognitive decline (rapid ageing)، chronic inflammation.</li></ul></div>

<div class="card"><h4>5. Proteins</h4>
<ul><li><b>4 cal/g</b>. الاحتياج <b>0.8 g/kg</b> من وزن الجسم (حوالي <b>60 g/day</b>)، يعني <b>10–35%</b> من الـ calories.</li>
<li>كل خلية مبنية من بروتين: عضلات (actin و myosin)، شعر وضوافر (<b>keratin</b>)، جلد وأوعية وعظم (<b>collagen</b>)، وبينظم المية والـ acids.</li>
<li><b>Animal protein</b>: balanced amino acids، بس ممكن يبقى فيه saturated fat. <b>Plant</b>: soy و flaxseed كويسين، وباقي المكسرات والبذور ناقصها essential amino acids.</li>
<li>من الـ 20 amino acid فيه <b>10 essential</b>: arginine، histidine، isoleucine، leucine، lysine، methionine، phenylalanine، threonine، tryptophan، valine.</li>
<li>بروتين ناقص essential amino acid بيعمل nitrogen waste زيادة يطلع في البول.</li></ul>
<table><tr><th>Deficiency</th><th>السن</th><th>المميز</th></tr>
<tr><td>Marasmus</td><td><b>أقل من سنة</b> (بعد الفطام)</td><td>نقص وزن شديد جدًا، wasting، الضلوع باينة، وش gaunt، عيون غايرة، ممكن mental retardation</td></tr>
<tr><td>Kwashiorkor</td><td><b>1–3 سنين</b></td><td>Irritability، جلد patchy و cracked و scaly، stunted growth، رجلين مقوسة، bulging eyes</td></tr>
<tr><td>Cachexia</td><td>—</td><td>من أمراض نقص البروتين</td></tr></table></div>

<div class="card"><h4>6. Burning calories &amp; weight loss</h4>
<ol><li>الأول بيحرق <b>carbs (glycogen)</b> من الكبد والعضلات، وده سريع وقصير.</li>
<li>بعدين <b>fat</b>، والوزن بينزل أبطأ لأن الدهون طاقتها أعلى، بس مخزونها كبير.</li>
<li><b>Protein</b> بس في الحرمان الشديد الطويل. والـ total starvation بتعمل وفاة في <b>8–12 أسبوع</b>.</li></ol></div>
""",
[
 ("Nutrient groups", [
  ("Of about 100,000 substances in food, how many are essential nutrients?", ["45", "300", "1000", "13"], "imp", "300 nutrients، منهم 45 essential."),
  ("Essential nutrients are those that:", ["Cannot be synthesized by the body and must be in the diet", "Are made in the liver", "Are not needed", "Are only vitamins"], "imp", ""),
  ("Macronutrients are needed in amounts of:", ["1 gram to ¼ kg per day", "Less than 1 mg", "1 microgram", "More than 5 kg"], "", ""),
  ("Which of the following is a trace (micro) mineral?", ["Zinc", "Calcium", "Sodium", "Potassium"], "", ""),
  ("Fiber and antioxidants are classified as:", ["Protective nutrients", "Macronutrients", "Essential amino acids", "Electrolytes"], "imp", ""),
 ]),
 ("Carbohydrates", [
  ("Carbohydrates provide …… calories per gram:", ["4", "9", "7", "2"], "imp", ""),
  ("According to Lec 2, carbohydrates should form …… of caloric intake:", ["50–55%", "10–15%", "20–35%", "80–90%"], "", ""),
  ("Daily carbohydrate need on a 2000-calorie diet is about:", ["250–275 g", "60 g", "40–70 g", "1000 g"], "", ""),
  ("Excess carbohydrates are stored first as:", ["Glycogen, and the rest is converted to fat", "Protein", "Ketones", "Vitamins"], "imp", ""),
  ("Carbohydrate deficiency reduces endurance by almost:", ["50%", "5%", "90%", "10%"], "", ""),
  ("Accumulation of ketones in the body due to low carbohydrates is:", ["Ketosis", "Marasmus", "Scurvy", "Kwashiorkor"], "imp", ""),
  ("Low carbohydrate intake causes mood swings due to reduced:", ["Serotonin", "Insulin", "Collagen", "Keratin"], "imp", ""),
 ]),
 ("Fats", [
  ("Fats provide …… calories per gram:", ["9", "4", "7", "12"], "imp", ""),
  ("Recommended fat intake on a 2000-calorie diet is:", ["40–70 g/day", "250 g/day", "5 g/day", "150 g/day"], "", ""),
  ("Oils that are liquid at room temperature are:", ["Unsaturated fats", "Saturated fats", "Trans fats", "Lard"], "imp", ""),
  ("Which saturated fat is NOT linked to high cholesterol?", ["Coconut oil", "Butter", "Lard", "Shortening"], "imp", ""),
  ("Excess omega-6:", ["Is inflammatory and increases cancer risk", "Has no effect", "Prevents all diseases", "Is a protein"], "", ""),
  ("Fish oil and flaxseed oil are good sources of:", ["Omega-3 (DHA, EPA)", "Trans fat", "Saturated fat", "Cholesterol"], "", ""),
  ("Thickening of the artery wall due to cholesterol accumulation is:", ["Atherosclerosis", "Cognitive decline", "Ketosis", "Kwashiorkor"], "", ""),
 ]),
 ("Proteins & weight loss", [
  ("Daily protein requirement is:", ["0.8 g/kg body weight", "5 g/kg", "0.1 g/kg", "2 kg/day"], "imp", ""),
  ("Hair and fingernails are made of a protein called:", ["Keratin", "Collagen", "Myosin", "Actin"], "imp", ""),
  ("The protein that strengthens skin, vessels, bones and teeth is:", ["Collagen", "Keratin", "Hemoglobin", "Insulin"], "", ""),
  ("The number of essential amino acids (out of 20) is:", ["10", "20", "5", "9"], "imp", ""),
  ("Which is NOT an essential amino acid?", ["Glycine", "Leucine", "Lysine", "Tryptophan"], "", ""),
  ("Marasmus occurs in infants:", ["Below one year of age after weaning", "Aged 1–3 years", "Aged 10 years", "Adults only"], "imp", ""),
  ("Kwashiorkor occurs in children aged:", ["1–3 years", "Below 6 months", "10–15 years", "Adults"], "imp", ""),
  ("Patchy, cracked, scaly skin with irritability and bulging eyes is typical of:", ["Kwashiorkor", "Marasmus", "Scurvy", "Pellagra"], "", ""),
  ("When fewer calories are consumed, the body first uses:", ["Stored carbohydrates (glycogen)", "Protein", "Fat", "Bone"], "imp", ""),
  ("The body breaks down protein for energy:", ["Only during prolonged severe energy shortage", "First", "Before carbohydrates", "Never"], "", ""),
  ("In total starvation, death occurs in:", ["8–12 weeks", "2 days", "1 year", "3 days"], "", ""),
 ]),
])

# ============================================================ Lec 3
T("l3", "Lec 3 — Water-Soluble Vitamins (B group, C, Folate)", "Lec 3 Vit B & C", "🍊",
  "سلايدات Lec 3 + شرح المحاضرة",
"""
<div class="card"><h4>1. Introduction</h4>
<ul><li>الـ <b>Micronutrients</b> (vitamins و minerals) ليها دور أساسي في الـ metabolism والحفاظ على الأنسجة.</li>
<li><b>Vitamin</b> = مادة <b>organic</b> ضرورية للـ enzymes، والجسم <b>مش بيصنعها بكمية كفاية</b> فلازم تيجي من الأكل.</li>
<li>وظايفها: cell signalling و growth (<b>Vit A</b>)، coenzymes، hormones (<b>Vit D</b>)، antioxidant (<b>Vit E</b>).</li>
<li>عددهم <b>13</b>: <b>4 fat soluble (KEDA)</b> و <b>9 water soluble</b> (C و folate و الـ B group).</li></ul></div>

<div class="card"><h4>2. B vitamins — باختصار</h4>
<div class="vit"><div class="vit-h">B1 Thiamine</div><ul><li><b>Function:</b> طاقة من الـ carbs (ATP)، الأعصاب (acetylcholine)، الشهية</li><li><b>Deficiency:</b> <b>Beriberi</b> (لو أقل من 1 mg/day): depression، weakness، tingling، paralysis، وقلب سريع وكبير</li><li><b>ملاحظة:</b> Nontoxic. RDA للكبار <b>1.1–1.2 mg</b></li></ul></div><div class="vit"><div class="vit-h">B2 Riboflavin</div><ul><li><b>Function:</b> طاقة، antibodies و RBCs، الرؤية والجلد، وبيفعّل فيتامينات تانية</li><li><b>Deficiency:</b> <b>Ariboflavinosis</b>: عيون بتحرق، شقوق في البُق والشفايف، حساسية للضوء، dermatitis</li><li><b>ملاحظة:</b> Nontoxic. <b>الضوء بيدمره</b>، فاللبن يتباع في علب opaque</li></ul></div><div class="vit"><div class="vit-h">B3 Niacin</div><ul><li><b>Function:</b> Electron carriers للطاقة، الجلد واللسان والأعصاب</li><li><b>Deficiency:</b> <b>Pellagra = 3 Ds</b>: dermatitis، diarrhea، dementia، والرابعة <b>death</b></li><li><b>ملاحظة:</b> <b>Toxic</b>: UL <b>35 mg</b>. الـ nicotinic acid من 50–100 mg بيعمل "<b>niacin flush</b>" وأذى للكبد</li></ul></div><div class="vit"><div class="vit-h">B6 Pyridoxine</div><ul><li><b>Function:</b> Metabolism البروتين، أكتر من 100 enzyme، hemoglobin، neurotransmitters، myelin</li><li><b>Deficiency:</b> Depression، confusion، numbness، seizures، anemia، و<b>homocysteine</b> بيزيد فـ heart disease</li><li><b>ملاحظة:</b> جرعات عالية لفترة طويلة بتعمل <b>permanent nerve damage</b> (بيتاخد لـ carpal tunnel)</li></ul></div><div class="vit"><div class="vit-h">B12 Cobalamin</div><ul><li><b>Function:</b> الأعصاب (myelin)، RBCs، DNA</li><li><b>Deficiency:</b> Anemia، nerve damage. الـ <b>pernicious anemia</b> بتتعالج بحقن</li><li><b>ملاحظة:</b> موجود <b>بس في الأكل الحيواني</b>، فالـ vegetarians محتاجين fortified. وكبار السن عندهم مشكلة امتصاص</li></ul></div>
<p><b>Beriberi تفاصيل:</b> التشخيص بـ 24 hr urine thiamine (الطبيعي 40–100 µg/day، وأقل من 15 يبقى deficient) أو الـ <b>red cell transketolase</b> (أقل من 15% طبيعي، 15–25% mild، أكتر من 25% severe). العلاج: mild <b>5 mg/day PO</b>، severe <b>10 mg IV BD</b>، والأعراض بتتحسن في <b>24–48 ساعة</b>.</p>
<p><b>Who's at risk:</b> B2: cataracts و sickle cell و alcoholics. B6: alcoholics و kidney failure و oral contraceptives.</p></div>

<div class="card"><h4>3. Vitamin C (Ascorbic acid)</h4>
<ul><li><b>Functions</b>: <b>collagen</b>، neurotransmitters و hormones و carnitine، <b>antioxidant</b>، بيجدد الـ Vit E، و<b>بيزود امتصاص الحديد</b>.</li>
<li><b>Sources</b>: الموالح (برتقال، ليمون)، فراولة، طماطم، فلفل، بروكلي.</li>
<li>RDA <b>75–90 mg</b>، و UL <b>2000 mg</b>. أكتر من 1 g بيعمل diarrhea و nausea و cramps.</li>
<li><b>Deficiency = Scurvy</b>: الكولاجين مش بيتعمل، فبيحصل poor wound healing و <b>bleeding gums</b> و loose teeth و blood vessels ضعيفة و fractures.</li></ul></div>

<div class="card"><h4>4. Folic acid</h4>
<ul><li>ضروري لنمو كل الخلايا، و<b>تكاثر خلايا الجنين</b>، وبيقلل الـ homocysteine (يعني القلب)، والأعصاب، والـ serotonin.</li>
<li>Sources: cereals مدعمة، برتقال، asparagus، بروكلي، liver، legumes.</li>
<li>RDA بيزيد مع السن (infants 70 µg)، و<b>الحامل والمرضع 400 µg</b>.</li>
<li><b>Deficiency</b>: <b>megaloblastic anemia</b>، مشاكل ذاكرة، heart disease و cancer، و<b>neural tube defect</b> في الحمل.</li></ul></div>
""",
[
 ("Vitamins basics", [
  ("Vitamins are:", ["Organic substances essential for enzymatic functions", "Inorganic minerals", "Proteins only", "Hormones only"], "imp", ""),
  ("The number of known vitamins is:", ["13", "9", "4", "20"], "imp", ""),
  ("The fat-soluble vitamins are:", ["K, E, D, A", "B and C", "C and folate", "B1 and B12"], "imp", "KEDA."),
  ("The number of water-soluble vitamins is:", ["9", "4", "13", "6"], "", ""),
  ("The vitamin that acts as a hormone is:", ["Vitamin D", "Vitamin C", "Vitamin B1", "Vitamin K"], "", ""),
  ("The vitamin that acts as an antioxidant (as listed in functions) is:", ["Vitamin E", "Vitamin B12", "Vitamin D", "Folate"], "", ""),
 ]),
 ("B vitamins", [
  ("Thiamine (B1) deficiency causes:", ["Beriberi", "Pellagra", "Scurvy", "Rickets"], "imp", ""),
  ("Beriberi occurs in adults when thiamine intake drops below:", ["1 mg/day", "10 mg/day", "100 mg/day", "0.01 mg/day"], "", ""),
  ("Thiamine is a coenzyme needed for synthesis of:", ["Acetylcholine", "Collagen", "Rhodopsin", "Prothrombin"], "", ""),
  ("Red cell transketolase activity increase of more than 25% indicates:", ["Severe thiamine deficiency", "Normal", "Mild deficiency", "Toxicity"], "", ""),
  ("Treatment of severe beriberi is:", ["10 mg IV twice daily", "5 mg/day orally", "1 g/day", "No treatment"], "", ""),
  ("Riboflavin (B2) deficiency is called:", ["Ariboflavinosis", "Beriberi", "Pellagra", "Scurvy"], "imp", ""),
  ("Milk should be sold in opaque containers because …… destroys riboflavin:", ["Light", "Heat", "Cold", "Air"], "", ""),
  ("Pellagra (niacin deficiency) is characterized by:", ["Dermatitis, diarrhea, dementia (and death)", "Bleeding gums", "Night blindness", "Bowed legs"], "imp", ""),
  ("The vitamin that is toxic at high doses causing 'flush' is:", ["Niacin (B3)", "Riboflavin (B2)", "Thiamine (B1)", "Vitamin C"], "imp", ""),
  ("The UL of niacin is:", ["35 mg", "2000 mg", "1 mg", "3000 µg"], "", ""),
  ("Continued high doses of B6 may result in:", ["Permanent nerve damage", "Scurvy", "Bleeding", "Night blindness"], "imp", ""),
  ("Deficiency of B6 increases heart disease risk through accumulation of:", ["Homocysteine", "Glucose", "Ketones", "Calcium"], "", ""),
  ("Vitamin B12 is found only in:", ["Animal products", "Plant foods", "Fruits", "Water"], "imp", ""),
  ("Pernicious anemia is treated with regular:", ["B12 injections", "Vitamin C tablets", "Iron only", "Vitamin K"], "", ""),
 ]),
 ("Vitamin C & folic acid", [
  ("Vitamin C is essential for the synthesis of:", ["Collagen", "Rhodopsin", "Prothrombin", "Keratin only"], "imp", ""),
  ("Vitamin C enhances the absorption of:", ["Iron", "Calcium", "Fat", "Vitamin D"], "imp", ""),
  ("Vitamin C deficiency causes:", ["Scurvy", "Beriberi", "Rickets", "Pellagra"], "imp", ""),
  ("Bleeding gums, loose teeth and poor wound healing are signs of:", ["Scurvy", "Night blindness", "Kwashiorkor", "Beriberi"], "", ""),
  ("The UL of vitamin C is:", ["2000 mg", "35 mg", "90 mg", "1 mg"], "", ""),
  ("Folate requirement in pregnant and lactating women is:", ["400 µg/day", "70 µg/day", "4 mg/day", "1 µg/day"], "imp", ""),
  ("Folic acid deficiency in pregnancy causes:", ["Neural tube defect", "Rickets", "Scurvy", "Night blindness"], "imp", ""),
  ("Folate deficiency causes:", ["Megaloblastic anemia", "Hemolytic anemia", "Iron overload", "Hypercalcemia"], "", ""),
 ]),
])

# ============================================================ Lec 4
T("l4", "Lec 4 — Fat-Soluble Vitamins (A, D, E, K) & Macrominerals", "Lec 4 ADEK & Minerals", "🥕",
  "سلايدات Lec 4 + صور سلايدات المعادن + شرح المحاضرة",
"""
<div class="card"><h4>1. Vitamin A</h4>
<ul><li>اسم عام: <b>Retinoids</b> = preformed (جاهز، في الأكل الحيواني). <b>Carotenoids</b> (β-carotene) = provitamin A (في النبات). الاتنين بيتمتصوا مع الدهون، و<b>بيتخزن في الكبد</b>.</li>
<li><b>Functions</b>: <b>Vision</b> (retinol → retinal → <b>rhodopsin</b>، للرؤية في الضلمة)، gene expression و cell differentiation، المناعة (T cells)، النمو، و antioxidant (β-carotene).</li>
<li><b>Sources</b>: حيواني (cod liver oil، كبدة، بيض، زبدة، لبن). نباتي (بطاطا، <b>جزر</b>، سبانخ، مشمش، بابايا).</li>
<li>RDA: infants 300–400، children 400–600، adolescent 900 M / 700 F µg. و UL <b>3000 µg</b>.</li>
<li><b>Deficiency</b>: <b>night blindness</b>، xerophthalmia، blindness دائم، growth retardation، anemia، ضعف مناعة، keratinization.</li>
<li><b>Toxicity</b> (أكتر من 50,000 IU/day لشهور): dermatitis، fatigue، vomiting، <b>bone pain و fractures</b>، hepatosplenomegaly. و<b>الـ carotenoids مش toxic</b>.</li></ul></div>

<div class="card"><h4>2. Vitamin D</h4>
<ul><li>الجسم بيستخدم <b>D3 (cholecalciferol)</b> وبيصنعه: cholesterol → <b>7-dehydrocholesterol</b> → (UV من الشمس) → D3.</li>
<li>بيبقى inactive لحد ما يتعمله hydroxylation في الـ <b>liver والـ kidney</b>، فيبقى <b>1,25 dihydroxycholecalciferol</b>، وده بيشتغل كـ <b>hormone</b>.</li>
<li><b>Functions</b>: Ca و P (نسبتهم في الدم)، cell differentiation، المناعة (cell-mediated، ومنع الكانسر).</li>
<li><b>Sources</b>: <b>الشمس أهم مصدر</b>، fish liver oil، سلمون، صفار بيض، لبن. و<b>النبات مفيهوش D3</b>.</li>
<li>Intake: 5 µg (200 IU) للشباب، 10 µg (400 IU) لـ 50–70 سنة، 15 µg (600 IU) فوق 70. و UL <b>50 µg (2000 IU)</b>.</li>
<li><b>Deficiency</b>: <b>Rickets</b> (أطفال)، <b>osteomalacia</b>، osteoporosis، وكانسر (colon، breast، prostate)، type 1 DM، MS. وبيقل مع الـ high latitudes والجلد الغامق.</li></ul>
<p><b>Rickets</b> = mineralization ناقص للعظم اللي بيكبر:</p>
<ul><li>Signs: <b>bowed legs (genu varum)</b> في الـ toddlers، <b>knock knees (genu valgum)</b> في الأطفال الأكبر، <b>craniotabes</b> (جمجمة طرية)، double malleoli، greenstick fractures، muscle weakness.</li>
<li>Investigations: widening of growth plate، 25(OH)D3 قليل، <b>alkaline phosphatase عالي</b>، والـ Ca طبيعي أو قليل.</li>
<li>Treatment: Vit D <b>60,000 IU</b> (مرة واحدة أو يوميًا 10 أيام)، وبعدها <b>400 IU/day</b>، مع calcium 50–75 mg/kg/day.</li>
<li>Toxicity نادر: hypercalcemia، عطش و polyuria، itching، <b>kidney stones</b>، coma.</li></ul></div>

<div class="card"><h4>3. Vitamin E (Tocopherol)</h4>
<ul><li><b>Antioxidant</b> بيحمي الـ unsaturated fatty acids في جدار الخلية، وبيحمي RBCs والأعصاب، ومن المعادن التقيلة (lead و mercury)، وبيمنع oxidation الـ LDL.</li>
<li>Sources: مكسرات، زيوت نباتية، wheat germ. RDA الكبار <b>15 mg</b>، و UL <b>1000 mg</b>.</li>
<li><b>Deficiency</b>: في الـ <b>low birth weight / premature</b>: <b>hemolytic anemia</b>، nerve degeneration. والـ prophylaxis بيقلل الـ retinopathy of prematurity.</li>
<li>Toxicity: أكتر من 1000 mg بيتعارض مع <b>Vit K</b>.</li></ul></div>

<div class="card"><h4>4. Vitamin K</h4>
<ul><li>Cofactor لتكوين الـ <b>prothrombin</b> و clotting factors في الكبد.</li>
<li>Sources: الخضار الورقية والزيوت.</li>
<li><b>Deficiency</b>: coagulation defect، <b>hemorrhagic disease of the newborn</b>. العلاج: <b>1 mg IM للمولود</b>، والحالات الشديدة 2.5–5 mg.</li></ul></div>

<div class="card"><h4>5. Macrominerals</h4>
<p>Calcium، phosphorus، magnesium، sodium، chloride، potassium. المعادن كلها حوالي <b>4%</b> من وزن الجسم: Ca <b>1.75%</b>، P <b>1.10%</b>، Mg <b>0.04%</b>.</p>
<table><tr><th>Mineral</th><th>أهم حاجة</th><th>الأرقام</th></tr>
<tr><td>Calcium</td><td>العظم، acid-base، الأعصاب، muscle contraction. Deficiency: osteoporosis و rickets. Toxicity: constipation و kidney stones و arrhythmia</td><td>DRI <b>1000 mg/day</b>، athletes 1300–1500، UL 2500</td></tr>
<tr><td>Sodium</td><td>Fluid balance، nerve impulses، contraction. مصدره الملح والأكل المصنّع</td><td>DRI 1300–2400 mg، UL <b>2.3 g</b></td></tr>
<tr><td>Potassium</td><td>Membrane potential، water balance، nerve و muscle، بيزود الـ BMD. مصدره fresh fruits و vegetables</td><td>DRI <b>4.7 g</b>. الـ toxicity حوالي 18 g بتعمل <b>cardiac arrest</b></td></tr>
<tr><td>Phosphorus</td><td>مع الـ Ca للعظم (2 Ca : 1 P)، والطاقة (<b>ATP و CP</b>). امتصاصه محتاج Vit D. والنقص نادر، يحصل مع antacids فيها <b>aluminum hydroxide</b></td><td>RDA <b>700 mg</b>، UL 4000 mg</td></tr>
<tr><td>Magnesium</td><td>Electrical potential للأعصاب والعضلات، وفي أكتر من 300 reaction. النقص بيعمل <b>tremors و convulsions</b></td><td>310–320 F / 400–420 M mg</td></tr>
<tr><td>Chloride</td><td>Extracellular، fluid balance، gastric juice. بيمشي مع الصوديوم، والنقص بييجي مع العرق والإسهال والقيء. والملح فيه 60% chloride</td><td>2.3 g، UL 3.6 g</td></tr></table></div>
""",
[
 ("Vitamin A", [
  ("Preformed vitamin A is called:", ["Retinoids", "Carotenoids", "Tocopherol", "Calciferol"], "imp", ""),
  ("β-carotene is called:", ["Provitamin A", "Preformed vitamin A", "Vitamin D3", "Vitamin E"], "imp", ""),
  ("Vitamin A is stored in the:", ["Liver", "Kidney", "Bone", "Skin"], "", ""),
  ("Vitamin A is necessary for dark adaptation through formation of:", ["Rhodopsin", "Collagen", "Prothrombin", "Keratin"], "imp", ""),
  ("The earliest ocular sign of vitamin A deficiency is:", ["Night blindness", "Cataract", "Glaucoma", "Myopia"], "imp", ""),
  ("Which form of vitamin A is NOT toxic?", ["Carotenoids", "Retinoids", "Retinol supplements", "Cod liver oil"], "imp", ""),
  ("Vitamin A toxicity causes:", ["Bone pain, fractures and hepatosplenomegaly", "Scurvy", "Rickets", "Pellagra"], "", ""),
  ("The UL of vitamin A is:", ["3000 µg", "50 µg", "1000 mg", "35 mg"], "", ""),
 ]),
 ("Vitamin D", [
  ("The form of vitamin D utilized by humans is:", ["D3 (cholecalciferol)", "D2 (ergosterol)", "D1", "Retinal"], "imp", ""),
  ("The precursor of vitamin D3 in the skin is:", ["7-dehydrocholesterol", "Tryptophan", "β-carotene", "Tocopherol"], "imp", ""),
  ("Vitamin D3 is activated by hydroxylation in the:", ["Liver and kidney", "Skin and lung", "Stomach", "Bone"], "imp", ""),
  ("The active form of vitamin D acts as a:", ["Hormone", "Enzyme only", "Mineral", "Fiber"], "", ""),
  ("The most important source of vitamin D is:", ["Sunlight", "Plants", "Rice", "Water"], "imp", "النبات مفيهوش D3."),
  ("Vitamin D deficiency in small children causes:", ["Rickets", "Osteomalacia", "Scurvy", "Pellagra"], "imp", ""),
  ("Bowed legs in toddlers with rickets is:", ["Genu varum", "Genu valgum", "Craniotabes", "Kyphosis"], "imp", "والـ knock knees = genu valgum في الأطفال الأكبر."),
  ("Soft skull in rickets is called:", ["Craniotabes", "Genu valgum", "Xerophthalmia", "Osteoporosis"], "", ""),
  ("A laboratory finding in rickets is:", ["Elevated serum alkaline phosphatase", "High 25(OH)D3", "Low alkaline phosphatase", "Hypercalcemia"], "imp", ""),
  ("Maintenance dose of vitamin D after rickets treatment is:", ["400 IU/day", "60,000 IU/day forever", "10 IU/day", "2000 mg/day"], "", ""),
  ("Factors reducing vitamin D synthesis in skin include:", ["High latitudes and dark skin", "Sun exposure", "Fair skin", "Summer"], "", ""),
  ("Vitamin D toxicity causes:", ["Hypercalcemia, polyuria and kidney stones", "Night blindness", "Bleeding", "Scurvy"], "", ""),
 ]),
 ("Vitamins E & K", [
  ("The main function of vitamin E is:", ["Antioxidant protecting cell membranes", "Blood clotting", "Vision", "Bone formation"], "imp", ""),
  ("Vitamin E deficiency in premature infants causes:", ["Hemolytic anemia", "Rickets", "Scurvy", "Night blindness"], "imp", ""),
  ("Excess vitamin E (>1000 mg) may interfere with:", ["Vitamin K", "Vitamin C", "Iron", "Calcium"], "", ""),
  ("Vitamin K is a cofactor in the formation of:", ["Prothrombin", "Rhodopsin", "Collagen", "Hemoglobin"], "imp", ""),
  ("Vitamin K deficiency in newborns causes:", ["Hemorrhagic disease of the newborn", "Rickets", "Kwashiorkor", "Beriberi"], "imp", ""),
  ("Newborns are given vitamin K as:", ["1 mg IM", "60,000 IU orally", "10 mg IV BD", "400 µg"], "", ""),
 ]),
 ("Macrominerals", [
  ("Total mineral content of the body is about:", ["4% of body weight", "40%", "0.04%", "15%"], "", ""),
  ("The mineral making up about 1.75% of body weight is:", ["Calcium", "Phosphorus", "Magnesium", "Sodium"], "imp", ""),
  ("Calcium and phosphorus combine in a ratio of about:", ["2 Ca : 1 P", "1 Ca : 2 P", "1 : 1", "5 : 1"], "", ""),
  ("Energy for muscular work comes largely from phosphorus compounds:", ["ATP and creatine phosphate", "Glycogen and glucose", "Ketones", "Urea"], "", ""),
  ("Phosphorus deficiency may occur with long-term use of:", ["Antacids containing aluminum hydroxide", "Vitamin C", "Milk", "Sunlight"], "imp", ""),
  ("Magnesium deficiency results in:", ["Tremors and convulsions", "Scurvy", "Night blindness", "Goiter"], "imp", ""),
  ("Potassium toxicity (about 18 g) may lead to:", ["Cardiac arrest", "Rickets", "Pellagra", "Constipation"], "", ""),
  ("Most potassium is found:", ["Inside cells", "In plasma only", "In bone", "In sweat"], "", ""),
  ("Table salt is about …… chloride:", ["60%", "10%", "90%", "25%"], "", ""),
  ("Calcium DRI for adults is about:", ["1000 mg/day", "100 mg/day", "4.7 g/day", "35 mg/day"], "", ""),
 ]),
])

# ============================================================ Lec 5
T("l5", "Lec 5 — Water", "Lec 5 Water", "💧",
  "شرح المحاضرة الخامسة (مفيش سلايدات للمحاضرة دي في الملفات)",
"""
<div class="card"><h4>1. Water = elixir of life</h4>
<ul><li>من غير مية الإنسان <b>مش بيعيش أكتر من حوالي 4 أيام</b>.</li>
<li>جرام بجرام محتاجين مية <b>أكتر</b> من الـ carbs والدهون والبروتين، ونقصها بيعمل أعراض <b>أسرع من أي nutrient</b>.</li>
<li>ساعة exercise في جو حر ورطب ممكن تعمل nausea و dizziness و weakness.</li></ul></div>

<div class="card"><h4>2. المية فين في الجسم؟</h4>
<ul><li><b>Intracellular</b> (جوه الخلايا) و <b>extracellular</b> (برا)، والـ extracellular حوالي <b>⅓</b> من مية الجسم.</li>
<li>من الـ extracellular: حوالي <b>¾ interstitial</b>، والباقي plasma و lymph وتجاويف (GIT، العين، المفاصل، spinal cord).</li>
<li><b>Electrolytes</b>: الـ <b>Na⁺ و Cl⁻ برا</b> الخلية، والـ <b>K⁺ جوه</b>، وهم اللي بيوزعوا المية.</li>
<li><b>Osmosis</b>: المية بتتحرك من التركيز <b>الواطي</b> للمذابات للتركيز <b>العالي</b>. مثال: سكر على فراولة، فالمية بتطلع والفراولة بتكش.</li></ul></div>

<div class="card"><h4>3. المية بتعمل إيه؟ (4 وظايف)</h4>
<p>الجسم حوالي <b>60% مية</b>.</p>
<ol><li><b>Transport</b>: الدم <b>90% مية</b>، بينقل O₂ والـ nutrients والهرمونات، وبيشيل CO₂ والـ wastes، والبول بيطلّع الـ wastes.</li>
<li><b>Structure &amp; protection</b>: عضلات <b>75%</b>، عظم <b>25%</b>، دهون <b>20–35%</b> مية. Lubricant و cleanser (دموع، ريق)، و cushion (العين، الـ spinal cord، المفاصل).</li>
<li><b>Chemical reactions</b>: solvent (الملح بيدوب لأن المية ليها طرف + وطرف −). <b>Hydrolysis</b> (إضافة مية بتكسر molecule). <b>Condensation</b> (شيل مية بيربط). وبتساعد في الـ pH.</li>
<li><b>Temperature</b>: في الحر الأوعية <b>dilate</b> (الجلد يحمر)، وفي البرد <b>constrict</b>، و<b>العرق</b> لما يتبخر بيبرّد.</li></ol></div>

<div class="card"><h4>4. Water intake &amp; losses</h4>
<ul><li>من المشروبات ومن الأكل كمان (اللبن low-fat 90%، التفاح 85%، اللحمة 50%). والـ metabolism بيعمل مية قليلة مش مهمة.</li>
<li>الامتصاص بالـ <b>osmosis</b>. المية لوحدها بتتمتص أسرع، ومع الأكل أبطأ.</li>
<li>حوالي 1.7 L من الأكل و<b>7 L من الإفرازات</b> بيدخلوا الـ GIT يوميًا، وأغلبه بيتمتص في الـ small intestine.</li></ul>
<table><tr><th>Loss</th><th>الكمية</th></tr>
<tr><td>Urine</td><td><b>1–2 L/day</b>. بيزيد مع البروتين الكتير (urea) والـ weight loss (ketones) والملح</td></tr>
<tr><td>Feces</td><td>100–200 ml بس، لأن أكتر من 95% بيتمتص (والإسهال الشديد بيضيّع كتير)</td></tr>
<tr><td>Insensible (جلد ورئة)</td><td>حوالي <b>1 L/day</b>. الواحد مش حاسس بيه، وبيزيد في الجو الناشف</td></tr>
<tr><td>Sweat</td><td>شغل خفيف في 29°C من 2–3 L/day، و exercise شديد في الحر <b>2–4 L في الساعة</b></td></tr></table>
<p><b>Diarrhea can be deadly</b>: بتموّت حوالي <b>2 مليون طفل</b> في السنة بسبب الـ dehydration. العلاج <b>ORS</b> (سكر + electrolytes + مية) مش مية بس، والسكر بيساعد الامتصاص. فعال في <b>90–95%</b>، والـ WHO اعتمده سنة <b>1978</b>.</p></div>

<div class="card"><h4>5. Balance: water in = water out</h4>
<ul><li>المية <b>مش بتتخزن</b>. الـ intake بيتنظم بالـ <b>thirst</b> (مش دقيق)، والـ output بيتنظم <b>بدقة بالـ kidneys</b>.</li>
<li><b>Thirst</b>: بُق ناشف + الـ thirst center في المخ بيحس بقلة المية وزيادة الـ solutes. بس العطش <b>بيتأخر</b> عن الاحتياج الحقيقي (زي الرياضيين).</li></ul>
<table><tr><th>System</th><th>Stimulus</th><th>Effect</th></tr>
<tr><td><b>ADH</b> (من الـ pituitary)</td><td>Solute concentration <b>عالي</b></td><td>الكلى بتمتص مية أكتر فبيقل البول</td></tr>
<tr><td><b>RAAS</b></td><td>Blood pressure أو sodium <b>واطي</b></td><td>Renin → angiotensin II (vasoconstriction) → <b>aldosterone</b> → sodium reabsorption، والمية بتمشي ورا الصوديوم</td></tr></table>
<p class="key">الـ <b>sodium</b> هو الـ primary determinant للـ extracellular fluid volume.</p></div>

<div class="card"><h4>6. Dehydration</h4>
<ul><li>Early: headache، fatigue، loss of appetite، dry eyes و mouth، <b>بول غامق</b>.</li>
<li><b>2–3%</b> من الوزن: الأداء الجسدي والذهني بيقل. <b>3% فأكتر</b>: الـ cardiac output بيقل، والعرق يقل، والحرارة تزيد، فيبقى heat exhaustion أو heat stroke. <b>10–20%</b>: <b>death</b>.</li>
<li><b>At risk</b>: <b>infants</b> (الكلى مش بتركز، والـ surface area كبير، ومش بيعرفوا يطلبوا)، <b>elderly</b> (العطش أقل)، <b>athletes</b>.</li>
<li>لون البول: pale yellow = hydrated، medium = mild، dark/amber = severe.</li></ul></div>

<div class="card"><h4>7. Too much water — Hyponatremia</h4>
<ul><li>Water intoxication: مية كتير أو <b>صوديوم قليل</b>. مثال: رياضي بيعرق ويشرب <b>مية سادة بس</b>، فالصوديوم بيتخفف. المهم الـ <b>concentration</b> مش الكمية.</li>
<li>المية بتطلع من الدم للأنسجة: في الرئة بتعطل الـ gas exchange، وفي المخ disorientation و seizures و coma و death.</li>
<li>Early: nausea، muscle cramps، confusion، slurred speech.</li>
<li>Boston Marathon 2002: <b>13%</b> عندهم hyponatremia. اللي بيتمرن أكتر من ساعة يشرب electrolytes (4 tsp سكر + ¼ tsp ملح + كوباية مية).</li></ul></div>

<div class="card"><h4>8. نشرب قد إيه؟</h4>
<table><tr><th>الوقت</th><th>الكمية</th></tr>
<tr><td>قبل الـ exercise</td><td>حوالي 0.5 L قبلها بـ <b>4 ساعات</b></td></tr>
<tr><td>أثناء</td><td>0.2–0.4 L كل <b>15–20 دقيقة</b>. لو أقل من 60 دقيقة <b>مية سادة كفاية</b>، ولو أكتر من 60 دقيقة carbs + electrolytes</td></tr>
<tr><td>بعد</td><td>0.5–0.7 L لكل pound نزل</td></tr></table>
<ul><li>الإجمالي: <b>الستات حوالي 2.7 L</b> و<b>الرجالة حوالي 3.7 L</b> يوميًا. حوالي <b>80% من المشروبات و20% من الأكل</b>.</li>
<li>الـ caffeine diuretic بس تأثيره قصير، فالقهوة والشاي بيتحسبوا.</li>
<li><b>بيزود الاحتياج</b>: exercise، جو ناشف، low-calorie diet (ketones)، high-protein (urea)، high-salt، high-fiber.</li>
<li>Life stages: <b>infants</b> (6 شهور حوالي 0.7 L)، <b>pregnancy</b>، <b>lactation</b> (+0.7 L).</li></ul></div>
""",
[
 ("Water basics & distribution", [
  ("Without water, a person cannot survive more than about:", ["4 days", "4 weeks", "4 months", "4 hours"], "imp", ""),
  ("A lack of which nutrient causes symptoms fastest?", ["Water", "Protein", "Vitamin C", "Iron"], "imp", ""),
  ("Extracellular fluid forms about …… of body water:", ["One-third", "Two-thirds", "One-half", "Nine-tenths"], "imp", ""),
  ("About three-fourths of extracellular fluid is:", ["Interstitial fluid", "Plasma", "Lymph", "CSF"], "", ""),
  ("Most potassium is found:", ["Inside cells", "In extracellular fluid", "In plasma", "In bone"], "imp", "والـ Na و Cl برا."),
  ("Osmosis is the movement of water from:", ["Low solute concentration to high solute concentration", "High to low solute concentration", "Cells to bone", "Blood to air"], "imp", ""),
  ("The human body is about …… water:", ["60%", "90%", "25%", "10%"], "imp", ""),
  ("Blood is about …… water:", ["90%", "60%", "25%", "50%"], "", ""),
  ("Muscle tissue is about …… water:", ["75%", "25%", "20%", "95%"], "", "العظم 25%."),
  ("Addition of water to break a large molecule into two smaller ones is:", ["Hydrolysis", "Condensation", "Osmosis", "Oxidation"], "imp", ""),
  ("In hot environments, skin blood vessels:", ["Dilate to release heat", "Constrict to conserve heat", "Do not change", "Close completely"], "", ""),
 ]),
 ("Intake, losses & regulation", [
  ("Average daily urine output is:", ["1–2 L", "100–200 ml", "5–6 L", "10 L"], "imp", ""),
  ("Fecal water loss is usually:", ["100–200 ml/day", "1–2 L/day", "5 L/day", "Zero"], "", ""),
  ("Water loss through skin and lungs that a person is unaware of is called:", ["Insensible loss", "Sweat loss", "Urine loss", "Fecal loss"], "imp", ""),
  ("Strenuous exercise in heat can cause sweat losses of:", ["2–4 L per hour", "100 ml per day", "10 L per minute", "None"], "", ""),
  ("The best treatment for dehydration in childhood diarrhea is:", ["Oral Rehydration Solution (ORS)", "Plain water only", "Antibiotics only", "Fasting"], "imp", ""),
  ("The sugar in ORS:", ["Helps the intestine absorb fluid and electrolytes", "Provides only taste", "Causes diarrhea", "Is not needed"], "", ""),
  ("Water intake is regulated mainly by …… while water loss is regulated precisely by ……", ["Thirst; kidneys", "Kidneys; thirst", "Liver; skin", "Lungs; heart"], "imp", ""),
  ("ADH is secreted when blood solute concentration is:", ["High", "Low", "Normal", "Zero"], "imp", ""),
  ("ADH acts on the kidneys to:", ["Reabsorb water and reduce urine", "Excrete more water", "Excrete sodium", "Produce renin"], "", ""),
  ("The RAAS is activated by:", ["Low blood pressure", "High blood pressure", "High solute concentration only", "Eating"], "imp", ""),
  ("Aldosterone increases reabsorption of:", ["Sodium (water follows)", "Potassium only", "Urea", "Glucose"], "", ""),
  ("The primary determinant of extracellular fluid volume is:", ["Sodium", "Potassium", "Calcium", "Glucose"], "imp", ""),
 ]),
 ("Dehydration, hyponatremia & needs", [
  ("Mild dehydration impairing performance occurs at a body water loss of:", ["2–3% of body weight", "10–20%", "0.1%", "50%"], "imp", ""),
  ("Water loss that can result in death is:", ["10–20% of body weight", "2–3%", "1%", "0.5%"], "imp", ""),
  ("Groups at high risk of dehydration include all EXCEPT:", ["Young sedentary adults in cool weather", "Infants", "Elderly", "Athletes"], "", ""),
  ("Infants are at risk of dehydration because:", ["Their kidneys can't concentrate urine and surface area is large", "They drink too much", "They sweat less", "Their thirst is strong"], "", ""),
  ("Dark yellow/amber urine indicates:", ["Severe dehydration", "Good hydration", "Overhydration", "Normal"], "", ""),
  ("Hyponatremia in athletes is usually caused by:", ["Drinking plain water only after losing sodium in sweat", "Eating salty food", "Drinking sports drinks", "Not drinking"], "imp", ""),
  ("In hyponatremia, fluid accumulation in the brain causes:", ["Disorientation, seizures, coma", "Bleeding", "Rickets", "Night blindness"], "", ""),
  ("For exercise lasting 60 minutes or less, the adequate replacement fluid is:", ["Plain water", "Sports drink with carbs", "Coffee", "Milk"], "imp", ""),
  ("During exercise, fluid should be consumed every:", ["15–20 minutes", "2 hours", "5 hours", "Only after exercise"], "", ""),
  ("Recommended total water intake for women is about:", ["2.7 L/day", "3.7 L/day", "1 L/day", "6 L/day"], "imp", "والرجالة حوالي 3.7 L."),
  ("About 80% of fluid intake comes from:", ["Beverages", "Food", "Metabolism", "Fruits only"], "", ""),
  ("Which diet INCREASES water needs?", ["High-protein diet", "Normal diet", "Low-salt diet", "Low-fiber diet"], "", "عشان الـ urea."),
 ]),
])

# ============================================================ Lec 6
T("l6", "Lec 6 — Healthy Diet & Eat Smart", "Lec 6 Healthy diet", "🥗",
  "سلايدات Lec 6",
"""
<div class="card"><h4>1. Unhealthy diet</h4>
<ul><li>Risk factor لـ high BP، diabetes، blood lipids، obesity، CVD، cancer.</li>
<li>الـ WHO: <b>2.7 مليون وفاة/سنة</b> بسبب قلة الفاكهة والخضار.</li>
<li>بتسبب حوالي <b>19%</b> من سرطانات الـ GIT، و<b>31%</b> من الـ ischaemic heart disease، و<b>11%</b> من الـ strokes.</li></ul></div>

<div class="card"><h4>2. What is a healthy diet? (WHO)</h4>
<ul><li>كُل calories <b>قد اللي بتحرقه</b>.</li>
<li>قلل الدهون، وفضّل الـ unsaturated على الـ saturated والـ trans.</li>
<li>زوّد النبات: فاكهة، خضار، legumes، whole grains، مكسرات.</li>
<li><b>السكر أقل من 10%</b> simple sugars.</li>
<li>قلل الملح، وخليه <b>iodized</b>.</li>
<li>كمان: micronutrients، وابعد عن السموم (heavy metals) والـ carcinogens (benzene) والأكل الملوث (E. coli).</li></ul></div>

<div class="card"><h4>3. Healthy eating plate (اختيارات)</h4>
<ul><li><b>Carbs</b>: whole grains، وابعد عن العيش والرز الأبيض والـ sodas.</li>
<li><b>Protein</b>: سمك، فراخ، مكسرات، فول. <b>قلل اللحمة الحمرا</b>.</li>
<li><b>Fats</b>: زيوت نباتية ومكسرات وسمك. قلل الـ saturated وابعد عن الـ <b>trans</b>.</li>
<li>Fiber، وخضار وفاكهة ملونة ومتنوعة.</li>
<li><b>Calcium مهم، بس اللبن مش أحسن ولا الوحيد مصدر</b> (collards، bok choy، soy milk مدعم).</li>
<li><b>المية أحسن مشروب</b>. قلل العصاير واللبن، وابعد عن المشروبات المسكرة. والـ sports drinks بس للي بيتمرن <b>أكتر من ساعة</b>.</li>
<li>Multivitamin يومي + Vit D إضافي ممكن يفيد. وكمان exercise ووزن صحي.</li></ul></div>

<div class="card"><h4>4. Strategies for healthy eating (8)</h4>
<ol><li>Enough calories</li><li>Variety of foods</li><li>Moderate portions</li><li>Fruits، vegetables، legumes، grains</li><li>Water</li><li>Limit sugary foods، salt، refined grains</li><li>Don't be the food police</li><li>Get moving</li></ol>
<p><b>Healthy foods:</b> fruits (vitamins و potassium)، grains (B1 و manganese و folate)، seafood (<b>omega-3</b>: lobster، shrimps، mussel، seabass)، eggs و low-fat dairy، poultry و lean meats. وفيه الـ <b>Mediterranean diet pyramid</b>.</p></div>

<div class="card"><h4>5. Eat smart</h4>
<p>مش بس <b>بتاكل إيه</b>، كمان <b>بتاكل إزاي</b>:</p>
<ol><li><b>Chew slowly</b> واستمتع بكل لقمة.</li>
<li><b>Avoid stress</b>: خد نفس عميق، ومتاكلش وانت بتشتغل أو بتسوق أو بتتخانق أو بتتفرج على TV، وشغّل موسيقى هادية.</li>
<li><b>Listen to your body</b>: ممكن تكون عطشان مش جعان، <b>وقف قبل ما تشبع</b>، وكُل ببطء وكميات صغيرة.</li>
<li><b>Eat early, eat often</b>: ابدأ يومك بـ <b>breakfast</b> صحي.</li></ol>
<p class="key">Health is wealth.</p></div>
""",
[
 ("Healthy diet", [
  ("According to WHO, a diet low in fruits and vegetables causes about …… deaths/year:", ["2.7 million", "27 thousand", "270 million", "2.7 billion"], "imp", ""),
  ("Unhealthy diet causes about …… of ischaemic heart disease:", ["31%", "19%", "11%", "90%"], "imp", "19% GIT cancer و 11% strokes."),
  ("Simple sugars should be limited to less than:", ["10% of intake", "50%", "30%", "75%"], "imp", ""),
  ("Salt in a healthy diet should be:", ["Limited and iodized", "Unlimited", "Completely avoided", "Non-iodized"], "", ""),
  ("A healthy weight is a balance between:", ["Energy consumed and energy burnt", "Protein and fat", "Water and salt", "Sugar and fiber"], "", ""),
  ("Which carbohydrate choice is healthier?", ["Whole grains", "White bread", "White rice", "Pastries"], "", ""),
  ("In the healthy protein package, it is better to avoid:", ["Red meat", "Fish", "Beans", "Nuts"], "", ""),
  ("The best source of liquid is:", ["Water", "Juice", "Sugary drinks", "Milk"], "imp", ""),
  ("Sports drinks are recommended only for people who exercise:", ["More than an hour at a stretch", "10 minutes", "Never", "Once a week"], "imp", ""),
  ("Regarding calcium sources:", ["Milk is not the best or only source", "Milk is the only source", "Calcium is unimportant", "Only supplements provide calcium"], "", ""),
  ("Seafood is essential mainly for:", ["Omega-3", "Trans fats", "Vitamin C", "Fiber"], "", ""),
 ]),
 ("Eat smart", [
  ("'Eat smart' means:", ["Not just what you eat, but how you eat", "Eating fast", "Skipping breakfast", "Eating while watching TV"], "imp", ""),
  ("Eat-smart strategies include all EXCEPT:", ["Eating while driving or arguing", "Chewing slowly", "Stopping before feeling full", "Starting the day with breakfast"], "imp", ""),
  ("'Listen to your body' includes:", ["Stopping eating before you feel full", "Eating until very full", "Ignoring thirst", "Eating large portions"], "", ""),
  ("'Eat early, eat often' means:", ["Start your day with a healthy breakfast", "Eat only at night", "One big meal daily", "Skip meals"], "", ""),
  ("Which is NOT one of the 8 strategies for healthy eating?", ["Avoid all fats completely", "Variety of foods", "Moderate portions", "Get moving"], "", ""),
 ]),
])

TF_DRILL = [
 ("Fat provides 4 calories per gram.", 1, "9."),
 ("Carbohydrates are the primary source of energy.", 0, ""),
 ("Protein's primary function is energy production.", 1, "Tissue building."),
 ("Essential nutrients can be synthesized by the body.", 1, "مش بيتصنعوا."),
 ("A diet of carbs, proteins and fats only is balanced.", 1, "لازم الـ 6."),
 ("Malnutrition includes both undernutrition and overnutrition.", 0, ""),
 ("Undernutrition cannot occur in hospitals.", 1, "ممكن يحصل."),
 ("Coconut oil is a saturated fat not linked to high cholesterol.", 0, ""),
 ("Marasmus occurs in children aged 1–3 years.", 1, "أقل من سنة. والـ kwashiorkor 1–3."),
 ("There are 10 essential amino acids.", 0, ""),
 ("Vitamin B12 is found in plant foods.", 1, "حيواني بس."),
 ("Niacin is nontoxic even at high doses.", 1, "Toxic (niacin flush)."),
 ("Pellagra is characterized by dermatitis, diarrhea and dementia.", 0, ""),
 ("Vitamin C enhances iron absorption.", 0, ""),
 ("Folic acid deficiency in pregnancy causes neural tube defects.", 0, ""),
 ("Carotenoids are toxic in high doses.", 1, "Not toxic."),
 ("Plants contain vitamin D3.", 1, ""),
 ("Vitamin D is activated in the liver and kidney.", 0, ""),
 ("Genu varum (bowed legs) appears in toddlers with rickets.", 0, ""),
 ("Vitamin K deficiency causes hemorrhagic disease of the newborn.", 0, ""),
 ("Most sodium is found inside cells.", 1, "برا الخلية. والـ K جوه."),
 ("Water moves by osmosis toward the area of higher solute concentration.", 0, ""),
 ("Water can be stored in the body.", 1, ""),
 ("ADH is secreted when blood solute concentration is low.", 1, "High."),
 ("Plain water is the best treatment for childhood diarrhea.", 1, "ORS."),
 ("Drinking only plain water after heavy sweating may cause hyponatremia.", 0, ""),
 ("Sports drinks are needed for exercise lasting less than 60 minutes.", 1, "مية سادة كفاية."),
 ("Simple sugars should be less than 10% of intake.", 0, ""),
]
