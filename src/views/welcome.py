from src.resources.img_paths import *
from src.resources.folder_paths import outputFolderPathFace
from tkinter import Label, PhotoImage
import tkinter as tk
from PIL import Image, ImageTk
import cv2
from src.controllers.save_checkin import saveCheckIn

def welcome(id_user, clases):
    # Window
    pantalla4 = tk.Toplevel()
    pantalla4.title('PROFILE')
    pantalla4.geometry("1280x720")

    # Background
    imagenbc = PhotoImage(file=imgBackground2)
    bc = Label(pantalla4, image=imagenbc, text='Bienvenido')
    bc.place(x=0, y=0, relheight=1, relwidth=1)
    bc.image = imagenbc

    if id_user in clases:
        saveCheckIn(id_user)

        # label Img
        lblimage = Label(pantalla4)
        lblimage.place(x=490, y=80)

        imgUser = cv2.imread(f'{outputFolderPathFace}/{id_user}.png')
        imgUser = cv2.cvtColor(imgUser, cv2.COLOR_RGB2BGR)
        imgUser = Image.fromarray(imgUser)
        imgUser = imgUser.resize((325,325))

        IMG = ImageTk.PhotoImage(image=imgUser)

        lblimage.configure(image=IMG)
        lblimage.image = IMG
