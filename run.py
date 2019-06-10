import face_detect

print('---DETECTION DES VISAGES--------')

def main():

    print("------ Face Detect ---------")
    print("1. Detecter sur une photo")
    print("2. Detecter a partir du webcam")
    print("0. Quitter")
    choice = int(input("tapez  pour continuer..."))

    if choice == 0 :

        image_path = input("entrez le chemin de l'image a ce format : /chemin/vers/le/fichier.jpg : ")
        face_detect.detect_face(image_path)
    
    else :
        main()
    
if(__name__== '__main__'):
    main()