from flask import render_template

def home():
    return render_template('home.html')

# ------------------- LEARN SECTION: ------------------- 
def learn():
    return render_template('learn.html')

def mobile_security():
    return render_template('learn/mobile-security.html')

def encryption():
    return render_template('learn/encryption.html')

def password_security():
    return render_template('learn/password-security.html')

def two_factor_authentication():
    return render_template('learn/two-factor-authentication.html')

def phishing():
    return render_template('learn/phishing.html')

def software_updates():
    return render_template('learn/software-updates.html')

def identity_theft():
    return render_template('learn/identity-theft.html')

def malware():
    return render_template('learn/malware.html')

def vpn():
    return render_template('learn/vpn.html')


# ------------------- GUIDES SECTION: ------------------- 
def guides():
    return render_template('guides.html')

def secure_mobile():
    return render_template('guides/secure-mobile.html')

def use_encryption():
    return render_template('guides/use-encryption.html')

def secure_passwords():
    return render_template('guides/secure-passwords.html')

def use_two_factor():
    return render_template('guides/use-two-factor.html')

def spot_phishing():
    return render_template('guides/spot-phishing.html')

def how_to_update_software():
    return render_template('guides/how-to-update-software.html')

def prevent_theft():
    return render_template('guides/prevent-theft.html')

def malware_protection():
    return render_template('guides/malware-protection.html')

def use_vpn():
    return render_template('guides/use-vpn.html')


# ------------------- TOOLS SECTION: ------------------- 
def tools():
    return render_template('tools.html')
