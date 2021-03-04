from web.server import *


@app.route('/get_user_by_id/<user_id>')
def get_user_by_id(user_id):
    return api.get_user_by_id(user_id)


@app.route('/get_user_by_nickname/<nickname>')
def get_user_by_nickname(nickname):
    return api.get_user_by_nickname(nickname)
