from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=99)
params = {
    'max_depth': range(1, 10),
    'min_samples_leaf': range(1, 20, 2),
    'min_samples_split': range(2, 20, 2)
}
model = GridSearchCV(
    DecisionTreeClassifier(random_state=1),
    param_grid=params,
    cv=5
)
model.fit(X_train, y_train)
print("Best Accuracy:", model.best_score_)
print("Test Accuracy:", accuracy_score(y_test, model.predict(X_test)))
plt.figure(figsize=(10, 6))
plot_tree(model.best_estimator_, filled=True)
plt.show()
OUTPUT:
Best Accuracy: 0.9714285714285715
Test Accuracy: 0.9555555555555556
