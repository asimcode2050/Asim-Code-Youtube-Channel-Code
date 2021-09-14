'''
Asim Code
https://youtu.be/L4FSRCdhD0w
Random Password Generator
'''
import random
import string
pass_string  = string.ascii_letters + string.digits + string.punctuation
pass_length = 16
password = "".join(random.sample(pass_string,pass_length))
print(password)
