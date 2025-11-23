from PIL import Image
import streamlit as st
from streamlit_navigation_bar import st_navbar
from Pages import Datasets
from Pages import Introduction
from Pages import GDP
from Pages import Movies
from Pages import Survey
import os
import pandas as pd
import numpy as np

image = Image.open('img/logo-browser.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image, page_title="Data analysis in streamlit")

logo_path = os.path.join(os.path.dirname(__file__), "img", "logo-home.svg")
pages = [" ",'Introduction','Datasets', 'GDP', 'Movies','Survey']
pages = ['Introduction', 'Datasets', 'GDP', 'Movies','Survey']


styles = {
    "nav": {
        "background-color": "transparent",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "color": "#4CAF50",
        "font-family": "Tahoma, sans-serif",
        "margin": "0, 0.125rem",
        "padding": "0.4375rem 0.625rem",
        "border-left" : "1px solid #fff",
        "border-top" : "1px solid #fff",
        "border-right": "1px solid #848484",
        "border-bottom": "1px solid #848484",
        "background-color": "transparent",
        "padding": "3px 15px 3px 15px"
    },
    "active": {
        "border-right" : "1px solid #fff",
        "border-bottom": "1px solid #fff",
        "border-left": "1px solid #848484",
        "border-top": "1px solid #848484",
    },
    "hover": {
        "background-color": "transparent",
    },
    "img": {
        "position": "absolute",
        "left": "-20px",
        "font-size":"15px",
        "top":"4px",
        "width":"100px",
        "height":"40px",
    },
}

options = {
    "show_menu":False,
    "show_sidebar":True,
}

page = st_navbar(pages, styles=styles,logo_path=logo_path,options=options )

if page == 'Introduction':
    Introduction.Introduction().app()
elif page == 'Datasets':
    Datasets.Datasets().app()
elif page == 'GDP':
    GDP.GDP().app()
elif page == 'Movies':
    Movies.Movies().app()
elif page == 'Survey':
    Survey.Survey().app()
else:
    Introduction.Introduction().app()


