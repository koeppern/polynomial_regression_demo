# 2023-05-17, J. Köppern
# Sweep over the model's degree, fir polynomial, remove outliers and store result

# %%
import pandas as pd
import numpy as np

# Parameters
filename_csv = "../../data/raw/raw_data.csv"

max_degree = 8

rel_imporvement_threshold = 0.05

# Load data
df = pd.read_csv(filename_csv)
# %%
# Loop over the polinomial's dgree
for this_degree in range(max_degree + 1):
    this_df = df.copy()

    for _ in range(500):
        this_poly = np.poly1d(np.polyfit(
            this_df.x,
            this_df.y,
            this_degree
        ))

        y_poly = this_poly(this_df.x)

        error = y_poly - this_df.y

        rel_abs_error = abs(np.divide(error, this_df.y, out=np.array(error), where=this_df.y != 0))

        this_mean_rel_abs_error = np.mean(rel_abs_error)

        if this_mean_rel_abs_error >= rel_imporvement_threshold:
            i_max = np.argmax(rel_abs_error)

            this_df = this_df.drop(this_df.index[i_max])


        
        last_mean_rel_error = this_mean_rel_abs_error
    print(this_degree, last_mean_rel_error, len(this_df))
    # %%
