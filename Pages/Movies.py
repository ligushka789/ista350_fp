import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Made by Pavel Yeremenko
class Movies:
    def __init__(self):
        pass

    def app(self):
        st.title("Movies")
        st.subheader("""
                     This dataset is aimed to fulfill my interest in the success of a movie
                     based on its characteristics such as: budget, runtime and the year of release.
                     
                     With the scatter plot and the regression line I'll be able to figure out if the movie's
                     success rises as budget increases, are longer movies really better than the short ones 
                     and if the best movies were really made in the 1990s.                                 
                     """)

        # Get the csv
        smoko = "csv/tmdb_5000_movies_rfw.csv"  #csv files folder
        try:
            df = pd.read_csv(smoko)
        except FileNotFoundError:
            st.error(f"Static file '{smoko}' not found. Please check the file path.") #if error with file occurs
            return

        #The slider
        st.subheader("View the dataset")
        row_range = st.slider("Select range of rows to display(affects the scatter plot):", 0, len(df) - 1, (0, 10))
        selected_rows = df.iloc[row_range[0]:row_range[1] + 1]
        st.dataframe(selected_rows, height=400, width=600)

        st.subheader("Movies scatter plot: Regression line edition")     #the plot name
        #limit the axis to the value
        x_axis_choices = ["runtime", "release_date"]
        x_col = st.selectbox("Select X-axis column", x_axis_choices)

        #limit the axis to the value #2
        y_axis_choices = ["vote_average", "budget", "vote_count"]
        y_col = st.selectbox("Select Y-axis column", y_axis_choices)
        #streamlit button
        if st.button("Generate Scatter Plot"):
            if x_col in selected_rows.columns and y_col in selected_rows.columns:
                x = selected_rows[x_col].dropna()
                y = selected_rows[y_col].dropna()
                if x_col == "release_date":
                    x = pd.to_datetime(x, errors='coerce').dropna()
                # check the endpoints
                min_length = min(len(x), len(y))
                x, y = x[:min_length], y[:min_length]

                # regression line with lambda function thx to stackoferflow
                if x_col == "release_date":
                    # Convert dates to ordinal values for regression
                    x_ordinal = x.apply(lambda date: date.toordinal())
                else:
                    x_ordinal = x
                coefficients = np.polyfit(x_ordinal, y, 1)
                regression_line = np.polyval(coefficients, x_ordinal)

                #Plot the graph (scatter plot)
                fig, ax = plt.subplots()
                ax.scatter(x, y, color='blue', alpha=0.5, label="Data Points")
                ax.plot(x, regression_line, color='red', label="Regression Line")
                ax.set_xlabel(x_col)
                ax.set_ylabel(y_col)
                ax.set_title(f"Scatter Plot: {y_col} vs {x_col}")
                ax.legend()
                ax.grid()
                if x_col == "release_date":
                    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%Y-%m-%d'))
                    plt.xticks(rotation=45)

                st.pyplot(fig)
            else:
                st.warning("The selected columns are not valid for plotting.")

        st.image("img/mmp.png")

        # ------------------------STYLES------------------------


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
    app = Movies()
    app.app()
