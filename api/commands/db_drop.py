import click, os
from flask.cli import with_appcontext

from api import db

@click.command()
@with_appcontext
@click.confirmation_option(prompt="\nAre you sure you want to drop the db?\nThis action cannot be undone and all data will be lost.")
def db_drop() -> None:
    """Drop the database."""
    try:
        db.engine.execute("TRUNCATE TABLE alembic_version RESTART IDENTITY CASCADE;")
        db.drop_all()
    except Exception as e:
        click.echo("Error when trying to drop tables", e)

    click.echo("All tables dropped.")
