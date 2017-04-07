#: --*-- coding: utf8 --*--
"""
configuration.py
~~~~~~~~~~~~~~~~

Holds the configuration for the various areas of the application
"""
import os

class Config(object):
    """
    Config class holds application defaults to be used in various environment
    """
    #: main config
    SECRET_KEY = 'cRypt0!N$yb0l$'
    SQLALCHEMY_DATABASE_URI = 'postgres://beast:beast@localhost:5432/DOCSYSTEM'
    SECURITY_PASSWORD_SALT = 'cRypt0!N$yb0l$|^^33+D0>+Or$'
    WTF_CSRF_ENABLED = True

     # mail settings
    # MAIL_SERVER = 'smtp.gmail.com'
    # MAIL_PORT = 465
    # MAIL_USE_TLS = False
    # MAIL_USE_SSL = True
    #
    # # gmail authentication
    # MAIL_USERNAME = 'beast@gmail.com'
    # MAIL_PASSWORD = 'BeastMail'
    #
    # # mail accounts
    # MAIL_DEFAULT_SENDER = 'beast@gmail.com'

class ProductionConfig(Config):
    """
    Config class holds application defaults to be used in production environment
    """
    DEBUG = False



class DevelopmentConfig(Config):
    """
    DevelopmentConfig class holds application defaults to be used in development environment
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True



class TestingConfig(Config):
    """
    TestingConfig class holds application defaults to be used in testing environment
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
