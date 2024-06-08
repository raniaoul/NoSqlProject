from flask import Blueprint, request, jsonify, render_template
from models.mongo_models import add_user, authenticate_user

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_data = request.json if request.is_json else request.form.to_dict()
        add_user(user_data)
        return jsonify({"message": "User registered successfully"}), 201
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.json if request.is_json else request.form.to_dict()
        if authenticate_user(data['username'], data['password']):
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401
    return render_template('login.html')
