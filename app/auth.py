from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("Email already exists, please log in.", category="error")

        if len(email) < 4:
            flash("Email must be greater than 4 characters", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters long", category="error")
        else:
            # creating a new user
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(
                    password1, method="pbkdf2", salt_length=16
                ),
            )
            db.session.add(new_user)
            db.session.commit()

            # login_user(new_user, remember=True)
            flash("Account created.", category="success")
            return redirect(url_for("views.home"))
        
    return render_template('sign_up.html')

