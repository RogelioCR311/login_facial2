from tkinter import messagebox
from bson import ObjectId
from src.models.edit_user import editUserById

def editUser(nombre, apellido, fecha_nac, id_user):
  if len(nombre) != 0 and len(apellido) != 0 and len(fecha_nac) != 0:
    
    idSearch={"_id":ObjectId(id_user)}
    newValues = {
      "$set": {
        "name": nombre, 
        "lastname": apellido, 
        "birthdate": fecha_nac
      }
    }
  
    editUserById(idSearch, newValues)
    messagebox.showinfo(message='Usuario editado exitosamente')
  else:
    messagebox.showerror(message='Los campos no pueden estar vacios')