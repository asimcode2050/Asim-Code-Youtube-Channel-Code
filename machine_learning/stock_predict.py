# Stock Price Prediction
# pip install pandas numpy matplotlib scikit-learn yfinance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
ticker = 'AAPL'  # You can change this to any other stock ticker symbol
data = yf.download(ticker, start='2010-01-01', end='2024-01-01')
print(data.head())
data = data[['Close']]
data['Close'].plot(title=f'{ticker} Stock Price History', figsize=(10, 6))
plt.show()
data['Prev Close'] = data['Close'].shift(1)
data = data.dropna()
X = data[['Prev Close']]  # Features (previous day's close price)
y = data['Close']        # Labels (current day's close price)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
plt.figure(figsize=(10, 6))
plt.plot(y_test.index, y_test, label='Actual Prices', color='blue')
plt.plot(y_test.index, y_pred, label='Predicted Prices', color='red')
plt.title(f'{ticker} Stock Price Prediction vs Actual Prices')
plt.legend()
plt.show()
last_known_price = data['Close'].iloc[-1]  # The most recent closing price
next_day_pred = model.predict(np.array([[last_known_price]]))
print(f"Predicted next day's close price: {next_day_pred[0]}")
