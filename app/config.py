import os
from pathlib import Path

path = Path(__file__).parent.absolute()

SECRET_KEY = os.urandom(12)
SQLALCHEMY_TRACK_MODIFICATIONS = False

DB_USER = 'test_user'
DB_PASSWORD = 'test_password'
DB_NAME = 'adex_db'

SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}'
# SQLALCHEMY_DATABASE_URI = f'sqlite:///{path}/db/main.db'
DEBUG = False


MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_USERNAME = 'MAIL_USERNAME'
MAIL_PASSWORD = 'MAIL_PASSWORD'
