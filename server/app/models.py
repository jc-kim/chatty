import datetime
from functools import partial

from . import db


Column = partial(db.Column, nullable=False)

users_rooms = db.Table('users_rooms',
    Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    Column('room_id', db.Integer, db.ForeignKey('room.id'), primary_key=True),
    Column('unread_count', db.Integer, default=0),
)


class User(db.Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(db.Unicode(255), unique=True)
    password = Column(db.Unicode(255))
    nickname = Column(db.Unicode(255), unique=True)
    rooms = db.relationship('Room', secondary=users_rooms, lazy='subquery',
                            backref=db.backref('users', lazy=True))


class Room(db.Model):
    id = Column(db.Integer, primary_key=True)
    last_log_at = Column(db.DateTime, default=datetime.datetime.utcnow,
                         index=True)
    logs = db.relationship('ChatLog', backref='room', lazy=True)


class ChatLog(db.Model):
    id = Column(db.Integer, primary_key=True)
    room_id = Column(db.Integer, db.ForeignKey('room.id'))
    writer_id = Column(db.Integer, db.ForeignKey('user.id'))
    message = Column(db.UnicodeText)
    created_at = Column(db.DateTime, default=datetime.datetime.utcnow)