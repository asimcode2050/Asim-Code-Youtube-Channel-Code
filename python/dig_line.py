'''
Python program to print all lines containing digits
Please Subscribe to Asim Code
https://youtu.be/j_ReWqhKIVg
'''
import re
digit_line = re.compile(r'\d') 
with open('myfile.txt') as f:
    for line in f:
        if digit_line.search(line):
            print(line, end='')
            
