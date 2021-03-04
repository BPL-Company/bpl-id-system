from db.users import Users


class UserChecks:
    def __init__(self, db: Users):
        self.user_repo = db.user_repo
        self.user_method = db.user_methods
        self.user_search = db.user_search

    def is_id_exist(self, user_id):
        return bool(self.user_search.get_user_by_id(user_id))

    def is_nickname_exist(self, nickname):
        return bool(self.user_search.get_user_by_nickname(nickname))

    def is_auth_exist(self, auth_method, auth_string):
        return bool(self.user_search.get_users_by_auth(auth_method, auth_string))
