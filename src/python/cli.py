#
# This is the starting point of all CLI wrappers.
#

import click
import json
import index
from lcmap.client import Client

#
# A wrapper uses the LCMAP REST API Python Client to
# retrieve and persist model results.
#
client = Client()

@click.group()
def cli():
    pass

@click.command()
@click.option('--point')
@click.option('--time')
def echo(point, time):
    result = {'point':point,'time':time}
    click.echo(json.dumps(result))
    return result

cli.add_command(echo)

if __name__ == '__main__':
    cli()
