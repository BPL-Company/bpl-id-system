from pymongo import MongoClient
from .user_search import UserSearch


class UserMethods:
    def __init__(self, db: MongoClient):
        self.user_search = UserSearch(db)
        self.user_repo = self.user_search.users

    def update_nickname(self, user_id, nickname):
        user = self.user_search.get_user_by_id(user_id)
        self.user_repo.update_user(user, {'nickname': nickname})
        self.user_repo.update_user(user, {'nicknames': nickname}, '$addToSet')

    def add_auth(self, user_id, auth_method, auth_string):
        self.user_repo.update_user({"_id": user_id},
                                   {f'auth.{auth_method}': auth_string}, '$addToSet')

    def add_connection(self, user_id, connection):
        self.user_repo.update_user({"_id": user_id},
                                   {'connected_to': connection}, '$addToSet')

    def remove_auth(self, user_id, auth_method, auth_string):
        self.user_repo.update_user({"_id": user_id},
                                   {f'auth.{auth_method}': auth_string}, '$pop')

    def remove_connection(self, user_id, connection):
        self.user_repo.update_user({"_id": user_id},
                                   {'connected_to': connection}, '$pop')

    def remove_nickname(self, user_id, nickname):
        self.user_repo.update_user({"_id": user_id}, {'nicknames': nickname}, '$pop')
