import click

from . import __version__


@click.command()
@click.version_option(version=__version__)
def main():
    """PowerSchool to G Suite Student Account Sync"""
    click.echo(f"Entry point for {__name__}")
