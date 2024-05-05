from pymongo import MongoClient

class MongoDB:
    def __init__(self, host='localhost', port=27017, db_name='face-checkin'):
        self.host = host
        self.port = port
        self.db_name = db_name
        self.client = None
        self.db = None

    def connect(self):
        try:
            uri = f"mongodb://{self.host}:{self.port}/{self.db_name}"

            self.client = MongoClient(uri)
            self.db = self.client[self.db_name]
            # print("Conexión exitosa a MongoDB.")
            return self.db
        except Exception as e:
            print(f"Error al conectar a MongoDB: {str(e)}")

    def close_connection(self):
        if self.client:
            self.client.close()
            print("Conexión cerrada.")

# Create MongoDB instance
# mongo = MongoDB()
# mongo.connect()