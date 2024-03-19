from tkinter import Tk, PhotoImage, Label, Entry, Button
from src.resources.img_paths import *
from src.controllers.home import signUp, signIn

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
    inputNameReg.place(x=300, y=420)

    # Button
    # SignUp
    imagenBR = PhotoImage(file=imgBtnSignUp)
    btReg = Button(pantalla, text='Registro', image=imagenBR, height='40', width='200')
    btReg = Button(pantalla, text='Registro', image=imagenBR, height='40', width='200', command=lambda: signUp(inputNameReg))
    btReg.place(x=260, y=510)

    # LogIn 
    imagenBL = PhotoImage(file=imgBtnSignIn)
    btLog = Button(pantalla, text='Inicio', image=imagenBL, height='40', width='200')
    btLog = Button(pantalla, text='Inicio', image=imagenBL, height='40', width='200', command=lambda: signIn())
    btLog.place(x=800, y=510)

    pantalla.mainloop()