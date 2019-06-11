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


    # affichage des resultats
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(3) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
