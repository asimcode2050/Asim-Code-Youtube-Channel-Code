'''
Calculator for average in Python
Please Subscribe to Asim Code
https://youtu.be/heKTN0F_9JA
'''
our_list = list()

while True:
    value = input(f"Please enter a number , (Enter end to begin calculation):")
    if value == 'end':
        break
    our_value = float(value)
    our_list.append(our_value)
average = sum(our_list) / len(our_list)
print(f"The Numbers are : {our_list}")
print(f"Average is :", average)
