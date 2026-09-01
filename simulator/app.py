import streamlit as st
import os

st.title("Мой рисунок")

# Ищем картинку в текущей папке или в родительской
image_path = None
for path in ["image.png", "simulator/image.png", "../image.png"]:
    if os.path.exists(path):
        image_path = path
        break

if image_path:
    st.image(image_path, caption="Это изображение из проекта")
else:
    st.error("Файл image.png не найден.")
