'''
* #1 startup file
* from 'file' import 'class'
'''
from flask import Flask #1
from config import Config
from flask_sqlalchemy import SQLAlchemy #
from flask_migrate import Migrate #


app = Flask(__name__) #2 an instance of class Flask within the __init__.py script
app.config.from_object(Config) # reads & applies the config.py file
db = SQLAlchemy(app) #
migrate = Migrate(app, db) #

from app import routes, models #3 'app' refers to folder # routes always-at-bottom due to 'circular imports'
