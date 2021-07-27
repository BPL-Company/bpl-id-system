from pymongo import MongoClient
from .user_search import UserSearch


class UserMethods:
    def __init__(self, db: MongoClient):
        self.user_search = UserSearch(db)
        self.user_repo = self.user_search.users

    def delete_user(self, user_id):
        self.user_repo.delete_user(user_id)

    def update_nickname(self, user_id, nickname):
        self.user_repo.update_user({'_id': user_id}, {'nickname': nickname})

    def add_auth(self, user_id, auth_method, auth_string):
        self.user_repo.bpl[auth_method].update_one({"_id": user_id}, {auth_method: auth_string}, '$addToSet')

    def remove_auth(self, user_id, auth_method, auth_string):
        self.user_repo.bpl[auth_method].update_one({"_id": user_id}, {auth_method: auth_string}, '$pull')

    def set_money(self, user_id, count):
        self.user_repo.update_user({"_id": user_id}, {'money': count}, '$set')

    def increase_money(self, user_id, count):
        self.user_repo.update_user({"_id": user_id}, {'money': count}, '$inc')

    def decrease_money(self, user_id, count):
        self.user_repo.update_user({"_id": user_id}, {'money': -count}, '$inc')

