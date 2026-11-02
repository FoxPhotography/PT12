# -*- coding: utf-8 -*-

short_notes_list = [
    # Topic 1: Radiation Laws
    {
        "id": "sn1",
        "topic": "Electromagnetic Spectrum & Physical Radiation Laws",
        "title": "State and explain the Inverse Square Law and Cosine Law in electrotherapy with their clinical significance.",
        "icon": "📐",
        "badge": "Physical Laws",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">1. Inverse Square Law:</h4>
            <p><strong>Definition:</strong> The intensity of radiation (I) received by a surface is inversely proportional to the square of the distance (d) from the source: <code>I ∝ 1 / d²</code>.</p>
            <ul class="sn-list">
                <li><strong>Clinical Significance:</strong> If the distance of an IR/UV lamp is doubled (e.g. from 50 cm to 100 cm), intensity drops to <strong>1/4 (25%)</strong>. If distance is halved, intensity increases <strong>4 times (400%)</strong>. Precise distance measurement is vital to avoid patient skin burns.</li>
            </ul>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">2. Cosine Law (Lambert's Law):</h4>
            <p><strong>Definition:</strong> Maximum absorption of radiant energy occurs when the radiant beam strikes the skin at a right angle (90° / perpendicular). As the angle shifts from 90°, intensity decreases according to <code>I = I₀ × cos θ</code>.</p>
            <ul class="sn-list">
                <li><strong>Clinical Significance:</strong> The lamp head must always be aligned perpendicular to the target treatment area to ensure maximum therapeutic absorption and prevent wasteful reflection.</li>
            </ul>
        </div>
        """
    },
    {
        "id": "sn2",
        "topic": "Electromagnetic Spectrum & Physical Radiation Laws",
        "title": "Explain Grotthus-Draper Law, Bunsen-Roscoe Law, and Arndt-Schultz Principle.",
        "icon": "📜",
        "badge": "Physical Laws",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Grotthus-Draper Law:</strong> Only radiation that is <em>absorbed</em> by biological tissues can produce physical or chemical effects. Reflected or transmitted energy produces no biological response.</li>
            <li><strong>Bunsen-Roscoe Law of Reciprocity:</strong> The biological photochemical effect is determined by the total energy absorbed: <code>Intensity × Exposure Time = Constant</code>.</li>
            <li><strong>Arndt-Schultz Principle:</strong> Weak stimuli promote/excite physiological activity; moderate stimuli support and favor it; strong stimuli inhibit it; excessive stimuli abolish and destroy tissue.</li>
        </ul>
        """
    },
    # Topic 2: IRR
    {
        "id": "sn3",
        "topic": "Infra-Red Radiation (IRR)",
        "title": "Compare between Luminous and Non-Luminous Infra-Red Generators.",
        "icon": "💡",
        "badge": "IRR Generators",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Luminous Generator</th>
                    <th>Non-Luminous Generator</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Source</strong></td>
                    <td>Tungsten / Carbon filament bulb</td>
                    <td>Carborundum / Porcelain coil wire</td>
                </tr>
                <tr>
                    <td><strong>Emission</strong></td>
                    <td>70% Near IR (IR-A) + 5% Visible + 25% Far IR</td>
                    <td>100% Far IR (IR-B & IR-C)</td>
                </tr>
                <tr>
                    <td><strong>Wavelength</strong></td>
                    <td>760 - 1400 nm (predominantly short)</td>
                    <td>1400 - 15000 nm (long wave)</td>
                </tr>
                <tr>
                    <td><strong>Penetration</strong></td>
                    <td>Deeper (1 - 3 mm, reaches dermis capillaries)</td>
                    <td>Superficial (< 0.5 mm, epidermis only)</td>
                </tr>
                <tr>
                    <td><strong>Warm-up Time</strong></td>
                    <td>Instant (no warm-up needed)</td>
                    <td>Requires 5 - 15 minutes pre-heating</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "id": "sn4",
        "topic": "Infra-Red Radiation (IRR)",
        "title": "List the main Physiological Effects, Indications, and Contraindications of Infra-Red Radiation.",
        "icon": "🔴",
        "badge": "IRR Clinical",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">A. Physiological Effects:</h4>
            <ul class="sn-list">
                <li>Cutaneous vasodilation & immediate mottled erythema.</li>
                <li>Sedative effect on sensory nerve endings & pain reduction (Gate Control mechanism).</li>
                <li>Muscle relaxation & reduction of muscle spasm.</li>
                <li>Increased local metabolism (10-13% per 1°C rise via Q10 effect) and tissue healing.</li>
            </ul>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">B. Indications:</h4>
            <ul class="sn-list">
                <li>Subacute and chronic musculoskeletal pain (e.g. chronic lumbago, cervicalgia, osteoarthritis).</li>
                <li>Muscle spasm prior to manual therapy or exercise.</li>
                <li>Chronic joint stiffness and contractures.</li>
            </ul>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">C. Absolute Contraindications:</h4>
            <ul class="sn-list">
                <li>Impaired skin thermal sensation (risk of severe burns).</li>
                <li>Acute hemorrhage or bleeding tendency.</li>
                <li>Malignant tumors over the treatment site.</li>
                <li>Severe peripheral vascular disease / Ischemic tissue.</li>
                <li>Unreliable patients (infants, dementia, severe unconsciousness).</li>
            </ul>
        </div>
        """
    },
    {
        "id": "sn5",
        "topic": "Infra-Red Radiation (IRR)",
        "title": "Explain the difference between Infra-Red Erythema and Ultraviolet Erythema.",
        "icon": "⚖️",
        "badge": "IR vs UV Erythema",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Infra-Red Erythema</th>
                    <th>Ultraviolet Erythema</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Onset / Latency</strong></td>
                    <td>Immediate during exposure</td>
                    <td>Delayed (latent period 6 - 8 hours)</td>
                </tr>
                <tr>
                    <td><strong>Appearance</strong></td>
                    <td>Mottled, patchy, irregular redness</td>
                    <td>Uniform, homogenous, well-demarcated redness</td>
                </tr>
                <tr>
                    <td><strong>Duration</strong></td>
                    <td>Fades rapidly within 30 - 60 minutes</td>
                    <td>Lasts several days to a week</td>
                </tr>
                <tr>
                    <td><strong>Mechanism</strong></td>
                    <td>Thermal vasodilation (axon reflex + local heat)</td>
                    <td>Photochemical release of Nitric Oxide & Prostaglandins</td>
                </tr>
                <tr>
                    <td><strong>Pigmentation</strong></td>
                    <td>None (unless chronic exposure causes Erythema Ab Igne)</td>
                    <td>Causes prominent tanning and epidermal thickening</td>
                </tr>
            </tbody>
        </table>
        """
    },
    # Topic 3: UVR
    {
        "id": "sn6",
        "topic": "Ultraviolet Therapy (UVR)",
        "title": "Discuss the Physiological Effects of Ultraviolet Radiation on the Skin.",
        "icon": "☀️",
        "badge": "UVR Physiology",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>1. Delayed Erythema:</strong> Caused by UVB via gradual photochemical release and accumulation of <em>Nitric Oxide</em> and prostaglandins around dermal capillaries.</li>
            <li><strong>2. Pigmentation (Tanning):</strong> Immediate tanning (UVA photo-oxidation of existing melanin) and delayed tanning (UVB stimulation of tyrosinase enzyme synthesizing new melanin in basal melanocytes).</li>
            <li><strong>3. Epidermal Thickening (Hyperplasia):</strong> Accelerated mitotic turnover of keratinocytes leads to thicker stratum corneum, serving as a biological protective filter.</li>
            <li><strong>4. Vitamin D3 Production:</strong> UVB converts <em>7-dehydrocholesterol</em> in skin oils to cholecalciferol (Vitamin D3), facilitating Calcium and Phosphorus absorption for bone mineralization.</li>
            <li><strong>5. Immunosuppressive Effect:</strong> UVB destroys epidermal <em>Langerhans cells</em> (Birbeck granules) and stimulates suppressor T-cells, preventing autoimmune attacks in psoriasis.</li>
            <li><strong>6. Bactericidal Effect:</strong> UV-C (260-280 nm) destroys bacterial DNA, used for sterilizing open infected wounds.</li>
        </ul>
        """
    },
    {
        "id": "sn7",
        "topic": "Ultraviolet Therapy (UVR)",
        "title": "Describe the Minimal Erythema Dose (MED) test and outline the Erythema Dosage Grades (E1, E2, E3, E4).",
        "icon": "📊",
        "badge": "UVR Dosage",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">A. MED Test Procedure:</h4>
            <p>Performed on forearm/abdomen using a test sleeve with 5-6 cutout openings exposed at 15-30 second intervals. The MED is the exposure time producing a <em>just-perceptible faint erythema at 6-8 hours that disappears within 24 hours without peeling</em>.</p>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">B. Dosage Degrees:</h4>
            <ul class="sn-list">
                <li><strong>E1 (First Degree):</strong> <code>1.25 × MED</code>. Faint pink, disappears in 24-48h, no peeling. Progressed by 25% each session.</li>
                <li><strong>E2 (Second Degree):</strong> <code>2.5 × MED</code>. Definite red sunburn, mild tenderness, fades in 2-3 days, powdery desquamation. Progressed by 50%.</li>
                <li><strong>E3 (Third Degree):</strong> <code>5 × MED</code>. Dark fiery red, severe edema, burning pain, lasts 1 week, peeling in sheets. Progressed by 75%.</li>
                <li><strong>E4 (Fourth Degree / Blistering):</strong> <code>10 × MED</code>. Destructive inflammation with blisters (bullae), restricted to small areas (< 25 cm²).</li>
            </ul>
        </div>
        """
    },
    {
        "id": "sn8",
        "topic": "Ultraviolet Therapy (UVR)",
        "title": "Compare the Kromayer Lamp and Alpine Sunlamp.",
        "icon": "🔦",
        "badge": "UV Lamps",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Kromayer Lamp</th>
                    <th>Alpine Sunlamp</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Cooling System</strong></td>
                    <td>Water-cooled (circulating water jacket)</td>
                    <td>Air-cooled</td>
                </tr>
                <tr>
                    <td><strong>Application Distance</strong></td>
                    <td>Can be applied in direct contact with tissue</td>
                    <td>Used at standardized distance (24 - 40 inches / 60-100 cm)</td>
                </tr>
                <tr>
                    <td><strong>Clinical Use</strong></td>
                    <td>Localized lesions, sinuses, mouth, open pressure ulcers</td>
                    <td>Generalized or large-area body irradiation</td>
                </tr>
                <tr>
                    <td><strong>Window Material</strong></td>
                    <td>Quartz crystal window (transmits UV rays)</td>
                    <td>Quartz burner tube</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "id": "sn9",
        "topic": "Ultraviolet Therapy (UVR)",
        "title": "Define Photokeratitis and state how it is prevented in physical therapy.",
        "icon": "🥽",
        "badge": "Eye Safety",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Definition:</strong> Photokeratitis ('arc eye' / snow blindness) is an acute inflammation of the conjunctiva and cornea caused by absorption of UV rays by ocular tissues.</li>
            <li><strong>Clinical Manifestation:</strong> Latent period of 6 to 24 hours followed by foreign body sensation ('sand in eyes'), severe photophobia, lacrimation, and blepharospasm.</li>
            <li><strong>Prevention:</strong> Opaque UV-absorbing safety goggles must be worn by <strong>both the patient and the physical therapist</strong> at all times during UV machine operation.</li>
        </ul>
        """
    },
    # Topic 4: Ultrasound
    {
        "id": "sn10",
        "topic": "Therapeutic Ultrasound (US)",
        "title": "Explain the Reverse Piezoelectric Effect and the crystal materials used in Ultrasound transducers.",
        "icon": "⚡",
        "badge": "US Physics",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Reverse (Converse) Piezoelectric Effect:</strong> When a high-frequency alternating electrical voltage is applied across a piezoelectric crystal, the crystal rapidly expands and contracts mechanically, generating ultrasonic acoustic compression-rarefaction waves.</li>
            <li><strong>Crystal Materials:</strong>
                <ul>
                    <li><strong>Synthetic PZT (Lead Zirconate Titanate):</strong> Most widely used in modern clinical ultrasound due to superior electro-acoustic efficiency, durability, and low cost.</li>
                    <li><strong>Natural Quartz:</strong> Historically used; chemically stable but requires very high voltage.</li>
                    <li><strong>Barium Titanate:</strong> Synthetic ceramic material.</li>
                </ul>
            </li>
        </ul>
        """
    },
    {
        "id": "sn11",
        "topic": "Therapeutic Ultrasound (US)",
        "title": "Compare 1 MHz vs 3 MHz Ultrasound Frequencies in Physical Therapy.",
        "icon": "📊",
        "badge": "US Frequencies",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>1 MHz Ultrasound</th>
                    <th>3 MHz Ultrasound</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Frequency</strong></td>
                    <td>1 Million cycles / second</td>
                    <td>3 Million cycles / second</td>
                </tr>
                <tr>
                    <td><strong>Penetration Depth</strong></td>
                    <td>Deep (3 to 5 cm)</td>
                    <td>Superficial (1 to 2.5 cm)</td>
                </tr>
                <tr>
                    <td><strong>Absorption Rate</strong></td>
                    <td>Lower superficial absorption, penetrates deeper</td>
                    <td>3 times faster absorption in superficial tissues</td>
                </tr>
                <tr>
                    <td><strong>Clinical Indications</strong></td>
                    <td>Hip joint, deep quadriceps, piriformis, sciatica, thick muscle belly</td>
                    <td>Lateral epicondylitis, patellar tendon, Achilles tendon, wrist ligaments, plantar fascia</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "id": "sn12",
        "topic": "Therapeutic Ultrasound (US)",
        "title": "Define ERA, BNR, Acoustic Impedance, and Standing Waves in Ultrasound.",
        "icon": "📐",
        "badge": "US Parameters",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>ERA (Effective Radiating Area):</strong> The actual surface area of the transducer crystal face that emits ultrasonic energy (always slightly smaller than the geometric soundhead face).</li>
            <li><strong>BNR (Beam Non-uniformity Ratio):</strong> Ratio of spatial peak intensity to spatial average intensity (<code>I_peak / I_avg</code>). Acceptable clinical range is <strong>2:1 to 6:1</strong>. Values > 6:1 produce dangerous hot spots.</li>
            <li><strong>Acoustic Impedance (Z):</strong> The resistance of a tissue to sound wave transmission: <code>Z = Tissue Density (ρ) × Velocity of Sound (c)</code>. Gel is mandatory to bridge the air-skin impedance mismatch.</li>
            <li><strong>Standing Waves:</strong> Created when reflected waves superimpose on incident waves at acoustic boundaries (e.g. bone periosteum). Prevented by continuously moving the transducer head at 2-4 cm/s.</li>
        </ul>
        """
    },
    {
        "id": "sn13",
        "topic": "Therapeutic Ultrasound (US)",
        "title": "Discuss the Non-Thermal Effects of Ultrasound (Cavitation, Acoustic Streaming, Micromassage).",
        "icon": "🌊",
        "badge": "US Non-Thermal",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>1. Stable Cavitation:</strong> Formation and rhythmic oscillation of microscopic gas bubbles in tissue fluids without collapsing. Increases cell membrane permeability and enhances tissue repair.</li>
            <li><strong>2. Acoustic Streaming & Microstreaming:</strong> Unidirectional physical fluid flow along acoustic boundaries, stimulating fibroblast activity, accelerating collagen synthesis, and enhancing cellular metabolism.</li>
            <li><strong>3. Micromassage:</strong> High-frequency microscopic mechanical compression and expansion of cells, reducing tissue edema and increasing membrane diffusion.</li>
            <li><em>Note on Transient Cavitation:</em> Violent implosion of bubbles occurring at excessively high intensities (> 3 W/cm²); hazardous and causes tissue destruction.</li>
        </ul>
        """
    },
    {
        "id": "sn14",
        "topic": "Therapeutic Ultrasound (US)",
        "title": "Define Phonophoresis and list its clinical advantages and commonly used medications.",
        "icon": "💊",
        "badge": "Phonophoresis",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Definition:</strong> Phonophoresis (sonophoresis) is the therapeutic use of ultrasound acoustic waves to drive topical drug molecules transdermally into target subcutaneous tissues.</li>
            <li><strong>Advantages:</strong> Non-invasive, painless, avoids gastrointestinal side effects and first-pass hepatic metabolism of oral drugs, avoids risk of needle injection infection.</li>
            <li><strong>Common Drugs Used:</strong>
                <ul>
                    <li>Anti-inflammatory corticosteroids (Hydrocortisone, Dexamethasone).</li>
                    <li>NSAIDs (Ketoprofen, Diclofenac gel).</li>
                    <li>Local anesthetics (Lidocaine for local pain relief).</li>
                </ul>
            </li>
        </ul>
        """
    },
    # Topic 5: SWD
    {
        "id": "sn15",
        "topic": "Shortwave Diathermy (SWD)",
        "title": "Compare between Capacitive and Inductive Shortwave Diathermy Methods.",
        "icon": "⚡",
        "badge": "SWD Methods",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Capacitive (Electric Field) Method</th>
                    <th>Inductive (Magnetic Field) Method</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Mechanism</strong></td>
                    <td>High-frequency alternating electric field between plates/pads</td>
                    <td>Time-varying magnetic field creating circular Eddy Currents</td>
                </tr>
                <tr>
                    <td><strong>Target Heating</strong></td>
                    <td>High-resistance / low-conductivity tissues (Subcutaneous fat & bone interfaces)</td>
                    <td>High-conductivity / vascular tissues (Deep muscle, blood, synovial fluid)</td>
                </tr>
                <tr>
                    <td><strong>Applicators</strong></td>
                    <td>Rigid Space Plates, flexible Rubber Pads</td>
                    <td>Housed Drum (Monode/Diplode), insulated Cable coil</td>
                </tr>
                <tr>
                    <td><strong>Heating Profile</strong></td>
                    <td>More superficial heating (fat layer)</td>
                    <td>True deep muscle heating (penetration 3 - 5 cm)</td>
                </tr>
                <tr>
                    <td><strong>Clinical Use</strong></td>
                    <td>Superficial joints, spine, fat-poor areas</td>
                    <td>Large deep muscle spasm (quadriceps, hamstrings, back)</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "id": "sn16",
        "topic": "Shortwave Diathermy (SWD)",
        "title": "Describe the Electrode Placement Configurations in Capacitive SWD (Contraplanar, Coplanar, Cross-fire, Longitudinal).",
        "icon": "🔌",
        "badge": "SWD Electrodes",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>1. Contraplanar Method:</strong> Electrodes placed on opposite sides of the body part (e.g. medial & lateral knee). Produces uniform deep heating of internal joint structures.</li>
            <li><strong>2. Coplanar Method:</strong> Electrodes placed side-by-side on the same surface of the body part (e.g. lumbar spine). Produces superficial heating of back musculature. Spacing between electrodes must equal at least the diameter of one electrode.</li>
            <li><strong>3. Cross-fire Method:</strong> Half of the treatment session is given with electrodes in one diagonal axis, and the remaining half in the perpendicular diagonal axis. Specially used for air-filled cavities (Sinuses) and pelvic organs (Uterus).</li>
            <li><strong>4. Longitudinal Method:</strong> Electrodes placed at opposite ends of a limb (e.g. upper thigh and foot) to direct current along the length of the limb.</li>
        </ul>
        """
    },
    {
        "id": "sn17",
        "topic": "Shortwave Diathermy (SWD)",
        "title": "List the Absolute Contraindications and Safety Precautions of Shortwave Diathermy.",
        "icon": "🚫",
        "badge": "SWD Safety",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">A. Absolute Contraindications:</h4>
            <ul class="sn-list">
                <li><strong>Metallic Implants / Surgical Pins / Jewelry:</strong> Metals have low impedance, concentrate field lines, and cause severe deep tissue burns.</li>
                <li><strong>Cardiac Pacemakers / Implanted Neurostimulators:</strong> RF interference disrupts electronic pacemaker function.</li>
                <li><strong>Impaired Thermal Sensation.</strong></li>
                <li><strong>Active Hemorrhage / Bleeding Tendency / Menstruation.</strong></li>
                <li><strong>Malignant Tumors</strong> (increases metastasis risk).</li>
                <li><strong>Pregnancy</strong> (teratogenic risk to fetus).</li>
                <li><strong>Acute Deep Vein Thrombosis (DVT) / Severe Ischemia.</strong></li>
            </ul>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">B. Critical Safety Precautions:</h4>
            <ul class="sn-list">
                <li>Skin must be completely dry (sweat concentrates electric field lines causing scalding burns).</li>
                <li>Maintain proper electrode spacing (2-4 cm) and at least 2 cm dry towel thickness with pad electrodes.</li>
            </ul>
        </div>
        """
    },
    {
        "id": "sn18",
        "topic": "Shortwave Diathermy (SWD)",
        "title": "Outline Schliephake's Dosage Classification for Shortwave Diathermy.",
        "icon": "🌡️",
        "badge": "SWD Dosage",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Grade I (Sub-thermal / Lowest):</strong> No sensation of heat. Used for acute inflammatory conditions (especially with Pulsed SWD).</li>
            <li><strong>Grade II (Mild / Low thermal):</strong> Barely perceptible, faint, gentle sensation of warmth. Used for subacute conditions.</li>
            <li><strong>Grade III (Moderate / Medium thermal):</strong> Distinct, comfortable, pleasant warmth. Used for chronic subacute pain and resolution of inflammation.</li>
            <li><strong>Grade IV (Vigorous / Heavy thermal):</strong> Strong, intense warmth just below pain threshold. Used for chronic joint contractures and dense fibrotic scar softening.</li>
        </ul>
        """
    },
    # Topic 6: Pain Physiology
    {
        "id": "sn19",
        "topic": "Physiology of Pain in Physical Therapy",
        "title": "Define Pain (IASP) and explain the 4 Neural Processes of Pain (Transduction, Transmission, Perception, Modulation).",
        "icon": "🧠",
        "badge": "Pain Basics",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">A. IASP Definition of Pain:</h4>
            <p>"An unpleasant sensory and emotional experience associated with, or resembling that associated with, actual or potential tissue damage."</p>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">B. The 4 Neural Processes:</h4>
            <ul class="sn-list">
                <li><strong>1. Transduction:</strong> Conversion of noxious mechanical, thermal, or chemical stimuli into electrical receptor potentials at free nerve endings (nociceptors).</li>
                <li><strong>2. Transmission:</strong> Propagation of electrical impulses along afferent fibers (A-delta and C) through dorsal horn, spinothalamic tract, and thalamus to the cortex.</li>
                <li><strong>3. Perception:</strong> Conscious subjective awareness and emotional interpretation of pain in the somatosensory cortex and limbic system.</li>
                <li><strong>4. Modulation:</strong> Dynamic physiological inhibition or amplification of pain signals along spinal and supraspinal neural circuits.</li>
            </ul>
        </div>
        """
    },
    {
        "id": "sn20",
        "topic": "Physiology of Pain in Physical Therapy",
        "title": "Comprehensive Comparison between A-beta, A-delta, and C Nerve Fibers.",
        "icon": "🔬",
        "badge": "Nerve Fibers",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>A-beta (Aβ) Fibers</th>
                    <th>A-delta (Aδ) Fibers</th>
                    <th>C-Fibers</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Diameter</strong></td>
                    <td>6 - 14 μm (Thick)</td>
                    <td>1 - 6 μm (Medium)</td>
                    <td>0.2 - 1.5 μm (Thin)</td>
                </tr>
                <tr>
                    <td><strong>Myelination</strong></td>
                    <td>Heavily Myelinated</td>
                    <td>Thinly Myelinated</td>
                    <td><strong>Unmyelinated</strong></td>
                </tr>
                <tr>
                    <td><strong>Conduction Velocity</strong></td>
                    <td>30 - 70 m/s (Fastest)</td>
                    <td>4 - 30 m/s (Medium)</td>
                    <td>0.5 - 2 m/s (Slowest)</td>
                </tr>
                <tr>
                    <td><strong>Threshold</strong></td>
                    <td>Low threshold</td>
                    <td>Medium threshold</td>
                    <td>High threshold</td>
                </tr>
                <tr>
                    <td><strong>Function / Sensation</strong></td>
                    <td>Light touch, vibration, hair movement, pressure (Closes pain gate)</td>
                    <td><strong>First Pain:</strong> Fast, sharp, pricking, well-localized pain</td>
                    <td><strong>Second Pain:</strong> Slow, dull, burning, aching, poorly localized pain</td>
                </tr>
                <tr>
                    <td><strong>Neurotransmitter</strong></td>
                    <td>Acetylcholine / Glutamate</td>
                    <td><strong>Glutamate</strong> (fast acting)</td>
                    <td><strong>Substance P</strong> & CGRP (slow acting)</td>
                </tr>
                <tr>
                    <td><strong>Spinal Termination</strong></td>
                    <td>Laminae III - VI (Dorsal horn)</td>
                    <td>Laminae I & V</td>
                    <td>Laminae II & III (Substantia Gelatinosa)</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "id": "sn21",
        "topic": "Physiology of Pain in Physical Therapy",
        "title": "Explain the Gate Control Theory of Pain (Melzack & Wall, 1965) with its clinical application in Physical Therapy.",
        "icon": "🚪",
        "badge": "Gate Control",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">A. Mechanism of Gate Control:</h4>
            <ul class="sn-list">
                <li>Located in the <strong>Substantia Gelatinosa (SG - Lamina II)</strong> of the spinal dorsal horn.</li>
                <li><strong>Transmission projection cells (T-cells)</strong> transmit pain impulses up the spinothalamic tract to the brain.</li>
                <li>Small nociceptive fibers (<strong>Aδ and C</strong>) carry noxious input and <em>inhibit</em> SG interneurons → <strong>Opens the Gate</strong> → T-cells fire actively → Pain is perceived.</li>
                <li>Large non-nociceptive fibers (<strong>Aβ</strong>) carry touch/vibration and <em>stimulate</em> inhibitory SG interneurons → <strong>Closes the Gate</strong> → Presynaptic inhibition blocks Aδ/C neurotransmitter release → T-cell firing is suppressed → Pain is blocked.</li>
            </ul>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">B. Clinical Application:</h4>
            <p>Explains why rubbing a bruised knee, massage, vibration, and high-frequency <strong>TENS (Transcutaneous Electrical Nerve Stimulation)</strong> provide immediate pain relief.</p>
        </div>
        """
    },
    {
        "id": "sn22",
        "topic": "Physiology of Pain in Physical Therapy",
        "title": "Describe the Descending Pain Modulatory (Inhibitory) Pathway and the role of Endogenous Opioids.",
        "icon": "🧬",
        "badge": "Descending Pathway",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>1. Origin:</strong> Initiates in the <strong>Periaqueductal Gray (PAG)</strong> matter of the midbrain.</li>
            <li><strong>2. Relay Nuclei:</strong> PAG sends excitatory projections to the <strong>Nucleus Raphe Magnus (NRM)</strong> in the rostral medulla.</li>
            <li><strong>3. Spinal Projection:</strong> Serotonergic and Noradrenergic axons descend via the dorsolateral funiculus to the spinal dorsal horn.</li>
            <li><strong>4. Presynaptic Inhibition:</strong> These descending fibers stimulate local enkephalinergic interneurons in Substantia Gelatinosa → release <strong>Enkephalin</strong> → binds to presynaptic opioid receptors on incoming C-fiber terminals → blocks Ca²⁺ channels and prevents <strong>Substance P</strong> release.</li>
            <li><strong>5. Endogenous Opioids:</strong>
                <ul>
                    <li><em>Beta-Endorphin:</em> Synthesized in anterior pituitary & hypothalamus (long-lasting systemic analgesia).</li>
                    <li><em>Enkephalins (Met- & Leu-enkephalin):</em> Synthesized locally in PAG and spinal dorsal horn.</li>
                    <li><em>Dynorphins:</em> Modulate spinal nociception.</li>
                </ul>
            </li>
        </ul>
        """
    },
    # Topic 7: Histology & Bio-electricity
    {
        "id": "sn23",
        "topic": "Organization of Body Tissue & Histology / Nerve Bio-electricity",
        "title": "Explain the 5 Layers of the Epidermis and the Histological Structure of the Skin.",
        "icon": "🔬",
        "badge": "Skin Histology",
        "answer_html": """
        <div class="sn-section">
            <h4 class="sn-subtitle">A. Epidermal Layers (Deep to Superficial):</h4>
            <ul class="sn-list">
                <li><strong>1. Stratum Basale (Germinativum):</strong> Single row of stem cells with rapid mitotic division; contains Melanocytes (melanin) and Merkel cells (touch).</li>
                <li><strong>2. Stratum Spinosum:</strong> Spiny prickle cells connected by desmosomes; contains antigen-presenting <em>Langerhans cells</em>.</li>
                <li><strong>3. Stratum Granulosum:</strong> 3-5 layers containing keratohyalin granules; cells begin to die.</li>
                <li><strong>4. Stratum Lucidum:</strong> Clear, thin layer of flat dead cells; present ONLY in thick skin (palms and soles).</li>
                <li><strong>5. Stratum Corneum:</strong> 20-30 layers of dead, anucleated keratinized scales; primary water barrier and highest electrical resistance barrier.</li>
            </ul>
        </div>
        <div class="sn-section">
            <h4 class="sn-subtitle">B. Dermis & Hypodermis:</h4>
            <ul class="sn-list">
                <li><strong>Dermis:</strong> Papillary layer (loose areolar, capillary loops, Meissner corpuscles) and Reticular layer (dense collagen, sweat glands, hair follicles, Arrector pili).</li>
                <li><strong>Hypodermis (Subcutaneous fat):</strong> Adipose tissue for thermal insulation and mechanical shock absorption.</li>
            </ul>
        </div>
        """
    },
    {
        "id": "sn24",
        "topic": "Organization of Body Tissue & Histology / Nerve Bio-electricity",
        "title": "Describe the Ionic Steps and Phases of a Nerve Action Potential.",
        "icon": "⚡",
        "badge": "Action Potential",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>1. Resting State:</strong> Resting Membrane Potential (RMP) is <code>-70 mV</code> (inside negative), maintained by high resting K⁺ permeability and the Na⁺/K⁺ ATPase pump.</li>
            <li><strong>2. Threshold:</strong> A depolarizing stimulus reaches <code>-55 mV</code>, triggering the opening of voltage-gated Na⁺ channels.</li>
            <li><strong>3. Depolarization Phase:</strong> Massive influx of Na⁺ rapidly drives the internal membrane potential up to <code>+30 mV</code> (All-or-None response).</li>
            <li><strong>4. Repolarization Phase:</strong> Voltage-gated Na⁺ channels inactivate and close; voltage-gated K⁺ channels open slowly, causing rapid K⁺ efflux back toward resting potential.</li>
            <li><strong>5. Hyperpolarization (Undershoot):</strong> Slower closure of K⁺ channels drives potential to <code>-90 mV</code>. This refractory state ensures unidirectional signal propagation.</li>
            <li><strong>6. Return to Resting Potential:</strong> The active <strong>Na⁺/K⁺ pump</strong> (pumping 3 Na⁺ out for 2 K⁺ in) restores baseline ionic concentrations.</li>
        </ul>
        """
    },
    {
        "id": "sn25",
        "topic": "Organization of Body Tissue & Histology / Nerve Bio-electricity",
        "title": "Classify Peripheral Nerve Fibers according to Erlanger & Gasser (Type A, B, and C).",
        "icon": "🗂️",
        "badge": "Nerve Classification",
        "answer_html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Class</th>
                    <th>Diameter</th>
                    <th>Myelination</th>
                    <th>Velocity</th>
                    <th>Examples / Functions</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Type A</strong></td>
                    <td>1.5 - 20 μm</td>
                    <td>Thickly Myelinated</td>
                    <td>4 - 120 m/s</td>
                    <td>Somatic motor (alpha/gamma), sensory afferents to muscle spindles and skin (touch, fast pain)</td>
                </tr>
                <tr>
                    <td><strong>Type B</strong></td>
                    <td>1.5 - 3.5 μm</td>
                    <td>Moderately Myelinated</td>
                    <td>3 - 15 m/s</td>
                    <td>Preganglionic autonomic visceral efferents</td>
                </tr>
                <tr>
                    <td><strong>Type C</strong></td>
                    <td>0.1 - 2.0 μm</td>
                    <td><strong>Unmyelinated</strong></td>
                    <td>0.5 - 2.0 m/s</td>
                    <td>Postganglionic sympathetic efferents, slow dull burning pain afferents, warm/cold thermoreceptors</td>
                </tr>
            </tbody>
        </table>
        """
    },
    # Clinical Scenarios / Exam Cases
    {
        "id": "sn26",
        "topic": "Clinical Scenario / Short Case",
        "title": "Case 1: A 45-year-old patient with chronic osteoarthritis of the knee and a metallic pin in the proximal tibia. What electrotherapy modality is contraindicated and what is safe?",
        "icon": "🏥",
        "badge": "Clinical Case",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Contraindicated Modality:</strong> <strong>Shortwave Diathermy (SWD)</strong> is ABSOLUTELY CONTRAINDICATED because the metallic pin has low electrical impedance, concentrates electric/magnetic field lines, and causes intense local heating leading to severe deep bone and tissue burns.</li>
            <li><strong>Safe Alternative Modalities:</strong>
                <ul>
                    <li>Superficial Infra-Red Radiation (IRR) or Hot Packs (heats superficial skin and capsular tissues safely without deep metallic overheating).</li>
                    <li>Transcutaneous Electrical Nerve Stimulation (TENS) for pain modulation via Gate Control Theory.</li>
                    <li>Pulsed Ultrasound (at low intensity, moving head technique, avoiding direct stationary exposure over the metal pin).</li>
                </ul>
            </li>
        </ul>
        """
    },
    {
        "id": "sn27",
        "topic": "Clinical Scenario / Short Case",
        "title": "Case 2: A 28-year-old tennis player presents with acute lateral epicondylitis (pain duration: 2 days). Detail your Ultrasound parameters and justification.",
        "icon": "🎾",
        "badge": "Clinical Case",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Frequency:</strong> <strong>3 MHz</strong> (because the common extensor tendon origin at the lateral epicondyle is a superficial structure, depth 1-2 cm).</li>
            <li><strong>Mode & Duty Cycle:</strong> <strong>Pulsed mode at 20% duty cycle</strong> (1:4 mark-to-space ratio) to eliminate thermal heating and obtain non-thermal acoustic streaming and stable cavitation for acute tissue repair.</li>
            <li><strong>Intensity:</strong> Low intensity: <strong>0.5 to 0.8 W/cm²</strong> (SATA).</li>
            <li><strong>Treatment Duration:</strong> 5 minutes with continuous circular motion of the soundhead at 2-4 cm/s using aqueous coupling gel.</li>
        </ul>
        """
    },
    {
        "id": "sn28",
        "topic": "Clinical Scenario / Short Case",
        "title": "Case 3: A patient with chronic severe plaque psoriasis is referred for UV phototherapy. Explain the treatment protocol and precautions.",
        "icon": "🩹",
        "badge": "Clinical Case",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Pre-treatment:</strong> Determine the patient's Minimal Erythema Dose (MED) using a sleeve test on the forearm or abdomen.</li>
            <li><strong>Initial Dose:</strong> Start with an <strong>E1 dose (1.25 × MED)</strong>.</li>
            <li><strong>Progression:</strong> Increase the exposure time by <strong>25% each subsequent session</strong> to compensate for epidermal thickening and melanin tanning.</li>
            <li><strong>Precautions:</strong>
                <ul>
                    <li>Mandatory UV-protective goggles for patient and therapist.</li>
                    <li>Shield sensitive unexposed areas (face, genitalia).</li>
                    <li>Screen for photosensitizing medications (tetracyclines, thiazides).</li>
                </ul>
            </li>
        </ul>
        """
    },
    {
        "id": "sn29",
        "topic": "Clinical Scenario / Short Case",
        "title": "Case 4: A physical therapist is treating deep piriformis muscle spasm in an athlete. Compare Capacitive vs Inductive SWD for this case.",
        "icon": "🏃",
        "badge": "Clinical Case",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Recommendation:</strong> <strong>Inductive Shortwave Diathermy (Drum / Diplode)</strong> is the treatment of choice.</li>
            <li><strong>Reasoning:</strong>
                <ul>
                    <li>The piriformis is a deep muscular structure beneath the gluteus maximus and subcutaneous fat.</li>
                    <li>Inductive SWD uses time-varying magnetic fields that pass unimpeded through superficial fat and selectively generate circular <em>Eddy Currents</em> in deep, vascular, highly conductive muscle tissue.</li>
                    <li>Capacitive SWD would unnecessarily overheat the superficial adipose fat layer due to its high electrical resistance (P = I²R) before adequately heating the deep piriformis.</li>
                </ul>
            </li>
        </ul>
        """
    },
    {
        "id": "sn30",
        "topic": "Clinical Scenario / Short Case",
        "title": "Case 5: A patient with chronic low back pain receives TENS. Explain the neurophysiological mechanism of immediate pain relief.",
        "icon": "⚡",
        "badge": "Clinical Case",
        "answer_html": """
        <ul class="sn-list">
            <li><strong>Mechanism:</strong> Based on the <strong>Gate Control Theory (Melzack & Wall)</strong>.</li>
            <li>High-frequency conventional TENS selectively activates large-diameter, myelinated <strong>A-beta (Aβ) sensory nerve fibers</strong>.</li>
            <li>Aβ collateral branches enter the spinal cord dorsal horn and stimulate inhibitory interneurons in the <strong>Substantia Gelatinosa (Lamina II)</strong>.</li>
            <li>Activated SG interneurons release GABA/Enkephalin, exerting <strong>Presynaptic Inhibition</strong> on the presynaptic terminals of incoming <strong>A-delta and C nociceptive fibers</strong>.</li>
            <li>This blocks the release of Substance P and Glutamate, preventing Transmission projection cells (T-cells) from firing, thereby 'closing the spinal gate' and inhibiting pain perception in the brain.</li>
        </ul>
        """
    }
]
