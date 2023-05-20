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

default_multiplyer = 1.5



if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame()

if "df_cleaned" not in st.session_state:
    st.session_state.df_cleaned = pd.DataFrame()

if "df_removed" not in st.session_state:
    st.session_state.df_removed = pd.DataFrame()

st.title(streamlit_texts ["app_title"])

st.markdown("2023-05-18, J. Köppern, see [GitHub](https://koeppern.github.io/polynomial_regression_demo/)")

st.download_button(label="Download data_raw.csv", file_name="data_raw.csv", data="data_raw.csv")

st.markdown(streamlit_texts["intro_text"])

with st.expander("About this app"):
    st.markdown(streamlit_texts["app_text"])


insert_section_load_create(raw_data_filename)


remove_outliers(default_window_size, default_multiplyer)


st.header("Fit polynomials")

make_plots = st.checkbox("Insert plots", value=True)

if st.button("Fit polynomial"):
    df_poly = fit_poly(st.session_state.df_cleaned, plot=make_plots)

    st.dataframe(df_poly)



# %%
