import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

dataGames = pd.read_csv(r"databases/games.csv")

def extract_prepare_data(data):
    # getting the points scored by each team for all the games of the season
    allScores = []

    for i in range(len(data['h_pts'])):
        allScores.append(data['h_pts'].iloc[i])
    for i in range(len(data['a_pts'])):
        allScores.append(data['a_pts'].iloc[i])

    # classifying the points using given marks
    allScoresCount = {}

    for score in allScores:
        # >150
        if score > 150:
            if ">150" in allScoresCount:
                allScoresCount[">150"] += 1
            else:
                allScoresCount[">150"] = 1
        # >125
        if score > 125:
            if ">125" in allScoresCount:
                allScoresCount[">125"] += 1
            else:
                allScoresCount[">125"] = 1
        # >110
        if score > 110:
            if ">110" in allScoresCount:
                allScoresCount[">110"] += 1
            else:
                allScoresCount[">110"] = 1
        # >100
        if score > 100:
            if ">100" in allScoresCount:
                allScoresCount[">100"] += 1
            else:
                allScoresCount[">100"] = 1
        # >90
        if score > 90:
            if ">90" in allScoresCount:
                allScoresCount[">90"] += 1
            else:
                allScoresCount[">90"] = 1
        # <90
        if score < 90:
            if "<90" in allScoresCount:
                allScoresCount["<90"] += 1
            else:
                allScoresCount["<90"] = 1

    desiredOrder = ['>90', '>150', '>100', '>110', '>125', '<90']
    allScoresCountSorted = {key: allScoresCount[key] for key in desiredOrder}

    return allScoresCountSorted


if __name__ == '__main__':
    # Heading
    st.title("Teams' scoring splits of the season")

    allScoresCountSorted= extract_prepare_data(dataGames)

    st.dataframe(allScoresCountSorted)

    # preparing the data to be plotted in the pie chart
    allScoresCountKeys = []
    allScoresCountValues = []

    for i in allScoresCountSorted:
        allScoresCountKeys.append(i)
        allScoresCountValues.append(allScoresCountSorted[i])

    plt.pie(allScoresCountValues, labels=allScoresCountKeys)
    plt.title("Pie chart of scoring")
    st.pyplot(plt)