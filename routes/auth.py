from flask import Blueprint, request, jsonify
from models.mongo_models import add_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    user_data = request.json
    add_user(user_data)
    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    if authenticate_user(data['username'], data['password']):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401
