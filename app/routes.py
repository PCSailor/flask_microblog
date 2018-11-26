'''
* #2 startup file

'''
from flask import render_template, flash, redirect, url_for, request #
from flask_login import current_user, login_user, logout_user, login_required
from app import app #1
from app import db
from app.forms import LoginForm, RegistrationForm, EditProfileForm # import the Login class from forms.py, instantiated an object from it, & sent it to the template
from app.models import User
from werkzeug.urls import url_parse
from datetime import datetime

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

# Log in
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

# Log Out
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    '''
    Logic done inside 'if validate_on_submit()' conditional creates new user with username-email-password, writes it to database, & redirects to login prompt so user can log in
    '''
    if current_user.is_authenticated:
        return redirect(url_for('index')) # ensure the user is not logged in
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

# Create User Profile
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Post from routes.py/user() function #1'},
        {'author': user, 'body': 'Post from routes.py/user() function #2'}
    ]
    return render_template('user.html', user=user, posts=posts)

# Last Visit Time
@app.before_request # flask register decorator implementation checks if the current_user is logged in, & if so sets the last_seen field to the current time
def before_request(): # view function
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# Edit Profile
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Yours changes have been saved.')
        return redirect(url_for('edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Edit Profile', form=form)

    form = EditProfileForm(current_user.username) # Fix duplicate username bug
