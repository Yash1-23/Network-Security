
from pymongo_client import MongoClient

uri = "mongodb+srv://YahwanthSingh:<@password>@cluster0.6jb2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

#Create a new clinet and connect to the server
clinet = MongoClient(uri)

#Send a ping to confirm a successful connection

try:
    client.admin.command('ping')
    print("Pinned your deployment. You succesfully connected to MongoDB!")
except Exception as e:
    print(e)