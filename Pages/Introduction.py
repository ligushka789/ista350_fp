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

        # create lottie_anim1 and give it json url
        lottie_anim1 = load_lottieurl("https://lottie.host/ef0d69e7-85c3-41d5-9def-d76e9d129876/f6hH1U5edi.json")

        # Create two columns
        left_column, right_column = st.columns([5, 3])

        # left column for intro
        with left_column:
            st.title("Introduction to the Project")
            st.write("---")
            st.write(
                """
                This project is aimed at expanding our understanding in dataframe analysis.
                For this module, our group of three have created different visualizations through the use of
                libraries that have been explored during ISTA 131 course, such as:

                - Pandas
                - Matplotlib
                - Numpy

                As well as auxiliary required libraries:

                - Streamlit
                """
            )
            st.write("---")
            st.subheader("Used Environment")
            st.write(
                """
                In order to offer the easier perception of our visualizations, we've
                decided to use the Streamlit framework, which allowed us to organize
                our work through the use of several pages, one for every member of
                our team.
                """
            )
            st.write("---")
            st.subheader("Repository Information")
            st.write(
                """
                If you wish to review the structure of the content as well as
                check the sequence of our Git actions, you can visit our GitHub
                repository at:
                """
            )
            st.write("[GitHub link >](https://github.com/ligushka789/ista131_Fp)")

        # right column for video player and animation
        with right_column:
            st.subheader("Choose Presentation to Watch:")
            video_gribanov = "https://youtu.be/Bel9mRRAPGs"
            video_babayev = "https://youtu.be/eHVcVcBw0aE"
            video_yeremenko = "https://youtu.be/7FJayrjoWrA"
            video_in_details = "https://youtu.be/_HRJL-q603A"

            # buttons for presentations

            if st.button("Gribanov"):
                st.video(video_gribanov)

            if st.button("Babayev"):
                st.video(video_babayev)

            if st.button("Yeremenko"):
                st.video(video_yeremenko)

            if st.button("In details"):
                st.video(video_in_details)

            #add lottie_anim1
            if lottie_anim1:
                st_lottie(lottie_anim1, height=300, key="coding")

        # styles part
        st.markdown(
            """
            <style>
            h1 {
                color: #4CAF50;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
