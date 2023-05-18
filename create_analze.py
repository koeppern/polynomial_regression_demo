# 2023-05-18, J. Köppern

# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Parameters
raw_data_filename ="./data_raw.csv"

window_size = 10

# Functions
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

    df_concat = pd.concat(windows, ignore_index=True)

    plot_xy(df_concat.x, df_concat.y)

    return df_concat

def plot_xy(x, y):
    plt.plot(x, y)

    plt.title("Interpolation points")

    plt.grid(True)


# %%
def create_data(filename):
    # Crete data
    ## Interpolation points through which the polynomial is to pass
    x = np.array([0, 50, 100, 200, 250, 290, 300])
    y = np.array([0, 50, 110, 170, 130, 120, 120]) / 10



    plot_xy(x, y)

    n_degree = len(x) - 1

    poly = np.poly1d(np.polyfit(x, y, n_degree))

    x_poly = np.linspace(min(x), max(x), 1000)

    y_poly = poly(x_poly)

    plot_xy(x_poly, y_poly)
    # Add noise and outlyers
    noise_percentag = 0.1
    noise_magnitude = noise_percentag * np.abs(y_poly)

    noise = np.random.uniform(
        low=-noise_magnitude, 
        high=noise_magnitude, 
        size=y_poly.shape)

    y_poly_with_noise = y_poly + noise

    # Apply the lower bound of zero
    y_poly_with_noise = np.maximum(y_poly_with_noise, 0)

    plot_xy(x_poly, y_poly_with_noise)
    # Add outliers
    n_outliers = 5

    y_poly_with_noise_outliers = y_poly_with_noise

    outlier_indices = [np.random.randint(0, len(y_poly_with_noise)) for i in range(n_outliers)]


    y_poly_with_noise_outliers[outlier_indices] = 0

    plot_xy(x_poly, y_poly_with_noise_outliers)
    # Create CSV
    # Assuming x_poly and y_poly_with_noise_outliers are your arrays
    data = {'x': x_poly, 'y': y_poly_with_noise_outliers}

    # Create a DataFrame
    df = pd.DataFrame(data)

    df.to_csv(filename, index=False)

    print(f"{raw_data_filename} created.")

    return df

# %%
df = create_data(raw_data_filename)

df_cleaned = process_data_in_windows(df, "y", window_size)


# %%
# Fit polxnomials of various degrees
for this_degree in range(10):
    