from .views import *

def register_routes(app):
    # Home page route
    app.add_url_rule('/<lang>/','home', home)

    # ------------------- LEARN SECTION: -------------------
    app.add_url_rule('/<lang>/learn', 'learn', learn)
    app.add_url_rule('/<lang>/learn/mobile_security', 'mobile_security', mobile_security)
    app.add_url_rule('/<lang>/learn/encryption', 'encryption', encryption)
    app.add_url_rule('/<lang>/learn/password_security', 'password_security', password_security)
    app.add_url_rule('/<lang>/learn/two_factor_authentication', 'two_factor_authentication', two_factor_authentication)
    app.add_url_rule('/<lang>/learn/phishing', 'phishing', phishing)
    app.add_url_rule('/<lang>/learn/software_updates', 'software_updates', software_updates)
    app.add_url_rule('/<lang>/learn/identity_theft', 'identity_theft', identity_theft)
    app.add_url_rule('/<lang>/learn/malware', 'malware', malware)
    app.add_url_rule('/<lang>/learn/vpn', 'vpn', vpn)

    # ------------------- LEARN/QUIZZES SECTION: -------------------
    app.add_url_rule('/<lang>/learn/mobile_security/quiz', 'mobile_security_quiz', mobile_security_quiz)
    app.add_url_rule('/<lang>/learn/encryption/quiz', 'encryption_quiz', encryption_quiz)
    app.add_url_rule('/<lang>/learn/password_security/quiz', 'password_security_quiz', password_security_quiz)
    app.add_url_rule('/<lang>/learn/two_factor_authentication/quiz', 'two_factor_authentication_quiz', two_factor_authentication_quiz)
    app.add_url_rule('/<lang>/learn/phishing/quiz', 'phishing_quiz', phishing_quiz)
    app.add_url_rule('/<lang>/learn/software_updates/quiz', 'software_updates_quiz', software_updates_quiz)
    app.add_url_rule('/<lang>/learn/identity_theft/quiz', 'identity_theft_quiz', identity_theft_quiz)
    app.add_url_rule('/<lang>/learn/malware/quiz', 'malware_quiz', malware_quiz)
    app.add_url_rule('/<lang>/learn/vpn/quiz', 'vpn_quiz', vpn_quiz)

    # ------------------- GUIDE SECTION: -------------------
    app.add_url_rule('/<lang>/guides', 'guides', guides)
    app.add_url_rule('/<lang>/guides/secure_mobile', 'secure_mobile', secure_mobile)
    app.add_url_rule('/<lang>/guides/use_encryption', 'use_encryption', use_encryption)
    app.add_url_rule('/<lang>/guides/secure_passwords', 'secure_passwords', secure_passwords)
    app.add_url_rule('/<lang>/guides/use_two_factor', 'use_two_factor', use_two_factor)
    app.add_url_rule('/<lang>/guides/spot_phishing', 'spot_phishing', spot_phishing)
    app.add_url_rule('/<lang>/guides/how_to_update_software', 'how_to_update_software', how_to_update_software)
    app.add_url_rule('/<lang>/guides/prevent_theft', 'prevent_theft', prevent_theft)
    app.add_url_rule('/<lang>/guides/malware_protection', 'malware_protection', malware_protection)
    app.add_url_rule('/<lang>/guides/use_vpn', 'use_vpn', use_vpn)

    # ------------------- TOOLS SECTION: -------------------
    app.add_url_rule('/<lang>/tools', 'tools', tools)
