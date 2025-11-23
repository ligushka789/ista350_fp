import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
from streamlit_lottie import st_lottie

#Made by Ruslan Babayev
class GDP:
    def __init__(self):
        pass

    def app(self):
        st.title('GDP')
        st.subheader("""
                                     This dataset is aimed to compare the gross domestic product
                                     of four states: California, New Mexico, Arizona and Texas.
                                     That information could be beneficial for the comparison of
                                     economic growth for different regions of the country, which would
                                     let us indicate the difference of economic situation.
                                      

                                     """)
        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()

        lottie_anim1 = load_lottieurl("https://lottie.host/474d5a43-b87f-43e5-b72b-fdbdef03d27f/Z6mnyA4rw5.json")

        # Function to load default data
        def load_default_data():
            file_path = 'csv/USA_GDP_dataset_updated.csv'
            data = pd.read_csv(file_path)
            data.columns = data.columns.str.strip()  # Clean column names
            return data

        # Load the dataset
        df = load_default_data()

        # Display the dataset
        st.dataframe(df, height=400, width=600)

        # Simplified labels for Y-axis options
        simplified_labels = {
            "GDP": ["AZ GDP (Billions of US $)", "CA GDP (Billions of US $)",
                    "TX GDP (Billions of US $)", "NM GDP (Billions of US $)"],
            "Per Capita": ["AZ Per Capita (US $)", "CA Per Capita (US $)",
                           "TX Per Capita (US $)", "NM Per Capita (US $)"],
            "Annual Change": ["AZ Annual % Change", "CA Annual % Change",
                              "TX Annual % Change", "NM Annual % Change"]
        }

        # Dropdown for selecting X-axis and Y-axis
        x_axis = st.selectbox("Select X-axis", ["Date"])  # X-axis is fixed to Date
        y_axis_label = st.selectbox("Select Y-axis", list(simplified_labels.keys()))  # Y-axis simplified options

        if st.button("Generate Graph"):
            if x_axis and y_axis_label:
                # Retrieve the actual column names for the selected Y-axis option
                y_axis_columns = simplified_labels[y_axis_label]

                # Define colors for each state
                state_colors = {
                    "AZ GDP (Billions of US $)": "red",
                    "CA GDP (Billions of US $)": "blue",
                    "TX GDP (Billions of US $)": "yellow",
                    "NM GDP (Billions of US $)": "green",
                    "AZ Per Capita (US $)": "red",
                    "CA Per Capita (US $)": "blue",
                    "TX Per Capita (US $)": "yellow",
                    "NM Per Capita (US $)": "green",
                    "AZ Annual % Change": "red",
                    "CA Annual % Change": "blue",
                    "TX Annual % Change": "yellow",
                    "NM Annual % Change": "green"
                }

                # Plot the graph
                fig, ax = plt.subplots()
                for column in y_axis_columns:
                    # Handle missing data by filling NaN values with zeros
                    cleaned_data = df[column].fillna(0)  # Or use .dropna() to exclude missing values
                    ax.plot(df["Date"], cleaned_data, marker='o', linestyle='-',
                            color=state_colors[column], label=column.split(" ")[0])  # Extract state name for the legend

                ax.set_xlabel("Date")
                ax.set_ylabel(y_axis_label)
                ax.set_title(f"{y_axis_label} vs Date for All States")
                ax.legend(title='States')

                # Rotate x-axis labels for readability
                plt.xticks(rotation=90)
                st.pyplot(fig)
            else:
                st.warning("Please select both X-axis and Y-axis options.")


        st_lottie(lottie_anim1, height=200, key="")
        # Style customization
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
            unsafe_allow_html=True
        )


# Run the app
if __name__ == "__main__":
    app = GDP()
    app.app()