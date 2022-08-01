from signal import SIGKILL
from subprocess import CompletedProcess
from turtle import title
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """a user"""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(20), nullable = False)
    lname = db.Column(db.String(20), nullable = False)
    email = db.Column(db.String(50), nullable = False, unique=True)
    password = db.Column(db.String(20), nullable = False)


class Pattern(db.Model):
    """a pattern"""

    __tablename__ = 'patterns'

    pattern_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable = False, unique=True)
    skill = db.Column(db.String(20), nullable = False)
    type = db.Column(db.String(20), nullable = False)
    pattern = db.Column(db.Text, nullabe=False)

    
