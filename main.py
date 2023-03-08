from datetime import datetime, date

from flask import Flask, render_template, redirect, url_for, flash, abort, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
#
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
#
import sqlite3
# import os
# import requests

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

db.create_all()
class MyModelView(ModelView):
    def is_accessible(self):



            return True


admin = Admin(app)
admin.add_view(MyModelView(User, db.session))


@app.route('/')
def start():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        number = request.form.get('phoneNumber')
        password = request.form.get('password')
        user = User.query.filter_by(phone=number).first()
        if not user:
            flash("That email does not exist, please try again.")
            return "redirect(url_for('login'))"
            # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return "f"
        # Email exists and password correct
        else:
            return "loged in "

    return render_template("login.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        if User.query.filter_by(phone=request.form.get('number')).first():
            # User already exists
            flash("You've already signed up with that number, log in instead!")
            return redirect(url_for('login'))

        hash_and_salted_password = generate_password_hash(
            request.form.get('password'),
            method='pbkdf2:sha256',
            salt_length=8
        )
        new_user = User(
            phone=request.form.get('number'),
            name=request.form.get('Username'),
            password=hash_and_salted_password

        )
        db.session.add(new_user)
        db.session.commit()
        return "done"

    return render_template("register0.html")


@app.route('/register/1', methods=["GET", "POST"])
def registerfirst():
    return render_template("register0.html")























if __name__ == "__main__":
    app.run(debug=True)
