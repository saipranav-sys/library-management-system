import unittest
from library_management_system import app

class TestLibraryManagementSystem(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Welcome to the Library Management System API!", response.data)

if __name__ == '__main__':
    unittest.main()
