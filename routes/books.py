from flask import Blueprint, request, jsonify
from models.mongo_models import add_book, get_all_books
from models.neo4j_models import sync_book_to_neo4j

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET'])
def get_books():
    books = get_all_books()
    return jsonify(books)

@books_bp.route('/books', methods=['POST'])
def create_book():
    book_data = request.json
    add_book(book_data)
    sync_book_to_neo4j(book_data)
    return jsonify({"message": "Book added successfully"}), 201
