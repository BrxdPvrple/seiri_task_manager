from application import db
from flask_login import UserMixin

# Users table class
class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False) # User ID
    first_name = db.Column(db.VARCHAR(20))
    surname = db.Column(db.VARCHAR(20))
    username = db.Column(db.VARCHAR(15), unique=True)
    email = db.Column(db.VARCHAR(50), nullable=False, unique=True)
    password = db.Column(db.VARCHAR(255))

    tasks = db.relationship("Tasks", backref="user")

#Tasks table class
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False) # Task ID
    content = db.Column(db.VARCHAR(255)) # Task Content

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

# db.drop_all()
db.create_all()