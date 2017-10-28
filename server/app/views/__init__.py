from .user import bp as userBP
from .room import bp as roomBP

def set_blueprint(app):
    app.register_blueprint(userBP)
    app.register_blueprint(roomBP)