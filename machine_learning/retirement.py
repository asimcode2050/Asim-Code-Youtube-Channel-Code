import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
data = {
    'current_age': [30, 35, 40, 45, 50],  # Current age of the person
    'target_retirement_age': [65, 65, 65, 65, 65],  # Target retirement age
    'current_savings': [50000, 75000, 100000, 120000, 150000],
    'annual_savings': [10000, 12000, 15000, 18000, 20000],  # Annual savings
    'retirement_goal': [1500000, 1500000, 1500000, 1500000, 1500000]
}
df = pd.DataFrame(data)
X = df[['current_age', 'target_retirement_age', 'current_savings',
        'annual_savings']]  # Features (independent variables)
y = df['retirement_goal']  # Target (dependent variable)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)  # Fit the model with the training data
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'Coefficients: {model.coef_}')
print(f'Intercept: {model.intercept_}')
new_data = pd.DataFrame([[40, 65, 100000, 15000]], columns=[
                        'current_age', 'target_retirement_age', 'current_savings', 'annual_savings'])
predicted_goal = model.predict(new_data)
print(f'Predicted Retirement Goal: {predicted_goal[0]}')
