from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
text = "This is a simple sentence, and it contains stopwords like the, and, or, is."
words = text.split()
print("Original Words:", words)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
print("Filtered Words:", filtered_words)
