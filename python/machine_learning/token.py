import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
text = "Hello there! How are you doing today? I hope everything is fine."
tokens = nltk.word_tokenize(text)
''' ['Hello', 'there', '!'] '''
print(tokens)
