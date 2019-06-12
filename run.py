import face_detect as fd
import face_recognition as fr

print('---DETECTION DES VISAGES--------')

def main():

    print("------ Face Detect ---------")
    print("1. Detecter sur une photo")
    print("2. Detecter a partir du webcam")
    print("3. Reconnaissance faciale")
    print("0. Quitter")

    choice = int(input("tapez  pour continuer..."))

    if choice == 1 :

        image_path = input("entrez le chemin de l'image a ce format : /chemin/vers/le/fichier.jpg : ")
        fd.detect_simple_image(image_path)

    elif choice == 2:
        fd.detect_by_video_capture()

    elif choice == 3:
        fr.recognize()

    elif choice == 0:
        exit
    
    else :
        main()
    
if(__name__== '__main__'):
    main()