from flask import render_template

from .user import bp as userBP
from .room import bp as roomBP
from .chat import socketio


def set_blueprint(app):
    app.register_blueprint(userBP)
    app.register_blueprint(roomBP)
    socketio.init_app(app)