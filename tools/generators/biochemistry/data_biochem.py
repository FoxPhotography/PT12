# Biochemistry II (year 2) — midterm (Lec 1–7) + full-course batch bank
# Tab: (tid, title, short, icon, source, summary, groups)
# MCQ: (q, [correct, wrong...], tag, expl)  tag: 'qz' = أسئلة الدفعة, 'imp' = مهم/الدكتور أكد عليه
# Fixed T/F group: (title, [(q, opts, ci, expl)], "fixed")
TABS = []
def T(*a): TABS.append(a)
_TF = ["True ✓", "False ✗"]
def tf(q, c, e=""): return (q, _TF, c, e)

SHEET = """
<div class="card"><h4>📌 منهج الميد</h4>
<ul><li>المحاضرات من 1 لـ 7: Bioenergetics و ATP، والـ ETC، والـ Glycolysis، والـ PDH والـ TCA، والـ Glycogen، والـ HMP shunt.</li>
<li><b>مش علينا</b> حسب تحديدات الدفعة:
<ul><li>خطوات الـ HMP (الرسمة).</li>
<li>الـ Regulation according to availability of substrate بتاع الـ Krebs.</li>
<li>نقطة الـ Fe²⁺ → Fe³⁺ (met Hb).</li>
<li>جزء الـ catabolism/anabolism الدكتور قال غالبًا مش بيجي عليه أسئلة، بس اعرف إن <b>catabolic = هدم</b> و<b>anabolic = بناء</b>.</li></ul></li>
<li>الحسابات هنا: <b>NADH = 3 ATP</b> و<b>FADH₂ = 2 ATP</b>.</li></ul></div>

<div class="card"><h4>⚡ Lec 1 — Bioenergetics &amp; ATP</h4>
<table><tr><th>الحاجة</th><th>الإجابة</th></tr>
<tr><td>ΔG</td><td>طاقة الـ products ناقص طاقة الـ reactants</td></tr>
<tr><td>ΔG بالسالب</td><td><b>Exergonic</b>: بينتج طاقة، catabolism، <b>spontaneous</b></td></tr>
<tr><td>ΔG بالموجب</td><td><b>Endergonic</b>: بيستهلك طاقة، anabolism، <b>non-spontaneous</b></td></tr>
<tr><td><span dir="ltr">ΔG = 0</span></td><td><b>Equilibrium</b>: مفيش طاقة اتنتجت ولا اتستهلكت</td></tr>
<tr><td>kcal/g</td><td><span dir="ltr">Carbs <b>4</b> · Lipid <b>9</b> · Protein <b>4</b></span></td></tr>
<tr><td>Adenine + ribose</td><td><b>Adenosine</b></td></tr>
<tr><td>C5 (CH₂OH) مع الفوسفات</td><td><b>Ester bond</b> = <b>low energy</b></td></tr>
<tr><td>فوسفات مع فوسفات</td><td><b>Acid anhydride (phosphoanhydride)</b> = <b>high energy (~)</b></td></tr>
<tr><td>High-energy bonds</td><td><span dir="ltr">ATP <b>2</b> · ADP <b>1</b> · AMP <b>0</b></span><br>والـ low energy bonds في الـ ATP: <b>1</b></td></tr>
<tr><td>الحد الفاصل</td><td><b>7 kcal</b>: أعلى منه high، وأقل منه low</td></tr>
<tr><td>Creatine~P + ADP → ATP</td><td><b>Substrate-level phosphorylation</b> (minor method)</td></tr></table></div>

<div class="card"><h4>🔋 Lec 2 — ETC</h4>
<ul><li>بيحصل في الـ <b>inner mitochondrial membrane</b>. الـ <b>O₂</b> هو الـ final electron acceptor عند <b>Complex IV</b>.</li>
<li>الـ protons بتتضخ للـ <b>intermembrane space</b>، فبيتكوّن <b>proton gradient</b>. ورجوعها من <b>Complex V (ATP synthase)</b> بيعمل ATP، ودي اسمها <b>oxidative phosphorylation</b>.</li>
<li><b>Uncouplers</b>: الـ oxidation بتحصل والـ phosphorylation لأ، لأن الـ membrane بيبقى permeable للـ protons، فالطاقة بتطلع <b>heat</b>. مثال: <b>aspirin</b> بجرعات toxic (حرارة 40°C فأكتر). و<b>Thermogenin</b> = physiological uncoupler في الـ <b>newborns</b>.</li>
<li>هضم النشا: Starch (branched) ← <b>amylase</b> (salivary أو pancreatic) ← <b>dextrin</b> ← <b>maltose + isomaltose</b>.</li></ul></div>

<div class="card"><h4>🔥 Lec 3–4 — Glycolysis</h4>
<table><tr><th>Step</th><th>الـ enzyme</th><th>ملحوظة</th></tr>
<tr><td>1 Glucose → G6P</td><td><b>Hexokinase / Glucokinase</b></td><td>أول خطوة بتستهلك ATP · irreversible</td></tr>
<tr><td>2 G6P ⇌ F6P</td><td><b>Isomerase</b></td><td>isomerization</td></tr>
<tr><td>3 F6P → F1,6-BP</td><td><b>PFK-1</b></td><td><b>أهم خطوة و rate-limiting</b> · ATP تاني · irreversible</td></tr>
<tr><td>4 F1,6-BP → G3P + DHAP</td><td><b>Aldolase</b></td><td>6C بيتقسم لـ 3C + 3C</td></tr>
<tr><td>5 G3P → 1,3-BPG</td><td><b>Dehydrogenase</b></td><td>بيطلع <b>2 NADH</b></td></tr>
<tr><td>6 1,3-BPG → 3PG</td><td><b>Phosphoglycerate kinase</b></td><td><b>2 ATP</b> بالـ substrate-level</td></tr>
<tr><td>3PG → 2PG</td><td><b>Mutase</b></td><td>الفوسفات بيتنقل من C3 لـ C2</td></tr>
<tr><td>2PG → PEP</td><td><b>Enolase</b></td><td>PEP فيه high-energy bond</td></tr>
<tr><td>PEP → pyruvate</td><td><b>Pyruvate kinase</b></td><td><b>2 ATP</b> بالـ substrate-level · irreversible</td></tr></table>
<ul><li>Aerobic بيطلع <b>pyruvate</b>، و anaerobic بيطلع <b>lactate</b>. بيحصل في الـ <b>cytosol</b>. الخطوات <b>10</b>.</li>
<li>الـ ATP: اتصرف <b>2</b> واتكسب <b>4</b>، فالـ net <b>2</b>. ومع الـ 2 NADH (aerobic) يبقى <b>8 ATP</b>.</li>
<li>الـ HK بيتثبط بالـ <b>G6P</b> (feedback). الـ PFK-1 بيتنشط بالـ <b>AMP</b>، وبيتثبط بالـ <b>ATP و citrate</b>. والـ PK <b>active وهو dephosphorylated</b>، وبيتثبط بالـ ATP العالي.</li>
<li>الـ <b>Insulin</b> بينشط الـ glycolysis، والـ <b>Glucagon</b> بيثبطه.</li>
<li>أهم حاجة للـ <b>RBCs</b> (مفيهاش mitochondria) وللـ <b>skeletal muscle</b> وقت الـ contraction.</li></ul></div>

<div class="card"><h4>🔄 Lec 5 — PDH &amp; Krebs</h4>
<ul><li>الـ <b>PDH</b>: pyruvate (3C) → acetyl-CoA (2C)، ودي <b>oxidative decarboxylation</b> في الـ mitochondria. بيطلع NADH = <b>3 ATP</b>. بيتثبط بالـ <b>NADH و ATP و acetyl-CoA</b>، وبيتنشط بالـ <b>Calcium</b>.</li>
<li>الـ <b>TCA</b> في الـ <b>mitochondria</b> بس، عشان كده الـ RBCs مفيهاش Krebs. بيبدأ بـ <b>oxaloacetate (4C) + acetyl-CoA → citrate (6C، 3 COOH)</b>.</li>
<li>الدورة الواحدة: <b>2 CO₂ + 3 NADH + 1 FADH₂ + 1 ATP</b> = <b>12 ATP</b> لكل acetyl-CoA (9 + 2 + 1).</li>
<li>الـ ATP الوحيد بالـ substrate-level عند <b>succinyl-CoA → succinate</b> بالـ <b>succinyl-CoA synthetase</b>. والـ <b>11 ATP</b> الباقيين بالـ oxidative phosphorylation.</li>
<li>الـ Dehydrogenases (<b>IKSM</b>): Isocitrate و α-Ketoglutarate (دول بيطلعوا CO₂)، و <b>Succinate (FADH₂)</b>، و Malate.</li>
<li>الأهمية: energy، و<b>final common pathway</b> للـ carbs والدهون والبروتين، و<b>interconversion</b> (gluconeogenesis و lipogenesis و non-essential amino acids).</li>
<li>الـ <b>NADH/NAD و ATP/ADP العاليين بيثبطوه</b>. وهو <b>aerobic بس</b>.</li>
<li>Pyruvate كامل = 3 + 12 = <b>15 ATP</b>.</li></ul></div>

<div class="card"><h4>🍬 Lec 6 — Glycogen</h4>
<table><tr><th></th><th>Liver</th><th>Muscle</th></tr>
<tr><td>% wet weight</td><td><b>8–10%</b> (حوالي 100 g)</td><td><b>2%</b> بس، والمخزون <b>3–4 أضعاف</b> (حوالي 300 g)</td></tr>
<tr><td>Function</td><td><b>Blood glucose</b> بين الوجبات (store للجسم كله)</td><td>Private store للعضلة وقت الـ contraction</td></tr>
<tr><td>Sources</td><td>Glucose و hexoses و glycerol و glucogenic amino acids و lactate</td><td><b>Blood glucose بس</b></td></tr>
<tr><td>Fate</td><td>Blood glucose</td><td><b>Lactic acid</b></td></tr>
<tr><td>بيخلص</td><td>بعد <b>12–18 ساعة</b> صيام</td><td>بعد exercise طويل بس</td></tr>
<tr><td>Starvation / Exercise</td><td>بيتكسر بسرعة / مش بيتأثر</td><td>مش بيتأثر / بيتستهلك</td></tr></table>
<ul><li>الـ <b>Glycogenesis</b>: glycogen synthase (key enzyme) + branching enzyme، وبيتنشط بالـ <b>insulin</b>. الـ <b>Glycogenolysis</b>: glycogen phosphorylase + debranching، وبيطلع <b>glucose-1-phosphate</b>. الاتنين في الـ <b>cytoplasm</b>.</li>
<li>بينشطوا الـ phosphorylase: <b>Glucagon (liver بس)</b>، و<b>Epinephrine (liver و muscle)</b>، و<b>AMP (muscle)</b>.</li>
<li>G1P ⇌ G6P بالـ <b>phosphoglucomutase</b>. والـ G6P → glucose بالـ <b>G6Pase</b>، وده موجود في الكبد ومش موجود في العضلات (<b>MCQ</b>).</li></ul></div>

<div class="card"><h4>🛡️ Lec 7 — HMP shunt</h4>
<ul><li>الـ <b>Alternative pathway</b> لأكسدة الـ glucose (حوالي 10%). في الـ <b>cytoplasm</b>: liver، adipose، adrenals، ovaries، testis، <b>RBCs</b>، retina.</li>
<li>G6P ← <b>NADPH + ribose-5-phosphate</b>.</li>
<li><b>R-5-P</b> للـ nucleotides والـ nucleic acids (DNA و RNA). والـ ribose اللي في الأكل بيطلع في البول، لأن مفيش <b>pentokinase</b>.</li>
<li>الـ HMP <b>main source of NADPH</b>، والـ NADPH بيستخدم في:
<ul><li><b>Fatty acid synthesis</b>: liver، adipose، lactating mammary gland.</li>
<li><b>Steroid synthesis</b>: adrenal cortex، testis، ovaries، placenta.</li>
<li><b>Vision</b>: الـ retinal reductase بيحول retinal → retinol.</li></ul></li>
<li>في الـ <b>RBCs</b>: الـ H₂O₂ oxidant قوي. الـ <b>Glutathione peroxidase (Se)</b> بيشيله: H₂O₂ + 2GSH → H₂O + GSSG. والـ <b>Glutathione reductase</b> بيرجّع الـ GSH بالـ <b>NADPH</b>.</li>
<li>الـ <b>Lipid peroxidation</b> بتعمل membrane fragility، فيحصل lysis ← anemia و jaundice.</li>
<li><b>Favism</b>: نقص <b>G6PD</b> (الـ rate-limiting enzyme للـ HMP، وراثي)، فالـ NADPH يقل. بيظهر مع <b>fava beans</b> أو drugs (<b>aspirin، sulfonamides، primaquine</b>).</li>
<li>الـ <b>Insulin</b> بيزود الـ HMP (inducer لتصنيع الـ G6PD).</li></ul></div>
"""

