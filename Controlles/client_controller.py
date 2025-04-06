from flask import Blueprint, render_template, request, redirect, url_for
from app.models.client import Client
from app import db

client_bp = Blueprint('client', __name__, url_prefix='/clients')

@client_bp.route('/')
def liste_clients():
    clients = Client.query.all()
    return render_template('client/liste.html', clients=clients)

@client_bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter_client():
    if request.method == 'POST':
        nom = request.form['nom']
        adresse = request.form['adresse']
        email = request.form['email']

        nouveau_client = Client(nom=nom, adresse=adresse, email=email, role="client")
        db.session.add(nouveau_client)
        db.session.commit()
        return redirect(url_for('client.liste_clients'))

    return render_template('client/ajouter.html')
