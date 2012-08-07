#!/usr/bin/env python

import transform_numpy
import time

if __name__ == '__main__':
    t = time.time()
    val = transform_numpy.transform()
    print 'Time:', (time.time() - t) * 1000
    print 'Result:',  val
