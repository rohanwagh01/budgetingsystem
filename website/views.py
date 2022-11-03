#store routes for website and all views
#ewww front end, jk i like frontend sometimes

from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")
