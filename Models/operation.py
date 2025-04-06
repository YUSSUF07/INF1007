from app import db
from datetime import datetime

class Operation(db.Model):
    __tablename__ = 'operation'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)  # exemple : "redémarrage"
    statut = db.Column(db.String(50), default="en attente")
    date = db.Column(db.DateTime, default=datetime.utcnow)
    decodeur_id = db.Column(db.Integer, db.ForeignKey('decodeur.id'))

    def executer(self):
        self.statut = "exécutée"

    def notifier_utilisateur(self):
        # Logique de notification simulée
        print(f"Notification envoyée pour l'opération {self.type}")

    def suivi_logs(self):
        return f"[{self.date}] - {self.type} - {self.statut}"
