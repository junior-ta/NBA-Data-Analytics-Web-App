#%%
import csv
import pandas as pd
import matplotlib.pyplot as plt

basic= pd.read_csv(r"C:\Users\ttjrb\OneDrive\Desktop\University Important\summer 2024 work\projects\databases\ALL 1320 nba games 2022-23\basic.csv",usecols=('name','SEC','FGpct','3PM','3Ppct','FTM','FTpct','ORB','TRB','AST','STL','BLK','TOV','PTS','plusminusPTS'))
advanced=pd.read_csv(r"C:\Users\ttjrb\OneDrive\Desktop\University Important\summer 2024 work\projects\databases\ALL 1320 nba games 2022-23\advanced.csv",usecols=('USGpct','DEFRTG'))
#%%
df=pd.concat([basic,advanced], axis=1)

playerNames= df['name'].unique()
len(playerNames)

dfTemp=df.set_index('name')

eligiblePlayersList=[]
statsCategoriesList= dfTemp.columns
resultList=[]
for player in playerNames:
    iteration= dfTemp.loc[player]
    if len(iteration)>58:
        eligiblePlayersList.append(player)
        avg= iteration.mean()
        playerStatsList=[]      
        for i in range(len(statsCategoriesList)):
            playerStatsList.append(avg[statsCategoriesList[i]])            
        playerDict={}
        for i in range(len(statsCategoriesList)):
            playerDict[statsCategoriesList[i]]= playerStatsList[i]
        resultList.append(playerDict)

playersAvg=pd.DataFrame(resultList)
playersAvg.insert(0,'name',eligiblePlayersList)

def topKLeader(category,K):
    statsSorted=playersAvg.sort_values(category,ascending=False)
    statsForVisualization= statsSorted.head(K)[category]
    namesForVisualization= statsSorted.head(K)['name']

    plt.bar(namesForVisualization, statsForVisualization,width=0.3)
    plt.title('Top '+ str(K)+'  '+category+' players in the NBA 2022/23')
    plt.xlabel('players')
    plt.ylabel(category)
    plt.show()
#%%
par1= input('what category leaders do you need?')
par2=int(input('how many leader do you need'))
topKLeader(par1, par2)
#%%
#........................Step by Step process..........................................................................................................
#%%
#concatenate boths dataframes row-wise to make the work easier

df=pd.concat([basic,advanced], axis=1)
#%%
df
#%%
#getting the name of every single NBA player of the season and adding to a list

playerNames= df['name'].unique()
len(playerNames)
#%%
#setting players names as index temporarily to ease the work
dfTemp=df.set_index('name')
#%%
#Iterating the players and finding their average stats for the season

eligiblePlayersList=[]
statsCategoriesList= dfTemp.columns
resultList=[]
#iterating each player
for player in playerNames:
    iteration= dfTemp.loc[player]
#determining if he is eligible
    if len(iteration)>58:
        eligiblePlayersList.append(player)
#finding the average stats of the player
        avg= iteration.mean()
        playerStatsList=[]
#appending the player's stats to his list (respective of categories and in order)        
        for i in range(len(statsCategoriesList)):
            playerStatsList.append(avg[statsCategoriesList[i]])
#creating the player's dictionary for his entry in the result list, key= stat category, value= his average stats            
        playerDict={}
        for i in range(len(statsCategoriesList)):
            playerDict[statsCategoriesList[i]]= playerStatsList[i]
        resultList.append(playerDict)

        
#%%
#Converting the final result list of dictionaries to a dataframe and adding back the names of players who are eligible for ranking
playersAvg=pd.DataFrame(resultList)
playersAvg.insert(0,'name',eligiblePlayersList)

#Yessss!!! we did it
playersAvg
#%%
#showing the top leaders graphically
def topKLeader(category,K):
#Using the stat category and the K number of players asked by the user
    statsSorted=playersAvg.sort_values(category,ascending=False)
    statsForVisualization= statsSorted.head(K)[category]
    namesForVisualization= statsSorted.head(K)['name']

#drawing the bar chart
    plt.bar(namesForVisualization, statsForVisualization,width=0.3)
    plt.title('Top '+ str(K)+'  '+category+' players in the NBA 2022/23')
    plt.xlabel('players')
    plt.ylabel(category)
    plt.show()

#%%
#Finding top 3 scorers in the NBA
topKLeader('PTS',3)
#%%
#par1= input('what category leaders do you need?')
#par2=int(input('how many leader do you need'))
#topKLeader(par1, par2)