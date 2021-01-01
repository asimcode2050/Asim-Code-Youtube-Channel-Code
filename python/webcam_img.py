import cv2
vid = cv2.VideoCapture(0)
if not vid.isOpened():
    raise IOError("Cannot open our webcam!")
while True:
    ret, frame = vid.read()
    frame = cv2.resize(frame,None, fx=0.5, fy=0.5,interpolation=cv2.INTER_AREA)
    cv2.imgshow('Frame',frame)  
    our_key = cv2.waitKey(1)
    if our_key == 27:
        break
vid.release()
cv2.destroyAllWindows()
 
