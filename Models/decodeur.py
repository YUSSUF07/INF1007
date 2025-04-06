from app import db
from datetime import datetime

class Decodeur(db.Model):
    __tablename__ = 'decodeur'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    etat = db.Column(db.String(50), default="éteint")
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))

    operations = db.relationship('Operation', backref='decodeur', lazy=True)

    def redemarrer(self):
        self.etat = "redémarré"

    def eteindre(self):
        self.etat = "éteint"

    def reinitialiser(self):
        self.etat = "réinitialisé"

    def get_etat(self):
        return self.etat

    def suivi_temps_reel(self):
        # Simulé : on renverrait des données en temps réel ici
        return f"État actuel : {self.etat} à {datetime.now()}"
