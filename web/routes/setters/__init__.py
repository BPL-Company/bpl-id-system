from web.server import *
from bson import Decimal128


@app.route('/merge_users')
@require_token
def merge_users():
    return api.errors.missing_args()
    first_id = request.args['first_id']
    second_id = request.args['second_id']
    if not first_id or not second_id:
        return api.errors.missing_args()
    return api.merge_users(first_id, second_id)


@app.route('/create_tg_user')
@require_token
def create_tg_user():
    nickname = request.args['nickname']
    tg_id = request.args['tg_id']
    if not nickname or not tg_id:
        return api.errors.missing_args()
    return api.create_tg_user(nickname, tg_id)


@app.route('/create_minecraft_user')
@require_token
def create_minecraft_user():
    nickname = request.args['nickname']
    if not nickname:
        return api.errors.missing_args()
    return api.create_minecraft_user(nickname)


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
    user_id = int(request.args['user_id'])
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not user_id:
        return api.errors.missing_args()
    return api.add_auth(user_id, auth_method, auth_string)


@app.route('/delete_user')
@require_token
def delete_user():
    user_id = int(request.args['user_id'])
    if not user_id:
        return api.errors.missing_args()
    return api.delete_user(user_id)


@app.route('/remove_auth')
@require_token
def remove_auth():
    user_id = int(request.args['user_id'])
    auth_method = request.args['auth_method']
    auth_string = request.args['auth_string']
    if not auth_string or not auth_method or not user_id:
        return api.errors.missing_args()
    return api.remove_auth(user_id, auth_method, auth_string)


@app.route('/update_nickname')
@require_token
def update_nickname():
    nickname = request.args['nickname']
    user_id = int(request.args['user_id'])
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.update_nickname(user_id, nickname)


@app.route('/remove_nickname')
@require_token
def remove_nickname():
    nickname = request.args['nickname']
    user_id = int(request.args['user_id'])
    if not nickname or not user_id:
        return api.errors.missing_args()
    return api.remove_nickname(user_id, nickname)


@app.route('/set_money_tg')
@require_token
def set_money_tg():
    telegram = request.args.get('telegram')
    count = request.args.get('count')
    if not telegram or not count:
        return api.errors.missing_args()

    count = int(count)
    telegram = int(telegram)

    user = api.get_user_by_tg_id(telegram)['result']
    user_id = user['_id']

    return api.set_money(user_id, count)


@app.route('/inc_money_tg')
@require_token
def inc_money_tg():
    telegram = request.args.get('telegram')
    count = request.args.get('count')
    if not telegram or not count:
        return api.errors.missing_args()

    count = int(count)
    telegram = int(telegram)

    if count <= 0:
        return api.errors.invalid_money_count()

    user = api.get_user_by_tg_id(telegram)['result']
    user_id = user['_id']

    return api.inc_money(user_id, count)


@app.route('/dec_money_tg')
@require_token
def dec_money_tg():
    telegram = request.args.get('telegram')
    count = request.args.get('count')
    if not telegram or not count:
        return api.errors.missing_args()

    count = int(count)
    telegram = int(telegram)

    if count <= 0:
        return api.errors.invalid_money_count()

    user = api.get_user_by_tg_id(telegram)['result']
    user_id = user['_id']

    return api.dec_money(user_id, count)


@app.route('/set_money')
@require_token
def set_money():
    user_id = request.args.get('user_id')
    minecraft = request.args.get('minecraft')
    telegram = request.args.get('telegram')
    count = request.args.get('count')
    if not user_id and not minecraft and not telegram:
        return api.errors.missing_args()
    if not count:
        return api.errors.missing_args()

    count = int(count)

    if count <= 0:
        return api.errors.invalid_money_count()

    if not user_id:
        user = api.get_user_by_minecraft(minecraft)['result']
        user_id = user['_id']
    elif not minecraft:
        telegram = int(telegram)
        user = api.get_user_by_tg_id(telegram)['result']
        user_id = user['_id']

    return api.set_money(user_id, count)


@app.route('/inc_money')
@require_token
def inc_money():
    user_id = request.args.get('user_id')
    minecraft = request.args.get('minecraft')
    telegram = request.args.get('telegram')
    count = request.args.get('count')
    if not user_id and not minecraft and not telegram:
        return api.errors.missing_args()
    if not count:
        return api.errors.missing_args()

    count = int(count)

    if count <= 0:
        return api.errors.invalid_money_count()

    if not user_id:
        user = api.get_user_by_minecraft(minecraft)['result']
        user_id = user['_id']
    elif not minecraft:
        telegram = int(telegram)
        user = api.get_user_by_tg_id(telegram)['result']
        user_id = user['_id']

    return api.increase_money(user_id, count)


@app.route('/dec_money')
@require_token
def dec_money():
    user_id = request.args.get('user_id')
    minecraft = request.args.get('minecraft')
    telegram = request.args.get('telegram')
    count = request.args.get('count')
    if not user_id and not minecraft and not telegram:
        return api.errors.missing_args()
    if not count:
        return api.errors.missing_args()

    count = int(count)

    if count <= 0:
        return api.errors.invalid_money_count()

    if not user_id:
        user = api.get_user_by_minecraft(minecraft)['result']
        user_id = user['_id']
    elif not minecraft:
        telegram = int(telegram)
        user = api.get_user_by_tg_id(telegram)['result']
        user_id = user['_id']

    return api.decrease_money(user_id, count)
