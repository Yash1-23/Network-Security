from pymongo import MongoClient

# Replace '<password>' with your actual MongoDB password
uri = "mongodb+srv://YahwanthSingh:<password>@cluster0.6jb2e.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinned your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
