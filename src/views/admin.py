from src.views.create_user import createUser
from src.models.delete_data import deleteData
from src.models.edit_user import getUserById
from src.models.get_data import getData
from src.views.edit_user import editUserView
from src.resources.img_paths import *
import tkinter as tk
from tkinter import ttk

ID_USER = ''

def refreshData(table, create, edit, delete):
  collection = getData()

  registers = table.get_children()
  for register in registers:
    table.delete(register)
  for document in collection:
    table.insert('', 0, text=document["_id"], values=(document["name"], document["lastname"]))
  
  create["state"] = "normal"
  edit["state"] = "disabled"
  delete["state"] = "disabled"

def doubleClickTable(table, create, edit, delete):
  global ID_USER
  ID_USER = str(table.item(table.selection())['text'])
  # document = collection.find({"_id":ObjectId(ID_USER)})[0]
  create["state"] = "disabled"
  edit["state"] = "normal"
  delete["state"] = "normal"

def admin():
  window = tk.Tk()
  window.geometry('1280x720')
  window.title('Administracion')

  # Fondo
  imagenF = tk.PhotoImage(file=imgBase)
  background = tk.Label(image=imagenF, text='Inicio')
  background.place(x=0, y=0, relheight=1, relwidth=1)

  table = ttk.Treeview(window, columns=('Nombre', 'Apellido'))
  table.place(x=350, y=150)
  table.heading('#0', text='ID')
  table.heading('#1', text='Nombre')
  table.heading('#2', text='Apellido')

  # Button create
  create = tk.Button(window, text='Crear Usuario', command=lambda:createUser(), bg='green', fg='white')
  create.place(x=460, y=100)

  # Button edit
  edit = tk.Button(window, text='Editar Usuario', command=lambda:editUserById(), bg='yellow', fg='black')
  edit.place(x=560, y=100)
  edit["state"] = "disabled"

  # Button delete
  delete = tk.Button(window, text='Eliminar Usuario', command=lambda:deleteAndRefresh(table, create, edit, delete), bg='red', fg='black')
  delete.place(x=660, y=100)
  delete["state"] = "disabled"
  
  # Button Refresh
  refresh = tk.Button(window, text='Refrescar Tabla', command=lambda:refreshData(table, create, edit, delete), bg='pink', fg='black')
  refresh.place(x=770, y=100)

  table.bind('<Double-Button-1>', lambda event: doubleClickTable(table, create, edit, delete))

  refreshData(table, create, edit, delete)

  window.mainloop()

def deleteAndRefresh(table, create, edit, delete):
  deleteData(ID_USER)
  refreshData(table, create, edit, delete)

def editUserById():
  document = getUserById(ID_USER)
  editUserView(document, ID_USER)
