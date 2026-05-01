"""Main CLI entry point for gh-profiler."""

import click

from . import gh_profiler


@click.command()
@click.argument("target")
def main(target):
    gh_profiler.main(target)
