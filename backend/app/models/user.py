from app.extensions import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson.objectid import ObjectId

class User:
    def __init__(self, username, email, password, is_admin=False):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin

    def save(self):
        user_data = {
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'is_admin': self.is_admin
        }
        mongo.db.users.insert_one(user_data)

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({'email': email})

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})

    @staticmethod
    def find_by_id(user_id):
        return mongo.db.users.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def check_password(stored_password, provided_password):
        return check_password_hash(stored_password, provided_password)

    @staticmethod
    def update_password(email, new_password):
        hashed_password = generate_password_hash(new_password)
        mongo.db.users.update_one({'email': email}, {'$set': {'password': hashed_password}})
