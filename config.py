import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'This is the SECRET_KEY 2nd term hard-coded string option'
