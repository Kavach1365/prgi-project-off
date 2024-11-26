
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://chandu:Pa55word@cluster0.zndqewl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.pgriTestData
titlesCollection = db['testTitles1']


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("You successfully connected to MongoDB!")
except Exception as e:
    print(e)