'''
How to remove images background with Rembg using Python
https://youtu.be/tT2WZrXrSM0
YouTube Channel : Asim Code
'''
from rembg import remove

input_image ='animal.jpg'
output_image = 'out.jpg'
with open(input_image,'rb') as i:
    with open(output_image,'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)
