from app import mongo
from bson.objectid import ObjectId


class UserService:

    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        res = []
        for user in users:
            user["_id"] = str(user["_id"])  
            res.append(user)
        return res

    @staticmethod
    def get_user_by_id(id):
        user = mongo.db.users.find_one({"_id": ObjectId(id)})
        return user

    @staticmethod
    def create_user(data):
        return mongo.db.users.insert_one(data).inserted_id

    @staticmethod
    def update_user(id, data):
        return mongo.db.users.update_one({"_id": ObjectId(id)}, {"$set": data})

    @staticmethod
    def delete_user(id):
        return mongo.db.users.delete_one({"_id": ObjectId(id)})
