from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
week = [[1], [2], [3], [4], [5]]
sales = [1.2, 1.8, 2.6, 3.2, 3.8]
model = LinearRegression()
model.fit(week, sales)
y_pred = model.predict(week)
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
plt.scatter(week, sales, color='blue')
plt.plot(week, y_pred, color='red')
plt.title('Simple Linear Regression(y=mx+c)')
plt.xlabel('week')
plt.ylabel('sales')
plt.show()
OUTPUT:
Slope: 0.6600000000000004
Intercept: 0.5399999999999994
