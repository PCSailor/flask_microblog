'''
* #1 startup file
* from 'file' import 'class'
'''
from flask import Flask #1
from config import Config
from flask_migrate import Migrate #
from flask_sqlalchemy import SQLAlchemy #
from flask_login import LoginManager # 

app = Flask(__name__) #2 an instance of class Flask within the __init__.py script
app.config.from_object(Config) # reads & applies the config.py file
db = SQLAlchemy(app) #
migrate = Migrate(app, db) #
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors #3 'app' refers to folder # routes always-at-bottom due to 'circular imports'
