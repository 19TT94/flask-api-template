import subprocess
import click

@click.command('test')
@click.argument('path', default='api/tests')
def run_tests(path):
    """
    Run a tests, default run all. Specify path for individual tests.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = 'py.test {0}'.format(path)
    return subprocess.call(cmd, shell=True)
