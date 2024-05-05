from src.models.mongodb import MongoDB

def saveData(document):
  mongo = MongoDB()
  collection = mongo.connect()["users"]

  collection.insert_one(document)
