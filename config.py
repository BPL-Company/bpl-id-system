from os import environ
try:
    from tokens import db_url, auth_token
except ImportError:
    db_url = environ['database']
    auth_token = environ['auth_token']

api_port = environ.get('PORT') or 5000
