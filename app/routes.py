'''
'''
from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm # import the Login class from forms.py, instantiated an object from it, & sent it to the template
# Decorators modifiy the function that follows it
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

@app.route('/login', methods=['GET', 'POST']) # decorator # BUG: if kept above login screen fails
def login():
    form = LoginForm()
    if form.validate_on_submit(): # method doing all from processing
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('index')) # return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)