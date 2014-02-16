# -*- coding: utf-8 -*-

from flask import redirect, url_for
from flask.ext import login

from .. import app, db

from models import User


login_manager = login.LoginManager()
login_manager.init_app(app)

# Create user loader function


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)


@app.route('/logout/')
def logout():
    login.logout_user()
    return redirect(url_for('index'))
