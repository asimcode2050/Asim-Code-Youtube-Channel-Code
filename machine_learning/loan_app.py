import pandas as pd  # For handling data
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
data = {
    'Income': [50000, 60000, 120000, 30000, 70000],
    'Credit_Score': [650, 700, 750, 620, 680],
    'Debt_to_Income': [0.3, 0.2, 0.1, 0.5, 0.4],
    'Approved': [1, 1, 1, 0, 1]  # 1 means loan approved, 0 means loan denied
}
df = pd.DataFrame(data)
X = df[['Income', 'Credit_Score', 'Debt_to_Income']]
y = df['Approved']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()  # Creating a scaler object
X_train_scaled = scaler.fit_transform(X_train)  # Scaling the training data
X_test_scaled = scaler.transform(X_test)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)  # Predicting loan approval on test data
labels = [0, 1]  # These are the possible labels in binary classification
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
conf_matrix = confusion_matrix(y_test, y_pred, labels=labels)
print("Confusion Matrix:")
print(conf_matrix)
class_report = classification_report(y_test, y_pred)
print("Classification Report:")
print(class_report)
