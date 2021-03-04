from web.server import *


@app.route('/create_user')
def create_user():
    nickname = request.args['nickname']
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not nickname:
        return api.errors.missing_args()
    return api.create_user(nickname, auth_method, auth_string)


@app.route('/add_connection')
def add_connection():
    user_id = request.args['user_id']
    connection = request.args['connection']
    if not connection or not user_id:
        return api.errors.missing_args()
    return api.add_connection(user_id, connection)


@app.route('/add_auth')
def add_auth():
    user_id = request.args['user_id']
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not user_id:
        return api.errors.missing_args()
    return api.add_auth(user_id, auth_method, auth_string)


@app.route('/update_nickname')
def update_nickname():
    nickname = request.args['user_id']
    user_id = request.args['nickname']
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.update_nickname(user_id, nickname)


@app.route('/remove_nickname')
def remove_nickname():
    nickname = request.args['user_id']
    user_id = request.args['nickname']
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.remove_nickname(user_id, nickname)

