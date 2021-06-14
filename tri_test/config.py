import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


class ProdConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'do-not-use-this-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///tri_test.sqlite'


class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SECRET_KEY = 'do-not-use-this-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = 'do-not-use-this-in-production'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
