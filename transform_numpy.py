import numpy as np

def transform():
    size = 128000

    a = 2.0
    b = 0.5
    c = 0.1
    d = 0.5
    e = 2.0
    f = 0.1

    data = np.empty((size, 2))
    i = np.arange(128000)

    data[:,0] = a*i + c*i + e
    data[:,1] = b*i + d*i + f

    s = np.sum(data[:,0])

    return s
