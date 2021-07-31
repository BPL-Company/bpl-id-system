from flask_pymongo import MongoClient
from .users import UserRepo


class UserSearch:
    def __init__(self, db: MongoClient):
        self.users = UserRepo(db)
        self.db = self.users.bpl

    def get_users_by_auth_method(self, auth_method: str):
        return self.db[auth_method].find_users()

    def get_user_by_auth(self, auth_method: str, auth_string: str):
        return self.db[auth_method].find_one({auth_method: auth_string})

    def get_user_by_nickname(self, nickname: str):
        return self.users.find_user({'nickname': nickname})

    def get_user_by_minecraft(self, minecraft):
        user = self.get_user_by_auth('minecraft', minecraft)
        if not user:
            self.users.create_user('minecraft', minecraft, minecraft)
        user = self.get_user_by_auth('minecraft', minecraft)
        user.update(self.get_user_by_id(user['_id']))
        return user

    def get_user_by_tg_id(self, tg_id):
        user = self.get_user_by_auth('telegram', tg_id)
        if not user:
            self.users.create_user('telegram', tg_id, f'TG-{tg_id}')
        user = self.get_user_by_auth('telegram', tg_id)
        user.update(self.get_user_by_id(user['_id']))
        return user

    def get_user_by_id(self, user_id):
        return self.users.find_user({'_id': user_id})

    def get_user_by_query(self, query):
        return self.users.find_user(query)

    def get_users_by_query(self, query):
        return self.users.find_user(query)

    def get_users_count(self):
        return len(self.users.find_users())
