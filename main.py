import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.header("The Best Company")
st.write("""lorem ipsum lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem
 ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem 
 ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem 
 ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem 
 ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem 
 ipsumlorem ipsumlorem ipsumlorem ipsum
""")

st.subheader("Our Team")

df = pandas.read_csv("data.csv")
col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(row['first name'].capitalize() + " " + row['last name'].capitalize())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(row['first name'].capitalize() + " " + row['last name'].capitalize())
        st.write(row['role'])
        st.image("images/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row['first name'].capitalize() + " " + row['last name'].capitalize())
        st.write(row['role'])
        st.image("images/" + row['image'])


