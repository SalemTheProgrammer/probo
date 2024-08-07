from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_pymongo import PyMongo

bcrypt = Bcrypt()
jwt = JWTManager()
mail = Mail()
mongo = PyMongo()
