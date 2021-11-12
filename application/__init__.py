from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from os import getenv
import pymysql

# Create an instance of Flask
app = Flask(__name__)

# Instantiate Bootstrap
Bootstrap(app)

#Initialize database
app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DB_URI")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db' # Temporary database for offline testing
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secretkey')
db = SQLAlchemy(app)


import application.models
import application.forms
import application.routes