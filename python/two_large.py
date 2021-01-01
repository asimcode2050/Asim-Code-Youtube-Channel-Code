def find_two_largest(my_list):
    max_value, second = my_list[:2]
    if max_value < second:
        max_value,second = second,max_value

    for i in range(2,len(my_list)):
        if max_value < my_list[i]:
            max_value, second = my_list[i],max_value
        elif second < my_list[i]:
            second = my_list[i]
        
    return (max_value,second)

list1 = [10,2,3,9,5,4,1]
print(find_two_largest(list1))