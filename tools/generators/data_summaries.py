# -*- coding: utf-8 -*-

summary_tables = [
    {
        "title": "1. Comparison of Peripheral Nerve Fibers & Pain Transmission",
        "icon": "🧠",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Fiber Type</th>
                    <th>Diameter</th>
                    <th>Myelin</th>
                    <th>Velocity</th>
                    <th>Sensation / Function</th>
                    <th>Neurotransmitter</th>
                    <th>Spinal Laminae</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>A-beta (Aβ)</strong></td>
                    <td>6 - 14 μm</td>
                    <td>Heavy</td>
                    <td>30 - 70 m/s</td>
                    <td>Touch, Vibration, Pressure (Closes Pain Gate)</td>
                    <td>ACh / Glutamate</td>
                    <td>Laminae III - VI</td>
                </tr>
                <tr>
                    <td><strong>A-delta (Aδ)</strong></td>
                    <td>1 - 6 μm</td>
                    <td>Thin</td>
                    <td>4 - 30 m/s</td>
                    <td><strong>Fast / First Pain:</strong> Sharp, Pricking, Localized</td>
                    <td><strong>Glutamate</strong></td>
                    <td>Laminae I & V</td>
                </tr>
                <tr>
                    <td><strong>C-Fibers</strong></td>
                    <td>0.2 - 1.5 μm</td>
                    <td><strong>None</strong></td>
                    <td>0.5 - 2 m/s</td>
                    <td><strong>Slow / Second Pain:</strong> Dull, Burning, Aching</td>
                    <td><strong>Substance P</strong></td>
                    <td>Laminae II & III (SG)</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "2. Comparison of Therapeutic Ultrasound Frequencies (1 MHz vs 3 MHz)",
        "icon": "🔊",
        "html": """
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
                    <td>1,000,000 Hz</td>
                    <td>3,000,000 Hz</td>
                </tr>
                <tr>
                    <td><strong>Penetration Depth</strong></td>
                    <td><strong>Deep: 3 to 5 cm</strong></td>
                    <td><strong>Superficial: 1 to 2.5 cm</strong></td>
                </tr>
                <tr>
                    <td><strong>Absorption Rate</strong></td>
                    <td>Lower in superficial tissue, travels deep</td>
                    <td>3x faster in superficial tissues</td>
                </tr>
                <tr>
                    <td><strong>Clinical Targets</strong></td>
                    <td>Hip joint, deep quadriceps, piriformis, thick muscles</td>
                    <td>Epicondylitis, Achilles tendon, patellar tendon, wrist ligaments</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "3. Comparison of Shortwave Diathermy Methods (Capacitive vs Inductive)",
        "icon": "⚡",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Feature</th>
                    <th>Capacitive (Electric Field)</th>
                    <th>Inductive (Magnetic Field)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Primary Field</strong></td>
                    <td>High-frequency alternating Electric Field</td>
                    <td>Time-varying Magnetic Field (Eddy Currents)</td>
                </tr>
                <tr>
                    <td><strong>Tissue Heated Most</strong></td>
                    <td>High-resistance tissues (Subcutaneous fat, bone interfaces)</td>
                    <td>High-conductivity tissues (Deep muscle, blood, synovial fluid)</td>
                </tr>
                <tr>
                    <td><strong>Applicators</strong></td>
                    <td>Rigid Space Plates, flexible Rubber Pads</td>
                    <td>Monode Drum, Diplode, wrapped Cable</td>
                </tr>
                <tr>
                    <td><strong>Penetration Profile</strong></td>
                    <td>Superficial / Fat heating</td>
                    <td>Deep muscle heating (3 to 5 cm)</td>
                </tr>
                <tr>
                    <td><strong>Skin Spacing</strong></td>
                    <td>2 to 4 cm (or 2 cm towel with pads)</td>
                    <td>5 to 10 cm between cable turns</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "4. Comparison of Infra-Red Erythema vs Ultraviolet Erythema",
        "icon": "🔴",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Parameter</th>
                    <th>Infra-Red (IR) Erythema</th>
                    <th>Ultraviolet (UV) Erythema</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Latency / Onset</strong></td>
                    <td><strong>Immediate</strong> during exposure</td>
                    <td><strong>Delayed (6 to 8 hours)</strong></td>
                </tr>
                <tr>
                    <td><strong>Appearance</strong></td>
                    <td>Mottled, patchy, irregular redness</td>
                    <td>Uniform, homogenous, well-demarcated redness</td>
                </tr>
                <tr>
                    <td><strong>Duration</strong></td>
                    <td>Fades rapidly within 30 - 60 minutes</td>
                    <td>Lasts several days</td>
                </tr>
                <tr>
                    <td><strong>Mechanism</strong></td>
                    <td>Thermal vasodilation (axon reflex + local heat)</td>
                    <td>Photochemical release of Nitric Oxide & Prostaglandins</td>
                </tr>
                <tr>
                    <td><strong>Pigmentation</strong></td>
                    <td>None (unless Erythema Ab Igne in chronic exposure)</td>
                    <td>Produces prominent tanning and melanin synthesis</td>
                </tr>
                <tr>
                    <td><strong>Peeling / Desquamation</strong></td>
                    <td>No peeling</td>
                    <td>Prominent peeling (desquamation) in higher doses</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "5. Ultraviolet Erythema Dosage Classification (MED System)",
        "icon": "☀️",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Dose Level</th>
                    <th>Multiplier</th>
                    <th>Clinical Manifestation</th>
                    <th>Progression per Session</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>SED (Suberythemal)</strong></td>
                    <td>< 1.0 × MED</td>
                    <td>No visible redness, vitamin D stimulation</td>
                    <td>Standard</td>
                </tr>
                <tr>
                    <td><strong>MED / E1</strong></td>
                    <td><strong>1.25 × MED</strong></td>
                    <td>Faint pink redness in 6-8h, disappears in 24-48h, no peeling</td>
                    <td><strong>+25%</strong> of previous dose</td>
                </tr>
                <tr>
                    <td><strong>E2 (Second Degree)</strong></td>
                    <td><strong>2.5 × MED</strong></td>
                    <td>Definite red sunburn, mild tenderness, powdery desquamation</td>
                    <td><strong>+50%</strong> of previous dose</td>
                </tr>
                <tr>
                    <td><strong>E3 (Third Degree)</strong></td>
                    <td><strong>5.0 × MED</strong></td>
                    <td>Dark fiery red, severe edema, burning pain, peeling in sheets</td>
                    <td><strong>+75%</strong> of previous dose</td>
                </tr>
                <tr>
                    <td><strong>E4 (Fourth Degree)</strong></td>
                    <td><strong>10.0 × MED</strong></td>
                    <td>Blistering (bullae), destructive inflammation, small areas (< 25 cm²)</td>
                    <td>No routine progression</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "6. Shortwave Diathermy Dosage Classification (Schliephake)",
        "icon": "🌡️",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Grade</th>
                    <th>Heat Sensation</th>
                    <th>Clinical Stage / Indication</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Grade I (Sub-thermal)</strong></td>
                    <td>No sensation of heat</td>
                    <td>Acute inflammatory conditions (Pulsed SWD)</td>
                </tr>
                <tr>
                    <td><strong>Grade II (Mild / Low)</strong></td>
                    <td>Barely perceptible, faint warmth</td>
                    <td>Subacute injuries, resolving inflammation</td>
                </tr>
                <tr>
                    <td><strong>Grade III (Moderate)</strong></td>
                    <td>Distinct, comfortable, pleasant warmth</td>
                    <td>Chronic inflammation, muscle spasm</td>
                </tr>
                <tr>
                    <td><strong>Grade IV (Vigorous)</strong></td>
                    <td>Strong, intense heat just below pain threshold</td>
                    <td>Dense fibrotic contractures, joint stiffness</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "7. Summary of Physical Radiation Laws in Electrotherapy",
        "icon": "📜",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Law</th>
                    <th>Formula / Principle</th>
                    <th>Clinical Importance</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Inverse Square Law</strong></td>
                    <td><code>I ∝ 1 / d²</code></td>
                    <td>Doubling distance reduces intensity to 25%; halving distance quadruples intensity.</td>
                </tr>
                <tr>
                    <td><strong>Cosine (Lambert's) Law</strong></td>
                    <td><code>I = I₀ × cos θ</code></td>
                    <td>Maximum energy is absorbed at 90° (perpendicular); tilted angle reduces absorption.</td>
                </tr>
                <tr>
                    <td><strong>Grotthus-Draper Law</strong></td>
                    <td>Absorbed Energy = Effect</td>
                    <td>Only absorbed energy causes biological changes; reflected/transmitted waves have no effect.</td>
                </tr>
                <tr>
                    <td><strong>Bunsen-Roscoe Law</strong></td>
                    <td><code>Intensity × Time = Constant</code></td>
                    <td>Total photochemical dose determines biological response.</td>
                </tr>
                <tr>
                    <td><strong>Arndt-Schultz Principle</strong></td>
                    <td>Stimulus-Response Law</td>
                    <td>Weak stimuli excite, moderate favor, strong inhibit, excessive destroy tissue.</td>
                </tr>
            </tbody>
        </table>
        """
    },
    {
        "title": "8. Nerve Action Potential Phases & Ionic Mechanisms",
        "icon": "⚡",
        "html": """
        <table class="compare-table">
            <thead>
                <tr>
                    <th>Phase</th>
                    <th>Membrane Potential</th>
                    <th>Ionic Movement / Channel State</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Resting State</strong></td>
                    <td>-70 mV</td>
                    <td>Na+/K+ ATPase pump active (3 Na+ out, 2 K+ in), high resting K+ leak.</td>
                </tr>
                <tr>
                    <td><strong>Threshold</strong></td>
                    <td>-55 mV</td>
                    <td>Opening of initial voltage-gated Na+ channels.</td>
                </tr>
                <tr>
                    <td><strong>Depolarization</strong></td>
                    <td>-55 mV → +30 mV</td>
                    <td>Rapid <strong>Na+ influx</strong> through open voltage-gated Na+ channels.</td>
                </tr>
                <tr>
                    <td><strong>Repolarization</strong></td>
                    <td>+30 mV → -70 mV</td>
                    <td>Na+ channels inactivate/close; voltage-gated <strong>K+ channels open (K+ efflux)</strong>.</td>
                </tr>
                <tr>
                    <td><strong>Hyperpolarization</strong></td>
                    <td>-90 mV</td>
                    <td>Slow closure of K+ channels (ensures refractory period & unidirectional signal).</td>
                </tr>
                <tr>
                    <td><strong>Restoration</strong></td>
                    <td>-70 mV</td>
                    <td>Na+/K+ pump restores resting ion distribution.</td>
                </tr>
            </tbody>
        </table>
        """
    }
]

