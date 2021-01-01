def keysForValue(my_dict, value):
    foundKeys = []
    for keys in my_dict:
        if my_dict[keys] == value:
            foundKeys.append(keys)
    return foundKeys

our_dict = {'a':100,'b':200,'c':100,'d':500}
print(keysForValue(our_dict,100))
print(keysForValue(our_dict,200))