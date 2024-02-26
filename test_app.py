import unittest
from app import app

class BasicTests(unittest.TestCase):
    # udføres før hver test
    def setUp(self):
        # opretter en testklient
        app.testing = True
        self.app = app.test_client()

    # Test for at se, om root ('/') ruten returnerer 'Hello, World!'
    def test_main_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == "__main__":
    unittest.main()
