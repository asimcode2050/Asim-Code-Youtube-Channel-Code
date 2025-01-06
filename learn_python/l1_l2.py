import numpy as np
def mean_squared_error(y_true, y_pred):
    mse = np.mean((y_true - y_pred) **
                  2) 
    return mse 
def gradient_descent(X, y, initial_weights, learning_rate, epochs, regularization='L2', lambda_reg=0.01):

    weights = initial_weights.copy()
    for epoch in range(epochs):
        y_pred = X.dot(weights)
        error = y_pred - y
        gradient = (2 / X.shape[0]) * X.T.dot(error)
        if regularization == 'L2':
            gradient += 2 * lambda_reg * weights
        elif regularization == 'L1':
            gradient += lambda_reg * np.sign(weights)
        weights -= learning_rate * gradient
        if regularization == 'L2':
            loss = mean_squared_error(
                y, y_pred) + lambda_reg * np.sum(weights ** 2)
        elif regularization == 'L1':
            loss = mean_squared_error(
                y, y_pred) + lambda_reg * np.sum(np.abs(weights))
        else:
            loss = mean_squared_error(y, y_pred)

        if epoch % 100 == 0:
            print(
                f"Epoch {epoch}/{epochs} | Loss: {loss:.4f} | Weights: {weights}")

    return weights


if __name__ == "__main__":
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
    y = np.array([5, 7, 9, 11, 13])
    initial_weights = np.zeros(X.shape[1])
    learning_rate = 0.01
    epochs = 1000
    lambda_reg = 0.1
    print("Training with L2 regularization (Ridge)...")
    weights_L2 = gradient_descent(
        X, y, initial_weights, learning_rate, epochs, regularization='L2', lambda_reg=lambda_reg)
    print("Final weights with L2 regularization:", weights_L2)
    print("\nTraining with L1 regularization (Lasso)...")
    weights_L1 = gradient_descent(
        X, y, initial_weights, learning_rate, epochs, regularization='L1', lambda_reg=lambda_reg)
    print("Final weights with L1 regularization:", weights_L1)
