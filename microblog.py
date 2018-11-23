'''
#3 startup file
define & import the Flask application instance-pg7
'''
from app import app#, db #1 
# from app.models import User, Post

'''
# not working shell context menu:
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
'''