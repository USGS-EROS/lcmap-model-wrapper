import click
import json
import index
import numpy as np
from lcmap.client import Client

# Example Usage:
#
# ```
# python index/cli.py ndvi
#         --x "-1909498" --y "2978512" \
#         --t1 "2013-01-01" --t2 "2014-01-01"
# ```
#

def fetch(x, y, t1, t2):
    c = Client()
    vis_ubid = "LANDSAT_8/OLI_TIRS/sr_band4"
    _, vis = c.data.tiles(vis_ubid, x, y, t1, t2)
    nir_ubid = "LANDSAT_8/OLI_TIRS/sr_band5"
    _, nir = c.data.tiles(nir_ubid, x, y, t1, t2)
    return vis, nir


@click.group()
def cli():
    pass


@click.command()
@click.option('--x')
@click.option('--y')
@click.option('--t1')
@click.option('--t2')
def ndvi(x, y, t1, t2):
    vs, ns = fetch(x, y, t1, t2)
    results = []
    for (nir, vis) in zip(ns, vs):
        data = np.array(index.vndvi(nir.data, vis.data))
        data = (data * 1000).astype(int)[0].tolist()
        results.append({
            'data': data,
            'source': {
                'nir_x': nir.x,
                'nir_y': nir.y,
                'nir_ubid': nir.ubid,
                'nir_acquired': nir.acquired,
                'vis_x': vis.x,
                'vis_y': vis.y,
                'vis_ubid': vis.ubid,
                'vis_acquired': vis.acquired
            }
        })

    click.echo(json.dumps(results, indent=2))
    return results


cli.add_command(ndvi)


if __name__ == '__main__':
    cli()
