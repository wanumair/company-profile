import streamlit as st
import pandas


st.title("The Best Company")
st.write("lorem ipsum")

st.write("**Our Team**")

df = pandas.read_csv("data.csv", sep=',')
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    for index, row in df[:4].iterrows():
        st.header(row['first name'].capitalize() + " " + row['last name'].capitalize())



