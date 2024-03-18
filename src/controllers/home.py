from src.resources.folder_paths import *
from src.views.signup import signUpBiometric
from src.views.signin import signInBiometric
from src.controllers.codeface import codeFace
import cv2

info = []

def signUp(inputNameReg, inputUserReg, inputPassReg):
  regName, regUser, regPass = inputNameReg.get(), inputUserReg.get(), inputPassReg.get()
  # Form Incomplete
  if len(regName) == 0 or len(regUser) == 0 or len(regPass) == 0:
      print('FORMULARIO INCOMPLETO')
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

      # Check User
      if regUser in username:
          print('USUARIO REGISTRADO ANTERIORMENTE')

      else:
          # No registred
          info.append(regName)
          info.append(regUser)
          info.append(regPass)

          # Export info
          f = open(f'{outputFolderPathUser}/{regUser}.txt', 'w')
          f.write(f'{regName},')
          f.write(f'{regUser},')
          f.write(regPass)
          f.close()
          signUpBiometric(regUser)

def signIn(inputUserLog, inputPassLog):
    logUser, logPass = inputUserLog.get(), inputPassLog.get()

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
