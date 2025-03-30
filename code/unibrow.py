'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py

file_path = st.file_uploader("Upload a file", type=["csv", "xlsx", "json"])

if file_path:
    file_type = pl.get_file_extension(file_path.name)
    if file_type == "xlsx":
        df = pd.read_excel(file_path)
    elif file_type == "json":
        df = pd.read_json(file_path)
    elif file_type == "csv":
        df = pd.read_csv(file_path)
    else:
        st.warning("File type not supported")

    filter = st.toggle('Filter')

    if filter:
        colnames = pl.get_column_names(df)
        selected_col = st.selectbox("Column name:", colnames)
        uniqvals = pl.get_unique_values(df, selected_col)
        selected_val = st.selectbox("Unique value:", uniqvals)
        st.dataframe(df[df[selected_col] == selected_val])
    else:
        st.dataframe(df)