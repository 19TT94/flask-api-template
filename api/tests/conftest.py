import os
import tempfile

import pytest

from api import create_app
from api import db as _db

# Config Variables
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
host = os.environ.get("POSTGRES_HOST")
port = os.environ.get("POSTGRES_PORT")
name = os.environ.get("POSTGRES_DB")

@pytest.fixture(scope="session")
def app():
    """Create and configure a new app instance for each test."""
    _app = create_app()

    # Establish an application context before running the tests.
    ctx = _app.app_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope="function")
def client(app):
    """A test client for the app."""
    return app.test_client()
