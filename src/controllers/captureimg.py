from src.resources.img_paths import *
from src.resources.folder_paths import *
from src.models.saveimg import saveImg
from src.controllers.comparefaces import compareFaces
import cv2
import mediapipe as mp
from tkinter import *
from PIL import Image, ImageTk
import imutils
import math
import time

# Variables
parpadeo = False
conteo = 0
muestra = 0
step = 0

# Offset
offsety = 30
offsetx = 20

# Threshold
confThreshold = 0.5

# Tool Draw
mpDraw = mp.solutions.drawing_utils
configDraw = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

# Object Face Mesh
faceMeshObject = mp.solutions.face_mesh
faceMesh = faceMeshObject.FaceMesh(max_num_faces=1)

# Object Detect
faceObject = mp.solutions.face_detection
detector = faceObject.FaceDetection(min_detection_confidence= 0.5, model_selection=1)

# Read img
imgStep0 = cv2.imread(imgStep0)
imgStep1 = cv2.imread(imgStep1)
imgStep2 = cv2.imread(imgStep2)
imgCheck = cv2.imread(imgCheck)
imgLiveness = cv2.imread(imgLiveness)

def captureImg(cap, lblVideo, pantalla, method, regUser="", faceCode = "", clases = ""):
    global step, parpadeo, muestra, conteo
    # Check Cap
    if cap is not None:
        ret, frame = cap.read()

        # Resize
        frame = imutils.resize(frame, width=1280)

        # RGB
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frameSave = frame.copy()

        # Frame show
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        if ret == True:
            # Interference Face Mesh
            res = faceMesh.process(frameRGB)

            # Result List
            px = []
            py = []
            lista = []

            if res.multi_face_landmarks:
                # Extract Face Mesh
                for rostros in res.multi_face_landmarks:
                    # Draw
                    mpDraw.draw_landmarks(frame, rostros, faceMeshObject.FACEMESH_CONTOURS, configDraw, configDraw)

                    # Extract KeyPoint
                    for id, puntos in enumerate(rostros.landmark):
                        # Info img
                        al, an, c = frame.shape
                        x, y = int(puntos.x * an), int(puntos.y * al)
                        px.append(x)
                        py.append(y)
                        lista.append([id, x, y])

                        # 468 KeyPoints
                        if len(lista) == 468:
                            # Ojo derecho
                            x1, y1 = lista[145][1:]
                            x2, y2 = lista[159][1:]
                            longitud1 = math.hypot(x2-x1, y2-y1)
                            
                            # Ojo derecho
                            x3, y3 = lista[374][1:]
                            x4, y4 = lista[386][1:]
                            longitud2 = math.hypot(x4-x3, y4-y3)

                            # Parietal derecho
                            x5, y5 = lista[139][1:]

                            #Parietal izquierdo
                            x6, y6 = lista[368][1:]

                            # Ceja derecha
                            x7, y7 = lista[70][1:]
                            x8, y8 = lista[300][1:]


                            #Face Detect
                            faces = detector.process(frameRGB)

                            if faces.detections is not None:
                                for face in faces.detections:
                                    # Bbox: "ID, BBOX, SCORE"
                                    score = face.score
                                    score = score[0]
                                    bbox = face.location_data.relative_bounding_box

                                    # Threshold
                                    if score > confThreshold:
                                        # Pixels
                                        xi, yi, anc, alt = bbox.xmin, bbox.ymin, bbox.width, bbox.height
                                        xi, yi, anc, alt = int(xi * an), int(yi * al), int(anc * an), int(alt * al)

                                        # Offset X
                                        offsetan = (offsetx / 100 ) * anc
                                        xi = int(xi - int(offsetan/2))
                                        anc = int(anc + offsetan)
                                        xf = xi + anc

                                        # Offset Y
                                        offsetal = (offsety / 100 ) * alt
                                        yi = int(yi - int(offsetal/2))
                                        alt = int(alt + offsetal)
                                        yf = yi + alt
                                        
                                        # Error
                                        if xi < 0 : xi = 0
                                        if yi < 0 : yi = 0
                                        if anc < 0 : anc = 0
                                        if alt < 0 : alt = 0
                                        
                                        # Steps
                                        if step == 0:
                                            # Draw
                                            cv2.rectangle(frame, (xi, yi, anc, alt), (255, 255, 255), 2)

                                            # IMG Step0
                                            als0, ans0, c = imgStep0.shape
                                            frame[50:50 + als0, 50:50 + ans0] = imgStep0
                                            # IMG Step1
                                            als1, ans1, c = imgStep1.shape
                                            frame[50:50 + als1, 1030:1030 + ans1] = imgStep1
                                            # IMG Step2
                                            als2, ans2, c = imgStep2.shape
                                            frame[270:270 + als2, 1030:1030 + ans2] = imgStep2

                                            # Face Center
                                            if x7 > x5 and x8 < x6:
                                                #IMG Check
                                                # IMG Step2
                                                alch, anch, c = imgCheck.shape
                                                frame[165:165 + alch, 1105:1105 + anch] = imgCheck
                                                # Conteo Parpadeo
                                                if longitud1 <= 18 and longitud2 <= 18 and parpadeo == False:
                                                    conteo = conteo + 1
                                                    parpadeo = True
                                                elif longitud1 > 18 and longitud2 > 18 and parpadeo == True:
                                                    parpadeo = False

                                                cv2.putText(frame, f'Parpadeos: {int(conteo)}', (1070, 375), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255,255), 1)
                                                
                                                if conteo >= 3:
                                                    # IMG Check
                                                    alch, anch, c = imgCheck.shape
                                                    frame[385:385 + alch, 1105:1105 + anch] = imgCheck

                                                    # Open Eyes
                                                    if longitud1 > 20 and longitud2 > 20:
                                                        cut = frameSave[yi:yf, xi:xf]                 
                                                        step = 1

                                            else:
                                                conteo = 0
                                        
                                        if step == 1:
                                            # Draw
                                            cv2.rectangle(frame, (xi, yi, anc, alt), (0, 255, 0), 2)
                                            # IMG Check Liveness
                                            alli, anli, c = imgLiveness.shape
                                            frame[50:50 + alli, 50:50 + anli] = imgLiveness
        
                                            if method == 'signUp':
                                                saveImg(cut, regUser)
                                            elif method == "signIn":
                                                compareFaces(faceCode, clases, frameRGB)
                                            time.sleep(7)
                                            closeWindow(pantalla)
                                            return

        # Convert video
        im = Image.fromarray(frame)
        img = ImageTk.PhotoImage(image=im)

        # Show video
        lblVideo.configure(image=img)
        lblVideo.image = img
        lblVideo.after(10, lambda: captureImg(cap, lblVideo, pantalla, method, regUser, faceCode, clases))
    
    else:
        cap.release()

def closeWindow(pantalla):
    global step, conteo
    conteo = 0
    step = 0
    pantalla.destroy()