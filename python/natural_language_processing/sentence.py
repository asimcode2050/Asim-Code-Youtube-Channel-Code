import nltk
nltk.download('punkt')
text = "Hello! How are you? I hope you're having a great day."
''' (like '.', '?', '!') '''
sentences = nltk.sent_tokenize(text)
print(sentences)
