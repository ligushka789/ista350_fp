import streamlit as st
import pandas as pd

class Datasets:
    def __init__(self):
        pass
        #titles
    def app(self):
        st.title('Datasets')
        st.subheader("""    
                                  Datasets Page
                                  
                                  On this page, we can check any of datasets, which was used in 
                                  this project with any columns and values. Enjoy :)
                                    
                                    
                                    View the content
                                     """)

        datasets = {        # list of our datasets
            "life expectancy": "life_expectancy.csv",
            "ecology": "ngram_ecology_environment.csv",
            "releases": "releases_2024_detailed.csv"
        }

       # variable for name of dataset
        dataset_name = st.selectbox("Choose a dataset", list(datasets.keys()))

        # Get the corresponding file name based on the selected display name
        file_name = datasets[dataset_name]



        # function which load csv file
        def load_data(file_path):
            data = pd.read_csv(file_path)
            return data


        file_path = f"csv/{file_name}"
        df = load_data(file_path)

        if df is not None:
            st.dataframe(df, height=400, width=600)

            # choosing column for filter everything is in selectbox
            column = st.selectbox("Choose column for filter", df.columns)

            if column:
                unique_values = df[column].unique()
                selected_value = st.selectbox(f"Select a value for {column}", options=unique_values)

                # value for filter
                filtered_df = df[df[column] == selected_value]
                st.dataframe(filtered_df, height=400, width=600)
        else:
            st.warning("Could not load dataset")
            #styles part
        st.markdown("""
            <style>
            h1 {
                color: #4CAF50;
                font-size: 30px;
                text-align: center;
                font-family: Avantgarde, TeX Gyre Adventor, URW Gothic L, sans-serif;
            }
            </style>
        """, unsafe_allow_html=True)
