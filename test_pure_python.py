#!/usr/bin/env python

import transform
import time

if __name__ == '__main__':
    t = time.time()
    val = transform.transform()
    print 'Time:', (time.time() - t) * 1000
    print 'Result:',  val
