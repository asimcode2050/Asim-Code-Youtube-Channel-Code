def binary_search(my_list,key):
    size = len(my_list)
    lower = 0
    upper = size -1
    while lower <= upper:
        middle = (lower + upper) / 2
        if key == my_list[middle]:
            return middle
        else:
            if key < my_list[middle]:
                upper = middle -1
            else:
                lower = middle +1
    return -1

list_1 = [50,80,100,200,350]
key = int(input('Please enter key:'))
result = binary_search(list_1,key)
if result >= 0:
    print("Result index :")
    print(result)
else:
    print("No key found!")