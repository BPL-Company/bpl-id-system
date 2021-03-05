from web.server import *
from web.routes import *
from config import api_port

if __name__ == '__main__':
    app.run(port=api_port)
