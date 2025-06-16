import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st

@st.cache_data
def preparing_data():
    data = pd.read_csv(r"database/games.csv")

    data = data[['home', 'away', 'h_pts', 'a_pts', 'date']]
    data = data.rename(columns={'home': 'h_team', 'away': 'a_team'})


    # adding columns to specify whch team won
    data['h_win'] = np.where(data['h_pts'] > data['a_pts'], 1, 0)
    data['a_win'] = np.where(data['h_pts'] < data['a_pts'], 1, 0)

    data['count'] = 1


    # splitting home games and away games for every team
    home = data[['h_team', 'h_pts', 'a_pts', 'h_win', 'count', 'date']]
    home = home.rename(columns={'h_team': 'team', 'h_pts': 'pts', 'h_win': 'win', 'a_pts': 'opp_pts'})
    away = data[['a_team', 'a_pts', 'h_pts', 'a_win', 'count', 'date']]
    away = away.rename(columns={'a_team': 'team', 'a_pts': 'pts', 'a_win': 'win', 'h_pts': 'opp_pts'})


    # concatenating home and away, meaning that one game is in the table 2 times (both for the home and the away team)
    Data = pd.concat([home, away])

    # parsing the dates to split the season in 2
    Data['date'] = np.where(Data['date'].notna(),
                            Data['date'].str[0:4] + Data['date'].str[5:7] + Data['date'].str[8:10], 0)

    # converting dates to numeric
    Data['date'] = pd.to_numeric(Data['date'], errors='coerce').fillna(0).astype(int)


    # Splitting the regular season into before and after the all star break

    half1 = Data[Data['date'] < 20230219]
    half2 = Data[Data['date'] > 20230219]

    # Half1 teams records and totals, win % and pythogorean expectation

    half1 = half1.groupby('team')[['win', 'pts', 'opp_pts', 'count']].sum().reset_index()
    half1['win_perc'] = half1['win'] / half1['count']
    half1['p_expectation'] = half1['pts'] ** 2 / (half1['pts'] ** 2 + half1['opp_pts'] ** 2)

    # Half2 teams records and totals, win % and pythogorean expectation

    half2 = half2.groupby('team')[['win', 'pts', 'opp_pts', 'count']].sum().reset_index()
    half2['win_perc'] = half2['win'] / half2['count']
    half2['p_expectation'] = half2['pts'] ** 2 / (half2['pts'] ** 2 + half2['opp_pts'] ** 2)

    predictor = pd.merge(half1, half2, on='team')
    predictor = predictor[['team', 'win_perc_x', 'p_expectation_x', 'win_perc_y', 'p_expectation_y']]
    predictor = predictor.rename(
        columns={'win_perc_x': 'win_perc1st', 'p_expectation_x': 'p_expectation1st', 'win_perc_y': 'win_perc2nd',
                 'p_expectation_y': 'p_expectation2nd'})

    return predictor


if __name__ == '__main__':
    # Heading
    st.title('Using Pythagorean Prediction to predict the second half of the season in 2022/23')

    predictor= preparing_data()

    PE, WN = st.columns(2)

    with PE:
        st.markdown("")
        st.markdown("Plot:")
        st.subheader("Pythagorean Expectation (calculated from results of the first half of the season) against Win% in the second half of the season" )
        # First, plot Pythagorean Expectation against win percentage in the second half of the season
        st.pyplot(sns.relplot(x="p_expectation1st", y="win_perc2nd", data=predictor))


    with WN:
        # Now, compare this with a plot of win percentage from the first half of the season against win percentage
        # in the second half of the season
        st.markdown("")
        st.markdown("Plot:")
        st.subheader("Win% of the first half of the season against Win% in the second half of the season")
        for i in range(4): #to align graphs
            st.markdown("")
        st.pyplot(sns.relplot(x="win_perc1st", y="win_perc2nd", data=predictor))


    #deeper comparison because both plots look really alike
    st.markdown("")
    st.markdown("""
    The two plots look similar, obviously, Win% and Pythagorean Expectation are good predictors.
    We can be more precise still if we compare the correlation coefficients. The first row of the table shows the
    correlation of win percentage in second half of the season against itself, win percentage in the first half of the season,
    Pythagorean Expectation in the first half of the season, and Pythagorean Expectation in the second half of the season.
    Our focus is on comparing the second and third columns.
    """)


    predictorPL = predictor[['win_perc2nd', 'win_perc1st', 'p_expectation1st', 'p_expectation2nd']]
    st.write(predictorPL.corr())


    for i in range(2):
        st.markdown("")
    st.subheader("The final dataframe btw!!!")
    st.dataframe(predictor.sort_values(by=['win_perc2nd'], ascending=False).set_index('team'))
