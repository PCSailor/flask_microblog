'''
pg26
This is the login form
'''
from flask_wtf import FlaskForm # baseclass
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo # DataRequired=checks field not submitted empty
from app.models import User

class LoginForm(FlaskForm): # LoginForm class created
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()]) # 'Email()' is a WTForms-stock-validator ensuring what user types matches an email address structure
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')] # EqualTo is a WTForms-stock-validator ensuring its value is identical to the argument
    )
    submit = SubmitField('Register')
    '''
    2 methods, validate_username() and validate_email(), that match the pattern validate_<field_name> which WTForms takes as custom validators and invokes in addition to stock validators. These ensure the username and email address entered are not in the database. These two methods issue database queries expecting no results. If a result exists, a raised ValidationError is triggered.
    '''
    def validate_username(self, username): # method
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different user name')
    
    def validate_email(self, email): # method
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address')



