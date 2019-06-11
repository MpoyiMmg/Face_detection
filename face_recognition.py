import numpy as np
import cv2

cap = cv2.VideoCapture(0)
boolean = True

while(boolean):

    ret, frame = cap.read()

    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(3) == ord('q'):
        break

cap.release()
