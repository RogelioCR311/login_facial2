import cv2
from tkinter import *
import tkinter as tk
from src.controllers.captureimg import captureImg

def signInBiometric(faceCode, clases):
  # New screen
  pantalla2 = tk.Toplevel()
  pantalla2.title('LOGIN BIOMETRIC')
  pantalla2.geometry('1280x720')

  # Label Video
  lblVideo = Label(pantalla2)
  lblVideo.place(x=0, y=0)

  # Videocaptura
  cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
  cap.set(3, 1280)
  cap.set(4, 720)
  captureImg(cap, lblVideo, pantalla2, "signIn", "", faceCode, clases)