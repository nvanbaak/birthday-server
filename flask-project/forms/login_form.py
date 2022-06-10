from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class loginForm(FlaskForm):
    email=StringField(label="Enter email", validators=[DataRequired(),Email()])
    password=PasswordField(label="Enter password",validators=[DataRequired(), Length(min=6,max=20)])
    submit=SubmitField(label="Login")

class RegisterForm(FlaskForm):
    username = StringField(label="Enter username", validators=[DataRequired(), Length(min=6, max=20)])
    password=PasswordField(label="Enter password",validators=[DataRequired(), Length(min=8,max=20)])
    confirm_password = PasswordField(label="Confirm password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(label="Register")