import numpy as np
def binary_crossentropy(y_true, y_pred):
    epsilon = 1e-15
    y_pred = np.clip(y_pred, epsilon, 1 - epsilon)
    ''' BCE = -( y_true * log(y_pred) + (1 - y_true) * log(1 - y_pred) ) '''
    loss = -(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))
    return np.mean(loss)  # Returning the average BCE loss.

y_true = np.array([1, 0, 1, 0, 1])
y_pred = np.array([0.9, 0.1, 0.8, 0.3, 0.7])
loss = binary_crossentropy(y_true, y_pred)
print("Binary Cross-Entropy Loss:", loss)
