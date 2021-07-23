from flask_pymongo import MongoClient


class UserRepo:
    def __init__(self, db: MongoClient):
        self.db = db
        self.users = db.bpl.users
        self.email = db.bpl.email
        self.minecraft = db.bpl.minecraft
        self.phone = db.bpl.phone
        self.telegram = db.bpl.telegram
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
            try:
                self.minecraft.insert({'_id': user['_id'], 'minecraft': user['auth']['minecraft']})
            except:
                pass
            self.phone.insert({'_id': user['_id'], 'minecraft': user['auth']['phone']})
            self.telegram.insert({'_id': user['_id'], 'minecraft': user['auth']['telegram']})
            self.email.insert({'_id': user['_id'], 'minecraft': user['auth']['email']})

    def find_users(self, query=None):
        if query is None:
            query = {}
        return self.users.find(query)

    def find_user(self, query=None):
        if query is None:
            query = {}
        return self.users.find_one(query)

    def merge_users(self, first_id, second_id):
        first_user = self.find_user({'_id': first_id})
        second_user = self.find_user({'_id': second_id})

        for field in ['money']:
            first_user[field] += second_user[field]
        for field in self.base_auth_info:
            first_user['auth'][field] += second_user['auth'][field]
        self.update_user({'_id': first_id}, first_user)
        self.delete_user(second_id)

    def create_user(self, auth_method, auth_string, nickname: str):
        _id = list(self.users.find({}).sort('_id', -1).limit(1))
        _id = _id[0]['_id']+1 if _id else 0
        user = self.form_user_dict(auth_method, auth_string, nickname, _id)
        self.users.insert_one(user)

    def delete_user(self, user_id):
        self.users.delete_one({'_id': user_id})

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
            'auth': self.base_auth_info,
            'role': 'member',
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
