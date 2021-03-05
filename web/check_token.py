from functools import wraps
from config import auth_token


def require_token(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        from flask import request

        token = request.args.get('auth_token')

        if not token:
            return {'ok': False, 'reason': 'Token required.', 'errcode': -1}

        if token != auth_token:
            return {'ok': False, 'reason': 'Token invalid.', 'errcode': -2}

        return func(*args, **kwargs)
    return check_token
