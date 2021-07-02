import os, redis, logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_migrate import Migrate
from flask_cors import CORS
 
# Migrations
from api.database import db, migrate
from api.database import initialize_models

# API Routes
from api.router import initialize_routes

# Commands
from api.commands import initialize_commands

# Config Variables
secret_key = os.environ.get("SECRET_KEY")

user = os.environ.get("POSTGRES_USER")
pg_password = os.environ.get("POSTGRES_PASSWORD")
pg_host = os.environ.get("POSTGRES_HOST")
pg_port = os.environ.get("POSTGRES_PORT")
pg_name = os.environ.get("POSTGRES_DB")

session = os.environ.get("SESSION_TYPE")
redis_host = os.environ.get("REDIS_HOST")
redis_user = os.environ.get("REDIS_USER")
redis_password= os.environ.get("REDIS_PASSWORD")
redis_port = os.environ.get("REDIS_PORT")

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

    rdriver = redis.Redis(
        host=redis_host,
        port=redis_port,
        password=redis_password,
        db=0,
        ssl=ssl,
        ssl_cert_reqs=None
    )
    app.redis = rdriver

    # SQLAlchemy Config
    db_uri = "postgresql+psycopg2://{user}:{pw}@{host}:{port}/{db}".format(
        user=user,
        pw=pg_password,
        host=pg_host,
        port=pg_port,
        db=pg_name
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if settings_override:
        app.config.update(settings_override)

    engine = create_engine(db_uri)
    engine.connect()

    db.init_app(app)

    initialize_models(app)

    migrate.init_app(app, db, directory="api/database/migrations")

    # API Initialization
    initialize_routes(app)

    # Click Commands
    initialize_commands(app)

    return app
