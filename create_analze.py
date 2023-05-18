# 2023-05-18, J. Köppern

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from fit_poly_functions import *

# Parameters
raw_data_filename ="./data_raw.csv"

window_size = 10


# %%
df = create_data(raw_data_filename, plot=False)

df_cleaned = process_data_in_windows(
    df, 
    "y",
    window_size,
    plot=False)


df_poly = fit_poly(df_cleaned, plot=False)
# %%
