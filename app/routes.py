'''
* #2 startup file

'''
from flask import render_template, flash, redirect, url_for, request #
from flask_login import current_user, login_user, logout_user, login_required
from app import app #1
from app import db
from app.forms import LoginForm, RegistrationForm # import the Login class from forms.py, instantiated an object from it, & sent it to the template
from app.models import User
from werkzeug.urls import url_parse

# Decorators modifiy the function that follows it
@app.route('/') #2 # decorator
@app.route('/index') #3 # decorator
@login_required

def index(): #4
    # return "routes.py is hea!!" #5
    # user = {'username': 'Phil'}
    posts = [ # a list
        { # dictionary
            'author': {'username': 'Phil'},
            'body': 'Post #1 comng from routes.py'
        },
        { # another dictionary
            'author': {'username': 'Steph'},
            'body': 'Post #2 comng from routes.py.'
        }
    ]
    return render_template('index.html', title='Home', posts=posts)

@app.route('/login', methods=['GET', 'POST']) # decorator # BUG: if kept above login screen fails
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): # method doing all from processing
        user = User.query.filter_by(username=form.username.data).first() # query db for entered user name
        if user is None or not user.check_password(form.password.data):
            flash('Invalid user name or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page) # return redirect('/index')
        # return redirect(url_for('index')) # return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)