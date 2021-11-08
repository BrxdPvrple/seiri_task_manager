from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
# from forms import RegistrationForm, LoginForm
from os import getenv

# Create an instance of Flask & connect to database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRETKEY'] = getenv
db = SQLAlchemy(app)
# class Employees(db.Model):
#     empNo = db.Column(db.Integer, primary_key = True)
#     Name = db.Column(db.CHAR(20))
#     Subject = db.Column(db.CHAR(20))
#     Marks = db.Column(db.Integer)
#     Department = db.Column(db.CHAR(30))
#     Salary = db.Column(db.Integer)





# class Users(db.Model):
#     User_ID = db.Column(db.Integer, AUTO_INCREMENT, primary_key = True)
#     Surname = db.Column(db.VARCHAR(255))
#     First_Name = db.Column(db.VARCHAR(255))
#     Username = db.Column(db.VARCHAR(255))
#     Email = db.Column(db.VARCHAR(255))


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






app.run(debug=True)