import face_detect

print('---DETECTION DES VISAGES--------')

def main():
    choice = int(input("tapez sur 0 pour continuer..."))

    if choice == 0 :

        image_path = input("entrez le chemin de l'image a ce format : /chemin/vers/le/fichier.jpg : ")
        face_detect.detect_face(image_path)
    
    else :
        main()
    
if(__name__== '__main__'):
    main()