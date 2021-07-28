class Errors:
    def form_error(self, reason, errcode):
        return {'ok': False, 'reason': reason, 'errcode': errcode}

    def invalid_token(self):
        return self.form_error('Invalid token.', -2)

    def missing_token(self):
        return self.form_error('Missing token.', -1)

    def missing_args(self):
        return self.form_error('Missing some args. Recheck your request.', 0)

    def nickname_used(self):
        return self.form_error('User with this nickname already exist.', 1)

    def auth_used(self):
        return self.form_error('User with that auth already exist.', 2)

    def user_not_found(self):
        return self.form_error('User not found.', 3)

    def no_auth_found(self):
        return self.form_error('This auth not exist.', 4)

    def no_nickname_found(self):
        return self.form_error('This nickname never used.', 5)

    def invalid_money_count(self):
        return self.form_error('Money count invalid.', 6)