T("mid", "تجميعة الميد — Lec 1 to 7", "تجميعة الميد", "⭐",
  "ملخصات المحاضرات 1–7 بتحديداتها + أسئلة الدفعة",
  SHEET,
[
 ("Lec 1 — Bioenergetics & ATP", [
  ("If a given reaction is known to be energetically favorable, the value of ΔG is expected to be:", ["< zero", "> zero", "≤ zero", "≥ zero"], "qz", ""),
  ("ΔG is the difference between:", ["Energy of products and energy of reactants", "Energy of enzyme and substrate", "Heat and work", "ATP and ADP"], "imp", ""),
  ("If ΔG of a reaction is negative, the reaction is:", ["Exergonic", "Endergonic", "At equilibrium", "Non-spontaneous"], "imp", ""),
  ("Exergonic reactions are reactions that …… energy:", ["Produce", "Consume", "Store", "Neither produce nor consume"], "imp", ""),
  ("ΔG in endergonic reactions is:", ["Positive", "Negative", "Zero", "Always equal to 7 kcal"], "imp", ""),
  ("If ΔG is zero, it means:", ["The reaction runs in both directions (equilibrium)", "The reaction is mainly moving forward", "The reaction is mainly moving backward", "There is no reaction"], "qz", "مفيش طاقة اتنتجت ولا اتستهلكت."),
  ("Which statement about endergonic reactions is INCORRECT?", ["It occurs spontaneously", "The sign of ΔG is positive", "The product energy is higher than that of substrates", "It is an anabolic (building) reaction"], "qz", ""),
  ("Burning of 1 g of carbohydrates produces:", ["4 kcal", "9 kcal", "7 kcal", "2 kcal"], "imp", "Lipid 9، Protein 4."),
  ("Catabolism refers to:", ["Breakdown reactions that produce energy", "Building reactions that consume energy", "Reactions at equilibrium", "Storage of fat only"], "", ""),
  ("Combination of adenine with ribose sugar produces:", ["Adenosine", "Adenine nucleotide only", "Ribulose", "ATP"], "imp", ""),
  ("The bond between carbon 5 of ribose and phosphate is:", ["Ester bond (low energy)", "Acid anhydride bond (high energy)", "Peptide bond", "Glycosidic bond"], "imp", ""),
  ("The bond between phosphate groups in ATP is:", ["Acid anhydride (phosphoanhydride) bond — high energy", "Ester bond — low energy", "Hydrogen bond", "Peptide bond"], "imp", ""),
  ("Number of high-energy bonds in ADP:", ["1", "2", "0", "3"], "imp", "ATP فيه 2 و AMP صفر."),
  ("Number of high-energy bonds in AMP:", ["0", "1", "2", "3"], "imp", ""),
  ("Number of low-energy bonds in ATP:", ["1", "2", "3", "0"], "imp", "الـ ester."),
  ("The alcohol group (CH₂OH) in ribose that binds phosphate is at:", ["Carbon 5", "Carbon 1", "Carbon 2", "Carbon 3"], "imp", ""),
  ("A bond is considered high energy if its breakdown gives more than about:", ["7 kcal", "1 kcal", "20 kcal", "100 kcal"], "", ""),
  ("Creatine~P + ADP → ATP is an example of:", ["Substrate-level phosphorylation", "Oxidative phosphorylation", "Photophosphorylation", "Uncoupling"], "imp", "Minor method لتكوين الـ ATP."),
 ]),
 ("Lec 2 — Electron transport chain", [
  ("The electron transport chain takes place in the:", ["Inner mitochondrial membrane", "Outer mitochondrial membrane", "Cytosol", "Mitochondrial matrix only"], "imp", ""),
  ("The final electron acceptor in the ETC is:", ["Oxygen (Complex IV)", "NAD⁺", "FAD", "CO₂"], "imp", ""),
  ("During electron transfer, protons are pumped into the:", ["Intermembrane space", "Matrix", "Cytosol", "Nucleus"], "imp", "فبيتكوّن الـ proton gradient."),
  ("Protons return to the matrix through:", ["Complex V (ATP synthase)", "Complex I", "Complex III", "Complex IV"], "imp", ""),
  ("Oxidation of one NADH in the respiratory chain gives:", ["3 ATP", "2 ATP", "1 ATP", "12 ATP"], "imp", "والـ FADH₂ بيدي 2."),
  ("Uncouplers allow …… but prevent ……", ["Oxidation; phosphorylation", "Phosphorylation; oxidation", "Glycolysis; TCA", "Digestion; absorption"], "imp", "الـ membrane بيبقى permeable للـ protons، فالطاقة بتطلع heat."),
  ("Toxic doses of aspirin raise body temperature because aspirin acts as:", ["An uncoupler", "An ETC inhibitor of Complex V only", "An activator of PFK-1", "A source of NADPH"], "", ""),
  ("Thermogenin is a physiological uncoupler present in:", ["Newborns", "Elderly", "Athletes' muscles", "RBCs"], "imp", "بيولّد حرارة بدل ATP."),
  ("Starch is digested by amylase first into:", ["Dextrin", "Glucose", "Lactose", "Sucrose"], "", "وبعدين maltose و isomaltose."),
 ]),
 ("Lec 3 & 4 — Glycolysis", [
  ("Aerobic glycolysis ends with …… while anaerobic glycolysis ends with ……", ["Pyruvate; lactate", "Lactate; pyruvate", "Acetyl-CoA; ethanol", "CO₂; pyruvate"], "imp", ""),
  ("What is the end product of glycolysis in RBCs?", ["Lactate", "Pyruvate", "Acetyl CoA", "Ethanol"], "qz", "الـ RBCs مفيهاش mitochondria."),
  ("Which statement is NOT true about glycolysis?", ["It requires O₂ and the final product is CO₂", "Glucose is transformed into pyruvate", "It can take place by anaerobic metabolism", "It takes place mainly in the cytoplasm"], "qz", ""),
  ("The first step of glycolysis (glucose → glucose-6-P) is catalyzed by:", ["Hexokinase or glucokinase", "Isomerase", "Aldolase", "Enolase"], "imp", "أول خطوة بتستهلك ATP، وكمان بتحبس الـ glucose جوه الخلية."),
  ("Conversion of glucose-6-P to fructose-6-P is catalyzed by:", ["Isomerase", "Mutase", "Kinase", "Dehydrogenase"], "", ""),
  ("What is the rate-limiting step in glycolysis?", ["Formation of fructose 1,6-bisphosphate (PFK-1)", "Phosphorylation of glucose", "Formation of phosphoenolpyruvate", "Cleavage of fructose 1,6-bisphosphate"], "qz", "⚠️ Step 3 (PFK-1) هي أهم خطوة. الإجابة اللي كانت متحطوطة (Cleavage) غلط، الـ cleavage ده شغل الـ aldolase."),
  ("ATP-consuming steps of glycolysis are catalyzed by:", ["Hexokinase and PFK-1", "Pyruvate kinase and PGK", "Aldolase and enolase", "Isomerase and mutase"], "imp", "Steps 1 و 3."),
  ("Cleavage of fructose 1,6-bisphosphate into G3P and DHAP is by:", ["Aldolase", "PFK-1", "Enolase", "Isomerase"], "imp", ""),
  ("Conversion of 2 G3P into 2 1,3-bisphosphoglycerate produces:", ["2 NADH", "2 ATP", "2 FADH₂", "2 CO₂"], "imp", ""),
  ("1,3-bisphosphoglycerate → 3-phosphoglycerate is catalyzed by:", ["Phosphoglycerate kinase (2 ATP)", "Pyruvate kinase", "Mutase", "Enolase"], "imp", "Substrate-level phosphorylation."),
  ("Shifting phosphate from carbon 3 to carbon 2 (3PG → 2PG) is by:", ["Mutase", "Enolase", "Isomerase", "Kinase"], "", ""),
  ("Enolase converts 2-phosphoglycerate to:", ["Phosphoenolpyruvate (high-energy bond)", "Pyruvate", "3-phosphoglycerate", "Lactate"], "", ""),
  ("Which of the following is accompanied by formation of ATP?", ["Pyruvate kinase", "Hexokinase", "Glucokinase", "Phosphofructokinase"], "qz", ""),
  ("Irreversible key enzymes of glycolysis are all EXCEPT:", ["Aldolase", "Hexokinase/glucokinase", "PFK-1", "Pyruvate kinase"], "imp", ""),
  ("Hexokinase is inhibited by:", ["Glucose-6-phosphate (feedback)", "AMP", "Insulin", "Fructose-6-phosphate"], "imp", ""),
  ("PFK-1 is activated by …… and inhibited by ……", ["AMP; ATP and citrate", "ATP; AMP", "Citrate; AMP", "Glucagon; insulin"], "imp", "الدكتور قال الـ regulators دول مهمين."),
  ("Which increases glycolysis in muscle?", ["AMP", "ATP", "Citrate", "Glucose-6-phosphate"], "qz", ""),
  ("Pyruvate kinase is active when it is:", ["Dephosphorylated", "Phosphorylated", "Bound to ATP", "Bound to citrate"], "imp", ""),
  ("Glycolysis is stimulated by …… and inhibited by ……", ["Insulin; glucagon", "Glucagon; insulin", "Epinephrine; AMP", "ATP; AMP"], "imp", ""),
  ("Net ATP produced per glucose in aerobic glycolysis is:", ["8", "2", "4", "12"], "qz", "⚠️ 2 ATP net + 2 NADH × 3 = 8 (بحساب المحاضرات NADH = 3). مفتاح الدفعة كان 7، وده بحساب NADH = 2.5."),
  ("In glycolysis, ATP consumed is …… and ATP gained is ……", ["2; 4", "4; 2", "2; 2", "1; 4"], "imp", "Net 2."),
  ("Glycolysis is most needed in RBCs and contracting skeletal muscle because:", ["They have no alternative source for energy", "They have many mitochondria", "They store fat", "They lack glucose transporters"], "", ""),
 ]),
 ("Lec 5 — PDH & Krebs' cycle", [
  ("Pyruvate → acetyl-CoA (oxidative decarboxylation) occurs in the:", ["Mitochondria", "Cytosol", "ER", "Lysosome"], "qz", ""),
  ("Pyruvate dehydrogenase is activated by:", ["Calcium", "NADH", "ATP", "Acetyl-CoA"], "imp", "والـ NADH والـ ATP والـ acetyl-CoA بيثبطوه."),
  ("Which inhibits PDH?", ["Acetyl-CoA", "Calcium", "AMP", "NAD⁺"], "qz", ""),
  ("Krebs' cycle begins by condensation of acetyl-CoA with:", ["Oxaloacetate to form citrate", "Pyruvate to form malate", "Succinate to form fumarate", "Citrate to form isocitrate"], "imp", "Citrate فيه 3 COOH، عشان كده اسمه tricarboxylic."),
  ("The site of Krebs' cycle is the:", ["Mitochondria", "Cytosol", "Nucleus", "Cell membrane"], "imp", "عشان كده الـ RBCs مفيهاش Krebs."),
  ("During one turn of Krebs' cycle, the following are produced:", ["2 CO₂, 3 NADH, 1 FADH₂, 1 ATP", "3 CO₂, 2 NADH, 2 FADH₂", "1 CO₂, 1 NADH, 3 ATP", "2 CO₂, 2 NADH, 2 ATP"], "imp", ""),
  ("How many NADH + H⁺ are produced via the citric acid cycle per one glucose molecule?", ["6", "3", "4", "5"], "qz", "3 لكل acetyl-CoA × 2."),
  ("One mole of acetyl-CoA oxidized through Krebs' cycle gives:", ["12 ATP", "15 ATP", "8 ATP", "2 ATP"], "imp", ""),
  ("How many ATPs are produced from the (complete) oxidation of pyruvate?", ["15", "12", "18", "21"], "qz", "⚠️ 3 (PDH) + 12 (Krebs) = 15 بحساب المحاضرات. مفتاح الدفعة كان 12، وده بتاع الـ acetyl-CoA بس."),
  ("The only substrate-level phosphorylation in Krebs' cycle is catalyzed by:", ["Succinyl-CoA synthetase", "Isocitrate dehydrogenase", "Citrate synthase", "Malate dehydrogenase"], "imp", "Succinyl-CoA → succinate. والـ 11 ATP الباقيين oxidative."),
  ("The FADH₂-producing dehydrogenase of Krebs' cycle is:", ["Succinate dehydrogenase", "Malate dehydrogenase", "Isocitrate dehydrogenase", "α-Ketoglutarate dehydrogenase"], "", ""),
  ("Which enzyme produces CO₂ in the TCA cycle?", ["Isocitrate dehydrogenase", "Succinate dehydrogenase", "Malate dehydrogenase", "Citrate synthase"], "qz", "والـ α-KG dehydrogenase كمان."),
  ("Which statement regarding the TCA cycle is true?", ["It is not confined to carbohydrate metabolism", "It is an anaerobic process", "It occurs in the cytosol", "It contains no intermediates for gluconeogenesis"], "qz", "Final common pathway."),
  ("Krebs' cycle is inhibited by high:", ["NADH/NAD and ATP/ADP ratios", "AMP", "ADP", "NAD⁺"], "imp", ""),
 ]),
 ("Lec 6 — Glycogen metabolism", [
  ("The main storage form of carbohydrates in animal tissue is:", ["Glycogen", "Starch", "Cellulose", "Amylose"], "qz", ""),
  ("Liver glycogen forms about …… of the wet weight of the liver:", ["8–10%", "2%", "50%", "0.5%"], "imp", "والعضلات 2%."),
  ("Liver glycogen is depleted after:", ["12–18 hours fasting", "2 hours fasting", "5 days fasting", "1 hour of exercise"], "imp", ""),
  ("Although muscle glycogen is only 2% of muscle weight, its total store is:", ["3–4 times that of liver", "Half that of liver", "Equal to liver", "10 times less than liver"], "imp", "حوالي 300 g مقابل 100 g."),
  ("Liver glycogen is used mainly for:", ["Blood glucose maintenance", "Muscle contraction", "Fatty acid oxidation", "Ketone synthesis"], "qz", ""),
  ("Primary role of muscle glycogen:", ["Provide glucose within muscle during contraction", "Maintain blood glucose", "Provide glucose to other organs", "Ketone synthesis"], "qz", ""),
  ("The only source of muscle glycogen is:", ["Blood glucose", "Lactate", "Glycerol", "Amino acids"], "", ""),
  ("The fate of muscle glycogen is:", ["Lactic acid", "Blood glucose", "Fatty acids", "Ketones"], "", ""),
  ("In starvation, muscle glycogen is:", ["Not affected", "Broken rapidly to glucose", "Converted to fat", "Doubled"], "", "وفي الـ exercise بقى الـ liver glycogen هو اللي مش بيتأثر."),
  ("The key enzyme of glycogenesis is:", ["Glycogen synthase", "Glycogen phosphorylase", "Glucose-6-phosphatase", "Hexokinase"], "imp", ""),
  ("Glycogenolysis breaks glycogen into:", ["Glucose-1-phosphate", "Glucose-6-phosphate", "Free glucose only", "UDP-glucose"], "imp", "بالـ glycogen phosphorylase + debranching."),
  ("Rate-limiting enzyme of glycogenolysis:", ["Glycogen phosphorylase", "Glycogen synthase", "PFK-1", "Branching enzyme"], "qz", ""),
  ("Which statement is characteristic of the debranching enzyme?", ["It breaks an α-1,6 glycosidic linkage", "It requires ATP hydrolysis", "It releases UDP-glucose", "It synthesizes glycogen"], "qz", ""),
  ("Glucagon activates glycogen phosphorylase in:", ["Liver only", "Muscle only", "Liver and muscle", "Neither"], "imp", "Epinephrine في الاتنين، و AMP في العضلات."),
  ("Hormonal activator of glycogen phosphorylase in muscle:", ["Epinephrine", "Insulin", "Glucagon", "Thyroxine"], "qz", ""),
  ("Glycogen synthase is stimulated by:", ["Insulin", "Glucagon", "Epinephrine", "AMP"], "imp", ""),
  ("Glucose-1-phosphate ⇌ glucose-6-phosphate is catalyzed by:", ["Phosphoglucomutase", "Glucose-6-phosphatase", "Hexokinase", "Isomerase"], "", ""),
  ("Muscles cannot supply blood glucose due to lack of:", ["Glucose-6-phosphatase", "Glycogen phosphorylase", "Glycogen synthase", "Hexokinase"], "imp", "دي MCQ أكيد."),
  ("Glycogen metabolism occurs in the …… of liver and muscle cells:", ["Cytoplasm", "Mitochondria", "Nucleus", "Lysosomes"], "", ""),
 ]),
 ("Lec 7 — HMP shunt", [
  ("HMP shunt is:", ["An alternative pathway for oxidation of glucose", "The main pathway for ATP production", "A pathway of glycogen synthesis", "Part of Krebs' cycle"], "imp", "حوالي 10%."),
  ("HMP shunt occurs in the:", ["Cytoplasm", "Mitochondria", "Nucleus", "Lysosomes"], "imp", ""),
  ("HMP shunt is active in all EXCEPT:", ["Skeletal muscle", "Red blood cells", "Adrenals", "Retina"], "", "الأماكن: liver، adipose، adrenals، ovaries، testis، RBCs، retina."),
  ("The main products of HMP shunt are:", ["NADPH and ribose-5-phosphate", "ATP and lactate", "NADH and pyruvate", "FADH₂ and CO₂ only"], "imp", ""),
  ("Ribose-5-phosphate is important for synthesis of:", ["Nucleotides and nucleic acids", "Fatty acids", "Glycogen", "Steroids"], "imp", ""),
  ("Dietary ribose is excreted in urine because there is no:", ["Pentokinase", "G6PD", "Hexokinase", "Transketolase"], "", ""),
  ("The main source of NADPH in the body is:", ["HMP shunt", "Glycolysis", "Krebs' cycle", "ETC"], "imp", ""),
  ("NADPH from HMP is needed for all EXCEPT:", ["Glycogenolysis", "Fatty acid synthesis", "Steroid synthesis", "Vision (retinal → retinol)"], "imp", ""),
  ("HMP is very important in the lactating mammary gland for:", ["Fatty acid synthesis", "Steroid synthesis", "Vision", "Glycogen storage"], "", ""),
  ("HMP is active in adrenal cortex, testis, ovaries and placenta for:", ["Steroid synthesis", "Fatty acid synthesis", "Vision", "Nucleotide breakdown"], "", ""),
  ("In the eye, retinal reductase uses NADPH to convert:", ["Retinal into retinol", "Retinol into retinal", "Retinoic acid into retinal", "Rhodopsin into opsin"], "", ""),
  ("H₂O₂ in RBCs is removed by:", ["Glutathione peroxidase (and glutathione reductase)", "Catalase only", "PFK-1", "Pyruvate kinase"], "imp", ""),
  ("Glutathione peroxidase contains:", ["Selenium", "Iron", "Zinc", "Copper"], "", ""),
  ("Glutathione reductase regenerates reduced glutathione (GSH) using:", ["NADPH", "NADH", "FADH₂", "ATP"], "imp", ""),
  ("Lipid peroxidation in RBCs leads to:", ["Increased cell membrane fragility", "Increased glycogen", "Decreased H₂O₂", "Increased NADPH"], "", "فبيحصل lysis ← anemia و jaundice."),
  ("Favism is due to deficiency of:", ["Glucose-6-phosphate dehydrogenase (G6PD)", "Pyruvate kinase", "Glucose-6-phosphatase", "Glycogen phosphorylase"], "imp", "الـ rate-limiting enzyme للـ HMP."),
  ("In favism, hemolysis occurs because of decreased production of:", ["NADPH", "ATP", "NADH", "Lactate"], "imp", ""),
  ("Hemolysis in G6PD deficiency can be precipitated by all EXCEPT:", ["Insulin", "Fava beans", "Primaquine", "Sulfonamides"], "imp", "والـ aspirin كمان."),
  ("Insulin increases HMP activity by:", ["Inducing synthesis of G6PD", "Inhibiting G6PD", "Activating glycogen phosphorylase", "Inhibiting NADPH"], "", ""),
 ]),
 ("True or False", [
  tf("Exergonic reactions are spontaneous.", 0, ""),
  tf("ATP contains 3 high-energy bonds.", 1, "2 بس."),
  tf("Uncouplers allow ATP synthesis but stop oxidation.", 1, "العكس."),
  tf("Glucose 6-phosphate is an activator of hexokinase.", 1, "Inhibitor."),
  tf("ATP is an activator of glycolysis.", 1, "Inhibitor."),
  tf("Pyruvate kinase is inactive when phosphorylated.", 0, ""),
  tf("Glycolysis occurs in the mitochondria.", 1, "Cytosol."),
  tf("RBCs are totally dependent on substrate-level phosphorylation for energy production.", 0, ""),
  tf("Krebs' cycle can work under anaerobic conditions.", 1, "Aerobic بس."),
  tf("Glucose 6-phosphatase is deficient in the liver.", 1, "موجود في الكبد، والناقص منه العضلات."),
  tf("Muscle glycogenolysis is activated by glucagon.", 1, "No effect on muscle."),
  tf("Muscle glycogen can maintain blood glucose.", 1, "Never."),
  tf("G6PD is the rate-limiting enzyme of HMP.", 0, ""),
  tf("Favism is an acquired condition.", 1, "Genetic."),
 ], "fixed"),
])

