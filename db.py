from pymongo import MongoClient

uri = "mongodb+srv://weezys:boyqpc2k@cluster0-l3dhj.mongodb.net/test?retryWrites=true"
#1. connect
client = MongoClient(uri)
#2. get database
db = client.test
#3. get collection
food_collection = db["food"]
# #4. create a new document
new_food = {
    "name": "Pink",
    "price": 9999,
    }   #document
#5. insert new document into collection
food_collection.insert_one(new_food)
#6. close connection
def close():
    client.close()