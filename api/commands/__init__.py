def initialize_commands(app) -> None:
    """Initialize Application Commands"""
    from api.commands.test import run_tests
    from api.commands.cov import get_test_coverage
    from api.commands.generate_key import generate_key

    app.cli.add_command(run_tests)
    app.cli.add_command(get_test_coverage)
    app.cli.add_command(generate_key)
