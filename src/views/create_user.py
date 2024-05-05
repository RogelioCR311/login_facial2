import tkinter as tk
from tkinter import Label, PhotoImage, ttk
from tkcalendar import Calendar
from src.resources.img_paths import *
from src.controllers.save_user import saveUser

def popup(window, fecha_nac):
    win = tk.Toplevel(window)
    cal = Calendar(win)
    cal.pack()
    ttk.Button(win, text="Seleccionar Fecha", command=lambda: select_date(cal, fecha_nac)).pack()

def select_date(cal, fecha_nac):
    fecha_nac.config(state='normal')
    fecha_nac.delete(0, tk.END)
    fecha_nac.insert(0, cal.get_date())
    fecha_nac.focus_set()
    fecha_nac.config(state='readonly')

def createUser():
  window = tk.Toplevel()
  window.title('Crear Usuario')
  window.geometry('500x400')

  imagenbc = PhotoImage(file=imgForms)
  bc = Label(window, image=imagenbc, text='Bienvenido')
  bc.place(x=0, y=0, relheight=1, relwidth=1)
  bc.image = imagenbc

  # Name
  tk.Label(window, text='Nombre').place(x=50, y=50)
  nombre = tk.Entry(window)
  nombre.place(x=160, y=50)

  # Lastname
  tk.Label(window, text='Apellido').place(x=50, y=80)
  apellido = tk.Entry(window)
  apellido.place(x=160, y=80)

  # Birthdate
  btnFechaTxt = f'''Seleccionar Fecha
  de Nacimiento'''
  fecha_nac = ttk.Entry(window, state='readonly')
  fecha_nac.place(x=160, y=110)
  popup_btn = ttk.Button(window, text=btnFechaTxt, command=lambda:popup(window, fecha_nac))
  popup_btn.place(x=50, y=110)

  # Button Create
  accept = tk.Button(window, text='Aceptar', command=lambda:saveAndClose(nombre.get(), apellido.get(), fecha_nac.get(), window), bg='green', fg='white')
  accept.place(x= 100, y=180)
  
  # Button Cancel
  cancel = tk.Button(window, text='Cancelar', command=lambda:closeWindow(window), bg='red', fg='white')
  cancel.place(x= 180, y=180)

def saveAndClose(nombre, apellido, fecha_nac, window):
  saveUser(nombre, apellido, fecha_nac)
  window.destroy()
  
def closeWindow(window):
   window.destroy()

