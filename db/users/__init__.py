from .users import UserRepo
from .user_search import UserSearch
from .user_methods import UserMethods
from flask_pymongo import MongoClient


class Users:
    def __init__(self, db: MongoClient):
        self.user_repo = UserRepo(db)
        self.user_search = UserSearch(db)
        self.user_methods = UserMethods(db)
