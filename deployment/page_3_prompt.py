import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

@st.cache_data
def extract_prepare_data():
    data = pd.read_csv(r"database/games.csv")

    data = data[['home', 'away', 'h_pts', 'a_pts', 'date']]
    data = data.rename(columns={'home': 'h_team', 'away': 'a_team'})

    # adding columns to specify which team won
    data['homeWin'] = np.where(data['h_pts'] > data['a_pts'], 1, 0)
    data['awayWin'] = np.where(data['h_pts'] < data['a_pts'], 1, 0)

    data['count'] = 1

    home = data.groupby('h_team')[['homeWin', 'count']].sum()
    home['homeLost'] = home['count'] - home['homeWin']
    home = home.drop(['count'], axis=1).reset_index().rename(columns={'h_team': 'team'})
    away = data.groupby('a_team')[['awayWin', 'count']].sum()
    away['awayLost'] = away['count'] - away['awayWin']
    away = away.drop(['count'], axis=1).reset_index().rename(columns={'a_team': 'team'})

    teamRecords = pd.merge(home, away, on="team")
    teamRecords['totalWins'] = teamRecords['homeWin'] + teamRecords['awayWin']
    teamRecords['totalLosts'] = teamRecords['homeLost'] + teamRecords['awayLost']

    return teamRecords

if __name__ == '__main__':
    # Heading
    st.title('Teams rankings with home and away splits')

    teamsRecords= extract_prepare_data()

    bar= st.button('Bar chart(H)', help="display team rankings as a horizontal bar chart")
    table= st.button('Table', help="display team rankings as a table of records")

    if table:
        st.dataframe(teamsRecords.set_index('team').sort_values('totalWins', ascending=False), height=1085)

    if bar:
        topk = teamsRecords.sort_values('totalWins', ascending=False)

        plt.barh(topk['team'], topk['totalWins'])
        plt.ylabel('teams')
        plt.xlabel('wins')
        plt.title('Top teams in the NBA')
        plt.gca().invert_yaxis()
        st.pyplot(plt)


    if not bar and not table:
        for i in range(5):
            st.markdown("")

        st.markdown("PICK ONE OPTION BY CLICKING ON THE BUTTONS")

