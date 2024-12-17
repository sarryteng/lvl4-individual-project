from flask import Flask, request, g
from flask_babel import Babel, _
from backend.urls import register_routes

# Create the Flask app
def create_app():
    app = Flask(__name__)

    # Set the default language and supported languages
    app.config['LANGUAGES'] = ['en', 'fr', 'es']  # Add more languages as needed
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'  # Specify the translations folder

    # Initialize Babel
    babel = Babel()

    # Function to determine the best language to use based on request
    def get_locale():
        # Return the selected language from the 'lang' query parameter or use browser's language
        return request.args.get('lang') or request.accept_languages.best_match(['en', 'fr', 'es'])

    # Function to determine the best language to use based on request (for other uses)
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
    # Initialize Babel with the Flask app
    babel.init_app(app, locale_selector=get_locale)
    
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
