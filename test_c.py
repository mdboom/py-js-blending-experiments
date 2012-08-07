#!/usr/bin/env python

import ctransform
import time

if __name__ == '__main__':
    t = time.time()
    val = ctransform.transform()
    print 'Time:', (time.time() - t) * 1000
    print 'Result:',  val
