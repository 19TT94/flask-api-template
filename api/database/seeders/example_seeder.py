import os, uuid, click
from werkzeug.security import generate_password_hash

from api import db
from api.database.models.example import Example

def example() -> None:
    examples = [
        { "text": "test1" },
        { "text": "test2" },
        { "text": "test3" }
    ]
    click.echo("  Seeding User Types...")
    with click.progressbar(examples) as bar:
        for example_params in bar:
            example = Example(**example_params)
            db.session.add(example)
            db.session.commit()
