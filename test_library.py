import unittest
import json
from library_management_system import app  # Assuming the Flask app is in library_management_system.py

class LibraryManagementSystemTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_add_book(self):
        response = self.app.post('/books',
                                 data=json.dumps({
                                     "title": "Test Book",
                                     "author": "Test Author",
                                     "year_of_publication": 2024,
                                     "genre": "Fiction"
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Book', response.get_data(as_text=True))

    def test_get_books(self):
        self.app.post('/books',
                      data=json.dumps({
                          "title": "Test Book",
                          "author": "Test Author"
                      }),
                      content_type='application/json')

        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', response.get_data(as_text=True))

    def test_get_book_by_id(self):
        self.app.post('/books',
                      data=json.dumps({
                          "title": "Test Book",
                          "author": "Test Author"
                      }),
                      content_type='application/json')

        response = self.app.get('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', response.get_data(as_text=True))

    def test_update_book(self):
        self.app.post('/books',
                      data=json.dumps({
                          "title": "Test Book",
                          "author": "Test Author"
                      }),
                      content_type='application/json')

        response = self.app.put('/books/1',
                                 data=json.dumps({
                                     "title": "Updated Test Book"
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Test Book', response.get_data(as_text=True))

    def test_delete_book(self):
        # Add a book first
        self.app.post('/books',
                      data=json.dumps({
                          "title": "Test Book",
                          "author": "Test Author"
                      }),
                      content_type='application/json')

        response = self.app.delete('/books/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Book deleted successfully', response.get_data(as_text=True))

    def test_add_member(self):
        response = self.app.post('/members',
                                 data=json.dumps({
                                     "name": "Test Member",
                                     "email": "test@example.com"
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('Test Member', response.get_data(as_text=True))

    def test_get_members(self):
        # Add a member first
        self.app.post('/members',
                      data=json.dumps({
                          "name": "Test Member",
                          "email": "test@example.com"
                      }),
                      content_type='application/json')

        response = self.app.get('/members')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Member', response.get_data(as_text=True))

    def test_get_member_by_id(self):
        # Add a member first
        self.app.post('/members',
                      data=json.dumps({
                          "name": "Test Member",
                          "email": "test@example.com"
                      }),
                      content_type='application/json')

        response = self.app.get('/members/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Member', response.get_data(as_text=True))

    def test_update_member(self):
        # Add a member first
        self.app.post('/members',
                      data=json.dumps({
                          "name": "Test Member",
                          "email": "test@example.com"
                      }),
                      content_type='application/json')

        response = self.app.put('/members/1',
                                 data=json.dumps({
                                     "name": "Updated Member"
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Updated Member', response.get_data(as_text=True))

    def test_delete_member(self):
        # Add a member first
        self.app.post('/members',
                      data=json.dumps({
                          "name": "Test Member",
                          "email": "test@example.com"
                      }),
                      content_type='application/json')

        response = self.app.delete('/members/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Member deleted successfully', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
