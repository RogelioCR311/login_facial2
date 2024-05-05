from src.models.mongodb import MongoDB

def getData():
  mongo = MongoDB()
  collection = mongo.connect()["users"].find()

  return collection