# ============================================================ بنك المنهج كله
T("bank", "بنك المنهج كله — أسئلة الدفعة برا محاضرات الميد", "بنك المنهج كله", "📚",
  "أسئلة الدفعة اللي على مواضيع مش في المحاضرات 1–7",
"""<div class="card"><h4>📌 ملحوظة</h4>
<ul><li>الأسئلة دي على Gluconeogenesis و Fructose و GLUTs و PFK-2، ودي مواضيع <b>مش موجودة في المحاضرات 1–7</b>. يعني دي أسئلة على المنهج كله (الفاينال).</li>
<li>الأسئلة من 31 لـ 78 مكانتش موجودة في اللي اتبعت.</li>
<li>شيلت سؤال 94 لأنه غلط علميًا: الـ fructose-1-phosphate بينشط الـ glucokinase مش بيثبطه.</li></ul></div>""",
[
 ("Glucose transport & glycolysis regulation", [
  ("Which glucose transporter is insulin-dependent?", ["GLUT 4", "GLUT 1", "GLUT 2", "GLUT 3"], "qz", ""),
  ("GLUT2 is found mainly in:", ["Liver", "RBCs", "Brain", "Muscle"], "qz", ""),
  ("Main function of PFK-2:", ["Makes fructose 2,6-bisphosphate", "Makes fructose 1,6-bisphosphate", "Makes glucose 6-phosphate", "Makes pyruvate"], "qz", ""),
  ("Insulin activates PFK-2, which:", ["Activates glycolysis", "Inhibits glycolysis", "Activates gluconeogenesis", "Activates TCA"], "qz", ""),
  ("Which enzyme regenerates NAD⁺ in anaerobic glycolysis?", ["LDH", "PFK", "PDH", "GAPDH"], "qz", ""),
  ("Pyruvate kinase deficiency causes:", ["Hemolytic anemia", "Lactic acidosis", "Hypoglycemia", "Hyperglycemia"], "qz", ""),
 ]),
 ("Gluconeogenesis", [
  ("Which enzyme is involved in gluconeogenesis?", ["Pyruvate carboxylase", "Hexokinase", "Phosphofructokinase", "Pyruvate kinase"], "qz", ""),
  ("Rate-limiting enzyme of gluconeogenesis:", ["Fructose 1,6-bisphosphatase", "Pyruvate carboxylase", "PEP carboxykinase", "Glucose 6-phosphatase"], "qz", ""),
  ("Enzyme requiring biotin:", ["Pyruvate carboxylase", "PFK", "Pyruvate kinase", "LDH"], "qz", ""),
  ("Which enzyme forms phosphoenolpyruvate in gluconeogenesis?", ["PEP carboxykinase", "Pyruvate kinase", "LDH", "Hexokinase"], "qz", ""),
  ("Which is NOT used to synthesize glucose?", ["Acetyl CoA", "Oxaloacetate", "Lactate", "Pyruvate"], "qz", ""),
  ("Which amino acid is purely ketogenic (NOT glucogenic)?", ["Leucine", "Isoleucine", "Valine", "Alanine"], "qz", ""),
 ]),
 ("Glycogen & fructose (extra)", [
  ("The glycogen branching enzyme forms which bond?", ["α-1,6", "α-1,4", "β-1,4", "β-1,6"], "qz", ""),
  ("Allosteric inhibitor of muscle glycogen phosphorylase:", ["ATP", "AMP", "Ca²⁺", "cAMP"], "qz", "⚠️ نص السؤال كان ناقص، فكملته من الاختيارات والإجابة."),
  ("Which inhibits glycogen synthase?", ["Glucagon", "Insulin", "Glucose", "Glucose 6-phosphate"], "qz", ""),
  ("Main fate of fructose in the liver:", ["Enters glycolysis", "Enters PPP", "Converted to galactose", "Turns into ribose"], "qz", ""),
  ("Rate-limiting enzyme of fructose metabolism:", ["Aldolase B", "Aldolase A", "Hexokinase", "Glucokinase"], "qz", ""),
 ]),
 ("True or False", [
  tf("Fructose 2,6-bisphosphate activates glycolysis.", 0, ""),
  tf("All enzymes required for gluconeogenesis are present in the cytosol.", 1, "الـ Pyruvate carboxylase في الـ mitochondria."),
 ], "fixed"),
])
