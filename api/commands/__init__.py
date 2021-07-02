def initialize_commands(app) -> None:
    """Initialize Application Commands"""
    from api.commands.create_db import create_db
    from api.commands.db_seed import db_seed
    from api.commands.db_drop import db_drop
    from api.commands.test import run_tests
    from api.commands.cov import get_test_coverage
    from api.commands.generate_key import generate_key
    from api.commands.create_user import create_user

    app.cli.add_command(create_db)
    app.cli.add_command(db_seed)
    app.cli.add_command(db_drop)
    app.cli.add_command(run_tests)
    app.cli.add_command(get_test_coverage)
    app.cli.add_command(generate_key)
    app.cli.add_command(create_user)
