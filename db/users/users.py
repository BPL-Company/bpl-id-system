from flask_pymongo import MongoClient


class UserRepo:
    def __init__(self, db: MongoClient):
        self.db = db
        self.users = db.bpl.users
        self.sync_data()

    def update_user(self, query, data, method="$set"):
        self.users.update_one(query, {method: data})

    def sync_data(self):
        users = self.find_users()
        for user in users:
            synced_user = self.base_user_info
            synced_user.update(user)
            # synced_user['nicknames'] = list(set(synced_user['nicknames']))
            self.update_user(user, synced_user)

    def find_users(self, query=None):
        if query is None:
            query = {}
        return self.users.find(query)

    def find_user(self, query=None):
        if query is None:
            query = {}
        return self.users.find_one(query)

    def create_user(self, auth_method, auth_string, nickname: str):
        _id = list(self.users.find({}).sort('_id', -1).limit(1))
        print(_id)
        _id = _id[0]['_id']+1 if _id else 0
        print(_id)
        user = self.form_user_dict(auth_method, auth_string, nickname, _id)
        self.users.insert_one(user)

    def insert_user_document(self, user):
        self.users.insert_one(user)

    def form_user_from_document(self, user):
        base_doc = self.base_user_info
        base_doc.update(user)
        return base_doc

    def form_user_dict(self, auth_method, auth, nickname: str, _id=0):
        user = self.base_user_info
        user['nickname'] = nickname
        user['auth'][f'{auth_method}'].append(auth)
        user['_id'] = _id
        return user

    @property
    def base_user_info(self):
        return {
            '_id': 0,
            'nickname': 'None',
            'nicknames': [],
            'auth': self.base_auth_info,
            'role': 'member',
            'connected_to': [],
            'money': 0
        }

    @property
    def base_auth_info(self):
        return {
            'telegram_id': [],
            'email': [],
            'phone_number': [],
            'minecraft': []
        }
