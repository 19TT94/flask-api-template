import os
import binascii
import click

@click.command("generate_key")
def generate_key():
    """
    Generate Secret Key for API access.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    key = binascii.hexlify(os.urandom(24))
    click.echo("\nGenerated SECRET_KEY: \n{0}".format(key.decode("UTF-8")))
