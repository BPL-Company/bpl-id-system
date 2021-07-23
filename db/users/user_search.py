from flask_pymongo import MongoClient
from .users import UserRepo


class UserSearch:
    def __init__(self, db: MongoClient):
        self.users = UserRepo(db)

    def get_users_by_auth_method(self, auth_method: str):
        users = self.users.find_users()
        result = [user for user in users if user['auth'][f'{auth_method}']]
        return result

    def get_users_by_auth(self, auth_method: str, auth_string: str):
        users = self.users.find_users()
        result = [user for user in users if auth_string in user['auth'][f'{auth_method}']]
        return result

    def get_user_by_nickname(self, nickname: str):
        user = self.users.find_user({'nickname': nickname})
        if user:
            return user
        return None

    def get_user_by_minecraft(self, minecraft):
        users = self.users.find_users()
        result = [user for user in users if minecraft in user['auth']['minecraft']]
        if result:
            return result[0]
        return None

    def get_user_by_tg_id(self, tg_id):
        users = self.users.find_users()
        result = [user for user in users if tg_id in user['auth']['telegram_id']]
        if result:
            return result[0]
        return None
        # result = self.users.find_user({'auth.tele': user_id})
        # return result

    def get_user_by_id(self, user_id):
        result = self.users.find_user({'_id': user_id})
        return result

    def get_user_by_query(self, query):
        result = self.users.find_user(query)
        return result

    def get_users_by_query(self, query):
        result = self.users.find_user(query)
        return result

    def get_users_count(self):
        return len(self.users.find_users())
