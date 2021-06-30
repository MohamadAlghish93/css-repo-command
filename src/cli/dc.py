import contextlib
import os
import tempfile

import click
# import docker

from .utils import get_project
from ..config import DeployConfig, SSCIConf
from ..cookie import render
from ..runtime.utils import run_with_logs


@contextlib.contextmanager
def docker_compose(path:str=None):
    path = path or SSCIConf.COMPOSE_FILE
    if not os.path.exists(path):
        with open(path, 'w') as f:
            f.write(render(DeployConfig.load()))
    yield path

#
@click.command()
@click.argument('project', default='')
def rebuild(project):
    """Rebuild one or all projects"""
    if project == '':
        project = '*'
    else:
        get_project(project)
    click.echo(f"Triggering rebuild for projects {project}")
    with docker_compose() as path:
        name_image = "css"
        run_with_logs(f"docker-compose -f {path} exec {name_image} ash -c 'echo \"{project}\" > {SSCIConf.REBUILD_MARKER}'")

#
@click.group()
def dc():
    """Manipulate running projects"""
    pass


@dc.command()
def show():
    """Print current configuration in docker-compose format"""
    click.echo(render(DeployConfig.load()))


@dc.command()
def start():
    """Start ssci serving"""
    with docker_compose()as path:
        run_with_logs(f"docker-compose -f {path} up -d")


@dc.command()
def stop():
    """Stop ssci serving"""
    with docker_compose() as path:
        run_with_logs(f"docker-compose -f {path} stop")

@dc.command()
def restart():
    """Restart ssci serving"""
    with docker_compose() as path:
        run_with_logs(f"docker-compose -f {path} restart")

@dc.command()
@click.argument('command', default='ash')
def exec(command):
    """Exec command in ssci runtime (non-interactive)"""
    with docker_compose() as path:
        run_with_logs(f"docker-compose -f {path} exec ssci {command}")