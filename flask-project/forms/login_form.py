from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email, NumberRange


class loginForm(FlaskForm):
    email=StringField(label="Enter email", validators=[DataRequired(),Email()])
    password=PasswordField(label="Enter password",validators=[DataRequired(), Length(min=6,max=20)])
    submit=SubmitField(label="Login")

class RegisterForm(FlaskForm):
    username = StringField(label="Enter username", validators=[DataRequired(), Length(min=6, max=20)])
    email=StringField(label="Enter email", validators=[DataRequired(),Email()])
    password=PasswordField(label="Enter password",validators=[DataRequired(), Length(min=8,max=20)])
    confirm_password = PasswordField(label="Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Register")

class BirthDateForm(FlaskForm):
    birthday = DateField(label="Enter birthday", validators=[DataRequired()])
    num_results = IntegerField(label="Number of results", validators=[DataRequired(), NumberRange(min=1, max=20)])
    submit = SubmitField(label="Search")