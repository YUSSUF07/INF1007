from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def home():
    role = current_user.get_role()
    return render_template('home.html', user=current_user, role=role)
