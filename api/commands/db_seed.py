import click, os
from flask import current_app
from flask.cli import with_appcontext
from flask_migrate import upgrade
from alembic import command

from api import db

# Seeders
from api.database.seeders.seed import seed

@click.command()
@with_appcontext
@click.confirmation_option(prompt="\nAre you sure you want to seed the db? This action cannot be undone.")
@click.option(
    "--base",
    "-b",
    is_flag=True,
    default=False,
    help="Seed tables with data required by the client. This will override existing data and connot be undone."
)
@click.option(
    "--fake",
    "-f",
    is_flag=True,
    default=False,
    help="Seed fake data for testing. This will override existing data and connot be undone."
)
@click.option(
    "--model",
    "-m",
    help="Seed data for a specific Model."
)
def db_seed(base: bool=False, fake: bool=False, model: bool=False) -> None:
    """Seed the database."""
    
    # Reset DB
    if base or fake:
        db.engine.execute("TRUNCATE TABLE alembic_version RESTART IDENTITY CASCADE;")
        db.drop_all()
        upgrade(directory="api/database/migrations")

    click.echo("Running Seeders.\n")

    if base:
        seed("base")

    if fake:
        seed("fake")

    if model:
        response = seed("model", model)
        click.echo(response)

    click.echo("\nDatabase Seeded.\n")
        
