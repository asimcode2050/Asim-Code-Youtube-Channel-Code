import string
text = """Hello World!
Hi There! 
Who are you?"""
trans = str.maketrans('','',string.punctuation)
text = text.lower().translate(trans)
print(text)
