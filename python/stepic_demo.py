from PIL import Image
import stepic
img  = Image.open("screen.png")
img2 = stepic.encode(img,b'Hidden text')
img2.save('secret.png','PNG')
img2 = Image.open('secret.png')
data = stepic.decode(img2)
print("Decoded data :"+str(data))