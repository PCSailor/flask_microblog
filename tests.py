'''
pg 117
Unit Testing the User Model
'''
from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown():
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='phil') # todo: change username??
        u.set_password('cat') # todo: change password
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
    
    def test_avatar(self):
        u = User(username='phil', email='philcurtis.io') # Todo: need to change this??
        self.assertEqual(u.avatar(128), (
            'https://www.gravatar.com/avatar/'
            'd4c74594d841139328695756648b6bd6'
            '?d=identicon&s=128')
            ) # Todo: need to change this??

    def test_follow(self):
        u1 = User(username='phil', email='philcurtis.io') # Todo: need to change this??
        u2 = User(username='steph', email='steph@stephmn.com') # Todo: need to change this??
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.is_followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'phil')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'steph')

        u1.unfollow(u2)
        
        



        