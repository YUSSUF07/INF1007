from Controlles.client_controller import client_bp

def register_routes(app):
    app.register_blueprint(client_bp)
from Controlles.decodeur_controller import decodeur_bp

def register_routes(app):
    app.register_blueprint(decodeur_bp)
    app.register_blueprint(client_bp)  # s'assurer que les deux soient inclus
from Controlles.operation_controller import operation_bp

def register_routes(app):
    app.register_blueprint(client_bp)
    app.register_blueprint(decodeur_bp)
    app.register_blueprint(operation_bp)
from Controlles.admin_controller import admin_bp

def register_routes(app):
    app.register_blueprint(client_bp)
    app.register_blueprint(decodeur_bp)
    app.register_blueprint(operation_bp)
    app.register_blueprint(admin_bp)
from Controlles.auth_controller import auth_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(decodeur_bp)
    app.register_blueprint(operation_bp)
    app.register_blueprint(admin_bp)
from Controlles.main_controller import main_bp

def register_routes(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(client_bp)
    app.register_blueprint(decodeur_bp)
    app.register_blueprint(operation_bp)
    app.register_blueprint(admin_bp)
