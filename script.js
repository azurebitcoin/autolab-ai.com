// Multilingual Dictionary (UK / EN)
const translations = {
    uk: {
        nav_about: "Про проєкт",
        nav_tech: "Технологія",
        nav_features: "Функції",
        nav_roadmap: "План робіт",
        nav_budget: "Бюджет",
        nav_contact: "Контакти",
        nav_invest_btn: "Інвестувати",

        hero_badge: "MVP РАУНД • $220,000 • 6 МІСЯЦІВ",
        hero_title: "Штучний Інтелект Ситуаційної Безпеки для Автомобілів",
        hero_subtitle: "AETHERIS Automotive MVP — автономна система кругового огляду з 3 HDR-камерами, 2 радарами та Edge AI. Перетворює розрізнені потоки сенсорів у Living Security Context у реальному часі.",
        hero_btn_primary: "Інвестиційний Меморандум",
        hero_btn_secondary: "Огляд Архітектури",

        metric_budget: "Цільовий бюджет MVP",
        metric_timeline: "До ходового авто",
        metric_months_unit: "міс.",
        metric_sensors: "Камери HDR + Радари",
        metric_coverage: "Круговий Living Context",

        tag_front_cams: "3x HDR 120dB Камери",
        tag_radar: "77GHz FMCW Радар",
        tag_edge: "Edge Context AI",
        status_online: "AETHERIS Core: Online • 360° Multi-Sensor Fusion",

        about_tag: "ЧОМУ ЦЕ ПОТРІБНО",
        about_title: "Понад звичайний ADAS: Інтелект Захисту",
        about_desc: "Сучасні автосистеми лише запобігають ДТП або записують відео. Вони «сліпі» до загроз безпеки, переслідування, спостереження та зміни намірів об'єктів.",
        problem_title: "Обмеження класичних систем",
        problem_1: "Відеореєстратори пишуть окремі файли без просторового та часового зв'язку",
        problem_2: "ADAS орієнтований лише на утримання смуги та екстрене гальмування",
        problem_3: "Відсутність розуміння намірів: хто йде за авто, чи повторюється об'єкт на маршруті",
        problem_4: "Оператор перевантажений десятками розрізнених екранів і хибних тривог",

        solution_title: "Рішення AETHERIS",
        solution_1: "<strong>Living Security Context:</strong> єдина картина розвитку подій навколо авто",
        solution_2: "<strong>Re-Identification:</strong> супровід людей та авто при переході між камерами",
        solution_3: "<strong>Ф’южн сенсорів:</strong> перехресне підтвердження камер та 77GHz радарів",
        solution_4: "<strong>Пояснюваний ШІ:</strong> прозорі обґрунтування загроз для оператора",

        tech_tag: "ТЕХНІЧНИЙ СКЛАД",
        tech_title: "Апаратна та Програмна Архітектура",
        tech_desc: "Використання готових індустріальних компонентів мінімізує R&D ризики та забезпечує максимальну концентрацію на розробці алгоритмів контексту.",
        tech_sensors_title: "3x HDR Камери + 2 Радари",
        tech_sensors_desc: "Високоякісні HDR-камери з GMSL2 передачею даних. Два 77GHz радари для вимірювання швидкості та відстані.",
        tech_edge_title: "Локальний Edge AI Комп'ютер",
        tech_edge_desc: "Платформа промислового класу з апаратним прискоренням нейромереж. Локальна обробка 3 потоків у реальному часі без необхідності постійної хмари.",
        tech_engine_title: "Living Security Context Core",
        tech_engine_desc: "Унікальний рушій відстеження траєкторій, аналізу часових патернів та оцінки ризику. Зіставляє повторювані спостереження на всьому маршруті руху.",

        feat_tag: "ФУНКЦІОНАЛ MVP",
        feat_title: "5 Ключових Можливостей Демонстратора",
        feat_1_title: "Виявлення Людей та Авто",
        feat_1_desc: "Точна детекція об'єктів навколо машини в радіусі 360° вдень, уночі та за будь-якої погоди.",
        feat_2_title: "Сектор та Траєкторія",
        feat_2_desc: "Визначення точного сектора знаходження, напрямку руху, швидкості наближення та дистанції.",
        feat_3_title: "Міжкамерний Супровід",
        feat_3_desc: "Безшовне відстеження об'єкта, який виходить з поля зору передньої камери й з'являється на бічній або задній.",
        feat_4_title: "Радарно-Візуальний Ф’южн",
        feat_4_desc: "Зіставлення візуальних маркерів із доплерівськими відбитками радарів для усунення сліпих зон і туману.",
        feat_5_title: "Часова Послідовність Подій",
        feat_5_desc: "Складання структурованого журналу ситуації: хто, коли та скільки разів фіксувався поруч з об'єктом охорони.",
        feat_6_title: "Інтерфейс Оператора",
        feat_6_desc: "Інтуїтивний сенсорний екран для водія чи агента служби безпеки з візуалізацією загроз у реальному часі.",

        roadmap_tag: "ГРАФІК РОБІТ",
        roadmap_title: "6-Місячний План Створення MVP",
        roadmap_desc: "Чіткі послідовні віхи: від оренди лабораторії та стендових тестів до повноцінного тестового автомобіля на дорозі.",
        step_1_time: "Місяць 1",
        step_1_title: "Лабораторія та Закупівля",
        step_1_desc: "Оренда гаражного боксу (90–120 м²), купівля базового автомобіля, фіналізація архітектури та замовлення сенсорів.",
        step_2_time: "Місяць 2",
        step_2_title: "Стендові Тести Сенсорів",
        step_2_desc: "Лабораторна інтеграція камер, радарів та Edge-ПК. Тестування нейромереж детекції та перевірка GMSL2 зв'язку.",
        step_3_time: "Місяць 3",
        step_3_title: "Інженерне Проєктування",
        step_3_desc: "Розробка плати стабілізації живлення, захищених кронштейнів камер, термоізоляції та кабельних джгутів.",
        step_4_time: "Місяць 4",
        step_4_title: "Монтаж та Інтеграція в Авто",
        step_4_desc: "Установка апаратного комплексу в автомобіль. Синхронізація CAN-шини, GNSS/IMU та перший запуск застосунку оператора.",
        step_5_time: "Місяць 5",
        step_5_title: "Context Engine & Дорожні Тести",
        step_5_desc: "Калібрування Context Engine у русі: денні, нічні та дощові випробування. Перевірка сценаріїв виявлення спостереження.",
        step_6_time: "Місяць 6",
        step_6_title: "Фіналізація та Демонстрація",
        step_6_desc: "Стрес-тестування стабільності. Презентації для клієнтів (Executive Protection, спецслужби) та Seed-інвесторів.",

        budget_tag: "ФІНАНСОВА СТРУКТУРА",
        budget_title: "Розподіл Бюджету $220,000",
        budget_desc: "Бюджет розрахований на повний 6-місячний цикл створення діючого демонстратора з урахуванням технічного резерву.",
        total_round: "Загальний розмір раунду",
        b_team: "Основна інженерна команда (6 міс.)",
        b_hw: "Сенсори, Edge-комп’ютер, комплектуючі",
        b_lab: "Оренда та оснащення лабораторії",
        b_car: "Базовий автомобіль та підготовка",
        b_reserve: "Технічний та валютний резерв",
        b_ext: "Зовнішні інженерні роботи (Thermal/Mech)",
        b_expert: "Консультації Executive Protection & Кримінолог",
        b_legal: "Юридичний та кібербезпековий супровід",

        hw_breakdown_title: "Деталізація апаратних витрат ($35,000)",
        hw_1: "3 HDR-камери, GMSL2 плата, кабелі",
        hw_2: "Edge AI комп’ютер, NVMe, охолодження",
        hw_3: "2 радари міліметрового діапазону",
        hw_4: "GNSS, IMU, CAN-шлюз та синхронізація",
        hw_5: "Автомобільне живлення, захист АКБ",
        hw_6: "Сенсорний дисплей та мережевий шлюз",
        hw_7: "Запасні компоненти, доставка та мито",

        market_tag: "ЦІЛЬОВИЙ РИНОК",
        market_title: "Для Кого Створюється AETHERIS",
        m_1_title: "Служби Executive Protection",
        m_1_desc: "Захист перших осіб та VIP-кортежів. Виявлення спостереження, хвостів та небезпечних сценаріїв завчасно.",
        m_2_title: "Інкасація та Цінні Вантажі",
        m_2_desc: "Моніторинг периметра при зупинках, завантаженні та русі маршрутом високого ступеня ризику.",
        m_3_title: "Тактичні та Безпілотні Флоти",
        m_3_desc: "Інтеграція в автономні платформи для повного розуміння тактичної обстановки без оператора на борту.",

        cta_badge: "РАУНД ВІДКРИТО",
        cta_title: "Станьте Інвестором AETHERIS Automotive",
        cta_desc: "Ми шукаємо стратегічних інвесторів та партнерів для фінансування 6-місячного циклу створення MVP ($220,000). Отримайте повний Pitch Deck та фінансову модель.",
        opt_angel: "Business Angel ($25k - $50k)",
        opt_vc: "Venture Fund / Lead ($100k+)",
        opt_strategic: "Стратегічний партнер (Automotive / Security)",
        btn_request_deck: "Запитати Pitch Deck & Зустріч",
        form_success: "✓ Дякуємо! Ваш запит прийнято. Ми надішлемо матеріали на вказану пошту протягом кількох годин.",
        footer_copy: "AETHERIS Automotive Situational Intelligence Platform. © 2025 AutoLab AI. Всі права захищено.",
        
        // Auth overlay translations
        auth_subtitle: "Захищений інвестиційний портал. Введіть пароль доступу.",
        auth_btn: "Увійти",
        auth_error: "Невірний пароль. Спробуйте ще раз."
    },
    en: {
        nav_about: "About Project",
        nav_tech: "Technology",
        nav_features: "Features",
        nav_roadmap: "Roadmap",
        nav_budget: "Budget",
        nav_contact: "Contact",
        nav_invest_btn: "Invest Now",

        hero_badge: "MVP ROUND • $220,000 • 6 MONTHS",
        hero_title: "Situational Intelligence & Context AI for Autonomous Mobility",
        hero_subtitle: "AETHERIS Automotive MVP — 360° situational awareness platform powered by 3 HDR cameras, 2 FMCW radars, and Edge AI. Transforming raw sensor streams into real-time Living Security Context.",
        hero_btn_primary: "Investment Memorandum",
        hero_btn_secondary: "Architecture Overview",

        metric_budget: "MVP Target Budget",
        metric_timeline: "To Road Demonstrator",
        metric_months_unit: "mos",
        metric_sensors: "HDR Cameras + Radars",
        metric_coverage: "360° Living Context",

        tag_front_cams: "3x HDR 120dB Cameras",
        tag_radar: "77GHz FMCW Radar",
        tag_edge: "Edge Context AI",
        status_online: "AETHERIS Core: Online • 360° Multi-Sensor Fusion",

        about_tag: "THE OPPORTUNITY",
        about_title: "Beyond Conventional ADAS: Situational Security Intelligence",
        about_desc: "Modern automotive systems focus only on crash prevention and passive video recording. They remain blind to security threats, trailing vehicles, hostile surveillance, and shifting intentions.",
        problem_title: "Limitations of Existing Tech",
        problem_1: "Dashcams record isolated video clips lacking spatial and temporal continuity",
        problem_2: "ADAS is strictly tuned for lane-keeping and emergency braking",
        problem_3: "Zero intent understanding: who is following the vehicle across the route",
        problem_4: "Security operators are overwhelmed by disconnected camera grids and false alarms",

        solution_title: "The AETHERIS Solution",
        solution_1: "<strong>Living Security Context:</strong> A unified, explanatory picture of unfolding events",
        solution_2: "<strong>Cross-Camera Re-ID:</strong> Seamless tracking of pedestrians and vehicles across sectors",
        solution_3: "<strong>Multi-Sensor Fusion:</strong> Cross-validation between HDR vision and 77GHz radars",
        solution_4: "<strong>Explainable Edge AI:</strong> Transparent risk scoring for immediate operator response",

        tech_tag: "TECHNICAL STACK",
        tech_title: "Hardware & Software Architecture",
        tech_desc: "Built on industrial-grade COTS components to minimize R&D risks and focus core development on patentable situational context algorithms.",
        tech_sensors_title: "3x HDR Cameras + 2 Radars",
        tech_sensors_desc: "High-quality HDR cameras with GMSL2 data transmission. Dual 77GHz FMCW radars for velocity and distance precision.",
        tech_edge_title: "On-Board Edge AI Compute",
        tech_edge_desc: "Industrial-grade hardware with dedicated neural network accelerators. Processing 3 real-time video streams locally with zero cloud latency requirement.",
        tech_engine_title: "Living Security Context Core",
        tech_engine_desc: "Proprietary engine correlating multi-camera trajectories, temporal behavior patterns, and proximity anomalies throughout the vehicle's entire journey.",

        feat_tag: "MVP CAPABILITIES",
        feat_title: "5 Core Functions of the Demonstrator",
        feat_1_title: "Pedestrian & Vehicle Detection",
        feat_1_desc: "Precision 360° object detection day & night under harsh weather and extreme lighting transitions.",
        feat_2_title: "Sector & Trajectory Estimation",
        feat_2_desc: "Real-time sector positioning, velocity vector, distance estimation, and approach acceleration.",
        feat_3_title: "Cross-Camera Re-Identification",
        feat_3_desc: "Continuous tracking when an entity transitions from front cameras to lateral or rear surround zones.",
        feat_4_title: "Radar-Visual Fusion",
        feat_4_desc: "Correlating visual bounding boxes with millimeter-wave Doppler signatures to eliminate blind spots and fog.",
        feat_5_title: "Temporal Event Sequencing",
        feat_5_desc: "Compiling an explainable chronological event log: who, when, and how frequently observed near the asset.",
        feat_6_title: "Operator Tactical Console",
        feat_6_desc: "Intuitive touch screen interface for drivers and protective security details with real-time threat highlighting.",

        roadmap_tag: "DEVELOPMENT TIMELINE",
        roadmap_title: "6-Month MVP Delivery Plan",
        roadmap_desc: "Strict milestone-driven roadmap from lab prototyping and sensor bench validation to a fully operational road testbed.",
        step_1_time: "Month 1",
        step_1_title: "Lab Setup & Procurement",
        step_1_desc: "Facility lease (90–120 m²), test vehicle acquisition, architecture finalization, and COTS sensor procurement.",
        step_2_time: "Month 2",
        step_2_title: "Sensor Bench Integration",
        step_2_desc: "Lab bench testing of GMSL2 cameras, radars, and Edge compute. Computer vision model baseline benchmarking.",
        step_3_time: "Month 3",
        step_3_title: "Mechanical & Power Engineering",
        step_3_desc: "Custom automotive power distribution PCB, rugged camera brackets, thermal enclosures, and harness design.",
        step_4_time: "Month 4",
        step_4_title: "Vehicle Integration & Harnessing",
        step_4_desc: "Full hardware mounting in the testbed vehicle. CAN-bus, GNSS/IMU integration, and initial tactical UI testing.",
        step_5_time: "Month 5",
        step_5_title: "Context Engine & Field Testing",
        step_5_desc: "Living Security Context calibration in motion: day, night, rain, and synthetic hostile surveillance scenarios.",
        step_6_time: "Month 6",
        step_6_title: "System Hardening & Live Demos",
        step_6_desc: "Reliability validation, client live demonstrations for Executive Protection fleets, and Seed round closing.",

        budget_tag: "FINANCIAL STRUCTURE",
        budget_title: "$220,000 MVP Budget Allocation",
        budget_desc: "Fully budgeted for a complete 6-month cycle to build, test, and demonstrate an operational vehicle including contingency reserve.",
        total_round: "Total Round Size",
        b_team: "Core Engineering Team (6 months)",
        b_hw: "Sensors, Edge AI Compute & Components",
        b_lab: "Lab Lease & Workspace Equipping",
        b_car: "Vehicle Platform & Pre-conditioning",
        b_reserve: "Technical & FX Contingency Reserve",
        b_ext: "Specialized Mechanical & Thermal Engineering",
        b_expert: "Executive Protection & Criminology Expert",
        b_legal: "Legal, IP & Cyber Protection Advisory",

        hw_breakdown_title: "Hardware Cost Breakdown ($35,000)",
        hw_1: "3 HDR Cameras, GMSL2 Interface, Cables",
        hw_2: "Edge AI Industrial PC, NVMe, Active Cooling",
        hw_3: "2 Automotive 77GHz Millimeter-Wave Radars",
        hw_4: "GNSS, IMU, CAN-Bus Gateway & Sync Hub",
        hw_5: "Automotive Isolated Power & Battery Guard",
        hw_6: "Tactical Touch Display & High-Speed Gateway",
        hw_7: "Spares, Shipping, Import & Customs Fees",

        market_tag: "TARGET MARKET",
        market_title: "Commercialization & Target Verticals",
        m_1_title: "Executive Protection Details",
        m_1_desc: "VIP convoys and private security firms requiring early detection of surveillance, following vehicles, and ambushes.",
        m_2_title: "Armored Transport & High-Value Cargo",
        m_2_desc: "Perimeter monitoring during stops, transit, and loading in high-risk zones.",
        m_3_title: "Autonomous & Tactical Fleets",
        m_3_desc: "Seamless integration into robotic mobility platforms requiring comprehensive 360° tactical environmental comprehension.",

        cta_badge: "ROUND OPEN",
        cta_title: "Partner with AETHERIS Automotive",
        cta_desc: "We are inviting strategic angel investors and venture funds to co-found and finance the 6-month MVP delivery ($220,000). Request our Investor Pitch Deck and financial model.",
        opt_angel: "Business Angel ($25k - $50k)",
        opt_vc: "Venture Fund / Lead ($100k+)",
        opt_strategic: "Strategic Partner (Automotive / Security)",
        btn_request_deck: "Request Pitch Deck & Meeting",
        form_success: "✓ Thank you! Your request has been received. We will deliver the investor package to your email shortly.",
        footer_copy: "AETHERIS Automotive Situational Intelligence Platform. © 2025 AutoLab AI. All rights reserved.",

        // Auth overlay translations
        auth_subtitle: "Protected investor portal. Enter access password.",
        auth_btn: "Login",
        auth_error: "Incorrect password. Please try again."
    }
};

