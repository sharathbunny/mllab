import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

data_points = np.array([[2], [4], [10], [12], [3],
[11], [20], [30], [25]])

kmeans = KMeans(n_clusters=2,
random_state=0, n_init='auto').fit(data_points)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
plt.scatter(data_points,
np.zeros_like(data_points), c=labels, s=50,
cmap='viridis', label='Data Points')
plt.scatter(centroids[:, 0],
np.zeros_like(centroids[:, 0]), c='red', marker='x',
s=200, label='Centroids')
plt.title("Clustered Data with Centroids")
plt.legend()
plt.show()
print(f"Final Centroids : {centroids.flatten()}")
print(f"Cluster 1 points : {data_points[labels ==
0].flatten()}")
print(f"Cluster 2 points : {data_points[labels ==
1].flatten()}")

