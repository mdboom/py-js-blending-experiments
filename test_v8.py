#!/usr/bin/env python

import PyV8
import time

with open("transform.js", "rb") as fd:
    js_code = fd.read()

with PyV8.JSContext() as ctx:
    ctx.eval(js_code)
    t = time.time()
    result = ctx.eval("transform()")
    t = time.time() - t
    print "Time: %f ms" % (t * 1000.0)
    print "Result:", result
