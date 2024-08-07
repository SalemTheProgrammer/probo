
from app.models.user import User
from app.extensions import mongo
from bson.objectid import ObjectId

def get_user_by_email(email):
    return User.find_by_email(email)

def get_user_by_username(username):
    return User.find_by_username(username)

def get_user_by_id(user_id):
    return User.find_by_id(user_id)

def create_user(username, email, password):
    user = User(username=username, email=email, password=password)
    user.save()
    return user

def update_user_password(email, new_password):
    User.update_password(email, new_password)
