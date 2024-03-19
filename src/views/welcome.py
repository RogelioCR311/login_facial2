import cv2
import tkinter as tk
from tkinter import Label, PhotoImage
from PIL import Image, ImageTk
from src.resources.img_paths import *
from src.resources.folder_paths import outputFolderPathUser, outputFolderPathFace

def welcome(username, clases):
    # Window
    pantalla4 = tk.Toplevel()
    pantalla4.title('PROFILE')
    pantalla4.geometry("1280x720")

    # Background
    imagenbc = PhotoImage(file=imgBackground2)
    bc = Label(pantalla4, image=imagenbc, text='Bienvenido')
    bc.place(x=0, y=0, relheight=1, relwidth=1)
    bc.image = imagenbc

    # File
    userFile = open(f'{outputFolderPathUser}/{username}.txt', 'r')
    infoUser = userFile.read().split(',')
    name = infoUser[0]

    if name in clases:
        texto1 = Label(pantalla4, text=f'BIENVENIDO {name}')
        texto1.place(x=580, y=50)

        # label Img
        lblimage = Label(pantalla4)
        lblimage.place(x=490, y=80)

        imgUser = cv2.imread(f'{outputFolderPathFace}/{name}.png')
        imgUser = cv2.cvtColor(imgUser, cv2.COLOR_RGB2BGR)
        imgUser = Image.fromarray(imgUser)
        imgUser = imgUser.resize((325,325))

        IMG = ImageTk.PhotoImage(image=imgUser)

        lblimage.configure(image=IMG)
        lblimage.image = IMG