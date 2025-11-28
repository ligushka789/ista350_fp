import streamlit as st
import requests
from streamlit_lottie import st_lottie


class Introduction:
    def __init__(self):
        pass

    def app(self):
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        # Load lottie animation
        lottie_anim1 = load_lottieurl(
            "https://lottie.host/5c61b851-415c-4b94-bf48-782f7b4ef514/JzXkesEiLo.json"
        )

        # CENTER CONTAINER (only title)
        st.markdown("""
        <div style="max-width: 900px; margin: auto;">
        """, unsafe_allow_html=True)

        # Title centered
        st.markdown("<h1 style='text-align:center;'>Introduction to the Project</h1>", unsafe_allow_html=True)
        st.write("---")

        # Content LEFT aligned
        st.markdown("<div style='text-align:left;'>", unsafe_allow_html=True)

        st.write("""
        This project is aimed at expanding our understanding in webscraping and visualization.
        For this module, our group of two have created different visualizations through the use of
        libraries that have been explored during ISTA 350 course, such as:

        - Pandas
        - Matplotlib
        - Beautiful Soup
        - Webscraping technologies

        As well as auxiliary required libraries:

        - Streamlit (as a main framework to host our project)
        """)

        st.write("---")
        st.subheader("Used Environment")
        st.write("""
        In order to offer the easier perception of our visualizations, we've
        decided to use the Streamlit framework, which allowed us to organize
        our work through the use of several pages.
        """)

        st.write("---")
        st.subheader("Repository Information")
        st.write("""
        If you wish to review the structure of the content as well as
        check the sequence of our Git actions, you can visit our GitHub
        repository at:
        """)

        st.markdown("[GitHub link >](https://github.com/ligushka789/ista350_fp)")

        # Animation remains centered
        if lottie_anim1:
            st.markdown("<div style='text-align:center; margin-top:20px;'>", unsafe_allow_html=True)
            st_lottie(lottie_anim1, height=280, key="coding")
            st.markdown("</div>", unsafe_allow_html=True)

        # CLOSE LEFT ALIGN & MAIN CONTAINER
        st.markdown("</div></div>", unsafe_allow_html=True)

        # STYLE
        st.markdown("""
        <style>
        h1 {
            font-family: Tahoma, Arial, sans-serif;
            font-size: 30px;
            text-align: center;
            color: #fdffff;
        }

        h2, h3 {
            font-family: Tahoma;
            color: #fdffff;
        }

        p, li {
            color: #fdffff;
            font-family: Tahoma;
        }

        a {
            color: #00ccff;
            font-weight: bold;
            text-decoration: none;
        }

        a:hover {
            color: #ffffff;
            text-decoration: underline;
        }
        </style>
        """, unsafe_allow_html=True)
