from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm, LoginForm
from os import getenv

# Create an instance of Flask & connect to database
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRETKEY'] = getenv
db = SQLAlchemy(app)

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


# Landing page and sign up area
@app.route('/')
def homepage():
    return render_template('index.html')



@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name)

# Manage account details
@app.route('/manage_account')
def account():
    return render_template('account.html')




# Tasks overview and general user area




#Create a new task




# Edit tasks




# Delete tasks






app.run(debug=True, )