from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["recommendation_db"]

users = db["users"]
history = db["history"]
rules = db["rules"]
rules_collection = db["rules"]

users = [

    {
        "email": "admin@gmail.com",
        "password": "admin123",
        "role": "admin"
    },

    {
        "email": "user@gmail.com",
        "password": "user123",
        "role": "user"
    }

]