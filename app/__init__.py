'''
* #1 startup file
* from 'file' import 'class'

Error = "cannot import name 'db' from 'app'"
you are importing main BEFORE you are creating the instance of db in your __init__.py

If move the import to after your db = SQLAlchemy(app), it will work

db = SQLAlchemy(app)

from bookshelf.main.controllers import main #<--move this here

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
