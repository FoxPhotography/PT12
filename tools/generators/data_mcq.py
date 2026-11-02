# -*- coding: utf-8 -*-

mcq_topics = [
    {
        "id": "em_spectrum",
        "title": "Electromagnetic Spectrum & Physical Radiation Laws",
        "icon": "🌈",
        "color": "ic-blue",
        "questions": [
            {
                "q": "The fundamental equation relating the velocity of light (c), frequency (f), and wavelength (λ) is:",
                "options": [
                    "c = f / λ",
                    "c = f × λ",
                    "λ = c × f",
                    "f = c × λ"
                ],
                "correct": 1,
                "note": "معادلة انتشار الموجات الكهرومغناطيسية: c = f × λ (حيث c سرعة الضوء = 3 × 10⁸ م/ث)."
            },
            {
                "q": "According to Planck's Quantum Theory, the energy of a photon (E) is directly proportional to:",
                "options": [
                    "Wavelength (λ)",
                    "Frequency (f)",
                    "Distance squared",
                    "Velocity squared"
                ],
                "correct": 1,
                "note": "قانون بلانك: E = h × f. الطاقة تتناسب طردياً مع التردد وعكسياً مع الطول الموجي (كلما زاد التردد وقصر الطول الموجي زادت طاقة الفوتون)."
            },
            {
                "q": "Which of the following represents the correct order of electromagnetic radiation from longest wavelength to shortest wavelength?",
                "options": [
                    "Gamma rays → X-rays → UV → Visible → IR → Radio",
                    "Radio waves → Shortwave → IR → Visible → UV → X-rays → Gamma rays",
                    "UV → Visible → IR → Microwaves → Radio waves",
                    "Visible → UV → IR → Shortwave → Gamma rays"
                ],
                "correct": 1,
                "note": "الترتيب من الأطول موجة (الأقل تردداً) إلى الأقصر موجة: Radio → Shortwave → Microwaves → Infrared → Visible Light → Ultraviolet → X-rays → Gamma rays."
            },
            {
                "q": "The law stating that 'Only radiation that is absorbed by tissues can produce physical or chemical effects' is:",
                "options": [
                    "Inverse Square Law",
                    "Cosine Law (Lambert's Law)",
                    "Grotthus-Draper Law",
                    "Bunsen-Roscoe Law"
                ],
                "correct": 2,
                "note": "قانون جروثس-درابر (Grotthus-Draper Law): الإشعاع الممتص فقط هو الذي يحدث تأثيراً علاجياً أو كيميائياً، بينما المنعكس أو النافذ لا يؤثر."
            },
            {
                "q": "According to the Inverse Square Law, if the distance between an Infra-Red lamp and the patient is doubled (from 50 cm to 100 cm), the intensity of radiation received by the skin becomes:",
                "options": [
                    "Half (1/2)",
                    "One-quarter (1/4)",
                    "Double (2x)",
                    "One-eighth (1/8)"
                ],
                "correct": 1,
                "note": "قانون التربيع العكسي (I ∝ 1/d²): مضاعفة المسافة لمرتين تقلل شدة الإشعاع إلى الربع (25%)."
            },
            {
                "q": "If the distance between a radiant lamp and the target skin is reduced by half (from 60 cm to 30 cm), the radiation intensity received will:",
                "options": [
                    "Double (2x)",
                    "Quadruple (4x)",
                    "Remain unchanged",
                    "Reduce to half"
                ],
                "correct": 1,
                "note": "تقليل المسافة للنصف يؤدي إلى زيادة شدة الإشعاع بمقدار 4 أضعاف (400%)."
            },
            {
                "q": "According to the Cosine Law (Lambert's Law), maximum absorption and radiant energy transfer occur when the radiant beam strikes the skin at an angle of:",
                "options": [
                    "30 degrees",
                    "45 degrees",
                    "60 degrees",
                    "90 degrees (Right angle / Perpendicular)"
                ],
                "correct": 3,
                "note": "قانون جيب التمام (Cosine Law): أقصى شدة وامتصاص يحدث عندما تسقط الأشعة بزاوية قائمة 90° عمودية تماماً على الجلد (cos 0° = 1 بالنسبة للعمودي)."
            },
            {
                "q": "The Bunsen-Roscoe Law of Reciprocity states that:",
                "options": [
                    "Intensity is inversely proportional to the square of distance",
                    "The biological effect is determined by total energy (Intensity × Time = Constant)",
                    "Small stimuli promote life processes",
                    "Only absorbed energy produces physiological changes"
                ],
                "correct": 1,
                "note": "قانون بونزن-روسكو (Bunsen-Roscoe Law): حاصل ضرب الشدة في زمن التعرض يعطي نفس التأثير البيولوجي (Intensity × Time = Constant)."
            },
            {
                "q": "The Arndt-Schultz Principle states that:",
                "options": [
                    "Weak stimuli excite physiological activity, moderate favor it, strong inhibit it, and very strong abolish/destroy it",
                    "All radiation travels at the speed of light in vacuum",
                    "Energy can neither be created nor destroyed",
                    "Absorption is greatest at 45 degrees"
                ],
                "correct": 0,
                "note": "مبدأ أرندت-شولتز (Arndt-Schultz Principle): المنبهات الضعيفة تحفز النشاط الفسيولوجي، والمتوسطة تدعمه، والقوية تثبطه، والمفرطة تدمره."
            },
            {
                "q": "Visible light spectrum spans approximately which wavelength range?",
                "options": [
                    "100 nm to 280 nm",
                    "280 nm to 400 nm",
                    "400 nm to 760 nm",
                    "760 nm to 15,000 nm"
                ],
                "correct": 2,
                "note": "الضوء المرئي يمتد من 400 نانومتر (البنفسجي) إلى 760 نانومتر (الأحمر)."
            },
            {
                "q": "Which part of the electromagnetic spectrum is immediately adjacent to the long wavelength end of visible red light?",
                "options": [
                    "Ultraviolet-A",
                    "Infra-Red Radiation",
                    "X-rays",
                    "Microwaves"
                ],
                "correct": 1,
                "note": "الأشعة تحت الحمراء (Infra-Red) تقع مباشرة بعد الضوء الأحمر المرئي (فوق 760 نانومتر)."
            },
            {
                "q": "As the frequency of an electromagnetic wave increases, its wavelength:",
                "options": [
                    "Increases proportionally",
                    "Decreases proportionally",
                    "Remains constant",
                    "Doubles"
                ],
                "correct": 1,
                "note": "العلاقة بين التردد والطول الموجي عكسية دائماً لأن حاصل ضربهما يساوي سرعة الضوء الثابتة (c = f × λ)."
            },
            {
                "q": "Which of the following electromagnetic radiations has the highest photon energy?",
                "options": [
                    "Infra-Red rays",
                    "Shortwave diathermy",
                    "Ultraviolet rays",
                    "Radio waves"
                ],
                "correct": 2,
                "note": "الأشعة فوق البنفسجية (UV) لها أقصر طول موجي وأعلى تردد بين الخيارات، وبالتالي أعلى طاقة فوتونات (E = hf)."
            },
            {
                "q": "In physical therapy, electromagnetic modalities that produce thermal effects include:",
                "options": [
                    "Infra-Red (IRR) and Shortwave Diathermy (SWD)",
                    "Ultraviolet-C only",
                    "Low-level Laser only",
                    "Cold packs only"
                ],
                "correct": 0,
                "note": "الوسائل الكهرومغناطيسية الحرارية تشمل الأشعة تحت الحمراء (IRR) والموجات القصيرة (SWD)."
            },
            {
                "q": "What happens to the radiant intensity received by a patient if an IR lamp is tilted from 90° to 60° relative to the skin surface?",
                "options": [
                    "Increases",
                    "Decreases according to the cosine of the angle",
                    "Remains exactly the same",
                    "Quadruples"
                ],
                "correct": 1,
                "note": "أي ميلان عن الزاوية العمودية 90° يقلل شدة الإشعاع الممتص طبقاً لقانون جيب التمام (Cosine Law)."
            },
            {
                "q": "All electromagnetic waves travel in a vacuum with a constant speed equal to:",
                "options": [
                    "3 × 10⁶ m/s",
                    "3 × 10⁸ m/s (300,000 km/s)",
                    "1.5 × 10⁸ m/s",
                    "330 m/s"
                ],
                "correct": 1,
                "note": "سرعة الموجات الكهرومغناطيسية في الفراغ = 3 × 10⁸ م/ث (سرعة الضوء)."
            },
            {
                "q": "Which law explains why applying an ice pack on a cold area does not cause chemical excitation unless energy is absorbed?",
                "options": [
                    "Grotthus-Draper Law",
                    "Inverse Square Law",
                    "Cosine Law",
                    "Ohm's Law"
                ],
                "correct": 0,
                "note": "قانون جروثس-درابر يؤكد أن التأثير البيولوجي لا يحدث إلا بامتصاص الطاقة."
            },
            {
                "q": "Which radiation band has a wavelength range of 760 nm to 15,000 nm?",
                "options": [
                    "Ultraviolet",
                    "Infra-Red",
                    "Microwave",
                    "X-ray"
                ],
                "correct": 1,
                "note": "الأشعة تحت الحمراء تمتد أطوالها الموجية من 760 نانومتر حتى 15,000 نانومتر (أو 15 ميكرومتر)."
            }
        ]
    },
    {
        "id": "irr",
        "title": "Infra-Red Radiation (IRR)",
        "icon": "🔴",
        "color": "ic-red",
        "questions": [
            {
                "q": "Infra-Red Radiation (IRR) is classified into three bands (A, B, C). IR-A (Near IR) has a wavelength range of:",
                "options": [
                    "760 nm to 1400 nm",
                    "1400 nm to 3000 nm",
                    "3000 nm to 15,000 nm",
                    "100 nm to 280 nm"
                ],
                "correct": 0,
                "note": "IR-A (Near IR) يمتد من 760 إلى 1400 نانومتر وهو الأكثر اختراقاً للجلد (يصل حتى 1-3 ملم)."
            },
            {
                "q": "Luminous Infra-Red generators emit radiation consisting of:",
                "options": [
                    "100% Far Infra-Red only",
                    "70% Near IR (IR-A) + 5% Visible light + 25% Far IR",
                    "Ultraviolet-B and UV-C",
                    "Microwaves and Radio waves"
                ],
                "correct": 1,
                "note": "المولدات المضيئة (Luminous) تحتوي على مصباح تنجستن/كربون باعث للضوء المرئي مع 70% IR-A قصير الموجة و 25% IR بعيد."
            },
            {
                "q": "Non-luminous Infra-Red generators:",
                "options": [
                    "Require no warm-up time",
                    "Emit 100% Far Infra-Red (IR-B and IR-C) and require 5-15 minutes to heat up",
                    "Penetrate deeper than luminous generators (up to 10 mm)",
                    "Emit visible blue light"
                ],
                "correct": 1,
                "note": "المولدات غير المضيئة (Non-luminous) مصنوعة من عنصر خزفي/مقاومة سلكية، وتنتج فقط IR-B و IR-C وتحتاج من 5 إلى 15 دقيقة للتسخين المسبق."
            },
            {
                "q": "The depth of penetration of Near Infra-Red radiation (IR-A) into human skin is approximately:",
                "options": [
                    "0.1 mm (stratum corneum only)",
                    "1 to 3 mm (dermis and superficial capillary network)",
                    "3 to 5 cm (deep muscle and joint)",
                    "10 cm (bone)"
                ],
                "correct": 1,
                "note": "عمق اختراق الأشعة تحت الحمراء القريبة (IR-A) يتراوح بين 1 إلى 3 ملم في طبقة الأدمة والأوعية الشعرية."
            },
            {
                "q": "Which physiological mechanism explains the pain relief produced by Infra-Red Radiation?",
                "options": [
                    "Sedative effect on sensory nerve endings and counter-irritation closing the pain gate",
                    "Destruction of nociceptor nerve fibers",
                    "Release of Substance P and Bradykinin",
                    "Inhibition of motor unit recruitment"
                ],
                "correct": 0,
                "note": "تسكين الألم بالحرارة السطحية (IRR) يحدث عبر تأثير مهدئ للنهايات العصبية الحسية وتفعيل نظرية بوابة الألم (Counter-irritation)."
            },
            {
                "q": "Erythema produced by Infra-Red radiation is characterized by being:",
                "options": [
                    "Delayed by 6-8 hours and leading to deep tanning",
                    "Immediate, mottled (patchy), lasting 30-60 minutes, without direct pigmentation",
                    "Accompanied by blistering and peeling sheets",
                    "Permanent after a single treatment session"
                ],
                "correct": 1,
                "note": "حمامى الأشعة تحت الحمراء تظهر فوراً (Immediate)، وتكون غير منتظمة/مبقعة (Mottled)، وتزول خلال 30-60 دقيقة ولا تؤدي لتسمير فوري."
            },
            {
                "q": "Long-term, chronic, repeated exposure to Infra-Red radiation can result in a permanent brownish mottled skin condition called:",
                "options": [
                    "Photokeratitis",
                    "Erythema Ab Igne",
                    "Vitiligo",
                    "Psoriasis"
                ],
                "correct": 1,
                "note": "Erythema Ab Igne (حمامي النار): تصبغ بني شبكي دائم ينتج عن التعرض المزمن المتكرر للأشعة تحت الحمراء بسبب تكسر كرات الدم الحمراء وترسب الهيموسيديرين."
            },
            {
                "q": "What is the recommended standard distance for positioning a non-luminous Infra-Red lamp from the patient's skin?",
                "options": [
                    "10 to 15 cm",
                    "45 to 50 cm",
                    "100 to 150 cm",
                    "Direct contact with skin"
                ],
                "correct": 1,
                "note": "المسافة القياسية للمولدات غير المضيئة 45-50 سم، وللمولدات المضيئة الكبيرة 60-75 سم."
            },
            {
                "q": "What is the standard treatment duration for Infra-Red therapy in chronic musculoskeletal conditions?",
                "options": [
                    "2 to 5 minutes",
                    "20 to 30 minutes",
                    "60 to 90 minutes",
                    "10 seconds"
                ],
                "correct": 1,
                "note": "مدة جلسة الأشعة تحت الحمراء للحالات المزمنة هي 20-30 دقيقة (وللحالات الحادة حرارة خفيفة 10-15 دقيقة)."
            },
            {
                "q": "Before applying Infra-Red radiation to any patient, which mandatory test must be performed?",
                "options": [
                    "Hot and cold thermal sensation test",
                    "Blood pressure measurement only",
                    "Deep tendon reflex test",
                    "Audiometry test"
                ],
                "correct": 0,
                "note": "اختبار الإحساس بالحرارة والبرودة (Hot/Cold Sensation Test) إجباري لتجنب حرق المريض في حال غياب الإحساس الحراري."
            },
            {
                "q": "Which of the following is an ABSOLUTE contraindication for Infra-Red Radiation therapy?",
                "options": [
                    "Chronic osteoarthritis of knee",
                    "Impaired skin thermal sensation and acute hemorrhage",
                    "Chronic muscle spasm in upper trapezius",
                    "Subacute low back pain"
                ],
                "correct": 1,
                "note": "فقدان الإحساس الحراري والنزيف الحاد والأورام الخبيثة موانع مطلقة للعلاج بالأشعة تحت الحمراء."
            },
            {
                "q": "Why must the patient's eyes be protected with goggles or covered during facial Infra-Red treatment?",
                "options": [
                    "To prevent dry eye syndrome only",
                    "To prevent corneal drying and long-term risk of infrared-induced cataracts",
                    "Because IR causes instant blindness",
                    "To improve melatonin production"
                ],
                "correct": 1,
                "note": "حماية العين ضرورية لمنع جفاف القرنية ولتجنب خطر تكون المياه البيضاء (Infra-Red Induced Cataract)."
            },
            {
                "q": "The local metabolic rate of tissues heated by Infra-Red radiation increases by approximately what percentage for each 1°C rise in temperature (Van't Hoff's Q10 rule)?",
                "options": [
                    "1%",
                    "10% to 13%",
                    "50%",
                    "100%"
                ],
                "correct": 1,
                "note": "قاعدة فانت هوف (Q10 rule): يزداد معدل الأيض الخلوي بنسبة 10-13% لكل ارتفاع بمقدار 1 درجة مئوية."
            },
            {
                "q": "In which condition is Infra-Red radiation NOT recommended?",
                "options": [
                    "Acute severe inflammation and acute joint swelling within the first 24 hours",
                    "Chronic lumbago",
                    "Post-immobilization joint stiffness",
                    "Muscle spasm before manual therapy"
                ],
                "correct": 0,
                "note": "الالتهابات الحادة في أول 24-48 ساعة يمنع فيها الحرارة منعاً باتاً لأنها تزيد الوذمة والتورم والالتهاب (نستخدم كمادات باردة)."
            },
            {
                "q": "How does Infra-Red radiation promote muscle relaxation?",
                "options": [
                    "By increasing gamma motor neuron discharge",
                    "By decreasing muscle spindle sensitivity and increasing local blood flow to clear metabolic waste",
                    "By causing direct muscle denervation",
                    "By freezing calcium channels"
                ],
                "correct": 1,
                "note": "الحرارة تقلل من استثارة المغازل العضلية (Muscle Spindles) وتزيد تدفق الدم فتزيل نواتج الأيض المسببة للتقلص."
            },
            {
                "q": "What should the therapist instruct the patient to feel during an Infra-Red treatment session?",
                "options": [
                    "Intense burning heat to speed recovery",
                    "A comfortable, pleasant, soothing warmth",
                    "Mild numbness and tingling",
                    "No sensation at all"
                ],
                "correct": 1,
                "note": "يجب أن يشعر المريض بدفء مريح ولطيف (Comfortable pleasant warmth) وليس بحرارة حارقة."
            },
            {
                "q": "Which type of generator is preferred when immediate treatment without pre-heating time is desired?",
                "options": [
                    "Non-luminous generator",
                    "Luminous generator",
                    "Alpine sunlamp",
                    "Kromayer lamp"
                ],
                "correct": 1,
                "note": "المولدات المضيئة (Luminous) تبدأ بإشعاع الحرارة فور تشغيلها دون الحاجة لوقت تسخين مسبق."
            },
            {
                "q": "Superficial vasodilation under Infra-Red exposure is mediated primarily by:",
                "options": [
                    "Direct axon reflex and release of chemical vasodilators (histamine-like substances)",
                    "Sympathetic vasoconstriction",
                    "Decreased blood pressure in the aorta only",
                    "Activation of alpha-1 adrenergic receptors"
                ],
                "correct": 0,
                "note": "توسع الأوعية السطحية بالحرارة يتم عبر منعكس المحور العصبي وإفراز مواد شبيهة بالهيستامين والبراديكينين."
            },
            {
                "q": "What is the primary heat transfer mechanism of an Infra-Red lamp to the skin?",
                "options": [
                    "Conduction",
                    "Convection",
                    "Radiation (Electromagnetic waves)",
                    "Conversion"
                ],
                "correct": 2,
                "note": "انتقال الحرارة من لمبة الـ IR إلى جسم المريض يتم عن طريق الإشعاع الكهرومغناطيسي (Radiation)."
            },
            {
                "q": "If a patient reports that the heat from the IR lamp is becoming uncomfortably hot during the session, the therapist should:",
                "options": [
                    "Tell the patient to endure it",
                    "Increase the distance of the lamp from the patient or reduce output",
                    "Turn off the clinic lights",
                    "Apply ice while keeping the lamp on"
                ],
                "correct": 1,
                "note": "إذا شعر المريض بحرارة زائدة يجب زيادة مسافة اللمبة فوراً طبقاً لقانون التربيع العكسي أو تقليل الشدة لتجنب الحروق."
            }
        ]
    },
    {
        "id": "uvr",
        "title": "Ultraviolet Therapy (UVR)",
        "icon": "🟣",
        "color": "ic-purple",
        "questions": [
            {
                "q": "Ultraviolet Radiation (UVR) spectrum is divided into UV-A, UV-B, and UV-C. The wavelength band of UV-B is:",
                "options": [
                    "315 nm to 400 nm",
                    "280 nm to 315 nm",
                    "100 nm to 280 nm",
                    "760 nm to 1400 nm"
                ],
                "correct": 1,
                "note": "نطاق UV-B يمتد من 280 إلى 315 نانومتر وهو المسؤول عن حروق الشمس وتصنيع فيتامين D وتسمير الجلد."
            },
            {
                "q": "Which Ultraviolet band is known as 'Germicidal' or 'Bactericidal' radiation and has a peak efficacy at 260-280 nm?",
                "options": [
                    "UV-A",
                    "UV-B",
                    "UV-C",
                    "Visible violet"
                ],
                "correct": 2,
                "note": "نطاق UV-C (من 100 إلى 280 نانومتر) هو الأكثر قضاءً على البكتيريا ويستخدم لتعقيم الجروح والقرح الملوثة."
            },
            {
                "q": "The Kromayer lamp is a specialized Ultraviolet generator that is:",
                "options": [
                    "Air-cooled and used only at a distance of 36 inches",
                    "Water-cooled, high-pressure mercury arc lamp that can be used in direct contact with skin or mucous membranes",
                    "A low-intensity incandescent bulb",
                    "An infrared heater"
                ],
                "correct": 1,
                "note": "مصباح كروماير (Kromayer Lamp) يحتوي على غلاف تبريد مائي يمنع الحرارة ويسمح بالتلامس المباشر مع الجلد والتجاويف المخاطية كالفم والجيوب."
            },
            {
                "q": "Why does Ultraviolet erythema have a delayed onset (latency of 6 to 8 hours) compared to immediate Infra-Red erythema?",
                "options": [
                    "Because UV rays travel slower than IR rays",
                    "Because UV causes gradual photochemical release and diffusion of vasodilators like Nitric Oxide and prostaglandins in the epidermis",
                    "Because UV activates sympathetic vasoconstrictors first",
                    "Because UV only heats the bone"
                ],
                "correct": 1,
                "note": "حمامى الـ UV تتأخر (6-8 ساعات) لأنها ناتجة عن تفاعل كيميائي ضوئي وتراكم بطيء للموسع الوعائي (Nitric Oxide) والبروستاغلاندينات."
            },
            {
                "q": "Ultraviolet-B stimulates the synthesis of Vitamin D3 in the skin by converting which precursor sterol?",
                "options": [
                    "Ergosterol to Vitamin A",
                    "7-dehydrocholesterol to cholecalciferol (Vitamin D3)",
                    "Bilirubin to biliverdin",
                    "Tyrosine to melanin"
                ],
                "correct": 1,
                "note": "الأشعة فوق البنفسجية B تحول مركب 7-dehydrocholesterol في دهون الجلد إلى كوليكالسيفيرول (فيتامين D3)."
            },
            {
                "q": "What clinical advice should be given to patients regarding showering after sun or UV exposure for Vitamin D production?",
                "options": [
                    "Scrub vigorously with soap immediately",
                    "Avoid washing the exposed skin with hot soapy water immediately because Vitamin D3 formed on the skin surface takes hours to absorb into the blood",
                    "Apply ice immediately",
                    "Take a sauna bath"
                ],
                "correct": 1,
                "note": "فيتامين D3 يتكون كمركب دهني على سطح الجلد ويحتاج ساعات ليمتصه تيار الدم، لذا ينصح بعدم الاستحمام العنيف بالصابون الساخن فوراً."
            },
            {
                "q": "How does Ultraviolet radiation exert its immunosuppressive therapeutic effect in skin conditions like psoriasis?",
                "options": [
                    "By destroying Langerhans cells in the epidermis and stimulating suppressor T cells",
                    "By destroying red blood cells",
                    "By inhibiting thyroid hormone",
                    "By increasing histamine production"
                ],
                "correct": 0,
                "note": "الأشعة فوق البنفسجية تثبط خلايا لانجرهانز (Langerhans cells) المناعية في البشرة وتحفز خلايا T المثبطة لمنع الهجوم المناعي الذاتي على الجلد."
            },
            {
                "q": "Langerhans cells in the skin are characterized by containing specialized organelles called:",
                "options": [
                    "Birbeck granules",
                    "Nissl granules",
                    "Zymogen granules",
                    "Melanosomes only"
                ],
                "correct": 0,
                "note": "خلايا لانجرهانز (خلايا مناعية عارضة للمستضد في البشرة) تحتوي على حبيبات بيربيك (Birbeck granules)."
            },
            {
                "q": "The Minimal Erythema Dose (MED) is defined as:",
                "options": [
                    "The dose that causes no visible erythema",
                    "The smallest dose of UVR that produces a just-visible, faint erythema 6-8 hours after exposure, disappearing within 24 hours",
                    "The dose that causes severe blistering and ulceration",
                    "A dose applied for 60 minutes continuously"
                ],
                "correct": 1,
                "note": "الجرعة الحمامية الصغرى (MED): أقل جرعة تحدث احمراراً خفيفاً بعد 6-8 ساعات ويختفي تماماً خلال 24 ساعة بدون تقشير."
            },
            {
                "q": "What is the dosage multiplier for a Second Degree Erythema (E2) dose in UV therapy?",
                "options": [
                    "1.25 × MED",
                    "2.5 × MED",
                    "5 × MED",
                    "10 × MED"
                ],
                "correct": 1,
                "note": "مضاعف الجرعة لـ E2 هو 2.5 × MED (بينما E1 = 1.25x، E3 = 5x، E4 = 10x)."
            },
            {
                "q": "A Fourth Degree Erythema (E4) dose is characterized by:",
                "options": [
                    "Faint pink redness disappearing in 24 hours",
                    "Severe blistering (bullae), exudation, and destructive inflammation, used only for small areas (< 25 cm²)",
                    "Suberythemal effect without redness",
                    "No peeling"
                ],
                "correct": 1,
                "note": "جرعة الدرجة الرابعة (E4 = 10x MED) تسبب فقاعات وحروق شديدة وتستخدم فقط لمساحات موضعية صغيرة جداً أقل من 25 سم²."
            },
            {
                "q": "Due to progressive thickening of the stratum corneum and tanning during a course of UV therapy, how should subsequent E1 doses be progressed?",
                "options": [
                    "Kept exactly the same throughout",
                    "Increased by 25% of the previous dose at each session",
                    "Decreased by 50%",
                    "Multiplied by 10 every day"
                ],
                "correct": 1,
                "note": "تدرج الجرعات: جرعة E1 تزيد بمقدار 25% في كل جلسة للتغلب على زيادة سمك طبقة الكيراتين والتسمير."
            },
            {
                "q": "Photokeratitis ('arc eye' / snow blindness) is an acute inflammation of the cornea and conjunctiva caused by unprotected UV exposure. Its symptoms typically appear after a latency period of:",
                "options": [
                    "1 minute",
                    "6 to 24 hours",
                    "3 weeks",
                    "2 months"
                ],
                "correct": 1,
                "note": "التهاب القرنية الضوئي (Photokeratitis) يظهر بعد 6 إلى 24 ساعة من التعرض للـ UV ويسبب حساسية للضوء، إحساس بجسم غريب، ودموع غزيرة."
            },
            {
                "q": "Which dermatological condition is a prime indication for UV-B phototherapy (such as Goeckerman regimen or PUVA)?",
                "options": [
                    "Psoriasis",
                    "Acute Eczema",
                    "Systemic Lupus Erythematosus (SLE)",
                    "Herpes Simplex"
                ],
                "correct": 0,
                "note": "الصدفية (Psoriasis) من أشهر دواعي استخدام الـ UV-B والـ PUVA لتقليل الانقسام الزائد لخلايا الكيراتين وتثبيط المناعة."
            },
            {
                "q": "Which of the following is an ABSOLUTE contraindication for Ultraviolet Radiation therapy?",
                "options": [
                    "Chronic non-healing pressure ulcer",
                    "Systemic Lupus Erythematosus (SLE) and acute generalized eczema",
                    "Acne vulgaris",
                    "Vitiligo"
                ],
                "correct": 1,
                "note": "مرض الذئبة الحمراء (SLE) والإكزيما الحادة والهربس من الموانع المطلقة للـ UV لأنها تزيد الحالة اشتعالاً."
            },
            {
                "q": "The process of darkening of existing skin melanin within 10 minutes of UV-A exposure is due to:",
                "options": [
                    "New melanin synthesis by ribosomes",
                    "Photo-oxidation (darkening) of pre-existing melanin",
                    "Destruction of red blood cells",
                    "Hyperplasia of Langerhans cells"
                ],
                "correct": 1,
                "note": "التسمير الفوري (Immediate Tanning) تحت UV-A يحدث نتيجة الأكسدة الضوئية للميلانين الموجود مسبقاً في الخلايا."
            },
            {
                "q": "Why is protective eyewear (opaque UV goggles) mandatory for BOTH patient and therapist during UV therapy?",
                "options": [
                    "To prevent thermal burn only",
                    "To prevent photokeratitis, conjunctivitis, and lens cataract damage",
                    "Because UV light impairs night vision permanently in 5 seconds",
                    "To avoid distraction"
                ],
                "correct": 1,
                "note": "النظارات الواقية إجبارية للمريض والمعالج لمنع التهاب ملتحمة وقرنية العين وخطر المياه البيضاء."
            },
            {
                "q": "Which medications act as 'Photosensitizers', greatly increasing skin sensitivity and burn risk under UVR?",
                "options": [
                    "Tetracycline antibiotics, Sulphonamides, and Psoralens",
                    "Vitamin C supplements",
                    "Paracetamol",
                    "Saline nasal spray"
                ],
                "correct": 0,
                "note": "أدوية التتراسيكلين، السلفوناميد، والبسورايلين تعتبر محفزات للحساسية الضوئية (Photosensitizers) وتزيد خطر الحروق بشدة."
            },
            {
                "q": "UV-C radiation at 254 nm kills bacteria primarily by:",
                "options": [
                    "Direct thermal coagulation of bacterial cytoplasm",
                    "Disrupting bacterial DNA/RNA and preventing replication (thymine dimer formation)",
                    "Freezing bacterial cell walls",
                    "Dehydrating surrounding water"
                ],
                "correct": 1,
                "note": "أشعة UV-C تقضي على البكتيريا عبر تدمير شفرة الـ DNA/RNA وتكوين روابط الثايمين المعطلة لانقسام الخلية."
            },
            {
                "q": "What is the primary skin layer responsible for melanin production?",
                "options": [
                    "Stratum corneum",
                    "Stratum basale (deepest layer of epidermis)",
                    "Subcutaneous fat",
                    "Reticular dermis"
                ],
                "correct": 1,
                "note": "الخلايا الصبغية (Melanocytes) توجد في الطبقة القاعدية (Stratum basale) في قاع البشرة."
            },
            {
                "q": "In treating an infected pressure sore (ulcer) with UV-C, the surrounding healthy skin must be:",
                "options": [
                    "Exposed to maximum intensity",
                    "Draped and shielded with UV-opaque cloth or zinc oxide paste to prevent healthy tissue burning",
                    "Scrubbed with alcohol",
                    "Heated with Shortwave simultaneously"
                ],
                "correct": 1,
                "note": "عند علاج القرح بـ UV-C يجب تغطية الجلد السليم المحيط بستائر واقية أو مرهم أكسيد الزنك لمنع حرقه."
            },
            {
                "q": "An Alpine sunlamp is typically standardized at what distance from the patient?",
                "options": [
                    "5 to 10 cm",
                    "24 to 40 inches (approx. 60 to 100 cm)",
                    "Direct contact",
                    "3 meters"
                ],
                "correct": 1,
                "note": "المسافة القياسية لمصباح Alpine الهوائي تتراوح بين 24 إلى 40 بوصة (حوالي 60-100 سم)."
            },
            {
                "q": "What effect does chronic, excessive lifetime exposure to UV radiation have on the skin?",
                "options": [
                    "Skin elasticity increases",
                    "Premature photo-aging (wrinkles, loss of elasticity) and increased risk of skin cancers (Basal cell, Squamous cell, Melanoma)",
                    "Prevents all forms of skin cancer",
                    "Eliminates hair growth permanently"
                ],
                "correct": 1,
                "note": "التعرض المفرط طويل الأمد للـ UV يسبب شيخوخة الجلد المبكرة ويزيد خطر سرطانات الجلد (Basal cell, Squamous cell, Malignant melanoma)."
            },
            {
                "q": "Desquamation (peeling of skin) after UV exposure is caused by:",
                "options": [
                    "Increased turnover of keratinocytes shedding superficial stratum corneum cells in sheets",
                    "Fat necrosis in hypodermis",
                    "Nerve axon degeneration",
                    "Decreased blood supply"
                ],
                "correct": 0,
                "note": "تقشير الجلد (Desquamation) ينتج عن تسارع انقسام الخلايا الكيراتينية وتساقط الطبقة القرنية السطحية على شكل قشور."
            }
        ]
    },
    {
        "id": "ultrasound",
        "title": "Therapeutic Ultrasound (US)",
        "icon": "🔊",
        "color": "ic-cyan",
        "questions": [
            {
                "q": "Therapeutic Ultrasound produces acoustic waves through which fundamental physical principle?",
                "options": [
                    "Electromagnetic induction",
                    "Reverse (Converse) Piezoelectric Effect",
                    "Thermoelectric Seebeck effect",
                    "Photoelectric effect"
                ],
                "correct": 1,
                "note": "الموجات فوق الصوتية تنتج عبر ظاهرة الكهروانضغاطية العكسية (Reverse Piezoelectric Effect) حيث يتمدد وينكمش الكريستال عند تعرضه لتيار متناوب عالي التردد."
            },
            {
                "q": "The synthetic crystal material most commonly used in modern therapeutic ultrasound transducers is:",
                "options": [
                    "Lead Zirconate Titanate (PZT)",
                    "Pure Silicon",
                    "Copper wire",
                    "Tungsten filament"
                ],
                "correct": 0,
                "note": "المادة الأكثر استخداماً في رؤوس السونار هي PZT (Lead Zirconate Titanate) لكفاءتها العالية ومقاومتها."
            },
            {
                "q": "Which ultrasound frequency is selected for treating DEEP structures (3 to 5 cm depth, such as the hip joint or quadriceps)?",
                "options": [
                    "3 MHz",
                    "1 MHz",
                    "10 MHz",
                    "20 kHz"
                ],
                "correct": 1,
                "note": "تردد 1 MHz أقل تشتتاً وامتصاصاً سطحياً، وبالتالي ينفذ إلى الأنسجة العميقة (3-5 سم)."
            },
            {
                "q": "Which ultrasound frequency is selected for treating SUPERFICIAL structures (1 to 2.5 cm depth, such as lateral epicondylitis or patellar tendon)?",
                "options": [
                    "1 MHz",
                    "3 MHz",
                    "0.5 MHz",
                    "27.12 MHz"
                ],
                "correct": 1,
                "note": "تردد 3 MHz يمتص في الأنسجة السطحية بمعدل أسرع 3 مرات مقارنة بـ 1 MHz، لذا يناسب الإصابات السطحية (1-2.5 سم)."
            },
            {
                "q": "Why is a coupling medium (such as aqueous acoustic gel) mandatory during therapeutic ultrasound application?",
                "options": [
                    "To cool the patient's skin only",
                    "Because the acoustic impedance mismatch between air and skin causes 99.9% of sound waves to be reflected",
                    "To disinfect the transducer head",
                    "To conduct electrical current into the muscle"
                ],
                "correct": 1,
                "note": "الجل الصوتي إجباري لأن وجود أي هواء بين رأس السونار والجلد يعكس 99.9% من الموجات بسبب اختلاف المعاوقة الصوتية."
            },
            {
                "q": "Acoustic Impedance (Z) of a biological tissue is defined mathematically as:",
                "options": [
                    "Z = Frequency × Wavelength",
                    "Z = Tissue Density (ρ) × Velocity of Sound in that tissue (c)",
                    "Z = Voltage / Current",
                    "Z = Force × Distance"
                ],
                "correct": 1,
                "note": "المعاوقة الصوتية Z = ρ × c (الكثافة النسيجية × سرعة الصوت في النسيج)."
            },
            {
                "q": "Among the following biological tissues, ultrasound absorption and heating are HIGHEST in tissues with high protein/collagen content, ranked as:",
                "options": [
                    "Blood > Fat > Muscle",
                    "Bone > Cartilage > Tendon > Ligament > Muscle > Fat > Blood",
                    "Fat > Muscle > Bone",
                    "Skin > Fat > Nerve"
                ],
                "correct": 1,
                "note": "امتصاص الموجات فوق الصوتية يتناسب طردياً مع محتوى الكولاجين: العظم > الغضاريف > الأوتار > الأربطة > العضلات > الدهون > الدم."
            },
            {
                "q": "What is the primary danger of holding an ultrasound transducer stationary (still) during continuous ultrasound treatment?",
                "options": [
                    "Transducer will freeze",
                    "Formation of Standing Waves causing periosteal bone overheating ('hot spots') and endothelial damage",
                    "Immediate battery depletion",
                    "Total loss of coupling gel"
                ],
                "correct": 1,
                "note": "تثبيت رأس السونار يؤدي لتداخل الموجات الساقطة والمنعكسة وتكون موجات موقوفة (Standing Waves) تسبب ألماً عظمياً حاداً وحرق السمحاق."
            },
            {
                "q": "The Effective Radiating Area (ERA) of an ultrasound transducer is:",
                "options": [
                    "The total surface area of the metal housing",
                    "The actual surface area of the crystal face that transmits ultrasonic energy (always slightly smaller than the geometric soundhead face)",
                    "The depth of penetration in cm",
                    "The frequency divided by intensity"
                ],
                "correct": 1,
                "note": "المساحة الإشعاعية الفعالة (ERA): المساحة الحقيقية للكريستال الباعثة للموجات، وتكون دائماً أصغر قليلاً من الوجه الخارجي للرأس."
            },
            {
                "q": "The Beam Non-uniformity Ratio (BNR) is the ratio of spatial peak intensity to spatial average intensity. A clinically safe and acceptable BNR value is:",
                "options": [
                    "Between 2:1 and 6:1 (ideally close to 1:1)",
                    "50:1",
                    "100:1",
                    "0:1"
                ],
                "correct": 0,
                "note": "نسبة عدم انتظام الحزمة (BNR) الآمنة سريرياً هي أقل من 6:1 (والمثالية 1:1). إذا تجاوزت 6:1 تسبب نقاط حرارية خطيرة."
            },
            {
                "q": "In acute musculoskeletal injuries, which ultrasound mode and duty cycle should be selected to achieve non-thermal healing effects?",
                "options": [
                    "Continuous mode (100% duty cycle)",
                    "Pulsed mode with a 20% duty cycle (1:4 mark-to-space ratio)",
                    "High-intensity continuous SWD",
                    "Hot packs"
                ],
                "correct": 1,
                "note": "في الإصابات الحادة نستخدم النمط النبضي (Pulsed 20%) لتشتيت الحرارة والحصول على التأثيرات الميكانيكية وإصلاح الأنسجة بدون تسخين."
            },
            {
                "q": "The phenomenon where gas-filled microbubbles oscillate in size in response to acoustic pressure waves without imploding is called:",
                "options": [
                    "Transient cavitation",
                    "Stable cavitation",
                    "Phonophoresis",
                    "Standing waves"
                ],
                "correct": 1,
                "note": "التجويف المستقر (Stable Cavitation): اهتزاز الفقاعات الدقيقة دون انفجار، وهو المسؤول عن زيادة نفاذية الغشاء الخلوي والتئام الأنسجة."
            },
            {
                "q": "Transient (unstable) cavitation in ultrasound therapy is considered hazardous because it leads to:",
                "options": [
                    "Violent bubble collapse producing extreme local temperatures, shockwaves, and tissue destruction",
                    "Immediate muscle freezing",
                    "Loss of skin sensation permanently",
                    "Formation of bone spurs"
                ],
                "correct": 0,
                "note": "التجويف العابر/غير المستقر (Transient Cavitation) يحدث عند شدات عالية جداً ويؤدي لانفجار الفقاعات وتدمير الخلايا."
            },
            {
                "q": "Acoustic Microstreaming produced by ultrasound refers to:",
                "options": [
                    "Unidirectional movement of fluid along cell membranes, altering cell membrane permeability to Calcium and Sodium ions",
                    "Flow of electric current through nerve fibers",
                    "Radio wave transmission across skin",
                    "Movement of lymph in thoracic duct"
                ],
                "correct": 0,
                "note": "التدفق الصوتي الدقيق (Microstreaming): حركة موضعية للسوائل حول الأغشية الخلوية تزيد نفاذيتها لأيونات الكالسيوم وتحفز بناء البروتين."
            },
            {
                "q": "Phonophoresis (Sonophoresis) is defined as:",
                "options": [
                    "The use of ultrasound waves to drive topical medication molecules through the skin into target tissues",
                    "The measurement of sound frequency in hearing tests",
                    "Using ultrasound for body weight reduction",
                    "Electrical stimulation with direct current"
                ],
                "correct": 0,
                "note": "الفونوفوريسيس (Phonophoresis): استخدام الموجات فوق الصوتية لإدخال الأدوية الموضعية (مثل مضادات الالتهاب كالكورتيزون) عبر الجلد."
            },
            {
                "q": "When treating irregular, bony body parts (such as fingers, toes, or malleoli) where good transducer contact is difficult, which method is recommended?",
                "options": [
                    "Water Immersion Method (underwater technique with soundhead 1-2 cm away from skin)",
                    "Direct contact without any gel",
                    "Using dry towels",
                    "Holding the transducer 50 cm away in air"
                ],
                "correct": 0,
                "note": "طريقة الغمر بالماء (Water Immersion): وضع العضو في وعاء ماء غير معدني مع إمساك الرأس على بعد 1-2 سم من الجلد للمناطق غير المستوية."
            },
            {
                "q": "The recommended speed for moving the ultrasound soundhead across the skin is:",
                "options": [
                    "Held completely motionless",
                    "Slow, rhythmic circles or longitudinal strokes at approximately 2 to 4 cm/second",
                    "Extremely fast at 50 cm/second",
                    "Left on skin for 10 minutes without touching"
                ],
                "correct": 1,
                "note": "سرعة تحريك رأس السونار المثالية هي 2-4 سم/ثانية في دوائر متداخلة أو حركات طولية لضمان التوزيع المتساوي للطاقة."
            },
            {
                "q": "Which of the following conditions is an ABSOLUTE contraindication for therapeutic ultrasound?",
                "options": [
                    "Chronic shoulder supraspinatus tendinopathy",
                    "Application directly over pregnant uterus, cardiac pacemaker, eyes, or deep vein thrombosis (DVT)",
                    "Subacute ankle sprain",
                    "Plantar fasciitis"
                ],
                "correct": 1,
                "note": "تطبيق السونار فوق الرحم الحامل، منظم ضربات القلب، العين، أو الجلطات الوريدية العميقة (DVT) من الموانع المطلقة."
            },
            {
                "q": "Why is continuous high-intensity ultrasound contraindicated over open growth plates (epiphyses) in growing children?",
                "options": [
                    "It causes premature epiphyseal closure and bone growth retardation",
                    "It causes muscle hyper-flexibility",
                    "It turns bone into cartilage",
                    "It eliminates white blood cells"
                ],
                "correct": 0,
                "note": "السونار الحراري عالي الشدة فوق مراكز النمو (Epiphyses) للأطفال قد يؤدي لإغلاقها مبكراً وتوقف نمو العظام."
            },
            {
                "q": "Half-Value Depth (HVD) of ultrasound in tissue is defined as:",
                "options": [
                    "The depth at which 50% of the initial ultrasound beam intensity has been attenuated/absorbed",
                    "Half the diameter of the soundhead",
                    "The time needed to complete half the treatment",
                    "Half the frequency in MHz"
                ],
                "correct": 0,
                "note": "عمق نصف القيمة (Half-Value Depth): العمق الذي تنخفض عنده شدة حزمة الموجات فوق الصوتية بمقدار 50% بسبب الامتصاص والتوهين."
            },
            {
                "q": "If a patient experiences a deep, dull, aching pain during continuous ultrasound treatment over a joint, what is the most likely cause?",
                "options": [
                    "Normal beneficial therapeutic response",
                    "Periosteal overheating due to wave reflection and standing waves (hot spot)",
                    "Skin frostbite",
                    "Coupling gel allergy"
                ],
                "correct": 1,
                "note": "الألم العظمي العميق الحاد (Aching pain) يشير إلى ارتفاع حرارة السمحاق العظمي (Periosteal overheating) بسبب الانعكاس، ويجب تقليل الشدة فوراً."
            },
            {
                "q": "The total treatment area for an ultrasound session should generally NOT exceed:",
                "options": [
                    "2 to 3 times the ERA (Effective Radiating Area) of the soundhead",
                    "The entire lower limb in one go",
                    "10 times the soundhead size",
                    "500 cm²"
                ],
                "correct": 0,
                "note": "المساحة المعالجة في الجلسة الواحدة لا يجب أن تتجاوز 2-3 أضعاف مساحة الـ ERA لضمان وصول جرعة علاجية كافية."
            },
            {
                "q": "Which tissue has the lowest ultrasound attenuation/absorption coefficient and allows sound to pass through with minimal heating?",
                "options": [
                    "Cortical bone",
                    "Tendon",
                    "Blood and body fluids (water)",
                    "Articular cartilage"
                ],
                "correct": 2,
                "note": "السوائل والدم تحتوي على أقل معامل امتصاص وتسمح بمرور الموجات بأقل توليد للحرارة."
            },
            {
                "q": "The primary clinical indication for thermal continuous ultrasound (100% duty cycle, 1.0 - 2.0 W/cm²) is:",
                "options": [
                    "Acute ligament tear within 2 hours",
                    "Chronic joint contracture, deep scar tissue, and chronic muscle spasm to increase collagen extensibility",
                    "Acute open bleeding wound",
                    "Acute bacterial infection"
                ],
                "correct": 1,
                "note": "السونار الحراري المستمر يستخدم لزيادة مرونة ألياف الكولاجين في حالات تيبس المفاصل والندبات والتشنج العضلي المزمن."
            },
            {
                "q": "In ultrasound physics, Attenuation includes which of the following three processes?",
                "options": [
                    "Absorption, Reflection, and Refraction/Scattering",
                    "Conduction, Convection, Evaporation",
                    "Depolarization, Repolarization, Hyperpolarization",
                    "Transduction, Transmission, Modulation"
                ],
                "correct": 0,
                "note": "توهين الموجات (Attenuation) يشمل الامتصاص (Absorption) والانعكاس (Reflection) والانكسار/التشتت (Refraction/Scattering)."
            },
            {
                "q": "What is the relationship between ultrasound frequency and depth of penetration?",
                "options": [
                    "Direct relationship (Higher frequency penetrates deeper)",
                    "Inverse relationship (Higher frequency has higher absorption and penetrates shallower)",
                    "Frequency has no effect on depth",
                    "Linear exponential increase"
                ],
                "correct": 1,
                "note": "العلاقة عكسية: التردد الأعلى (3 MHz) يمتص بسرعة ويكون سطحي، والتردد الأقل (1 MHz) ينفذ أعمق."
            }
        ]
    },
    {
        "id": "swd",
        "title": "Shortwave Diathermy (SWD)",
        "icon": "⚡",
        "color": "ic-yellow",
        "questions": [
            {
                "q": "The standard internationally allocated operating frequency for Shortwave Diathermy (SWD) in physical therapy is:",
                "options": [
                    "1 MHz",
                    "27.12 MHz (Wavelength = 11.06 meters)",
                    "2450 MHz",
                    "100 kHz"
                ],
                "correct": 1,
                "note": "التردد القياسي الأكثر استخداماً للموجات القصيرة هو 27.12 ميجاهرتز (بطول موجي 11.06 متر)."
            },
            {
                "q": "In the Capacitive (Electric Field / Condenser) SWD method, energy concentrates and produces GREATEST heating in which type of tissue?",
                "options": [
                    "Deep vascular muscle tissue",
                    "Low-conductivity / high-resistance tissues such as subcutaneous adipose fat and bone-muscle interfaces",
                    "Blood vessels and sweat",
                    "Synovial fluid"
                ],
                "correct": 1,
                "note": "المجال السعوي (Capacitive) يمر عبر الأنسجة على التوالي فيولد أعلى حرارة في الأنسجة عالية المقاومة كالدهون السطحية والواجهات العظمية."
            },
            {
                "q": "In the Inductive (Magnetic Field / Inductothermy) SWD method, heat is generated primarily by:",
                "options": [
                    "Direct conduction of electrons",
                    "Time-varying magnetic fields inducing circular Eddy Currents in high-conductivity tissues (muscle and blood)",
                    "Friction of air molecules",
                    "UV photon absorption"
                ],
                "correct": 1,
                "note": "المجال الحثي (Inductive) يولد مجالاً مغناطيسياً ينشئ تيارات إيدي (Eddy Currents) في الأنسجة عالية الموصلية كالعضلات والدم."
            },
            {
                "q": "Why is the Inductive method preferred over the Capacitive method when treating deep muscle spasm in a patient with a moderate subcutaneous fat layer?",
                "options": [
                    "Because magnetic fields pass through superficial fat unimpeded without being shunted, targeting deep vascular muscle",
                    "Because inductive coils freeze the fat",
                    "Because capacitive plates have no electrical current",
                    "Because inductive coils work only on bones"
                ],
                "correct": 0,
                "note": "المجال المغناطيسي الحثي ينفذ عبر دهون الجلد دون أن تمتصه، ليتركز التسخين عميقاً في العضلات الغنية بالماء والأيونات."
            },
            {
                "q": "When using flexible Rubber Pad electrodes in Capacitive SWD, what is the minimum towel thickness required between the electrode and the skin to prevent burns?",
                "options": [
                    "0.5 mm",
                    "2 cm (approx. 4-6 layers of dry towel)",
                    "10 cm",
                    "No towel is needed"
                ],
                "correct": 1,
                "note": "يجب لف مخدات المطاط (Pads) في فوط جافة بسمك لا يقل عن 2 سم؛ السمك الأقل يسبب حروقاً والأكبر يقلل الجرعة."
            },
            {
                "q": "In Capacitive SWD, what happens if the spacing between the electrode and the skin is too small (closer to the skin)?",
                "options": [
                    "Deep heating is increased",
                    "Heating becomes superficial and concentrates intensely directly under the close electrode",
                    "No heat is produced",
                    "The machine shuts down automatically"
                ],
                "correct": 1,
                "note": "تقريب القطب من الجلد يجعل التسخين سطحياً جداً وتتركز خطوط المجال تحته مباشرة مسببة خطر الحرق."
            },
            {
                "q": "In Capacitive SWD, the 'Cross-fire' electrode technique is specially designed and recommended for treating:",
                "options": [
                    "The whole femur",
                    "Air-containing cavities and deep pelvic organs such as Sinuses and the Uterus",
                    "Superficial fingers",
                    "The Achilles tendon only"
                ],
                "correct": 1,
                "note": "تقنية Cross-fire (نصف الجلسة في اتجاه قطري والنصف الآخر في الاتجاه المعاكس) مثالية لتجاويف الجسم كالجيوب الأنفية والرحم."
            },
            {
                "q": "What electrode configuration has electrodes placed on OPPOSITE sides of a joint or limb to treat deeply placed structures?",
                "options": [
                    "Coplanar method",
                    "Contraplanar method",
                    "Longitudinal method",
                    "Monode method"
                ],
                "correct": 1,
                "note": "الوضع المتقابل (Contraplanar): وضع الأقطاب على جانبين متقابلين لعلاج الهياكل العميقة في المفاصل كالمفصل الركبي أو الفخذي."
            },
            {
                "q": "What electrode configuration has both electrodes placed on the SAME side of the body part to treat superficial structures (such as the lumbar spine)?",
                "options": [
                    "Contraplanar method",
                    "Coplanar method",
                    "Cross-fire method",
                    "Inductothermy"
                ],
                "correct": 1,
                "note": "الوضع المتوازي (Coplanar): وضع القطبين على نفس الجانب لعلاج الهياكل السطحية كعضلات الظهر."
            },
            {
                "q": "When wrapping an insulated SWD Cable around a patient's limb, what is the required spacing between adjacent turns of the coil?",
                "options": [
                    "Touching each other tightly",
                    "5 to 10 cm maintained by felt/rubber spacers",
                    "50 cm",
                    "1 meter"
                ],
                "correct": 1,
                "note": "عند لف كابل الموجات القصيرة يجب ترك مسافة 5-10 سم بين اللفات بواسطة فواصل مطاطية/لباد لمنع التماس ودارة القصر."
            },
            {
                "q": "Why is the presence of METALLIC implants, surgical pins, or internal pacemakers an ABSOLUTE contraindication for SWD?",
                "options": [
                    "Metal reflects all waves back into the machine",
                    "Metal has very low electrical impedance and concentrates electromagnetic lines, causing extreme local overheating and severe deep tissue burns",
                    "Metal causes the patient to become magnetized",
                    "Metal cools down the body"
                ],
                "correct": 1,
                "note": "المعادن توصل الكهرباء بسهولة وتجمع خطوط المجال حولها مسببة ارتفاعاً حرارياً هائلاً وحروقاً عميقة خطيرة، وتشوش على منظم ضربات القلب."
            },
            {
                "q": "Why must the patient's skin be thoroughly dried of SWEAT and covered with a dry towel before SWD application?",
                "options": [
                    "Sweat smells bad under heat",
                    "Sweat is a high-conductivity electrolyte solution that concentrates the electric field on the skin surface, creating dangerous 'hot spots' and scalding burns",
                    "Sweat prevents machine tuning",
                    "Sweat turns into ice"
                ],
                "correct": 1,
                "note": "العرق سائل موصل غني بالأملاح يجمع خطوط المجال مسبباً بقعاً حارقة (Hot spots) وسلقاً للجلد، لذا يجب تجفيف الجلد تماماً."
            },
            {
                "q": "According to Schliephake's dosage classification for SWD, a 'Grade II (Mild / Low thermal)' dose is characterized by:",
                "options": [
                    "No heat sensation at all",
                    "Barely perceptible, faint, gentle sensation of warmth (used for subacute conditions)",
                    "Strong, intense heat just below pain threshold",
                    "Burning pain"
                ],
                "correct": 1,
                "note": "الدرجة الثانية (Grade II - Mild): شعور خفيف بالكاد محسوس بالدفء، ويستخدم للحالات الحادة وتحت الحادة."
            },
            {
                "q": "According to Schliephake's classification, a 'Grade IV (Vigorous / Heavy thermal)' dose is used primarily for:",
                "options": [
                    "Acute traumatic sprains in first 24 hours",
                    "Chronic conditions requiring intense heating to soften thick fibrotic adhesions and joint contractures",
                    "Infant fever treatment",
                    "Facial nerve acute paralysis"
                ],
                "correct": 1,
                "note": "الدرجة الرابعة (Grade IV - Vigorous): حرارة قوية ومكثفة لتليين الالتصاقات الليفية المزمنة وتيبس المفاصل المزمن."
            },
            {
                "q": "What is meant by 'Tuning' or 'Resonance' in Shortwave Diathermy operation?",
                "options": [
                    "Adjusting the radio channel for music",
                    "Adjusting the patient circuit capacitance so its resonant frequency matches the generator's internal oscillating frequency, maximizing energy transfer",
                    "Setting the treatment timer to zero",
                    "Cooling down the vacuum tubes"
                ],
                "correct": 1,
                "note": "التوليف (Tuning/Resonance): ضبط دائرة المريض لتتوافق ترددياً مع دائرة المولد لتحقيق أقصى نقل للطاقة الكهرومغناطيسية."
            },
            {
                "q": "If one electrode is significantly SMALLER than the other in a capacitive setup, where will the heat concentrate?",
                "options": [
                    "Under the larger electrode",
                    "Under the smaller electrode (higher electric field density)",
                    "Equally between both",
                    "In the air between them"
                ],
                "correct": 1,
                "note": "القطب الأصغر حجماً يركز خطوط المجال وتكون كثافة الطاقة تحته أعلى بكثير، فيحدث التسخين الأكبر تحته."
            },
            {
                "q": "Pulsed Shortwave Diathermy (PSWD) is selected when the therapist desires:",
                "options": [
                    "Maximum deep tissue heating and heavy sweating",
                    "Non-thermal biological effects (cellular repair, edema reduction, and wound healing in acute/subacute stages)",
                    "Permanent muscle ablation",
                    "Direct bone fracture fixation"
                ],
                "correct": 1,
                "note": "الموجات القصيرة النبضية (PSWD) توفر تأثيرات غير حرارية تعزز شفاء الأنسجة وامتصاص الارتشاح في المراحل الحادة."
            },
            {
                "q": "Which of the following is an ABSOLUTE contraindication for Shortwave Diathermy?",
                "options": [
                    "Cardiac pacemaker (active implant)",
                    "Chronic osteoarthritis",
                    "Healed surgical scar without metal",
                    "Chronic neck pain"
                ],
                "correct": 0,
                "note": "منظم ضربات القلب (Cardiac Pacemaker) مانع مطلق، ويجب ألا يقترب حامله من جهاز الـ SWD العامل لمسافة أقل من 3-5 أمتار."
            },
            {
                "q": "Why is Shortwave Diathermy contraindicated over the abdomen or pelvis during pregnancy?",
                "options": [
                    "It causes morning sickness",
                    "RF electromagnetic fields and hyperthermia can cause severe teratogenic developmental defects or miscarriage in the fetus",
                    "It increases maternal appetite",
                    "It reduces fetal heart rate to zero immediately"
                ],
                "correct": 1,
                "note": "الحمل مانع مطلق لأن الحرارة العميقة والمجال الكهرومغناطيسي قد يسببان تشوهات خلقية للجنين أو إجهاضاً."
            },
            {
                "q": "What is the recommended treatment time for continuous Shortwave Diathermy in chronic conditions?",
                "options": [
                    "1 to 2 minutes",
                    "15 to 20 minutes (up to 30 minutes)",
                    "2 hours continuously",
                    "10 seconds"
                ],
                "correct": 1,
                "note": "مدة جلسة الـ SWD المستمرة للحالات المزمنة هي 15 إلى 20 دقيقة (وحتى 30 دقيقة كحد أقصى)."
            },
            {
                "q": "In inductive drum application, if the patient's subcutaneous fat layer is greater than 2 cm, what precaution is noted?",
                "options": [
                    "No precaution needed",
                    "Penetration to deeper muscle may be reduced and heat may accumulate in the fat layer",
                    "The machine explodes",
                    "Treatment time must be doubled"
                ],
                "correct": 1,
                "note": "إذا زادت سماكة الدهون عن 2 سم فإن نفاذ الحث المغناطيسي للعضلات يقل وقد تتراكم الحرارة سطحياً."
            },
            {
                "q": "When applying Capacitive SWD, the electrodes should be placed:",
                "options": [
                    "Parallel to the skin surface to maintain a uniform electric field",
                    "At a 45 degree tilt to skin",
                    "Directly touching bare skin without spacing",
                    "Submerged in water"
                ],
                "correct": 0,
                "note": "يجب وضع الأقطاب موازية لسطح الجلد لضمان توزيع منتظم لخطوط المجال وتجنب تركزها عند الحواف."
            },
            {
                "q": "Air in body cavities (like sinuses) offers high electrical resistance. In capacitive SWD, the electric field lines will:",
                "options": [
                    "Pass through the air easily",
                    "Deviate around the air cavity, heating the moist cavity walls/mucous membranes",
                    "Disappear completely",
                    "Create a lightning spark"
                ],
                "correct": 1,
                "note": "الهواء في التجاويف يقاوم الكهرباء، فتنحرف خطوط المجال لتمر وتسخن الجدران المخاطية الرطبة المحيطة بالتجويف."
            },
            {
                "q": "Which of the following clinical conditions benefits most from deep heating via Inductive Shortwave Diathermy?",
                "options": [
                    "Deep spasm and contracture of hamstring or quadriceps muscles",
                    "Acute bleeding hemarthrosis",
                    "Malignant bone tumor",
                    "Acute thrombophlebitis"
                ],
                "correct": 0,
                "note": "التقلصات والتيبس العضلي العميق في العضلات الكبيرة (كالفخذية والهامسترينج) هي المستفيد الأكبر من التسخين الحثي للـ SWD."
            }
        ]
    },
    {
        "id": "pain",
        "title": "Physiology of Pain in Physical Therapy",
        "icon": "🧠",
        "color": "ic-pink",
        "questions": [
            {
                "q": "According to the International Association for the Study of Pain (IASP), pain is defined as:",
                "options": [
                    "A purely mechanical motor reflex",
                    "An unpleasant sensory and emotional experience associated with, or resembling that associated with, actual or potential tissue damage",
                    "An increase in muscle tone only",
                    "A simple spinal cord twitch"
                ],
                "correct": 1,
                "note": "تعريف الألم (IASP): تجربة حسية وعاطفية غير سارة مرتبطة بتلف فعلي أو محتمل في الأنسجة."
            },
            {
                "q": "The process by which noxious thermal, mechanical, or chemical stimuli are converted into electrical action potentials at nociceptor endings is called:",
                "options": [
                    "Transmission",
                    "Transduction",
                    "Perception",
                    "Modulation"
                ],
                "correct": 1,
                "note": "التحويل (Transduction): تحويل المنبه المؤلم (ميكانيكي/حراري/كيميائي) إلى نبضات كهربائية في المستقبلات العصبية."
            },
            {
                "q": "Which peripheral nerve fibers transmit FAST, SHARP, well-localized, pricking pain at a conduction velocity of 4 to 30 m/s?",
                "options": [
                    "A-beta (Aβ) fibers",
                    "A-delta (Aδ) fibers (thinly myelinated)",
                    "C-fibers (unmyelinated)",
                    "Type B preganglionic fibers"
                ],
                "correct": 1,
                "note": "ألياف A-delta (Aδ): رفيعة الميالين، تنقل الألم الأولي السريع الحاد المحدد بدقة (Fast sharp pain) بسرعة 4-30 م/ث وناقلها هو الجلوتامات."
            },
            {
                "q": "Which peripheral nerve fibers transmit SLOW, DULL, aching, burning, poorly localized chronic pain at a slow velocity of 0.5 to 2 m/s?",
                "options": [
                    "A-alpha fibers",
                    "A-beta fibers",
                    "C-fibers (unmyelinated)",
                    "Ia spindle afferents"
                ],
                "correct": 2,
                "note": "ألياف C: عديمة الميالين ورفيعة، تنقل الألم البطيء الحارق المنتشر (Slow burning aching pain) بسرعة 0.5-2 م/ث وناقلها هو Substance P."
            },
            {
                "q": "The primary neurotransmitter released by A-delta fibers for fast synaptic transmission in the spinal dorsal horn is:",
                "options": [
                    "Glutamate",
                    "Substance P",
                    "Dopamine",
                    "Acetylcholine"
                ],
                "correct": 0,
                "note": "الناقل العصبي لألياف A-delta هو الجلوتامات (Glutamate) الذي يعمل سريعاً على مستقبلات AMPA/NMDA."
            },
            {
                "q": "The primary peptide neurotransmitter released by C-fibers associated with slow, persistent, chronic inflammatory pain is:",
                "options": [
                    "Substance P (and CGRP)",
                    "GABA",
                    "Glycine",
                    "Norepinephrine"
                ],
                "correct": 0,
                "note": "الناقل العصبي لألياف C هو مادة P (Substance P) المرتبطة بالألم البطيء والالتهابي المزمن."
            },
            {
                "q": "In the spinal cord dorsal horn, C-fibers synapse predominantly in which histological layer (Laminae)?",
                "options": [
                    "Laminae II and III (Substantia Gelatinosa of Rolando - SGR)",
                    "Lamina IX (Motor pool)",
                    "Lamina X (Central canal)",
                    "Ventral horn"
                ],
                "correct": 0,
                "note": "ألياف C تنتهي وتتشابك في الصفيحتين II و III في المادة الهلامية (Substantia Gelatinosa of Rolando)."
            },
            {
                "q": "The ascending tract responsible for transmitting discriminative fast pain, temperature, and crude touch to the thalamus is the:",
                "options": [
                    "Dorsal Column Pathway (Fasciculus gracilis/cuneatus)",
                    "Lateral Spinothalamic Tract (Neospinothalamic pathway)",
                    "Spinocerebellar tract",
                    "Corticospinal tract"
                ],
                "correct": 1,
                "note": "الحزمة الشوكية المهادية الجانبية (Lateral Spinothalamic Tract) هي المسار الصاعد الرئيسي لنقل إشارات الألم والحرارة."
            },
            {
                "q": "Which brain structure acts as the primary sensory relay station ('switchboard') for pain signals before reaching the cerebral cortex?",
                "options": [
                    "Cerebellum",
                    "Thalamus",
                    "Basal Ganglia",
                    "Pons"
                ],
                "correct": 1,
                "note": "المهاد (Thalamus): محطة الترحيل والتحويل الحسية المركزية لجميع إشارات الألم المتجهة للقشرة المخية."
            },
            {
                "q": "Conscious perception, precise spatial localization, and intensity discrimination of pain take place in the:",
                "options": [
                    "Primary Somatosensory Cortex (Postcentral gyrus, Broadman areas 3, 1, 2)",
                    "Occipital visual cortex",
                    "Spinal ventral horn",
                    "Adrenal medulla"
                ],
                "correct": 0,
                "note": "الإدراك الواعي وتحديد موقع وشدة الألم يتم في القشرة الحسية الجسدية الأولية (Postcentral gyrus)."
            },
            {
                "q": "The emotional, affective, and unpleasant suffering aspects of chronic pain are processed in the:",
                "options": [
                    "Limbic System (Cingulate cortex, Insula, Amygdala)",
                    "Dorsal column nuclei",
                    "Posterior horn of gray matter",
                    "Optic chiasm"
                ],
                "correct": 0,
                "note": "الجوانب العاطفية والنفسية والمعاناة في الألم المزمن تتم معالجتها في الجهاز الحوفي (Limbic System) والتلفيف الحزامي."
            },
            {
                "q": "The Gate Control Theory of Pain was proposed in 1965 by:",
                "options": [
                    "Ronald Melzack and Patrick Wall",
                    "Ivan Pavlov",
                    "Albert Einstein",
                    "Sigmund Freud"
                ],
                "correct": 0,
                "note": "نظرية بوابة الألم وضعها العالمان رونالد ميلزاك وباتريك وول (Ronald Melzack & Patrick Wall) عام 1965."
            },
            {
                "q": "According to the Gate Control Theory, how does rubbing, massage, or TENS relieve pain?",
                "options": [
                    "By stimulating large-diameter A-beta (Aβ) fibers which activate inhibitory interneurons in Substantia Gelatinosa, closing the gate to A-delta and C nociceptive input",
                    "By cutting the spinal cord",
                    "By increasing Substance P release",
                    "By cooling the thalamus"
                ],
                "correct": 0,
                "note": "تحفيز ألياف A-beta الكبيرة (عبر اللمس والتدليك والتيارات) ينشط خلايا المادة الهلامية المثبطة، مما يغلق البوابة أمام إشارات ألياف الألم A-delta و C."
            },
            {
                "q": "In the spinal dorsal horn, Enkephalin released by inhibitory interneurons causes:",
                "options": [
                    "Presynaptic inhibition of C-fiber terminals, blocking Calcium influx and preventing Substance P release",
                    "Direct excitation of T-cells",
                    "Vasoconstriction of femoral artery",
                    "Destruction of dorsal root ganglion"
                ],
                "correct": 0,
                "note": "الإنكيفالين يسبب تثبيطاً قبل مشبكي (Presynaptic Inhibition) لنهايات ألياف C، فيمنع دخول الكالسيوم ويمنع إفراز مادة Substance P."
            },
            {
                "q": "Which major brainstem region is the primary origin of the Descending Pain Modulatory (Inhibitory) System?",
                "options": [
                    "Periaqueductal Gray (PAG) matter of the midbrain",
                    "Corpus callosum",
                    "Anterior pituitary",
                    "Optic nerve"
                ],
                "correct": 0,
                "note": "المادة الرمادية حول القناة (Periaqueductal Gray - PAG) في الدماغ المتوسط هي منشأ المسار الهابط لتثبيط الألم."
            },
            {
                "q": "The Periaqueductal Gray (PAG) projects descending fibers to which medullary nucleus to inhibit spinal pain transmission?",
                "options": [
                    "Nucleus Raphe Magnus (NRM)",
                    "Substantia Nigra",
                    "Red Nucleus",
                    "Dentate nucleus"
                ],
                "correct": 0,
                "note": "الـ PAG ترسل إشارات إلى نواة الرفاء الكبرى (Nucleus Raphe Magnus - NRM) في النخاع المستطيل التي تفرز السيروتونين والنورأدرينالين نحو الحبل الشوكي."
            },
            {
                "q": "Which of the following endogenous opioid peptides is synthesized in the pituitary gland and hypothalamus and provides potent systemic analgesia?",
                "options": [
                    "Beta-endorphin (β-endorphin)",
                    "Histamine",
                    "Bradykinin",
                    "Prostaglandin E2"
                ],
                "correct": 0,
                "note": "بيتا-إندورفين (β-endorphin) ببتيد أفيوني داخلي يفرز من الغدة النخامية والمهاد لتسكين الألم العام في الجسم."
            },
            {
                "q": "Which cutaneous mechanoreceptor responds primarily to skin stretch and sustained tension?",
                "options": [
                    "Ruffini endings",
                    "Meissner corpuscles",
                    "Pacinian corpuscles",
                    "Free nerve endings"
                ],
                "correct": 0,
                "note": "نهايات روفيني (Ruffini endings) تستجيب لشد وتوتر الجلد والحرارة المستمرة."
            },
            {
                "q": "Which cutaneous mechanoreceptor responds primarily to high-frequency vibration and deep transient pressure?",
                "options": [
                    "Pacinian corpuscles",
                    "Merkel discs",
                    "Krause end bulbs",
                    "Nociceptors"
                ],
                "correct": 0,
                "note": "جسيمات باتشيني (Pacinian corpuscles) تستجيب للاهتزاز عالي التردد والضغط العميق."
            },
            {
                "q": "Dorsal column pathway damage results in:",
                "options": [
                    "Sensory ataxia and loss of two-point discrimination, conscious proprioception, and vibration",
                    "Loss of pain and temperature sensation only",
                    "Complete motor paralysis of face",
                    "Loss of hearing"
                ],
                "correct": 0,
                "note": "تلف الأعمدة الخلفية يسبب ترنحاً حسياً (Sensory Ataxia) وفقدان التمييز بين نقطتين وإحساس الاهتزاز والوضع المفصلي الواعي."
            },
            {
                "q": "Spinocerebellar tract damage leads to:",
                "options": [
                    "Cerebellar ataxia and clumsy, uncoordinated movements",
                    "Loss of vision",
                    "Loss of taste sensation",
                    "Hypertension"
                ],
                "correct": 0,
                "note": "تلف المسار الشوكي المخيخي (Spinocerebellar) يؤدي لترنح مخيخي (Cerebellar Ataxia) وحركات غير متناسقة."
            },
            {
                "q": "Pain that arises from internal organs but is perceived in a distant somatic body surface sharing the same embryonic dermatome is called:",
                "options": [
                    "Referred Pain (e.g. cardiac pain referred to left arm and jaw)",
                    "Phantom limb pain",
                    "Psychogenic pain",
                    "Neuroma"
                ],
                "correct": 0,
                "note": "الألم الرجيع (Referred Pain): ألم ينشأ في الأحشاء الداخلية ويشعر به المريض في منطقة جلدية تشترك معها في نفس القطاع العصبي الجنيني."
            },
            {
                "q": "The chemical algogenic substances released during tissue injury that directly sensitize or activate nociceptors include:",
                "options": [
                    "Bradykinin, Prostaglandins, Histamine, Potassium ions (K+), and H+ ions",
                    "Insulin and Glucagon",
                    "Hemoglobin and Myoglobin",
                    "Melanin and Keratin"
                ],
                "correct": 0,
                "note": "المواد الكيميائية المولدة للألم عند تلف الأنسجة تشمل البراديكينين، البروستاغلاندينات، الهيستامين، وأيونات البوتاسيوم والهيدروجين."
            },
            {
                "q": "What is the primary difference in pain sensation between A-delta and C fibers?",
                "options": [
                    "A-delta gives immediate sharp localizable pain; C gives delayed dull aching persistent burning pain",
                    "A-delta gives burning pain; C gives cold sensation",
                    "A-delta has no conduction; C conducts at 100 m/s",
                    "There is no difference"
                ],
                "correct": 0,
                "note": "ألياف A-delta مسؤولة عن الألم الحاد الأولي السريع، بينما ألياف C مسؤولة عن الألم البطيء الحارق والمزمن الثاني."
            }
        ]
    },
    {
        "id": "tissue_histology",
        "title": "Organization of Body Tissue & Histology / Nerve Bio-electricity",
        "icon": "🧬",
        "color": "ic-green",
        "questions": [
            {
                "q": "The human body is composed of four primary tissue types, which are:",
                "options": [
                    "Epithelial, Connective, Muscle, and Nervous tissues",
                    "Bone, Cartilage, Fat, and Skin only",
                    "Blood, Lymph, Serum, and Plasma",
                    "Epidermis, Dermis, Hypodermis, and Hair"
                ],
                "correct": 0,
                "note": "الأنسجة الأربعة الأساسية في جسم الإنسان: الطلائي (Epithelial)، الضام (Connective)، العضلي (Muscle)، والعصبي (Nervous)."
            },
            {
                "q": "Which of the following is a key characteristic of Epithelial tissue?",
                "options": [
                    "Highly vascular with abundant intercellular substance",
                    "Avascular, highly cellular with minimal extracellular matrix, possessing apical and basal polarity, resting on a basement membrane",
                    "Consists only of non-living calcium crystals",
                    "Contains only multinucleated skeletal muscle cells"
                ],
                "correct": 1,
                "note": "النسيج الطلائي عديم الأوعية الدموية (Avascular)، خلاياه متراصة، له قطبية (سطح قمي وقاعدي)، ويستقر على غشاء قاعدي."
            },
            {
                "q": "Connective tissue proper is distinguished by having:",
                "options": [
                    "Cells widely separated by abundant extracellular matrix containing protein fibers (collagen, elastic, reticular) and ground substance",
                    "No extracellular matrix at all",
                    "Only one cell type",
                    "Direct synaptic connections"
                ],
                "correct": 0,
                "note": "النسيج الضام يتميز بوجود مادة بين خلوية وفيرة (Extracellular Matrix) تفصل الخلايا وتحتوي على ألياف الكولاجين والإيلاستين."
            },
            {
                "q": "Which layer of the human skin represents the primary electrical resistance (highest impedance) barrier to electrotherapy currents?",
                "options": [
                    "Stratum corneum of the epidermis (dead keratinized layer)",
                    "Papillary dermis",
                    "Subcutaneous fat",
                    "Reticular dermis"
                ],
                "correct": 0,
                "note": "الطبقة القرنية السطحية (Stratum Corneum) في البشرة المكونة من خلايا ميتة جافة تمثل العائق الأكبر والمقاومة الكهربائية الأعلى لمرور التيارات."
            },
            {
                "q": "The Dermis layer of skin consists of two sub-layers, which are:",
                "options": [
                    "Stratum basale and Stratum spinosum",
                    "Papillary layer (superficial loose areolar with capillaries) and Reticular layer (deep dense irregular connective tissue)",
                    "Adipose and Bone layers",
                    "Keratin and Melanin layers"
                ],
                "correct": 1,
                "note": "الأدمة (Dermis) تنقسم إلى طبقة حليمية سطحية (Papillary) غنية بالشعيرات، وطبقة شبكية عميقة (Reticular) غنية بألياف الكولاجين."
            },
            {
                "q": "According to the Erlanger-Gasser classification, Type A nerve fibers are characterized by:",
                "options": [
                    "Being the thickest (1.5 - 20 μm), myelinated, with the fastest conduction velocity (4 - 120 m/s)",
                    "Being unmyelinated with 0.5 m/s velocity",
                    "Being postganglionic sympathetic fibers",
                    "Having no axon"
                ],
                "correct": 0,
                "note": "ألياف Type A هي الأكثر سمكاً (1.5-20 ميكرون) ومغلفة بالميالين وتتميز بأعلى سرعة توصيل عصبي (4-120 م/ث)."
            },
            {
                "q": "Type B nerve fibers are:",
                "options": [
                    "Thick motor fibers to skeletal muscle",
                    "Medium-sized (1.5 - 3.5 μm), myelinated, preganglionic autonomic efferents with conduction velocity of 3 - 15 m/s",
                    "Unmyelinated pain fibers",
                    "Receptors in the retina"
                ],
                "correct": 1,
                "note": "ألياف Type B متوسطة الحجم (1.5-3.5 ميكرون) وميالينية، وتمثل الألياف اللاإرادية قبل العقدية وتوصل بسرعة 3-15 م/ث."
            },
            {
                "q": "Type C nerve fibers are:",
                "options": [
                    "The smallest (0.1 - 2 μm), unmyelinated, slowest conducting (0.5 - 4 m/s), including postganglionic autonomic efferents and slow pain afferents",
                    "Somatic alpha motor fibers",
                    "Fast touch fibers",
                    "Muscle spindle primary afferents"
                ],
                "correct": 0,
                "note": "ألياف Type C هي الأصغر والأنحف وغير مغلفة بالميالين وتوصل ببطء (0.5-4 م/ث) وتشمل ألياف الألم البطيء والودية بعد العقدية."
            },
            {
                "q": "What is the normal Resting Membrane Potential (RMP) of a typical human nerve cell?",
                "options": [
                    "0 mV",
                    "-70 mV (inside negative relative to outside)",
                    "+30 mV",
                    "-55 mV"
                ],
                "correct": 1,
                "note": "جهد الراحة الغشائي الطبيعي للخلية العصبية هو -70 ملي فولت (الداخل سالب مقارنة بالخارج)."
            },
            {
                "q": "What is the critical 'Threshold Potential' that must be reached to trigger an Action Potential in a neuron?",
                "options": [
                    "-90 mV",
                    "-55 mV",
                    "+30 mV",
                    "0 mV"
                ],
                "correct": 1,
                "note": "عتبة الإثارة (Threshold Potential) هي -55 ملي فولت، وعند الوصول إليها تفتح قنوات الصوديوم المبوبة بالجهد دفعة واحدة."
            },
            {
                "q": "The Depolarization phase of the action potential (from -55 mV up to +30 mV) is caused by the rapid opening of voltage-gated channels and influx of:",
                "options": [
                    "Potassium ions (K+) efflux",
                    "Sodium ions (Na+) influx",
                    "Chloride ions (Cl-) influx",
                    "Calcium pump inactivation"
                ],
                "correct": 1,
                "note": "مرحلة إزالة الاستقطاب (Depolarization) تنتج عن التدفق السريع لأيونات الصوديوم (Na+ Influx) إلى داخل الخلية."
            },
            {
                "q": "The Repolarization phase of the action potential (returning from +30 mV back toward negative) is caused by:",
                "options": [
                    "Closing of Na+ channels and opening of slower voltage-gated Potassium (K+) channels causing K+ efflux",
                    "Continuous Na+ influx",
                    "Calcium entry into nucleus",
                    "ATP synthesis shutdown"
                ],
                "correct": 0,
                "note": "مرحلة إعادة الاستقطاب (Repolarization) تنتج عن انغلاق قنوات الصوديوم وتدفق أيونات البوتاسيوم للخارج (K+ Efflux)."
            },
            {
                "q": "During the action potential, the membrane potential overshoots the resting state down to about -90 mV. This phase is called:",
                "options": [
                    "Depolarization",
                    "Hyperpolarization (Undershoot)",
                    "Threshold",
                    "Resting potential"
                ],
                "correct": 1,
                "note": "فرط الاستقطاب (Hyperpolarization): نزول الجهد إلى -90 ملي فولت بسبب بطء انغلاق قنوات البوتاسيوم."
            },
            {
                "q": "What is the critical physiological significance of the Hyperpolarization phase in nerve conduction?",
                "options": [
                    "It raises the threshold (Refractory period) and ensures that action potentials propagate strictly in one forward direction along the axon",
                    "It causes the nerve to die",
                    "It reverses blood circulation",
                    "It stops muscle contraction permanently"
                ],
                "correct": 0,
                "note": "أهمية فرط الاستقطاب: يضمن فترة الجموح (Refractory Period) ويمنع ارتداد الإشارة العصبية للخلف ليضمن سريانها في اتجاه واحد فقط."
            },
            {
                "q": "Following hyperpolarization, which cellular mechanism restores the resting ionic concentrations of Na+ and K+ across the membrane?",
                "options": [
                    "Simple passive diffusion only",
                    "Sodium-Potassium ATPase pump (Na+/K+ pump, pumping 3 Na+ out for 2 K+ in)",
                    "Endocytosis",
                    "Gravity"
                ],
                "correct": 1,
                "note": "مضخة الصوديوم والبوتاسيوم (Na+/K+ ATPase pump) تضخ 3 أيونات صوديوم للخارج مقابل 2 بوتاسيوم للداخل لإعادة التوزيع الأيوني لحالة الراحة."
            },
            {
                "q": "Neurons with a single axon and many branching dendrites (such as spinal motor neurons and pyramidal cells) are classified as:",
                "options": [
                    "Multipolar neurons",
                    "Bipolar neurons",
                    "Pseudounipolar neurons",
                    "Anaxonic neurons"
                ],
                "correct": 0,
                "note": "الخلايا العصبية عديدة الأقطاب (Multipolar): تحتوي على محور واحد والعديد من الزوائد الشجيرية كخلايا القرن الأمامي للحبل الشوكي."
            },
            {
                "q": "Sensory dorsal root ganglion neurons that have one process bifurcating into central and peripheral axonal branches are classified as:",
                "options": [
                    "Multipolar neurons",
                    "Pseudounipolar neurons",
                    "Bipolar neurons",
                    "Interneurons"
                ],
                "correct": 1,
                "note": "خلايا العقد الجذرية الخلفية (DRG) تعتبر أحادية القطب كاذبة (Pseudounipolar)."
            },
            {
                "q": "Neurons that carry nerve impulses from the central nervous system outward to muscles or glands are called:",
                "options": [
                    "Sensory (afferent) neurons",
                    "Motor (efferent) neurons",
                    "Interneurons",
                    "Glial cells"
                ],
                "correct": 1,
                "note": "الخلايا العصبية الحركية (Motor / Efferent): تنقل الأوامر العصبية من الجهاز العصبي المركزي إلى العضلات والغدد."
            },
            {
                "q": "Arrector pili muscles attached to hair follicles in the dermis are composed of which type of muscle tissue?",
                "options": [
                    "Smooth muscle (involuntary)",
                    "Skeletal muscle (voluntary)",
                    "Cardiac muscle",
                    "Elastic cartilage"
                ],
                "correct": 0,
                "note": "عضلات ناصبة الشعر (Arrector Pili) هي عضلات ملساء لا إرادية (Smooth Muscle) تنقبض عند البرد أو الخوف مسببة وقوف الشعر."
            },
            {
                "q": "Which tissue in the human body has the HIGHEST electrical conductivity when applying electrotherapy currents?",
                "options": [
                    "Tissues with high water and electrolyte content such as blood, muscle, and cerebrospinal fluid",
                    "Cortical bone",
                    "Subcutaneous adipose fat",
                    "Dry stratum corneum"
                ],
                "correct": 0,
                "note": "الأنسجة الغنية بالماء والأملاح (كالدم والعضلات والسائل النخاعي) تمتلك أعلى موصلية كهربائية وأقل مقاومة لمرور التيارات."
            }
        ]
    }
]
