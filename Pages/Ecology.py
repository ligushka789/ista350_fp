import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Made by Pavel Yeremenko
class Ecology:
    def __init__(self):
        pass

    def app(self):
        st.title("Ecology Interest & Environmental Trend")
        st.subheader("""
            This graph shows how people's interest in ecology has changed over time
            (based on Google N-gram data), and how the general discussion of the
            environment evolved in parallel.

            The values have been rescaled for readability (mentions per 1 million words).
        """)

        # Load N-gram ecology dataset
        file_path = "csv/ngram_ecology_environment.csv"

        try:
            df = pd.read_csv(file_path)
        except FileNotFoundError:
            st.error(f"File not found: {file_path}")
            return

        st.subheader("Dataset Preview")
        st.dataframe(df, height=400)

        # Clean dataframe
        required_cols = {"year", "ecology", "environment"}
        if not required_cols.issubset(df.columns):
            st.error("CSV must contain columns: 'year', 'ecology', 'environment'")
            return

        # ============================
        # SCALE VALUES (IMPROVED VISIBILITY)
        # ecology is boosted ×10 more than environment
        # ============================
        df["environment_scaled"] = df["environment"] * 1_000_000
        df["ecology_scaled"] = df["ecology"] * 10_000_000   # stronger boost

        st.subheader("Ecology Interest vs. Environmental Discussion (Scaled)")

        if st.button("Generate Ecology Trend Graph"):
            fig, ax = plt.subplots(figsize=(12, 6))

            # ecology curve (boosted strongly)
            ax.plot(
                df["year"],
                df["ecology_scaled"],
                label="Ecology (boosted for visibility)",
                color="green",
                linewidth=2.8
            )

            # environment curve
            ax.plot(
                df["year"],
                df["environment_scaled"],
                label="Environment (mentions per 1M words)",
                color="blue",
                linewidth=2.5
            )

            ax.set_xlabel("Year", fontsize=12)
            ax.set_ylabel("Scaled Mentions", fontsize=12)
            ax.set_title("Ecology & Environment Interest Over Time (Boosted Visibility)", fontsize=16)

            ax.grid(alpha=0.3)
            ax.legend(fontsize=12)

            st.pyplot(fig)

        # Optional image
        st.image("img/mmp.png", caption="Ecology Concept Image", use_container_width=True)

        # Styles
        st.markdown("""
            <style>
            h1 {
                color: #4CAF50;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
        """, unsafe_allow_html=True)


# Run the app
if __name__ == "__main__":
    app = Ecology()
    app.app()