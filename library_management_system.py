# Library Management System using Flask

from flask import Flask, request, jsonify
from typing import List, Dict, Optional
import secrets
import time

app = Flask(__name__)

books = []  
members = []  
sessions = {}  

book_id_counter = 1
member_id_counter = 1

def authenticate(token: Optional[str]) -> bool:
    if token in sessions:
        if sessions[token] > time.time():
            return True
        else:
            del sessions[token] 
    return False


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"error": "Username and password required"}), 400

    token = secrets.token_hex(16)
    sessions[token] = time.time() + 3600 
    return jsonify({"token": token})

@app.route('/books', methods=['POST'])
def create_book():
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    global book_id_counter
    data = request.json
    if not data or 'title' not in data or 'author' not in data:
        return jsonify({"error": "Title and author are required"}), 400

    book = {
        "id": book_id_counter,
        "title": data['title'],
        "author": data['author']
    }
    books.append(book)
    book_id_counter += 1
    return jsonify(book), 201

@app.route('/books', methods=['GET'])
def list_books():
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 10))

    filtered_books = books
    if title:
        filtered_books = [book for book in filtered_books if title.lower() in book['title'].lower()]
    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]

    start = (page - 1) * limit
    end = start + limit
    paginated_books = filtered_books[start:end]

    return jsonify(paginated_books)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    for book in books:
        if book['id'] == book_id:
            book.update({key: data[key] for key in ['title', 'author'] if key in data})
            return jsonify(book)

    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Deletes a book by ID."""
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    global books
    books = [book for book in books if book['id'] != book_id]
    return jsonify({"message": "Book deleted"})

@app.route('/members', methods=['POST'])
def create_member():
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    global member_id_counter
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400

    member = {
        "id": member_id_counter,
        "name": data['name']
    }
    members.append(member)
    member_id_counter += 1
    return jsonify(member), 201

@app.route('/members', methods=['GET'])
def list_members():
    token = request.headers.get('Authorization')
    if not authenticate(token):
        return jsonify({"error": "Unauthorized"}), 401

    return jsonify(members)

if __name__ == '__main__':
    app.run(debug=True)


