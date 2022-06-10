import email
from flask import Flask, render_template, request, redirect
from flask_login import login_user, login_required, logout_user
from models import db, login, UserModel
from forms.login_form import loginForm, RegisterForm

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

def add_user(email, username, password):
    """
    Adds a user to the user database if not already present.
    Returns True if operation was successful, False otherwise.
    """
    # check if email exists
    user = UserModel.query.filter_by(email=email).first()
    if user is None:

        # create db entry and submit
        user = UserModel()
        user.set_password(password)
        user.email=email
        user.name = username
        db.session.add(user)
        db.session.commit()
        return True
    else: return False

@app.before_first_request
def create_table():
    db.create_all()
    user = UserModel.query.filter_by(email = "lhhung@uw.edu").first()
    if user is None:
        add_user("lhhung@uw.edu","qwerty")

@app.route("/")
@login_required
def display_home():
    return render_template("home.html")

@app.route("/")
def redirect_to_login():
    return redirect("/login")

@app.route("/login", methods=["GET","POST"])
def login():
    form=loginForm()
    if form.validate_on_submit():
        if request.method == "POST":
            email=request.form["email"]
            password=request.form["password"]
            user = UserModel.query.filter_by(email=email).first()
            if user is not None and user.check_password(password):
                login_user(user)
                return redirect("/home")
    return render_template("login.html",form=form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        username = request.form["username"]
        user = UserModel.query.filter_by(email=email).first()
        if user is None:
            add_user(email=email, username=username, password=password)
            return redirect('/login')
        elif user is not None and user.check_password(password):
            login_user(user)
            return redirect('/dashboard')
    return render_template("/user/register.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/login")

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)