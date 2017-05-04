import numpy as np
cimport numpy as np


cdef extern from "hello.hpp" namespace "example":
    void hello_world(int *buf, int size)


def world():
    cdef int[::1] v = np.arange(3, dtype=np.int32)
    hello_world(&v[0], v.size)
