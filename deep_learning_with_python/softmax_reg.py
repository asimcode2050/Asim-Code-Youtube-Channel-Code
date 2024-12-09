import numpy as np
X = np.array([[2.0, 3.0, 1.0],
              [1.0, 5.0, 7.0],
              [6.0, 1.0, 8.0]])
y_true = np.array([0, 1, 2])
weights = np.random.randn(3, 3)
biases = np.random.randn(3)


def softmax(scores):
    exp_scores = np.exp(scores)
    return exp_scores / np.sum(exp_scores, axis=0)


def predict(X, weights, biases):
    scores = np.dot(X, weights.T) + biases
    probabilities = softmax(scores.T)
    return probabilities


predicted_probabilities = predict(X, weights, biases)
print("Predicted probabilities for each observation:")
print(predicted_probabilities)
predicted_classes = np.argmax(predicted_probabilities, axis=0)
print("Predicted classes for each observation:")
print(predicted_classes)
accuracy = np.mean(predicted_classes == y_true)
print("Accuracy of the model: ", accuracy)
