from app.models.utilisateur import Utilisateur
from app.models.decodeur import Decodeur
from app import db


class Client(Utilisateur):
    __tablename__ = 'client'
    id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), primary_key=True)
    adresse = db.Column(db.String(200))
    email = db.Column(db.String(100), unique=True, nullable=False)

    decodeurs = db.relationship('Decodeur', backref='client', lazy=True)

    __mapper_args__ = {
        'polymorphic_identity': 'client',
    }

    def ajouter_decodeur(self, decodeur):
        self.decodeurs.append(decodeur)

    def supprimer_decodeur(self, decodeur):
        self.decodeurs.remove(decodeur)

    def get_decodeurs(self):
        return self.decodeurs

    def authentifier(self):
        # Exemple simplifié
        return True
