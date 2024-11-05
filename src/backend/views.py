from flask import render_template

def home():
    return render_template('home.html')

# ------------------- LEARN SECTION: ------------------- 
def learn():
    return render_template('learn.html')

def mobile_security():
    return render_template('learn/mobile_security.html')

def encryption():
    return render_template('learn/encryption.html')

def strong_passwords():
    return render_template('learn/strong_passwords.html')

def two_factor_authentication():
    return render_template('learn/two_factor_authentication.html')

def phishing():
    return render_template('learn/phishing.html')

def software_updates():
    return render_template('learn/software_updates.html')

def identity_theft():
    return render_template('learn/identity_theft.html')

def malware():
    return render_template('learn/malware.html')

def vpn():
    return render_template('learn/vpn.html')


# ------------------- GUIDES SECTION: ------------------- 
def guides():
    return render_template('guides.html')


# ------------------- TOOLS SECTION: ------------------- 
def tools():
    return render_template('tools.html')
