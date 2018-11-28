'''
* pg 117
* Unit Testing the User Model
* Run with this command:
    * (venv) $ python tests.py
        * Note: server is running
'''
from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post

class UserModelCase(unittest.TestCase):
    '''
    setUp() and tearDown() methods are special methods that unit testing framework executes before & after each test, respectively
    setup() has a hack implementation preventing unit tests using the regular database # todo: where is this?
    '''
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://' # with sqlite, SQLAlchemy uses a RAM-only-database during testing
        db.create_all() # creates all the db tables & is quick way to create a db from scratch useful for testing

    def tearDown(self):
        db.session.remove() # pg 118
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='susan') # todo: change username??
        u.set_password('cat') # todo: change password
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
    
    def test_avatar(self):
        u = User(username='john', email='john@example.com') # Todo: need to change this??
        self.assertEqual(u.avatar(128), (
            'https://www.gravatar.com/avatar/'
            'd4c74594d841139328695756648b6bd6'
            '?d=identicon&s=128')) # Todo: need to change this??

    def test_follow(self):
        u1 = User(username='john', email='john@example.com') # Todo: need to change this??
        u2 = User(username='susan', email='susan@example.com') # Todo: need to change this??
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.is_followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'susan')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john') # pg 119

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)
        
    def test_follow_posts(self):
        # create 4 users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add([u1, u2, u3, u4])

        # create 4 posts
        now = datetime.utcnow()
        p1 = Post(body="post from john", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2, timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u4, timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup followers
        u1.follow(u2) # john follows susan # pg 120
        u1.follow(u4) # john follows david
        u2.follow(u3) # susan follows mary
        u3.follow(u4) # mary follows david
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])

        if __name__ == '__main__':
            unittest.main(verbosity=2)