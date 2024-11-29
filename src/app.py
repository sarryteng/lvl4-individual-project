from flask import Flask
from backend.urls import register_routes

def create_app():
    app = Flask(__name__)

    # Register all routes
    register_routes(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
