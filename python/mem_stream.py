""" Youtube Channel : Asim Code 
In memory stream in Python
https://youtu.be/bpqBl0Z75EA
"""
import io
stream = io.StringIO()
stream.write('Hello World\n')
print('I love Python programming',file=stream)
contents = stream.getvalue()
print(contents)
stream.close()
