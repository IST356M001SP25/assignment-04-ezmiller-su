'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])

if file:
    if file.name.endswith(".xlsx"):
        df = pd.read_excel(file)
    elif file.name.endswith(".json"):
        df = pd.read_json(file)
    elif file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        st.warning("File type not supported")

    filter = st.toggle('Filter')

    if filter:
        cols = pl.get_column_names(df)

        x = st.selectbox("Select a column", cols)

        if x:
            st.write(x)
            st.dataframe(df[x])
    else:
        st.dataframe(df)