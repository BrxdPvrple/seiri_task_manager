from flask import render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from application import app, db
from application.models import Users, Tasks
from application.forms import SignUpForm, LoginForm


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


# Manage logins
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))




# Landing page
@app.route('/')
def index():
    return render_template('index.html')




# Account sign up page
@app.route('/signup',  methods=["GET", "POST"])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Users(first_name=form.fname.data, surname=form.sname.data, username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return render_template('login.html', form=form)

        # data = Users.query.all()
        # return render_template('TESTING.html', record=data) #Temporary solution to view user table in browser

    return render_template('signup.html', form=form)



# Account login page
@app.route('/login',  methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        return '<h1>Invalid Username or Password</h1>'

    return render_template('login.html', form=form)



# User dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')




# Logout current user
@app.route('/logout')
@login_required
def logout():
    return render_template('index.html')
    


# Manage account details
@app.route('/manage_account')
def account():
    return render_template('account.html')




# Tasks overview and general user area
@app.route('/task_overview')
def show_tasks():
    return render_template('task_manager.html')




#Create a new task
@app.route('/task_input')
def new_task():
    return render_template('new_task.html')



# Edit tasks
@app.route('/task_update')
def edit_task():
    return render_template('edit_task.html')


# Delete tasks
@app.route('/task_delete')
def delete_task():
    pass