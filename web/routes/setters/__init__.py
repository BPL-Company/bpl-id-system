from web.server import *


@app.route('/create_user')
@require_token
def create_user():
    nickname = request.args['nickname']
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not nickname:
        return api.errors.missing_args()
    return api.create_user(nickname, auth_method, auth_string)


@app.route('/add_connection')
@require_token
def add_connection():
    user_id = request.args['user_id']
    connection = request.args['connection']
    if not connection or not user_id:
        return api.errors.missing_args()
    return api.add_connection(user_id, connection)


@app.route('/add_auth')
@require_token
def add_auth():
    user_id = request.args['user_id']
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not user_id:
        return api.errors.missing_args()
    return api.add_auth(user_id, auth_method, auth_string)


@app.route('/update_nickname')
@require_token
def update_nickname():
    nickname = request.args['nickname']
    user_id = request.args['user_id']
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.update_nickname(user_id, nickname)


@app.route('/remove_nickname')
@require_token
def remove_nickname():
    nickname = request.args['nickname']
    user_id = request.args['user_id']
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.remove_nickname(user_id, nickname)


@app.route('/set_money')
@require_token
def set_money():
    user_id = request.args['user_id']
    count = request.args['count']
    if not count or not user_id:
        return api.errors.missing_args()
    return api.set_money(user_id, count)


@app.route('/inc_money')
@require_token
def inc_money():
    user_id = request.args['user_id']
    count = request.args['count']
    if not count or not user_id:
        return api.errors.missing_args()
    return api.increase_money(user_id, count)


@app.route('/dec_money')
@require_token
def dec_money():
    user_id = request.args['user_id']
    count = request.args['count']
    if not count or not user_id:
        return api.errors.missing_args()
    return api.decrease_money(user_id, count)
