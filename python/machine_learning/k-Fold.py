import numpy as np
from sklearn.model_selection import KFold
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
iris = load_iris()
X = iris.data  # Features of the dataset "shape = (150, 4)"
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

k = 5

kf = KFold(n_splits=k, shuffle=True, random_state=42)

clf = LogisticRegression(max_iter=200)

accuracies = []

for train_index, test_index in kf.split(X_train):

    X_train_fold, X_test_fold = X_train[train_index], X_train[test_index]
    y_train_fold, y_test_fold = y_train[train_index], y_train[test_index]

    clf.fit(X_train_fold, y_train_fold)

    y_pred_fold = clf.predict(X_test_fold)

    accuracy = accuracy_score(y_test_fold, y_pred_fold)

    accuracies.append(accuracy)

average_accuracy = np.mean(accuracies)
print(f"Average Accuracy across {
      k}-Fold Cross-Validation: {average_accuracy:.4f}")

clf.fit(X_train, y_train)
y_test_pred = clf.predict(X_test)
final_accuracy = accuracy_score(y_test, y_test_pred)
print(f"Accuracy on the final test set: {final_accuracy:.4f}")
