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

    # premier choix est la detection du visage sur une image simple
    if choice == 1 :
        image_path = input("entrez le chemin de l'image a ce format : /chemin/vers/le/fichier.jpg : ")
        fd.detect_simple_image(image_path)

    # deuxieme choix est la detection du visage a partir d'une webcam
    elif choice == 2:
        fd.detect_by_video_capture()

    # troisieme choix est la Reconnaissance faciale a partir de la webcam
    elif choice == 3:
        print("1. Utiliser la webcam")
        print("2. Importer une video")
        print("2. simple image")

        ch = int(input("Faites le choix : "))

        if ch == 1:
            fr.recognize()

        elif ch == 2:
            print("...en cours de conception")

        elif ch == 3:
            print("...en cours de conception")

        else : 
            run()


    elif choice == 0:
        exit
    
    else :
        main()
    
if(__name__== '__main__'):
    main()