from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def initialize_models(api) -> None:
    """Initialize Database Models"""
    from api.database.models.example import Example
