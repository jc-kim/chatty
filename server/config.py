import datetime

DEBUG = True
HOST = '0.0.0.0'
PORT = 5000

SQLALCHEMY_DATABASE_URI = 'postgres://chatty:chattychatty@localhost/chatty'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'something_must_be_secret'

JWT_AUTH_URL_RULE = '/user/login'
JWT_EXPIRATION_DELTA = datetime.timedelta(hours=6)