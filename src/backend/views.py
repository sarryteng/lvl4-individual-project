from flask import render_template, g

def home(lang):
    g.lang = lang
    return render_template('home.html')

# ------------------- LEARN SECTION: ------------------- 
def learn(lang):
    g.lang = lang
    return render_template('learn.html')

def mobile_security(lang):
    g.lang = lang
    return render_template('learn/mobile-security.html')

def encryption(lang):
    g.lang = lang
    return render_template('learn/encryption.html')

def password_security(lang):
    g.lang = lang
    return render_template('learn/password-security.html')

def two_factor_authentication(lang):
    g.lang = lang
    return render_template('learn/two-factor-authentication.html')

def phishing(lang):
    g.lang = lang
    return render_template('learn/phishing.html')

def software_updates(lang):
    g.lang = lang
    return render_template('learn/software-updates.html')

def identity_theft(lang):
    g.lang = lang
    return render_template('learn/identity-theft.html')

def malware(lang):
    g.lang = lang
    return render_template('learn/malware.html')

def vpn(lang):
    g.lang = lang
    return render_template('learn/vpn.html')


# ------------------- GUIDES SECTION: ------------------- 
def guides(lang):
    g.lang = lang
    return render_template('guides.html')

def secure_mobile(lang):
    g.lang = lang
    return render_template('guides/secure-mobile.html')

def use_encryption(lang):
    g.lang = lang
    return render_template('guides/use-encryption.html')

def secure_passwords(lang):
    g.lang = lang
    return render_template('guides/secure-passwords.html')

def use_two_factor(lang):
    g.lang = lang
    return render_template('guides/use-two-factor.html')

def spot_phishing(lang):
    g.lang = lang
    return render_template('guides/spot-phishing.html')

def how_to_update_software(lang):
    g.lang = lang
    return render_template('guides/how-to-update-software.html')

def prevent_theft(lang):
    g.lang = lang
    return render_template('guides/prevent-theft.html')

def malware_protection(lang):
    g.lang = lang
    return render_template('guides/malware-protection.html')

def use_vpn(lang):
    g.lang = lang
    return render_template('guides/use-vpn.html')


# ------------------- TOOLS SECTION: ------------------- 
def tools(lang):
    g.lang = lang
    return render_template('tools.html')
