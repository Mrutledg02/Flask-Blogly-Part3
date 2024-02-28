import unittest
from app import app, db
from models import User, Post, Tag

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        """Tear down test environment."""
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_homepage(self):
        """Test homepage route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recent Posts", response.data)

    def test_add_user(self):
        """Test adding a new user."""
        response = self.app.post('/users/new', data=dict(
            first_name="John",
            last_name="Doe",
            image_url="https://example.com/johndoe.jpg"
        ), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"John Doe", response.data)

    # Add more test cases for other critical routes...

if __name__ == '__main__':
    unittest.main()
