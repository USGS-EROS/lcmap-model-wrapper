"""CCDC Python-C interoperabilitiy module for index functions.
"""

import ctypes
import numpy as np

#
# C-library Wrapped
#

index = ctypes.CDLL("index.so")
ndvif = index.ndvi_float
ndvif.restype = ctypes.c_float;

def ndvi(nir, vis):
    nir = ctypes.c_float(nir)
    vis = ctypes.c_float(vis)
    return ndvif(nir, vis)

vndvi = np.vectorize(ndvi)

#
# Pure Python
#

def ndvi_py(nir, vis):
    return (nir-vis) / (nir+vis);

#
# Usage Example:
#

def example():
    vis = np.array(range(1,10))
    vis = vis.reshape((3,3))
    nir = np.ones((3,3))
    res = vndvi(vis,nir)
    print(res)
