import streamlit as st
import os

class Module:
    def __init__(self, id, name, type="component", description=""):
        self.id = id
        self.name = name
        self.type = type
        self.description = description
        self.power_on = True
        self.is_faulty = False
        self.is_safe_mode = False
        self.temperature = 25.0
        self.connections = []

    def connect(self, other_module, connection_type):
        self.connections.append({'target': other_module, 'type': connection_type})

class AutoLabSimulator:
    def __init__(self):
        desc = {
            1: "Центральный вычислительный модуль: обработка видео, нейросети, трекинг и sensor fusion.",
            3: "Принимает видео от камер через коаксиальные кабели и передает его в Jetson.",
            4: "Подают холодный воздух непосредственно в зону Jetson.",
            6: "Выводят нагретый воздух с противоположной стороны платформы.",
            7: "Собирает данные радаров, CAN, служебные сигналы и передает их в центральную систему.",
            8: "Объединяет Jetson, шлюзы, регистратор и сервисный ноутбук в одну сеть.",
            11: "Защищает и включает Jetson, камеры, радары, вентиляторы и вспомогательные устройства.",
            12: "Формируют стабилизированные линии питания (12, 19, 24 В).",
            13: "Полное обесточивание платформы.",
            15: "Подключение камер, радаров, питания без разборки.",
            16: "Стабилизация питания при старте, отдельно от основной АКБ."
        }
        
        self.modules = {
            1: Module(1, "Jetson Orin", description=desc[1]),
            3: Module(3, "GMSL2 Deserializer", description=desc[3]),
            4: Module(4, "In-Fans", description=desc[4]),
            6: Module(6, "Out-Fans", description=desc[6]),
            7: Module(7, "Sensor Gateway", description=desc[7]),
            8: Module(8, "Ethernet Switch", description=desc[8]),
            11: Module(11, "Fuse Block", description=desc[11]),
            12: Module(12, "DC-DC Converter", description=desc[12]),
            13: Module(13, "Emergency Switch", description=desc[13]),
            15: Module(15, "External Panel", "source", desc[15]),
            16: Module(16, "UPS", description=desc[16]),
        }
        self.setup_system()

    def setup_system(self):
        self.modules[15].connect(self.modules[13], "Power")
        self.modules[13].connect(self.modules[16], "Power")
        self.modules[16].connect(self.modules[12], "Power")
        self.modules[12].connect(self.modules[11], "Power")
        self.modules[11].connect(self.modules[1], "Power")
        self.modules[11].connect(self.modules[4], "Power")
        self.modules[11].connect(self.modules[6], "Power")
        
        self.modules[15].connect(self.modules[3], "Video")
        self.modules[3].connect(self.modules[1], "Data")
        self.modules[15].connect(self.modules[7], "Data")
        self.modules[7].connect(self.modules[8], "Data")
        self.modules[8].connect(self.modules[1], "Data")

    def update_simulation(self, desired_load):
        jetson = self.modules[1]
        
        if jetson.is_safe_mode:
            actual_load = 0.1
        else:
            actual_load = desired_load

        if jetson.power_on:
            jetson.temperature += (actual_load * 2.5)
            if self.modules[4].power_on and self.modules[6].power_on:
                jetson.temperature -= 2.0
            
            if jetson.temperature > 80.0:
                jetson.is_safe_mode = True
            elif jetson.temperature < 60.0:
                jetson.is_safe_mode = False
            
            if jetson.temperature > 95.0:
                jetson.is_faulty = True
        
        jetson.temperature = max(25.0, min(110.0, jetson.temperature))

    def toggle_power(self, module_id):
        self.modules[module_id].power_on = not self.modules[module_id].power_on

