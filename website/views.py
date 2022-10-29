#store routes for website and all views
#ewww front end, jk i like frontend sometimes

from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test<h1>"
