import streamlit as st
   import os

   st.title("Мой рисунок")

   if os.path.exists("image.png"):
       st.image("image.png", caption="Это изображение из проекта")
   else:
       st.error("Файл image.png не найден в корневой папке.")
