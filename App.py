from PIL import Image
import streamlit as st
from Pages import Datasets, Introduction, Life_expectancy, Ecology, Releases

# --- базовые настройки ---
st.set_page_config(
    page_title="ISTA350final",
    page_icon='img/logo-browser.svg',
    layout="wide"
)

image = Image.open('img/logo-browser.png')
st.markdown("""
<style>

/* ===== ШИРОКИЙ ЭКРАН ===== */
.block-container {
    max-width: 100% !important;
    padding-left: 20px;
    padding-right: 20px;
}

/* ===== ОСНОВНОЙ ФОН ===== */
[data-testid="stAppViewContainer"] {
    background: #818181;
    font-family: Tahoma, Arial, sans-serif;
     color: #fdffff;
}

/* ===== УБРАТЬ STREAMLIT HEADER ===== */
header[data-testid="stHeader"] {
    display: none;
}

/* ===== НАВБАР ===== */
div[data-testid="stHorizontalBlock"] {
    background: linear-gradient(180deg, #9a9a9a, #707070);
    padding: 10px 12px;
    margin-bottom: 12px;
}

/* ===== КНОПКИ ===== */
button {
    background: #bcbcbc !important;
    border: 2px solid #3a3a3a !important;
    box-shadow:
        inset 1px 1px 0 #ffffff,
        inset -1px -1px 0 #404040 !important;
    font-family: Tahoma, Arial, sans-serif;
    font-size: 12px !important;
    color: #fdffff;
    border-radius: 0 !important;
    padding: 6px 14px !important;
    transition: background 0.12s ease;
}

/* Hover — Windows Blue */
button:hover {
    background: #010081 !important;
    color: white !important;
}

/* Active */
button:active {
    box-shadow:
        inset -1px -1px 0 #ffffff,
        inset 1px 1px 0 #404040 !important;
}

/* ===== НЕ ТРОГАТЬ ТАБЛИЦЫ ===== */
/* DataFrame остаются дефолтные */

/* ===== INPUT ===== */
input, textarea {
    background: #efefef !important;
    border: 1px solid #3a3a3a !important;
    font-family: Tahoma, Arial, sans-serif;
    color: #fdffff;
}

/* ===== ЗАГОЛОВКИ ===== */
h1, h2, h3 {
    color: #000000;
}

/* ===== СКРОЛЛБАР ===== */
::-webkit-scrollbar {
    width: 14px;
}
::-webkit-scrollbar-thumb {
    background: #a9a9a9;
}
::-webkit-scrollbar-track {
    background: #7a7a7a;
}

</style>
""", unsafe_allow_html=True)



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
