
class Initialise_path():

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

class Face_cascade():

    def __init__(self):
        self.initialise   = Initialise_path()
        self.face_cascade = None
        self.eye_cascade  = None

    def _get_face_cascade(self):
        if(self.face_cascade == None): return self.face_cascade

    def _get_eye_cascade(self):
        if(self.eye_cascade == None): return self.eye_cascade