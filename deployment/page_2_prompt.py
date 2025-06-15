import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import page_1_prompt as p1

if __name__ == "__main__":
    # Heading
    st.title('Displaying the stats of the 5 NBA leaders for X category')

    # extracting the data
    df_stats = p1.extract_data()

    # getting user input
    stats = st.multiselect('Stats', df_stats.drop(['name'], axis=1).columns)

    #Data preparation
    playersAvg = p1.prepare_data(df_stats)

    # Using the cleaned data from prompt 1 to create tables of leaders for each requested category
    for category in stats:
        statsSorted = playersAvg.sort_values(category, ascending=False)
        st.markdown("Top 5  " + category + " players in the NBA:")
        st.dataframe(statsSorted.head())
        st.markdown("")
