from web.server import *


@app.route('/get_auth_token')
def get_auth_token():
    return {'result': 'KOZA.'}


@app.route('/get_users_count')
def get_users_count():
    return api.get_users_count()


@app.route('/get_user_by_id/<user_id>')
def get_user_by_id(user_id):
    return api.get_user_by_id(int(user_id))


@app.route('/get_user_by_nickname/<nickname>')
def get_user_by_nickname(nickname):
    return api.get_user_by_nickname(nickname)


@app.route('/get_user_by_minecraft/<nickname>')
def get_user_by_minecraft(nickname):
    return api.get_user_by_minecraft(nickname)


@app.route('/get_user_by_tg_id/<tg_id>')
def get_user_by_tg_id(tg_id):
    return api.get_user_by_tg_id(tg_id)
