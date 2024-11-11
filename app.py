from functools import wraps
import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_session import Session
from cs50 import SQL

app = Flask(__name__)
app.secret_key = "your-secret-key-here"

# Configure session
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# create the sqlite database if the file does not exist
if not os.path.exists("database.db"):
    open("database.db", "w").close()

    # create the tables
    db = SQL("sqlite:///database.db")
    with open("database.sql", "r") as sql_file:
        db.execute(sql_file.read())
else:
    db = SQL("sqlite:///database.db")


def login_required(f):
    """
    Decorator to require login
    Redirects to the login page if the user is not logged in
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        user = None
        if True:  # TODO: check if the user is logged in
            flash("Please login first", "error")
            return redirect(url_for("login"))

        return f(user, *args, **kwargs)

    return decorated_function


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("not_implemented.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("not_implemented.html")


@app.route("/user/<int:user_id>")
@login_required
def user_profile(user, user_id):  # 'user' is the current logged-in user from @login_required
    return "Not implemented yet", 501


if __name__ == "__main__":
    app.run(debug=True)
