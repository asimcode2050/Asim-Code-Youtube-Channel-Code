def rev_string_1(string):
    if string:
        return string[::-1]
    return string

def rev_string_2(string):
    if string:
        return ''.join(reversed(string))
    return string

print(rev_string_1("car"))
print(rev_string_2("foo"))