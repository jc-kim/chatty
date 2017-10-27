from flask import Flask
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
socketio = SocketIO()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    socketio.init_app(app)

    from app import models
    from app.views import set_blueprint

    set_blueprint(app)

    return app