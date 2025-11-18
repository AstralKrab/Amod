import requests as rq
import py7zr as pyZ
import zipfile as zip
import json
import struct
import click

@click.command(name= "AMod")
def setup():
    ApiKey = click.prompt('please enter your nexus api key')
    click.echo(f"your api key is:[{ApiKey}]")

if __name__ == "__main__":
    click.