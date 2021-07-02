import os
import click

from sqlalchemy_utils import database_exists, create_database
from flask_migrate import upgrade

from api import create_app
from api.database import db

# Config Variables
user =  os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")
name = os.environ.get("POSTGRES_DB")

@click.command()
@click.option(
    "--test",
    "-t",
    is_flag=True,
    default=False,
    help="Create a test db."
)
def create_db(test: bool=False) -> None:
    """
    Create the database instance.

    :param test: Create a test database.
    :return: None
    """
    # SQLAlchemy Config
    db_uri = 'postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
        user=user,
        password=password,
        host=host,
        port=port,
        db=name
    )

    params = {}

    if test:
        click.echo("Configuring Test DB...")
        db_uri = '{0}_test'.format(db_uri)
        params["DEBUG"] = False
        params["TESTING"] = True

        if not database_exists(db_uri):
            click.echo("Database does not exist, initializing...")
            create_database(db_uri)
            click.echo("Database Created.\n")

    params["SQLALCHEMY_DATABASE_URI"] = db_uri

    _app = create_app(settings_override=params)

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    # Clear existing data
    db.drop_all()

    # Run migrations
    upgrade(directory="api/database/migrations")

    ctx.pop()
    click.echo("Database Initialization Complete")
