from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('home.html', user=current_user)

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)


@main.route('/groups')
@login_required
def groups():
    return render_template('groups.html', user=current_user)


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=current_user)