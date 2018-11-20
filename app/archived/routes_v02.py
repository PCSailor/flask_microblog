'''
'''
from flask import render_template
from app import app
# a decorator modifies the function that follows it
@app.route('/') # decorator
@app.route('/index') # decorator
def index():
    user = {'username': 'Phil'}
    return render_template('index.html', title='Home', user=user)
