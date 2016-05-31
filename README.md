# Science Model Wrapper

This is project wraps a shared object (implement in C) a Python wrapper.

It is arguably easier to handle IO using Python. Moreover, `lcmap-client-py` is a designed specifically for retrieving source data and saving model outputs using the LCMAP REST API.

## Example Usage

Create the docker image.

```
make docker
```

Execute a docker container.

```
docker run -t usgseros/lcmap-model-wrapper python3 index/cli.py ndvi \
  --x  "-1909498"   \
  --y  "2978512"    \
  --t1 "2013-01-01" \
  --t2 "2014-01-01" \
  --job-id TBD
```

This command can also be invoked by `lcmap-see`.
