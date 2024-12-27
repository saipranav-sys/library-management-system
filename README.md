# Library Management System

This project is a simple Flask-based Library Management System API that allows CRUD operations for books and members. Additionally, it includes search functionality for books, pagination, and token-based authentication.

## How to Run the Project

1. Clone this repository or download the code:
   ```bash
   git clone https://github.com/your-repo-link
   cd library-management-system
   ```
2. Set up a virtual environment and install Flask:

   ```bash
   Copy code
   python3 -m venv venv
   source venv/bin/activate
   pip install flask
   ```

3. Run the Flask application:

```bash
Copy code
python library_management_system.py
Access the API via http://127.0.0.1:5000/ in your browser or API testing tools (e.g., Postman).
```

4. API Endpoints
   Books:

POST /books: Add a new book.
GET /books: Get a list of books.
PUT /books/<id>: Update a book by its ID.
DELETE /books/<id>: Delete a book by its ID.

Members:

POST /members: Add a new member.
GET /members: Get a list of members.
PUT /members/<id>: Update a member by its ID.
DELETE /members/<id>: Delete a member by its ID.

# Architecture:

Built using Flask, leveraging Python's built-in functionality without external dependencies.
Separation of concerns for books and members with distinct routes and logic.

# Authentication:

Implemented token-based authentication to secure API endpoints, ensuring only authorized users can perform actions.

# Pagination:

Manual pagination was implemented to handle large datasets efficiently without using third-party libraries.

# Search:

Basic substring matching for searching books by title or author.
Assumptions and Limitations

# Assumptions:

Each book and member has a unique ID.
All requests must include valid JSON data in the body.
No persistent database is used; data exists in memory for simplicity.

# Limitations:

Data resets every time the server restarts.
Token-based authentication is implemented manually, which may not be as robust as standard libraries.
Limited error handling for edge cases due to the constraint of using zero third-party libraries.
Future Improvements

# Persistent Storage:

Integrate a database (e.g., SQLite, PostgreSQL) for long-term data storage.

# Enhanced Security:

Replace manual token-based authentication with Flask-JWT or similar standard libraries.
Advanced Pagination:

Add configurable page sizes and advanced navigation options.
Improved Error Handling:

Provide detailed error messages for invalid inputs and server issues.

# User Interface:

Build a frontend interface for user-friendly interactions with the API.
Testing

# Framework:

The application includes automated tests using Python's built-in unittest framework.

# How to Run Tests:

Run the test script:

```bash
Copy code
python test_library_management_system.py
Ensure all test cases pass successfully before deployment.
```
