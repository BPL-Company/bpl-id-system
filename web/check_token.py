from functools import wraps
from config import auth_token
from api.errors import Errors
errors = Errors()


def require_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        from flask import request

        token = request.args.get('auth_token')

        if not token:
            return errors.missing_token()

        if token != auth_token:
            return errors.invalid_token()

        return func(*args, **kwargs)
    return check_token
