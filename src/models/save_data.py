from src.models.mongodb import MongoDB

mongo = MongoDB()

def saveData(document):
  collection = mongo.connect()["users"]

  collection.insert_one(document)

def saveCheckIn(document):
  collection = mongo.connect()["check-ins"]

  collection.insert_one(document)
