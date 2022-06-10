from flask import Flask, render_template, request, redirect
from flask_login import current_user, login_user, login_required, logout_user
from models import db, login, UserModel
from forms import loginForm

#####################################
#    Flask boilerplate from demo
#####################################

app = Flask(__name__)
app.secret_key="a secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/login.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login.init_app(app)