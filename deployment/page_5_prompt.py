import pandas as pd
import streamlit as st


traditional = pd.read_csv(r"database/basic.csv")
advanced = pd.read_csv(r"database/advanced.csv")

#Getting the data from the database
def extract_process_data():
    df_traditional = traditional.drop(['gameid', 'home', 'team', 'playerid'], axis=1)
    df_advanced = advanced.drop(['gameid', 'home', 'team', 'playerid', 'name', 'SEC'], axis=1)
    df_stats= pd.concat([df_traditional,df_advanced], axis=1)

    return df_stats

if __name__ == '__main__':
    # Heading
    st.title('Individual performance frequencies')

    df = extract_process_data()

    #getting user input
    category=st.selectbox('Stats', df.drop(['name'], axis=1).columns)
    value= st.slider("performance", min_value=0, value=0)


    st.markdown(("frequency: " + str(len(df[df[category] >= value]))))
    st.dataframe(df[df[category] >= value].set_index('name'))