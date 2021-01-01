LIST_SIZE = 20
C_List = []
F_List = []
for i in range(1,LIST_SIZE+1):
    c_item = i*5
    C_List.append(c_item)
    f_item = c_item * (9.0/5.0) + 32.0
    F_List.append(f_item)

print("Temperature in Celsius:")
print(C_List)
print("Temperature in Fahrenheit:")
print(F_List)
