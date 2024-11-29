from .views import *

def register_routes(app):
    app.add_url_rule('/', 'home', home)

    # ------------------- LEARN SECTION: ------------------- 
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

    # ------------------- GUIDE SECTION: ------------------- 
    app.add_url_rule('/guides', 'guides', guides)
    app.add_url_rule('/guides/secure_mobile', 'secure_mobile', secure_mobile)
    app.add_url_rule('/guides/use_encryption', 'use_encryption', use_encryption)
    app.add_url_rule('/guides/secure_passwords', 'secure_passwords', secure_passwords)
    app.add_url_rule('/guides/use_two_factor', 'use_two_factor', use_two_factor)
    app.add_url_rule('/guides/spot_phishing', 'spot_phishing', spot_phishing)
    app.add_url_rule('/guides/how_to_update_software', 'how_to_update_software', how_to_update_software)
    app.add_url_rule('/guides/prevent_theft', 'prevent_theft', prevent_theft)
    app.add_url_rule('/guides/malware_protection', 'malware_protection', malware_protection)
    app.add_url_rule('/guides/use_vpn', 'use_vpn', use_vpn)

    # ------------------- TOOLS SECTION: ------------------- 
    app.add_url_rule('/tools', 'tools', tools)
