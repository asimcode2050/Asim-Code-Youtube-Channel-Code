import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt  # For plotting loss curves

X = np.linspace(-10, 10, 500)

y = X**2 + np.random.normal(0, 2, 500)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

X_train = X_train.reshape(-1, 1)
X_test = X_test.reshape(-1, 1)
model = Sequential()
model.add(Dense(10, input_dim=1, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

history = model.fit(X_train, y_train, epochs=200,
                    batch_size=32, validation_data=(X_test, y_test))

plt.plot(history.history['loss'], label='Training Loss')  # Training loss curve
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()
