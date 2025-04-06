from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models.utilisateur import Utilisateur

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method == 'POST':
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']

        user = Utilisateur.query.filter_by(email=email).first()
        if user and user.check_password(mot_de_passe):
            login_user(user)
            flash("Connexion réussie", "success")
            return redirect(url_for('home'))  # ou dashboard selon rôle
        flash("Identifiants invalides", "danger")

    return render_template('auth/connexion.html')

@auth_bp.route('/deconnexion')
@login_required
def deconnexion():
    logout_user()
    flash("Déconnecté avec succès", "info")
    return redirect(url_for('auth.connexion'))
from flask_login import login_required, current_user

@admin_bp.route('/secret')
@login_required
def secret_admin():
    if current_user.get_role() != 'admin':
        return "Accès refusé"
    return "Zone admin sécurisée"
