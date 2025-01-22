import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

texts = [
    'I love programming in Python', 
    'Python is a great programming language',
    'I hate bugs in my code',
    'Debugging code is fun', 
    'I love solving problems with code',
    'Python is awesome for data science', 
    'I dislike slow code execution',  # Negative sentiment
    'Writing code is challenging but rewarding'  # Positive sentiment
]
labels = ['positive', 'positive', 'negative', 'positive',
          'positive', 'positive', 'negative', 'positive']
X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=42)
vectorizer = CountVectorizer()  # Initializing the vectorizer object.
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
classifier = MultinomialNB()  # Initialize the Naive Bayes classifier.
classifier.fit(X_train_vectorized, y_train)
y_pred = classifier.predict(X_test_vectorized)
accuracy = metrics.accuracy_score(y_test, y_pred)
classification_report = metrics.classification_report(y_test, y_pred)
print(f"Accuracy: {accuracy}")
print(f"Classification Report:\n{classification_report}")
