import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AETHERIS Automotive MVP | Investor Portal",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for professional dark/tech theme
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #00FFA3;
        margin-bottom: 0px;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #A0AEC0;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #1A202C;
        border: 1px solid #2D3748;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .highlight-box {
        background-color: #1A202C;
        border-left: 4px solid #00FFA3;
        padding: 15px;
        margin: 10px 0;
        border-radius: 0 8px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# Language selection
lang = st.sidebar.selectbox("🌐 Language / Мова", ["UA", "EN"])

# Dictionary of texts
texts = {
    "UA": {
        "title": "AETHERIS Automotive MVP",
        "subtitle": "Інвестиційний портал та технічна специфікація демонстраційного автомобіля",
        "nav_home": "Головна та Візія",
        "nav_proto": "Лабораторний Прототип",
        "nav_video": "Відеопрезентація з диктором",
        "nav_budget": "Бюджет та План",
        "nav_team": "Команда та Лабораторія",
        "nav_contact": "Контакти для інвесторів",
        
        # Home
        "vision_title": "Мета проєкту та Філософія",
        "vision_text": "AETHERIS — це не просто система відеоспостереження, а філософія осмислення подій навколо автомобіля. Ми створюємо цілісне, пояснюване та контекстне розуміння ситуації (Living Security Context) для професійних служб безпеки, захищених перевезень та корпоративного транспорту.",
        "key_metrics_title": "Ключові показники MVP",
        "budget_metric": "Загальний бюджет",
        "time_metric": "Термін реалізації",
        "sensors_metric": "Сенсорна мережа",
        
        # Prototype
        "proto_title": "Лабораторний екземпляр та Архітектура",
        "proto_desc": "Повноцінний мобільний доказ того, що технологія AETHERIS працює в реальному дорожньому та міському середовищі.",
        "hw_title": "Апаратна конфігурація лабораторії:",
        "hw_items": [
            "📷 **Камери:** Конфігурація з високоякісними HDR-камерами (до 8 камер сумарно: 3 спереду, 3 ззаду, 2 бокові з синхронною передачею через GMSL2).",
            "📡 **Радари:** 2 незалежні радари (передній і задній сектори, 76–81 ГГц TI AWR1843BOOST) для вимірювання дистанції, напрямку та відносної швидкості.",
            "🧠 **Мозок системи (Edge AI):** NVIDIA Jetson AGX Orin (до 275 TOPS, 64 ГБ пам'яті) для локального оброблення багатопотокового відео та сенсорів без затримки хмари.",
            "⚡ **Автономне живлення:** Окрема система живлення, що захищає обладнання й акумулятор автомобіля під час запуску, зупинки та тривалої стоянки (робота при вимкненому двигуні).",
            "🔌 **CAN-шина та синхронізація:** Ізольований CAN-шлюз у режимі читання для комунікації з бортовими системами автомобіля та апаратна синхронізація потоків камер і радарів.",
            "🎛️ **Лабораторна монтажна плата:** Спеціально розроблений електронний блок (плата живлення, інтерфейси, охолодження, корпус з модульним доступом)."
        ],
        
        # Video
        "video_title": "Відеоролик з диктором (Презентація для інвесторів)",
        "video_desc": "Нижче наведено відеопрезентацію проєкту та сценарій професійного диктора для демонстрації інвесторам.",
        "script_title": "Сценарій диктора (Voiceover Script):",
        "script_content": """
        [Кадр 1: Інтер'єр лабораторії, монтажна плата з Jetson Orin та сенсори]
        Диктор: «Сучасні системи безпеки бачать дорожні перешкоди. AETHERIS бачить ситуацію в цілому. Ми створюємо лабораторний прототип автомобіля, що здатний мислити контекстом.»
        
        [Кадр 2: Крупний план плати Jetson Orin, підключення до камер і радарів]
        Диктор: «Серцем нашої системи є потужний обчислювальний модуль NVIDIA Jetson Orin, який обробляє синхронізовані потоки з камер та двох високоточних радарів у реальному часі.»
        
        [Кадр 3: Демонстрація системи живлення та підключення до CAN-шини автомобіля]
        Диктор: «Завдяки автономній системі живлення комплекс продовжує працювати навіть при вимкненому двигуні, а безпечний CAN-шлюз забезпечує повну комунікацію з бортовими системами автомобіля.»
        
        [Кадр 4: Інтерфейс планшета оператора — Living Security Context]
        Диктор: «AETHERIS перетворює розрізнені сигнали на прозору картину подій, надаючи оператору повну ситуаційну обізнаність. Інвестуйте в безпеку майбутнього.»
        """,
        
        # Budget
        "budget_title": "Бюджет проєкту ($220,000) та План робіт",
        "budget_desc": "Фінансування спрямовується безпосередньо на команду, закупівлю обладнання, створення лабораторії та дорожні випробування.",
        "timeline_title": "План робіт (6 місяців):",
        "timeline_items": [
            "**Місяць 1:** Оренда лабораторії, придбання автомобіля, фіналізація архітектури.",
            "**Місяць 2:** Стендова робота камер, радарів і Edge-комп'ютера, тестування моделей.",
            "**Місяць 3:** Проєктування блока електроніки, плат, корпусу, живлення та кріплень.",
            "**Місяць 4:** Монтаж обладнання в автомобіль, синхронізація та мобільний застосунок.",
            "**Місяць 5:** Робота Context Engine, перевірка сценаріїв, денні та нічні випробування.",
            "**Місяць 6:** Усунення помилок, фінальна стабільність та демонстрація інвесторам."
        ],
        
        # Team
        "team_title": "Команда та Лабораторний простір",
        "team_desc": "Ядро команди складається з практикуючих інженерів, архітекторів штучного інтелекту та фахівців з професійної безпеки (Executive Protection).",
        
        # Contact
        "contact_title": "Зв'язатися з засновниками",
        "contact_desc": "Зацікавлені в інвестиціях або партнерстві? Отримайте повний фінансовий план та запрошення на демонстрацію в лабораторному боксі.",
        "contact_btn": "Надіслати запит інвестора"
    },
    "EN": {
        "title": "AETHERIS Automotive MVP",
        "subtitle": "Investor Portal & Technical Specification of Demonstration Vehicle",
        "nav_home": "Home & Vision",
        "nav_proto": "Laboratory Prototype",
        "nav_video": "Narrated Video Presentation",
        "nav_budget": "Budget & Roadmap",
        "nav_team": "Team & Laboratory",
        "nav_contact": "Investor Contact",
        
        # Home
        "vision_title": "Project Vision & Philosophy",
        "vision_text": "AETHERIS is not just a video surveillance system, but a philosophy of understanding events around the vehicle. We create a holistic, explainable, and contextual situational awareness (Living Security Context) for professional security services, secure transportation, and corporate fleets.",
        "key_metrics_title": "Key MVP Metrics",
        "budget_metric": "Total Budget",
        "time_metric": "Timeline",
        "sensors_metric": "Sensor Network",
        
        # Prototype
        "proto_title": "Laboratory Prototype & Architecture",
        "proto_desc": "A fully functional mobile proof that the AETHERIS core technology operates in real road and urban environments.",
        "hw_title": "Laboratory Hardware Configuration:",
        "hw_items": [
            "📷 **Cameras:** High-end HDR camera setup (up to 8 cameras total: 3 front, 3 rear, 2 side with synchronous GMSL2 transmission).",
            "📡 **Radars:** 2 independent radars (front and rear sectors, 76–81 GHz TI AWR1843BOOST) for distance, direction, and relative speed measurement.",
            "🧠 **System Brain (Edge AI):** NVIDIA Jetson AGX Orin (up to 275 TOPS, 64GB RAM) for local multi-stream video and sensor processing without cloud latency.",
            "⚡ **Autonomous Power Supply:** Dedicated power system protecting equipment and vehicle battery during startup, shutdown, and extended parking (operates with engine off).",
            "🔌 **CAN Bus & Synchronization:** Read-only isolated CAN gateway for communication with vehicle systems and hardware synchronization of camera and radar streams.",
            "🎛️ **Laboratory Mounting Board:** Custom-designed electronic unit (power board, interfaces, cooling, modular enclosure)."
        ],
        
        # Video
        "video_title": "Narrated Video Presentation (Investor Pitch)",
        "video_desc": "Below is the project video presentation and the professional voiceover script for investor demonstrations.",
        "script_title": "Voiceover Script:",
        "script_content": """
        [Scene 1: Laboratory interior, mounting board with Jetson Orin and sensors]
        Narrator: 'Modern vehicle safety systems see road obstacles. AETHERIS sees the situation as a whole. We are building a laboratory vehicle prototype capable of context-aware thinking.'
        
        [Scene 2: Close-up of Jetson Orin board, connection to cameras and radars]
        Narrator: 'The heart of our system is the powerful NVIDIA Jetson Orin computing module, processing synchronized streams from cameras and two high-precision radars in real time.'
        
        [Scene 3: Demonstration of power system and CAN bus vehicle integration]
        Narrator: 'Thanks to an autonomous power supply, the complex continues to operate even with the engine off, while a secure CAN gateway ensures full communication with vehicle systems.'
        
        [Scene 4: Operator tablet interface — Living Security Context]
        Narrator: 'AETHERIS transforms fragmented signals into a transparent picture of events, granting the operator full situational awareness. Invest in the future of security.'
        """,
        
        # Budget
        "budget_title": "Project Budget ($220,000) & Roadmap",
        "budget_desc": "Funding is allocated directly to the engineering team, hardware procurement, laboratory setup, and road testing.",
        "timeline_title": "Roadmap (6 Months):",
        "timeline_items": [
            "**Month 1:** Lab rental, vehicle acquisition, architecture finalization.",
            "**Month 2:** Camera, radar, and Edge computer bench testing, model validation.",
            "**Month 3:** Design of electronics block, PCBs, enclosure, power, and mounts.",
            "**Month 4:** Vehicle hardware installation, synchronization, and mobile app.",
            "**Month 5:** Context Engine operation, expert scenario checks, day/night testing.",
            "**Month 6:** Bug fixing, final stability check, and investor demonstrations."
        ],
        
        # Team
        "team_title": "Team & Laboratory Space",
        "team_desc": "The core team consists of practicing engineers, AI architects, and professional security (Executive Protection) specialists.",
        
        # Contact
        "contact_title": "Contact the Founders",
        "contact_desc": "Interested in investing or partnering? Get the full financial model and an invitation for a live demonstration in our laboratory garage.",
        "contact_btn": "Submit Investor Inquiry"
    }
}

