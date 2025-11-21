import numpy as np
from collections import Counter
from math import sqrt
ed = lambda p1, p2: sqrt(np.sum((np.array(p1) -np.array(p2))**2))
def knn(train_data, labels, test, k):
    dists = sorted([(ed(test, tp), label) for tp, label
    in zip(train_data, labels)])
    return Counter([label for _, label in
    dists[:k]]).most_common(1)[0][0]
train_data = np.array([[40, 20], [50, 50], [60, 70],
[30, 10], [70, 80], [25, 80], [10, 55]])
labels = np.array(['red', 'red', 'blue', 'red', 'blue','blue', 'red'])
test_point = np.array([20, 35])
k = 5
print(f"Prediction: {knn(train_data, labels,test_point, k)}")

OUTPUT:
Prediction: red
