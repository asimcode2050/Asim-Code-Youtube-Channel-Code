import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
stemmer = PorterStemmer()
sentence = "Running runs ran easily"
words = nltk.word_tokenize(sentence)
stemmed_words = [stemmer.stem(word) for word in words]
print("Original Words:", words)  # Output the list of original words.
print("Stemmed Words:", stemmed_words)  # Output the list of stemmed words.
