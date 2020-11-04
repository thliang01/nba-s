import streamlit as st
import pandas as pd
import numpy as np

# --------------------------------------------------------------
# Import and clean data
game_details = pd.read_csv('games_details.csv')
print(game_details.head(5))
game_details.drop(['GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'START_POSITION',
                   'COMMENT', 'TEAM_ABBREVIATION'], axis=1, inplace=True)
game_details['FTL'] = game_details['FTA'] - game_details['FTM']
game_details = game_details.dropna()
# game_details.shape
# game_details.info()


game_details['MIN'] = game_details['MIN'].str.strip(':').str[0:2]
df = game_details.copy()

# st.write
# print(df.head(5))

st.write("Players Game Details")
st.dataframe(df.head(5))
st.write("""
# My first app
Hello *world!*
""")

x = st.slider("Select a number")
st.write("You selected:", x)
