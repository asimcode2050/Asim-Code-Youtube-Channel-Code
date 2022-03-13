"""
How to extract date from a text string in Python
https://youtu.be/z_855JguorQ
Please Subscribe to Asim Code.
"""
import re
text = 'Today is 3/14/2022 and Tomorrow is 3/15/2022.'
print(re.findall(r'\d+/\d+/\d+',text))
