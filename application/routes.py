from flask import render_template, request, redirect
from application import app, db
from application.models import Users, Tasks
from application.forms import SignUpForm, LoginForm


# Landing page
@app.route('/')
def index():
    return render_template('index.html')


# Account sign up page
@app.route('/signup',  methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if request.method == 'POST':
        first_name = form.fname.data
        surname = form.sname.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        

        new_user = Users(first_name=first_name, surname=surname, username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')
    return render_template('signup.html', form=form)



# Account login page
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


# User dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
    




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

