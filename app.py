from flask import Flask, render_template, request, jsonify
from routes.books import books_bp
from routes.adherents import adherents_bp
from routes.prets import prets_bp
from routes.auth import auth_bp
from models.mongo_models import get_all_adherents, add_adherent, delete_all_adherents, add_pret


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

# Route pour afficher la page HTML des livres
@app.route('/books')
def books():
    return render_template('books.html')

# Route pour afficher les adhérents
@app.route('/adherents/html')
def adherents_page():
    return render_template('adherents.html')

# Route pour afficher les prêts
@app.route('/prets/html')
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

# Route pour obtenir tous les adhérents
@app.route('/adherents', methods=['GET'])
def get_adherents():
    adherents = get_all_adherents()
    return jsonify(adherents)

# Route pour ajouter un adhérent
@app.route('/adherents', methods=['POST'])
def create_adherent():
    adherent_data = request.json
    add_adherent(adherent_data)
    return jsonify({"message": "Adherent added successfully"}), 201

# Route pour supprimer tous les adhérents
@app.route('/adherents', methods=['DELETE'])
def delete_all_adherents_route():
    delete_count = delete_all_adherents()
    return jsonify({"deleted_count": delete_count})

# Route pour ajouter un prêt
@app.route('/prets', methods=['POST'])
def create_pret():
    pret_data = request.json
    add_pret(pret_data)
    return jsonify({"message": "Loan added successfully"}), 201

# Route pour afficher la page d'ajout de livre
@app.route('/addBook')
def add_book_page():
    return render_template('addBook.html')

@app.route('/api/books', methods=['POST'])
def add_book():
    book_data = request.json
    # Ajoutez ici le code pour enregistrer les données du livre dans la base de données
    # Exemple de code pour ajouter un livre à une base de données fictive
    new_book = {
        "title": book_data.get('title'),
        "author": book_data.get('author'),
        "isbn": book_data.get('isbn'),
        "image_url": book_data.get('image_url')
    }
    # Enregistrement du livre (exemple fictif)
    # books_collection.insert_one(new_book)
    return jsonify({"message": "Book added successfully"}), 201



if __name__ == '__main__':
    app.run(debug=True)
