def find_diff(d1,d2):
    result = {}
    uniq_keys = d1.keys() | d2.keys()

    for key in uniq_keys:
        if d1.get(key) != d2.get(key):
            result[key] = [d1.get(key),d2.get(key)]
    
    return result

a1 = {'a':4,'b':5,'c':6}
a2 = {'a':4,'b':5,'c':8}
print(find_diff(a1,a2))