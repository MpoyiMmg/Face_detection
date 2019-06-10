import cv2 

def detect_simple_image(path):

    face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

    image = cv2.imread(path)
    resize_image = cv2.resize(image, (int(image.shape[1]/2), int(image.shape[0]/2)))

    gray_image = cv2.cvtColor(resize_image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)
    i = 0
    for x,y,w,h in faces:
        image = cv2.rectangle(resize_image, (x,y), (x+w, y+h), (0,255,0), 3)
        i += 1
        
    print(" sur cette image il'ya ",i," faces")
    cv2.imshow("Detect",image)
    cv2.waitKey(0)


# fonction qui permet de detecter la face a partir de la camera du pc
def detect_by_video_capture():

    # chargement du fichier cascade
    face_cascade = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

    # ouverture de la camera
    video = cv2.VideoCapture(0) #0 est pour le webcam du pc; si c'etait une camera externe on mettra 1

    while True:

        _,img = video.read() #lecture de chaque image renvoyée par la webcam 
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # detection des points qui correspond a une face
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for(x, y, w, h) in faces:
            # place du rectangle vert sur la face detecter
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        #affichage du resultat
        cv2.imshow("vide capture", img)
        k =cv2.waitKey(30)
        if k == 27:
            break

    video.release()
