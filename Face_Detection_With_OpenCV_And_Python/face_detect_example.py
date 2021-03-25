# https://www.youtube.com/watch?v=QKV_bUKz1KY&feature=youtu.be&ab_channel=AsimCode
# sudo apt-get install libopencv-dev python3-opencv python3-numpy python3-scipy
# download the facial detection training file:
# wget http://eclecti.cc/files/2008/03/haarcascade_frontalface_alt.xml

import cv2
import os

IMAGES = '/home/asimcode/images'
FACES = '/home/asimcode/faces'
TRAIN = '/home/asimcode/training'

def face_detect(srcdir=IMAGES, target_dir=FACES,train_dir=TRAIN):
    for fname in os.listdir(srcdir):
        if not fname.upper().endswith('.JPG'):
            continue
        fullname = os.path.join(srcdir,fname)
        newfilename = os.path.join(target_dir,fname)
        img = cv2.imread(fullname)
        if img is None:
            continue
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        training = os.path.join(train_dir, 'haarcascade_frontalface_alt.xml')
        cascade = cv2.CascadeClassifier(training)
        rect_coord = cascade.detectMultiScale(gray,1.3,5)
        try:
            if rect_coord.any():
                print('Face Detected!')
                rect_coord[:, 2:] += rect_coord[:, :2]
        except AttributeError:
            print(f'No faces found : {fname}')
            continue
        for x1,y1, x2, y2 in rect_coord:
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.imwrite(newfilename,img)

if __name__== '__main__':
    face_detect()

