from flask import Blueprint, render_template, request, redirect, url_for
from Models.admin import Administrateur
from app import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/')
def dashboard_admin():
    admins = Administrateur.query.all()
    return render_template('admin/liste.html', admins=admins)

@admin_bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter_admin():
    if request.method == 'POST':
        nom = request.form['nom']
        admin = Administrateur(nom=nom, role="admin")
        db.session.add(admin)
        db.session.commit()
        return redirect(url_for('admin.dashboard_admin'))
    return render_template('admin/ajouter.html')
