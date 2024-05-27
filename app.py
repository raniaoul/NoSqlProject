from flask import Flask, render_template, request, jsonify
from routes.books import books_bp
from routes.adherents import adherents_bp
from routes.prets import prets_bp
from routes.auth import auth_bp

app = Flask(__name__)

# Enregistrer les Blueprints
app.register_blueprint(books_bp)
app.register_blueprint(adherents_bp)
app.register_blueprint(prets_bp)
app.register_blueprint(auth_bp)

# Route pour la page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour afficher les livres
@app.route('/books')
def books():
    return render_template('books.html')

# Route pour afficher les adhérents
@app.route('/adherents')
def adherents():
    return render_template('adherents.html')

# Route pour afficher les prêts
@app.route('/prets')
def prets():
    return render_template('prets.html')

# Route pour la page de connexion
@app.route('/login', methods=['GET'])
def login_page():

    return render_template('login.html')

# Traitement de la connexion
def authenticate_user(username, password):
    # Add your authentication logic here
    pass

@app.route('/login', methods=['POST'])
def login():
    data = request.form
    username = data['username']
    password = data['password']
    if authenticate_user(username, password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
