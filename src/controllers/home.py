from src.resources.folder_paths import *
from src.views.signup import signUpBiometric
from src.views.signin import signInBiometric
from src.controllers.codeface import codeFace
import cv2

info = []

def signUp(inputNameReg):
  regName = inputNameReg.get()
  # Form Incomplete
  if len(regName) == 0:
      print('PORFAVOR INGRESE UN NOMBRE')
  else:
      userList = os.listdir(pathUserCheck)
      
      username = []

      # Check user List
      for lis in userList:
          #Extract User
          user = lis
          user = user.split('.')
          # Save User
          username.append(user[0])

      else:
          # No registred
          info.append(regName)

          # Export info
          f = open(f'{outputFolderPathUser}/{regName}.txt', 'w')
          f.write(f'{regName},')
          f.close()
          signUpBiometric(regName)

def signIn():
    # DB Faces
    images = []
    clases = []
    lista = os.listdir(outputFolderPathFace)

    for lis in lista:
        # Read Img
        imgdb = cv2.imread(f'{outputFolderPathFace}/{lis}')
        images.append(imgdb)
        clases.append(os.path.splitext(lis)[0])

    faceCode = codeFace(images)
    signInBiometric(faceCode, clases)
