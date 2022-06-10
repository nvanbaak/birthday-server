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

#####################################
#              Setup
#####################################

def addUser(email, password):
    """
    Adds a user to the user database if not already present.
    Returns True if operation was successful, False otherwise.
    """
    # check if email exists
    user = UserModel.query.filter_by(email).first()
    if user is None:

        # create db entry and submit
        user = UserModel()
        user.set_password(password)
        user.email=email
        db.session.add(user)
        db.session.commit()
        return True
    else: return False

@app.before_first_request
def create_table():
    db.create_all()
    user = UserModel.query.filter_by(email = "lhhung@uw.edu").first()
    if user is None:
        addUser("lhhung@uw.edu","qwerty")

