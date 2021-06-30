import click
from ..config import DeployConfig
from ..runtime.main import main


@click.command()
def run():
    """Run ssci runtime (not in container)"""
    main(DeployConfig.load())
