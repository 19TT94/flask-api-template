import subprocess
import click

@click.command('cov')
@click.argument('path', default='api')
def get_test_coverage(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'py.test --cov-report term-missing --cov {0}'.format(path)
    return subprocess.call(cmd, shell=True)
