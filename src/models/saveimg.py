import cv2
from src.resources.folder_paths import outputFolderPathFace

def saveImg(img, regUser):
  cv2.imwrite(f'{outputFolderPathFace}/{regUser}.png', img)
