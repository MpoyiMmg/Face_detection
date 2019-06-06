import cv2 

face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

image = "images/mmg.jpg"
resize_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))