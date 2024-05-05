from tkinter import Tk, PhotoImage, Label, Entry, Button
from src.resources.img_paths import *
from src.controllers.home import signUp, signIn
from src.views.admin import admin
from src.views.asistencias import asistencias

def home():
    pantalla = Tk()
    pantalla.title('FACE RECOGNITION SYSTEM')
    pantalla.geometry('1280x720')

    # Fondo
    imagenF = PhotoImage(file=imgInicio2)
    background = Label(image=imagenF, text='Inicio')
    background.place(x=0, y=0, relheight=1, relwidth=1)

    # Button
    # Usuarios
    imagenBU = PhotoImage(file=imgBtUsuarios)
    btUsuarios = Button(pantalla, text='Usuarios', image=imagenBU, height='40', width='200', command=lambda: openAdminAndClose(pantalla))
    btUsuarios.place(x=260, y=410)
    
    # SignUp
    imagenBA = PhotoImage(file=imgBtAsistencias)
    btAsistencia = Button(pantalla, text='Asistencias', image=imagenBA, height='40', width='200', command=lambda: openAsistAndClose(pantalla))
    btAsistencia.place(x=260, y=510)

    # LogIn 
    imagenBR = PhotoImage(file=imgBtRegistrarEnt)
    btReg = Button(pantalla, text='RegEntrada', image=imagenBR, height='40', width='200', command=lambda: signIn())
    btReg.place(x=800, y=510)

    pantalla.mainloop()

def openAdminAndClose(pantalla):
    pantalla.destroy()
    admin()

def openAsistAndClose(pantalla):
    pantalla.destroy()
    asistencias()

