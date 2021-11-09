from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField


class SignUp(FlaskForm):
    fname = StringField("First Name")
    sname = StringField("Surname")
    username = StringField("Username")
    email = StringField("Email")
    password = StringField("Password")

class Login(FlaskForm):
    username = StringField("Username")
    password = StringField("Password")

# class AddEmp(FlaskForm):
#     name = StringField("Name")
#     salary = IntegerField("Salary")
#     marks = IntegerField("Marks")
#     subject = SelectField("Subject", choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript','Javascript'), ('C++', 'C++')])
#     dept = SelectField('Department', choices=[('Front End', 'Front End'), ('Back End', 'Back End'), ('Devops', 'DevOps'), ('Lead Dev', 'Lead Dev')])
#     submit = SubmitField('Add Employee')

# class UpdateEmp(FlaskForm):
#     name = StringField("Name")
#     salary = IntegerField("Salary")
#     marks = IntegerField("Marks")
#     subject = SelectField("Subject", choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript','Javascript'), ('C++', 'C++')])
#     dept = SelectField('Department', choices=[('Front End', 'Front End'), ('Back End', 'Back End'), ('Devops', 'DevOps'), ('Lead Dev', 'Lead Dev')])
#     submit = SubmitField('Update Employee')
