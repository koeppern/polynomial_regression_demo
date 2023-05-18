# 2023-05-18, J. Köppern

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fit_poly_functions import *
import streamlit as st
import seaborn as sns

# Parameters
raw_data_filename ="./data_raw.csv"

default_window_size = 10



if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

if "df_cleaned" not in st.session_state:
    st.session_state.df_cleaned = pd.DataFrame()

st.title(streamlit_texts ["app_title"])

with st.expander("About this app"):
    st.markdown(streamlit_texts ["app_text"])


insert_section_load_create(raw_data_filename)


remove_outliers(default_window_size)


st.header("Fit polynomials")

# df_poly = fit_poly(df_cleaned, plot=False)



# %%
