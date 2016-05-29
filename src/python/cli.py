import click
import json
import index
from lcmap.client


@click.group()
def cli():
    pass

@click.command()
@click.option('--point')
@click.option('--time')
def ndvi(point, time):
    result = {'point':point,'time':time}
    click.echo(json.dumps(result))
    return result


cli.add_command(ndvi)


if __name__ == '__main__':
    cli()
