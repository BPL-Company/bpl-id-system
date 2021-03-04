from os import environ
try:
    from tokens import db_url
except ImportError:
    db_url = environ['database']