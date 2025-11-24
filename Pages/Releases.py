import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class Releases:
    def __init__(self):
        pass

    def app(self):
        st.title("Music Releases — Friday Success Analysis")
        st.subheader("""
            Do releases dropped on Friday tend to be more successful?
            Measured using the UserScore. Below is a clean & clear bar chart comparing
            average scores across days of the week.
        """)

        @st.cache_data
        def load_data():
            file_path = "csv/releases_2024_detailed.csv"
            return pd.read_csv(file_path)

        df = load_data()

        st.subheader("Dataset Preview")
        st.dataframe(df, height=400)

        # ----- Check required columns -----
        required_cols = {"Weekday", "UserScore"}
        if not required_cols.issubset(df.columns):
            st.error("Dataset must contain 'Weekday' and 'UserScore' columns.")
            return

        # ----- Normalize weekday order -----
        weekday_order = [
            "Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"
        ]

        df = df[df["Weekday"].isin(weekday_order)]
        df["Weekday"] = pd.Categorical(df["Weekday"], categories=weekday_order, ordered=True)

        # ============================
        # BAR CHART — Average Score by Weekday
        # ============================
        st.subheader("Average UserScore by Weekday")

        # Compute average UserScore by weekday
        weekday_avg = df.groupby("Weekday")["UserScore"].mean().reindex(weekday_order)

        # Color Friday differently
        colors = ["orange" if day == "Friday" else "skyblue" for day in weekday_avg.index]

        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(weekday_avg.index, weekday_avg.values, color=colors, edgecolor="black")

        # Add numeric value labels
        for i, v in enumerate(weekday_avg.values):
            ax.text(i, v + 0.1, f"{v:.2f}", ha="center", fontsize=10)

        ax.set_xlabel("Weekday")
        ax.set_ylabel("Average UserScore")
        ax.set_title("Average UserScore by Weekday — Friday Highlighted")
        ax.grid(axis="y", linestyle="--", alpha=0.3)

        st.pyplot(fig)

        # ============================
        # SUMMARY
        # ============================
        friday_avg = weekday_avg["Friday"]
        other_avg = weekday_avg.drop("Friday").mean()

        st.subheader("Statistical Summary")
        st.write(f"**Average UserScore (Friday):** {friday_avg:.2f}")
        st.write(f"**Average UserScore (Other days):** {other_avg:.2f}")

        if friday_avg > other_avg:
            st.success("Friday releases ARE more successful on average! 🎉")
        else:
            st.warning("Friday releases do NOT appear to be more successful.")

# Run
if __name__ == '__main__':
    Releases().app()
