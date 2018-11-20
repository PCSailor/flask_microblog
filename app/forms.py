'''
This is the login form
'''
from flask_wtf import FlaskForm # baseclass
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired # checks that the field is not submitted empty

class LoginForm(FlaskForm): # LoginForm class created
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')




