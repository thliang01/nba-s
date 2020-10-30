import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

x = st.slider("Select a number")
st.write("You selected:", x)
