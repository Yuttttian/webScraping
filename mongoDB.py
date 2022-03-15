# Requires pymongo 3.6.0+
from bson.int64 import Int64
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.vokwf.mongodb.net/test")
database = client["samples_pokemon"]
collection = database["samples_pokemon"]

# querying and printing to screen all Pokémon character names with candy_count >= month + day of your birthday.
query = {}
query["candy_count"] = {
    u"$gte": Int64(26)
}

projection = {}
projection["name"] = u"$name"
projection["_id"] = 0

cursor = collection.find(query, projection = projection)
for doc in cursor:
    print(doc)

# querying and printing to screen all Pokémon character names with num = month or num = day of your birthday.
query2 = {}
query2["candy_count"] = {
    u"$in": [
        Int64(11),
        Int64(15)
    ]
}

cursor = collection.find(query2, projection = projection)
for doc in cursor:
        print(doc)

client.close()
