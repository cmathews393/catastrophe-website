from flask import Flask
from flask_bootstrap import Bootstrap5
from .routes import main_blueprint


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    Bootstrap5(app)

    app.register_blueprint(main_blueprint)

    return app
