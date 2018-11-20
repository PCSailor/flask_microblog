'''
* db.Model is a base class of SQLAlchemy
* __repr__ tells how to print objects of this class
'''
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # had a comma at end of this line, caused me an hour of wasted time!
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)
