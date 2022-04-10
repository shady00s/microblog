from datetime import datetime
from encodings import utf_8
from hashlib import md5
from flask_login import LoginManager, UserMixin
from sqlalchemy import PrimaryKeyConstraint
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(64))
    posts = db.relationship('Post',backref='author',lazy='dynamic' )
    last_seen = db.Column(db.DateTime,default = datetime.utcnow)
    about_me = db.Column(db.String(140))
    # to create password hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # to check if the password hash is correct

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    #to create avatar using email 
    def avatar(self , size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest,size)

# method used to point to objects in class
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(120))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

    # to initalize table in sqlAlchemy
    # flask db init

    # to migrate the class objects into sql code
    # flask migrate -m "name of the table "

    # to update the db with the new schema
    # flask upgrade
