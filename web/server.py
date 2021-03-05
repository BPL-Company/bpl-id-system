from flask import Flask, request
app = Flask('app')

from db.startup import *
from web.check_token import require_token
