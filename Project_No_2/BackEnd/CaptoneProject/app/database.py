#writ the code for connect to the database
# This file creates a single shared connection to mongoDB using pymongo

from pymongo import MongoClient
from pymongo.database import Database

from app.config import settings

# MongoCLient manages a pool of connections to the mongoDB server.
client : MongoClient = MongoClient(settings.MONGO_URI)
database:Database = client[settings.MONGO_DB_NAME]

# Sends a ping command to mongoDB to confirm  the connection is alive.
def ping_database() -> bool:
    try:
        client.admin.command("ping")
        return True
        
    except Exception:
        return False