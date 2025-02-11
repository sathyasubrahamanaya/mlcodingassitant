import pandas as pd
import streamlit as st

@st.cache_data
def load_dataframe(uploaded_file):
    """Load and cache the uploaded CSV file as a DataFrame."""
    return pd.read_csv(uploaded_file)