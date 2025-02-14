from . import db
from flask_login import UserMixin

class Result(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.DateTime(timezone=True), default = func.now())
    accuracy = db.Column(db.Float)
    speed = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
