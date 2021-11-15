from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from os import getenv
from flask_wtf.csrf import CSRFProtect
import pymysql

# Create an instance of Flask
app = Flask(__name__)

# Instantiate Bootstrap
Bootstrap(app)

csrf = CSRFProtect(app)

#Initialize database
# app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')
db = SQLAlchemy(app)


import application.models
import application.forms
import application.routes