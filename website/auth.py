from flask import Blueprint, render_template, request, flash
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #post request is a login request
    data = request.form
    print(data)
    #get request needs the sign in page returned
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    #post request is a sign up request
    if request.method == 'POST':
        data = request.form
        print(data)
        email = data.get('email')
        firstName = data.get('firstName')
        lastName = data.get('lastName')
        password = data.get('password1')
        passwordConfirm = data.get('password2')
        #regex email matching
        p = re.compile(r'[\S]+@[\S]+.[\S]+')
        if not p.fullmatch(email):
            flash('Email is invalid', category="error")
        elif len(firstName) == 0:
            flash('First Name cannot be empty', category="error")
        elif len(lastName) == 0:
            flash('Last Name cannot be empty', category="error")
        elif password != passwordConfirm:
            flash('Passwords do not match', category="error")
        elif len(password) < 7:
            flash('Password is too short', category="error")
        else:
            flash('Success', category="pass") 
            #add user to db
    #get request needs the sign in page returned

    return render_template("sign_up.html")