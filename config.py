import sys
import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))+os.path.sep


class Config(object):
    SECRET_KEY = "default_secret_key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 12


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@localhost/pydiary'
    DEBUG = True
    WTF_CSRF_ENABLED = True


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + PROJECT_DIR + "test.db"
    DEBUG = False
    TESTING = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', DevelopmentConfig.SQLALCHEMY_DATABASE_URI)
    DEBUG = False

