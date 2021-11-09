from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SelectField, SubmitField

class AddEmp(FlaskForm):
    name = StringField("Name")
    salary = IntegerField("Salary")
    marks = IntegerField("Marks")
    subject = SelectField("Subject", choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript','Javascript'), ('C++', 'C++')])
    dept = SelectField('Department', choices=[('Front End', 'Front End'), ('Back End', 'Back End'), ('Devops', 'DevOps'), ('Lead Dev', 'Lead Dev')])
    submit = SubmitField('Add Employee')

class UpdateEmp(FlaskForm):
    name = StringField("Name")
    salary = IntegerField("Salary")
    marks = IntegerField("Marks")
    subject = SelectField("Subject", choices=[('Python', 'Python'), ('Java', 'Java'), ('Javascript','Javascript'), ('C++', 'C++')])
    dept = SelectField('Department', choices=[('Front End', 'Front End'), ('Back End', 'Back End'), ('Devops', 'DevOps'), ('Lead Dev', 'Lead Dev')])
    submit = SubmitField('Update Employee')
