import pandas as pd
import csv
import matplotlib.pyplot as plt
import streamlit as st

dataGames = pd.read_csv(r"database/games.csv")

#Getting the data from basketball reference
def extract_prepare_data(data):


    # finding out each unique team that played in the NBA
    teams = data['home'].unique()
    teamsRecordsList = []

    # iterating through every team
    for team in teams:
        teamRecord = {}
        # extracting Home games results
        df1 = data[data['home'] == team]
        homeWin = 0
        homeLoss = 0
        for i in range(len(df1)):
            if df1['h_pts'].iloc[i] > df1['a_pts'].iloc[i]:
                homeWin += 1
            else:
                homeLoss += 1

        # extracting Away games results
        df2 = data[data['away'] == team]
        awayWin = 0
        awayLoss = 0
        for i in range(len(df2)):
            if df2['h_pts'].iloc[i] < df2['a_pts'].iloc[i]:
                awayWin += 1
            else:
                awayLoss += 1

        # creating the team record dictionary and adding it my final list of teams' records
        teamRecord['name'] = team
        teamRecord['homeWin'] = homeWin
        teamRecord['awayWin'] = awayWin
        teamRecord['totalWins'] = homeWin + awayWin
        teamRecord['homeLoss'] = homeLoss
        teamRecord['awayLoss'] = awayLoss
        teamRecord['totalLosses'] = homeLoss + awayLoss

        teamsRecordsList.append(teamRecord)

    # creating a data frame with teams and their records
    teamsRecords = pd.DataFrame(teamsRecordsList)

    return  teamsRecords

if __name__ == '__main__':
    # Heading
    st.title('Teams rankings with home and away splits')

    teamsRecords= extract_prepare_data(dataGames)

    bar= st.button('Bar chart(H)', help="display team rankings as a horizontal bar chart")
    table= st.button('Table', help="display team rankings as a table of records")

    if table:
        st.dataframe(teamsRecords.set_index('name').sort_values('totalWins', ascending=False), height=1085)

    if bar:
        topk = teamsRecords.sort_values('totalWins', ascending=False)

        plt.barh(topk['name'], topk['totalWins'])
        plt.ylabel('teams')
        plt.xlabel('wins')
        plt.title('Top teams in the NBA')
        plt.gca().invert_yaxis()
        st.pyplot(plt)


    if not bar and not table:
        for i in range(5):
            st.markdown("")

        st.markdown("PICK ONE OPTION BY CLICKING ON THE BUTTONS")

