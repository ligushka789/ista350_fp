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

        # --------------------
        # LOTTIE
        # --------------------
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_anim1 = load_lottieurl(
            "https://lottie.host/474d5a43-b87f-43e5-b72b-fdbdef03d27f/Z6mnyA4rw5.json"
        )

        # --------------------
        # LOAD DATA
        # --------------------
        def load_default_data():
            df = pd.read_csv("csv/life_expectancy.csv")
            df.columns = df.columns.str.strip()
            return df

        df = load_default_data()

        st.subheader("Dataset Preview")
        st.dataframe(df, height=400, use_container_width=True)

        # --------------------
        # IMAGES
        # --------------------
        st.subheader("Reference Images")
        st.image("img/1.jpg", caption="UN Life Expectancy Table", use_container_width=True)
        st.image("img/2.jpg", caption="Numbeo Healthcare Index Map/Table", use_container_width=True)

        # -------------------------------------
        # REGION MAP (GLOBAL, ONE TIME)
        # -------------------------------------
        region_map = {
            "Japan": "Asia", "South Korea": "Asia", "Singapore": "Asia", "Taiwan": "Asia",
            "China": "Asia", "India": "Asia", "Thailand": "Asia", "Malaysia": "Asia",

            "France": "Europe", "Germany": "Europe", "Italy": "Europe",
            "Spain": "Europe", "Norway": "Europe", "Sweden": "Europe",
            "Finland": "Europe", "Netherlands": "Europe", "Denmark": "Europe",
            "United Kingdom": "Europe", "UK": "Europe",
            "Switzerland": "Europe", "Ireland": "Europe", "Belgium": "Europe",

            "USA": "North America", "United States": "North America",
            "Canada": "North America", "Mexico": "North America",

            "Brazil": "South America", "Argentina": "South America", "Chile": "South America",

            "Australia": "Oceania", "New Zealand": "Oceania",

            "Israel": "Middle East", "Saudi Arabia": "Middle East", "UAE": "Middle East",

            "South Africa": "Africa", "Egypt": "Africa", "Nigeria": "Africa"
        }

        # Assign regions once
        df["Region"] = df["Country"].map(region_map)
        df_clean = df.dropna(subset=["Region"])

        # --------------------
        # COLORS
        # --------------------
        region_colors = {
            "Europe": "royalblue",
            "Asia": "crimson",
            "North America": "mediumseagreen",
            "South America": "purple",
            "Oceania": "cyan",
            "Middle East": "saddlebrown",
            "Africa": "darkorange"
        }

        # ============================
        # FIRST GRAPH — SCATTER + TREND
        # ============================
        st.subheader("Scatter Plot: Life Expectancy vs Healthcare Index (Colored by Region)")

        if st.button("Show Scatter Plot with Regions"):
            if "Healthcare_Index" not in df.columns or "All" not in df.columns:
                st.error("Dataset must contain 'Healthcare_Index' and 'All'")
            else:

                x = df_clean["Healthcare_Index"]
                y = df_clean["All"]

                # Regression line
                m, b = np.polyfit(x, y, 1)
                reg_x = np.linspace(x.min(), x.max(), 200)

                fig, ax = plt.subplots(figsize=(11, 7))

                # Scatter by region
                for region in df_clean["Region"].unique():
                    sub = df_clean[df_clean["Region"] == region]
                    ax.scatter(
                        sub["Healthcare_Index"],
                        sub["All"],
                        s=90,
                        color=region_colors[region],
                        edgecolors="black",
                        alpha=0.85,
                        label=region
                    )

                # Trend line
                ax.plot(reg_x, m * reg_x + b, color="red", linewidth=3, label="Trend Line")

                ax.set_xlabel("Healthcare Index (Higher = Better Medicine)")
                ax.set_ylabel("Life Expectancy (Years)")
                ax.set_title("Life Expectancy vs Healthcare Quality (Regions + Trend Line)")
                ax.grid(alpha=0.3)
                ax.legend(title="Region")

                st.pyplot(fig)

                st.success("""
                Each dot represents a country.

                The red line is the **global trend** showing that as healthcare quality increases,
                life expectancy also increases.

                Regions show strong clustering:
                • Europe and Asia concentrate at the top
                • Africa is lower and more spread
                • North America is high but not dominant

                This confirms a strong global relationship between healthcare systems and lifespan.
                """)

        # ============================
        # SECOND GRAPH — BOXPLOT
        # ============================
        st.subheader("Life Expectancy Distribution by Region")

        if st.button("Show Regional Boxplot"):
            fig2, ax2 = plt.subplots(figsize=(11, 6))

            regions = df_clean["Region"].unique()
            data = [df_clean[df_clean["Region"] == r]["All"] for r in regions]

            ax2.boxplot(data, tick_labels=regions, patch_artist=True)

            ax2.set_xlabel("Region")
            ax2.set_ylabel("Life Expectancy (Years)")
            ax2.set_title("Life Expectancy Distribution by Region")
            ax2.grid(alpha=0.3)

            st.pyplot(fig2)

            st.success("""
            This boxplot shows:
            • The median life expectancy per region
            • How spread out countries are inside regions
            • Which regions have the biggest inequality

            Combined with the scatter plot, it proves:
            Not only does healthcare matter,
            BUT it also shapes inequality between whole regions.
            """)

        # --------------------
        # LOTTIE
        # --------------------
        st_lottie(lottie_anim1, height=200, key="lottie1")

        # --------------------
        # STYLE
        # --------------------
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


# Run
if __name__ == "__main__":
    Life_expectancy().app()
