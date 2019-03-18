from db import food_collection
from bson import ObjectId
# def add(a,b):
    
#     new_food={
#         "name": a,
#         "price": int(b)
#     }
    
    
#     food_collection.insert_one(new_food)

def get(query):
    food_list = food_collection.find(query)
        # {
        #     "price": {"$gte": 9000 }
        # }
    
    return food_list
def get_by_id(id):
    f = food_collection.find_one({ "_id": ObjectId(id) })
    return f
def delete_by_id(id):
    a = food_collection.delete_one({ "_id": ObjectId(id) })
    return a   
def update_by_id(id, name, price):
    query = {"_id": ObjectId(id)}
    updater = {
        "$set": {"price": price},
        "$set": {"name": name}
        }
    food_collection.find_one_and_update(query, updater)
#update_by_id("5c812523ddb02c151c8ea3b3",)
#def find_by_username(username)
if __name__ == "__main__":
    query = {"_id": ObjectId("5c812523ddb02c151c8ea3b3")}
    updater = {"$set": {"price": 10000}} #$inc(tăng), $dec(giảm), $set(change), $usnet(break)
    food_collection.find_one_and_update(query, updater)    
    print(*get({}), sep="\n")
    # while True:
    #     a = input("Name: ")
    #     b = input("Price: ")
    #     new_food={}
    #     new_food["name"] = a
    #     new_food["price"] = b
        
    #     c=input("stop?(y/n)")
    #     if c=="n":
    #         break
    #food_list = get()
    # food_collection.delete_one({"_id": ObjectId("5c8131c4ddb02c1cb87004d9") })
    
    f = get_by_id("5c8131c4ddb02c1cb87004d9")
    for food in get({ "_id": ObjectId("5c8131c4ddb02c1cb87004d9") }):
        print(food)
    if f != None:
        print(f["name"])
    else:
        print("Not found")  

        
   
            