t = texts[lang]

# Sidebar Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", [
    t["nav_home"],
    t["nav_proto"],
    t["nav_video"],
    t["nav_budget"],
    t["nav_team"],
    t["nav_contact"]
])

# MAIN CONTENT
st.markdown(f'<p class="main-header">{t["title"]}</p>', unsafe_allow_html=True)
st.markdown(f'<p class="sub-header">{t["subtitle"]}</p>', unsafe_allow_html=True)

# 1. HOME & VISION
if section == t["nav_home"]:
    st.header(t["vision_title"])
    st.write(t["vision_text"])
    
    st.markdown("---")
    st.subheader(t["key_metrics_title"])
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h3>$220,000</h3>
            <p>{t["budget_metric"]}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h3>6 Months</h3>
            <p>{t["time_metric"]}</p>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h3>8 Cameras + 2 Radars</h3>
            <p>{t["sensors_metric"]}</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("---")
    st.markdown(f"""
    <div class="highlight-box">
    <b>Core Innovation:</b> Living Security Context — translating raw sensor feeds into actionable, explainable event sequences for professional security mobility.
    </div>
    """, unsafe_allow_html=True)

# 2. LABORATORY PROTOTYPE
elif section == t["nav_proto"]:
    st.header(t["proto_title"])
    st.write(t["proto_desc"])
    
    st.subheader(t["hw_title"])
    for item in t["hw_items"]:
        st.markdown(f"- {item}")
        
    st.markdown("---")
    st.info("💡 **Lab Setup Note:** The lab is built across two connected garage boxes (90–120 m²) — one for vehicle integration, the second for electronics, sensors bench, and software development.")

