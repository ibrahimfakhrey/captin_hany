from datetime import datetime, date

from flask import Flask, render_template, redirect, url_for, flash, abort, request
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
#
# from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
#
# import sqlite3
# import os
# import requests
# from quiz import PopQuiz
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)


@app.route('/')
def start():
    return render_template("login.html")


























if __name__ == "__main__":
    app.run(debug=True)
