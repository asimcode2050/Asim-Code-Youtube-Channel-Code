def binary_search(my_list, key):
    size = len(my_list)
    lower = 0
    upper = size -1
    while lower <= upper:
         middle = (lower+upper) / 2
         if key == my_list[middle]:
             return middle
         else:
             if key < my_list[middle]:
                 upper = middle -1
             else:
                 lower = middle +1 
    return -1

list_1 = [20,50,80,90,100]
key = int(input('Enter key:'))
result = binary_search(list_1,key)
if result >= 0:
    print('Result Index :')
    print(result)

else:
    print('Key not found!')

