'''
'''
from flask import render_template
from app import app
# a decorator modifies the function that follows it
@app.route('/') # decorator
@app.route('/index') # decorator
def index():
    user = {'username': 'Phil'}
    posts = [ # a list
        { # dictionary
            'author': {'username': 'Phil'},
            'body': 'Post #1 comng from routes.py'
        },
        { # another dictionary
            'author': {'username': 'Steph'},
            'body': 'Post #2 comng from routes.py'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
