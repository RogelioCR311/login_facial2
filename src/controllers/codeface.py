import cv2
import face_recognition as fr

def codeFace(images):
    listacod = []

    # Iteramos
    for img in images:
        # Color
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # IMG Code
        cod = fr.face_encodings(img)[0]
        # Save List
        listacod.append(cod)
    
    return listacod