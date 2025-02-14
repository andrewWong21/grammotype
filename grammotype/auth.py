from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        if len(email) < 3:
            flash("Email must be at least 3 characters", category="error")
        elif len(firstName) < 2:
            flash("Name must be at least 2 characters", category="error")
        elif len(password1) < 2:
            flash("Password must be at least 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            flash("Account successfully created.", category="success")

    return render_template("register.html")
