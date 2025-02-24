import unittest
from flask_testing import TestCase
from app import create_app  

class TestApp(TestCase):
    def create_app(self):
        app = create_app()
        app.config.from_object('config.TestConfig')
        return app

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
    
    def test_secure_mobile_route(self):
        response = self.client.get('/en/guides/secure_mobile')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Mobile Security', response.data)

    def test_use_encryption_route(self):
        response = self.client.get('/en/guides/use_encryption')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Encryption', response.data)

    def test_secure_password_route(self):
        response = self.client.get('/en/guides/secure_passwords')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Secure Passwords', response.data)
    
    def test_use_2fa_route(self):
        response = self.client.get('/en/guides/use_two_factor')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Two Factor Authentication (2FA)', response.data)

    def test_spot_phishing_route(self):
        response = self.client.get('/en/guides/spot_phishing')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Phishing', response.data)

    def test_update_software_route(self):
        response = self.client.get('/en/guides/how_to_update_software')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Software Updates', response.data)
    
    def test_prevent_theft_route(self):
        response = self.client.get('/en/guides/prevent_theft')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Identity Theft', response.data)

    def test_malware_protection_route(self):
        response = self.client.get('/en/guides/malware_protection')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Malware', response.data)
    
    def test_use_vpn_route(self):
        response = self.client.get('/en/guides/use_vpn')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'VPN', response.data)

if __name__ == '__main__':
    unittest.main()