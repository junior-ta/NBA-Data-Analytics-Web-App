import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


year=st.selectbox('Year', list(reversed(range(1950,2026))))

#Getting the data from basketball reference
#@st.cache
def extract_data(season):
    url1= "https://www.basketball-reference.com/leagues/NBA_" + str(season) + "_per_game.html" #loading the table
    url2= "https://www.basketball-reference.com/leagues/NBA_" + str(season) + "_advanced.html"
    traditional=(pd.read_html(url1, header = 0))[0] #pandas reads the link and considers column 0 as the header, returns the list of tables at url, select table 0
    advanced=(pd.read_html(url2, header = 0))[0]

    df_traditional=traditional.drop(traditional[traditional.Team == 'Team'].index)
    df_advanced = advanced.drop(advanced[advanced.Team == 'Team'].index)
    df_advanced= df_advanced.drop(['Rk','Age','Team','Pos','G','GS','MP'], axis=1)
    df_stats=pd.merge(df_traditional,df_advanced, on='Player', how='outer')
    df_stats= df_stats.drop(['Rk'], axis=1)
    return df_stats
df_stats= extract_data(year)


#getting user input
stats= st.selectbox('Stats',df_stats.columns)
playercount= st.number_input('How many players do you need?',1)

st.write(df_stats)

#process the data
def prepare_data():
    playerNames= df_stats['Player'].unique()
    dfTemp= df_stats.set_index('Player')

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

#%%
#showing the top leaders graphically
def topKLeader(category,K):
#Using the stat category and the K number of players asked by the user
    statsSorted=playersAvg.sort_values(category,ascending=False)
    statsForVisualization= statsSorted.head(K)[category]
    namesForVisualization= statsSorted.head(K)['Player']

#drawing the bar chart
    plt.bar(namesForVisualization, statsForVisualization,width=0.3)
    plt.title('Top '+ str(K)+'  '+category+' players in the NBA 2022/23')
    plt.xlabel('players')
    plt.ylabel(category)
    plt.show()

    return
topKLeader(stats,playercount)

#st.write(df_stats)
