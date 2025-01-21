import numpy as np
class Perceptron:

    def __init__(self, n_features, learning_rate=0.01, n_iterations=1000):
        self.weights = np.zeros(n_features)
        self.bias = 0
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations

    def fit(self, X, y):
        for _ in range(self.n_iterations):
            for i in range(len(X)):

                linear_output = np.dot(X[i], self.weights) + self.bias
                prediction = 1 if linear_output >= 0 else -1

                if prediction != y[i]:
                    self.weights += self.learning_rate * y[i] * X[i]
                    self.bias += self.learning_rate * y[i]

    def predict(self, X):
        
        linear_output = np.dot(X, self.weights) + self.bias

        return np.where(linear_output >= 0, 1, -1)


if __name__ == "__main__":
    X = np.array([[2, 3], [4, 5], [1, 2], [3, 4]])
    y = np.array([1, 1, -1, -1])  # 1D numpy array for labels (target values)
    perceptron = Perceptron(
        n_features=2, learning_rate=0.01, n_iterations=1000)
    perceptron.fit(X, y)
    predictions = perceptron.predict(X)
    print("Predictions:", predictions)
