from PIL import Image
import streamlit as st
from Pages import Datasets, Introduction, Life_expectancy, Ecology, Releases

# --- базовые настройки ---
image = Image.open('img/logo-browser.png')
st.set_page_config(
    page_title="Data analysis in Streamlit",
    page_icon=image,
    layout="wide"
)

NAV_PAGES = ["Introduction", "Datasets", "Life_expectancy", "Ecology", "Releases"]

# текущая страница
if "current_page" not in st.session_state:
    st.session_state.current_page = "Introduction"


# ---------- ГОРИЗОНТАЛЬНЫЙ НАВБАР С ЛОГО СЛЕВА ----------
col_logo, col_buttons = st.columns([1, 8])

# Логотип слева
with col_logo:
    st.image("img/logo-home.svg", width=90)

# Кнопки справа
with col_buttons:
    cols = st.columns(len(NAV_PAGES))
    for i, page_name in enumerate(NAV_PAGES):
        if cols[i].button(page_name, key=f"nav_{page_name}", use_container_width=True):
            st.session_state.current_page = page_name

st.write("---")


# ---------- Роутинг страниц ----------
page = st.session_state.current_page

if page == 'Introduction':
    Introduction.Introduction().app()
elif page == 'Datasets':
    Datasets.Datasets().app()
elif page == 'Life_expectancy':
    Life_expectancy.Life_expectancy().app()
elif page == 'Ecology':
    Ecology.Ecology().app()
elif page == 'Releases':
    Releases.Releases().app()
