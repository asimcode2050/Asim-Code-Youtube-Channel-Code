def check_unique_chars(string):
    if string is None:
        return False
    for char in string:
        if string.count(char) > 1:
            return False
    return True
print(check_unique_chars("cat"))
print(check_unique_chars("foo"))