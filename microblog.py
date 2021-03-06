'''
#3 startup file
define & import the Flask application instance-pg7
'''
from app import app, db
from app.models import User, Post

# shell context
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}