# 3. VIDEO PRESENTATION
elif section == t["nav_video"]:
    st.header(t["video_title"])
    st.write(t["video_desc"])
    
    # Video placeholder box
    st.markdown("""
    <div style="background-color: #0E1117; border: 2px dashed #00FFA3; padding: 40px; text-align: center; border-radius: 10px; margin-bottom: 20px;">
        <h2 style="color: #00FFA3;">🎥 [ Video Pitch with Narrator Placeholder ]</h2>
        <p style="color: #A0AEC0;">Featuring the laboratory vehicle prototype, Jetson Orin brain, autonomous power system, and live sensor synchronization.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader(t["script_title"])
    st.code(t["script_content"], language="text")

# 4. BUDGET & ROADMAP
elif section == t["nav_budget"]:
    st.header(t["budget_title"])
    st.write(t["budget_desc"])
    
    st.subheader(t["timeline_title"])
    for item in t["timeline_items"]:
        st.markdown(f"- {item}")
        
    st.markdown("---")
    st.subheader("Budget Allocation Summary")
    
    import pandas as pd
    df_budget = pd.DataFrame({
        "Category (Напрям)": [
            "Основна команда (Core Team)",
            "Сенсори, Edge-комп'ютер та інтеграція",
            "Оренда й оснащення лабораторії",
            "Автомобіль і початкова підготовка",
            "Технічний та валютний резерв",
            "Зовнішні інженерні роботи",
            "Фахівець з Executive Protection",
            "Правова і кібербезпекова підготовка"
        ],
        "Budget ($)": [104000, 35000, 25000, 20000, 17000, 10000, 6000, 3000]
    })
    st.dataframe(df_budget, use_container_width=True)

# 5. TEAM & LABORATORY
elif section == t["nav_team"]:
    st.header(t["team_title"])
    st.write(t["team_desc"])
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Key Roles
        - **Technical Project Lead / System Architect** (Context Engine & overall integration)
        - **Edge AI / Computer Vision Engineer** (Object detection & tracking)
        - **Hardware / Embedded Engineer** (CAN bus, power supply, sensors sync)
        - **Mechanical / Thermal Design Engineer** (Enclosure, cooling, vibration protection)
        """)
    with col2:
        st.markdown("""
        ### Expert Advisors
        - **Executive Protection & Criminology Expert** (Defining realistic threat scenarios)
        - **Application / Frontend Engineer** (Operator tablet dashboard)
        - **Testing Engineer** (Road tests and validation)
        """)

# 6. CONTACT
elif section == t["nav_contact"]:
    st.header(t["contact_title"])
    st.write(t["contact_desc"])
    
    with st.form("investor_form"):
        name = st.text_input("Name / Ім'я")
        email = st.text_input("Email / Електронна пошта")
        company = st.text_input("Fund / Company / Фонд або Компанія")
        message = st.text_area("Message / Повідомлення")
        
        submitted = st.form_submit_button(t["contact_btn"])
        if submitted:
            st.success("Дякуємо! Ваш запит надіслано засновникам проєкту. Ми зв'яжемося з вами найближчим часом." if lang == "UA" else "Thank you! Your inquiry has been sent. We will contact you shortly.")
