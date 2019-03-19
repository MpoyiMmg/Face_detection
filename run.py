
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
        self.initialise   = Initialise_path._get_instance()
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
        self.image = None