import os, logging
from flask import Flask
from flask_cors import CORS
 
# API Routes
from api.router import initialize_routes

# Commands
from api.commands import initialize_commands

# Config Variables
secret_key = os.environ.get("SECRET_KEY")

def create_app(settings_override=None) -> None:
    """Create and configure the app -> api"""
    app = Flask(__name__, instance_relative_config=True)

    app.config["SECRET_KEY"] = secret_key

    logging.basicConfig(format=f"%(asctime)s %(levelname)s %(name)s : %(message)s")

    CORS(
        app,
        origins=os.environ.get("CLIENT_APP"),
        supports_credentials=True
    )

    ssl = app.config["ENV"] != "development"

    if settings_override:
        app.config.update(settings_override)

    # API Initialization
    initialize_routes(app)

    # Click Commands
    initialize_commands(app)

    return app
