import pyscreenshot as ImageGrab
import ftplib
img = ImageGrab.grab()
img.save('screen.png')
session =ftplib.FTP('yourserver.com','username','password')
f=open('screen.png','rb')

session.storbinary('STOR screen.png',f)
f.close()
session.quit()

