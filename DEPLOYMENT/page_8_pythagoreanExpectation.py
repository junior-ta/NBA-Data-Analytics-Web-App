import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import statsmodels.formula.api as smf
import streamlit as st

gamesData=pd.read_csv(r"C:\Users\ttjrb\OneDrive\Desktop\University Important\summer 2024 work\projects\databases\ALL 1320 nba games 2022-23\games.csv")

def preparing_data(data):
    data = data[['home', 'away', 'h_pts', 'a_pts', 'date']]
    data = data.rename(columns={'home': 'h_team', 'away': 'a_team'})

    data['h_win'] = 0
    for i in range(len(data['h_pts'])):
        if data['h_pts'].iloc[i] > data['a_pts'].iloc[i]:
            data.iloc[i, 5] = 1

    data['a_win'] = np.where(data['h_pts'] < data['a_pts'], 1, 0)

    data['count'] = 1

    # performance of teams at home
    home = data.groupby('h_team')[['h_win', 'h_pts', 'a_pts', 'count']].sum().reset_index()
    home = home.rename(columns={'h_team': 'team', 'h_pts': 'pts_h', 'a_pts': 'opp_pts_h', 'count': 'h_games'})


    # performance of teams on the road
    away = data.groupby('a_team')[['a_win', 'h_pts', 'a_pts', 'count']].sum().reset_index()
    away = away.rename(columns={'a_team': 'team', 'h_pts': 'opp_pts_a', 'a_pts': 'pts_a', 'count': 'a_games'})

    # merging for each team
    df = pd.merge(home, away, on='team')

    return df


def pythagoreanExp_calculation(data):
    data['wins'] = data['h_win'] + data['a_win']
    data['games_played'] = data['h_games'] + data['a_games']
    data['pts_scored'] = data['pts_h'] + data['pts_a']
    data['pts_opp'] = data['opp_pts_h'] + data['opp_pts_a']

    # defining win% and pythagorean expectation
    data['win%'] = data['wins'] / data['games_played']
    data['p_expectation'] = data['pts_scored'] ** 2 / (data['pts_scored'] ** 2 + data['pts_opp'] ** 2)

    return data


if __name__ == '__main__':
    # Heading
    st.title('Pythagorean expectation of teams in 2022/23')

    # preparing the data
    df = preparing_data(gamesData)

    #calculating win% and pyth expec...
    df=pythagoreanExp_calculation(df)

    st.markdown("The expected performance of a team over a season is given by the formula:")
    st.latex(r"""
    \frac{\left(\text{pts scored}\right)^2}
    {\left(\text{pts scored}\right)^2 + \left(\text{opponents pts}\right)^2}
    """)

    st.markdown("This should be approximately equal to the win% of the team for the entire season.")

    #plotting my linear correlation plot
    st.markdown("")
    st.pyplot(sns.relplot(x='p_expectation', y='win%', data=df))

    #creating a regression analysis
    df.rename(columns={'win%': 'win_percent'}, inplace=True)
    pyth_lm = smf.ols(formula='win_percent~p_expectation', data=df).fit()
    st.markdown("")
    st.subheader("Regression results")
    st.write(pyth_lm.summary())

    #my analysis


