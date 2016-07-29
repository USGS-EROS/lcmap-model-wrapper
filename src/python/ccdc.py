"""CCDC Python-C interoperabilitiy module.
"""

import ctypes
ccdc = ctypes.CDLL("ccdc.so")


class Result(ctypes.Structure):

    _fields_ = [("start", ctypes.c_int),
                ("stop", ctypes.c_int),
                ("c1", ctypes.c_int),
                ("c2", ctypes.c_int),
                ("c3", ctypes.c_int)]


def initialize(rs, gs, bs, ms, ts):
    """Invoke CCDC-like initialization.

    Transforms Python inputs into ctypes and lib output ctypes
    into Python types.
    """

    # create ctype arrays for inputs to init call
    length = len(rs)
    to_int_array = len(rs) * ctypes.c_int
    to_long_array = len(rs) * ctypes.c_long
    to_short_array = len(rs) * ctypes.c_uint8

    # create c-compatible arrays for each band
    ra = to_int_array(*rs)
    ga = to_int_array(*gs)
    ba = to_int_array(*bs)
    ta = to_long_array(*ts)
    ma = to_short_array(*ms)

    # the number of results isn't known ahead of time...
    count = ctypes.pointer(ctypes.c_int(0))

    # an instance of Result required when making pointers...
    results = ctypes.pointer(ctypes.pointer(Result()))
    ccdc.init(ra, ga, ba, ta, ma, count, results)

    # We use the result count to cast the result reference...
    count_val = count.contents.value

    # Result class is used when casting, but I don't know why...
    results_cast = ctypes.cast(results, ctypes.POINTER(ctypes.POINTER(Result*count_val)))

    # It'd be a pain for the caller to have to work with ctypes...
    return [to_dict(r) for r in results_cast.contents.contents]


def to_dict(r):
    """Transform result struct into dict.
    """
    return dict((f, getattr(r, f)) for f, _ in r._fields_)
