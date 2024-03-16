from tkinter import Tk, PhotoImage, Label, Entry, Button
from src.resources.img_paths import *

def home():
    pantalla = Tk()
    pantalla.title('FACE RECOGNITION SYSTEM')
    pantalla.geometry('1280x720')

    # Fondo
    imagenF = PhotoImage(file=imgInicio)
    background = Label(image=imagenF, text='Inicio')
    background.place(x=0, y=0, relheight=1, relwidth=1)

    # Input text
    # Name
    inputNameReg = Entry(pantalla)
    inputNameReg.place(x=110, y=320)

    # User
    inputUserReg = Entry(pantalla)
    inputUserReg.place(x=110, y=430)

    # Pass
    inputPassReg = Entry(pantalla)
    inputPassReg.place(x=110, y=540)

    # Input Text Sign Up
    # User
    inputUserLog = Entry(pantalla)
    inputUserLog.place(x=730, y=420)

    # Pass
    inputPassLog = Entry(pantalla)
    inputPassLog.place(x=730, y=530)

    # Button
    # SignUp
    imagenBR = PhotoImage(file=imgBtnSignUp)
    btReg = Button(pantalla, text='Registro', image=imagenBR, height='40', width='200')
    # btReg = Button(pantalla, text='Registro', image=imagenBR, height='40', width='200', command=signUp)
    btReg.place(x=300, y=580)

    # LogIn 
    imagenBL = PhotoImage(file=imgBtnSignIn)
    btLog = Button(pantalla, text='Inicio', image=imagenBL, height='40', width='200')
    # btLog = Button(pantalla, text='Inicio', image=imagenBL, height='40', width='200', command=signIn)
    btLog.place(x=800, y=580)

    pantalla.mainloop()