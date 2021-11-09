from application import db

# Users table class
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False) # User ID
    surname = db.Column(db.VARCHAR(255))
    first_name = db.Column(db.VARCHAR(255))
    username = db.Column(db.VARCHAR(255))
    email = db.Column(db.VARCHAR(255), nullable=False)
    password = db.Column(db.VARCHAR(255))

    tasks = db.relationship("Tasks", backref="user")

#Tasks table class
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False) # Task ID
    content = db.Column(db.VARCHAR(255)) # Task Content

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

db.drop_all()
db.create_all()