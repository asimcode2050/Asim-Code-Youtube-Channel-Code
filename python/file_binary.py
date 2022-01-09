"""
Reading and writing files in binary mode in Python
Youtube Channel : Asim Code
https://youtu.be/2PvHHZBiy0Y
"""
with open('demo.bin','wb') as file:
    file.write(b'Hello world in binary')
    
with open('demo.bin','rb') as f:
    print(f.read())
