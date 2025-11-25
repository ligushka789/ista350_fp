import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
from streamlit_lottie import st_lottie
import streamlit as st

# Made by ROMAN AND PAVEL
class Life_expectancy:
    def __init__(self):
        pass

    def app(self):
        st.title("Life Expectancy Analysis")
        st.subheader("Healthcare Quality → Life Expectancy")

        # Lottie loader
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_anim1 = load_lottieurl(
            "https://lottie.host/474d5a43-b87f-43e5-b72b-fdbdef03d27f/Z6mnyA4rw5.json"
        )

        # Load data
        def load_default_data():
            df = pd.read_csv("csv/life_expectancy.csv")
            df.columns = df.columns.str.strip()
            return df

        df = load_default_data()

        # Show dataset
        st.dataframe(df, height=400, width=600)

        # ============================
        # ADD IMAGES
        # ============================
        st.subheader("Reference Images")
        st.image("img/1.jpg", caption="UN Life Expectancy Table", use_container_width=True)
        st.image("img/2.jpg", caption="Numbeo Healthcare Index Map/Table", use_container_width=True)

        # ============================
        # BEST VISUALIZATION: BINNED BAR CHART
        # ============================
        st.subheader("Life Expectancy by Healthcare Index Groups")

        if st.button("Show Clean Bar Chart"):
            if "Healthcare_Index" not in df.columns or "All" not in df.columns:
                st.error("Dataset must contain 'Healthcare_Index' and 'All'")
            else:

                # Create bins for Healthcare Index
                bins = [30, 40, 50, 60, 70, 80, 90]
                labels = ["30–40", "40–50", "50–60", "60–70", "70–80", "80–90"]

                df["HC_Group"] = pd.cut(df["Healthcare_Index"], bins=bins, labels=labels)

                # Compute mean Life Expectancy for each HC range
                grouped = df.groupby("HC_Group")["All"].mean().reset_index()

                fig, ax = plt.subplots(figsize=(10, 6))

                ax.bar(grouped["HC_Group"], grouped["All"], color="skyblue", edgecolor="black")

                # Add values above bars
                for i, v in enumerate(grouped["All"]):
                    ax.text(i, v + 0.5, f"{v:.1f}", ha="center", fontsize=10)

                ax.set_xlabel("Healthcare Index Groups")
                ax.set_ylabel("Average Life Expectancy (Years)")
                ax.set_title("Higher Healthcare Index → Higher Life Expectancy (Clean Comparison)")

                st.pyplot(fig)

        # Optional Lottie animation
        st_lottie(lottie_anim1, height=200, key="lottie1")

        # Style
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


# Run the app
if __name__ == "__main__":
    app = Life_expectancy()
    app.app()