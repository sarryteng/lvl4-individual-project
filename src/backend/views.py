from flask import render_template

def home():
    return render_template('home.html')

def learn():
    return render_template('learn.html')

def guides():
    return render_template('guides.html')

def tools():
    return render_template('tools.html')