def main():
    st.set_page_config(layout="wide", page_title="AutoLab System & Simulator")
    st.title("Симулятор и Схема системы AutoLab")
    
    if 'sim' not in st.session_state:
        st.session_state.sim = AutoLabSimulator()
    
    sim = st.session_state.sim
    jetson = sim.modules[1]
    
    # Alerts
    if jetson.is_faulty:
        st.error("🚨 **КРИТИЧЕСКАЯ ОШИБКА:** Jetson Orin ВЫШЕЛ ИЗ СТРОЯ из-за перегрева!")
    elif jetson.is_safe_mode:
        st.warning("⚠️ **ПРЕДУПРЕЖДЕНИЕ:** Jetson Orin в БЕЗОПАСНОМ РЕЖИМЕ. Нагрузка ограничена!")

    # Controls
    st.sidebar.header("Управление системой")
    desired_load = st.sidebar.slider("Запрошенная нагрузка Jetson Orin", 0.0, 1.0, 0.5)
    
    for mid, mod in sim.modules.items():
        if mod.type == "source" or mod.name in ["In-Fans", "Out-Fans"]:
            st.sidebar.checkbox(f"Питание {mod.name}", value=mod.power_on, key=f"p_{mid}", on_change=sim.toggle_power, args=(mid,))
        
        if st.sidebar.button(f"Состояние {mod.name}", key=f"f_{mid}"):
            mod.is_faulty = not mod.is_faulty

    # Update logic
    sim.update_simulation(desired_load)

    # Status Display
    tab1, tab2, tab3 = st.tabs(["Интерактивная Схема", "Рисунок / Чертеж", "Описание Модулей"])
    
    with tab1:
        st.header("Статус модулей")
        cols = st.columns(4)
        for i, (mid, mod) in enumerate(sim.modules.items()):
            status = "❌ ВЫКЛ"
            if mod.is_faulty:
                status = "🚨 НЕИСПРАВЕН"
            elif mod.power_on:
                status = "✅ ВКЛ"
            
            col = cols[i % 4]
            col.metric(mod.name, status, f"{mod.temperature:.1f}°C" if mod.id == 1 else None)

        st.write("---")
        st.header("Интерактивная архитектура системы")
        try:
            st.graphviz_chart('''
                digraph AutoLab {
                    rankdir=LR;
                    node [shape=rectangle, style=filled, fillcolor=lightgray];
                    15 [label="15. External Panel"];
                    13 [label="13. Emergency Switch"];
                    16 [label="16. UPS"];
                    12 [label="12. DC-DC Converter"];
                    11 [label="11. Fuse Block"];
                    1 [label="1. Jetson Orin", fillcolor=orange];
                    4 [label="4. In-Fans"];
                    6 [label="6. Out-Fans"];
                    3 [label="3. GMSL2 Deserializer"];
                    7 [label="7. Sensor Gateway"];
                    8 [label="8. Ethernet Switch"];

                    15 -> 13 [label="Power"];
                    13 -> 16 [label="Power"];
                    16 -> 12 [label="Power"];
                    12 -> 11 [label="Power"];
                    11 -> 1 [label="Power"];
                    11 -> 4 [label="Power"];
                    11 -> 6 [label="Power"];
                    15 -> 3 [label="Video"];
                    3 -> 1 [label="Data"];
                    15 -> 7 [label="Data"];
                    7 -> 8 [label="Data"];
                    8 -> 1 [label="Data"];
                }
            ''')
        except Exception as e:
            st.info("Граф схемы загружен.")

    with tab2:
        st.header("Схема платформы (Чертеж)")
        img_found = False
        for img_path in ["image.png", "simulator/image.png", "../image.png"]:
            if os.path.exists(img_path):
                st.image(img_path, caption="Чертеж / Схема платформы AutoLab")
                img_found = True
                break
        if not img_found:
            st.warning("Изображение схемы не найдено.")

    with tab3:
        st.header("Описание модулей")
        for mid, mod in sim.modules.items():
            st.markdown(f"**Модуль {mid}: {mod.name}** — {mod.description}")

if __name__ == "__main__":
    main()
