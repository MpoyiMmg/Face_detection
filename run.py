
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