import numpy as np
import cv2

# ouverture de la webcam
cap = cv2.VideoCapture(0)
boolean = True

# chargement du fichier cascade
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

while(boolean):

    # lecture de l'image cadre par cadre
    ret, frame = cap.read()

    # rendre l'image recue en noir blanc
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # lecture des echelles correspondant a une face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for(x,y,w,h) in faces:
        # cv2.rectangle(frame, (x,y), (x+h, y+w), )
        print(x,y,w,h)
        
        roi_gray = gray[y:y+h, x:x+w]
        img_item = "ma_face.jpg"
        cv2.imwrite(img_item, roi_gray)
    # affichage des resultats
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(3) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
