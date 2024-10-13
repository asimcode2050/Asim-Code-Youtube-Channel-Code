import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

data ={
    'email':[
        "Congratulation! You've won a lottery. Click here to claim.",
        "Your invoice from our recent purchase is attached.",
        "Urgent: Verify your account immediately!",
        "Hello! Just checking in to see how you're doing.",
        "Important: update your payment information.",
        "Meet your new colleague at the office."
    ],
    'label':[1,0,1,0,1,0]
}

df = pd.DataFrame(data)

X = df['email']
y = df['label']

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)
X_train , X_test, y_train, y_test = train_test_split(X_vectorized,y,test_size=0.2, random_state=42)
model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:",accuracy_score(y_test, y_pred))
print("Classification Report:\n",classification_report(y_test,y_pred))

new_emails =["Claim your prize now!","Meeting ar 2 PM tomorrow."]
new_emails_vectorized = vectorizer.transform(new_emails)
predictions = model.predict(new_emails_vectorized)
print('Predictions:',predictions)

