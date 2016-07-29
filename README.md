# Science Model Wrapper

This is project wraps a shared object (implement in C) a Python wrapper.

It is arguably easier to handle IO using Python. Moreover, `lcmap-client-py` is a designed specifically for retrieving source data and saving model outputs using the LCMAP REST API.

## Examples

* Defining a C-library: `src/c/index.c`
* Wrapping a C-library using Python ctypes: `src/python/index/index.py`
* Calling a Python wrapped C-library using a Jupyter notebook: `src/python/index/index.ipynb`
* Supporting a command-line interface to a Python wrapped C-library: `src/python/index/cli.py`
* Building a docker image for a Python wrapped C-library: `docker/lcmap-model-wrapper/Dockerfile`

## Important Note

These examples assume that the LCMAP REST Python Client can connect to an instance of the LCMAP system. Without it, you will not be able to retrieve data.
