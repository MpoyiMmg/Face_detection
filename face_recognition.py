import numpy as np
import cv2
import pickle

# ouverture de la webcam
cap = cv2.VideoCapture(0)
boolean = True

# chargement du fichier cascade
face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}

with open("labels.pickle", 'rb') as f:
    og_labels = pickle.load(f)
    labels = {v:k for k,v in og_labels.items()}

while(boolean):

    # lecture de l'image cadre par cadre
    ret, frame = cap.read()

    # rendre l'image recue en noir blanc
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # lecture des echelles correspondant a une face
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

    for(x,y,w,h) in faces:
        # cv2.rectangle(frame, (x,y), (x+h, y+w), )
        # print(x,y,w,h)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        id_, conf = recognizer.predict(roi_gray)

        if conf >= 45 and conf <= 85:
            print(id_)
            print(labels[id_])

        img_item = "ma_face.jpg"
        cv2.imwrite(img_item, roi_gray)

        #cadrage de la face
        color = (255, 255, 255)
        stroke = 2
        width = x + w
        height = y + h
        cv2.rectangle(frame, (x, y), (width, height), color, stroke)
    # affichage des resultats
    cv2.imshow('Frame',frame)
    
    if cv2.waitKey(3) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