let currentLang = localStorage.getItem('autolab_lang') || 'uk';

function switchLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('autolab_lang', lang);
    document.documentElement.lang = lang;

    // Update switcher buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.toggle('active', btn.id === `btn-${lang}`);
    });

    // Update all i18n text nodes
    document.querySelectorAll('[data-i18n]').forEach(el => {
        const key = el.getAttribute('data-i18n');
        if (translations[lang] && translations[lang][key]) {
            el.innerHTML = translations[lang][key];
        }
    });
}

function handleFormSubmit(e) {
    e.preventDefault();
    const name = document.getElementById('investorName').value;
    const email = document.getElementById('investorEmail').value;
    const company = document.getElementById('investorCompany').value;
    const type = document.getElementById('investorType').value;

    const successEl = document.getElementById('formSuccess');
    if (successEl) {
        successEl.style.display = 'block';
        successEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    // Optional mailto trigger
    const subject = encodeURIComponent(`Investor Inquiry: AETHERIS MVP ($220k Round) - ${name}`);
    const body = encodeURIComponent(`Hello AutoLab AI Team,\n\nI would like to request the Pitch Deck and schedule an introductory call.\n\nName: ${name}\nEmail: ${email}\nOrganization: ${company}\nInvestor Profile: ${type}\n`);
    
    // Reset form after short delay
    setTimeout(() => {
        document.getElementById('investorForm').reset();
    }, 1500);
}

// Initial load
document.addEventListener('DOMContentLoaded', () => {
    // Check if password protection is passed
    const isAuth = sessionStorage.getItem('autolab_auth') === 'true';
    const authOverlay = document.getElementById('authOverlay');
    
    if (isAuth) {
        authOverlay.style.display = 'none';
        document.body.style.overflow = 'auto';
    } else {
        authOverlay.style.display = 'flex';
        document.body.style.overflow = 'hidden';
    }

    switchLanguage(currentLang);
});

// Password verification function
function handleAuth(e) {
    e.preventDefault();
    const passwordInput = document.getElementById('authPassword').value;
    const authError = document.getElementById('authError');
    const authOverlay = document.getElementById('authOverlay');

    if (passwordInput === '123123aA') {
        sessionStorage.setItem('autolab_auth', 'true');
        authOverlay.style.display = 'none';
        document.body.style.overflow = 'auto';
        authError.style.display = 'none';
    } else {
        authError.style.display = 'block';
        document.getElementById('authPassword').value = '';
    }
}

