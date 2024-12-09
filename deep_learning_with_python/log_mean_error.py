import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
exam_passed = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
model = LogisticRegression()
model.fit(hours_studied, exam_passed)
predictions = model.predict_proba(hours_studied)[:, 1]
mse = mean_squared_error(exam_passed, predictions)
print("Predictions (probabilities of passing):", predictions)
print("Mean Squared Error (MSE):", mse)
