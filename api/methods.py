from db.users import Users
from api.checks import UserChecks
from api.errors import Errors


class ApiMethods:
    def __init__(self, db: Users):
        self.user_repo = db.user_repo
        self.user_method = db.user_methods
        self.user_search = db.user_search

        self.user_checks = UserChecks(db)

        self.errors = Errors()

    def create_user(self, nickname, auth_method, auth_string):
        if self.user_checks.is_nickname_exist(nickname):
            return self.errors.nickname_used()
        if self.user_checks.is_auth_exist(auth_method, auth_string):
            return self.errors.auth_used()

        self.create_user(nickname=nickname, auth_method=auth_method, auth_string=auth_string)
        new_user = self.user_search.get_user_by_nickname(nickname)
        return {'ok': True, 'result': new_user}

    def get_user_by_id(self, user_id):
        user = self.user_search.get_user_by_id(user_id)
        if not user:
            return self.errors.user_not_found()
        return {'ok': True, 'result': user}

    def get_user_by_nickname(self, nickname):
        user = self.user_search.get_user_by_nickname(nickname)
        if not user:
            return self.errors.user_not_found()
        return {'ok': True, 'result': user}

    def add_auth(self, user_id, auth_method, auth_string):
        if not self.user_checks.is_id_exist(user_id):
            return self.errors.user_not_found()
        if self.user_checks.is_auth_exist(auth_method, auth_string):
            return self.errors.auth_used()

        self.user_method.add_auth(user_id, auth_method, auth_string)
        return {'ok': True}

    def update_nickname(self, user_id, nickname):
        user = self.user_search.get_user_by_id(user_id)
        if not user:
            return self.errors.user_not_found()
        if self.user_checks.is_nickname_exist(nickname):
            return self.errors.nickname_used()
        self.user_method.update_nickname(user, nickname)
        return {'ok': True}

    def add_connection(self, user_id, connection):
        if not self.user_checks.is_id_exist(user_id):
            return self.errors.user_not_found()
        self.user_method.add_connection(user_id, connection)
        return {'ok': True}

    def remove_auth(self, user_id, auth_method, auth_string):
        if not self.user_checks.is_id_exist(user_id):
            return self.errors.user_not_found()
        if not self.user_checks.is_auth_exist(auth_method, auth_string):
            return self.errors.no_auth_found()
        self.user_method.remove_auth(user_id, auth_method, auth_string)
        return {'ok': True}

    def remove_nickname(self, user_id, nickname):
        if not self.user_checks.is_id_exist(user_id):
            return self.errors.user_not_found()
        if not self.user_checks.is_nickname_exist(nickname):
            return self.errors.no_nickname_found()
        self.user_method.remove_nickname(user_id, nickname)
        return {'ok': True}

    def get_users_count(self):
        result = self.user_search.get_users_count()
        return {'ok': True, 'result': result}
