from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
X = [
    [1000, 2, 5, 1],
    [1500, 3, 10, 2],
    [1800, 4, 8, 2],
    [1200, 3, 12, 1],
    [2500, 5, 3, 3]
]
y = [50, 75, 100, 65, 130]
model = LinearRegression()
model.fit(X, y)
area = float(input("Enter area in sqft: "))
bedrooms = int(input("Enter number of bedrooms: "))
age = int(input("Enter age of the house (in years): "))
floors = int(input("Enter number of floors: "))
user_input = [[area, bedrooms, age, floors]]
predicted_price = model.predict(user_input)[0]
print(f"\nPredicted house price: ₹{predicted_price:.2f} lakhs")
y_pred = model.predict(X)
plt.scatter(y, y_pred, color='purple')
plt.plot([min(y), max(y)], [min(y), max(y)], linestyle='--', color='gray')
plt.xlabel("Actual Prices (in lakhs)")
plt.ylabel("Predicted Prices (in lakhs)")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.tight_layout()
plt.show()
OUTPUT:
Enter area in sqft: 250
Enter number of bedrooms: 2
Enter age of the house (in years): 3
Enter number of floors: 2
Predicted house price: ₹132.19 lakhs
