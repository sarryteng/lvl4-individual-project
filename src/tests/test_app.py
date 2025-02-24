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

    # test - 'learn' and 'learn' sub-routes are accessible
    def test_learn_route(self):
        response = self.client.get('/en/learn')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Learn about Cybersecurity Concepts', response.data)

    def test_mobile_security_route(self):
        response = self.client.get('/en/learn/mobile_security')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mobile Security', response.data)

    def test_encryption_route(self):
        response = self.client.get('/en/learn/encryption')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Encryption', response.data)

    def test_password_security_route(self):
        response = self.client.get('/en/learn/password_security')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Password Security', response.data)

    def test_two_factor_authentication_route(self):
        response = self.client.get('/en/learn/two_factor_authentication')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Two Factor Authentication (2FA)', response.data)

    def test_phishing_route(self):
        response = self.client.get('/en/learn/phishing')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Phishing', response.data)

    def test_software_updates_route(self):
        response = self.client.get('/en/learn/software_updates')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Software Updates', response.data)

    def test_identity_theft_route(self):
        response = self.client.get('/en/learn/identity_theft')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Identity Theft', response.data)

    def test_malware_route(self):
        response = self.client.get('/en/learn/malware')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Malware', response.data)

    def test_vpn_route(self):
        response = self.client.get('/en/learn/vpn')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'VPN', response.data)

    # test - 'guides' and 'guides' sub-routes are accessible
    def test_guides_route(self):
        response = self.client.get('/en/guides')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Guides', response.data)
    
        

if __name__ == '__main__':
    unittest.main()