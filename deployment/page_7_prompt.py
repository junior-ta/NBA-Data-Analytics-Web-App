import pandas as pd
import streamlit as st

@st.cache_data
def process_data():
    data = pd.read_csv(r"database/matchups.csv")

    df= data.groupby(['ofplayer', 'deplayer'])[['matchupSEC', 'playerPTS']].sum().reset_index()

    # create an empty dataframe with the desired columns
    df.columns = ['name', 'matchup', 'time', 'pts']

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