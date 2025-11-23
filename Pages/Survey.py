import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Made by Roman Gribanov
class Survey:
    def __init__(self):
        pass

    def app(self):
        st.title("Survey Data Analysis")
        st.subheader("""
                             This dataset is aimed to see 
                             The interdependence of employment in a
                             technical company and the subsequent consequences for mental health.
                             For the purity of stats, survey was taken from 5 countries
                             USA, Canada, Australia, France, the United Kingdom,
                             looking first at the stats of people from the survey who consider the presence
                             or absence of mental problems and their employment in a tech company.
                             Also, a chart with gender is needed for optional information.
                             
                             
                             View the dataset: 
                                
                             """)

        def load_default_data():                        #File Reader
            file_path = "csv/survey1.csv"
            data = pd.read_csv(file_path)
            return data

        df = load_default_data()            #Get csv file as dataframe

        st.subheader("Dataset Preview")                     #Header and visualization of dataframe
        st.dataframe(df, height=400, width=600)             #with streamlit library


        st.subheader("Filter and Visualize Categories")             # Just a sub header to separate dataset and graphs part

        allowed_categories = ["mental_health_consequence", "tech_company", "Gender"]        #we are interested only in these columns
        y_axis = st.selectbox("Select a Category for Y-axis", options=allowed_categories)       #st.selectbox which allow us to create box with categories
        selected_countries = ["United States", "Australia", "Canada", "United Kingdom", "France"] #that's x-axis, we need only these countries
        filtered_data = df[df["Country"].isin(selected_countries)]      # that stuff add it in dataframe
        filtered_data_gender = filtered_data[filtered_data['Gender'].isin(['male', 'female'])]      #from gender category we want to show only male and female genders

        if st.button("Generate Graph"):         #if button was clicked it begin the proccess of creating it
            if y_axis:
                if y_axis not in filtered_data.columns:                             # just check for the errors does columns even exist.
                    st.error(f"Selected category '{y_axis}' does not exist in the dataset.")
                else:
                    fig, ax = plt.subplots(figsize=(12, 6))     #create bars and inner part of the graph with fixed size
                    grouped_data = filtered_data_gender.groupby("Country")[y_axis].value_counts(normalize=True).unstack(
                        fill_value=0) * 100                     # there are a few things. first of all creating y axis by chosen category,
                                                                # get the frequency and change it to percentage
                    bar_width = 0.2
                    x_positions = np.arange(len(selected_countries))            #create a massive for each yes/no/maybe(just for instance)

                    for i, response in enumerate(grouped_data.columns):         #for each thing from grouped data created its own bar
                        ax.bar(x_positions + i * bar_width, grouped_data[response], width=bar_width,
                               label=f"{y_axis}: {response}")

                    ax.set_xlabel("Country")                    #I think this part is clear
                    ax.set_ylabel("Percentage")
                    ax.set_title(f"Distribution of {y_axis} by Country")
                    ax.set_xticks(x_positions + bar_width * (len(grouped_data.columns) - 1) / 2)
                    ax.set_xticklabels(selected_countries, rotation=45, ha='right')
                    ax.legend(title="Categories", bbox_to_anchor=(1.05, 1), loc="upper left")
                    st.pyplot(fig)
            else:
                st.warning("Please select a category for Y-axis.")              #if category was not chosen for some reason

        # just a style part
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

#it launches our project
if __name__ == '__main__':
    Survey= Survey()
    Survey.app()

