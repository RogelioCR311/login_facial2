from src.views.welcome import welcome
import face_recognition as fr
import numpy as np

def compareFaces(faceCode, clases, frameRGB):
  # Find Faces
  facess = fr.face_locations(frameRGB)
  facescod = fr.face_encodings(frameRGB, facess)
  # Iteramos
  for facecod, facesloc in zip(facescod, facess):

      # Matching
      match = fr.compare_faces(faceCode, facecod)

      # Sim
      simi = fr.face_distance(faceCode, facecod)

      # Min
      min = np.argmin(simi)
      if match[min]:
        username = clases[min]
        welcome(username, clases)
      else:
        return