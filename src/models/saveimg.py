from src.resources.folder_paths import outputFolderPathFace
from src.models.edit_user import getUserById
from src.controllers.edit_user import editUser
from bson import ObjectId
import cv2

def saveImg(img, id_user):
  userImgOutputFolder = f'{outputFolderPathFace}/{id_user}.png'

  cv2.imwrite(userImgOutputFolder, img)

  document = getUserById(id_user)

  editUser(document["name"], document["lastname"], document["birthdate"], id_user, userImgOutputFolder)






