from bson.objectid import ObjectId
from src.models.mongodb import MongoDB
from tkinter import messagebox
import pymongo

def deleteData(id_user):
  mongo = MongoDB()
  collection = mongo.connect()["users"]
  try:
    idSearch={"_id":ObjectId(id_user)}
    collection.delete_one(idSearch)
    messagebox.showinfo(message='Usuario eliminado exitosamente')
  except pymongo.errors.ConnectionFailure as error:
    print(error)