from tkinter import messagebox
from src.models.save_data import saveData

def saveUser(nombre, apellido, fecha_nac):
  if len(nombre) != 0 and len(apellido) != 0 and len(fecha_nac) != 0:
    document = {
      "name": nombre, 
      "lastname": apellido, 
      "birthdate": fecha_nac
    }
  
    saveData(document)
    messagebox.showinfo(message='Usuario guardado exitosamente')
  else:
    messagebox.showerror(message='Los campos no pueden estar vacios')