import pandas as pd
import csv
import matplotlib.pyplot as plt
import streamlit as st

@st.cache_data
def process_data():
    data = pd.read_csv(r"C:\Users\ttjrb\OneDrive\Desktop\University Important\summer 2024 work\projects\databases\ALL 1320 nba games 2022-23\matchups.csv")

    # create an empty dataframe with the desired columns
    df = pd.DataFrame(columns=['name', 'matchup', 'time', 'pts'])

    # extract the list of unique players that played during this season
    players = data['ofplayer'].unique()
    i = 0

    # iterating every player and isolating all their matchups data in a new data frame
    for player in players:
        playerLoc = data[data['ofplayer'] == player]

        # extract the list of unique players the actual player (iteration) had a matchup against
        playerMatchups = playerLoc['deplayer'].unique()

        # iterating every player from the matchups list and finding the sum of the matchup time and of the points scored
        for matchup in playerMatchups:
            matchupTime = playerLoc[playerLoc['deplayer'] == matchup]['matchupSEC'].sum()
            matchupPts = playerLoc[playerLoc['deplayer'] == matchup]['playerPTS'].sum()

            # appending each matchup total stats to the pre-created dataframe
            df.loc[i] = [player, matchup, matchupTime, matchupPts]
            i += 1

    return df

if __name__ == '__main__':
    # Heading
    st.title("Players' matchup stats")

    df = process_data()

    options = df['name'].unique()

    selected_name = st.selectbox(
        'Pick an offensive player',
        options
    )

    st.write(f'You selected: {selected_name}')

    st.dataframe(df[df["name"] == selected_name].sort_values('pts', ascending=False).set_index('name'), height=500)