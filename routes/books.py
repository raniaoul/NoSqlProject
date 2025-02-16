from flask import Blueprint, request, jsonify
from models.mongo_models import add_book, get_all_books, delete_all_books
from models.neo4j_models import sync_book_to_neo4j
from bson import ObjectId  # Add this import

books_bp = Blueprint('books', __name__)
def serialize_book(book):
    """Convert MongoDB book document to JSON-serializable format."""
    serialized_book = {}
    
    if "title" in book:
        serialized_book["title"] = book["title"]
    if "author" in book:
        serialized_book["author"] = book["author"]
    if "isbn" in book:
        serialized_book["isbn"] = book["isbn"]
    if "image_url" in book:
        serialized_book["image_url"] = book["image_url"]

    if "_id" in book:
        serialized_book["id"] = str(book["_id"])  # Convert ObjectId to string

    return serialized_book


# This route returns JSON data
@books_bp.route('/api/books', methods=['GET'])
def get_books():
    books = get_all_books()
    serialized_books = [serialize_book(book) for book in books]
    return jsonify(serialized_books)

# This route adds a new book
@books_bp.route('/api/books', methods=['POST'])
def create_book():
    book_data = request.json
    inserted_id = add_book(book_data)  # Get the inserted ObjectId
    book_data["_id"] = str(inserted_id)  # Convert ObjectId to string
    sync_book_to_neo4j(book_data)  # Sync book to Neo4j
    return jsonify({"message": "Book added successfully"}), 201


# This route deletes all books
@books_bp.route('/api/books', methods=['DELETE'])
def delete_books():
    deleted_count = delete_all_books()
    return jsonify({"message": f"Deleted {deleted_count} books"}), 200

