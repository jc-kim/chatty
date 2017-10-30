from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_pyfile('../config.py')
    if config is not None:
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    from app.models import User
    from app.views import set_blueprint

    set_blueprint(app)

    login_manager.user_loader(lambda username: User.query.filter_by(username=username).first())

    return app