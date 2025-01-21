import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
ridge = Ridge(alpha=1.0)  # 'alpha' is the regularization strength parameter.
ridge.fit(X_train, y_train)
lasso = Lasso(alpha=0.1)
lasso.fit(X_train, y_train)  # Train the Lasso model using the training data.
ridge_predictions = ridge.predict(X_test)
lasso_predictions = lasso.predict(X_test)
ridge_mse = mean_squared_error(y_test, ridge_predictions)
lasso_mse = mean_squared_error(y_test, lasso_predictions)
print("Ridge Regression MSE:", ridge_mse)
print("Lasso Regression MSE:", lasso_mse)

plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='black', label='Actual data')
plt.plot(X_test, ridge_predictions, color='blue',
         label='Ridge Prediction')
plt.plot(X_test, lasso_predictions, color='red',
         label='Lasso Prediction')
plt.title('Ridge vs Lasso Regression')
plt.xlabel('Feature')
plt.ylabel('Target')
plt.legend()
plt.show() 
