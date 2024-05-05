from src.models.mongodb import MongoDB
from bson import ObjectId
import pymongo

mongo = MongoDB()
collection = mongo.connect()["users"]

def getUserById(id_user):
  try:
    document = collection.find({"_id":ObjectId(id_user)})[0]
    return document
  except pymongo.errors.ConnectionFailure as error:
    print(error)

def editUserById(idSearch, newValues):
  collection.update_one(idSearch, newValues)