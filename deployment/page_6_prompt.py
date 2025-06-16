import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

teamsAdvanced=pd.read_csv(r"database/team_advanced.csv")

def process_data(data):
    # finding the length of the season (in terms of number of games played) and dividing it into 4 equal splits
    n = len(data)
    split = n // 4

    # Creating a list containing the 4 splits data frames extracted from the entire season dataframe
    splitn = [teamsAdvanced.iloc[:split], teamsAdvanced.iloc[split:(2 * split)],
              teamsAdvanced.iloc[(2 * split):(3 * split)], teamsAdvanced.iloc[(3 * split):]]

    # creating a list of paces throughout the season for the data visualization
    paceList = []

    for split in splitn:
        pace = split['pace'].mean()
        paceList.append(pace)

    return paceList

if __name__ == '__main__':
    # Heading
    st.title('Teams pace throughout the season')

    paceList = process_data(teamsAdvanced)
    percentage = ["25%", "50%", "75%", "100%"]

    # spacing
    for i in range(3):
        st.markdown("")

    plt.plot(percentage, paceList, marker="o")
    plt.title('linear progression of pace for the season 2022/23')
    plt.xlabel('Season split')
    plt.ylabel('Pace')
    st.pyplot(plt)

    st.markdown("This confirms the theory that teams start off a little slowly as they are getting back into competitive shape. They peak in the christmas and as we approach the all star game which represents the 2nd part of the season")
    st.markdown("They keep slowing down as the season progresses. This is an assumption made on basis of fatigue affecting pace, more analysis required!")