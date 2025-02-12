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
        if len(email) == 0:
            flash("Email cannot be empty", category="error")
        elif len(firstName) == 0:
            flash("Name cannot be empty", category="error")
        elif len(password1) == 0:
            flash("Password cannot be empty", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        else:
            flash("Account successfully created.", category="success")

    return render_template("register.html")