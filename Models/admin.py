from app.models.utilisateur import Utilisateur
from app import db

class Administrateur(Utilisateur):
    __tablename__ = 'administrateur'

    id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def gerer_clients(self):
        return "Gestion des clients"

    def ajouter_utilisateur(self):
        return "Nouvel utilisateur ajouté"

    def surveiller_activite(self):
        return "Surveillance en cours"
