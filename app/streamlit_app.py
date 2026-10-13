import streamlit as st
import pandas as pd
from ucimlrepo import fetch_ucirepo

st.title("🩺 Diabetes Risk Miner")
st.write("Welcome to the DS311 Data Mining project dashboard!")

# Load dataset button
if st.button("Load CDC Diabetes Dataset"):
    with st.spinner("Fetching data from UCI Repository..."):
        cdc_data = fetch_ucirepo(id=891)
        X = cdc_data.data.features
        y = cdc_data.data.targets
        st.success("Data loaded successfully!")
        st.write("Features shape:", X.shape)
        st.dataframe(X.head())
