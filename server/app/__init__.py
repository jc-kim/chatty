from flask import Flask
from flask_cors import CORS
from flask_jwt import JWT
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
jwt = JWT()


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)

    from app.models import User
    from app.views import set_blueprint
    from app.utils import initialize_jwt

    set_blueprint(app)

    initialize_jwt(jwt, app)

    return app