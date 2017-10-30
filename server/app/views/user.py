from flask import Blueprint, g, jsonify, make_response, request, session
from flask_login import current_user, login_required, login_user, logout_user

from app.forms import RegisterForm, LoginForm
from app.models import User
from app.utils import create_user, login_check


bp = Blueprint('user', __name__, url_prefix='/user')


@bp.route('/register', methods=['POST'])
def register():
    form = RegisterForm(request.form)
    if not form.validate():
        return make_response(jsonify(), 400)

    try:
        user = create_user(form.username.data,
                           form.password.data,
                           form.nickname.data)
    except Exception as e:
        print(e)
        return make_response(jsonify(), 400)
    login_user(user)
    return make_response(jsonify(), 200)


@bp.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if not form.validate():
        return make_response(jsonify(), 400)
    user = login_check(form.username.data, form.password.data)

    if user is None or not login_user(user):
        return make_response(jsonify(), 400)

    return make_response(jsonify({
        'nickname': user.nickname
    }), 200)


@bp.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return make_response(jsonify(), 200)


@bp.route('/list', methods=['GET'])
@login_required
def user_list():
    return make_response(jsonify([{
        'username': u.username,
        'nickname': u.nickname
    } for u in User.query.filter(User.username != current_user.username)]), 200)