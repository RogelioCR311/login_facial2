import datetime
from src.models.edit_user import getUserById
from src.models.save_data import saveCheckIn as saveData

def saveCheckIn(id_user):

  document = getUserById(id_user)

  newData = {
    "name": document["name"], 
    "lastname": document["lastname"], 
    "time": datetime.datetime.now()
  }

  saveData(newData)
