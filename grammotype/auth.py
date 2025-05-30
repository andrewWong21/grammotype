from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, current_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Successfully logged in", category='success')
                login_user(user, remember=True)
                redirect(url_for('views.home'))
            else:
                flash("Incorrect username or password.", category='error')
        else:
            flash("Incorrect username or password.", category='error')
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already in use.", category="error")
        elif len(email) < 3:
            flash("Email must be at least 3 characters", category="error")
        elif len(first_name) < 2:
            flash("Name must be at least 2 characters", category="error")
        elif len(password1) < 2:
            flash("Password must be at least 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account successfully created.", category="success")
            return redirect(url_for('views.home'))

    return render_template("register.html", user=current_user)
