'''
* #1 startup file
* from 'file' import 'class'
'''
import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask #1
from config import Config
from flask_migrate import Migrate #
from flask_sqlalchemy import SQLAlchemy #
from flask_login import LoginManager # 
# from flask_mail import Mail


app = Flask(__name__) #2 an instance of class Flask within the __init__.py script
app.config.from_object(Config) # reads & applies the config.py file
db = SQLAlchemy(app) #
migrate = Migrate(app, db) #
login = LoginManager(app)
login.login_view = 'login'
# mail = Mail(app)

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']) # error here=forgot two ()
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='website failure',
            credentials=auth, secure=secure
        )
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    # Logging to a file
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')





from app import routes, models, errors #3 'app' refers to folder # routes always-at-bottom due to 'circular imports'
