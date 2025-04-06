from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))  # "client" ou "admin"

    __mapper_args__ = {
        'polymorphic_on': role,
        'polymorphic_identity': 'utilisateur'
    }

    def authentifier(self):
        # Méthode générique
        return True

    def deconnecter(self):
        return "Utilisateur déconnecté."

    def get_role(self):
        return self.role

class Utilisateur(UserMixin, db.Model):
    __tablename__ = 'utilisateur'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe_hash = db.Column(db.String(128))
    role = db.Column(db.String(50))  # "client" ou "admin"

    __mapper_args__ = {
        'polymorphic_on': role,
        'polymorphic_identity': 'utilisateur'
    }

    def set_password(self, password):
        self.mot_de_passe_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.mot_de_passe_hash, password)

    def get_id(self):
        return str(self.id)

    def get_role(self):
        return self.role
