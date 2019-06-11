import os
import cv2
import numpy as np
from PIL import Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')

current_id = 0
labels_id = 0

y_labels = []
x_train  =  []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file)
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            print(label," : ",path)
            y_labels.append(label)
            x_train.append(path) #verifie l'image et la transforme en tableau numpy

            pil_image = Image.open(path).convert("L") #grayscale
            image_array = np.array(pil_image, "uint8")

            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)

            for (x,y,w,h) in faces :

                roi = image_array[y:y+h, x:x+w]
                x_train.append(roi)

            print(image_array)