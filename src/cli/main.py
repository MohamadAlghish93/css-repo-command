import click

from .config import config, new, set, remove, show, notification, switch
from .dc import rebuild, dc
from .git import gi
from .run import run

@click.group()
def cli():
    """Main CLI entrypoint"""
    pass

""" config command """
cli.add_command(config)
cli.add_command(new)
cli.add_command(set)
cli.add_command(remove)
cli.add_command(show)
cli.add_command(notification)
cli.add_command(switch)

""" dc command """
cli.add_command(rebuild)
cli.add_command(dc)

""" git command """
cli.add_command(gi)

""" run command """
cli.add_command(run)
