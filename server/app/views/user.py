from flask import Blueprint, g, jsonify, make_response, request, session
from flask_jwt import jwt_required, current_identity

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
        return make_response(jsonify({
            'error': str(e),
        }), 400)
    return make_response(jsonify(), 200)


@bp.route('/my')
@jwt_required()
def my_info():
    return make_response(jsonify({
        'username': current_identity.username,
        'nickname': current_identity.nickname
    }))


@bp.route('/list', methods=['GET'])
@jwt_required()
def user_list():
    return make_response(jsonify([{
        'username': u.username,
        'nickname': u.nickname
    } for u in User.query.filter(User.username != current_identity.username)]),
    200)