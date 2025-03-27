from flask import Flask, request, g, redirect, url_for
from flask_babel import Babel
from backend.urls import register_routes

def create_app():
    app = Flask(__name__)

    # Set the default language and supported languages
    app.config['LANGUAGES'] = ['en', 'fr']
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'

    # Initialize Babel
    babel = Babel()

    # Function to determine the best language to use based on request
    def get_locale():
        lang = request.args.get('lang') or g.get('lang')  # Check query parameter or global context
        if lang and lang in app.config['LANGUAGES']:
            return lang
        return app.config['BABEL_DEFAULT_LOCALE']  # Default to 'en'

    # Redirect from root to the default language
    @app.route('/')
    def home_redirect():
        return redirect(url_for('home', lang=app.config['BABEL_DEFAULT_LOCALE']))

    # Register all routes
    register_routes(app)

    # Initialize Babel with the Flask app
    babel.init_app(app, locale_selector=get_locale)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5001, debug=True)
