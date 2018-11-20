'''
* import template:
    * from file import Class
'''
from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

from app import routes # kept at bottom due to flask bug
