# 2023-05-17, J. Köppern
# Generate noisy data with outlyers

# %%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# %%
# Interpolation points through which the polynomial is to pass
x = np.array([0, 50, 100, 200, 250, 290, 300])
y = np.array([0, 50, 110, 170, 130, 120, 120]) / 10

def plot_xy(x, y):
    plt.plot(x, y)

    plt.title("Interpolation points")

    plt.grid(True)

plot_xy(x, y)
# %%
n_degree = len(x)

poly = np.poly1d(np.polyfit(x, y, n_degree))

x_poly = np.linspace(min(x), max(x), 1000)

y_poly = poly(x_poly)

plot_xy(x_poly, y_poly)
# %%
# Add noise and outlyers
noise_percentag = 0.1
noise_magnitude = noise_percentag * np.abs(y_poly)

noise = np.random.uniform(low=-noise_magnitude, 
                          high=noise_magnitude, 
                          size=y_poly.shape)

y_poly_with_noise = y_poly + noise

# Apply the lower bound of zero
y_poly_with_noise = np.maximum(y_poly_with_noise, 0)

plot_xy(x_poly, y_poly_with_noise)
# %%
# Add outliers
n_outliers = 5

y_poly_with_noise_outliers = y_poly_with_noise

outlier_indices = [np.random.randint(0, len(y_poly_with_noise)) for i in range(n_outliers)]


y_poly_with_noise_outliers[outlier_indices] = 0

plot_xy(x_poly, y_poly_with_noise_outliers)
# %%
# Create CSV
# Assuming x_poly and y_poly_with_noise_outliers are your arrays
data = {'x': x_poly, 'y': y_poly_with_noise_outliers}

# Create a DataFrame
df = pd.DataFrame(data)

#df.to_csv('./../../data/raw/raw_data.csv', index=False)
df.to_csv('./data/raw/raw_data.csv', index=False)

import os

current_path = os.getcwd()
print(current_path)


# %%