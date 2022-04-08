from datetime import datetime
from flask_login import LoginManager, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(64))
    # to create password hash

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    # to check if the password hash is correct

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# method used to point to objects in class
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Integer, primary_key=True)
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
