import re
s = "hello hello 2 2 hi there"
patt = r'(\b\w+\b)\W\1'
print(re.findall(patt,s))