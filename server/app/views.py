from flask import Blueprint, g, jsonify, make_response, request, session

from .models import User
from .utils import create_user, login_check


bp = Blueprint('user', __name__)


def set_blueprint(app):
    app.register_blueprint(bp)


@bp.before_request
def logged_check():
    setattr(g, 'user', None)
    user_id: int = session.get('user_id', 0)
    if user_id > 0:
        setattr(g, 'user', User.query.get(user_id))


@bp.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')
    nickname = request.form.get('nickname')

    try:
        user = create_user(username, password, nickname)
    except Exception as e:
        print(e)
        return make_response(jsonify(), 400)
    session['user_id'] = user.id
    return make_response(jsonify(), 200)


@bp.route('/login', methods=['POST'])
def login():
    user = login_check(request.form.get('username'), 
                          request.form.get('password'))
    if user is None:
        return make_response(jsonify(), 400)
    session['user_id'] = user.id
    return make_response(jsonify({
        'nickname': user.nickname
    }), 200)


@bp.route('/logout', methods=['POST'])
def logout():
    user_id = session.pop('user_id', None)
    return make_response(jsonify(), 200 if user_id is not None else 400)