from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
#@login_required
def home():
    if not current_user.is_authenticated:
        flash("Log in to save your results.", category='info')
    return render_template("home.html", user=current_user)