from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Narf(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    height = db.Column(db.String(10), nullable=False)
    color = db.Column(db.String(10), nullable=False)
    claws = db.Column(db.String(10), nullable=False)
    teeth = db.Column(db.String(10), nullable=False)
    fur = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    narfs = db.relationship("Narf")
    