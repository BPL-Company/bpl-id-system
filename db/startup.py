from pymongo import MongoClient
from db.users import Users
from config import db_url

users = Users(MongoClient(db_url))

from api.methods import ApiMethods
api = ApiMethods(users)
