from flask import Flask, request, g
from flask_babel import Babel
from backend.urls import register_routes

def create_app():
    app = Flask(__name__)

    # Set the default language and supported languages
    app.config['LANGUAGES'] = ['en', 'fr', 'es']  # Add more languages as needed
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language

    # Initialize Babel
    babel = Babel(app)

    # Function to determine the best language to use based on request
    @app.before_request
    def before_request():
        # Check the 'lang' query parameter or use the browser's preferred language
        lang = request.args.get('lang')
        if lang and lang in app.config['LANGUAGES']:
            g.lang = lang
        else:
            g.lang = request.accept_languages.best_match(app.config['LANGUAGES'])

    # Register all routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
