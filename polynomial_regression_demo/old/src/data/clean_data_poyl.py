
# 2023-05-17, J. Köppern
# Cleans data in .data/raw/raw_data.csv by removing outliers

# %%
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor


# Parameters
filename_csv = "../../data/raw/raw_data.csv"

n_neighbors = 20

contamination = 0.2

# Load data
df_original = pd.read_csv(filename_csv)

df = df_original.copy()
# %%
# Local outlier method
lof = LocalOutlierFactor(n_neighbors=n_neighbors, 
                         contamination=contamination)
outlier_labels = lof.fit_predict(df)

df['outlier_label'] = outlier_labels

cleaned_df = df[df['outlier_label'] == 1].drop(columns=['outlier_label'])

print(cleaned_df)
# %%
