import click
import json
import numpy as np
from time import gmtime, strftime

from index import ndvi, vndvi
from lcmap.client import Client

# Example Usage:
#
# ```
# python index/cli.py ndvi
#         --x "-1909498" --y "2978512" \
#         --t1 "2013-01-01" --t2 "2014-01-01"
# ```
#

def load(x, y, t1, t2):
    c = Client()
    vis_ubid = "LANDSAT_8/OLI_TIRS/sr_band4"
    _, vis = c.data.tiles(vis_ubid, x, y, t1, t2)
    nir_ubid = "LANDSAT_8/OLI_TIRS/sr_band5"
    _, nir = c.data.tiles(nir_ubid, x, y, t1, t2)
    return vis, nir

def save(results):
    for result in results:
        pass


@click.group()
def cli():
    pass


@click.command()
@click.option('--x', required=True)
@click.option('--y', required=True)
@click.option('--t1', required=True)
@click.option('--t2', required=True)
@click.option('--job-id', required=True)
def ndvi(x, y, t1, t2, job_id):
    vs, ns = load(x, y, t1, t2)
    results = []
    for (nir, vis) in zip(ns, vs):
        data = np.array(vndvi(nir.data, vis.data))
        data = (data * 1000).astype(int)[0].tolist()
        results.append({
            'job_id': job_id,
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

    # The results are saved, not emitted to STDOUT.
    # click.echo(json.dumps(results, indent=2))
    save(results)

    # Details about the job execution are emitted to STDOUT.
    execution = {
        'model': 'lcmap.ndvi',
        'version': '0.5.0',
        'job-id': job_id,
        'completed': strftime("%Y-%m-%d %H:%M:%S", completed)
    }
    click.echo(json.dumps(execution, indent=2))


cli.add_command(ndvi)


if __name__ == '__main__':
    cli()
