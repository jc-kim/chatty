import datetime
from functools import wraps
from typing import List

from flask import g, abort
from flask_jwt import current_identity
from flask_socketio import disconnect
from sqlalchemy import exc
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .models import ChatLog, Room, User


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
        if not current_identity:
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
        db.session.rollback()
        raise Exception('db error')  # TODO
    return room


def add_chat(user: User, room_id: int, message: str):
    if user is None:
        raise Exception('invalid input')  # TODO
    try:
        room: Room = Room.query.get(room_id)
    except exc.SQLAlchemyError:
        raise Exception('invalid input')
    
    if room not in user.rooms:
        raise Exception('invalid input')
    
    if len(message) <= 0:
        raise Exception('invalid input')
    
    new_log = ChatLog(writer=user, message=message,
                      created_at=datetime.datetime.utcnow())
    room.logs.append(new_log)
    room.last_log_at = new_log.created_at
    try:
        db.session.commit()
    except exc.SQLAlchemyError:
        db.session.rollback()
        raise Exception('db error')

    return new_log


def _jwt_authenticate(username, password):
    user = User.query.filter_by(username=username).scalar()
    if user and check_password_hash(user.password, password):
        return user


def _jwt_identity(payload):
    user_id = payload['identity']
    try:
        return User.query.get(user_id)
    except:
        return None


def initialize_jwt(jwt, app):
    jwt.authentication_handler(_jwt_authenticate)
    jwt.identity_handler(_jwt_identity)
    jwt.init_app(app)