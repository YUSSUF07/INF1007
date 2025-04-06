from flask import Flask
from Models import db
from routes import register_routes
from flask_login import LoginManager
from Models.utilisateur import Utilisateur
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mon_projet.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "secret"

    db.init_app(app)

    with app.app_context():
        db.create_all()

    register_routes(app)
    return app

login_manager = LoginManager()
login_manager.login_view = 'auth.connexion'

def create_app():
    app = Flask(__name__)
    # ...
    login_manager.init_app(app)
    return app

@login_manager.user_loader
def load_user(user_id):
    return Utilisateur.query.get(int(user_id))
