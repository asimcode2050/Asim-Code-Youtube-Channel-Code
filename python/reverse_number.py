# https://youtu.be/JId3BOeJGw8
from math import copysign
def rev_number(num):
    return copysign(float(str(num)[::-1].replace('-','')),num)

print(rev_number(321))
print(rev_number(-456))
print(rev_number(75.6))
