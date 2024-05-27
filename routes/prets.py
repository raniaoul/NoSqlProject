from flask import Blueprint, request, jsonify
from models.mongo_models import add_pret, get_all_prets

prets_bp = Blueprint('prets', __name__)

@prets_bp.route('/prets', methods=['GET'])
def get_prets():
    prets = get_all_prets()
    return jsonify(prets)

@prets_bp.route('/prets', methods=['POST'])
def create_pret():
    pret_data = request.json
    add_pret(pret_data)
    return jsonify({"message": "Pret added successfully"}), 201
