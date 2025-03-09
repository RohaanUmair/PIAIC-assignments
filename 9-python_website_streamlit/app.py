import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.title('Simple Data Dashboard')

uploaded_file = st.file_uploader('choose a CSV file', type='csv')

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader('Data Preview')
    st.write(df.head())

    st.subheader('Data Summary')
    st.write(df.describe())

    # st.subheader('Filter Data')
    # columns = df.columns.tolist()
    # selected_columns = st.selectbox('Select columns to filter by', columns)

    