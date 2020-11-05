import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------------------
# Import and clean data
game_details = pd.read_csv('games_details.csv')
# print(game_details.head(5))
game_details.drop(['GAME_ID', 'TEAM_ID', 'PLAYER_ID', 'START_POSITION',
                   'COMMENT', 'TEAM_ABBREVIATION'], axis=1, inplace=True)
game_details['FTL'] = game_details['FTA'] - game_details['FTM']
game_details = game_details.dropna()
# game_details.shape
# game_details.info()


game_details['MIN'] = game_details['MIN'].str.strip(':').str[0:2]
df = game_details.copy()

# --------------------------------------------------------------
# Import and clean data

st.write("Players Game Details")
st.dataframe(df.head(3))
# st.code('Hello')
top_activities = df.groupby(by='PLAYER_NAME')['PTS'].sum().sort_values(ascending=False).head(20).reset_index()
plt.figure(figsize=(15, 10))
plt.xlabel('POINTS', fontsize=15)
plt.ylabel('PLAYER_NAME', fontsize=15)
plt.title('Top 20 Players in the NBA League', fontsize=20)
ax = sns.barplot(x=top_activities['PTS'], y=top_activities['PLAYER_NAME'])
for i, (value, name) in enumerate(zip(top_activities['PTS'], top_activities['PLAYER_NAME'])):
    ax.text(value, i - .05, f'{value:,.0f}', size=10, ha='left', va='center')
ax.set(xlabel='POINTS', ylabel='PLAYER_NAME')
st.pyplot(plt)
# player = st.multiselect(
#
# )

st.write("""
# My first app
Hello *world!*
""")

x = st.slider("Select a number")
st.write("You selected:", x)
