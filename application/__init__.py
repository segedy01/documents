'''
__init__.py
~~~~~~~~~~~

Entry point for the application package
'''
#: third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import configurations
import os


#: db instantiation
config = configurations.DevelopmentConfig

#: initialize Flask
app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static/Documents')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#: load config from passed in config file to the app config dictionary
app.config.from_object(config)

db = SQLAlchemy(app)

from application.models.model import *
migrate = Migrate(app, db)

from application.views import *
