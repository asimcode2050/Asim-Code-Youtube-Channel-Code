'''
YouTube Channel:  Asim Code
Text to speech in Python
https://youtu.be/vsmDImERR_w

'''
from gtts import gTTS
import os
file = open("D:\\youtube\\asim_code\\python\\video\\readme.txt","r").read()
speech = gTTS(text=file, lang='en',slow=False)
speech.save("D:\\youtube\\asim_code\\python\\video\\audio.mp3")
os.system("D:\\youtube\\asim_code\\python\\video\\audio.mp3")
