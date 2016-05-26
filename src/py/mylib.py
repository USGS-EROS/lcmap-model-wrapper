"""CCDC Python-C interoperabilitiy module for mylib.so functions.
"""

import ctypes
import numpy as np

#
# C-library Wrapped
#

mylib = ctypes.CDLL("mylib.so")

def add(rs, gs, bs, ms, ts):

    length = len(rs)
    to_int_array = len(rs) * ctypes.c_int
    to_long_array = len(rs) * ctypes.c_long
    to_short_array = len(rs) * ctypes.c_uint8

    # create c-compatible arrays for each band
    ra = to_int_array(*rs)
    ga = to_int_array(*gs)
    ba = to_int_array(*bs)
    result = to_int_array(*ts)
    mylib.add(ra, ga, ba, length, result)

    return list(result)
