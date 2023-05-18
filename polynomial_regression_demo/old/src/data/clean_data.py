# 2023-05-17, J. Köppern
# Cleans data/remove outliers

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Parameters
filename_raw = "../../data/raw/data.csv"
#filename_raw = "/data/raw/raw_data.csv"

filename_cleaned = "../../data/processed/data.csv"

window_size = 10

# Functions
def plot_xy(x, y):
    plt.plot(x, y)

    plt.title("Interpolation points")

    plt.grid(True)

def outlier_detection_iqr(df, column, multiplier=1.5):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR

    return df.query(f"{column} >= {lower_bound} and {column} < {upper_bound}")

def process_data_in_windows(df, column, window_size, multiplier=1.5):
    windows = []

    for i in range(0, len(df), window_size):
        window = df.iloc[i:i + window_size]

        window_clean = outlier_detection_iqr(
            window, 
            column, 
            multiplier
        )

        windows.append(window_clean)

    return pd.concat(windows, ignore_index=True)

# %%
# Load data
df_original = pd.read_csv(filename_raw)

df = df_original.copy()
# %%
# rmove outliers
df_cleaned = process_data_in_windows(df, "y", window_size)

plot_xy(df.x, df.y)

plot_xy(df_cleaned.x, df_cleaned.y)

df_cleaned.to_csv(filename_cleaned, index=False)

# %%
