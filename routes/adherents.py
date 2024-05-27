from flask import Blueprint, request, jsonify
from models.mongo_models import add_adherent, get_all_adherents

adherents_bp = Blueprint('adherents', __name__)

@adherents_bp.route('/adherents', methods=['GET'])
def get_adherents():
    adherents = get_all_adherents()
    return jsonify(adherents)

@adherents_bp.route('/adherents', methods=['POST'])
def create_adherent():
    adherent_data = request.json
    add_adherent(adherent_data)
    return jsonify({"message": "Adherent added successfully"}), 201
