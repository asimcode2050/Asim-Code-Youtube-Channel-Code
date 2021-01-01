import difflib
s1 = 'My name is Asim'
s2 = 'My name is Peter'
s3 = 'Hello World'
print(difflib.SequenceMatcher(None,s1,s3,False).ratio())