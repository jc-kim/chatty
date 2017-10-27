from functools import wraps

from flask import g, abort
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User


def login_required(f):
    @wraps(f)
    def func(*args, **kwargs):
        if getattr(g, 'user', None) is None:
            return abort(403)
        return f(*args, **kwargs)
    return func


def create_user(username, password, nickname):
    user = User(username=username,
                password=generate_password_hash(password),
                nickname=nickname)
    try:
        db.session.add(user)
        db.session.commit()
        return user
    except exc.SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        raise Exception('db error') # TODO


def login_check(username, password) -> User:
    user = User.query.filter_by(username=username).first()
    if user is None:
        return None
    if not check_password_hash(user.password, password):
        return None
    return user