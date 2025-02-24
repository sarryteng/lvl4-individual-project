import unittest
from flask import g
from flask_testing import TestCase
from app import create_app  

class TestApp(TestCase):
    def create_app(self):
        app = create_app()
        app.config.from_object('config.TestConfig')
        return app

    # test - accessing the root URL (/) redirects to the home page with the default language 'en'
    def test_home_redirect(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)
        self.assertIn('/en/', response.location)

    # test - language is correctly set
    def test_language_setting(self):
        with self.client as client:
            response = client.get('/en/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(g.lang, 'en')

            response = client.get('/fr/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(g.lang, 'fr')

if __name__ == '__main__':
    unittest.main()