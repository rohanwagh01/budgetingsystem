#setup flask application
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy
DB_NAME = "database.db"

def create_app():
    '''
    Create a flask application
    '''
    app = Flask(__name__)
    #secure cookies and session data, aware that this is a goofy way to store this
    app.config['SECRET_KEY'] = 'T[;4eT%}!E:gl1X'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app

