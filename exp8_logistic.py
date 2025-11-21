import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
X = np.array([[i] for i in range(1, 11)])
y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
model = LogisticRegression().fit(X, y)
h = 8
p = model.predict([[h]])[0]
prob = model.predict_proba([[h]])[0][1]
print(f"Enter no. of hours studied: {h}")
print(f"Predicted Outcome: {'Pass' if p else'Fail'}")
print(f"Probability of Passing: {prob:.2f}")
xr = np.linspace(0, 11, 100).reshape(-1, 1)
yp = model.predict_proba(xr)[:, 1]
plt.scatter(X, y, color='black')
plt.plot(xr, yp, color='blue')
plt.xlabel("Hours studied")
plt.ylabel("Probability of passing")
plt.title("Logistic Regression Fit")
plt.grid(True)
plt.show()
OUTPUT:
Enter no. of hours studied: 8
Predicted Outcome: Pass
Probability of Passing: 0.98
