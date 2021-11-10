from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class SignUpForm(FlaskForm):
    fname = StringField("First Name", validators=[InputRequired(), Length(max=20)])
    sname = StringField("Surname", validators=[InputRequired(), Length(max=20)])
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    email = StringField("Email", validators=[InputRequired(), Length(max=50)])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must be identical'), Length(min=8, max=80)])
    confirm = PasswordField("Confirm Password", validators=[InputRequired(), Length(min=8, max=80)])
    submit = SubmitField("Submit")

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField("Password", validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember Me')


