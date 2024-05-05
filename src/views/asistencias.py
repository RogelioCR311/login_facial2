from datetime import datetime
from src.models.get_data import getAsistData
from src.resources.img_paths import *
import tkinter as tk
from tkinter import Button, PhotoImage, ttk

ID_USER = ''

def refreshData(table):
  collection = getAsistData()

  registers = table.get_children()
  for register in registers:
    table.delete(register)
  for document in collection:
    formattedDate = formatDate(document["time"])
    table.insert('', 0, text=document["_id"], values=(document["name"], document["lastname"], formattedDate))

def formatDate(date_str):
  date = datetime.fromisoformat(str(date_str))
  formattedDate = date.strftime("%H:%M %d/%m/%y")
  return formattedDate


def asistencias():
  window = tk.Tk()
  window.geometry('1280x720')
  window.title('Registro de Asistencias')

  # Fondo
  imagenBase = tk.PhotoImage(file=imgBase)
  background = tk.Label(image=imagenBase, text='Inicio')
  background.place(x=0, y=0, relheight=1, relwidth=1)

  table = ttk.Treeview(window, columns=('Nombre', 'Apellido', 'Asistencia'))
  table.place(x=250, y=150)
  table.heading('#0', text='ID')
  table.heading('#1', text='Nombre')
  table.heading('#2', text='Apellido')
  table.heading('#3', text='Asistencia')

  # Button Return
  imagenReturn = PhotoImage(file=imgRegresar)
  imagenReturn = imagenReturn.subsample(14, 14)
  btRet = Button(window, text='RegEntrada', image=imagenReturn, command=lambda:returnHome(window))
  btRet.place(x=100, y=100)

  refreshData(table)

  window.mainloop()

def returnHome(window):
  window.destroy()
  from src.views.home import home
  home()