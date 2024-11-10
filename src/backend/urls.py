from .views import *

def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/learn', 'learn', learn)
    app.add_url_rule('/learn/mobile_security', 'mobile_security', mobile_security)
    app.add_url_rule('/learn/encryption', 'encryption', encryption)
    app.add_url_rule('/learn/password_security', 'password_security', password_security)
    app.add_url_rule('/learn/two_factor_authentication', 'two_factor_authentication', two_factor_authentication)
    app.add_url_rule('/learn/phishing', 'phishing', phishing)
    app.add_url_rule('/learn/software_updates', 'software_updates', software_updates)
    app.add_url_rule('/learn/identity_theft', 'identity_theft', identity_theft)
    app.add_url_rule('/learn/malware', 'malware', malware)
    app.add_url_rule('/learn/vpn', 'vpn', vpn)
    app.add_url_rule('/guides', 'guides', guides)
    app.add_url_rule('/tools', 'tools', tools)
