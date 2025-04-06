# controllers/auth_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from Models.user import User, UserRepository

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserRepository.find_by_username(username)
        if user and user.verify_password(password):
            session['username'] = user.username
            return redirect(url_for('decoder.dashboard'))
        return render_template('login.html', error="Nom d'utilisateur ou mot de passe incorrect")
    return render_template('login.html')
