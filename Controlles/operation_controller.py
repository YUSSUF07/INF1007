from flask import Blueprint, render_template, request, redirect, url_for
from app.models.operation import Operation
from app import db

operation_bp = Blueprint('operation', __name__, url_prefix='/operations')

@operation_bp.route('/')
def liste_operations():
    operations = Operation.query.all()
    return render_template('operation/liste.html', operations=operations)

@operation_bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter_operation():
    if request.method == 'POST':
        type_op = request.form['type']
        statut = request.form['statut']
        decodeur_id = request.form['decodeur_id']

        op = Operation(type=type_op, statut=statut, decodeur_id=decodeur_id)
        db.session.add(op)
        db.session.commit()
        return redirect(url_for('operation.liste_operations'))

    return render_template('operation/ajouter.html')
