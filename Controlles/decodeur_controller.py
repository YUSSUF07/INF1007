from flask import Blueprint, render_template, request, redirect, url_for
from app.models.decodeur import Decodeur
from app import db

decodeur_bp = Blueprint('decodeur', __name__, url_prefix='/decodeurs')

@decodeur_bp.route('/')
def liste_decodeurs():
    decodeurs = Decodeur.query.all()
    return render_template('decodeur/liste.html', decodeurs=decodeurs)

@decodeur_bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter_decodeur():
    if request.method == 'POST':
        model = request.form['model']
        etat = request.form['etat']
        client_id = request.form['client_id']

        decodeur = Decodeur(model=model, etat=etat, client_id=client_id)
        db.session.add(decodeur)
        db.session.commit()
        return redirect(url_for('decodeur.liste_decodeurs'))

    return render_template('decodeur/ajouter.html')
