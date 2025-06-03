import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#Heading
st.title('Displaying the top K leaders in a particular stat category using a bar chart')

#Getting the data from basketball reference
def extract_data():
    traditional = pd.read_csv(r"C:\Users\ttjrb\OneDrive\Desktop\University Important\summer 2024 work\projects\databases\ALL 1320 nba games 2022-23\basic.csv")
    advanced = pd.read_csv(r"C:\Users\ttjrb\OneDrive\Desktop\University Important\summer 2024 work\projects\databases\ALL 1320 nba games 2022-23\advanced.csv")

    df_traditional = traditional.drop(['gameid', 'home', 'team', 'playerid'], axis=1)
    df_advanced = advanced.drop(['gameid', 'home', 'team', 'playerid', 'name', 'SEC'], axis=1)
    df_stats= pd.concat([df_traditional,df_advanced], axis=1)
    return df_stats
df_stats= extract_data()


#getting user input
stats= st.selectbox('Stats',df_stats.drop(['name'], axis= 1).columns)
playercount= st.number_input('How many players do you need?',1)


#process the data
def prepare_data():
    playerNames= df_stats['name'].unique()
    dfTemp= df_stats.set_index('name')

    # Iterating the players and finding their average stats for the season
    eligiblePlayersList = []
    statsCategoriesList = dfTemp.columns
    resultList = []

    # iterating each player
    for player in playerNames:
        iteration = dfTemp.loc[player]
        # determining if he is eligible for rankings (>58 games played)
        if len(iteration) > 58:
            eligiblePlayersList.append(player)
            # finding the average stats of the player
            avg = iteration.mean()
            playerStatsList = []
            # appending the player's stats to his list (respective of categories and in order)
            for i in range(len(statsCategoriesList)):
                playerStatsList.append(avg[statsCategoriesList[i]])
            # creating the player's dictionary for his entry in the result list, key= stat category, value= his average stats
            playerDict = {}
            for i in range(len(statsCategoriesList)):
                playerDict[statsCategoriesList[i]] = playerStatsList[i]
            resultList.append(playerDict)

    # Converting the final result list of dictionaries to a dataframe and adding back the names of players who are eligible for ranking
    playersAvg = pd.DataFrame(resultList)
    playersAvg.insert(0, 'Player', eligiblePlayersList)

    return  playersAvg
playersAvg= prepare_data()

#spacing
for i in range(3):
    st.markdown("")

#showing the top leaders graphically
def topKLeader(category,K):
#Using the stat category and the K number of players asked by the user
    statsSorted=playersAvg.sort_values(category,ascending=False)
    statsForVisualization= statsSorted.head(K)[category]
    namesForVisualization= statsSorted.head(K)['Player']

#drawing the bar chart
    plt.figure(figsize=(10, 6))  # Optional: improve sizing
    plt.bar(namesForVisualization, statsForVisualization, width=0.3)
    plt.title('Top ' + str(K) + ' ' + category + ' players in the NBA 2022/23')
    plt.xlabel('Players')
    plt.ylabel(category)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels if needed
    plt.tight_layout()  # Adjust layout so labels fit nicely

    st.pyplot(plt)  # Instead of plt.show()

topKLeader(stats,playercount)

