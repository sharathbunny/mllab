import numpy as np
from scipy import stats
data = np.array([1, 3, 5, 2, 4])
mean_value = stats.tmean(data)
print(f"Data: {data}")
print(f"Mean: {mean_value:.2f}")

OUTPUT:
Data: [1 3 5 2 4]
Mean: 3.00
