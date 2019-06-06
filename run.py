import cv2 

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

image = cv2.imread( "images/mmg.jpg")
resize_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))

gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)
