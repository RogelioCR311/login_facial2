from src.models.mongodb import MongoDB

mongo = MongoDB()

def getData():
  collection = mongo.connect()["users"].find()

  return collection

def getAsistData():
  collection = mongo.connect()["check-ins"].find()

  return collection