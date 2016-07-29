# Science Model Wrapper

This is project wraps a shared object (implement in C) a Python wrapper.

It is arguably easier to handle IO using Python. Moreover, `lcmap-client-py` is a designed specifically for retrieving source data and saving model outputs using the LCMAP REST API.

## Examples

* Defining a C-library: `src/c/index.c`
* Wrapping a C-library using Python ctypes: `src/python/index/index.py`
* Calling a Python wrapped C-library using a Jupyter notebook: `src/python/index/index.ipynb`
* Supporting a command-line interface to a Python wrapped C-library: `src/python/index/cli.py`
* Building a docker image for a Python wrapped C-library: `docker/lcmap-model-wrapper/Dockerfile`

## Using a Docker Container

These examples provide a way to build a docker image that wraps an example model. The container uses the LCMAP REST Python Client to retrieve data and store data, and as such, it requires a URL that can be resolved from the container.

It is important to update the `lcmap.client` section of *this project's* `config/lcmap.ini` file (used to build a docker image) to refer to the IP address of the REST API. This should match the IP address specfied in the `lcmap.rest` section of `~/.usgs/lcmap.ini` **localhost will not work**

After you update `config/lcmap.ini` you can use `make docker` to build the image expected by `lcmap-rest`.
