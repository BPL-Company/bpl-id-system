from flask import Flask, request
app = Flask(__name__)

from db.startup import *
