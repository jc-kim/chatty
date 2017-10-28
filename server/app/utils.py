from functools import wraps
from typing import List

from flask import g, abort
from flask_login import current_user
from flask_socketio import disconnect
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import User, Room

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


def authenticated_only(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not current_user.is_authenticated:
            disconnect()
        else:
            return f(*args, **kwargs)
    return wrapped


def make_room(*users: List[User]) -> Room:
    room = Room(users=list(users))
    try:
        db.session.add(room)
        db.session.commit()
    except exc.SQLAlchemyError:
        raise Exception('db error')  # TODO
    return room