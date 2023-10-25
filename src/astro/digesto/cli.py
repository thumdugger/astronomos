import click
import re

from pathlib import Path


@click.group("digesto")
@click.pass_context
def digesto_cli(ctx: click.Context) -> None:
    """Organize astrophotography session image stacks."""
    obj = ctx.ensure_object(dict)


@digesto_cli.command("biases")
@click.option(
    "--image-type", "-T", "image_types", multiple=True, metavar="SUFFIX"
    , default = ("RAW", "NEF", "DNG", "CRW", "CR2", "RW2", "ARW")
    , help="Restrict digesting to images of form SEQUENCE*.SUFFIX (can be declared multiple times)")
@click.argument("sequence", metavar="SEQUENCE")
@click.pass_obj
def biases_cmd(obj: dict) -> None:
    """Process images as a biases substack."""
    print("digesto.darks_cmd()")


@digesto_cli.command("flats")
@click.pass_obj
def flats_cmd(obj) -> None:
    """Process images as a flats substack."""
    print("digesto.flats_cmd()")


@digesto_cli.command("darks")
@click.pass_obj
def darks_cmd(obj) -> None:
    """Process images as a darks substack."""
    print("digesto.darks_cmd()")


@digesto_cli.command("lights")
@click.pass_obj
def lights_cmd(obj) -> None:
    """Process images as a lights substack."""
    print("digesto.lights_cmd()")
