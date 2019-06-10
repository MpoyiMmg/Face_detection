import face_detect

print('---DETECTION DES VISAGES--------')

def main():

    print("------ Face Detect ---------")
    print("1. Detecter sur une photo")
    print("2. Detecter a partir du webcam")
    print("0. Quitter")

    choice = int(input("tapez  pour continuer..."))

    if choice == 1 :

        image_path = input("entrez le chemin de l'image a ce format : /chemin/vers/le/fichier.jpg : ")
        face_detect.detect_simple_image(image_path)

    elif choice == 2:
        face_detect.detect_by_video_capture()
    
    else :
        main()
    
if(__name__== '__main__'):
    main()