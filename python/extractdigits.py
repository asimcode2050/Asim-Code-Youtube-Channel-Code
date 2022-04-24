'''
How To extract the digits of a number in Python
Please Subscribe to Asim Code
https://youtu.be/Bu7gXGE8-dY
'''
def digits_from_number(number):
    value = number
    while value > 0:
        digit = value % 10
        value  = value // 10
        print(digit, end= ' ')
    print()

digits_from_number(76589)
