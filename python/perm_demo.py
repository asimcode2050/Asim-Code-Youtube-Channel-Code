def check_permutation(str1,str2):
    if str1 is None or str2 is None:
        return False
    return sorted(str1) == sorted(str2)
print(check_permutation("act","cat"))
print(check_permutation("bill","billy"))

