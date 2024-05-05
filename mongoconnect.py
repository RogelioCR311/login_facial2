import tkinter as tk
from tkinter import END, Button, Entry, Label, PhotoImage, ttk
from src.resources.img_paths import imgBase
from tkinter import messagebox
import pymongo
from bson.objectid import ObjectId
import pymongo.errors
from tkcalendar import Calendar

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS="face-checkin"
MONGO_COLECCION="users"

ID_USER=""

client=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
database=client[MONGO_BASEDATOS]
collection=database[MONGO_COLECCION]
print(collection)

def popup():
    win = tk.Toplevel(window)
    cal = Calendar(win)
    cal.pack()
    ttk.Button(win, text="Seleccionar Fecha", command=lambda: select_date(cal)).pack()

def select_date(cal):
    fecha_nac.config(state='normal')
    fecha_nac.delete(0, tk.END)
    fecha_nac.insert(0, cal.get_date())
    fecha_nac.focus_set()
    fecha_nac.config(state='readonly')

def showData():
  try: 
    registers = table.get_children()
    for register in registers:
      table.delete(register)
    for document in collection.find():
      table.insert('', 0, text=document["_id"], values=(document["name"], document["lastname"]))
      pass
  except pymongo.errors.ServerSelectionTimeoutError as timeExeption:
    print(f'Time exceded: {timeExeption}')
  except pymongo.errors.ConnectionFailure as connectionError: 
    print(f'Failed to connect to Mongo {connectionError}')

def saveUser():
  if len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(fecha_nac.get()) != 0:
    try:     
      document = {
          "name": nombre.get(), 
          "lastname": apellido.get(), 
          "birthdate": fecha_nac.get()
        }
      collection.insert_one(document)
      nombre.delete(0, END)
      apellido.delete(0, END)
      fecha_nac.delete(0, END)
    except pymongo.errors.ConnectionFailure as error:
      print(error)
  else:
    messagebox.showerror(message='Los campos no pueden estar vacios')
  showData()

def doubleClickTable(event):
  global ID_USER
  ID_USER = str(table.item(table.selection())['text'])
  fecha_nac.config(state='normal')
  document = collection.find({"_id":ObjectId(ID_USER)})[0]
  nombre.delete(0, END)
  nombre.insert(0, document["name"])
  apellido.delete(0, END)
  apellido.insert(0, document["lastname"])
  fecha_nac.delete(0, END)
  fecha_nac.insert(0, document["birthdate"])
  create["state"] = "disabled"
  edit["state"] = "normal"
  fecha_nac.config(state='readonly')
  create["state"] = "disabled"
  edit["state"] = "normal"
  delete["state"] = "normal"

def editUser():
  global ID_USER
  if len(nombre.get()) != 0 and len(apellido.get()) != 0 and len(fecha_nac.get()) != 0:
    try:
      idSearch={"_id":ObjectId(ID_USER)}
      newValues = {
        "$set": {
          "name": nombre.get(), 
          "lastname": apellido.get(), 
          "birthdate": fecha_nac.get()
        }
      }
      collection.update_one(idSearch, newValues)
      nombre.delete(0, END)
      apellido.delete(0, END)
      fecha_nac.config(state='normal')
      fecha_nac.delete(0, END)
      fecha_nac.config(state='readonly')
    except pymongo.errors.ConnectionFailure as error:
      print(error)
  else:
    messagebox.showerror(message='Los campos no pueden estar vacios')
  showData()
    
  create["state"] = "normal"
  edit["state"] = "disabled"

def deleteUser():
  global ID_USER
  try:
    idSearch={"_id":ObjectId(ID_USER)}
    collection.delete_one(idSearch)
    nombre.delete(0, END)
    apellido.delete(0, END)
    fecha_nac.config(state='normal')
    fecha_nac.delete(0, END)
    fecha_nac.config(state='readonly')
  except pymongo.errors.ConnectionFailure as error:
    print(error)
  create["state"] = "normal"
  edit["state"] = "disabled"
  delete["state"] = "disabled"
  showData()

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

# Name
tk.Label(window, text='Nombre').place(x=500, y=400)
nombre = tk.Entry(window)
nombre.place(x=650, y=400)

# Lastname
tk.Label(window, text='Apellido').place(x=500, y=430)
apellido = tk.Entry(window)
apellido.place(x=650, y=430)

# Birthdate
btnFechaTxt = f'''Seleccionar Fecha
de Nacimiento'''
popup_btn = ttk.Button(window, text=btnFechaTxt, command=popup)
popup_btn.place(x=500, y=460)
fecha_nac = ttk.Entry(window, state='readonly')
fecha_nac.place(x=650, y=460)

# Button create
create = tk.Button(window, text='Crear Usuario', command=saveUser, bg='green', fg='white')
create.place(x=500, y=100)

# Button edit
edit = tk.Button(window, text='Editar Usuario', command=editUser, bg='yellow')
edit.place(x=600, y=100)
edit["state"] = "disabled"

# Button delete
delete = tk.Button(window, text='Eliminar Usuario', command=deleteUser, bg='red')
delete.place(x=700, y=100)
delete["state"] = "disabled"

table.bind('<Double-Button-1>', doubleClickTable)

showData()

window.mainloop()