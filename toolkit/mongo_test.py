from pymongo import MongoClient
from pprint import pprint

client = MongoClient()
db = client.crandom

cursor = db.joke.aggregate(
        [ {"$sample": {"size": 3}}]
)

# cursor = db.joke.find()

for document in cursor:
    print(document)
