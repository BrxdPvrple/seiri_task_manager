from flask import render_template, request, redirect
from application import app, db
# from application.forms import 
from application.models import Users, Tasks


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
@app.route('/task_overview')
def show_tasks():
    pass




#Create a new task
@app.route('/task_input')
def new_task():
    pass



# Edit tasks
@app.route('/task_update')
def edit_task():
    pass


# Delete tasks
@app.route('/task_delete')
def delete_task():
    pass

