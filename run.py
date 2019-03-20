
import cv2 as opencv

class Initialise_path:

    def __init__(self):
        self.face  = "haarcascades/haarcascade_frontalface_default.xml"
        self.eye   = "haarcascades/haarcascade_eye.xml"
        self.image = "/home/gaelmmg/Pictures/IMG-20190220-WA0018.jpg"

    def _get_face(self):
        return self.face

    def _get_eye(self):
        return self.eye

    def _get_image(self):
        return self.image

    def _get_instance(self):
        return Initialise_path()
    
# =============================================================================>

class Face_cascade:

    def __init__(self):
        self.initialise   = None
        self.face_cascade = None
        self.eye_cascade  = None

    def _get_face_cascade(self):
        return self.face_cascade

    def _get_eye_cascade(self):
        return self.eye_cascade
    
    def _set_face_cascade(self, face_cascade): 
        if(self.face_cascade == None) : self.face_cascade = face_cascade
        
    def _set_eye_cascade(self, eye_cascade):
        if(self.eye_cascade == None): self.eye_cascade = eye_cascade

# ==============================================================================>

class Image_Treat:

    def __init__(self):
        self.initialise = Initialise_path()
        self.image      = self.initialise._get_image()
        self.image_load = opencv.imread(self.image)
        self.gray       = opencv.cvtColor(self.image_load, opencv.COLOR_BGR2GRAY)

    def _get_image(self):
        return self.image_load
    
    def _get_gray(self):
        return self.gray

# ==============================================================================>

class Face_Recognition:

    def __init__(self):
        self.face_instance  = Face_cascade()
        self.image_instance = Image_Treat()
        self.face_cascade   = None
        self.eye_cascade    = None
        self.image          = None
        self.gray           = None

    def face(self):
        self.face_cascade = opencv.CascadeClassifier(self.face_instance._get_face_cascade())
        self.eye_cascade  = opencv.CascadeClassifier(self.face_instance._get_eye_cascade())

        self.image        = self.image_instance._get_image()
        self.gray         = self.image_instance._get_gray()

        faces             = self.face_cascade.detectMultiScale(self.gray)

        return faces

    def recognition(self):
        faces = self.face()

        for(x,y,w,h) in faces:
            self.image = opencv.rectangle(self.image, (x,y), (x+w, y+h),(255,0,0), 2)

            roi_gray = self.gray[y:y+h, x:x+h]
            roi_eye  = self.image[y:y+h, x:x+h]
            eyes     = self.eye_cascade.detectMultiScale(roi_gray)

            for (ex,ey,eh,ew) in eyes:
                opencv.rectangle(roi_eye, (ex,ey), (ex+ew, ey+eh),(255,255,0),2)
        return self.image

    
    def display(self):
        img = self.recognition() 
        opencv.imshow("image",img)
        opencv.waitKey(0)
        opencv.destroyWindow("test")

# ===============================================================================>

class Main:
