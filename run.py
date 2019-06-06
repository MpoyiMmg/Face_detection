import face_detect

print('---DETECTION DES VISAGES--------')

def main():
    choice = int(input("tapez sur 0 pour continuer..."))

    if choice == 0 :
        face_detect.detect_face()
    
    else :
        main()
    
if(__name__== '__main__'):
    main()