flashcards_list = [
    {"q": "Wave equation in electrotherapy?", "a": "c = f × λ (Speed of light = Frequency × Wavelength = 3 × 10⁸ m/s)."},
    {"q": "Quantum energy equation?", "a": "E = h × f (Energy is directly proportional to frequency and inversely to wavelength)."},
    {"q": "Inverse Square Law formula & clinical rule?", "a": "I ∝ 1/d². If distance is doubled, intensity drops to 1/4 (25%). If distance is halved, intensity quadruples (4x)."},
    {"q": "Cosine Law (Lambert's Law) rule?", "a": "Maximum absorption occurs when radiation strikes skin at 90° (perpendicular)."},
    {"q": "Grotthus-Draper Law?", "a": "Only radiation that is absorbed by tissues can produce physical or chemical effects."},
    {"q": "Wavelength range of Infra-Red Radiation?", "a": "760 nm to 15,000 nm (divided into IR-A: 760-1400nm, IR-B: 1400-3000nm, IR-C: 3000-15000nm)."},
    {"q": "Penetration depth of Near IR (IR-A)?", "a": "1 to 3 mm (reaches dermis capillary network)."},
    {"q": "Characteristics of IR Erythema?", "a": "Immediate onset, mottled/patchy, lasts 30-60 minutes, no immediate tanning."},
    {"q": "What is Erythema Ab Igne?", "a": "Permanent brownish mottled skin pigmentation caused by chronic repeated long-term exposure to Infra-Red radiation."},
    {"q": "Standard distance for non-luminous IR lamp?", "a": "45 to 50 cm (and 60 to 75 cm for luminous lamps)."},
    {"q": "Wavelength range of UV-B?", "a": "280 nm to 315 nm (sunburn spectrum, stimulates Vitamin D synthesis)."},
    {"q": "Wavelength range of UV-C?", "a": "100 nm to 280 nm (peak bactericidal efficacy at 260-280 nm)."},
    {"q": "Kromayer lamp cooling & use?", "a": "Water-cooled quartz lamp; can be applied in direct contact with skin and mucous membranes."},
    {"q": "Why is UV erythema delayed (6-8 hours)?", "a": "Due to gradual photochemical release and diffusion of Nitric Oxide and prostaglandins."},
    {"q": "Vitamin D precursor in skin?", "a": "7-dehydrocholesterol (converted by UVB to Vitamin D3)."},
    {"q": "What is MED in UV therapy?", "a": "Minimal Erythema Dose: smallest dose causing faint erythema in 6-8h, disappearing in 24h without peeling."},
    {"q": "Multipliers for UV doses E1, E2, E3, E4?", "a": "E1 = 1.25x MED, E2 = 2.5x MED, E3 = 5x MED, E4 = 10x MED."},
    {"q": "What is Photokeratitis?", "a": "Acute corneal/conjunctival inflammation ('arc eye') with 6-24h latency; prevented by wearing UV goggles."},
    {"q": "Piezoelectric effect in Ultrasound?", "a": "Reverse piezoelectric effect: alternating electrical voltage across PZT crystal causes mechanical acoustic vibrations."},
    {"q": "1 MHz vs 3 MHz Ultrasound depth?", "a": "1 MHz = Deep (3-5 cm); 3 MHz = Superficial (1-2.5 cm)."},
    {"q": "Safe BNR value in Ultrasound?", "a": "Between 2:1 and 6:1 (Beam Non-uniformity Ratio; > 6:1 causes dangerous hot spots)."},
    {"q": "What causes Standing Waves in Ultrasound?", "a": "Reflection of sound waves at acoustic interfaces (bone periosteum); prevented by constantly moving soundhead at 2-4 cm/s."},
    {"q": "Standard Shortwave Diathermy frequency & wavelength?", "a": "27.12 MHz and Wavelength λ = 11.06 meters."},
    {"q": "Capacitive vs Inductive SWD heating targets?", "a": "Capacitive heats high-resistance fat & bone interfaces; Inductive heats high-conductivity deep muscle & blood via Eddy currents."},
    {"q": "Absolute contraindications for SWD?", "a": "Metallic implants/pins, Cardiac pacemakers, Impaired sensation, Hemorrhage, Malignancy, Pregnancy."},
    {"q": "IASP Pain definition?", "a": "An unpleasant sensory and emotional experience associated with, or resembling that associated with, actual or potential tissue damage."},
    {"q": "A-delta vs C fiber pain sensation & speed?", "a": "A-delta: Fast sharp pain (4-30 m/s, Glutamate). C-fiber: Slow dull burning pain (0.5-2 m/s, Substance P)."},
    {"q": "Gate Control Theory mechanism (Melzack & Wall)?", "a": "Stimulating large A-beta fibers activates inhibitory interneurons in Substantia Gelatinosa (Lamina II), closing the gate to A-delta/C pain input."},
    {"q": "Origin of Descending Pain Inhibitory Pathway?", "a": "Periaqueductal Gray (PAG) in midbrain → projects to Nucleus Raphe Magnus (NRM) in medulla → activates Enkephalin release in spinal cord."},
    {"q": "Nerve Action Potential ionic phases?", "a": "Resting: -70 mV → Threshold: -55 mV → Depolarization: +30 mV (Na+ influx) → Repolarization: (K+ efflux) → Hyperpolarization: -90 mV."}
]
