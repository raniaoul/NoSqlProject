from flask import Blueprint, request, jsonify, render_template
from models.mongo_models import add_pret, get_all_prets, delete_pret_by_id

prets_bp = Blueprint('prets', __name__)

# Route pour récupérer tous les prêts
@prets_bp.route('/prets', methods=['GET'])
def get_prets():
    prets = get_all_prets()
    return jsonify(prets)

# Route pour ajouter un nouveau prêt
@prets_bp.route('/prets', methods=['POST'])
def create_pret():
    pret_data = request.json
    add_pret(pret_data)
    return jsonify({"message": "Pret added successfully"}), 201

# Route pour supprimer un prêt par son identifiant
@prets_bp.route('/prets/<id>', methods=['DELETE'])
def delete_pret(id):
    deleted_count = delete_pret_by_id(id)
    if deleted_count:
        return jsonify({"message": "Pret deleted successfully"}), 200
    else:
        return jsonify({"message": "Pret not found"}), 404

# Route pour afficher les prêts sur une page HTML
@prets_bp.route('/prets/html', methods=['GET'])
def get_prets_html():
    prets = get_all_prets()
    return render_template('prets.html', prets=prets)
