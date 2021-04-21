# https://youtu.be/7fcbRAv0-V0
def sort_dict_value(my_dict,reverse = False):
    return dict(sorted(my_dict.items(),key = lambda x: x[1], reverse = reverse))

our_dict = {'one':1,'three':3,'five':5,'six':6,'two':2,'four':4}
print(sort_dict_value(our_dict))
print(sort_dict_value(our_dict, True))
