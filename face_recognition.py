import numpy as np
import cv2

cap = cv2.VideoCapture(0)
boolean = True

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

while(boolean):

    ret, frame = cap.read()

    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(3) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
