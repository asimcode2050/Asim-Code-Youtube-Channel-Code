# Home value prediction using machine learning
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import fetch_california_housing
import matplotlib.pyplot as plt
data = fetch_california_housing()
df = pd.DataFrame(data=data.data, columns=data.feature_names)
df['target'] = data.target
print(df.head())
X = df.drop('target', axis=1)  # Features: All columns except the target
y = df['target']  # Target: The column with home values
print(X.isnull().sum())
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
r2 = r2_score(y_test, y_pred)
print(f"R-squared (R2 score): {r2}")
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue', edgecolors='k', alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(),
                                        y_test.max()], 'r--', lw=2)  # Diagonal line
plt.title("True vs Predicted Home Values")
plt.xlabel("True Home Values")
plt.ylabel("Predicted Home Values")
plt.show()

