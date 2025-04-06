<<<<<<< HEAD
from flask import Blueprint, render_template, request, redirect, url_for
from Models.decodeur import Decodeur
from database import db

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
=======
# controllers/decoder_controller.py
from flask import Blueprint, render_template, request, redirect, url_for, session
from Models.decoder import DecoderRepository
from Models.channel import ChannelRepository

decoder_bp = Blueprint('decoder', __name__, url_prefix='/decoder')

@decoder_bp.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    decoders = DecoderRepository.get_all()
    return render_template('dashboard.html', decoders=decoders)

@decoder_bp.route('/<int:decoder_id>/add_channel', methods=['GET', 'POST'])
def add_channel(decoder_id):
    if 'username' not in session:
        return redirect(url_for('auth.login'))
    decoder = DecoderRepository.find_by_id(decoder_id)
    channels = ChannelRepository.get_all()
    if request.method == 'POST':
        channel_id = int(request.form['channel_id'])
        channel = ChannelRepository.find_by_id(channel_id)
        decoder.add_channel(channel)
        return redirect(url_for('decoder.dashboard'))
    return render_template('add_channel.html', decoder=decoder, channels=channels)
>>>>>>> f6def81 (dashbord)
